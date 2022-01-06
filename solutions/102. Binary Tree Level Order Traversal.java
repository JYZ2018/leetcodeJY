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
       
        Queue <TreeNode> q= new LinkedList<>();
        List<List<Integer>> res =new ArrayList<>();
        q.add(root);
        
        if (root==null) {return res;}
        
        while (!q.isEmpty() ) {
            List<Integer> vals = new ArrayList<Integer>();
            int n=q.size();
            for (int i=0; i<n;i++)  {
                TreeNode node=q.poll();
                
                vals.add(node.val);
                //System.out.println(vals);
                if (node.left!=null) {q.add(node.left);}
                if (node.right!=null) {q.add(node.right);}
            } 
            res.add(vals);
        }
       return res; 
    }
}
