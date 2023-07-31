/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int maxDepth(TreeNode root) {
        LinkedList<Pair<TreeNode, Integer>> stack = new LinkedList<>();
        if (root != null) {
            stack.add(new Pair(root, 1));
        }

        int max = 0;
        while (!stack.isEmpty()) {
            Pair<TreeNode, Integer> pair = stack.removeLast();
            TreeNode node = pair.getKey();
            Integer depth = pair.getValue();
            if (node != null) {
                max = Math.max(max, depth);
                stack.add(new Pair(node.left, depth + 1));
                stack.add(new Pair(node.right, depth + 1));
            }
        }

        return max;
    }
}