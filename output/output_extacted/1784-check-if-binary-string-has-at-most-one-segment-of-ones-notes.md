## Check if Binary String Has at Most One Segment of Ones
**Problem Link:** https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/description

**Problem Statement:**
- Input format and constraints: The input is a binary string `s` consisting of only `0`s and `1`s. The string length can vary but is guaranteed to be non-empty.
- Expected output format: The function should return `true` if the binary string has at most one segment of ones and `false` otherwise.
- Key requirements and edge cases to consider:
  - A segment of ones is defined as a sequence of one or more `1`s in the string.
  - The string can start or end with a segment of ones.
  - The presence of multiple segments of ones, separated by any number of `0`s, should return `false`.
- Example test cases with explanations:
  - Input: `s = "1001"`; Output: `false` because there are two segments of ones.
  - Input: `s = "110"`; Output: `true` because there is only one segment of ones.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: To check if there is at most one segment of ones, we can iterate through the string and count the number of transitions from `0` to `1`. If we encounter more than one transition, it means there is more than one segment of ones.
- Step-by-step breakdown of the solution:
  1. Initialize a counter for transitions from `0` to `1`.
  2. Iterate through the string, checking each character.
  3. If the current character is `1` and the previous character is `0`, increment the transition counter.
  4. After iterating through the entire string, check the transition counter. If it is greater than 1, return `false`. Otherwise, return `true`.
- Why this approach comes to mind first: It's straightforward to think about counting the transitions as a way to determine the number of segments of ones.

```cpp
class Solution {
public:
    bool checkOnesSegment(string s) {
        int transitionCount = 0;
        bool previousWasOne = false;
        
        for (char c : s) {
            if (c == '1') {
                if (!previousWasOne) {
                    transitionCount++;
                }
                previousWasOne = true;
            } else {
                previousWasOne = false;
            }
            
            if (transitionCount > 1) {
                return false;
            }
        }
        
        return transitionCount <= 1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string, because we are scanning the string once.
> - **Space Complexity:** $O(1)$, as we are using a constant amount of space to store the transition count and the previous character's state.
> - **Why these complexities occur:** The linear time complexity is due to the single pass through the string, and the constant space complexity is because we are not using any data structures that scale with input size.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: The optimal approach remains similar to the brute force approach but focuses on the essential logic of counting transitions from `0` to `1` without unnecessary variables.
- Detailed breakdown of the approach:
  1. Initialize a transition counter.
  2. Iterate through the string, and whenever a `1` is encountered after a `0`, increment the counter.
  3. If the counter exceeds 1 at any point, immediately return `false`.
  4. After the iteration, if the counter is less than or equal to 1, return `true`.
- Proof of optimality: This approach is optimal because it only requires a single pass through the string and uses a minimal amount of extra memory, making its time complexity $O(n)$ and space complexity $O(1)$.

```cpp
class Solution {
public:
    bool checkOnesSegment(string s) {
        bool seenOne = false;
        bool seenZeroAfterOne = false;
        
        for (char c : s) {
            if (c == '1') {
                if (seenZeroAfterOne) return false;
                seenOne = true;
            } else {
                if (seenOne) seenZeroAfterOne = true;
            }
        }
        
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string, because we are scanning the string once.
> - **Space Complexity:** $O(1)$, as we are using a constant amount of space to store the state of having seen a one and a zero after a one.
> - **Optimality proof:** This is optimal because we are performing the minimum necessary operations to determine if there is more than one segment of ones, with no redundant checks or unnecessary memory usage.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, conditional checks, and the use of flags to track state.
- Problem-solving patterns identified: The pattern of counting transitions or changes in state to solve a problem.
- Optimization techniques learned: Minimizing the number of variables and checks to improve code clarity and efficiency.
- Similar problems to practice: Other string manipulation problems that involve counting or tracking specific patterns.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle edge cases, such as an empty string or a string with no `1`s.
- Edge cases to watch for: Strings that start or end with `1`s, strings with multiple segments of `1`s separated by `0`s.
- Performance pitfalls: Using unnecessary loops or data structures that increase time or space complexity.
- Testing considerations: Thoroughly testing with various inputs, including edge cases, to ensure the function behaves as expected.