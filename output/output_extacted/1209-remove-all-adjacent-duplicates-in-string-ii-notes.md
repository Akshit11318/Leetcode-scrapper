## Remove All Adjacent Duplicates in String II

**Problem Link:** https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/description

**Problem Statement:**
- Input: A string `s` and an integer `k`.
- Constraints: `1 <= k <= s.length <= 10^5`.
- Expected output: The string after removing all adjacent duplicates in `s` where each duplicate occurs `k` times.
- Key requirements: The removal process should be repeated until no more adjacent duplicates exist.
- Example test cases:
  - Input: `s = "abcd", k = 2`
    - Output: `"abcd"`
  - Input: `s = "deeedbbcccbdaa", k = 3`
    - Output: `"aa"`
  - Input: `s = "pbbcggttciiippooaais", k = 2`
    - Output: `"ps"

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through the string and check for adjacent duplicates.
- Step-by-step breakdown:
  1. Initialize an empty stack to store characters and their counts.
  2. Iterate through the string. For each character:
    - If the stack is not empty and the top of the stack matches the current character, increment the count of the top of the stack.
    - If the count of the top of the stack equals `k`, pop the top of the stack.
    - Otherwise, push the current character and its count (1) onto the stack.
  3. After iterating through the string, construct the result string from the stack.

```cpp
#include <stack>
#include <string>

std::string removeDuplicates(std::string s, int k) {
    std::stack<std::pair<char, int>> stack;
    for (char c : s) {
        if (!stack.empty() && stack.top().first == c) {
            stack.top().second++;
            if (stack.top().second == k) {
                stack.pop();
            }
        } else {
            stack.push({c, 1});
        }
    }
    std::string result;
    while (!stack.empty()) {
        auto [char_, count] = stack.top();
        stack.pop();
        result.insert(0, count, char_);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string, because we iterate through the string once and stack operations (push and pop) take constant time.
> - **Space Complexity:** $O(n)$, because in the worst-case scenario, we might need to store all characters in the stack.
> - **Why these complexities occur:** These complexities occur because we process each character in the string exactly once and use a stack to keep track of characters and their counts.

---

### Optimal Approach (Required)

The brute force approach provided is already quite efficient and is considered optimal for this problem because it processes the string in a single pass and uses a stack to efficiently manage the removal of duplicates.

However, for clarity and completeness, let's reiterate the optimal approach with an emphasis on its optimality:

**Explanation:**
- Key insight: Utilizing a stack to keep track of characters and their counts allows for efficient removal of adjacent duplicates.
- Detailed breakdown: The approach remains the same as the brute force approach, emphasizing the use of a stack to process the string in a single pass.
- Proof of optimality: This approach is optimal because it only requires a single pass through the string, and the use of a stack ensures that the removal of duplicates is done efficiently without unnecessary iterations or comparisons.

The code provided in the brute force section is already the optimal solution.

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string, due to the single pass through the string.
> - **Space Complexity:** $O(n)$, because in the worst-case scenario, all characters might need to be stored in the stack.
> - **Optimality proof:** The single-pass nature and the efficient use of a stack make this approach optimal for the given problem constraints.

---

### Final Notes

**Learning Points:**
- Key algorithmic concept: Using a stack to efficiently manage and remove adjacent duplicates in a string.
- Problem-solving pattern: Processing a string in a single pass and leveraging a stack for efficient management of character counts.
- Optimization technique: Minimizing iterations and comparisons by utilizing a stack.

**Mistakes to Avoid:**
- Not considering the use of a stack for efficient management of character counts.
- Attempting to solve the problem with multiple passes through the string, which is unnecessary.
- Overcomplicating the solution by introducing additional data structures or operations beyond what is necessary.