## Maximum Value of an Ordered Triplet II
**Problem Link:** https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/description

**Problem Statement:**
- Input format: An array `nums` of integers.
- Constraints: The length of `nums` is between 3 and 10^5.
- Expected output format: The maximum possible value of an ordered triplet.
- Key requirements and edge cases to consider: The ordered triplet must be in the form of `(a, b, c)` where `a < b < c`, and all elements are distinct.
- Example test cases with explanations:
  - For `nums = [1,2,3,4,5]`, the maximum ordered triplet is `(1, 2, 5)` with a value of `1 * 2 * 5 = 10`.
  - For `nums = [5,5,5]`, the maximum ordered triplet is `(5, 5, 5)` but since all elements are the same, the function should return `0` as no valid triplet exists.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check every possible combination of three distinct numbers in the array to find the maximum product of an ordered triplet.
- Step-by-step breakdown of the solution:
  1. Generate all possible triplets from the array.
  2. For each triplet, check if the numbers are in ascending order and distinct.
  3. If they are, calculate the product of the triplet.
  4. Keep track of the maximum product found.
- Why this approach comes to mind first: It's a straightforward method to ensure all possibilities are considered.

```cpp
#include <vector>
#include <algorithm>

int maximumProduct(std::vector<int>& nums) {
    int maxProduct = 0;
    int n = nums.size();
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            for (int k = j + 1; k < n; ++k) {
                if (nums[i] < nums[j] && nums[j] < nums[k]) {
                    maxProduct = std::max(maxProduct, nums[i] * nums[j] * nums[k]);
                }
            }
        }
    }
    return maxProduct;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the number of elements in `nums`. This is because we have three nested loops, each iterating over the array.
> - **Space Complexity:** $O(1)$, not counting the space needed for the input and output, as we only use a constant amount of space to store the maximum product.
> - **Why these complexities occur:** The brute force approach has a high time complexity due to the generation and checking of all possible triplets, which grows cubically with the size of the input array.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We only need to consider the smallest, second smallest, second largest, and largest numbers in the array, as the maximum product of an ordered triplet can only be formed by these numbers.
- Detailed breakdown of the approach:
  1. Find the smallest, second smallest, largest, and second largest numbers in the array.
  2. Calculate the product of the smallest, second smallest, and largest numbers, and the product of the smallest, second largest, and largest numbers.
  3. Return the maximum of these two products.
- Proof of optimality: Since we are considering all possible combinations of the smallest and largest numbers, which are the only candidates for forming the maximum ordered triplet product, this approach is optimal.

```cpp
#include <vector>
#include <algorithm>

int maximumProduct(std::vector<int>& nums) {
    int min1 = INT_MAX, min2 = INT_MAX;
    int max1 = INT_MIN, max2 = INT_MIN;
    
    for (int num : nums) {
        if (num <= min1) {
            min2 = min1;
            min1 = num;
        } else if (num < min2) {
            min2 = num;
        }
        
        if (num >= max1) {
            max2 = max1;
            max1 = num;
        } else if (num > max2) {
            max2 = num;
        }
    }
    
    return std::max(min1 * min2 * max1, min1 * max2 * max1);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in `nums`. This is because we make a single pass through the array to find the required numbers.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the minimum and maximum numbers.
> - **Optimality proof:** This approach is optimal because it considers all possible combinations of the smallest and largest numbers in a single pass, resulting in a linear time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Finding maximum and minimum values, considering all possible combinations of these values.
- Problem-solving patterns identified: Looking for patterns that reduce the problem space, such as focusing on the smallest and largest numbers.
- Optimization techniques learned: Reducing the problem space by considering only the relevant elements.
- Similar problems to practice: Finding the maximum or minimum of other types of combinations, such as pairs or subsets.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing variables correctly, not considering edge cases.
- Edge cases to watch for: Empty arrays, arrays with duplicate elements.
- Performance pitfalls: Using brute force approaches for large inputs.
- Testing considerations: Test with arrays of varying sizes, including edge cases like empty arrays or arrays with duplicate elements.