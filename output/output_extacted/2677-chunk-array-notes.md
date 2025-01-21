## Chunk Array
**Problem Link:** https://leetcode.com/problems/chunk-array/description

**Problem Statement:**
- Input: `arr` (the input array), `size` (the chunk size)
- Constraints: `arr` is a 1D array, `size` is an integer
- Expected Output: A 2D array with chunks of the input array
- Key Requirements: Split the input array into chunks of the specified size
- Edge Cases: Handle cases where the input array is empty, or the chunk size is larger than the array length
- Example Test Cases:
  - `chunkArray([1, 2, 3, 4], 2)` returns `[[1, 2], [3, 4]]`
  - `chunkArray([1, 2, 3, 4, 5], 2)` returns `[[1, 2], [3, 4], [5]]`

---

### Brute Force Approach

**Explanation:**
- Initialize an empty result array to store the chunks
- Iterate over the input array, creating a new chunk every `size` elements
- Add each chunk to the result array
- Return the result array

```cpp
vector<vector<int>> chunkArray(vector<int>& arr, int size) {
    vector<vector<int>> result;
    vector<int> chunk;
    for (int i = 0; i < arr.size(); i++) {
        chunk.push_back(arr[i]);
        if ((i + 1) % size == 0 || i == arr.size() - 1) {
            result.push_back(chunk);
            chunk.clear();
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input array, because we iterate over the array once.
> - **Space Complexity:** $O(n)$, because we store the chunks in the result array.
> - **Why these complexities occur:** The iteration over the input array causes the time complexity, while the storage of chunks causes the space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Use a loop to create chunks of the specified size
- Use the `vector` constructor to create each chunk in a single operation
- Add each chunk to the result array

```cpp
vector<vector<int>> chunkArray(vector<int>& arr, int size) {
    vector<vector<int>> result;
    for (int i = 0; i < arr.size(); i += size) {
        result.push_back(vector<int>(arr.begin() + i, arr.begin() + min(i + size, (int)arr.size())));
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input array, because we iterate over the array in chunks.
> - **Space Complexity:** $O(n)$, because we store the chunks in the result array.
> - **Optimality proof:** This is the most efficient approach because we only iterate over the array once and use a single operation to create each chunk.

---

### Final Notes

**Learning Points:**
- **Array chunking**: Splitting an array into smaller sub-arrays of a specified size.
- **Vector construction**: Using the `vector` constructor to create a new vector from a range of elements.
- **Optimization techniques**: Minimizing the number of operations and memory allocations to improve performance.

**Mistakes to Avoid:**
- **Incorrect chunk size**: Failing to handle cases where the chunk size is larger than the array length.
- **Memory leaks**: Failing to clear temporary vectors or arrays, causing memory leaks.
- **Performance pitfalls**: Using inefficient algorithms or data structures, leading to poor performance.