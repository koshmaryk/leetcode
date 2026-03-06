class Solution {
    public boolean isValid(String s) {
        var brackets = new HashMap<Character, Character>();
        brackets.put(')', '(');
        brackets.put('}', '{');
        brackets.put(']', '[');

        var stack = new ArrayDeque<Character>();
        for (char c: s.toCharArray()) {
            if (brackets.containsKey(c)) {
                if (!stack.isEmpty() && stack.peek() == brackets.get(c)) {
                    stack.pop();
                } else {
                    return false;
                }
            } else {
                stack.push(c);
            }
        }

        return stack.size() == 0;
    }
}