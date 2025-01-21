## Maximum Product Difference Between Two Pairs

**Problem Link:** https://leetcode.com/problems/maximum-product-difference-between-two-pairs/description

**Problem Statement:**
- Input: An integer array `nums` containing at least two elements.
- Constraints: All elements in `nums` are non-negative integers.
- Expected Output: The maximum difference between the products of two pairs that can be formed from the array.
- Key Requirements and Edge Cases:
  - The array must contain at least two elements.
  - All elements are non-negative integers.
- Example Test Cases:
  - For `nums = [5,6,2,7,4]`, the output should be `34` because the maximum product difference between two pairs is `(7*6) - (2*4) = 34`.
  - For `nums = [4,2,5,9,7,4,8]`, the output should be `64` because the maximum product difference between two pairs is `(9*8) - (2*4) = 64`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves calculating all possible pairs from the given array, computing their products, and then finding the difference between each pair of products.
- Step-by-step breakdown:
  1. Generate all possible pairs of numbers from the array.
  2. Calculate the product of each pair.
  3. Find all possible differences between the products of two pairs.
  4. Identify the maximum difference found in step 3 as the solution.

```cpp
#include <vector>
#include <algorithm>
#include <iostream>

int maxProductDifference(std::vector<int>& nums) {
    int n = nums.size();
    int maxDiff = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            int product1 = nums[i] * nums[j];
            for (int k = 0; k < n; k++) {
                for (int l = k + 1; l < n; l++) {
                    if (i != k && i != l && j != k && j != l) {
                        int product2 = nums[k] * nums[l];
                        maxDiff = std::max(maxDiff, std::abs(product1 - product2));
                    }
                }
            }
        }
    }
    return maxDiff;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^4)$, where $n$ is the number of elements in the array. This is because we are using four nested loops to generate all pairs and calculate their products.
> - **Space Complexity:** $O(1)$, as we are not using any additional space that scales with input size.
> - **Why these complexities occur:** The brute force approach involves generating all possible pairs and then finding the differences between all pairs of products, leading to a high time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to realize that to maximize the product difference, we should look for the maximum product and the minimum product that can be formed from two pairs in the array.
- Since the array contains non-negative integers, the maximum product will be formed by the two largest numbers, and the minimum product will be formed by the two smallest numbers.
- Therefore, we can simply find the two largest and the two smallest numbers in the array and calculate the difference between their products.

```cpp
#include <vector>
#include <algorithm>
#include <iostream>

int maxProductDifference(std::vector<int>& nums) {
    int n = nums.size();
    std::sort(nums.begin(), nums.end());
    int maxProduct = nums[n-1] * nums[n-2];
    int minProduct = nums[0] * nums[1];
    return maxProduct - minProduct;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting operation.
> - **Space Complexity:** $O(1)$ if we consider the input array as part of the space complexity, otherwise $O(n)$ for sorting in place for some sorting algorithms.
> - **Optimality proof:** This is the best possible time complexity for this problem because we must at least examine each element once to find the maximum and minimum products, and sorting allows us to find these in $O(n \log n)$ time.

---

### Final Notes

**Learning Points:**
- The importance of identifying key insights that simplify the problem.
- How sorting can be used to efficiently find extreme values in an array.
- The trade-off between time and space complexity in different approaches.

**Mistakes to Avoid:**
- Not considering the properties of the input data (e.g., non-negative integers) that can simplify the problem.
- Overcomplicating the solution by not identifying the most critical aspects of the problem.
- Not optimizing the solution for time complexity when dealing with large inputs.