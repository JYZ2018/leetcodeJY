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
    public List<Integer> inorderTraversal(TreeNode root) {
        
        List<Integer> res= new ArrayList<>();
        Stack<TreeNode> stack= new Stack<>();
        TreeNode node=root;
        
        while (node!=null || !stack.isEmpty()) {
            while (node!=null) {
                //System.out.println(node.val);
                stack.push(node);
                node=node.left;
            }
            
            node =stack.pop();
            //System.out.println(node);
            res.add(node.val);
            node=node.right;
        }
        
        return res;
    }
        
        
        
        
        
        
        
        
        
        
       /*
       List<Integer> res= new ArrayList<>();
       helper(root,res);
       return res;
    }
