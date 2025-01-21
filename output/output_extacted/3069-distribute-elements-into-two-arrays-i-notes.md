## Distribute Elements into Two Arrays I
**Problem Link:** https://leetcode.com/problems/distribute-elements-into-two-arrays-i/description

**Problem Statement:**
- Input: Two arrays `nums` of integers.
- Constraints: `2 <= nums.length <= 10^5`, `1 <= nums[i] <= 10^5`.
- Expected Output: Determine if it's possible to distribute the elements of `nums` into two arrays `a` and `b` such that `a[0] + a[1] + ... + a[a.length - 1] == b[0] + b[1] + ... + b[b.length - 1]`.
- Key Requirements: Find a way to partition `nums` into two arrays with equal sums.
- Example Test Cases:
  - Input: `nums = [1,2,3,4,5]`
    - Output: `True`
    - Explanation: We can distribute the elements into two arrays like this: `[1, 3, 5]` and `[2, 4]`.
  - Input: `nums = [1,1,1,1,1]`
    - Output: `True`
    - Explanation: We can distribute the elements into two arrays like this: `[1, 1, 1]` and `[1, 1]`.

---

### Brute Force Approach
**Explanation:**
- The initial thought process involves generating all possible subsets of the input array `nums` and checking if any subset has a sum equal to the sum of its complement.
- This approach involves using bit manipulation to generate all subsets.

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    bool canDistributeElements(vector<int>& nums) {
        int n = nums.size();
        int totalSum = 0;
        for (int num : nums) totalSum += num;
        
        if (totalSum % 2 != 0) return false;
        int targetSum = totalSum / 2;
        
        vector<bool> dp(targetSum + 1, false);
        dp[0] = true;
        
        for (int num : nums) {
            for (int i = targetSum; i >= num; i--) {
                if (dp[i - num]) dp[i] = true;
            }
        }
        
        return dp[targetSum];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times targetSum)$, where $n$ is the number of elements in `nums` and `targetSum` is the target sum we are trying to achieve. The reason for this complexity is the nested loop structure.
> - **Space Complexity:** $O(targetSum)$, for storing the dynamic programming table `dp`.
> - **Why these complexities occur:** The time complexity occurs because we are iterating over each number in `nums` and for each number, we are iterating from `targetSum` down to `num`. The space complexity occurs because we need to store the dynamic programming table `dp` of size `targetSum + 1`.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight here is to recognize this as a classic `0/1 Knapsack Problem`, where we are trying to find a subset of `nums` that sums up to `targetSum`.
- We use dynamic programming to solve this problem efficiently.
- The dynamic programming table `dp` is used to store whether it is possible to achieve a sum `i` using the first `j` numbers.

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    bool canDistributeElements(vector<int>& nums) {
        int n = nums.size();
        int totalSum = 0;
        for (int num : nums) totalSum += num;
        
        if (totalSum % 2 != 0) return false;
        int targetSum = totalSum / 2;
        
        vector<bool> dp(targetSum + 1, false);
        dp[0] = true;
        
        for (int num : nums) {
            for (int i = targetSum; i >= num; i--) {
                if (dp[i - num]) dp[i] = true;
            }
        }
        
        return dp[targetSum];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times targetSum)$, where $n$ is the number of elements in `nums` and `targetSum` is the target sum we are trying to achieve.
> - **Space Complexity:** $O(targetSum)$, for storing the dynamic programming table `dp`.
> - **Optimality proof:** This is the optimal solution because it uses dynamic programming to solve the problem in the most efficient way possible, with a time complexity that is linear with respect to the input size and the target sum.

---

### Final Notes

**Learning Points:**
- The `0/1 Knapsack Problem` is a classic problem in computer science and operations research that involves finding the optimal way to pack a set of items of different sizes and values into a knapsack of limited capacity.
- Dynamic programming is a powerful technique for solving problems that have overlapping subproblems and optimal substructure.
- The problem can be solved using a dynamic programming approach with a time complexity of $O(n \times targetSum)$.

**Mistakes to Avoid:**
- Not checking if the total sum is even before trying to find a subset with a sum equal to half of the total sum.
- Not using dynamic programming to solve the problem, which can lead to an exponential time complexity.
- Not handling edge cases, such as an empty input array or an array with a single element.