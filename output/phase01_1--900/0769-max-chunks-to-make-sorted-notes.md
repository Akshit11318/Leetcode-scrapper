## Max Chunks to Make Sorted
**Problem Link:** https://leetcode.com/problems/max-chunks-to-make-sorted/description

**Problem Statement:**
- Input format: An array of integers `arr`.
- Constraints: `1 <= arr.length <= 1000`, `0 <= arr[i] <= 1000`.
- Expected output format: The maximum number of chunks that can be made sorted.
- Key requirements and edge cases to consider:
  - A chunk is a contiguous subarray of the input array.
  - A chunk is considered sorted if its elements are in non-decreasing order.
  - The goal is to maximize the number of chunks.
- Example test cases with explanations:
  - For `arr = [4,3,2,1,0]`, the maximum number of chunks is 1, as the entire array is not sorted but can be considered as one chunk.
  - For `arr = [1,0,1,3,2]`, the maximum number of chunks is 2, as the subarrays `[1,0]` and `[1,3,2]` can be considered as two chunks, but only `[1,0]` and `[1,3,2]` is not a valid chunking since `[1,3,2]` is not sorted.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible chunkings of the array and check if each chunk is sorted.
- Step-by-step breakdown of the solution:
  1. Generate all possible chunkings of the array.
  2. For each chunking, check if each chunk is sorted.
  3. If a chunk is not sorted, skip this chunking.
  4. Keep track of the maximum number of chunks seen so far.
- Why this approach comes to mind first: It's a straightforward approach to try all possibilities and check if they satisfy the condition.

```cpp
int maxChunksToSorted(vector<int>& arr) {
    int n = arr.size();
    int maxChunks = 0;
    
    // Generate all possible chunkings
    for (int mask = 1; mask < (1 << n); mask++) {
        vector<int> chunks;
        int start = 0;
        
        // Create chunks based on the current mask
        for (int i = 0; i < n; i++) {
            if (mask & (1 << i)) {
                vector<int> chunk(arr.begin() + start, arr.begin() + i + 1);
                chunks.push_back(chunk);
                start = i + 1;
            }
        }
        
        // Check if each chunk is sorted
        bool allSorted = true;
        for (auto& chunk : chunks) {
            bool sorted = true;
            for (int j = 1; j < chunk.size(); j++) {
                if (chunk[j] < chunk[j - 1]) {
                    sorted = false;
                    break;
                }
            }
            if (!sorted) {
                allSorted = false;
                break;
            }
        }
        
        // Update maxChunks if all chunks are sorted
        if (allSorted) {
            maxChunks = max(maxChunks, (int)chunks.size());
        }
    }
    
    return maxChunks;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n^2)$, where $n$ is the length of the input array. This is because we generate $2^n$ possible chunkings and for each chunking, we check if each chunk is sorted in $O(n^2)$ time.
> - **Space Complexity:** $O(n)$, as we need to store the current chunking.
> - **Why these complexities occur:** The brute force approach tries all possible chunkings, which leads to an exponential number of possibilities. Checking if each chunk is sorted takes quadratic time due to the nested loops.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a prefix sum array to keep track of the maximum value seen so far. If the current element is equal to its index, we can start a new chunk.
- Detailed breakdown of the approach:
  1. Initialize a variable `maxChunks` to 0.
  2. Initialize a variable `maxVal` to 0, which keeps track of the maximum value seen so far.
  3. Iterate through the array. For each element:
     - Update `maxVal` to be the maximum of `maxVal` and the current element.
     - If `maxVal` is equal to the current index, increment `maxChunks`.
- Proof of optimality: This approach ensures that we start a new chunk whenever possible, which maximizes the number of chunks.

```cpp
int maxChunksToSorted(vector<int>& arr) {
    int maxChunks = 0;
    int maxVal = 0;
    
    for (int i = 0; i < arr.size(); i++) {
        maxVal = max(maxVal, arr[i]);
        if (maxVal == i) {
            maxChunks++;
        }
    }
    
    return maxChunks;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input array. This is because we make a single pass through the array.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum value seen so far and the number of chunks.
> - **Optimality proof:** This approach is optimal because it ensures that we start a new chunk whenever possible, which maximizes the number of chunks. This is achieved by using a prefix sum array to keep track of the maximum value seen so far.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Prefix sum arrays, greedy algorithms.
- Problem-solving patterns identified: Using prefix sum arrays to keep track of maximum values seen so far.
- Optimization techniques learned: Avoiding unnecessary computations by using prefix sum arrays.
- Similar problems to practice: Other problems that involve using prefix sum arrays to optimize computations.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing variables correctly, not handling edge cases properly.
- Edge cases to watch for: Empty input arrays, arrays with duplicate elements.
- Performance pitfalls: Using brute force approaches when more efficient algorithms are available.
- Testing considerations: Testing the function with different input arrays, including edge cases.