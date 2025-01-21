## Time Needed to Rearrange a Binary String

**Problem Link:** https://leetcode.com/problems/time-needed-to-rearrange-a-binary-string/description

**Problem Statement:**
- Input format: A binary string `s` containing only characters '0' and '1'.
- Constraints: `1 <= s.length <= 1000`.
- Expected output format: The minimum time needed to rearrange the binary string.
- Key requirements and edge cases to consider: The minimum time is calculated based on the number of adjacent different characters in the string.
- Example test cases with explanations:
  - Input: `s = "1111"`
    - Output: `0`
    - Explanation: The string is already rearranged.
  - Input: `s = "00110"`
    - Output: `1`
    - Explanation: We can rearrange the string to `"11000"`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible permutations of the binary string and calculate the time needed for each permutation.
- Step-by-step breakdown of the solution:
  1. Generate all permutations of the binary string.
  2. For each permutation, calculate the time needed by counting the number of adjacent different characters.
  3. Return the minimum time needed among all permutations.
- Why this approach comes to mind first: It is a straightforward approach to solve the problem by trying all possible solutions.

```cpp
#include <algorithm>
#include <string>
using namespace std;

int minimumTime(string s) {
    int minTime = INT_MAX;
    do {
        int time = 0;
        for (int i = 0; i < s.length() - 1; i++) {
            if (s[i] != s[i + 1]) {
                time++;
            }
        }
        minTime = min(minTime, time);
    } while (next_permutation(s.begin(), s.end()));
    return minTime;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n! \cdot n)$, where $n$ is the length of the string. This is because we are generating all permutations of the string and calculating the time needed for each permutation.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the string. This is because we need to store the string.
> - **Why these complexities occur:** The brute force approach has high time complexity because it tries all possible solutions, resulting in an exponential number of operations.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The minimum time needed to rearrange the binary string is equal to the minimum number of adjacent different characters in the string.
- Detailed breakdown of the approach:
  1. Count the number of '0's and '1's in the string.
  2. Calculate the minimum number of adjacent different characters based on the counts.
- Proof of optimality: This approach is optimal because it directly calculates the minimum number of adjacent different characters without trying all possible solutions.
- Why further optimization is impossible: This approach has a linear time complexity, which is the best possible time complexity for this problem.

```cpp
int minimumTime(string s) {
    int zeros = 0, ones = 0;
    for (char c : s) {
        if (c == '0') {
            zeros++;
        } else {
            ones++;
        }
    }
    return min(zeros, ones);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string. This is because we are counting the number of '0's and '1's in the string.
> - **Space Complexity:** $O(1)$, where $n$ is the length of the string. This is because we only need a constant amount of space to store the counts.
> - **Optimality proof:** This approach is optimal because it directly calculates the minimum number of adjacent different characters without trying all possible solutions.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Counting, permutation.
- Problem-solving patterns identified: Direct calculation, brute force.
- Optimization techniques learned: Reducing the number of operations by directly calculating the solution.
- Similar problems to practice: Other problems that involve counting and permutation.

**Mistakes to Avoid:**
- Common implementation errors: Not considering the edge cases, not optimizing the solution.
- Edge cases to watch for: Empty string, string with only one character.
- Performance pitfalls: Using brute force approach for large inputs.
- Testing considerations: Test the solution with different inputs, including edge cases.