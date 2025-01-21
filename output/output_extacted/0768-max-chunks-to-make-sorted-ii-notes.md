## Max Chunks To Make Sorted II
**Problem Link:** https://leetcode.com/problems/max-chunks-to-make-sorted-ii/description

**Problem Statement:**
- Input: An integer array `arr`.
- Constraints: `1 <= arr.length <= 10^4`, `0 <= arr[i] <= 10^9`.
- Expected Output: The maximum number of chunks in which the array can be divided such that each chunk is sorted.
- Key Requirements: 
  - A chunk is defined as a subarray that is sorted in ascending order.
  - The chunks must be non-overlapping.
- Edge Cases: 
  - If the array is already sorted, return the length of the array.
  - If the array cannot be divided into any chunks, return 0.
- Example Test Cases: 
  - Input: `[2,1,2,4,3,3,4,1,2,1]`, Output: `4`
  - Input: `[1,1]`, Output: `1`

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to generate all possible chunks of the array and check if each chunk is sorted.
- However, this approach is inefficient due to the large number of possible chunks.
- We can improve upon this by considering the properties of sorted arrays.

```cpp
class Solution {
public:
    int maxChunksToSorted(vector<int>& arr) {
        int n = arr.size();
        int chunks = 0;
        for (int i = 0; i < n; i++) {
            bool isSorted = true;
            for (int j = i; j < n; j++) {
                bool chunkSorted = true;
                for (int k = i; k < j; k++) {
                    if (arr[k] > arr[k + 1]) {
                        chunkSorted = false;
                        break;
                    }
                }
                if (chunkSorted) {
                    chunks++;
                    i = j;
                    break;
                }
            }
        }
        return chunks;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the array. This is because we have three nested loops.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space.
> - **Why these complexities occur:** The brute force approach has a high time complexity due to the nested loops, making it inefficient for large inputs.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a stack to keep track of the maximum element in each chunk.
- We iterate through the array, and for each element, we check if it is the maximum element in the current chunk.
- If it is, we increment the chunk count and reset the maximum element.
- We use the `max` function to keep track of the maximum element in the current chunk.

```cpp
class Solution {
public:
    int maxChunksToSorted(vector<int>& arr) {
        int chunks = 0;
        int maxVal = 0;
        for (int i = 0; i < arr.size(); i++) {
            maxVal = max(maxVal, arr[i]);
            if (maxVal == i) {
                chunks++;
            }
        }
        return chunks;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the array. This is because we only have a single loop.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space.
> - **Optimality proof:** This approach is optimal because we only need to iterate through the array once to find the maximum chunks. We use a single variable to keep track of the maximum element in the current chunk, making the space complexity constant.

---

### Final Notes

**Learning Points:**
- The importance of using a stack or a single variable to keep track of the maximum element in each chunk.
- How to optimize the solution by reducing the number of loops and using a single pass through the array.
- The use of the `max` function to simplify the code and improve readability.

**Mistakes to Avoid:**
- Using nested loops, which can lead to high time complexity.
- Not considering the properties of sorted arrays, which can simplify the solution.
- Not using a single variable to keep track of the maximum element in each chunk, which can reduce space complexity.

---