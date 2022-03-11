class Solution:
    def trap(self, height: List[int]) -> int:
        res=0
        left_max,right_max=[height[0]]*len(height),[height[-1]]*len(height)
        
        for i in range(1,len(height)):
            left_max[i]=max(height[i],left_max[i-1])
       
        for i in range(len(height)-2,-1,-1):
            right_max[i]=max(height[i],right_max[i+1])
        for i in range(1,len(height)-1):
            res+=min(left_max[i],right_max[i])-height[i]
        return res
        
        
        
        
        
        
        
        
        # my own answer, not so correct
        '''
        l,r=0,len(height)-1
        area=0
        print(l,r)
        while l<r:
            print("0: ",l,r)
            
            
            if l<r and height[l]>=height[l+1]:
               
                left=l
                tall=height[left]
                while l<r and height[l]>=height[l+1]:
                    l+=1
                    #print("0: ",l,r,height[l],height[l+1])
                if l<r and height[l] <height[l+1]:
                    while l<r and height[l]<height[l+1]:
                        print("0.5: ",l,r)
                        l+=1
                    right=l
                    print("1: ",l,r)
