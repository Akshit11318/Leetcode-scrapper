## Product of Array Except Self

**Problem Link:** https://leetcode.com/problems/product-of-array-except-self/description

**Problem Statement:**
- Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the numbers in the input array except `nums[i]`.
- Input format: Integer array `nums`
- Constraints: `2 <= nums.length <= 10^5`, `-30 <= nums[i] <= 30`
- Expected output format: Integer array `answer`
- Key requirements and edge cases to consider:
  - Handling zeros in the input array
  - Avoiding division to prevent precision loss
  - Ensuring the output array has the same length as the input array
- Example test cases with explanations:
  - For input `nums = [1,2,3,4]`, the output should be `[24,12,8,6]` because `24 = 2*3*4`, `12 = 1*3*4`, `8 = 1*2*4`, and `6 = 1*2*3`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Calculate the product of all numbers except the current one by iterating through the array for each element.
- Step-by-step breakdown of the solution:
  1. Initialize an output array `answer` of the same length as the input array `nums`.
  2. For each element `nums[i]` in the input array, calculate the product of all other numbers by iterating through the array again and multiplying all numbers except `nums[i]`.
  3. Store the calculated product in the corresponding index `i` of the output array `answer`.
- Why this approach comes to mind first: It directly addresses the problem statement by calculating the product of all other numbers for each element.

```cpp
vector<int> productExceptSelf(vector<int>& nums) {
    int n = nums.size();
    vector<int> answer(n, 1);
    
    for (int i = 0; i < n; i++) {
        int product = 1;
        for (int j = 0; j < n; j++) {
            if (i != j) {
                product *= nums[j];
            }
        }
        answer[i] = product;
    }
    
    return answer;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of elements in the input array, because for each element, we are iterating through the entire array again.
> - **Space Complexity:** $O(1)$, excluding the space required for the output array, because we are using a constant amount of space to store the product and indices.
> - **Why these complexities occur:** The nested loops cause the quadratic time complexity, and the need to store the output array results in additional space usage.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can calculate the prefix products (products of all numbers to the left of the current index) and suffix products (products of all numbers to the right of the current index) separately and then multiply them to get the product of all numbers except the current one.
- Detailed breakdown of the approach:
  1. Initialize two arrays, `prefix` and `suffix`, of the same length as the input array, to store the prefix and suffix products, respectively.
  2. Calculate the prefix products by iterating through the input array from left to right and multiplying the current prefix product by the current number.
  3. Calculate the suffix products by iterating through the input array from right to left and multiplying the current suffix product by the current number.
  4. Initialize the output array `answer` and calculate each element as the product of the corresponding prefix and suffix products.
- Proof of optimality: This approach avoids the need for nested loops and division, resulting in a linear time complexity.

```cpp
vector<int> productExceptSelf(vector<int>& nums) {
    int n = nums.size();
    vector<int> answer(n, 1);
    
    // Calculate prefix products
    for (int i = 1; i < n; i++) {
        answer[i] = answer[i - 1] * nums[i - 1];
    }
    
    // Calculate suffix products and update answer
    int suffixProduct = 1;
    for (int i = n - 1; i >= 0; i--) {
        answer[i] *= suffixProduct;
        suffixProduct *= nums[i];
    }
    
    return answer;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the input array, because we are iterating through the array twice: once for prefix products and once for suffix products.
> - **Space Complexity:** $O(1)$, excluding the space required for the output array, because we are using a constant amount of space to store the prefix and suffix products.
> - **Optimality proof:** This approach achieves a linear time complexity, which is optimal for this problem, as we must at least read the input array once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Prefix and suffix products, avoidance of division, and optimization of nested loops.
- Problem-solving patterns identified: Breaking down complex problems into simpler sub-problems and using auxiliary arrays to store intermediate results.
- Optimization techniques learned: Avoiding unnecessary computations and using iterative approaches instead of recursive ones.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect indexing, forgetting to handle edge cases, and using division instead of multiplication.
- Edge cases to watch for: Zeroes in the input array, negative numbers, and very large input arrays.
- Performance pitfalls: Using nested loops or recursive functions, which can lead to exponential time complexity.
- Testing considerations: Thoroughly testing the solution with various input cases, including edge cases and large input arrays.