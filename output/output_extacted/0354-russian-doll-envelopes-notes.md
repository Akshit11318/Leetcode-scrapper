## Russian Doll Envelopes

**Problem Link:** https://leetcode.com/problems/russian-doll-envelopes/description

**Problem Statement:**
- Input format: A 2D array `envelopes` where `envelopes[i] = [width, height]`.
- Constraints: `1 <= envelopes.length <= 100`, `1 <= width, height <= 10^5`.
- Expected output format: The maximum number of envelopes that can be Russian doll envelopes.
- Key requirements and edge cases to consider: 
    - An envelope can fit into another if and only if the width and height of the first are less than the width and height of the second.
    - The same envelope cannot be used more than once.
- Example test cases with explanations:
    - `envelopes = [[5,4],[6,4],[6,7],[2,3]]`, the maximum number of envelopes that can be Russian doll envelopes is 3 (`[2,3] => [5,4] => [6,7]`).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of envelopes and check if they can be Russian doll envelopes.
- Step-by-step breakdown of the solution:
    1. Generate all possible combinations of envelopes.
    2. For each combination, check if the envelopes can be Russian doll envelopes.
    3. Keep track of the maximum number of envelopes that can be Russian doll envelopes.
- Why this approach comes to mind first: It's a straightforward approach that tries all possible solutions.

```cpp
class Solution {
public:
    int maxEnvelopes(vector<vector<int>>& envelopes) {
        int n = envelopes.size();
        int maxEnvelopes = 0;
        for (int mask = 0; mask < (1 << n); mask++) {
            int count = 0;
            bool isValid = true;
            vector<pair<int, int>> currentEnvelopes;
            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) != 0) {
                    currentEnvelopes.push_back({envelopes[i][0], envelopes[i][1]});
                }
            }
            sort(currentEnvelopes.begin(), currentEnvelopes.end());
            for (int i = 0; i < currentEnvelopes.size(); i++) {
                bool canFit = false;
                for (int j = 0; j < i; j++) {
                    if (currentEnvelopes[j].first < currentEnvelopes[i].first && currentEnvelopes[j].second < currentEnvelopes[i].second) {
                        canFit = true;
                        break;
                    }
                }
                if (!canFit && i != 0) {
                    isValid = false;
                    break;
                }
                count++;
            }
            if (isValid) {
                maxEnvelopes = max(maxEnvelopes, count);
            }
        }
        return maxEnvelopes;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n^2)$, where $n$ is the number of envelopes. The reason is that we generate all possible combinations of envelopes ($2^n$) and for each combination, we check if the envelopes can be Russian doll envelopes ($n^2$).
> - **Space Complexity:** $O(n)$, where $n$ is the number of envelopes. The reason is that we store the current combination of envelopes.
> - **Why these complexities occur:** The brute force approach tries all possible combinations of envelopes, which leads to an exponential time complexity. The space complexity is linear because we only store the current combination of envelopes.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use dynamic programming to solve this problem. The idea is to sort the envelopes by width and then use a binary search to find the maximum number of envelopes that can be Russian doll envelopes.
- Detailed breakdown of the approach:
    1. Sort the envelopes by width.
    2. Initialize a dynamic programming array `dp` where `dp[i]` is the maximum number of envelopes that can be Russian doll envelopes ending with the `i-th` envelope.
    3. For each envelope, use a binary search to find the maximum number of envelopes that can be Russian doll envelopes ending with the previous envelopes.
    4. Update the dynamic programming array `dp` accordingly.
- Proof of optimality: The dynamic programming approach ensures that we consider all possible combinations of envelopes and find the maximum number of envelopes that can be Russian doll envelopes.

```cpp
class Solution {
public:
    int maxEnvelopes(vector<vector<int>>& envelopes) {
        int n = envelopes.size();
        sort(envelopes.begin(), envelopes.end(), [](vector<int>& a, vector<int>& b) {
            if (a[0] == b[0]) {
                return a[1] > b[1];
            }
            return a[0] < b[0];
        });
        vector<int> dp(n, 1);
        int maxEnvelopes = 1;
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (envelopes[j][0] < envelopes[i][0] && envelopes[j][1] < envelopes[i][1]) {
                    dp[i] = max(dp[i], dp[j] + 1);
                }
            }
            maxEnvelopes = max(maxEnvelopes, dp[i]);
        }
        return maxEnvelopes;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of envelopes. The reason is that we have two nested loops to update the dynamic programming array `dp`.
> - **Space Complexity:** $O(n)$, where $n$ is the number of envelopes. The reason is that we store the dynamic programming array `dp`.
> - **Optimality proof:** The dynamic programming approach ensures that we consider all possible combinations of envelopes and find the maximum number of envelopes that can be Russian doll envelopes.

---

### Alternative Approach

**Explanation:**
- Different perspective or technique: We can use a binary search approach to find the maximum number of envelopes that can be Russian doll envelopes.
- Unique trade-offs: The binary search approach has a time complexity of $O(n \log n)$, which is better than the dynamic programming approach for large inputs.
- Scenarios where this approach might be preferred: When the number of envelopes is very large, the binary search approach might be preferred due to its better time complexity.

```cpp
class Solution {
public:
    int maxEnvelopes(vector<vector<int>>& envelopes) {
        int n = envelopes.size();
        sort(envelopes.begin(), envelopes.end(), [](vector<int>& a, vector<int>& b) {
            if (a[0] == b[0]) {
                return a[1] > b[1];
            }
            return a[0] < b[0];
        });
        vector<int> dp;
        for (int i = 0; i < n; i++) {
            int index = lower_bound(dp.begin(), dp.end(), envelopes[i][1]) - dp.begin();
            if (index == dp.size()) {
                dp.push_back(envelopes[i][1]);
            } else {
                dp[index] = envelopes[i][1];
            }
        }
        return dp.size();
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of envelopes. The reason is that we use a binary search to find the maximum number of envelopes that can be Russian doll envelopes.
> - **Space Complexity:** $O(n)$, where $n$ is the number of envelopes. The reason is that we store the dynamic programming array `dp`.
> - **Trade-off analysis:** The binary search approach has a better time complexity than the dynamic programming approach for large inputs, but it has a higher constant factor due to the binary search.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, binary search.
- Problem-solving patterns identified: Using dynamic programming to solve problems with overlapping subproblems.
- Optimization techniques learned: Using binary search to improve the time complexity of the algorithm.
- Similar problems to practice: Other problems that involve dynamic programming and binary search, such as the Longest Increasing Subsequence problem.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases correctly, such as when the input array is empty.
- Edge cases to watch for: When the input array is empty, when the envelopes have the same width or height.
- Performance pitfalls: Using a brute force approach that has an exponential time complexity.
- Testing considerations: Testing the algorithm with different inputs, including edge cases, to ensure that it works correctly.