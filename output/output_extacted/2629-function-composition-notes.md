## Function Composition
**Problem Link:** https://leetcode.com/problems/function-composition/description

**Problem Statement:**
- Input format and constraints: Given two functions, `f` and `g`, where `f` has `n` functions and `g` has `m` functions. The functions are represented as arrays of integers, where each integer is the index of the function to be composed.
- Expected output format: The composition of `f` and `g` as an array of integers.
- Key requirements and edge cases to consider: The input functions `f` and `g` must have the same length, and the indices in the functions must be valid.
- Example test cases with explanations:
  - Example 1: `f = [1, 2, 3]`, `g = [3, 2, 1]`. The output should be `[3, 2, 1]`.
  - Example 2: `f = [2, 3]`, `g = [1, 2]`. The output should be `[2, 3]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through the functions `f` and `g`, and for each index in `f`, find the corresponding index in `g`.
- Step-by-step breakdown of the solution:
  1. Initialize an empty array `result` to store the composition of `f` and `g`.
  2. Iterate through the indices in `f`.
  3. For each index `i` in `f`, find the corresponding index `g[i]`.
  4. Append `g[i]` to the `result` array.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it may not be the most efficient.

```cpp
vector<int> compose(vector<int>& f, vector<int>& g) {
    vector<int> result;
    for (int i = 0; i < f.size(); i++) {
        result.push_back(g[f[i] - 1]);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the functions `f` and `g`. This is because we are iterating through the indices in `f` once.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the functions `f` and `g`. This is because we are storing the composition of `f` and `g` in the `result` array.
> - **Why these complexities occur:** These complexities occur because we are iterating through the indices in `f` once and storing the composition of `f` and `g` in the `result` array.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The same insight as the brute force approach, but we can improve the implementation by using a more efficient data structure.
- Detailed breakdown of the approach:
  1. Initialize an empty array `result` to store the composition of `f` and `g`.
  2. Iterate through the indices in `f`.
  3. For each index `i` in `f`, find the corresponding index `g[f[i] - 1]`.
  4. Append `g[f[i] - 1]` to the `result` array.
- Proof of optimality: This approach is optimal because we are iterating through the indices in `f` once and storing the composition of `f` and `g` in the `result` array.

```cpp
vector<int> compose(vector<int>& f, vector<int>& g) {
    vector<int> result;
    result.reserve(f.size()); // Reserve space to avoid reallocations
    for (int i = 0; i < f.size(); i++) {
        result.push_back(g[f[i] - 1]);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the functions `f` and `g`. This is because we are iterating through the indices in `f` once.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the functions `f` and `g`. This is because we are storing the composition of `f` and `g` in the `result` array.
> - **Optimality proof:** This approach is optimal because we are iterating through the indices in `f` once and storing the composition of `f` and `g` in the `result` array.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, indexing, and composition of functions.
- Problem-solving patterns identified: Using a more efficient data structure to improve the implementation.
- Optimization techniques learned: Reserving space in the `result` array to avoid reallocations.
- Similar problems to practice: Composition of functions with different lengths, composition of functions with multiple inputs.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if the indices in `f` are valid, not handling edge cases where `f` and `g` have different lengths.
- Edge cases to watch for: When `f` and `g` have different lengths, when the indices in `f` are not valid.
- Performance pitfalls: Not reserving space in the `result` array, leading to reallocations and decreased performance.
- Testing considerations: Test the implementation with different lengths of `f` and `g`, test the implementation with invalid indices in `f`.