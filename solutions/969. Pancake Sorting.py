class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        
        
        res=[]
        for i in range(len(arr)-1,-1,-1):
            max_i=arr.index(max(arr[0:i+1]))
            arr[0:max_i+1]=arr[0:max_i+1][::-1]
            #print(arr)
            res.append(max_i+1)
            arr[0:i+1]=arr[0:i+1][::-1]
            #print(arr)
            res.append(i+1)
        return res
            
        '''
        res=[]
        for i in range(len(arr)-1,-1,-1):
            max_i=arr.index(max(arr[0:i+1]))
            arr=arr[0:max_i+1][::-1]+arr[max_i+1:]
            print(arr)
            res.append(max_i+1)
            arr=arr[0:i+1][::-1]+arr[i+1:]
            print(arr)
            res.append(i+1)
        return res
        '''   
        
