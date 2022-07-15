class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        out=[]
        p=1
        for i in range(len(nums)):  #왼쪽으로부터 시작된 누적곱 구하기 
            out.append(p)     #i-1까지의 누적곱을 left에 저장
            p=p*nums[i]     #누적곱 
            
        #왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈.
        
        p=1
        
        for  i in range(len(nums)-1,-1,-1): 
            out[i]=out[i]*p   #나를 제외한 왼쪽요소들의 곱(우변out[i])와 오른쪽 요소들의 곱 p를 곱해 답을 구한다
            p=p*nums[i]         #다음 루프때의 i를 기준으로 오른쪽 값들의 값을 p에 저장해놓는다.

        return out
