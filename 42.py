class Solution:
    def trap(self, height:List[int])->int:
        stack=[]
        volume=0

        for i in range(len(height)):
            #if present bar is higher than before
            while stack and height[i]>height[stack[-1]]:
                top=stack.pop()     #직전의 낮은 높이를 꺼낸다

                if not len(stack):
                    #if stack is empty, end statement 'while'
                    break

                distance=i-stack[-1]-1
                #find minimum height from present bar and former bars
                waters=min(height[i],height[stack[-1]])-height[top]

                volume+=distance*waters

                
            stack.append(i)
        return volume
