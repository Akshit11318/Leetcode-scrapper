## Number of Subarrays that Match a Pattern II
**Problem Link:** https://leetcode.com/problems/number-of-subarrays-that-match-a-pattern-ii/description

**Problem Statement:**
- Given an array `nums` and a pattern `pattern`, find the number of subarrays that match the given pattern.
- The pattern is represented as a string of '0's and '1's, where '0' represents a smaller number and '1' represents a larger number in the context of the subarray.
- The input array `nums` contains integers.
- The expected output is the count of subarrays that match the pattern.
- Key requirements include considering all possible subarrays and correctly interpreting the pattern to compare elements within each subarray.
- Example test cases include arrays with varying lengths and patterns, demonstrating the need to handle different scenarios.

---

### Brute Force Approach
**Explanation:**
- The initial thought process involves checking every possible subarray against the given pattern.
- This approach comes to mind first because it ensures all possibilities are considered, even if it's not efficient.
- Step-by-step, this involves iterating over all possible start and end indices for subarrays, then for each subarray, comparing its elements according to the pattern.

```cpp
int numSubarrays(vector<int>& nums, string pattern) {
    int count = 0;
    for (int start = 0; start < nums.size(); start++) {
        for (int end = start + pattern.size(); end <= nums.size(); end++) {
            vector<int> subarray(nums.begin() + start, nums.begin() + end);
            bool match = true;
            for (int i = 0; i < pattern.size() - 1; i++) {
                if ((pattern[i] == '0' && subarray[i] >= subarray[i + 1]) ||
                    (pattern[i] == '1' && subarray[i] <= subarray[i + 1])) {
                    match = false;
                    break;
                }
            }
            if (match) count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the size of `nums`, because for each possible subarray, we potentially compare each element to its next one according to the pattern.
> - **Space Complexity:** $O(n)$ for storing the subarray, as in the worst case, the subarray could be the entire input array.
> - **Why these complexities occur:** The nested loops for generating all possible subarrays and the inner loop for comparing elements according to the pattern contribute to these complexities.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to directly compare adjacent elements in the subarray based on the pattern, without needing to explicitly store the subarray or compare all elements in the subarray against each other.
- This approach is optimal because it minimizes the number of operations by only considering the necessary comparisons based on the pattern.
- Step-by-step, this involves iterating over the array with a sliding window of the pattern's length, comparing adjacent elements according to the pattern at each position.

```cpp
int numSubarrays(vector<int>& nums, string pattern) {
    int count = 0;
    for (int i = 0; i <= nums.size() - pattern.size(); i++) {
        bool match = true;
        for (int j = 0; j < pattern.size() - 1; j++) {
            if ((pattern[j] == '0' && nums[i + j] >= nums[i + j + 1]) ||
                (pattern[j] == '1' && nums[i + j] <= nums[i + j + 1])) {
                match = false;
                break;
            }
        }
        if (match) count++;
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the size of `nums` and $m$ is the length of the pattern, because we are considering each element in the context of the pattern's length.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the count and other variables, regardless of the input size.
> - **Optimality proof:** This is the best possible complexity because we must at least read the input once, and our algorithm does so in a linear fashion with respect to the size of the input array and the pattern.

---

### Final Notes
**Learning Points:**
- Key algorithmic concepts demonstrated include the use of sliding windows and direct comparison of adjacent elements based on a given pattern.
- Problem-solving patterns identified include reducing the problem space by focusing on the essential comparisons needed to match the pattern.
- Optimization techniques learned include minimizing unnecessary operations and comparisons.

**Mistakes to Avoid:**
- Common implementation errors include incorrectly interpreting the pattern or failing to handle edge cases such as an empty input array or pattern.
- Performance pitfalls include using unnecessary data structures or algorithms that lead to higher time or space complexities than required.