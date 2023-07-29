class Solution {
    public int minimumSemesters(int n, int[][] relations) {
        Map<Integer, List<Integer>> adj = new HashMap<>();
        for (int[] relation : relations) {
            List<Integer> list = adj.getOrDefault(relation[0], new ArrayList<>());
            list.add(relation[1]);
            adj.put(relation[0], list);
        }

        int[] visited = new int[n + 1];
        int maxLength = 1;
        for (int u = 1; u < n + 1; ++u) {
            if (visited[u] == 0) {
                int length = maxLength(u, visited, adj);
                if (length == -1) {
                    return -1;
                }

                maxLength = Math.max(maxLength, length);
            }
        }

        return maxLength;
    }

    private int maxLength(int u, int[] visited, Map<Integer, List<Integer>> adj) {
        if (visited[u] != 0) {
            return visited[u];
        }

        visited[u] = -1;
        int maxLength = 1;
        for (int v : adj.getOrDefault(u, new ArrayList<>())) {
            int length = maxLength(v, visited, adj);
            if (length == -1) {
                return -1;
            }

            maxLength = Math.max(maxLength, length + 1);
        }

        visited[u] = maxLength;

        return maxLength;
    }
}