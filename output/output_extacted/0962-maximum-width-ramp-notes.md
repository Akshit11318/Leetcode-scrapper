## Maximum Width Ramp

**Problem Link:** https://leetcode.com/problems/maximum-width-ramp/description

**Problem Statement:**
- Input: An array of integers `nums`.
- Constraints: The length of `nums` is in the range `[2, 10^5]`.
- Expected Output: The maximum width of a ramp in the given array.
- Key Requirements: A ramp is defined as a sequence of elements where every element is either greater than or equal to the previous element, or every element is less than or equal to the previous element.
- Edge Cases: The input array may contain duplicate elements, and the length of the array can vary.

**Example Test Cases:**
- Example 1: Input: `nums = [6,0,8,2,1,5]`, Output: `4`, Explanation: The maximum width ramp is `[0, 2, 1, 5]`.
- Example 2: Input: `nums = [9,8,1,0,1,9,4,0,4,1]`, Output: `7`, Explanation: The maximum width ramp is `[9,8,1,0,1,9,4]`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to check every possible pair of elements in the array and calculate the width of the ramp.
- We iterate over the array and for each element, we check all the elements to its right to see if they form a ramp.
- We keep track of the maximum width ramp found so far.

```cpp
class Solution {
public:
    int maxWidthRamp(vector<int>& nums) {
        int n = nums.size();
        int maxWidth = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                bool isRamp = true;
                int prev = nums[i];
                for (int k = i + 1; k <= j; k++) {
                    if (nums[k] < prev) {
                        isRamp = false;
                        break;
                    }
                    prev = nums[k];
                }
                if (isRamp) {
                    maxWidth = max(maxWidth, j - i + 1);
                }
            }
        }
        return maxWidth;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the input array. This is because we have three nested loops.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum width and other variables.
> - **Why these complexities occur:** The brute force approach has high time complexity due to the nested loops, but it has low space complexity since we don't use any additional data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a stack to keep track of the indices of the elements in the array.
- We iterate over the array from left to right and push the indices of the elements onto the stack if the current element is greater than or equal to the top element of the stack.
- We then iterate over the array from right to left and pop the indices from the stack if the current element is less than or equal to the top element of the stack.
- We keep track of the maximum width ramp found so far.

```cpp
class Solution {
public:
    int maxWidthRamp(vector<int>& nums) {
        int n = nums.size();
        vector<int> stack;
        for (int i = 0; i < n; i++) {
            if (stack.empty() || nums[i] > nums[stack.back()]) {
                stack.push_back(i);
            }
        }
        int maxWidth = 0;
        for (int i = n - 1; i >= 0; i--) {
            while (!stack.empty() && nums[i] <= nums[stack.back()]) {
                int idx = stack.back();
                stack.pop_back();
                maxWidth = max(maxWidth, i - idx + 1);
            }
        }
        return maxWidth;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input array. This is because we make two passes over the array.
> - **Space Complexity:** $O(n)$, as in the worst case, we may push all indices onto the stack.
> - **Optimality proof:** This approach is optimal because we only make two passes over the array and use a stack to keep track of the indices, which reduces the time complexity from $O(n^3)$ to $O(n)$.

---

### Final Notes

**Learning Points:**
- The importance of using a stack to keep track of indices in the array.
- The technique of making two passes over the array to find the maximum width ramp.
- The optimization of using a single stack to reduce space complexity.

**Mistakes to Avoid:**
- Not checking for the edge case where the input array is empty.
- Not handling the case where the stack is empty before popping elements from it.
- Not keeping track of the maximum width ramp found so far.

**Similar Problems to Practice:**
- Finding the maximum sum subarray.
- Finding the longest increasing subsequence.
- Finding the maximum width of a binary tree.