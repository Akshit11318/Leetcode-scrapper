## Longest Common Subsequence Between Sorted Arrays

**Problem Link:** https://leetcode.com/problems/longest-common-subsequence-between-sorted-arrays/description

**Problem Statement:**
- Input: Two sorted arrays `arr1` and `arr2` of integers.
- Output: The length of the longest common subsequence between the two arrays.
- Key requirements: The subsequence must be increasing.
- Edge cases: Empty arrays, arrays of different lengths, arrays with duplicate elements.

Example test cases:
- `arr1 = [1, 3, 5, 7], arr2 = [2, 3, 5, 6]`, output: `2` (because `[3, 5]` is the longest common increasing subsequence).
- `arr1 = [1, 2, 3, 4], arr2 = [1, 2, 3, 4]`, output: `4` (because the arrays are identical).
- `arr1 = [1, 3, 5], arr2 = [2, 4, 6]`, output: `0` (because there is no common element).

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking every possible subsequence of `arr1` to see if it exists in `arr2` and is increasing.
- This involves generating all possible subsequences of `arr1`, then for each subsequence, checking if it exists in `arr2` in an increasing order.

```cpp
#include <vector>
#include <algorithm>

int findLength(std::vector<int>& arr1, std::vector<int>& arr2) {
    int n = arr1.size();
    int m = arr2.size();
    int maxLength = 0;
    
    // Generate all possible subsequences of arr1
    for (int mask = 1; mask < (1 << n); ++mask) {
        std::vector<int> subsequence;
        for (int i = 0; i < n; ++i) {
            if ((mask & (1 << i))) {
                subsequence.push_back(arr1[i]);
            }
        }
        
        // Check if the subsequence exists in arr2 in increasing order
        bool exists = true;
        int j = 0;
        for (int i = 0; i < m; ++i) {
            if (arr2[i] == subsequence[j]) {
                ++j;
                if (j == subsequence.size()) break;
            }
        }
        
        if (j == subsequence.size()) {
            maxLength = std::max(maxLength, (int)subsequence.size());
        }
    }
    
    return maxLength;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot m)$, where $n$ is the size of `arr1` and $m$ is the size of `arr2`. This is because we generate $2^n$ subsequences and for each, we potentially scan `arr2` once.
> - **Space Complexity:** $O(n)$, for storing the current subsequence.
> - **Why these complexities occur:** The exponential time complexity comes from generating all possible subsequences, and the linear space complexity comes from storing one subsequence at a time.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use dynamic programming to track the length of the longest common increasing subsequence ending at each position in `arr1` and `arr2`.
- We maintain two arrays `dp1` and `dp2` where `dp1[i]` is the length of the longest common increasing subsequence ending at `arr1[i]`, and similarly for `dp2`.

```cpp
#include <vector>
#include <algorithm>

int findLength(std::vector<int>& arr1, std::vector<int>& arr2) {
    int n = arr1.size();
    int m = arr2.size();
    std::vector<int> dp1(n, 1);
    std::vector<int> dp2(m, 1);
    
    for (int i = 1; i < n; ++i) {
        for (int j = 0; j < i; ++j) {
            if (arr1[i] > arr1[j]) {
                dp1[i] = std::max(dp1[i], dp1[j] + 1);
            }
        }
    }
    
    for (int i = 1; i < m; ++i) {
        for (int j = 0; j < i; ++j) {
            if (arr2[i] > arr2[j]) {
                dp2[i] = std::max(dp2[i], dp2[j] + 1);
            }
        }
    }
    
    int maxLength = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (arr1[i] == arr2[j]) {
                maxLength = std::max(maxLength, dp1[i]);
            }
        }
    }
    
    return maxLength;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 + m^2)$, where $n$ and $m$ are the sizes of `arr1` and `arr2`, respectively. This is because we perform two separate dynamic programming passes over `arr1` and `arr2`.
> - **Space Complexity:** $O(n + m)$, for storing `dp1` and `dp2`.
> - **Optimality proof:** This is optimal because we must at least read the input once, and the dynamic programming approach ensures we do not miss any potential common increasing subsequences.

---

### Final Notes

**Learning Points:**
- The importance of identifying increasing subsequences.
- Dynamic programming for tracking lengths of longest common increasing subsequences.
- The trade-off between time and space complexity in different approaches.

**Mistakes to Avoid:**
- Not considering the increasing nature of the subsequence.
- Failing to optimize the brute force approach by not using dynamic programming.
- Incorrectly implementing the dynamic programming solution.

Similar problems to practice include finding the longest common subsequence in general (not necessarily increasing) and variations involving different constraints on the subsequence.