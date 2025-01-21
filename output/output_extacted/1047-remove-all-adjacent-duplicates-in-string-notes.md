## Remove All Adjacent Duplicates in String
**Problem Link:** https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description

**Problem Statement:**
- Input format and constraints: The input is a string `S` containing lowercase letters.
- Expected output format: The output should be a string after removing all adjacent duplicates from `S`.
- Key requirements and edge cases to consider: Handle cases where the string is empty, has a single character, or has no adjacent duplicates.
- Example test cases with explanations:
  - Input: `"abbaca"` - Output: `"ca"` - Explanation: Remove all adjacent duplicates to get `"ca"`.
  - Input: `"azxxzy"` - Output: `"ay"` - Explanation: Remove all adjacent duplicates to get `"ay"`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through the string and check each character with its adjacent one. If they are the same, remove them.
- Step-by-step breakdown of the solution:
  1. Initialize an empty string to store the result.
  2. Iterate through the input string.
  3. For each character, check if it is the same as the last character in the result string.
  4. If they are the same, remove the last character from the result string.
  5. If they are different, append the current character to the result string.
- Why this approach comes to mind first: It directly addresses the problem statement by comparing adjacent characters and removing duplicates.

```cpp
string removeDuplicates(string S) {
    string result = "";
    for (char c : S) {
        if (result.empty() || result.back() != c) {
            result += c;
        } else {
            result.pop_back();
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the length of the string, because we make a single pass through the string.
> - **Space Complexity:** $O(n)$ because in the worst case, the result string could be the same length as the input string.
> - **Why these complexities occur:** The time complexity is linear due to the single pass through the string, and the space complexity is linear because we store the result in a new string.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal approach is essentially the same as the brute force approach because it already has a linear time complexity, which is the best we can achieve for this problem since we must examine every character at least once.
- Detailed breakdown of the approach: The approach remains the same as the brute force: iterate through the string, comparing each character with the last character in the result string, and update the result string accordingly.
- Proof of optimality: Since we must check every character in the string to determine if it should be included in the result, the optimal time complexity is $O(n)$, which our solution achieves.
- Why further optimization is impossible: Given that we must examine every character, any algorithm must have at least a time complexity of $O(n)$, making our solution optimal in terms of time complexity.

```cpp
string removeDuplicates(string S) {
    string result = "";
    for (char c : S) {
        if (result.empty() || result.back() != c) {
            result += c;
        } else {
            result.pop_back();
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string, because we make a single pass through the string.
> - **Space Complexity:** $O(n)$ because in the worst case, the result string could be the same length as the input string.
> - **Optimality proof:** The solution is optimal because it achieves the minimum possible time complexity of $O(n)$ for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, conditional checks, and string manipulation.
- Problem-solving patterns identified: The importance of examining each element in the input to solve the problem.
- Optimization techniques learned: Recognizing when a simple, straightforward approach is already optimal due to the inherent complexity of the problem.
- Similar problems to practice: Other string manipulation problems, such as removing duplicates from an array or linked list.

**Mistakes to Avoid:**
- Common implementation errors: Failing to check for an empty string before accessing its elements, or not handling the case where the result string is empty.
- Edge cases to watch for: Handling strings with a single character, or strings with no adjacent duplicates.
- Performance pitfalls: Using inefficient data structures or algorithms that result in higher than necessary time or space complexity.
- Testing considerations: Thoroughly testing the function with a variety of input cases, including edge cases and large inputs, to ensure correctness and performance.