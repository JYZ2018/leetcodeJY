/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        if (preorder==null || preorder.length==0 ) return null;
        int index=0;
        
        TreeNode root = new TreeNode (preorder[0]);
        
        int j=0;
        for (int i=0; i<inorder.length; i++) {
            if (inorder[i]==preorder[0]) {
                j=i;
                break;
            }
        }
         index++; 
        int[] preorder2 = Arrays.copyOfRange(preorder, index, j+1);
        int[] inorder2 = Arrays.copyOfRange(inorder, 0, j);
        
        
        root.left = buildTree(preorder2, inorder2);
        
        
        
        int[] preorder1 = Arrays.copyOfRange(preorder, j+1, preorder.length);
        int[] inorder1 = Arrays.copyOfRange(inorder, j+1, inorder.length);
        
        
        root.right = buildTree(preorder1, inorder1);
        
        return root;
     
         
        
    }
 
}
