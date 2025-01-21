## Largest Number After Mutating Substring
**Problem Link:** https://leetcode.com/problems/largest-number-after-mutating-substring/description

**Problem Statement:**
- Input: A string `num` representing a non-negative integer and an integer `k`.
- Constraints: `1 <= num.length <= 10^4`, `0 <= k <= 10^4`, `num` consists of only digits, and `k` is a non-negative integer.
- Expected Output: The largest possible integer after possibly changing the digits of the number `num` at most `k` times.
- Key Requirements and Edge Cases: The string `num` can contain leading zeros, and `k` can be larger than the length of `num`.
- Example Test Cases:
  - Input: `num = "1317", k = 2`, Output: `"8181"`
  - Input: `num = "3202", k = 1`, Output: `"9221"`

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Generate all possible combinations of digits by replacing up to `k` digits in `num` and find the maximum among them.
- Step-by-step breakdown:
  1. Generate all possible combinations of digits with up to `k` replacements.
  2. For each combination, convert the digits back to a string and compare it with the current maximum.
  3. Update the maximum if a larger number is found.

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

void backtrack(std::string& num, int k, std::string& max_num, int index) {
    if (k == 0 || index == num.size()) {
        if (num > max_num) {
            max_num = num;
        }
        return;
    }
    for (int i = index; i < num.size(); ++i) {
        for (char c = '0'; c <= '9'; ++c) {
            if (c != num[i]) {
                --k;
                if (k < 0) break;
                num[i] = c;
                backtrack(num, k, max_num, i + 1);
                num[i] = num[i] - (c - num[i]);
                ++k;
            }
        }
    }
}

std::string largestNumberAfterMutatingSubstring(std::string num, int k) {
    std::string max_num = num;
    backtrack(num, k, max_num, 0);
    return max_num;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(10^{k} \cdot n)$, where $n$ is the length of `num`, because in the worst case, we generate all possible combinations of digits with up to `k` replacements.
> - **Space Complexity:** $O(n)$, because we use recursive call stack to store the current combination of digits.
> - **Why these complexities occur:** The brute force approach generates all possible combinations of digits with up to `k` replacements, resulting in exponential time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of generating all possible combinations of digits, we can use a greedy approach to replace the smallest digits with the largest possible digits.
- Detailed breakdown:
  1. Iterate through the string `num` and replace the smallest digits with the largest possible digits (`'9'`) until `k` replacements are used up.
  2. The resulting string will be the largest possible integer after possibly changing the digits of `num` at most `k` times.

```cpp
std::string largestNumberAfterMutatingSubstring(std::string num, int k) {
    for (int i = 0; i < num.size() && k > 0; ++i) {
        if (num[i] < '9') {
            num[i] = '9';
            --k;
        }
    }
    return num;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of `num`, because we iterate through the string `num` once.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the current index and the number of replacements left.
> - **Optimality proof:** This approach is optimal because it replaces the smallest digits with the largest possible digits, resulting in the largest possible integer after possibly changing the digits of `num` at most `k` times.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Greedy approach, string manipulation.
- Problem-solving patterns identified: Using a greedy approach to optimize the solution.
- Optimization techniques learned: Avoiding unnecessary computations by using a greedy approach.
- Similar problems to practice: Other problems that involve optimizing a solution using a greedy approach.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as `k` being larger than the length of `num`.
- Edge cases to watch for: Leading zeros in the input string `num`.
- Performance pitfalls: Using a brute force approach that generates all possible combinations of digits.
- Testing considerations: Testing the solution with different input cases, including edge cases.