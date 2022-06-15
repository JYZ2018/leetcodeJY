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
    public boolean isSameTree(TreeNode p, TreeNode q) {
        // wrong for [1,2] [1,null,2] - corrected
        
//         List<Integer> plist = preorder(p);
//         List<Integer> qlist = preorder(q);
//         return plist.equals(qlist);
        
        
        if (p==null && q==null) return true;
        else if ((p==null && q!=null) ||(p!=null && q==null)) return false;
        //else if (p.val == q.val) return true;
        else if (p.val!=q.val) return false;
        return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
        
        
        
        
        
        
    }
    
    public List<Integer> preorder(TreeNode x) {
        List<Integer> res = new ArrayList<>();
        if (x==null) return res;
        
        Stack<TreeNode> stack = new Stack<>();
        stack.push(x);
        while (!stack.isEmpty()) {
            TreeNode node = stack.pop();
            if (node==null) res.add(null);
            else{
            res.add(node.val);
             stack.push(node.left);
             stack.push(node.right);
            }
        }
        return res;
    }
}
