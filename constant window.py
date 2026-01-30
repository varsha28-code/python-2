# constant window example 

arr = list(map(int,input().split()))
k = int(input())
left = 0
right = k-1 
Sum = sum(arr[0:k])
maxSum = Sum 
n = len(arr)
while(right<n-1):
    Sum-=arr[left]
    left+=1 
    right+=1 
    Sum+=arr[right]
    maxSum = max(maxSum,Sum)
print(maxSum) 

# max card points 

class Solution:
    def maxScore(self, cardPoints, k):
        # code here.
        n = len(cardPoints)
        left = 0
        right = k-1 
        Sum = sum(cardPoints[0:k]) 
        maxSum = Sum 
        j = n-1    
        for _ in range(k):
            Sum-=cardPoints[right]
            right-=1 
            Sum+=cardPoints[j]
            j-=1 
            maxSum = max(maxSum,Sum)
        return maxSum
