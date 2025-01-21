## Remove Outermost Parentheses

**Problem Link:** https://leetcode.com/problems/remove-outermost-parentheses/description

**Problem Statement:**
- Input: A string `s` containing only parentheses.
- Constraints: `s` is a valid parentheses sequence, and the length of `s` is less than or equal to `10^4`.
- Expected Output: A string with the outermost parentheses removed from each primitive substring in the given string.
- Key Requirements: Identify the outermost parentheses in each primitive substring and remove them.
- Example Test Cases:
  - Input: `"(()())(())()"`, Output: `"()()()"`
  - Input: `"(()())(())()((()))"`, Output: `"()()()()(())"`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through the string to identify the outermost parentheses of each primitive substring.
- Step-by-step breakdown:
  1. Initialize an empty stack to track the opening parentheses.
  2. Initialize an empty result string.
  3. Iterate through the input string. For each character:
    - If the character is an opening parenthesis, push it onto the stack.
    - If the character is a closing parenthesis, pop the corresponding opening parenthesis from the stack.
    - If the stack is not empty after popping (meaning we are inside a primitive substring), append the closing parenthesis to the result string.
  4. However, the brute force approach as described would need adjustments to accurately identify and remove the outermost parentheses from each primitive substring.

```cpp
string removeOuterParentheses(string s) {
    string result;
    int stackSize = 0;
    string primitiveSubstring;
    
    for (char c : s) {
        if (c == '(') {
            if (stackSize > 0) {
                primitiveSubstring += c;
            }
            stackSize++;
        } else {
            stackSize--;
            if (stackSize > 0) {
                primitiveSubstring += c;
            }
            if (stackSize == 0) {
                result += primitiveSubstring;
                primitiveSubstring.clear();
            }
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string, because we iterate through the string once.
> - **Space Complexity:** $O(n)$, as in the worst case, the result string could be of the same length as the input string.
> - **Why these complexities occur:** The iteration through the string and the construction of the result string dictate the time and space complexities.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of using a stack to track the parentheses, we can directly identify the outermost parentheses by counting the balance of opening and closing parentheses.
- Detailed breakdown:
  1. Initialize an empty result string and a counter for the balance of parentheses.
  2. Initialize a flag to track whether we are currently within a primitive substring.
  3. Iterate through the input string. For each character:
    - If the character is an opening parenthesis and the balance is 0, it's the start of a new primitive substring, so do not append it to the result.
    - Otherwise, append the character to the result.
    - Update the balance accordingly.
  4. This approach directly constructs the result string without needing to identify and remove the outermost parentheses in a separate step.

```cpp
string removeOuterParentheses(string s) {
    string result;
    int balance = 0;
    
    for (char c : s) {
        if (c == '(' && balance == 0) {
            // Skip the outermost opening parenthesis
            balance++;
        } else if (c == '(') {
            result += c;
            balance++;
        } else if (c == ')' && balance == 1) {
            // Skip the outermost closing parenthesis
            balance--;
        } else {
            result += c;
            balance--;
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string, because we iterate through the string once.
> - **Space Complexity:** $O(n)$, as in the worst case, the result string could be of the same length as the input string.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the input string and uses a minimal amount of extra space to keep track of the balance of parentheses.

---

### Final Notes

**Learning Points:**
- Key algorithmic concept demonstrated: Using a balance counter to track the nesting of parentheses.
- Problem-solving pattern identified: Direct construction of the result string by selectively including characters based on their position within the primitive substrings.
- Optimization technique learned: Avoiding unnecessary operations by skipping the outermost parentheses directly during the iteration.

**Mistakes to Avoid:**
- Not correctly handling the edge cases where the input string starts or ends with a primitive substring.
- Failing to update the balance counter correctly, leading to incorrect identification of the outermost parentheses.
- Not considering the possibility of an empty input string or a string with no primitive substrings.