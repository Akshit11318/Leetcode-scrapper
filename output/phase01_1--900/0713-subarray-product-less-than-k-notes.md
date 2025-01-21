## Subarray Product Less Than K

**Problem Link:** https://leetcode.com/problems/subarray-product-less-than-k/description

**Problem Statement:**
- Input format: Given an array of integers `nums` and an integer `k`.
- Constraints: `1 <= nums.length <= 3 * 10^4`, `1 <= nums[i] <= 10^3`, `0 < k <= 10^6`.
- Expected output format: Return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than `k`.
- Key requirements and edge cases to consider:
  - Handling subarrays of varying lengths.
  - Considering the impact of large numbers in the array on the product.
  - Ensuring the product calculation does not overflow.
- Example test cases with explanations:
  - For `nums = [10, 5, 2, 6]` and `k = 100`, the output should be `8` because all possible subarrays have products less than `100`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To solve this problem, we can start by considering every possible subarray within the given array `nums`.
- Step-by-step breakdown of the solution:
  1. Generate all possible subarrays of `nums`.
  2. For each subarray, calculate the product of its elements.
  3. Check if the product is less than `k`.
  4. Count the number of subarrays that meet this condition.
- Why this approach comes to mind first: It's a straightforward method that ensures we consider every possible subarray, which aligns with the requirement of finding all contiguous subarrays with a product less than `k`.

```cpp
int numSubarrayProductLessThanK(vector<int>& nums, int k) {
    int count = 0;
    for (int i = 0; i < nums.size(); i++) {
        long long product = 1;
        for (int j = i; j < nums.size(); j++) {
            product *= nums[j];
            if (product < k) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of elements in `nums`. This is because for each element, we potentially iterate through the rest of the array.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input array, because we only use a constant amount of space to store the count and the product.
> - **Why these complexities occur:** The time complexity is quadratic due to the nested loop structure, which generates all possible subarrays. The space complexity is constant because we do not allocate any additional data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of recalculating the product for each subarray from scratch, we can use a sliding window approach. This approach maintains a running product of the current window and adjusts it as the window moves.
- Detailed breakdown of the approach:
  1. Initialize the window boundaries and the running product.
  2. Expand the window to the right by multiplying the running product by the next element.
  3. If the product exceeds or equals `k`, start shrinking the window from the left by dividing the running product by the leftmost element.
  4. For each position of the window, count the number of subarrays that can be formed within the current window that have a product less than `k`.
- Proof of optimality: This approach is optimal because it only requires a single pass through the array, avoiding the need for nested loops and thus reducing the time complexity to linear.

```cpp
int numSubarrayProductLessThanK(vector<int>& nums, int k) {
    if (k <= 1) return 0; // Because the product of any number with a number greater than 1 will be greater than k
    int left = 0;
    long long product = 1;
    int count = 0;
    for (int right = 0; right < nums.size(); right++) {
        product *= nums[right];
        while (product >= k && left <= right) {
            product /= nums[left];
            left++;
        }
        // The number of subarrays ending at 'right' with product less than k is 'right - left + 1'
        count += right - left + 1;
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in `nums`. This is because we make a single pass through the array.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the window boundaries and the product.
> - **Optimality proof:** The time complexity is linear because we only iterate through the array once, and each operation within the loop takes constant time. The space complexity is constant because we do not use any data structures that scale with the input size.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sliding window technique, maintaining a running product to avoid redundant calculations.
- Problem-solving patterns identified: Using a single pass through the data to achieve linear time complexity.
- Optimization techniques learned: Avoiding unnecessary recalculations by adjusting the window boundaries.
- Similar problems to practice: Other problems involving subarrays or sliding windows, such as maximum subarray sum or longest substring without repeating characters.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for division by zero, not handling edge cases like an empty input array.
- Edge cases to watch for: Handling arrays with large numbers, ensuring the product calculation does not overflow.
- Performance pitfalls: Using nested loops when a single pass is possible, not optimizing the calculation of the product within the window.
- Testing considerations: Testing with arrays of varying lengths, including arrays with a single element, and ensuring the function handles `k` values of 1 or less correctly.