class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        Map<Integer, List<Integer>> adj = new HashMap<>();
        for (int[] prerequisite : prerequisites) {
            List<Integer> list = adj.getOrDefault(prerequisite[1], new ArrayList<>());
            list.add(prerequisite[0]);
            adj.put(prerequisite[1], list);
        }

        
        Stack<Integer> stack = new Stack<>();
        int[] visited = new int[numCourses];
        for (int u = 0; u < numCourses; ++u) {
            if (visited[u] == 0) {
                if (isCycle(u, stack, visited, adj)) {
                    return new int[0];
                }
            }
        }

        int[] ordering = new int[numCourses];
        int i = 0;
        while (!stack.isEmpty()) {
            ordering[i++] = stack.pop();
        }

        return ordering;
    }

    private boolean isCycle(int u, Stack<Integer> stack,  int[] visited, Map<Integer, List<Integer>> adj) {
        if (visited[u] == -1) {
            return true;
        }

        visited[u] = -1;

        for (int v : adj.getOrDefault(u, new ArrayList<>())) {
            if (visited[v] != 1) {
                if (isCycle(v, stack, visited, adj)) {
                    return true;
                }
            }
        }

        visited[u] = 1;
        stack.push(u);

        return false;
    }

    
}