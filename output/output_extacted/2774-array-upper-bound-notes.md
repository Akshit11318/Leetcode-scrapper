## Array Upper Bound
**Problem Link:** https://leetcode.com/problems/array-upper-bound/description

**Problem Statement:**
- Input format and constraints: Given a sorted array `arr` of integers and a target integer `target`, find the smallest index `i` such that `arr[i] > target`.
- Expected output format: Return the smallest index `i` such that `arr[i] > target`. If no such index exists, return `arr.length`.
- Key requirements and edge cases to consider:
  - The input array is sorted in ascending order.
  - The target integer may be present in the array or not.
  - The array may contain duplicate elements.
- Example test cases with explanations:
  - Example 1: `arr = [1, 2, 3, 4, 5]`, `target = 3`. Output: `3` because `arr[3] = 4 > 3`.
  - Example 2: `arr = [1, 2, 3, 4, 5]`, `target = 5`. Output: `5` because there is no element greater than `5` in the array.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through the array from left to right and check each element to see if it's greater than the target.
- Step-by-step breakdown of the solution:
  1. Initialize an index variable `i` to `0`.
  2. Iterate through the array using a for loop.
  3. Inside the loop, check if the current element `arr[i]` is greater than the target.
  4. If it is, return the current index `i`.
  5. If the loop completes without finding an element greater than the target, return the length of the array.
- Why this approach comes to mind first: It's the most straightforward way to solve the problem, but it's not efficient for large arrays.

```cpp
int upperBound(vector<int>& arr, int target) {
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] > target) {
            return i;
        }
    }
    return arr.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array. This is because in the worst case, we need to iterate through the entire array.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the index and target variables.
> - **Why these complexities occur:** The brute force approach has a linear time complexity because it checks each element in the array once. The space complexity is constant because we don't use any data structures that grow with the size of the input.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Since the array is sorted, we can use a binary search approach to find the smallest index `i` such that `arr[i] > target`.
- Detailed breakdown of the approach:
  1. Initialize two pointers, `low` and `high`, to the start and end of the array, respectively.
  2. While `low` is less than or equal to `high`, calculate the midpoint `mid`.
  3. If the element at the midpoint `arr[mid]` is less than or equal to the target, move the `low` pointer to `mid + 1`.
  4. Otherwise, move the `high` pointer to `mid - 1`.
  5. When the loop exits, `low` will be the smallest index `i` such that `arr[i] > target`.
- Proof of optimality: Binary search is an optimal algorithm for finding an element in a sorted array, with a time complexity of $O(\log n)$.

```cpp
int upperBound(vector<int>& arr, int target) {
    int low = 0;
    int high = arr.size() - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] <= target) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return low;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log n)$, where $n$ is the number of elements in the array. This is because we divide the search space in half at each step.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the pointers and target variable.
> - **Optimality proof:** The binary search approach is optimal because it minimizes the number of comparisons needed to find the smallest index `i` such that `arr[i] > target`.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Binary search, sorted arrays, and optimization techniques.
- Problem-solving patterns identified: Using a binary search approach to find an element in a sorted array.
- Optimization techniques learned: Reducing the time complexity from $O(n)$ to $O(\log n)$ using binary search.

**Mistakes to Avoid:**
- Common implementation errors: Not checking the bounds of the array, not handling the case where the target is not found.
- Edge cases to watch for: Empty arrays, arrays with a single element, and arrays with duplicate elements.
- Performance pitfalls: Using a brute force approach for large arrays, not optimizing the search algorithm.
- Testing considerations: Testing the function with different input arrays and target values to ensure it works correctly.