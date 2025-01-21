## Make the String Great

**Problem Link:** https://leetcode.com/problems/make-the-string-great/description

**Problem Statement:**
- Input format: a string `s` consisting of lowercase and uppercase letters.
- Constraints: `1 <= s.length <= 100`.
- Expected output format: a string `s` with all adjacent characters that are the same when ignoring case removed.
- Key requirements and edge cases to consider: handle all possible combinations of uppercase and lowercase letters, including single-character strings and empty strings.
- Example test cases with explanations:
  - Input: `"leEeetcode"`; Output: `"leetcode"`. Explanation: We can remove `"le"` because it is the same when ignoring case.
  - Input: `"abBAcC"`; Output: `"". Explanation: We can remove all characters because they are the same when ignoring case.
  - Input: `"s"`; Output: `"s"`. Explanation: No adjacent characters can be removed.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: iterate through the string, comparing each character with its adjacent one, and remove them if they are the same when ignoring case.
- Step-by-step breakdown of the solution:
  1. Initialize an empty result string.
  2. Iterate through each character in the input string.
  3. Compare the current character with the last character in the result string (if it exists).
  4. If they are the same when ignoring case, skip the current character; otherwise, append it to the result string.
  5. Repeat steps 2-4 until all characters in the input string have been processed.
- Why this approach comes to mind first: it directly addresses the problem statement by checking each character against its neighbor.

```cpp
string makeGood(string s) {
    string result = "";
    for (char c : s) {
        if (!result.empty() && tolower(result.back()) == tolower(c)) {
            result.pop_back();
        } else {
            result.push_back(c);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string. This is because we process each character in the string once.
> - **Space Complexity:** $O(n)$, as in the worst case, we might end up storing all characters in the result string.
> - **Why these complexities occur:** The linear time complexity is due to the single pass through the input string, and the space complexity is due to the storage required for the result string.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: utilizing a stack data structure to efficiently keep track of characters to be removed.
- Detailed breakdown of the approach:
  1. Initialize an empty stack.
  2. Iterate through each character in the input string.
  3. Compare the current character with the top of the stack (if it's not empty).
  4. If they are the same when ignoring case, pop the top of the stack; otherwise, push the current character onto the stack.
  5. After processing all characters, the stack will contain the characters of the resulting string.
- Proof of optimality: this approach is optimal because it processes each character exactly once, resulting in a linear time complexity.

```cpp
string makeGood(string s) {
    stack<char> stk;
    for (char c : s) {
        if (!stk.empty() && tolower(stk.top()) == tolower(c)) {
            stk.pop();
        } else {
            stk.push(c);
        }
    }
    string result = "";
    while (!stk.empty()) {
        result = stk.top() + result;
        stk.pop();
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string. This is because we process each character in the string once.
> - **Space Complexity:** $O(n)$, as in the worst case, we might end up storing all characters in the stack.
> - **Optimality proof:** The linear time complexity is due to the single pass through the input string, and the space complexity is due to the storage required for the stack.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: using a stack to efficiently process characters in a string, and iterating through a string to compare adjacent characters.
- Problem-solving patterns identified: utilizing data structures like stacks to simplify the processing of sequential data.
- Optimization techniques learned: recognizing the benefits of using a stack to avoid unnecessary comparisons and character removals.
- Similar problems to practice: other string manipulation problems involving character comparisons and removals.

**Mistakes to Avoid:**
- Common implementation errors: forgetting to handle edge cases like empty strings or single-character strings.
- Edge cases to watch for: ensuring the solution correctly handles strings with all uppercase or all lowercase letters.
- Performance pitfalls: using inefficient data structures or algorithms that lead to higher time or space complexities.
- Testing considerations: thoroughly testing the solution with various input cases to ensure correctness and efficiency.