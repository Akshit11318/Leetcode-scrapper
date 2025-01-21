## Cracking the Safe
**Problem Link:** https://leetcode.com/problems/cracking-the-safe/description

**Problem Statement:**
- Input format and constraints: The problem asks to crack a safe with `n` combination length and `k` possible digits. The goal is to find the shortest sequence of combinations that will open the safe, with the constraint that the last `n-1` digits of a combination must be the first `n-1` digits of the next combination.
- Expected output format: The output should be a string representing the shortest sequence of combinations that will open the safe.
- Key requirements and edge cases to consider:
  - The length of the combination is `n`.
  - There are `k` possible digits for each position in the combination.
  - The last `n-1` digits of a combination must be the first `n-1` digits of the next combination.
- Example test cases with explanations:
  - For `n = 3` and `k = 2`, the output should be "01110".
  - For `n = 2` and `k = 2`, the output should be "00".

---

### Brute Force Approach
**Explanation:**
- Initial thought process: The brute force approach involves trying all possible combinations of digits and checking if they satisfy the constraint.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of `n` digits from `k` possible digits.
  2. For each combination, check if the last `n-1` digits are the same as the first `n-1` digits of the next combination.
  3. If a combination satisfies the constraint, add it to the sequence.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it is not efficient for large values of `n` and `k`.

```cpp
#include <iostream>
#include <string>
#include <vector>

string crackSafe(int n, int k) {
    string result;
    vector<string> combinations;
    for (int i = 0; i < k; i++) {
        string combination;
        for (int j = 0; j < n; j++) {
            combination += to_string(i);
        }
        combinations.push_back(combination);
    }
    for (int i = 0; i < k; i++) {
        for (int j = 0; j < k; j++) {
            string combination = to_string(i) + to_string(j);
            for (int l = 0; l < n - 2; l++) {
                combination += to_string(i);
            }
            combinations.push_back(combination);
        }
    }
    for (const auto& combination : combinations) {
        result += combination;
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(k^{n})$, where $k$ is the number of possible digits and $n$ is the length of the combination. This is because we are generating all possible combinations of `n` digits from `k` possible digits.
> - **Space Complexity:** $O(k^{n})$, where $k$ is the number of possible digits and $n$ is the length of the combination. This is because we are storing all possible combinations in a vector.
> - **Why these complexities occur:** These complexities occur because we are using a brute force approach that involves trying all possible combinations of digits.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: The key insight is to use a De Bruijn sequence, which is a sequence of characters that contains every possible substring of a certain length exactly once.
- Detailed breakdown of the approach:
  1. Generate a De Bruijn sequence of length `k^n`.
  2. The De Bruijn sequence will contain every possible combination of `n` digits from `k` possible digits exactly once.
  3. The shortest sequence of combinations that will open the safe is the De Bruijn sequence itself.
- Proof of optimality: The De Bruijn sequence is optimal because it contains every possible combination of `n` digits from `k` possible digits exactly once, which means that it is the shortest possible sequence that will open the safe.
- Why further optimization is impossible: Further optimization is impossible because the De Bruijn sequence is already the shortest possible sequence that will open the safe.

```cpp
#include <iostream>
#include <string>
#include <vector>

string crackSafe(int n, int k) {
    string result;
    vector<int> a(n, 0);
    int count = 1;
    for (int i = 0; i < k; i++) {
        a[0] = i;
        while (count <= k) {
            for (int j = n - 1; j >= 0; j--) {
                result += to_string(a[j]);
            }
            int carry = 1;
            for (int j = n - 1; j >= 0; j--) {
                if (carry == 0) break;
                a[j] += carry;
                carry = a[j] / k;
                a[j] %= k;
            }
            count++;
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(k^{n})$, where $k$ is the number of possible digits and $n$ is the length of the combination. This is because we are generating a De Bruijn sequence of length `k^n`.
> - **Space Complexity:** $O(k^{n})$, where $k` is the number of possible digits and `n` is the length of the combination. This is because we are storing the De Bruijn sequence in a string.
> - **Optimality proof:** The De Bruijn sequence is optimal because it contains every possible combination of `n` digits from `k` possible digits exactly once, which means that it is the shortest possible sequence that will open the safe.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the use of De Bruijn sequences to solve a problem that involves finding the shortest sequence of combinations that will open a safe.
- Problem-solving patterns identified: The problem requires the use of a systematic approach to generate all possible combinations of `n` digits from `k` possible digits.
- Optimization techniques learned: The problem demonstrates the use of De Bruijn sequences to optimize the solution.
- Similar problems to practice: Other problems that involve finding the shortest sequence of combinations, such as the "Shortest Path" problem.

**Mistakes to Avoid:**
- Common implementation errors: One common implementation error is to use a brute force approach that tries all possible combinations of digits, which can be inefficient for large values of `n` and `k`.
- Edge cases to watch for: One edge case to watch for is when `n` is 1, in which case the solution is simply a string of `k` digits.
- Performance pitfalls: One performance pitfall is to use a recursive approach to generate the De Bruijn sequence, which can be slow for large values of `n` and `k`.
- Testing considerations: The solution should be tested for different values of `n` and `k` to ensure that it works correctly.