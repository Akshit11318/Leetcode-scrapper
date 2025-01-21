## Gray Code
**Problem Link:** https://leetcode.com/problems/gray-code/description

**Problem Statement:**
- Input: An integer `n`, which is the number of bits.
- Constraints: $1 \leq n \leq 16$
- Expected output: A list of integers representing the Gray code sequence for `n` bits.
- Key requirements: The sequence should contain all possible binary numbers with `n` bits, and each number should differ from its predecessor by exactly one bit.
- Example test cases:
  - For `n = 2`, the output should be `[0, 1, 3, 2]`, which corresponds to the binary numbers `00`, `01`, `11`, and `10`.
  - For `n = 3`, the output should be `[0, 1, 3, 2, 6, 7, 5, 4]`, which corresponds to the binary numbers `000`, `001`, `011`, `010`, `110`, `111`, `101`, and `100`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to generate all possible binary numbers with `n` bits and then try to find a sequence that satisfies the Gray code condition.
- Step-by-step breakdown:
  1. Generate all possible binary numbers with `n` bits.
  2. Try to find a sequence that satisfies the Gray code condition by iterating over all permutations of the binary numbers.
  3. Check each permutation to see if it satisfies the condition that each number differs from its predecessor by exactly one bit.
- Why this approach comes to mind first: It is a straightforward approach that tries to brute-force the solution by checking all possible permutations.

```cpp
#include <vector>
#include <algorithm>

class Solution {
public:
    std::vector<int> grayCode(int n) {
        std::vector<int> result;
        for (int i = 0; i < (1 << n); i++) {
            result.push_back(i);
        }
        // Try to find a sequence that satisfies the Gray code condition
        std::sort(result.begin(), result.end(), [&](int a, int b) {
            int diff = __builtin_popcount(a ^ b);
            return diff == 1;
        });
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n \cdot 2^n)$, where $2^n$ is the number of binary numbers with `n` bits, and $n$ is the number of bits to check for differences.
> - **Space Complexity:** $O(2^n)$, where $2^n$ is the number of binary numbers with `n` bits.
> - **Why these complexities occur:** The time complexity occurs because we are trying to find a sequence that satisfies the Gray code condition by iterating over all permutations of the binary numbers, and the space complexity occurs because we need to store all the binary numbers.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: The Gray code sequence can be generated recursively by reflecting the sequence for `n-1` bits and prefixing the reflected sequence with `1`.
- Detailed breakdown:
  1. Start with the base case where `n = 1`, and the sequence is `[0, 1]`.
  2. For each additional bit, reflect the sequence for `n-1` bits and prefix the reflected sequence with `1`.
- Proof of optimality: This approach is optimal because it generates the Gray code sequence directly without trying all permutations, resulting in a much faster time complexity.

```cpp
class Solution {
public:
    std::vector<int> grayCode(int n) {
        std::vector<int> result = {0, 1};
        for (int i = 2; i <= n; i++) {
            int size = result.size();
            for (int j = size - 1; j >= 0; j--) {
                result.push_back(result[j] | (1 << (i - 1)));
            }
        }
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where $2^n$ is the number of binary numbers with `n` bits.
> - **Space Complexity:** $O(2^n)$, where $2^n$ is the number of binary numbers with `n` bits.
> - **Optimality proof:** This approach is optimal because it generates the Gray code sequence directly without trying all permutations, resulting in a much faster time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: Recursive sequence generation, bit manipulation.
- Problem-solving patterns: Reflecting a sequence to generate a new sequence.
- Optimization techniques: Avoiding brute-force approaches by finding a direct generation method.

**Mistakes to Avoid:**
- Trying to brute-force the solution by checking all permutations.
- Not considering the recursive nature of the Gray code sequence.
- Not optimizing the solution to reduce time complexity.