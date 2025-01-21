## Find the Integer Added to Array I
**Problem Link:** https://leetcode.com/problems/find-the-integer-added-to-array-i/description

**Problem Statement:**
- Input format and constraints: The problem involves two arrays, `original` and `changed`, where `changed` is a modified version of `original` with an integer added to one of its elements. The task is to find the integer added.
- Expected output format: The function should return the integer added to the `changed` array.
- Key requirements and edge cases to consider: The input arrays will have the same length, and exactly one element in `changed` will be different from `original`. The added integer will always be positive.
- Example test cases with explanations:
  - `original = [1,2,3], changed = [1,3,3]`: The integer added is `1`, so the output should be `1`.
  - `original = [1,5,7,9], changed = [1,5,7,11]`: The integer added is `2`, so the output should be `2`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Compare each element of the `original` array with the corresponding element in the `changed` array. When a difference is found, calculate the added integer.
- Step-by-step breakdown of the solution:
  1. Iterate through both arrays simultaneously.
  2. For each pair of elements, check if they are different.
  3. When a difference is found, calculate the added integer by subtracting the element from `original` from the element in `changed`.
- Why this approach comes to mind first: It's straightforward and directly addresses the problem statement.

```cpp
int findAddedInteger(vector<int>& original, vector<int>& changed) {
    for (int i = 0; i < original.size(); i++) {
        if (original[i] != changed[i]) {
            return changed[i] - original[i];
        }
    }
    // This should not happen according to the problem constraints
    return -1; // or throw an exception
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input arrays, because we potentially iterate through each element once.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the loop variable and the result.
> - **Why these complexities occur:** The iteration through the arrays causes the linear time complexity, while the constant space usage is due to not using any data structures that scale with input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The problem constraints guarantee that exactly one element in `changed` will be different from `original`. Thus, the first approach is already optimal because it stops as soon as it finds the difference.
- Detailed breakdown of the approach: The same as the brute force approach because it is already optimal.
- Proof of optimality: Any solution must at least read the input arrays once to find the difference, resulting in a time complexity of at least $O(n)$. Thus, the provided solution is optimal.

```cpp
int findAddedInteger(vector<int>& original, vector<int>& changed) {
    for (int i = 0; i < original.size(); i++) {
        if (original[i] != changed[i]) {
            return changed[i] - original[i];
        }
    }
    // This should not happen according to the problem constraints
    return -1; // or throw an exception
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input arrays.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space.
> - **Optimality proof:** The solution is optimal because it achieves the minimum possible time complexity required to solve the problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, comparison, and basic arithmetic operations.
- Problem-solving patterns identified: Directly addressing the problem statement and considering the constraints to ensure efficiency.
- Optimization techniques learned: Recognizing when a straightforward approach is already optimal due to the problem's constraints.
- Similar problems to practice: Other problems involving array comparisons and modifications.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to check for the condition where the arrays might not have the same length or not handling the case where no difference is found (though the problem guarantees a difference will exist).
- Edge cases to watch for: Arrays with a single element, arrays with all elements being the same, and ensuring the added integer is indeed positive.
- Performance pitfalls: Unnecessary iterations or using data structures that increase space complexity without a need.
- Testing considerations: Thoroughly testing with various inputs, including edge cases, to ensure the solution works as expected.