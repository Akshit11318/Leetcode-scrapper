## Sum of All Subset XOR Totals

**Problem Link:** https://leetcode.com/problems/sum-of-all-subset-xor-totals/description

**Problem Statement:**
- Input format and constraints: Given an array of non-negative integers `nums`.
- Expected output format: Return the sum of all subset XOR totals for the array.
- Key requirements and edge cases to consider: 
  - The array can contain duplicate elements.
  - The array is not empty.
- Example test cases with explanations:
  - Input: `nums = [1, 3]`, Output: `6`, Explanation: The subsets of [1, 3] are: `[1]`, `[3]`, and `[1, 3]`. The XOR of `[1]` is `1`, of `[3]` is `3`, and of `[1, 3]` is `1 XOR 3 = 2`. Therefore, the sum of all subset XOR totals is `1 + 3 + 2 = 6`.
  - Input: `nums = [1, 2, 3, 4]`, Output: `60`, Explanation: The subsets of [1, 2, 3, 4] are: `[1]`, `[2]`, `[3]`, `[4]`, `[1, 2]`, `[1, 3]`, `[1, 4]`, `[2, 3]`, `[2, 4]`, `[3, 4]`, `[1, 2, 3]`, `[1, 2, 4]`, `[1, 3, 4]`, `[2, 3, 4]`, `[1, 2, 3, 4]`. Calculating the XOR of each subset and summing them up gives `60`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible subsets of the given array and calculate the XOR of each subset.
- Step-by-step breakdown of the solution:
  1. Generate all subsets of the given array.
  2. For each subset, calculate the XOR of its elements.
  3. Sum up the XOR totals of all subsets.

```cpp
#include <vector>
using namespace std;

int subsetXORSum(vector<int>& nums) {
    int n = nums.size();
    int total = 0;
    for (int mask = 0; mask < (1 << n); mask++) {
        int subsetXOR = 0;
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                subsetXOR ^= nums[i];
            }
        }
        total += subsetXOR;
    }
    return total;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot 2^n)$, where $n$ is the number of elements in the array. This is because we generate $2^n$ subsets and for each subset, we potentially iterate over all $n$ elements to calculate the XOR.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input array, because we only use a constant amount of space to store the current subset's XOR and the total sum.
> - **Why these complexities occur:** The time complexity is high because generating all subsets of an array results in exponential time complexity. The space complexity is low because we only need to keep track of a few variables, regardless of the size of the input.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The problem can be solved using bit manipulation to generate all subsets and then calculate the XOR of each subset.
- Detailed breakdown of the approach:
  1. Use bit manipulation to generate all subsets of the given array.
  2. For each subset, calculate the XOR of its elements using the XOR operation.
  3. Sum up the XOR totals of all subsets.
- Proof of optimality: This approach is optimal because it uses bit manipulation to efficiently generate all subsets and calculates the XOR of each subset in linear time with respect to the size of the subset.

```cpp
#include <vector>
using namespace std;

int subsetXORSum(vector<int>& nums) {
    int n = nums.size();
    int res = 0;
    for (int mask = 1; mask < (1 << n); mask++) {
        int xorSum = 0;
        for (int i = 0; i < n; i++) {
            if (mask & (1 << i)) {
                xorSum ^= nums[i];
            }
        }
        res += xorSum;
    }
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot 2^n)$, where $n$ is the number of elements in the array. This is because we generate $2^n$ subsets and for each subset, we potentially iterate over all $n$ elements to calculate the XOR.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input array, because we only use a constant amount of space to store the current subset's XOR and the total sum.
> - **Optimality proof:** The time complexity is optimal because generating all subsets of an array and calculating their XOR totals inherently requires exponential time complexity due to the nature of subset generation. The space complexity is optimal because we only need to keep track of a few variables, regardless of the size of the input.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Bit manipulation, subset generation, and XOR operation.
- Problem-solving patterns identified: Using bit manipulation to efficiently generate all subsets of an array.
- Optimization techniques learned: Calculating the XOR of each subset in linear time with respect to the size of the subset.
- Similar problems to practice: Problems involving subset generation, bit manipulation, and XOR operations.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly generating subsets or calculating the XOR of subsets.
- Edge cases to watch for: Handling empty arrays or arrays with duplicate elements.
- Performance pitfalls: Using inefficient algorithms for subset generation or XOR calculation.
- Testing considerations: Thoroughly testing the solution with various input cases, including edge cases.