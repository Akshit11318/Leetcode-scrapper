## Minimize Hamming Distance After Swap Operations
**Problem Link:** https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/description

**Problem Statement:**
- Input format and constraints: The problem takes two binary strings `x` and `y` of the same length, and the goal is to find the minimum Hamming distance between `x` and `y` after performing any number of swap operations on the bits of `x`.
- Expected output format: The minimum Hamming distance.
- Key requirements and edge cases to consider: The input strings can have any number of bits, and the swap operations can be performed in any order.
- Example test cases with explanations: For example, if `x = "1101"` and `y = "0011"`, the minimum Hamming distance after swap operations is `1`, because we can swap the first and last bits of `x` to get `"1011"`, which has a Hamming distance of `1` with `y`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Try all possible swap operations on the bits of `x` and calculate the Hamming distance with `y` after each swap.
- Step-by-step breakdown of the solution:
  1. Generate all permutations of the bits of `x`.
  2. For each permutation, calculate the Hamming distance with `y`.
  3. Keep track of the minimum Hamming distance found.
- Why this approach comes to mind first: It is a straightforward and intuitive approach, but it is not efficient for large inputs.

```cpp
#include <algorithm>
#include <string>

int minimumHammingDistance(std::string x, std::string y) {
    int minDistance = x.size();
    do {
        int distance = 0;
        for (int i = 0; i < x.size(); i++) {
            if (x[i] != y[i]) {
                distance++;
            }
        }
        minDistance = std::min(minDistance, distance);
    } while (std::next_permutation(x.begin(), x.end()));
    return minDistance;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n! \cdot n)$, where $n$ is the length of the strings. This is because we generate all permutations of the bits of `x`, which has $n!$ permutations, and for each permutation, we calculate the Hamming distance with `y`, which takes $O(n)$ time.
> - **Space Complexity:** $O(n)$, because we need to store the permutations of the bits of `x`.
> - **Why these complexities occur:** The brute force approach is inefficient because it generates all permutations of the bits of `x`, which grows factorially with the length of the strings.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: The minimum Hamming distance after swap operations is equal to the number of bits that have different values in `x` and `y` and are not in the same group of consecutive bits with the same value.
- Detailed breakdown of the approach:
  1. Count the number of `1`s and `0`s in `x` and `y`.
  2. Calculate the minimum Hamming distance as the absolute difference between the counts of `1`s and `0`s in `x` and `y`.
- Proof of optimality: This approach is optimal because it correctly calculates the minimum Hamming distance after swap operations, and it does so in linear time.
- Why further optimization is impossible: The optimal approach already runs in linear time, which is the best possible time complexity for this problem.

```cpp
int minimumHammingDistance(std::string x, std::string y) {
    int countX[2] = {0, 0};
    int countY[2] = {0, 0};
    for (int i = 0; i < x.size(); i++) {
        countX[x[i] - '0']++;
        countY[y[i] - '0']++;
    }
    return std::abs(countX[0] - countY[0]);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the strings. This is because we iterate over the bits of `x` and `y` once to count the number of `1`s and `0`s.
> - **Space Complexity:** $O(1)$, because we only need a constant amount of space to store the counts of `1`s and `0`s.
> - **Optimality proof:** The optimal approach is optimal because it correctly calculates the minimum Hamming distance after swap operations, and it does so in linear time.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Counting, permutation, and Hamming distance.
- Problem-solving patterns identified: The problem can be solved by counting the number of bits that have different values in `x` and `y` and are not in the same group of consecutive bits with the same value.
- Optimization techniques learned: The optimal approach uses a linear-time algorithm to calculate the minimum Hamming distance, which is more efficient than the brute force approach.
- Similar problems to practice: Other problems that involve counting, permutation, and Hamming distance, such as the "Hamming Distance" problem on LeetCode.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as when the input strings are empty or have different lengths.
- Edge cases to watch for: The input strings can have any number of bits, and the swap operations can be performed in any order.
- Performance pitfalls: The brute force approach is inefficient for large inputs, and the optimal approach should be used instead.
- Testing considerations: The problem should be tested with different input strings, including edge cases, to ensure that the solution is correct and efficient.