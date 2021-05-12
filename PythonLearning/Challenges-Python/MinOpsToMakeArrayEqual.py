"""
Challenge:-
----    
You have an array arr of length n where arr[i] = (2 * i) + 1 for all valid values of i (i.e. 0 <= i < n).
In one operation, you can select two indices x and y where 0 <= x, y < n and subtract 1 from arr[x] and add 1 to arr[y]
     (i.e. perform arr[x] -=1 and arr[y] += 1). The goal is to make all the elements of the array equal. 
     It is guaranteed that all the elements of the array can be made equal using some operations.
Given an integer n, the length of the array. Return the minimum number of operations needed to make all the elements 
    of arr equal.
    
    Ex:1
    Input: n = 3
    Output: 2
    Explanation: arr = [1, 3, 5]
    First operation choose x = 2 and y = 0, this leads arr to be [2, 3, 4]
    In the second operation choose x = 2 and y = 0 again, thus arr = [3, 3, 3].
    
    Ex:2
    Input: n = 6
    Output: 9
"""

class Solution:
    def minOperations(self, n:int) -> int:
        arr = [(i*2)+1 for i in range(0,n)]
        numToEq = sum(arr)//n
        midElementIndex = n//2
        
        sumToReturn = 0;
        for i in range(0,midElementIndex):
            sumToReturn = sumToReturn + (numToEq-arr[i])
        
        return sumToReturn;
    
    
    # With min Runtime (16ms)
    def minOperationsWithPow(self, n: int) -> int:
        return pow(n,2)//4 #or (n**2)//4
                
       
    
#Another solution, with easy tricks...
# lacks boundary conditions

    

some = Solution()
print(some.minOperations(4))
print(some.minOperations(5))
print(some.minOperations(6))

# allOdds = [x for x in range(0,6) if x%2!=0]
# print(allOdds)
# arr = [(x*2)+1 for x  in range(0,6) ]
# print (arr)
# 5//2
# 6//2

int((5-1.) * (5+1.) / 4.)