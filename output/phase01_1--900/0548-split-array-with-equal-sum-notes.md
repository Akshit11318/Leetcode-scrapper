## Split Array with Equal Sum
**Problem Link:** https://leetcode.com/problems/split-array-with-equal-sum/description

**Problem Statement:**
- Input: An integer array `nums` and an integer `m`.
- Output: Determine if it is possible to split the array into `m` non-empty subarrays such that the sum of elements in each subarray is equal.
- Constraints: `1 <= nums.length <= 10^5`, `1 <= m <= 50`.
- Key requirements: Find a way to divide the array into `m` parts with equal sums.
- Example test cases:
  - Input: `nums = [1,2,3,4,5,6,7,8,9], m = 3`, Output: `True` because `[1,2,3], [4,5,6], [7,8,9]` have equal sums.
  - Input: `nums = [1,2,3,4], m = 3`, Output: `False` because it is impossible to divide the array into 3 parts with equal sums.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves trying all possible ways to divide the array into `m` subarrays.
- Generate all possible combinations of subarrays.
- For each combination, check if the sum of elements in each subarray is equal.

```cpp
#include <vector>
#include <algorithm>

using namespace std;

bool splitArray(vector<int>& nums, int m) {
    int n = nums.size();
    vector<int> sums(m, 0);
    
    // Function to check if a combination of subarrays has equal sums
    auto check = [&](int idx, int part) {
        if (idx == n) return part == m;
        for (int i = idx; i < n; ++i) {
            sums[part] += nums[i];
            if (part == 0 || sums[part] == sums[part - 1]) {
                if (check(i + 1, part + 1)) return true;
            }
            sums[part] -= nums[i];
        }
        return false;
    };
    
    return check(0, 0);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, because in the worst case, we generate all possible subsets of the array.
> - **Space Complexity:** $O(m)$, for storing the sums of each subarray.
> - **Why these complexities occur:** The brute force approach involves generating all possible combinations of subarrays and checking their sums, leading to exponential time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to calculate the total sum of the array and then check if it is divisible by `m`.
- If the total sum is divisible by `m`, calculate the target sum for each subarray.
- Use a greedy approach to try to divide the array into subarrays with sums equal to the target sum.

```cpp
#include <vector>
#include <numeric>

using namespace std;

bool splitArray(vector<int>& nums, int m) {
    int n = nums.size();
    int totalSum = accumulate(nums.begin(), nums.end(), 0);
    
    if (totalSum % m != 0) return false; // Total sum must be divisible by m
    
    int targetSum = totalSum / m;
    int currentSum = 0;
    int parts = 0;
    
    for (int num : nums) {
        currentSum += num;
        if (currentSum == targetSum) {
            parts++;
            currentSum = 0;
        } else if (currentSum > targetSum) {
            return false; // Cannot divide the array into m parts with equal sums
        }
    }
    
    return parts == m;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space.
> - **Optimality proof:** This approach is optimal because it checks the divisibility of the total sum by `m` and then uses a single pass through the array to divide it into subarrays with equal sums.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: greedy approach, divisibility check.
- Problem-solving patterns identified: checking the total sum of the array, using a target sum to divide the array.
- Optimization techniques learned: avoiding unnecessary combinations, using a single pass through the array.
- Similar problems to practice: problems involving array partitioning, subset sums.

**Mistakes to Avoid:**
- Not checking the divisibility of the total sum by `m`.
- Not using a target sum to divide the array.
- Generating all possible combinations of subarrays.
- Not handling edge cases where the array cannot be divided into `m` parts with equal sums.