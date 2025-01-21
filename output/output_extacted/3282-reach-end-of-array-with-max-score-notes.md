## Reach End of Array with Max Score
**Problem Link:** https://leetcode.com/problems/reach-end-of-array-with-max-score/description

**Problem Statement:**
- Given an array of integers `arr` and an integer `d`, the goal is to find the maximum score that can be achieved by reaching the end of the array.
- The score is calculated by summing up the elements of the array from the starting index to the ending index.
- The movement is restricted to moving one step to the right or `d` steps to the right.
- The input array `arr` is guaranteed to have at least one element, and `d` is a positive integer.
- The expected output is the maximum score that can be achieved.

**Key Requirements and Edge Cases:**
- The array `arr` can contain negative numbers.
- The value of `d` can be larger than the length of the array.
- The starting index is always 0.
- If it's impossible to reach the end of the array, return -1.

**Example Test Cases:**
- Input: `arr = [1,-1,-2,4,-7,3], d = 2`
  Output: `7`
  Explanation: The maximum score can be achieved by moving from index 0 to index 4 with a score of 1 + (-1) + (-2) + 4 = 2, and then moving from index 4 to index 6 with a score of -7 + 3 = -4. However, we can get a higher score by moving from index 0 to index 2 with a score of 1 + (-1) + (-2) = -2, and then moving from index 2 to index 4 with a score of 4, and finally moving from index 4 to index 6 with a score of -7 + 3 = -4. So the maximum score is 1 + (-1) + (-2) + 4 + (-7) + 3 = 7 - 7 + 3 = -7 + 3 = -4, but we can get a higher score by moving from index 0 to index 2 with a score of 1 + (-1) + (-2) = -2, and then moving from index 2 to index 5 with a score of 4 + (-7) = -3, and finally moving from index 5 to index 6 with a score of 3. So the maximum score is 1 + (-1) + (-2) + 4 + (-7) + 3 = 1 + (-1) + (-2) + 4 - 7 + 3 = -5 + 7 = 2.
- Input: `arr = [100,-1,-100,-1,100], d = 1`
  Output: `200`
  Explanation: The maximum score can be achieved by moving from index 0 to index 4 with a score of 100 + (-1) + (-100) + (-1) + 100 = 98.

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to try all possible movements from the starting index to the ending index.
- The brute force approach involves using recursion to explore all possible paths.
- The base case for the recursion is when the current index is equal to the length of the array, in which case the score is 0.
- For each index, we can either move one step to the right or `d` steps to the right.

```cpp
class Solution {
public:
    int maxResult(vector<int>& arr, int d) {
        int n = arr.size();
        vector<int> memo(n, INT_MIN);
        return maxResultHelper(arr, d, 0, memo);
    }
    
    int maxResultHelper(vector<int>& arr, int d, int index, vector<int>& memo) {
        if (index == arr.size()) {
            return 0;
        }
        if (memo[index] != INT_MIN) {
            return memo[index];
        }
        int maxScore = INT_MIN;
        for (int i = 1; i <= d; i++) {
            if (index + i < arr.size()) {
                maxScore = max(maxScore, arr[index] + maxResultHelper(arr, d, index + i, memo));
            }
        }
        memo[index] = maxScore;
        return maxScore;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot d)$, where $n$ is the length of the array and $d$ is the maximum number of steps that can be taken to the right. This is because in the worst case, we need to explore all possible paths from each index.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the array. This is because we need to store the memoization table to avoid redundant computation.
> - **Why these complexities occur:** The time complexity occurs because we are using recursion to explore all possible paths, and the space complexity occurs because we are using memoization to store the results of subproblems.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight that leads to the optimal solution is to use dynamic programming to store the maximum score that can be achieved at each index.
- We can use a dynamic programming table `dp` of size `n`, where `dp[i]` represents the maximum score that can be achieved at index `i`.
- We can fill up the `dp` table in a bottom-up manner by iterating from the last index to the first index.
- For each index `i`, we can calculate the maximum score that can be achieved by considering all possible movements from index `i` to the right.

```cpp
class Solution {
public:
    int maxResult(vector<int>& arr, int d) {
        int n = arr.size();
        vector<int> dp(n);
        dp[n - 1] = arr[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            dp[i] = arr[i];
            for (int j = 1; j <= d; j++) {
                if (i + j < n) {
                    dp[i] = max(dp[i], arr[i] + dp[i + j]);
                }
            }
        }
        return dp[0];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot d)$, where $n$ is the length of the array and $d$ is the maximum number of steps that can be taken to the right. This is because we are iterating from the last index to the first index and considering all possible movements for each index.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the array. This is because we are using a dynamic programming table to store the maximum score that can be achieved at each index.
> - **Optimality proof:** The optimal solution is achieved by using dynamic programming to store the maximum score that can be achieved at each index, which allows us to avoid redundant computation and achieve the optimal time complexity.

---

### Final Notes
**Learning Points:**
- The key algorithmic concept demonstrated in this problem is dynamic programming, which is used to store the maximum score that can be achieved at each index.
- The problem-solving pattern identified in this problem is to use dynamic programming to avoid redundant computation and achieve the optimal time complexity.
- The optimization technique learned in this problem is to use memoization to store the results of subproblems and avoid redundant computation.

**Mistakes to Avoid:**
- A common implementation error is to forget to initialize the dynamic programming table with the correct values.
- An edge case to watch for is when the input array is empty, in which case the function should return 0.
- A performance pitfall is to use a naive recursive approach without memoization, which can lead to exponential time complexity.
- A testing consideration is to test the function with different input arrays and values of `d` to ensure that it produces the correct output.