class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        Map<Integer, List<Integer>> adj = new HashMap<>();
        for (int i = 0; i < numCourses; ++i) {
            adj.put(i, new ArrayList<>());
        }

        for (int[] prerequisite : prerequisites) {
            adj.get(prerequisite[0]).add(prerequisite[1]);
        }

        Set<Integer> visited = new HashSet<>();
        for (int u = 0; u < numCourses; ++u) {
            if (isCycle(u, visited, adj)) {
                return false;
            }
        }

        return true;
        
    }

    private boolean isCycle(int u, Set<Integer> visited, Map<Integer, List<Integer>> adj) {
        if (visited.contains(u)) {
            return true;
        }

        if (adj.get(u).isEmpty()) {
            return false;
        }

        visited.add(u);

        for (int v : adj.get(u)) {
            if (isCycle(v, visited, adj)) {
                return true;
            }
        }

        visited.remove(u);
        adj.put(u, new ArrayList<>());
        return false;
    } 
}