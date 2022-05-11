class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        if len(mat)*len(mat[0])!=r*c:
            return mat
        
        res=[[0 for _ in range(c)] for _ in range(r)]
        
        for i in range(len(mat)*len(mat[0])):
            res[i//c][i%c] = mat[i//len(mat[0])][i%len(mat[0])]
        return res
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if len(mat)*len(mat[0])!=r*c:
#             return mat
        
#         temp=[]
#         res=[]
#         for i in range(len(mat)):
#             for j in range(len(mat[0])):
#                 temp.append(mat[i][j])
         
#         index=0
#         for m in range(r):
#             temp_m=[]
#             for n in range(c):
#                 temp_m.append(temp[index])
#                 index+=1
#             res.append(temp_m)
#         return res
                
