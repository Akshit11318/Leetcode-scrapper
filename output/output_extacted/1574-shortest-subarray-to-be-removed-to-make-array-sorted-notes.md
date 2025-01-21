## Shortest Subarray to be Removed to Make Array Sorted

**Problem Link:** https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/description

**Problem Statement:**
- Input: An array of integers `arr`.
- Output: The length of the shortest subarray that needs to be removed to make `arr` sorted.
- Key Requirements: The subarray can be of any length, including 0, and the removal should result in a sorted array.
- Edge Cases: Empty array, single-element array, already sorted array, and arrays with duplicate elements.

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking all possible subarrays and their removal to see if the remaining array is sorted.
- Step-by-step breakdown:
  1. Generate all possible subarrays of `arr`.
  2. For each subarray, remove it from `arr` to get a new array.
  3. Check if the new array is sorted.
  4. Keep track of the shortest subarray that, when removed, results in a sorted array.

```cpp
class Solution {
public:
    int findLengthOfShortestSubarray(vector<int>& arr) {
        int n = arr.size();
        if (n == 0 || isSorted(arr)) return 0;

        int minLen = n;
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                vector<int> newArr;
                for (int k = 0; k < i; k++) newArr.push_back(arr[k]);
                for (int k = j + 1; k < n; k++) newArr.push_back(arr[k]);
                if (isSorted(newArr)) {
                    minLen = min(minLen, j - i + 1);
                }
            }
        }
        return minLen;
    }

    bool isSorted(vector<int>& arr) {
        for (int i = 0; i < arr.size() - 1; i++) {
            if (arr[i] > arr[i + 1]) return false;
        }
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the size of `arr`. This is because for each subarray, we potentially create a new array and check if it's sorted.
> - **Space Complexity:** $O(n)$, as we create new arrays to hold the subarrays without the removed part.
> - **Why these complexities occur:** The brute force approach involves generating all possible subarrays and checking each one, leading to exponential time complexity. The space complexity is linear because we only need to store one subarray at a time.

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use two pointers, one starting from the beginning of `arr` and one from the end, moving towards each other. We check for the longest prefix and suffix that are sorted and can be connected.
- Detailed breakdown:
  1. Find the longest prefix of `arr` that is sorted.
  2. Find the longest suffix of `arr` that is sorted.
  3. Try to connect the prefix and suffix. If they can be connected directly, the subarray to remove is the part between them.
  4. If the prefix and suffix cannot be connected directly, find the minimum length of the subarray that needs to be removed to connect them.

```cpp
class Solution {
public:
    int findLengthOfShortestSubarray(vector<int>& arr) {
        int n = arr.size();
        if (n == 0 || isSorted(arr)) return 0;

        int left = 0;
        while (left < n - 1 && arr[left] <= arr[left + 1]) left++;

        if (left == n - 1) return 0; // Already sorted

        int right = n - 1;
        while (right > 0 && arr[right - 1] <= arr[right]) right--;

        int res = min(n - left - 1, right);
        int i = 0, j = right;
        while (i <= left && j < n) {
            if (arr[i] <= arr[j]) {
                res = min(res, j - i - 1);
                i++;
            } else {
                j++;
            }
        }
        return res;
    }

    bool isSorted(vector<int>& arr) {
        for (int i = 0; i < arr.size() - 1; i++) {
            if (arr[i] > arr[i + 1]) return false;
        }
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of `arr`. This is because we only need to traverse `arr` a constant number of times.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space.
> - **Optimality proof:** This approach is optimal because it directly finds the shortest subarray that needs to be removed to make `arr` sorted, without unnecessary iterations or comparisons.

### Final Notes

**Learning Points:**
- The importance of identifying the longest sorted prefix and suffix in an array.
- How two pointers can be used to efficiently find these prefixes and suffixes.
- The concept of connecting sorted parts of an array to minimize the subarray to be removed.

**Mistakes to Avoid:**
- Not checking for the edge case where the array is already sorted.
- Not properly handling the connection between the prefix and suffix.
- Not considering all possible subarrays in the brute force approach, leading to incorrect results.