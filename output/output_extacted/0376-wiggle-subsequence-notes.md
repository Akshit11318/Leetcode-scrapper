## Wiggle Subsequence
**Problem Link:** https://leetcode.com/problems/wiggle-subsequence/description

**Problem Statement:**
- Input format and constraints: Given an integer array `nums` of size `n`, find the length of the longest wiggle subsequence. A wiggle subsequence is a sequence where every pair of adjacent numbers is in strictly increasing or decreasing order.
- Expected output format: The length of the longest wiggle subsequence.
- Key requirements and edge cases to consider: 
    - The array may contain duplicates.
    - The wiggle subsequence can start with either an increasing or decreasing pair.
    - If the array is empty, return 0.
- Example test cases with explanations:
    - For `nums = [1, 17, 5, 10, 13, 15, 10, 5, 16, 8]`, the longest wiggle subsequence is `[1, 17, 10, 13, 10, 16, 8]` or `[1, 17, 5, 10, 13, 15, 10, 5, 16, 8]`, so the output is `7`.
    - For `nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]`, the longest wiggle subsequence is `[1, 2]`, `[2, 3]`, ..., `[8, 9]`, so the output is `2`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible subsequences of the given array and check if they are wiggle subsequences.
- Step-by-step breakdown of the solution:
    1. Generate all possible subsequences of the given array.
    2. For each subsequence, check if it is a wiggle subsequence by comparing adjacent elements.
    3. Keep track of the longest wiggle subsequence found so far.
- Why this approach comes to mind first: It is a straightforward approach that checks all possible subsequences.

```cpp
class Solution {
public:
    int wiggleMaxLength(vector<int>& nums) {
        int n = nums.size();
        int max_length = 0;
        for (int mask = 1; mask < (1 << n); mask++) {
            vector<int> subsequence;
            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) != 0) {
                    subsequence.push_back(nums[i]);
                }
            }
            if (isWiggleSubsequence(subsequence)) {
                max_length = max(max_length, (int)subsequence.size());
            }
        }
        return max_length;
    }

    bool isWiggleSubsequence(vector<int>& subsequence) {
        if (subsequence.size() < 2) {
            return true;
        }
        for (int i = 1; i < subsequence.size(); i++) {
            if (subsequence[i] == subsequence[i - 1]) {
                return false;
            }
        }
        bool increasing = subsequence[1] > subsequence[0];
        for (int i = 2; i < subsequence.size(); i++) {
            if (increasing && subsequence[i] < subsequence[i - 1]) {
                increasing = false;
            } else if (!increasing && subsequence[i] > subsequence[i - 1]) {
                increasing = true;
            }
        }
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the size of the input array. This is because we generate all possible subsequences and check each one.
> - **Space Complexity:** $O(n)$, where $n$ is the size of the input array. This is because we store the longest wiggle subsequence found so far.
> - **Why these complexities occur:** The time complexity is high because we generate all possible subsequences, and the space complexity is relatively low because we only store the longest wiggle subsequence found so far.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use dynamic programming to keep track of the longest wiggle subsequence ending at each position.
- Detailed breakdown of the approach:
    1. Initialize two arrays, `up` and `down`, to store the length of the longest wiggle subsequence ending at each position with the last pair being increasing or decreasing, respectively.
    2. Iterate through the array and update `up` and `down` based on the comparison of adjacent elements.
    3. The length of the longest wiggle subsequence is the maximum of the last elements of `up` and `down`.
- Proof of optimality: This approach has a time complexity of $O(n)$ and a space complexity of $O(n)$, which is optimal because we must at least read the input array.

```cpp
class Solution {
public:
    int wiggleMaxLength(vector<int>& nums) {
        int n = nums.size();
        if (n < 2) {
            return n;
        }
        vector<int> up(n, 1);
        vector<int> down(n, 1);
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[i] > nums[j]) {
                    up[i] = max(up[i], down[j] + 1);
                } else if (nums[i] < nums[j]) {
                    down[i] = max(down[i], up[j] + 1);
                }
            }
        }
        return max(*max_element(up.begin(), up.end()), *max_element(down.begin(), down.end()));
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the size of the input array. This is because we iterate through the array and for each element, we iterate through all previous elements.
> - **Space Complexity:** $O(n)$, where $n$ is the size of the input array. This is because we store the length of the longest wiggle subsequence ending at each position.
> - **Optimality proof:** This approach is optimal because we must at least read the input array, and the time complexity is $O(n^2)$, which is the best we can do using dynamic programming.

However, we can optimize the above code to have a time complexity of $O(n)$ by only keeping track of the maximum length of the wiggle subsequence ending at the current position with the last pair being increasing or decreasing.

```cpp
class Solution {
public:
    int wiggleMaxLength(vector<int>& nums) {
        int n = nums.size();
        if (n < 2) {
            return n;
        }
        int up = 1;
        int down = 1;
        for (int i = 1; i < n; i++) {
            if (nums[i] > nums[i - 1]) {
                up = down + 1;
            } else if (nums[i] < nums[i - 1]) {
                down = up + 1;
            }
        }
        return max(up, down);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of the input array. This is because we only iterate through the array once.
> - **Space Complexity:** $O(1)$, where $n$ is the size of the input array. This is because we only store a constant amount of space.
> - **Optimality proof:** This approach is optimal because we must at least read the input array, and the time complexity is $O(n)$, which is the best we can do.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming and iteration.
- Problem-solving patterns identified: Using dynamic programming to solve problems that have overlapping subproblems.
- Optimization techniques learned: Reducing the time complexity from $O(2^n \cdot n)$ to $O(n)$ by using dynamic programming.
- Similar problems to practice: Longest Increasing Subsequence, Longest Decreasing Subsequence.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as an empty input array.
- Edge cases to watch for: An input array with duplicate elements.
- Performance pitfalls: Using a brute force approach that has a high time complexity.
- Testing considerations: Testing the function with different input arrays, including edge cases.