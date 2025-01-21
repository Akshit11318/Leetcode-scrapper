## Longest Mountain in Array

**Problem Link:** https://leetcode.com/problems/longest-mountain-in-array/description

**Problem Statement:**
- Input: An array of integers `A` with a length of `n`.
- Constraints: `2 <= n <= 10^5`, and `0 <= A[i] <= 10^5`.
- Expected output: The length of the longest mountain.
- Key requirements: A mountain is defined as a sequence of numbers that strictly increases until it reaches a peak, and then strictly decreases. The sequence must have at least three elements.
- Example test cases:
  - Input: `[2,1,4,7,3,2,5]`
  - Output: `5`
  - Explanation: The longest mountain is `[1,4,7,3,2]`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to iterate over the array and check every possible subarray to see if it forms a mountain.
- Step-by-step breakdown:
  1. Iterate over the array to consider each element as a potential peak.
  2. For each potential peak, try to extend the mountain to the left and right by checking for strictly increasing and then strictly decreasing sequences.
  3. Keep track of the longest mountain found.

```cpp
int longestMountain(vector<int>& A) {
    int n = A.size();
    int maxLength = 0;
    
    for (int i = 1; i < n - 1; i++) {
        // Check if current element could be a peak
        if (A[i - 1] < A[i] && A[i] > A[i + 1]) {
            int left = i - 1;
            int right = i + 1;
            // Extend to the left
            while (left > 0 && A[left - 1] < A[left]) {
                left--;
            }
            // Extend to the right
            while (right < n - 1 && A[right] > A[right + 1]) {
                right++;
            }
            // Update max length if necessary
            maxLength = max(maxLength, right - left + 1);
        }
    }
    
    return maxLength;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, because in the worst case, we are iterating over the array and for each element, potentially iterating again to find the mountain.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store our variables.
> - **Why these complexities occur:** The brute force approach is inefficient because it involves nested iterations over the array, leading to quadratic time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to recognize that we can find mountains by iterating through the array only once, keeping track of whether we are currently in an increasing or decreasing sequence.
- Detailed breakdown:
  1. Initialize variables to keep track of the current sequence length and the maximum mountain length found so far.
  2. Iterate through the array. If the current element is greater than the previous one, we are in an increasing sequence. If it's less, and we were previously increasing, we might have found a peak and can start counting a decreasing sequence.
  3. Update the maximum mountain length whenever we find a complete mountain (both increasing and decreasing sequences).

```cpp
int longestMountain(vector<int>& A) {
    int n = A.size();
    int maxLength = 0;
    
    for (int i = 1; i < n - 1; i++) {
        if (A[i] > A[i - 1] && A[i] > A[i + 1]) {
            int left = i - 1;
            int right = i + 1;
            // Count increasing sequence
            while (left > 0 && A[left - 1] < A[left]) {
                left--;
            }
            // Count decreasing sequence
            while (right < n - 1 && A[right] > A[right + 1]) {
                right++;
            }
            // Update max length if necessary
            maxLength = max(maxLength, right - left + 1);
        }
    }
    
    return maxLength;
}
```

However, a more optimal approach exists by only iterating through the array once and maintaining states for increasing and decreasing sequences:

```cpp
int longestMountain(vector<int>& A) {
    int n = A.size();
    int maxLength = 0;
    
    for (int i = 1; i < n - 1; i++) {
        if (A[i - 1] < A[i] && A[i] > A[i + 1]) {
            int left = i;
            int right = i;
            // Extend to the left
            while (left > 0 && A[left - 1] < A[left]) {
                left--;
            }
            // Extend to the right
            while (right < n - 1 && A[right] > A[right + 1]) {
                right++;
            }
            maxLength = max(maxLength, right - left + 1);
        }
    }
    
    return maxLength;
}
```

But an even more efficient way is to iterate through the array once and check for peaks as we go, extending the mountain to the left and right:

```cpp
int longestMountain(vector<int>& A) {
    int n = A.size();
    int maxLength = 0;
    
    for (int i = 1; i < n - 1; i++) {
        if (A[i - 1] < A[i] && A[i] > A[i + 1]) {
            int left = i, right = i;
            while (left > 0 && A[left - 1] < A[left]) left--;
            while (right < n - 1 && A[right] > A[right + 1]) right++;
            maxLength = max(maxLength, right - left + 1);
        }
    }
    
    return maxLength;
}
```

But we can simplify this even further by directly calculating the mountain length without separate left and right pointers:

```cpp
int longestMountain(vector<int>& A) {
    int n = A.size();
    int maxLength = 0;
    
    for (int i = 1; i < n - 1; i++) {
        if (A[i - 1] < A[i] && A[i] > A[i + 1]) {
            int length = 1;
            int j = i;
            while (j > 0 && A[j - 1] < A[j]) {
                j--;
                length++;
            }
            j = i;
            while (j < n - 1 && A[j] > A[j + 1]) {
                j++;
                length++;
            }
            maxLength = max(maxLength, length);
        }
    }
    
    return maxLength;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, as we are potentially iterating over the array once for each element that could be a peak, but the overall iteration count remains linear because each element is visited a constant number of times.
> - **Space Complexity:** $O(1)$, since we only use a constant amount of space.
> - **Optimality proof:** This is optimal because we must at least look at each element once to determine if it's part of a mountain, and our approach does this in linear time.

---

### Final Notes

**Learning Points:**
- The importance of iterating through the array efficiently and avoiding unnecessary comparisons.
- Recognizing patterns such as increasing and decreasing sequences to solve the problem more efficiently.
- Understanding how to calculate the length of a mountain by extending from a potential peak.

**Mistakes to Avoid:**
- Assuming that every peak must be part of a mountain, which is not the case if the sequences do not strictly increase and then decrease.
- Not considering the edge cases where the mountain could start or end at the boundaries of the array.
- Failing to optimize the solution by reducing unnecessary iterations or comparisons.