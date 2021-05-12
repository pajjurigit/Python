vowels = "aeiouAEIOU"
class Solution:
    def halvesAreAlike(self, inputStr:str) -> bool:
        length = len(inputStr)
        if length < 2 or length > 1000:
            print('string too short or too long')
            return False
        
        if length % 2 != 0:
            print('string length must be even')
            return False
        vowCnta = self.numVows(inputStr, 0, int(length/2)-1)
        vowCntb = self.numVows(inputStr, int(length/2), length-1)
        
        if vowCnta == vowCntb:
           return True
        else:
            return False
        
    def numVows(self, string:str, startIndex:int, endIndex:int) -> int:
        cnt = startIndex
        string = string.lower()
        vowCnt = 0;
        while cnt <= endIndex:
            if string[cnt] =='a' or string[cnt]=='e' or string[cnt]=='i' or string[cnt]=='o' or string[cnt]=='u':
                vowCnt = vowCnt + 1
            cnt = cnt+1
        return vowCnt;
    
    
#Another solution, with easy tricks...
# lacks boundary conditions
    def halvesAreAlike1(self, S: str) -> bool:
        mid, ans = len(S) // 2, 0
        for i in range(mid):
            if S[i] in vowels: ans += 1
            if S[mid+i] in vowels: ans -=1
        return ans == 0
    

some = Solution()
print(some.halvesAreAlike1('book12'))
print(some.halvesAreAlike1('abcdef'))
print(some.halvesAreAlike1('Abc1Def2'))
