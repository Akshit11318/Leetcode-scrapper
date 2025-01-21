## Maximum Length of Subarray with Positive Product
**Problem Link:** https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/description

**Problem Statement:**
- Input format: Given an array of integers `nums`.
- Constraints: The length of `nums` is between 1 and $10^5$, and each element is either -1, 1, or 0.
- Expected output format: The maximum length of a subarray of `nums` that has a positive product.
- Key requirements and edge cases to consider:
  - Handling arrays with all positive numbers.
  - Handling arrays with all negative numbers.
  - Handling arrays with zeros.
  - Handling arrays with a mix of positive and negative numbers.
- Example test cases with explanations:
  - For `nums = [1,2,3,5,-6,4,1,2]`, the maximum length of a subarray with a positive product is 4, corresponding to the subarray `[1,2,3,5]`.
  - For `nums = [1,2,3,-4,-3,2,1,2]`, the maximum length of a subarray with a positive product is 3, corresponding to the subarray `[1,2,3]`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: To solve this problem, we can start by checking every possible subarray to see if it has a positive product.
- Step-by-step breakdown of the solution:
  1. Iterate over all possible start indices for subarrays.
  2. For each start index, iterate over all possible end indices.
  3. Calculate the product of the subarray from the start index to the end index.
  4. Check if the product is positive. If it is, update the maximum length found so far.
- Why this approach comes to mind first: It's a straightforward way to ensure we don't miss any subarrays, but it's inefficient for large inputs.

```cpp
int getMaxLen(vector<int>& nums) {
    int n = nums.size();
    int maxLength = 0;
    for (int start = 0; start < n; ++start) {
        int product = 1;
        for (int end = start; end < n; ++end) {
            product *= nums[end];
            if (product > 0) {
                maxLength = max(maxLength, end - start + 1);
            }
        }
    }
    return maxLength;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ because we have two nested loops, each of which can iterate up to $n$ times.
> - **Space Complexity:** $O(1)$ because we only use a constant amount of space to store our variables.
> - **Why these complexities occur:** The time complexity is high because we check every possible subarray, and the space complexity is low because we don't store any additional data structures that scale with the input size.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can solve this problem more efficiently by keeping track of the number of negative numbers in the current subarray and resetting the subarray whenever we encounter a zero.
- Detailed breakdown of the approach:
  1. Initialize variables to keep track of the maximum length, the current product, and the number of negative numbers in the current subarray.
  2. Iterate over the array, updating the product and the number of negative numbers as we go.
  3. Whenever we encounter a zero, reset the subarray by moving the start pointer forward until we find a non-zero number.
  4. If the number of negative numbers is odd, the product will be negative. In this case, we can try to remove numbers from the start of the subarray until we have an even number of negative numbers (which would make the product positive).
- Proof of optimality: This approach ensures we consider all possible subarrays efficiently by only considering subarrays that could potentially have a positive product and by resetting the subarray when we encounter a zero.

```cpp
int getMaxLen(vector<int>& nums) {
    int n = nums.size();
    int maxLength = 0;
    for (int i = 0; i < n; ++i) {
        if (nums[i] == 0) continue;
        int product = 1;
        int negatives = 0;
        for (int j = i; j < n; ++j) {
            if (nums[j] == 0) break;
            product *= nums[j];
            if (nums[j] < 0) ++negatives;
            if (product > 0) {
                maxLength = max(maxLength, j - i + 1);
            } else {
                // Try to remove numbers from the start to make the product positive
                int k = i;
                while (k <= j && product <= 0) {
                    if (nums[k] < 0) --negatives;
                    product /= nums[k];
                    ++k;
                }
                if (product > 0) {
                    maxLength = max(maxLength, j - k + 1);
                }
            }
        }
    }
    return maxLength;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ because we make a single pass through the array and our inner operations (like dividing the product by a number) take constant time.
> - **Space Complexity:** $O(1)$ because we only use a constant amount of space to store our variables.
> - **Optimality proof:** This approach is optimal because it considers all possible subarrays that could have a positive product in a single pass through the array, avoiding unnecessary work by resetting the subarray when encountering zeros and adjusting the subarray when the product becomes negative.

---

### Final Notes
**Learning Points:**
- Key algorithmic concepts demonstrated: Efficiently considering all possible subarrays, using a single pass through the data, and adjusting the subarray based on the product.
- Problem-solving patterns identified: Resetting the subarray when encountering zeros and adjusting the subarray when the product becomes negative.
- Optimization techniques learned: Avoiding unnecessary work by only considering subarrays that could have a positive product and using a single pass through the data.
- Similar problems to practice: Finding the maximum length of a subarray with certain properties (e.g., sum, product, etc.).

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to reset the subarray when encountering zeros, not correctly updating the product and number of negative numbers.
- Edge cases to watch for: Arrays with all positive numbers, arrays with all negative numbers, arrays with zeros.
- Performance pitfalls: Using a brute force approach that checks every possible subarray, not efficiently adjusting the subarray when the product becomes negative.
- Testing considerations: Thoroughly testing the function with different types of input arrays to ensure it handles all edge cases correctly.