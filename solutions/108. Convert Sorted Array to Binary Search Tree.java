//             mid=l+(r-l)/2;
//             TreeNode left = new TreeNode(nums[mid]);
//             root.left=left;
//             root=root.left;
//         }
        
//         while (r<nums.length) {
//             l=mid+1;
//             r=nums.length;
//             TreeNode right = new TreeNode()
            
        
//         }
//         Stack<Integer> leftIndex = new Stack<>();
//         Stack<Integer> rightIndex = new Stack<>();
//         leftIndex.push(0);
//         rightIndex.push(nums.length-1);
        
//         while (!leftIndex.isEmpty()) {
//             left=leftIndex.pop
            
//         }
        
        // bfs
        TreeNode root = new TreeNode();
        
        Stack<TreeNode> nodeStack = new Stack<>();
        Stack<Integer> leftStack = new Stack<>();
        Stack<Integer> rightStack = new Stack<>();
        leftStack.push(0);
        rightStack.push(nums.length-1);
        nodeStack.push(root);
        
        while (!nodeStack.isEmpty()) {
            TreeNode node = nodeStack.pop();
            int left = leftStack.pop();
            int right= rightStack.pop();
           
            int mid = left+(right-left)/2;
            node.val=nums[mid];
          
            //while (left>0) {
            if (left<=mid-1) {
                
                node.left = new TreeNode();
                nodeStack.push(node.left);
                leftStack.push(left);
                rightStack.push(mid-1);
            }
            
            //while (left<nums.length-1) {
            if (mid+1<=right) {
                node.right = new TreeNode();
                nodeStack.push(node.right);
