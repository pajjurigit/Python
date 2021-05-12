
import re 

ccList = []
n = int(input())
for _ in range(n):
    ccList.append(str(input()))

def isValidCC(nbr):
    ret = False
    #regProg = re.compile("^(?!.*(\d)(-?\1){3})[456]\d{3}(?:-?\d{4}){3}$")
    regProg = re.compile(
            r"^"
            r"(?!.*(\d)(-?\1){3})"
            r"[456]"
            r"\d{3}"
            r"(?:-?\d{4}){3}"
            r"$")
    if regProg.search(nbr):
        ret = True
    if ret:
        return 'Valid' 
    else:
        return 'Invalid'

resList = list(map(isValidCC, ccList))

print("\n".join (resList))