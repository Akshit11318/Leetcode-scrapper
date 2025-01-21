## Maximum Number of Matching Indices After Right Shifts
**Problem Link:** https://leetcode.com/problems/maximum-number-of-matching-indices-after-right-shifts/description

**Problem Statement:**
- Input: Two arrays `a` and `b` of integers, both of length `n`.
- Output: The maximum number of indices `i` such that `a[i] == b[(i + shift) % n]` after applying a right shift to `b`.
- Key requirements: Find the optimal shift that maximizes the number of matching indices.
- Example test cases:
  - `a = [2,1,2,4,3]`, `b = [1,3,2,2,5]`, the maximum number of matching indices is `3`.
  - `a = [1,2,3,4,5]`, `b = [1,2,3,4,5]`, the maximum number of matching indices is `5`.

---

### Brute Force Approach
**Explanation:**
- The initial thought process involves checking every possible shift from `0` to `n-1` and counting the number of matching indices for each shift.
- For each shift, iterate through both arrays and compare elements at shifted indices.
- Keep track of the maximum count of matching indices across all shifts.

```cpp
int maximizeMatchingIndices(vector<int>& a, vector<int>& b) {
    int n = a.size();
    int maxCount = 0;
    for (int shift = 0; shift < n; shift++) {
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (a[i] == b[(i + shift) % n]) count++;
        }
        maxCount = max(maxCount, count);
    }
    return maxCount;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the arrays. This is because for each of the $n$ possible shifts, we are iterating through the array of length $n$.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input arrays, as we are using a constant amount of space to store the count and maximum count.
> - **Why these complexities occur:** The nested loop structure leads to the quadratic time complexity, while the use of a fixed amount of variables results in constant space complexity.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight here is to realize that for each element in `a`, we are looking for the same element in `b` but shifted. This can be approached by using a single pass through both arrays and counting the occurrences of each element in `a` and `b`.
- However, realizing that a simple count won't suffice due to the shift operation, we should instead consider how many times an element from `a` can match an element in `b` after a shift.
- The optimal approach involves recognizing that this problem can be solved by considering the shifts directly and their impact on the matching count without needing to iterate through all shifts explicitly.
- We notice that the maximum number of matches will occur when the shift aligns the most frequent elements in both arrays.

```cpp
int maximizeMatchingIndices(vector<int>& a, vector<int>& b) {
    int n = a.size();
    int maxCount = 0;
    for (int shift = 0; shift < n; shift++) {
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (a[i] == b[(i + shift) % n]) count++;
        }
        maxCount = max(maxCount, count);
    }
    return maxCount;
}
```

However, realizing that this is essentially the brute force approach due to the nature of the problem requiring a check of all shifts, the optimal approach in terms of time complexity does not deviate significantly from the brute force for this specific problem context. The nature of the problem necessitates checking each possible alignment of `a` and `b`, leading to a time complexity that remains $O(n^2)$ in the worst case for a straightforward implementation.

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, as explained, due to the necessity of checking all possible alignments.
> - **Space Complexity:** $O(1)$, as we're using a constant amount of space.
> - **Optimality proof:** The problem's nature requires checking all possible shifts to ensure the maximum number of matches is found, making $O(n^2)$ the best achievable time complexity for a straightforward solution.

---

### Final Notes

**Learning Points:**
- The importance of understanding the problem's constraints and how they impact the solution's complexity.
- Recognizing when a brute force approach might be necessary or optimal due to the problem's nature.
- Understanding how shifts and alignments can impact matching counts in array comparison problems.

**Mistakes to Avoid:**
- Assuming a more complex algorithm is always necessary; sometimes, the brute force approach is the most straightforward and efficient due to the problem's constraints.
- Not considering the impact of shifts on array alignments and how this affects the matching count.
- Overlooking the importance of checking all possible alignments to ensure the maximum number of matches is found.