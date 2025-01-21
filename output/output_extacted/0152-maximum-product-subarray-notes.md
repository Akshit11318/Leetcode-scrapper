## Maximum Product Subarray
**Problem Link:** https://leetcode.com/problems/maximum-product-subarray/description

**Problem Statement:**
- Input format and constraints: The input is an array of integers `nums`, where `1 <= nums.length <= 2 * 10^4` and `-10^5 <= nums[i] <= 10^5`. The task is to find the maximum product of a subarray within this array.
- Expected output format: The output should be the maximum product of a subarray, which can be a single element or a sequence of elements.
- Key requirements and edge cases to consider: The presence of negative numbers, which can flip the maximum product to a minimum and vice versa. Handling edge cases like an empty array or an array with a single element.
- Example test cases with explanations:
    - For `nums = [2,3,-2,4]`, the maximum product subarray is `[2,3,-2,4]`, which has a product of `6`.
    - For `nums = [-2,0,-1]`, the maximum product subarray is `[-1]`, which has a product of `-1`.

### Brute Force Approach

**Explanation:**
- Initial thought process: The most straightforward way to solve this problem is to generate all possible subarrays, calculate their products, and find the maximum one.
- Step-by-step breakdown of the solution:
    1. Initialize the maximum product found so far to negative infinity.
    2. Generate all possible subarrays using nested loops.
    3. For each subarray, calculate its product by multiplying all its elements.
    4. Update the maximum product if the current subarray's product is larger.
- Why this approach comes to mind first: It's a simple, intuitive approach that directly addresses the problem statement.

```cpp
int maxProduct(vector<int>& nums) {
    int n = nums.size();
    long long maxProductFound = LLONG_MIN;
    for (int i = 0; i < n; ++i) {
        long long product = 1;
        for (int j = i; j < n; ++j) {
            product *= nums[j];
            maxProductFound = max(maxProductFound, product);
        }
    }
    return (int)maxProductFound;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ because we have two nested loops, each potentially iterating over the entire array of size `n`.
> - **Space Complexity:** $O(1)$, not counting the input array, because we only use a constant amount of space to store the maximum product and the current product.
> - **Why these complexities occur:** The nested loops cause the quadratic time complexity, while the use of a fixed amount of variables leads to constant space complexity.

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Since the presence of a negative number can turn a maximum product into a minimum product and vice versa, we need to keep track of both the maximum and minimum product ending at each position.
- Detailed breakdown of the approach:
    1. Initialize `maxProduct` and `minProduct` to the first element of the array, and `result` (the maximum product found so far) to the first element.
    2. Iterate through the array starting from the second element. For each element:
        - Update `maxProduct` to be the maximum of the current element, the product of the current element and the previous `maxProduct`, and the product of the current element and the previous `minProduct`.
        - Update `minProduct` to be the minimum of the current element, the product of the current element and the previous `maxProduct`, and the product of the current element and the previous `minProduct`.
        - Update `result` if `maxProduct` is greater than `result`.
- Proof of optimality: This approach is optimal because it considers all possible subarrays and handles the impact of negative numbers in a single pass through the array.

```cpp
int maxProduct(vector<int>& nums) {
    if (nums.empty()) return 0;
    int n = nums.size();
    int maxProduct = nums[0], minProduct = nums[0], result = nums[0];
    for (int i = 1; i < n; ++i) {
        if (nums[i] < 0) swap(maxProduct, minProduct);
        maxProduct = max(nums[i], maxProduct * nums[i]);
        minProduct = min(nums[i], minProduct * nums[i]);
        result = max(result, maxProduct);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ because we make a single pass through the array.
> - **Space Complexity:** $O(1)$ because we only use a constant amount of space to store the maximum and minimum products, and the result.
> - **Optimality proof:** This solution is optimal because it achieves the best possible time complexity for this problem by only requiring a single pass through the array and considering the effect of negative numbers on the product.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, handling of negative numbers in product calculations.
- Problem-solving patterns identified: The need to consider all possible subarrays and the impact of negative numbers.
- Optimization techniques learned: Reducing the number of iterations by considering the properties of the problem, such as the effect of negative numbers.
- Similar problems to practice: Other dynamic programming problems, especially those involving arrays and sequences.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle edge cases like an empty array or not initializing variables correctly.
- Edge cases to watch for: The presence of zero in the array, which can reset the maximum and minimum product.
- Performance pitfalls: Using unnecessary nested loops or not considering the impact of negative numbers, leading to inefficient solutions.
- Testing considerations: Ensure to test with arrays containing negative numbers, zeros, and positive numbers, as well as edge cases like empty arrays or arrays with a single element.