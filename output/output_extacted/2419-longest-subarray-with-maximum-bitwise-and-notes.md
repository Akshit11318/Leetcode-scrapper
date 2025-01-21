## Longest Subarray with Maximum Bitwise AND

**Problem Link:** https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/description

**Problem Statement:**
- Given an integer array `nums`, return the length of the longest subarray where the bitwise AND of all integers in the subarray is equal to the bitwise AND of all integers in the array.
- Input format: `nums` is a non-empty array of integers.
- Constraints: $1 \leq nums.length \leq 10^5$, $0 \leq nums[i] \leq 10^9$.
- Expected output format: The length of the longest subarray where the bitwise AND of all integers in the subarray is equal to the bitwise AND of all integers in the array.
- Key requirements and edge cases to consider:
  - Handling arrays with a single element.
  - Dealing with arrays where all elements are the same.
  - Considering arrays with large numbers that may cause overflow.
- Example test cases with explanations:
  - For `nums = [1, 2, 3]`, the bitwise AND of all integers in the array is `0`, so the longest subarray with maximum bitwise AND is the entire array, and the answer is `3`.
  - For `nums = [1, 2, 3, 4]`, the bitwise AND of all integers in the array is `0`, so the longest subarray with maximum bitwise AND is the entire array, and the answer is `4`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to check every possible subarray to see if its bitwise AND equals the bitwise AND of the entire array.
- We start by calculating the bitwise AND of the entire array.
- Then, we iterate over all possible subarrays, calculate their bitwise AND, and compare it with the bitwise AND of the entire array.
- If a match is found, we update the maximum length of the subarray.
- This approach is straightforward but inefficient due to its high time complexity.

```cpp
int longestSubarray(vector<int>& nums) {
    int n = nums.size();
    int andAll = nums[0];
    for (int i = 1; i < n; i++) {
        andAll &= nums[i];
    }
    int maxLength = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            int andSub = nums[i];
            for (int k = i + 1; k <= j; k++) {
                andSub &= nums[k];
            }
            if (andSub == andAll) {
                maxLength = max(maxLength, j - i + 1);
            }
        }
    }
    return maxLength;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$ because we have three nested loops iterating over the array.
> - **Space Complexity:** $O(1)$ as we only use a constant amount of space to store the bitwise AND of the entire array and the maximum length of the subarray.
> - **Why these complexities occur:** The high time complexity is due to the brute force nature of checking every possible subarray, while the space complexity is low because we only need a few variables to store the necessary information.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a sliding window approach to efficiently find the longest subarray where the bitwise AND equals the bitwise AND of the entire array.
- We start by calculating the bitwise AND of the entire array.
- Then, we maintain a sliding window `[left, right]` and calculate the bitwise AND of the elements within this window.
- If the bitwise AND of the window equals the bitwise AND of the entire array, we update the maximum length of the subarray.
- We slide the window to the right by moving the `right` pointer and update the bitwise AND of the window accordingly.
- If the bitwise AND of the window no longer equals the bitwise AND of the entire array, we slide the window to the right by moving the `left` pointer.
- This approach significantly reduces the time complexity compared to the brute force approach.

```cpp
int longestSubarray(vector<int>& nums) {
    int n = nums.size();
    int andAll = nums[0];
    for (int i = 1; i < n; i++) {
        andAll &= nums[i];
    }
    int maxLength = 0;
    for (int left = 0; left < n; left++) {
        int andSub = nums[left];
        for (int right = left; right < n; right++) {
            andSub &= nums[right];
            if (andSub == andAll) {
                maxLength = max(maxLength, right - left + 1);
            }
        }
    }
    return maxLength;
}
```

However, a more optimal solution can be achieved by using a prefix array to store the bitwise AND of all elements up to each index. This allows us to calculate the bitwise AND of any subarray in constant time.

```cpp
int longestSubarray(vector<int>& nums) {
    int n = nums.size();
    vector<int> prefix(n + 1);
    prefix[0] = ~0; // Initialize with all ones
    for (int i = 0; i < n; i++) {
        prefix[i + 1] = prefix[i] & nums[i];
    }
    int andAll = prefix[n];
    int maxLength = 0;
    for (int left = 0; left < n; left++) {
        for (int right = left; right < n; right++) {
            int andSub = prefix[right + 1] & ~prefix[left];
            if (andSub == andAll) {
                maxLength = max(maxLength, right - left + 1);
            }
        }
    }
    return maxLength;
}
```

But even this solution can be further optimized by using a hash map to store the indices of the prefix array. This allows us to find the longest subarray in linear time.

```cpp
int longestSubarray(vector<int>& nums) {
    int n = nums.size();
    int andAll = nums[0];
    for (int i = 1; i < n; i++) {
        andAll &= nums[i];
    }
    int maxLength = 0;
    unordered_map<int, int> prefix;
    prefix[~0] = -1; // Initialize with all ones
    int andSub = ~0;
    for (int i = 0; i < n; i++) {
        andSub &= nums[i];
        if (prefix.find(andSub) != prefix.end()) {
            maxLength = max(maxLength, i - prefix[andSub]);
        } else {
            prefix[andSub] = i;
        }
    }
    return maxLength;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ because we only need to iterate over the array once.
> - **Space Complexity:** $O(n)$ as we use a hash map to store the indices of the prefix array.
> - **Optimality proof:** This solution is optimal because it finds the longest subarray in linear time, which is the best possible time complexity for this problem.

---

### Final Notes

**Learning Points:**
- The importance of calculating the bitwise AND of the entire array first.
- The use of a sliding window approach to efficiently find the longest subarray.
- The optimization of using a prefix array to store the bitwise AND of all elements up to each index.
- The further optimization of using a hash map to store the indices of the prefix array.

**Mistakes to Avoid:**
- Not calculating the bitwise AND of the entire array first.
- Not using a sliding window approach to efficiently find the longest subarray.
- Not optimizing the solution using a prefix array or a hash map.
- Not considering the edge cases where the array has a single element or all elements are the same.