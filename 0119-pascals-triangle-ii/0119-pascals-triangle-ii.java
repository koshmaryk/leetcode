class Solution {
    public List<Integer> getRow(int rowIndex) {
        Integer[] row = new Integer[rowIndex + 1];
        row[0] = 1;

        for (int i = 1; i < rowIndex + 1; ++i) {
            row[i] = 1;
            
            for (int j = i - 1; j > 0; j--) {
                row[j] += row[j - 1]; 
            }
        }

        return Arrays.asList(row);
    }
}