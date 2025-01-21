## Minimum Increment to Make Array Unique
**Problem Link:** https://leetcode.com/problems/minimum-increment-to-make-array-unique/description

**Problem Statement:**
- Input: An array of integers `A` of length `n`.
- Constraints: `1 <= A.length <= 40000`, `0 <= A[i] <= 40000`.
- Expected Output: The minimum number of increments needed to make all elements in the array unique.
- Key Requirements: Each element in the array must be unique after increments.
- Edge Cases: Empty array, array with all unique elements, array with duplicate elements.

**Example Test Cases:**
- Input: `A = [1,2,2]`, Output: `1`. Explanation: Increment the second `2` to `3`.
- Input: `A = [3,2,1,2,1,7]`, Output: `6`. Explanation: Increment the first `2` to `3`, the second `2` to `4`, the first `1` to `2`, and the second `1` to `5`, and the `3` to `6` and `7` to `8`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Sort the array and then iterate through it, incrementing any duplicate elements until they are unique.
- Step-by-step breakdown:
  1. Sort the array in ascending order.
  2. Initialize a variable to keep track of the minimum number of increments needed.
  3. Iterate through the sorted array, comparing each element with its previous one.
  4. If an element is the same as its previous one, increment it until it is unique and update the minimum increments needed.
- Why this approach comes to mind first: It's straightforward and ensures uniqueness by comparing each element with its previous one.

```cpp
vector<int> minIncrementForUnique(vector<int>& A) {
    sort(A.begin(), A.end());
    int increments = 0;
    for (int i = 1; i < A.size(); i++) {
        if (A[i] <= A[i - 1]) {
            increments += A[i - 1] - A[i] + 1;
            A[i] = A[i - 1] + 1;
        }
    }
    return A;
}
int minIncrementForUniqueCount(vector<int>& A) {
    sort(A.begin(), A.end());
    int increments = 0;
    for (int i = 1; i < A.size(); i++) {
        if (A[i] <= A[i - 1]) {
            increments += A[i - 1] - A[i] + 1;
            A[i] = A[i - 1] + 1;
        }
    }
    return increments;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to sorting, where $n$ is the number of elements in the array.
> - **Space Complexity:** $O(1)$ for the increments variable, assuming the input array can be modified in-place.
> - **Why these complexities occur:** Sorting dominates the time complexity, and a single variable is used to track increments, resulting in constant space complexity.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: The same approach as the brute force is actually optimal because it ensures uniqueness with the minimum number of increments by only incrementing elements when necessary.
- Detailed breakdown: The approach remains the same as the brute force: sort the array and then iterate through it, incrementing any duplicate elements until they are unique.
- Proof of optimality: Any other approach would either not guarantee uniqueness or would require more increments, as this approach only increments elements when necessary and does so in the most efficient manner possible.

```cpp
int minIncrementForUnique(vector<int>& A) {
    sort(A.begin(), A.end());
    int increments = 0, nextUnique = A[0];
    for (int i = 1; i < A.size(); i++) {
        if (A[i] <= nextUnique) {
            increments += nextUnique - A[i] + 1;
            nextUnique++;
        } else {
            nextUnique = A[i];
        }
    }
    return increments;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to sorting.
> - **Space Complexity:** $O(1)$, assuming the input array can be modified in-place.
> - **Optimality proof:** This approach guarantees uniqueness with the minimum number of increments by only incrementing elements when necessary and doing so in the most efficient manner possible.

---

### Final Notes
**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting, iteration, and conditional incrementing.
- Problem-solving patterns identified: Ensuring uniqueness through iterative comparison and adjustment.
- Optimization techniques learned: Minimizing increments by only adjusting elements when necessary.

**Mistakes to Avoid:**
- Not sorting the array before iteration, leading to incorrect comparisons.
- Not incrementing elements correctly, leading to non-uniqueness or excessive increments.
- Not considering edge cases, such as an empty array or an array with all unique elements.