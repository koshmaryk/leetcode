class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < numCourses; ++i) {
            adj.add(new ArrayList<>());
        }
        
        for (int[] prerequisite : prerequisites) {
            adj.get(prerequisite[0]).add(prerequisite[1]);
        }
        
        int[] visited = new int[numCourses];
        for (int u = 0; u < numCourses; ++u) {
            if (visited[u] == 0) {
                if (isCycle(u, visited, adj)) {
                    return false;
                }
            }
        }
        
        return true;
    }
    
    private boolean isCycle(int u, int[] visited, List<List<Integer>> adj) {
        if (visited[u] == -1) {
            return true;
        }
        
        visited[u] = -1;
        
        for (int v : adj.get(u)) {
            if (visited[v] != 1) {
                if (isCycle(v, visited, adj)) {
                    return true;
                }
            }
        }
        
        visited[u] = 1;
        
        return false;
    }
}