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
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        
        // TreeNode res = preorder(root,subRoot);
        // //System.out.println(res.val);
        // return sameTree(res, subRoot);
        if (subRoot==null) return true;
        if (root==null && subRoot!=null) return false;
        if (sameTree(root, subRoot)) return true;
        return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
        
        
    }
    
    public boolean sameTree(TreeNode node1, TreeNode node2) {
        if (node1==null && node2==null) return true;
        else if (node1==null || node2==null) return false;
        else if (node1.val!=node2.val) return false;
        return sameTree(node1.left, node2.left) && sameTree(node1.right, node2.right);
        
    }
    
    public TreeNode preorder(TreeNode root, TreeNode subnode) {
        
        Stack<TreeNode> stack = new Stack<>();
       
        
        stack.push(root); 
        while (!stack.isEmpty()) {
            TreeNode node =stack.pop();
            if (node.val==subnode.val) return node;
            if (node.left!=null) stack.push(node.left);
