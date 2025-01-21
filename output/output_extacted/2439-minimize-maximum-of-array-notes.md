## Minimize Maximum of Array
**Problem Link:** https://leetcode.com/problems/minimize-maximum-of-array/description

**Problem Statement:**
- Input format: An array of integers `nums` and an integer `p`.
- Constraints: `2 <= nums.length <= 10^5` and `0 <= nums[i] <= 10^5` for all `i`, `0 <= p <= 10^5`.
- Expected output format: The minimum possible maximum value after at most `p` operations.
- Key requirements and edge cases to consider: 
  - The array can contain duplicate values.
  - The value of `p` can be less than, equal to, or greater than the number of operations needed to minimize the maximum value.
- Example test cases with explanations:
  - For `nums = [8, 3, 5, 2, 1, 7, 4, 6]` and `p = 4`, the minimum possible maximum value is `6`.
  - For `nums = [1, 1, 1, 1]` and `p = 0`, the minimum possible maximum value is `1`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of operations to minimize the maximum value.
- Step-by-step breakdown of the solution:
  1. Sort the array in descending order to prioritize the largest numbers.
  2. Use a recursive function to try all possible combinations of operations.
  3. For each number, try reducing it by 1 and recursively call the function.
  4. Keep track of the minimum maximum value found so far.
- Why this approach comes to mind first: It is a straightforward and intuitive way to solve the problem, but it is inefficient due to the high number of recursive calls.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int minimizeMaximum(std::vector<int>& nums, int p) {
    std::sort(nums.rbegin(), nums.rend());
    int minMax = nums[0];
    
    function<void(int, int, int)> dfs = [&](int idx, int p, int maxVal) {
        if (idx == nums.size() || p < 0) return;
        minMax = std::min(minMax, maxVal);
        
        // Try reducing the current number by 1
        if (p > 0) {
            int newNum = nums[idx] - 1;
            dfs(idx + 1, p - 1, std::max(maxVal, newNum));
        }
        
        // Try not reducing the current number
        dfs(idx + 1, p, std::max(maxVal, nums[idx]));
    };
    
    dfs(0, p, 0);
    return minMax;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n \log n)$ due to the recursive calls and sorting.
> - **Space Complexity:** $O(n)$ for the recursive call stack.
> - **Why these complexities occur:** The brute force approach tries all possible combinations of operations, resulting in an exponential number of recursive calls. The sorting step adds a factor of $n \log n$ to the time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: The problem can be solved using a binary search approach to find the minimum possible maximum value.
- Detailed breakdown of the approach:
  1. Define a helper function `check` that takes a potential maximum value `x` and checks if it is possible to achieve it by performing at most `p` operations.
  2. Use a binary search range `[1, max(nums)]` to find the minimum possible maximum value.
  3. For each potential maximum value `x`, call the `check` function to determine if it is possible to achieve it.
  4. Update the binary search range based on the result of the `check` function.
- Proof of optimality: The binary search approach ensures that the minimum possible maximum value is found in the fewest number of iterations.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

bool check(std::vector<int>& nums, int x, int p) {
    int operations = 0;
    for (int num : nums) {
        operations += std::max(0, num - x);
    }
    return operations <= p;
}

int minimizeMaximum(std::vector<int>& nums, int p) {
    int low = 0, high = *std::max_element(nums.begin(), nums.end());
    while (low < high) {
        int mid = (low + high) / 2;
        if (check(nums, mid, p)) {
            high = mid;
        } else {
            low = mid + 1;
        }
    }
    return low;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log m)$, where $m$ is the maximum value in the array.
> - **Space Complexity:** $O(1)$, excluding the input array.
> - **Optimality proof:** The binary search approach ensures that the minimum possible maximum value is found in the fewest number of iterations, resulting in an optimal time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Binary search, helper functions, and iterative approaches.
- Problem-solving patterns identified: Using a helper function to simplify the problem and applying binary search to find the optimal solution.
- Optimization techniques learned: Reducing the problem size using binary search and avoiding unnecessary computations.
- Similar problems to practice: Other optimization problems that involve finding the minimum or maximum value of a function.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly implementing the binary search algorithm or the helper function.
- Edge cases to watch for: Handling cases where the input array is empty or the value of `p` is negative.
- Performance pitfalls: Using inefficient algorithms or data structures that result in high time or space complexities.
- Testing considerations: Thoroughly testing the solution with different input cases and edge cases to ensure correctness.