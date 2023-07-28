class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        int[] indegree = new int[numCourses];
        List<List<Integer>> adj = new ArrayList<>();
        for (int u = 0; u < numCourses; ++u) {
            adj.add(new ArrayList<>());
        }

        for (int[] prerequisite : prerequisites) {
            adj.get(prerequisite[1]).add(prerequisite[0]);
            indegree[prerequisite[0]]++;
        }

        LinkedList<Integer> queue = new LinkedList<>();
        for (int u = 0; u < numCourses; ++u) {
            if (indegree[u] == 0) {
                queue.offer(u);
            }
        }

        int visited = 0;
        while (!queue.isEmpty()) {
            int u = queue.poll();
            visited++;

            for (int v : adj.get(u)) {
                // delete the edge v->neighbor
                indegree[v]--;
                if (indegree[v] == 0) {
                    queue.offer(v);
                }
            }
        }

        return visited == numCourses;
    }
}