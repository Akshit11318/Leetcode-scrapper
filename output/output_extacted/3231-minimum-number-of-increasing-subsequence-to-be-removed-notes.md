## Minimum Number of Increasing Subsequence to be Removed
**Problem Link:** https://leetcode.com/problems/minimum-number-of-increasing-subsequence-to-be-removed/description

**Problem Statement:**
- Input format and constraints: The problem requires finding the minimum number of increasing subsequences that need to be removed from a given array to make it non-increasing. The array is of size `n`, and each element is a distinct integer.
- Expected output format: The output should be the minimum number of increasing subsequences to be removed.
- Key requirements and edge cases to consider: The array can contain duplicate elements, and the increasing subsequences can be of any length. The goal is to minimize the number of subsequences to be removed.
- Example test cases with explanations:
  - Example 1: Input: `[5, 4, 3, 2, 1]`, Output: `0` (The array is already non-increasing, so no subsequences need to be removed.)
  - Example 2: Input: `[4, 3, 10, 9, 8]`, Output: `1` (Removing the subsequence `[10]` makes the array non-increasing.)

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible subsequences of the given array and check if they are increasing. If an increasing subsequence is found, remove it and check if the remaining array is non-increasing.
- Step-by-step breakdown of the solution:
  1. Generate all possible subsequences of the given array.
  2. Check if each subsequence is increasing.
  3. If an increasing subsequence is found, remove it and check if the remaining array is non-increasing.
- Why this approach comes to mind first: This approach is straightforward and checks all possible subsequences, ensuring that no increasing subsequences are missed.

```cpp
#include <iostream>
#include <vector>

int minSubseqToRemove(vector<int>& arr) {
    int n = arr.size();
    int minRemoved = INT_MAX;
    for (int mask = 0; mask < (1 << n); mask++) {
        vector<int> subseq;
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                subseq.push_back(arr[i]);
            }
        }
        if (isNonIncreasing(subseq)) {
            minRemoved = min(minRemoved, (int)subseq.size());
        }
    }
    return n - minRemoved;
}

bool isNonIncreasing(vector<int>& arr) {
    for (int i = 1; i < arr.size(); i++) {
        if (arr[i] > arr[i - 1]) {
            return false;
        }
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the size of the input array. This is because we generate all possible subsequences (which takes $O(2^n)$ time) and check if each subsequence is non-increasing (which takes $O(n)$ time).
> - **Space Complexity:** $O(n)$, where $n$ is the size of the input array. This is because we need to store the subsequence being checked.
> - **Why these complexities occur:** The brute force approach generates all possible subsequences, which leads to an exponential time complexity. The space complexity is linear because we only need to store the current subsequence being checked.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a greedy approach to find the longest non-increasing subsequence in the given array. The minimum number of increasing subsequences to be removed is then equal to the difference between the length of the array and the length of the longest non-increasing subsequence.
- Detailed breakdown of the approach:
  1. Initialize an array `dp` to store the length of the longest non-increasing subsequence ending at each position.
  2. Iterate through the array and for each element, find the maximum length of the non-increasing subsequence ending at that position.
  3. Update `dp` with the maximum length found.
  4. The minimum number of increasing subsequences to be removed is then `n - max(dp)`.
- Proof of optimality: The greedy approach ensures that we find the longest non-increasing subsequence, which minimizes the number of increasing subsequences to be removed.

```cpp
int minSubseqToRemove(vector<int>& arr) {
    int n = arr.size();
    vector<int> dp(n, 1);
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (arr[i] <= arr[j]) {
                dp[i] = max(dp[i], dp[j] + 1);
            }
        }
    }
    int maxLength = *max_element(dp.begin(), dp.end());
    return n - maxLength;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the size of the input array. This is because we use two nested loops to find the longest non-increasing subsequence.
> - **Space Complexity:** $O(n)$, where $n$ is the size of the input array. This is because we need to store the `dp` array.
> - **Optimality proof:** The greedy approach ensures that we find the longest non-increasing subsequence, which minimizes the number of increasing subsequences to be removed. The time complexity is quadratic because we use two nested loops, and the space complexity is linear because we only need to store the `dp` array.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Greedy approach, dynamic programming.
- Problem-solving patterns identified: Finding the longest non-increasing subsequence.
- Optimization techniques learned: Using a greedy approach to minimize the number of increasing subsequences to be removed.
- Similar problems to practice: Finding the longest increasing subsequence, finding the shortest path in a graph.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the `dp` array correctly, not updating the `dp` array correctly.
- Edge cases to watch for: Handling arrays with duplicate elements, handling arrays with a single element.
- Performance pitfalls: Using a brute force approach, not using a greedy approach.
- Testing considerations: Testing with arrays of different sizes, testing with arrays containing duplicate elements.