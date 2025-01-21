## Partial Function with Placeholders
**Problem Link:** https://leetcode.com/problems/partial-function-with-placeholders/description

**Problem Statement:**
- Input format and constraints: The problem involves creating a partial function with placeholders. We're given a list of `n` integers representing the indices where the placeholders should be placed in the output list of size `n`. The output list is filled with zeros, except at the specified indices where the corresponding integer from the input list is used as the value.
- Expected output format: The output is a list of integers where the specified indices from the input list have their corresponding values, and the rest are filled with zeros.
- Key requirements and edge cases to consider: The input list can contain duplicate indices, and the output should handle such cases correctly.
- Example test cases with explanations: For example, given the list `[1, 2, 3]`, the output should be `[0, 1, 2, 3]`, assuming the list is 1-indexed. If the list is 0-indexed, the output would be `[0, 1, 2, 3]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The most straightforward approach is to iterate over the input list and directly construct the output list by placing the corresponding values at the specified indices.
- Step-by-step breakdown of the solution:
  1. Initialize an output list of size `n` filled with zeros.
  2. Iterate over the input list.
  3. For each index in the input list, place the corresponding value at that index in the output list.
- Why this approach comes to mind first: It directly addresses the problem statement and is easy to implement.

```cpp
vector<int> createPartialFunction(vector<int>& indices) {
    int n = indices.size();
    vector<int> output(n + 1, 0); // Initialize output list with zeros
    for (int i = 0; i < n; i++) {
        output[indices[i]] = i + 1; // Place value at specified index
    }
    return output;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of the input list, because we're iterating over the list once.
> - **Space Complexity:** $O(n)$, because we're creating an output list of size $n + 1$.
> - **Why these complexities occur:** The iteration over the input list and the creation of the output list are the primary operations causing these complexities.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The brute force approach is already quite straightforward and efficient. However, we can slightly optimize it by directly using the input list's indices without adding 1, assuming the input list is 0-indexed.
- Detailed breakdown of the approach: The same as the brute force approach but with the adjustment for 0-indexing.
- Proof of optimality: This approach is optimal because it still only requires a single pass through the input list and creates the output list in the same manner, but with a slight simplification.
- Why further optimization is impossible: Any solution must at least iterate over the input list and create an output list, so $O(n)$ time and space complexities are the minimum required.

```cpp
vector<int> createPartialFunctionOptimal(vector<int>& indices) {
    int n = indices.size();
    vector<int> output(n, 0); // Initialize output list with zeros
    for (int i = 0; i < n; i++) {
        if(indices[i] < n) {
            output[indices[i]] = i; // Place value at specified index
        }
    }
    return output;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of the input list, because we're still iterating over the list once.
> - **Space Complexity:** $O(n)$, because we're creating an output list of size $n$.
> - **Optimality proof:** The simplification in indexing does not change the overall complexity but makes the code slightly more efficient and straightforward.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Direct iteration and array construction.
- Problem-solving patterns identified: Handling indexing and list construction.
- Optimization techniques learned: Simplifying indexing operations.
- Similar problems to practice: Other array construction problems with specific indexing rules.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect indexing or bounds checking.
- Edge cases to watch for: Duplicate indices in the input list.
- Performance pitfalls: Unnecessary iterations or operations.
- Testing considerations: Ensure the function handles various input sizes and edge cases correctly.