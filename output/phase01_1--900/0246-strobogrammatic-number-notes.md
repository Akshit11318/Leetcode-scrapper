## Strobogrammatic Number
**Problem Link:** https://leetcode.com/problems/strobogrammatic-number/description

**Problem Statement:**
- Input format and constraints: The input is a string `num` containing only digits.
- Expected output format: The output is a boolean indicating whether the input string is a strobogrammatic number.
- Key requirements and edge cases to consider:
  - A strobogrammatic number is a number whose numeral is rotationally symmetric, so it appears the same when its digits are rotated by 180 degrees.
  - The mapping of digits that are rotationally symmetric: 0, 1, 6, 8, and 9 (where 6 becomes 9 and vice versa).
- Example test cases with explanations:
  - Input: `num = "69"` Output: `true`
  - Input: `num = "88"` Output: `true`
  - Input: `num = "962"` Output: `false`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To check if a number is strobogrammatic, we need to compare each digit from the start with its corresponding digit from the end and see if they are rotationally symmetric.
- Step-by-step breakdown of the solution:
  1. Create a mapping of rotationally symmetric digits.
  2. Compare each digit from the start with its corresponding digit from the end using the mapping.
  3. If all pairs match, the number is strobogrammatic.

```cpp
#include <iostream>
#include <string>
#include <unordered_map>

bool isStrobogrammatic(string num) {
    unordered_map<char, char> symmetricDigits = {{'0', '0'}, {'1', '1'}, {'6', '9'}, {'8', '8'}, {'9', '6'}};
    int left = 0, right = num.size() - 1;
    while (left <= right) {
        if (symmetricDigits[num[left]] != num[right]) {
            return false;
        }
        left++;
        right--;
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string `num`, because we are scanning the string once.
> - **Space Complexity:** $O(1)$, because the space used does not grow with the size of the input, as we are using a constant amount of space to store the mapping of symmetric digits.
> - **Why these complexities occur:** The time complexity is linear because we are making a single pass through the input string. The space complexity is constant because the size of the mapping does not depend on the input size.

---

### Optimal Approach (Required)

The brute force approach provided is already optimal for this problem, as it only requires a single pass through the input string to determine if it is strobogrammatic. The time complexity of $O(n)$ is the best we can achieve because we must at least read the input once. Therefore, there is no need to discuss a better approach or an alternative approach, as the brute force solution is already optimal for this problem.

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string `num`.
> - **Space Complexity:** $O(1)$, because the space used does not grow with the size of the input.
> - **Optimality proof:** This is optimal because we must read the input at least once to determine if it is strobogrammatic, and we do so in a single pass.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Use of a mapping to efficiently look up symmetric digits, and a two-pointer technique to compare digits from both ends of the string.
- Problem-solving patterns identified: The importance of understanding the problem constraints (in this case, the definition of a strobogrammatic number) and identifying a simple, efficient algorithm to solve it.
- Optimization techniques learned: Reducing the problem to its simplest form and using data structures like unordered maps for efficient lookups.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly implementing the mapping of symmetric digits or failing to handle edge cases like an empty input string.
- Edge cases to watch for: Handling inputs with non-digit characters or extremely large inputs.
- Performance pitfalls: Using inefficient algorithms or data structures that lead to higher than necessary time or space complexity.
- Testing considerations: Thoroughly testing the function with a variety of inputs, including edge cases, to ensure correctness.