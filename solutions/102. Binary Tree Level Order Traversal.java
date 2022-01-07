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
    public List<List<Integer>> levelOrder(TreeNode root) {
        
        //dfs
        
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        levelHelper(res, root, 0);
        return res;
    }
    
    public void levelHelper(List<List<Integer>> res, TreeNode root, int height) {
        if (root == null) return;
        if (height >= res.size()) {
            res.add(new LinkedList<Integer>());
        }
        res.get(height).add(root.val);
        System.out.println(res);
        levelHelper(res, root.left, height+1);
        levelHelper(res, root.right, height+1);}
    
    
       
        /*
        Queue <TreeNode> q= new LinkedList<>();
        List<List<Integer>> res =new ArrayList<>();
        q.add(root);
        
        if (root==null) {return res;}
        
        while (!q.isEmpty() ) {
            List<Integer> vals = new ArrayList<Integer>();
            int n=q.size();
            for (int i=0; i<n;i++)  {
