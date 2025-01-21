## Reordered Power of 2
**Problem Link:** https://leetcode.com/problems/reordered-power-of-2/description

**Problem Statement:**
- Input format: An integer `n`.
- Constraints: $1 \leq n \leq 10^9$.
- Expected output format: A boolean indicating whether any permutation of `n` is a power of 2.
- Key requirements and edge cases to consider:
  - Checking all possible permutations of `n` to see if any are a power of 2.
  - Handling large inputs and avoiding unnecessary computations.
- Example test cases with explanations:
  - `n = 1` returns `true` because 1 is a power of 2 ($2^0$).
  - `n = 10` returns `false` because no permutation of 10 is a power of 2.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all permutations of `n`, and for each permutation, check if it's a power of 2.
- Step-by-step breakdown of the solution:
  1. Convert `n` to a string to easily generate permutations.
  2. Use a recursive function or a library function to generate all permutations of the string.
  3. For each permutation, convert it back to an integer and check if it's a power of 2.
- Why this approach comes to mind first: It's straightforward to generate permutations and check each one, but this approach is inefficient for large inputs.

```cpp
#include <algorithm>
#include <string>

class Solution {
public:
    bool reorderedPowerOf2(int n) {
        std::string str = std::to_string(n);
        std::sort(str.begin(), str.end());
        for (int i = 0; i < 30; ++i) {
            std::string powerOf2Str = std::to_string(1 << i);
            std::sort(powerOf2Str.begin(), powerOf2Str.end());
            if (str == powerOf2Str) return true;
        }
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(30 \times \log(n) \times \log(\log(n)))$ where $\log(n)$ is the number of digits in `n`, and $\log(\log(n))$ is due to sorting the digits of each power of 2.
> - **Space Complexity:** $O(\log(n))$ for storing the string representation of `n` and the current power of 2.
> - **Why these complexities occur:** The time complexity is dominated by generating and sorting the string representations of `n` and the powers of 2. The space complexity is due to storing these strings.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of generating all permutations of `n` and checking each, compare the sorted digits of `n` with the sorted digits of each power of 2 up to $2^{29}$.
- Detailed breakdown of the approach:
  1. Convert `n` to a string and sort its digits.
  2. For each power of 2 from $2^0$ to $2^{29}$, convert it to a string, sort its digits, and compare with the sorted digits of `n`.
  3. If a match is found, return `true`. If no match is found after checking all powers of 2, return `false`.
- Proof of optimality: This approach is optimal because it avoids generating unnecessary permutations and directly compares the sorted digits of `n` with those of each power of 2.

```cpp
#include <algorithm>
#include <string>

class Solution {
public:
    bool reorderedPowerOf2(int n) {
        std::string str = std::to_string(n);
        std::sort(str.begin(), str.end());
        for (int i = 0; i < 30; ++i) {
            std::string powerOf2Str = std::to_string(1 << i);
            std::sort(powerOf2Str.begin(), powerOf2Str.end());
            if (str == powerOf2Str) return true;
        }
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(30 \times \log(n) \times \log(\log(n)))$ where $\log(n)$ is the number of digits in `n`, and $\log(\log(n))$ is due to sorting the digits of each power of 2.
> - **Space Complexity:** $O(\log(n))$ for storing the string representation of `n` and the current power of 2.
> - **Optimality proof:** This is the most efficient approach because it directly compares the sorted digits of `n` with those of each power of 2, avoiding unnecessary permutations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting, permutation generation, and comparison.
- Problem-solving patterns identified: Using string representations to easily generate permutations and compare digits.
- Optimization techniques learned: Avoiding unnecessary computations by directly comparing sorted digits.
- Similar problems to practice: Other permutation and string comparison problems.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly generating permutations or comparing strings.
- Edge cases to watch for: Handling large inputs and ensuring correct sorting and comparison.
- Performance pitfalls: Generating unnecessary permutations or using inefficient comparison methods.
- Testing considerations: Thoroughly testing with various inputs, including edge cases.