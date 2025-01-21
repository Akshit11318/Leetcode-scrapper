## Count Subarrays with Score Less Than K
**Problem Link:** https://leetcode.com/problems/count-subarrays-with-score-less-than-k/description

**Problem Statement:**
- Input format: Given an array `nums` of integers and an integer `k`.
- Constraints: `1 <= nums.length <= 10^5`, `1 <= nums[i] <= 10^5`, and `1 <= k <= 10^9`.
- Expected output format: The number of subarrays in `nums` with a score less than `k`.
- Key requirements and edge cases to consider: The score of a subarray is the product of all its elements. We need to count all possible subarrays where this product is less than `k`.
- Example test cases with explanations:
  - `nums = [1, 2, 3]`, `k = 10`, the subarrays with score less than `k` are `[1]`, `[2]`, `[3]`, `[1, 2]`, `[2, 3]`, `[1, 2, 3]`, so the answer is `7`.
  - `nums = [10, 5, 2, 6]`, `k = 100`, the answer is `8`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: For each possible subarray, calculate the product of its elements and check if it's less than `k`.
- Step-by-step breakdown of the solution:
  1. Generate all possible subarrays.
  2. For each subarray, calculate the product of its elements.
  3. Check if the product is less than `k`.
  4. Count all subarrays where the product is less than `k`.
- Why this approach comes to mind first: It's straightforward and directly addresses the problem statement.

```cpp
int numSubarrayProductLessThanK(vector<int>& nums, int k) {
    int count = 0;
    for (int i = 0; i < nums.size(); i++) {
        long long product = 1; // Use long long to handle large products
        for (int j = i; j < nums.size(); j++) {
            product *= nums[j];
            if (product >= k) break; // No need to continue if product exceeds k
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the size of `nums`, because we are generating all possible subarrays.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input, because we are using a constant amount of space to store the count and product.
> - **Why these complexities occur:** The nested loops over the array to generate all subarrays result in quadratic time complexity. The space complexity is constant because we only use a fixed amount of space regardless of the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Since the product of elements in a subarray is increasing as we extend the subarray to the right, we can use a sliding window approach to efficiently find subarrays with product less than `k`.
- Detailed breakdown of the approach:
  1. Initialize two pointers, `left` and `right`, to the start of the array.
  2. Calculate the product of the subarray between `left` and `right`.
  3. If the product is less than `k`, we can extend the window to the right and count the subarrays ending at `right`.
  4. If the product is not less than `k`, we need to shrink the window from the left.
- Proof of optimality: This approach ensures we consider all possible subarrays exactly once and avoids unnecessary recalculations of products, making it more efficient than the brute force approach.

```cpp
int numSubarrayProductLessThanK(vector<int>& nums, int k) {
    if (k <= 1) return 0; // Because product of any number with 1 or less is not less than k
    int left = 0, product = 1, count = 0;
    for (int right = 0; right < nums.size(); right++) {
        product *= nums[right];
        while (product >= k && left <= right) {
            product /= nums[left];
            left++;
        }
        // Count subarrays ending at right with product less than k
        count += right - left + 1;
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of `nums`, because we process each element once.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input, because we use a constant amount of space.
> - **Optimality proof:** This is optimal because we only process each element once and avoid unnecessary recalculations of products, resulting in linear time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sliding window technique and the importance of avoiding unnecessary recalculations.
- Problem-solving patterns identified: Using a two-pointer technique to efficiently scan through the array and consider all possible subarrays.
- Optimization techniques learned: Avoiding unnecessary calculations and using a sliding window to reduce the time complexity.
- Similar problems to practice: Other problems involving subarrays or sliding window techniques, such as maximum sum subarray or longest substring without repeating characters.

**Mistakes to Avoid:**
- Common implementation errors: Not handling the case where `k` is less than or equal to 1, or not properly updating the product when shrinking the window.
- Edge cases to watch for: Empty input array, or array with a single element.
- Performance pitfalls: Using a brute force approach for large inputs, or not optimizing the calculation of products within the sliding window.
- Testing considerations: Ensure to test with various inputs, including edge cases like empty arrays or arrays with a single element, and large inputs to verify performance.