        
        // bfs
//         TreeNode root = new TreeNode();
        
//         Stack<TreeNode> nodeStack = new Stack<>();
//         Stack<Integer> leftStack = new Stack<>();
//         Stack<Integer> rightStack = new Stack<>();
//         leftStack.push(0);
//         rightStack.push(nums.length-1);
//         nodeStack.push(root);
        
//         while (!nodeStack.isEmpty()) {
//             TreeNode node = nodeStack.pop();
//             int left = leftStack.pop();
//             int right= rightStack.pop();
           
//             int mid = left+(right-left)/2;
//             node.val=nums[mid];
          
//             //while (left>0) {
//             if (left<=mid-1) {
                
//                 node.left = new TreeNode();
//                 nodeStack.push(node.left);
//                 leftStack.push(left);
//                 rightStack.push(mid-1);
//             }
            
//             //while (left<nums.length-1) {
//             if (mid+1<=right) {
//                 node.right = new TreeNode();
//                 nodeStack.push(node.right);
//                 leftStack.push(mid+1);
//                 rightStack.push(right);
//             }
//         }
            
//           return root;  
        
        
        // dfs
        int left=0, right= nums.length-1;
        
        TreeNode root = dfs(nums,left,right);
        return root;
       
        }
    
  
 public TreeNode dfs(int[]nums, int left, int right) {
       
      int mid = left+(right-left)/2;
     
      TreeNode res = new TreeNode(nums[mid]);
      if (left<= mid-1) {
         res.left=dfs(nums, left, mid-1); 
      }
      if (mid+1<=right) {
         res.right=dfs(nums, mid+1,right); 
      } 
    return res;
  }     
      
}
