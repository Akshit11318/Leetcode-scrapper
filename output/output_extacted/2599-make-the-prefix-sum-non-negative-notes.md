## Make the Prefix Sum Non-Negative
**Problem Link:** https://leetcode.com/problems/make-the-prefix-sum-non-negative/description

**Problem Statement:**
- Input: An array of integers `nums`.
- Output: The minimum number of operations required to make all prefix sums non-negative.
- Key requirements:
  - In one operation, you can add 1 to any element of `nums`.
- Edge cases:
  - The input array can be empty.
  - All elements in the array can be non-negative, requiring no operations.
- Example test cases:
  - Input: `nums = [3,-4,5,1,-2,4]`
    - Output: `3`
    - Explanation: We can add 1 to `nums[1]`, `nums[4]`, and `nums[5]` to get `[3, -3, 5, 1, -1, 4]`. Now, all prefix sums are non-negative.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of adding 1 to elements to make all prefix sums non-negative.
- Step-by-step breakdown:
  1. Generate all possible combinations of adding 1 to elements in `nums`.
  2. For each combination, calculate the prefix sums.
  3. Check if all prefix sums are non-negative.
  4. If they are, count the number of operations performed to achieve this.
- Why this approach comes to mind first: It's a straightforward, exhaustive search approach that guarantees finding the minimum number of operations if the search space is small enough.

```cpp
#include <vector>
#include <algorithm>
using namespace std;

int minOperations(vector<int>& nums) {
    int n = nums.size();
    int minOps = INT_MAX;
    
    // Generate all possible combinations of adding 1 to elements
    for (int mask = 0; mask < (1 << n); mask++) {
        vector<int> temp = nums;
        int ops = 0;
        
        // Apply the current combination to temp
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i))) {
                temp[i]++;
                ops++;
            }
        }
        
        // Calculate prefix sums and check if all are non-negative
        int prefixSum = 0;
        bool allNonNegative = true;
        for (int i = 0; i < n; i++) {
            prefixSum += temp[i];
            if (prefixSum < 0) {
                allNonNegative = false;
                break;
            }
        }
        
        // Update minOps if all prefix sums are non-negative
        if (allNonNegative) {
            minOps = min(minOps, ops);
        }
    }
    
    return minOps == INT_MAX ? 0 : minOps;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the size of `nums`. This is because we generate $2^n$ combinations and for each, we perform $O(n)$ work to calculate prefix sums and check if they are non-negative.
> - **Space Complexity:** $O(n)$, for storing the temporary array `temp`.
> - **Why these complexities occur:** The brute force approach involves an exhaustive search through all possible combinations of adding 1 to elements, leading to exponential time complexity. The space complexity is linear because we only need to store one additional array of the same size as the input.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: We can use a single pass through the array to keep track of the minimum operations needed to keep the prefix sum non-negative. We maintain a variable `minOps` to store the minimum operations needed so far and `prefixSum` to store the current prefix sum.
- Detailed breakdown:
  1. Initialize `minOps` to 0 and `prefixSum` to 0.
  2. Iterate through `nums`. For each element:
    - Update `prefixSum` by adding the current element.
    - If `prefixSum` becomes negative, increment `minOps` by the absolute value of `prefixSum` and reset `prefixSum` to 0.
  3. Return `minOps`.
- Proof of optimality: This approach is optimal because it ensures that the prefix sum never goes below 0 by adding the minimum number of operations necessary to keep it non-negative. It does this in a single pass, avoiding unnecessary work.

```cpp
int minOperations(vector<int>& nums) {
    int minOps = 0;
    int prefixSum = 0;
    
    for (int num : nums) {
        prefixSum += num;
        if (prefixSum < 0) {
            minOps += abs(prefixSum);
            prefixSum = 0;
        }
    }
    
    return minOps;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of `nums`. This is because we make a single pass through the array.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store `minOps` and `prefixSum`.
> - **Optimality proof:** This approach is optimal because it uses the minimum number of operations necessary to keep the prefix sum non-negative. It does so in linear time, which is the best we can achieve since we must at least read the input once.

---

### Final Notes

**Learning Points:**
- The importance of identifying the minimum operations needed to achieve a certain condition (non-negative prefix sums).
- How to use a single pass through an array to solve problems that involve prefix sums or similar accumulative conditions.
- The concept of maintaining a running sum (`prefixSum`) and adjusting it based on the current element and the operations performed (`minOps`).

**Mistakes to Avoid:**
- Not considering the use of a single pass through the array, leading to more complex and less efficient solutions.
- Failing to recognize that the problem can be solved by maintaining a running sum and adjusting it based on the minimum operations needed to keep it non-negative.
- Overlooking the importance of handling edge cases, such as an empty input array or an array with all non-negative elements.