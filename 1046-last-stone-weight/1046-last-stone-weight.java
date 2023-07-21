class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> heap = new PriorityQueue<>((a, b) -> b - a);
        
        for (int stone : stones) {
            heap.offer(stone);
        }
        
        while (heap.size() > 1) {
            int y = heap.poll();
            int x = heap.poll();
            
            if (x != y) {
                heap.offer(y - x);
            }
        }
        
        return heap.isEmpty() ? 0 : heap.poll();
    }
}