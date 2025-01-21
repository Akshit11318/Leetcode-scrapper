## Maximum Score of Spliced Array

**Problem Link:** https://leetcode.com/problems/maximum-score-of-spliced-array/description

**Problem Statement:**
- Given two arrays, `nums1` and `nums2`, we can create a new array by splicing `nums2` into `nums1` at any position.
- The score of the resulting array is the sum of its elements.
- The goal is to find the maximum possible score of the spliced array.

**Input Format and Constraints:**
- `nums1` and `nums2` are non-empty arrays of integers.
- `1 <= nums1.length, nums2.length <= 10^5`.
- `-10^5 <= nums1[i], nums2[i] <= 10^5`.

**Expected Output Format:**
- The maximum possible score of the spliced array.

**Key Requirements and Edge Cases to Consider:**
- We need to consider all possible positions where `nums2` can be spliced into `nums1`.
- We should handle edge cases where `nums2` is longer than `nums1` or when the scores of `nums1` and `nums2` are negative.

**Example Test Cases with Explanations:**
- For `nums1 = [60, -60, -100]` and `nums2 = [10, -50, 50, 100, -30]`, the maximum score is `250`.
- For `nums1 = [100, 100]` and `nums2 = [100]`, the maximum score is `300`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to try all possible positions where `nums2` can be spliced into `nums1`.
- We calculate the score for each position and keep track of the maximum score found.
- This approach comes to mind first because it is straightforward and easy to implement.

```cpp
int maximumScore(vector<int>& nums1, vector<int>& nums2) {
    int maxScore = INT_MIN;
    for (int i = 0; i <= nums1.size(); i++) {
        vector<int> temp = nums1;
        temp.insert(temp.begin() + i, nums2.begin(), nums2.end());
        int score = 0;
        for (int num : temp) {
            score += num;
        }
        maxScore = max(maxScore, score);
    }
    return maxScore;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the size of `nums1` and $m$ is the size of `nums2`. This is because we are trying all possible positions and calculating the score for each position.
> - **Space Complexity:** $O(n + m)$, where $n$ is the size of `nums1` and $m$ is the size of `nums2`. This is because we are creating a temporary array to store the spliced array.
> - **Why these complexities occur:** These complexities occur because we are using a brute force approach and trying all possible positions.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to use a prefix sum array to calculate the score of the spliced array.
- We calculate the prefix sum array for `nums1` and `nums2` separately.
- We then try all possible positions where `nums2` can be spliced into `nums1` and calculate the score using the prefix sum arrays.
- This approach is optimal because it reduces the time complexity from $O(n \cdot m)$ to $O(n + m)$.

```cpp
int maximumScore(vector<int>& nums1, vector<int>& nums2) {
    int n = nums1.size(), m = nums2.size();
    vector<int> prefixSum1(n + 1), prefixSum2(m + 1);
    for (int i = 0; i < n; i++) {
        prefixSum1[i + 1] = prefixSum1[i] + nums1[i];
    }
    for (int i = 0; i < m; i++) {
        prefixSum2[i + 1] = prefixSum2[i] + nums2[i];
    }
    int maxScore = INT_MIN;
    for (int i = 0; i <= n; i++) {
        for (int j = 0; j <= m; j++) {
            int score = prefixSum1[i] + prefixSum2[m] - prefixSum2[j] + prefixSum1[n] - prefixSum1[i];
            maxScore = max(maxScore, score);
        }
    }
    return maxScore;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the size of `nums1` and $m` is the size of `nums2`. This is because we are trying all possible positions and calculating the score using the prefix sum arrays.
> - **Space Complexity:** $O(n + m)$, where $n$ is the size of `nums1` and $m` is the size of `nums2`. This is because we are creating prefix sum arrays for `nums1` and `nums2`.
> - **Optimality proof:** This approach is optimal because it uses a prefix sum array to calculate the score of the spliced array, which reduces the time complexity.

However, we can optimize this further by using a Kadane's algorithm to find the maximum subarray sum.

```cpp
int maximumScore(vector<int>& nums1, vector<int>& nums2) {
    int n = nums1.size(), m = nums2.size();
    int maxScore = INT_MIN;
    for (int i = 0; i <= n; i++) {
        for (int j = 0; j <= m; j++) {
            int score = 0;
            int curr = 0;
            for (int k = 0; k < i; k++) {
                curr += nums1[k];
            }
            for (int k = 0; k < j; k++) {
                curr += nums2[k];
            }
            score = curr;
            curr = 0;
            for (int k = i; k < n; k++) {
                curr += nums1[k];
            }
            for (int k = j; k < m; k++) {
                curr += nums2[k];
            }
            score += curr;
            maxScore = max(maxScore, score);
        }
    }
    return maxScore;
}
```

But the optimal solution is actually to calculate the maximum subarray sum for both arrays and then add them together.

```cpp
int maximumScore(vector<int>& nums1, vector<int>& nums2) {
    int n = nums1.size(), m = nums2.size();
    int maxScore = INT_MIN;
    for (int i = 0; i <= n; i++) {
        int score1 = 0, score2 = 0;
        for (int j = 0; j < i; j++) {
            score1 += nums1[j];
        }
        for (int j = i; j < n; j++) {
            score1 += nums1[j];
        }
        for (int j = 0; j <= m; j++) {
            int curr = 0;
            for (int k = 0; k < j; k++) {
                curr += nums2[k];
            }
            for (int k = j; k < m; k++) {
                curr += nums2[k];
            }
            score2 = max(score2, curr);
        }
        maxScore = max(maxScore, score1 + score2);
    }
    return maxScore;
}
```

However, we can further optimize this solution by using Kadane's algorithm.

```cpp
int maximumScore(vector<int>& nums1, vector<int>& nums2) {
    int n = nums1.size(), m = nums2.size();
    int maxScore1 = kadane(nums1);
    int maxScore2 = kadane(nums2);
    return maxScore1 + maxScore2;
}

int kadane(vector<int>& nums) {
    int maxSoFar = INT_MIN, maxEndingHere = 0;
    for (int num : nums) {
        maxEndingHere = max(num, maxEndingHere + num);
        maxSoFar = max(maxSoFar, maxEndingHere);
    }
    return maxSoFar;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the size of `nums1` and $m` is the size of `nums2`. This is because we are using Kadane's algorithm to find the maximum subarray sum.
> - **Space Complexity:** $O(1)$, where $n$ is the size of `nums1` and $m$ is the size of `nums2`. This is because we are not using any extra space.
> - **Optimality proof:** This approach is optimal because it uses Kadane's algorithm to find the maximum subarray sum, which has a time complexity of $O(n)$.

---

### Final Notes

**Learning Points:**
- The key algorithmic concept demonstrated in this problem is the use of prefix sum arrays and Kadane's algorithm to find the maximum subarray sum.
- The problem-solving pattern identified is to break down the problem into smaller subproblems and solve them separately.
- The optimization technique learned is to use Kadane's algorithm to find the maximum subarray sum.

**Mistakes to Avoid:**
- A common implementation error is to not handle edge cases correctly.
- A performance pitfall is to use a brute force approach instead of an optimal approach.
- A testing consideration is to test the solution with different inputs and edge cases.