## Apply Operations to Array to Maximize Sum of Squares
**Problem Link:** https://leetcode.com/problems/apply-operations-on-array-to-maximize-sum-of-squares/description

**Problem Statement:**
- Input: An integer array `nums`.
- Constraints: The length of `nums` is `n`, where `n` is an integer and `1 <= n <= 10^4`. Each element `nums[i]` is an integer, `0 <= nums[i] <= 10^4`.
- Expected output: The maximum possible sum of squares of `nums` after applying the given operations.
- Key requirements: For each element `nums[i]`, if `nums[i]` is odd, we can either keep it as is or subtract `1` from it and then square it. If `nums[i]` is even, we can either keep it as is or divide it by `2` and then square it.
- Example test cases:
    - Input: `nums = [1,2,3,4]`
    - Output: `47`
    - Explanation: We can transform the array into `[1,4,9,16]` and the sum of squares is `1 + 16 + 9 + 16 = 42`. However, a better transformation is to turn `1` into `0` (by subtracting `1`), `2` into `1` (by dividing by `2`), `3` into `2` (by subtracting `1`), and keep `4` as is. This gives us `[0,1,4,4]`, and the sum of squares is `0 + 1 + 16 + 16 = 33`. But the optimal solution involves understanding the impact of operations on the sum of squares directly.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of operations on each element and calculate the sum of squares for each combination.
- Step-by-step breakdown:
    1. Generate all possible combinations of operations for the array. For each element, decide whether to apply the operation (if applicable) or not.
    2. For each combination, apply the operations to the array elements.
    3. Calculate the sum of squares for the modified array.
    4. Keep track of the maximum sum of squares found.

```cpp
#include <vector>
#include <algorithm>
#include <cmath>

int maxSumOfSquares(std::vector<int>& nums) {
    int n = nums.size();
    int maxSum = 0;
    
    // Simulate all possible operations
    for (int mask = 0; mask < (1 << n); ++mask) {
        std::vector<int> modifiedNums = nums;
        for (int i = 0; i < n; ++i) {
            if ((mask & (1 << i)) && modifiedNums[i] % 2 == 0) {
                modifiedNums[i] /= 2;
            } else if ((mask & (1 << i)) && modifiedNums[i] % 2 == 1) {
                modifiedNums[i] -= 1;
            }
        }
        
        int sumOfSquares = 0;
        for (int num : modifiedNums) {
            sumOfSquares += num * num;
        }
        
        maxSum = std::max(maxSum, sumOfSquares);
    }
    
    return maxSum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the number of elements in the array. The reason is that we generate all possible combinations of operations (which is $2^n$) and for each combination, we apply the operations and calculate the sum of squares, which takes $O(n)$ time.
> - **Space Complexity:** $O(n)$, as we need to store the modified array for each combination.
> - **Why these complexities occur:** The brute force approach involves trying all possible combinations of operations, leading to exponential time complexity. The space complexity is linear because we only need to store one modified array at a time.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: For each element, we should decide whether applying the operation increases the sum of squares or not. If applying the operation increases the sum of squares, we apply it; otherwise, we do not.
- Detailed breakdown:
    1. For each odd number, subtracting `1` and then squaring it gives a larger result than keeping it as is and squaring it.
    2. For each even number, dividing it by `2` and then squaring it gives a smaller result than keeping it as is and squaring it.
    3. Therefore, we can decide for each number whether to apply the operation based on these rules.

```cpp
#include <vector>

int maxSumOfSquares(std::vector<int>& nums) {
    int sumOfSquares = 0;
    
    for (int num : nums) {
        if (num % 2 == 1) {
            sumOfSquares += (num - 1) * (num - 1);
        } else {
            sumOfSquares += num * num;
        }
    }
    
    return sumOfSquares;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array. We simply iterate through the array once.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the sum of squares and do not allocate any additional space that scales with input size.
> - **Optimality proof:** This approach is optimal because it makes the best decision for each element independently, maximizing the sum of squares. Any other approach would either make suboptimal decisions for some elements or involve unnecessary complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Greedy algorithms, decision-making based on local optimality.
- Problem-solving patterns identified: Breaking down problems into smaller, independent decisions.
- Optimization techniques learned: Making decisions based on the impact on the objective function (in this case, the sum of squares).
- Similar problems to practice: Other problems involving making decisions to maximize or minimize a quantity, such as scheduling or resource allocation problems.

**Mistakes to Avoid:**
- Common implementation errors: Failing to consider all possible decisions for each element, or incorrectly calculating the impact of each decision.
- Edge cases to watch for: Handling the case where the input array is empty, or where all elements are zero.
- Performance pitfalls: Using brute force approaches for problems that have more efficient solutions, leading to unnecessary time or space complexity.
- Testing considerations: Testing the function with a variety of inputs, including edge cases, to ensure it produces the correct output.