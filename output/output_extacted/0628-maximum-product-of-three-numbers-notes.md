## Maximum Product of Three Numbers
**Problem Link:** https://leetcode.com/problems/maximum-product-of-three-numbers/description

**Problem Statement:**
- Input format: An array of integers `nums`.
- Constraints: The array will have at least three elements.
- Expected output format: The maximum product of three numbers in the array.
- Key requirements and edge cases to consider: The product can be obtained from any three distinct elements in the array. Consider arrays with negative numbers, as two negative numbers multiplied together can give a positive product.
- Example test cases:
  - Input: `nums = [1,2,3]`, Output: `6` (Explanation: You can get the maximum product by multiplying 1*2*3 = 6).
  - Input: `nums = [1,2,3,4]`, Output: `24` (Explanation: You can get the maximum product by multiplying 1*3*4 = 12 or 2*3*4 = 24).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find the maximum product of three numbers, we can calculate the product of every possible combination of three distinct numbers in the array and keep track of the maximum product found.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of three distinct numbers from the array.
  2. For each combination, calculate the product of the three numbers.
  3. Keep track of the maximum product found so far.
- Why this approach comes to mind first: It's a straightforward approach that ensures we consider every possible combination, but it's inefficient for large arrays due to its high time complexity.

```cpp
#include <vector>
#include <algorithm>

int maximumProduct(std::vector<int>& nums) {
    int maxProduct = INT_MIN;
    int n = nums.size();
    
    // Generate all possible combinations of three numbers
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            for (int k = j + 1; k < n; k++) {
                // Calculate the product of the current combination
                int product = nums[i] * nums[j] * nums[k];
                // Update maxProduct if the current product is larger
                maxProduct = std::max(maxProduct, product);
            }
        }
    }
    
    return maxProduct;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the number of elements in the array. This is because we have three nested loops, each iterating over the array.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum product and the indices.
> - **Why these complexities occur:** The high time complexity is due to the brute force nature of generating all possible combinations of three numbers, which grows cubically with the size of the input array.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The maximum product of three numbers can be obtained by either multiplying the three largest numbers together or by multiplying the two smallest (most negative) numbers and the largest number. This is because two negative numbers multiplied together give a positive product.
- Detailed breakdown of the approach:
  1. Sort the array in ascending order.
  2. Calculate the product of the three largest numbers.
  3. Calculate the product of the two smallest numbers and the largest number.
  4. Return the maximum of these two products.
- Proof of optimality: This approach is optimal because it considers the two possible scenarios that can lead to the maximum product (three positive numbers or two negative numbers and one positive number) in linear time after sorting.

```cpp
#include <vector>
#include <algorithm>

int maximumProduct(std::vector<int>& nums) {
    std::sort(nums.begin(), nums.end());
    int n = nums.size();
    
    // Calculate the product of the three largest numbers
    int product1 = nums[n-1] * nums[n-2] * nums[n-3];
    // Calculate the product of the two smallest numbers and the largest number
    int product2 = nums[0] * nums[1] * nums[n-1];
    
    // Return the maximum of the two products
    return std::max(product1, product2);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of elements in the array. This is because we sort the array, which takes $O(n \log n)$ time in the worst case.
> - **Space Complexity:** $O(1)$ if we sort in-place, or $O(n)$ if we create a copy of the array to sort.
> - **Optimality proof:** This is the optimal approach because sorting allows us to find the necessary elements (smallest and largest) in a single pass, and then we only need to calculate two products, making the overall time complexity linear after sorting.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting, considering edge cases (negative numbers), and optimizing brute force approaches.
- Problem-solving patterns identified: Looking for patterns or properties of the data that can reduce the complexity of the problem.
- Optimization techniques learned: Sorting to find extreme values efficiently.
- Similar problems to practice: Finding the maximum or minimum of a set of numbers, considering the impact of negative numbers on products or sums.

**Mistakes to Avoid:**
- Common implementation errors: Not considering the impact of negative numbers, not handling edge cases properly.
- Edge cases to watch for: Empty arrays, arrays with less than three elements, arrays with all negative numbers.
- Performance pitfalls: Using brute force approaches for large inputs, not optimizing the algorithm based on the properties of the data.
- Testing considerations: Test with arrays of varying sizes, including edge cases like empty arrays or arrays with a single element.