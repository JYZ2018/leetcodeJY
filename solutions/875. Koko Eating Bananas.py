class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # binary search
        low,high=1,max(piles)
        start=int((low+high)/2)
        hour=0
        
        while low<high: #(mistake 1, this conditon I didn't make it right)
            hour=0
            start=int((low+high)/2)
            #print("start is: ",start)
            for i in piles:
                rem=i%start
                   
                if rem==0:
                    hour+=int(i/start)
                else:
                    hour+=(int(i/start)+1)
            #print(hour)
            if hour<=h: #(mistake 2, remember it is hour<=h)
                high=start  # (mistake 3,here it is very tricky, high is not start+1)             
            if hour>h:
                low=start+1
            #print("low and high is: ",low, high)
            
        #print(low,high,hour)
                
        return high ####(mistake 4, return is high, not start)
            
        
        
        
        
        
        
        
        # brute force, count from 1, time limit exceeded
        start=1
        hour=0
        while hour==0 or hour>h:
            hour=0
            for i in piles:
                rem=i%start
