## Max Consecutive Ones

**Problem Link:** https://leetcode.com/problems/max-consecutive-ones/description

**Problem Statement:**
- Input: An array of integers `nums` containing only `0`s and `1`s.
- Constraints: `1 <= nums.length <= 10^4`, `nums[i]` is either `0` or `1`.
- Expected Output: The maximum number of consecutive `1`s in the array.
- Key Requirements: Find the maximum sequence of `1`s in the array.
- Edge Cases: Empty array, array with all `0`s, array with all `1`s, array with a single element.
- Example Test Cases:
  - `nums = [1,1,0,1,1,1]`, Expected Output: `3`
  - `nums = [1,1,1,1,0,1,1,1]`, Expected Output: `4`

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking every possible sequence of `1`s in the array to find the maximum consecutive ones.
- This approach involves using nested loops to compare each element with the next ones and count the consecutive `1`s.

```cpp
class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int maxCount = 0;
        for (int i = 0; i < nums.size(); i++) {
            int count = 0;
            for (int j = i; j < nums.size(); j++) {
                if (nums[j] == 1) {
                    count++;
                } else {
                    break;
                }
            }
            maxCount = max(maxCount, count);
        }
        return maxCount;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of elements in the array. This is because we are using nested loops to compare each element with the next ones.
> - **Space Complexity:** $O(1)$, as we are only using a constant amount of space to store the `maxCount` variable.
> - **Why these complexities occur:** The time complexity is quadratic due to the nested loops, and the space complexity is constant because we are not using any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a single pass through the array, keeping track of the current count of consecutive `1`s and the maximum count seen so far.
- We initialize two variables, `currentCount` and `maxCount`, to `0`. We then iterate through the array. If we encounter a `1`, we increment `currentCount`. If we encounter a `0`, we reset `currentCount` to `0`.
- At each step, we update `maxCount` if `currentCount` is greater than `maxCount`.

```cpp
class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int maxCount = 0;
        int currentCount = 0;
        for (int num : nums) {
            if (num == 1) {
                currentCount++;
                maxCount = max(maxCount, currentCount);
            } else {
                currentCount = 0;
            }
        }
        return maxCount;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array. This is because we are making a single pass through the array.
> - **Space Complexity:** $O(1)$, as we are only using a constant amount of space to store the `maxCount` and `currentCount` variables.
> - **Optimality proof:** This solution is optimal because we are only making a single pass through the array, and we are keeping track of the necessary information (the current count of consecutive `1`s and the maximum count seen so far) to find the maximum consecutive ones.

---

### Final Notes

**Learning Points:**
- The importance of using a single pass through the array to improve time complexity.
- Keeping track of the necessary information (current count and maximum count) to find the maximum consecutive ones.
- The use of `max` function to update the maximum count.

**Mistakes to Avoid:**
- Using nested loops, which can lead to quadratic time complexity.
- Not keeping track of the necessary information, which can lead to incorrect results.
- Not updating the maximum count correctly, which can lead to incorrect results.

By following the optimal approach, we can solve the problem efficiently and effectively.