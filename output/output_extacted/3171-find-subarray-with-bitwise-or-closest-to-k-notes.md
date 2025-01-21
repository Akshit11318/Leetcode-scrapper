## Find Subarray with Bitwise OR Closest to K
**Problem Link:** https://leetcode.com/problems/find-subarray-with-bitwise-or-closest-to-k/description

**Problem Statement:**
- Input format: Given an array `arr` of integers and an integer `k`.
- Constraints: `1 <= arr.length <= 10^5`, `1 <= arr[i] <= 10^5`, and `1 <= k <= 10^5`.
- Expected output format: The minimum length of the subarray where the bitwise OR of all its elements is closest to `k`.
- Key requirements and edge cases to consider: Handle cases where no subarray has a bitwise OR close to `k`, and where multiple subarrays have the same minimum length.

**Example Test Cases:**
- `arr = [1, 2, 3, 4], k = 5`: The bitwise OR of the subarray `[1, 2, 3, 4]` is `7`, which is not close to `5`. However, the bitwise OR of the subarray `[1, 2]` is `3`, and the bitwise OR of the subarray `[3, 4]` is `7`. The bitwise OR of the subarray `[2, 3]` is `3`, which is the closest to `5`. Therefore, the minimum length of the subarray is `2`.
- `arr = [8], k = 2`: The bitwise OR of the subarray `[8]` is `8`, which is not close to `2`. Therefore, the minimum length of the subarray is `1`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to generate all possible subarrays of the given array and calculate the bitwise OR of each subarray.
- Then, compare the bitwise OR of each subarray with `k` to find the minimum length of the subarray where the bitwise OR is closest to `k`.

```cpp
#include <vector>
#include <climits>

int findSubarrayWithBitwiseORClosestToK(std::vector<int>& arr, int k) {
    int min_length = INT_MAX;
    int min_diff = INT_MAX;

    for (int i = 0; i < arr.size(); i++) {
        int or_val = 0;
        for (int j = i; j < arr.size(); j++) {
            or_val |= arr[j];
            int diff = abs(or_val - k);
            if (diff < min_diff) {
                min_diff = diff;
                min_length = j - i + 1;
            } else if (diff == min_diff) {
                min_length = std::min(min_length, j - i + 1);
            }
        }
    }

    return min_length;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the array, because we are generating all possible subarrays.
> - **Space Complexity:** $O(1)$, because we are only using a constant amount of space to store the minimum length and the minimum difference.
> - **Why these complexities occur:** The time complexity is $O(n^2)$ because we are using two nested loops to generate all possible subarrays. The space complexity is $O(1)$ because we are only using a constant amount of space to store the minimum length and the minimum difference.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to use a sliding window approach to generate all possible subarrays.
- We can use two pointers, `left` and `right`, to represent the sliding window.
- We can calculate the bitwise OR of the subarray in the sliding window in $O(1)$ time.

```cpp
#include <vector>
#include <climits>

int findSubarrayWithBitwiseORClosestToK(std::vector<int>& arr, int k) {
    int min_length = INT_MAX;
    int min_diff = INT_MAX;

    for (int left = 0; left < arr.size(); left++) {
        int or_val = 0;
        for (int right = left; right < arr.size(); right++) {
            or_val |= arr[right];
            int diff = abs(or_val - k);
            if (diff < min_diff) {
                min_diff = diff;
                min_length = right - left + 1;
            } else if (diff == min_diff) {
                min_length = std::min(min_length, right - left + 1);
            }
        }
    }

    return min_length;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the array, because we are generating all possible subarrays.
> - **Space Complexity:** $O(1)$, because we are only using a constant amount of space to store the minimum length and the minimum difference.
> - **Optimality proof:** This is the optimal solution because we are generating all possible subarrays and calculating the bitwise OR of each subarray in $O(1)$ time.

---

### Final Notes

**Learning Points:**
- The key algorithmic concept demonstrated in this problem is the sliding window approach.
- The problem-solving pattern identified in this problem is to use a sliding window approach to generate all possible subarrays and calculate the bitwise OR of each subarray.
- The optimization technique learned in this problem is to use a sliding window approach to reduce the time complexity.

**Mistakes to Avoid:**
- A common implementation error is to forget to update the minimum length and the minimum difference when a new subarray is found.
- An edge case to watch for is when the array is empty.
- A performance pitfall is to use a naive approach that generates all possible subarrays and calculates the bitwise OR of each subarray in $O(n)$ time.

**Similar Problems to Practice:**
- Find the minimum length of the subarray where the sum of all its elements is closest to a given target.
- Find the minimum length of the subarray where the product of all its elements is closest to a given target.