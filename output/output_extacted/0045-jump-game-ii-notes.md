## Jump Game II
**Problem Link:** https://leetcode.com/problems/jump-game-ii/description

**Problem Statement:**
- Input format: an array of non-negative integers `nums`, where `nums[i]` means the maximum jump length from index `i`.
- Constraints: `1 <= nums.length <= 10^4`, `0 <= nums[i] <= 10^5`.
- Expected output format: the minimum number of jumps to reach the last index.
- Key requirements: find the minimum number of jumps to reach the last index from the first index.
- Edge cases: if the input array is empty or only contains one element, return 0. If the input array is `null`, throw an exception.
- Example test cases:
  - Input: `[2,3,1,1,4]`, Output: `2`, Explanation: Jump 1 step from index 0 to index 1, then 3 steps to index 4.
  - Input: `[2,3,0,1,4]`, Output: `2`, Explanation: Jump 1 step from index 0 to index 1, then 1 step to index 2, then 1 step to index 3, then 1 step to index 4.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to try all possible jumps from each index and use recursion to find the minimum number of jumps.
- Step-by-step breakdown:
  1. Start from the first index.
  2. For each index, try all possible jumps.
  3. Recursively find the minimum number of jumps to reach the last index.
  4. Return the minimum number of jumps.

```cpp
class Solution {
public:
    int jump(vector<int>& nums) {
        return helper(nums, 0);
    }
    
    int helper(vector<int>& nums, int index) {
        if (index >= nums.size() - 1) {
            return 0;
        }
        
        int minJumps = INT_MAX;
        for (int i = 1; i <= nums[index]; i++) {
            minJumps = min(minJumps, 1 + helper(nums, index + i));
        }
        
        return minJumps;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the input array. This is because in the worst case, we try all possible jumps from each index, resulting in a quadratic time complexity.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input array. This is because of the recursive call stack.
> - **Why these complexities occur:** The brute force approach tries all possible jumps from each index, resulting in a high time complexity. The recursive call stack also contributes to the space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a greedy approach. We maintain a `maxReach` variable to keep track of the maximum reachable index.
- Step-by-step breakdown:
  1. Initialize `maxReach` to 0 and `jumps` to 0.
  2. Iterate through the input array.
  3. For each index, update `maxReach` to be the maximum of `maxReach` and the current index plus the jump length.
  4. If the current index is equal to `maxReach`, it means we need to make a jump. Increment `jumps` and update `maxReach` to be the current index.
  5. Return `jumps`.

```cpp
class Solution {
public:
    int jump(vector<int>& nums) {
        if (nums.size() <= 1) {
            return 0;
        }
        
        int maxReach = nums[0];
        int steps = nums[0];
        int jumps = 1;
        
        for (int i = 1; i < nums.size(); i++) {
            if (i == nums.size() - 1) {
                return jumps;
            }
            
            maxReach = max(maxReach, i + nums[i]);
            steps--;
            
            if (steps == 0) {
                jumps++;
                if (i >= maxReach) {
                    return -1; // handle the case where we cannot reach the end
                }
                steps = maxReach - i;
            }
        }
        
        return jumps;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input array. This is because we only iterate through the input array once.
> - **Space Complexity:** $O(1)$, where $n$ is the length of the input array. This is because we only use a constant amount of space to store the `maxReach`, `steps`, and `jumps` variables.
> - **Optimality proof:** The greedy approach is optimal because it always chooses the maximum reachable index, which minimizes the number of jumps.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: greedy approach, dynamic programming.
- Problem-solving patterns identified: using a `maxReach` variable to keep track of the maximum reachable index.
- Optimization techniques learned: using a greedy approach to minimize the number of jumps.
- Similar problems to practice: Jump Game, Jump Game III.

**Mistakes to Avoid:**
- Common implementation errors: not handling the case where we cannot reach the end.
- Edge cases to watch for: input array is empty or only contains one element.
- Performance pitfalls: using a brute force approach with high time complexity.
- Testing considerations: test the solution with different input arrays, including edge cases.