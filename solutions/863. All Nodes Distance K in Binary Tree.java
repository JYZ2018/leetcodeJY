/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public List<Integer> distanceK(TreeNode root, TreeNode target, int k) {
        
        Map<TreeNode, TreeNode> parent = new HashMap<>();
        dfs(root,null,parent);
        
        List<Integer> res = new ArrayList<>();
        Deque<TreeNode> queue = new LinkedList<>();
        Set<TreeNode> visited = new HashSet<>();
        queue.offer(target);
        visited.add(target);
        visited.add(null);
        int dis=0;
        
        while (!queue.isEmpty()) {
            int size = queue.size();
            
            // if (dis==k) {
            //     for (TreeNode n: queue) res.add(n.val);
            // }
            
            while (size>0) {
                TreeNode node = queue.poll();
                size--;
                
                if (!visited.contains(node.left)) {
                    queue.offer(node.left); 
