## Find Target Indices After Sorting Array
**Problem Link:** https://leetcode.com/problems/find-target-indices-after-sorting-array/description

**Problem Statement:**
- Input format: Given a sorted array `nums` and two integers `key` and `k`.
- Constraints: `1 <= k <= nums.length`, `1 <= nums.length <= 1000`.
- Expected output format: Return the `k` smallest indices of the array where `nums[i] == key`.
- Key requirements and edge cases to consider: 
  - Handling cases when `key` is not present in the array.
  - When `k` is larger than the number of occurrences of `key`.
  - When `k` is 1, return the smallest index.
- Example test cases with explanations:
  - For `nums = [1, 2, 3, 4, 5], key = 2, k = 1`, return `[0]` because the smallest index where `nums[i] == key` is 0.
  - For `nums = [1, 2, 3, 4, 5], key = 2, k = 2`, return `[]` because there's only one occurrence of `key`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Sort the array and then find all occurrences of `key`.
- Step-by-step breakdown of the solution:
  1. Create a copy of the input array to sort.
  2. Sort the copied array.
  3. Initialize an empty list to store indices where `nums[i] == key`.
  4. Iterate through the sorted array to find indices of `key`.
  5. If `k` indices are found, return them; otherwise, return all found indices.
- Why this approach comes to mind first: It's straightforward and involves basic operations like sorting and searching.

```cpp
vector<int> targetIndices(vector<int>& nums, int key, int k) {
    vector<int> sortedNums = nums;
    sort(sortedNums.begin(), sortedNums.end());
    vector<int> indices;
    for (int i = 0; i < sortedNums.size(); i++) {
        if (sortedNums[i] == key) {
            indices.push_back(i);
        }
    }
    if (indices.size() < k) {
        return indices;
    } else {
        return vector<int>(indices.begin(), indices.begin() + k);
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to sorting the array, where $n$ is the number of elements in the array.
> - **Space Complexity:** $O(n)$ for storing the sorted array and the indices.
> - **Why these complexities occur:** Sorting is the dominant operation, and storing the sorted array and indices requires additional space.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of sorting the entire array, count the number of elements less than `key` and the number of occurrences of `key`.
- Detailed breakdown of the approach:
  1. Count the total occurrences of `key` in the array.
  2. Count the number of elements less than `key`.
  3. The first occurrence of `key` will be at the index equal to the count of elements less than `key`.
  4. The `k`th occurrence will be at the index equal to the count of elements less than `key` plus `k-1`.
- Proof of optimality: This approach only requires a single pass through the array, making it more efficient than sorting.

```cpp
vector<int> targetIndices(vector<int>& nums, int key, int k) {
    int lessThanKey = 0, equalKey = 0;
    for (int num : nums) {
        if (num < key) lessThanKey++;
        if (num == key) equalKey++;
    }
    if (equalKey < k) return {};
    vector<int> result;
    for (int i = lessThanKey; i < lessThanKey + k; i++) {
        result.push_back(i);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array, because we make a single pass through the array.
> - **Space Complexity:** $O(k)$ for storing the result, where $k$ is the number of indices to return.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the array, avoiding the overhead of sorting.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Counting, sorting, and the importance of understanding the problem constraints.
- Problem-solving patterns identified: Looking for ways to avoid unnecessary computations, such as sorting the entire array when only specific information is needed.
- Optimization techniques learned: Using counts to determine indices instead of sorting.
- Similar problems to practice: Problems involving partial sorting, counting, or finding specific elements within an array.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases properly, such as when `k` is larger than the number of occurrences of `key`.
- Edge cases to watch for: When `key` is not present in the array, or when `k` equals 1.
- Performance pitfalls: Sorting the entire array when it's not necessary.
- Testing considerations: Ensure to test with various inputs, including edge cases, to verify the correctness of the solution.