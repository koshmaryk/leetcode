/**
 * Definition for a binary tree node.
 * class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
 *   var value: Int = _value
 *   var left: TreeNode = _left
 *   var right: TreeNode = _right
 * }
 */
import scala.collection.mutable.Stack


object Solution {
    def maxDepth(root: TreeNode): Int = {
        val stack = new Stack[(TreeNode, Int)]()
        if (root != null) stack.push((root, 1))

        var maxDepth = 0
        while (stack.nonEmpty) {
            val (node, depth) = stack.pop()
            if (node != null) {
                maxDepth = maxDepth.max(depth)
                stack.push((node.left, depth + 1))
                stack.push((node.right, depth + 1))
            }
        }
        
        maxDepth
    }
}