## Find the Prefix Common Array of Two Arrays
**Problem Link:** https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/description

**Problem Statement:**
- Given two arrays `A` and `B` of the same length, find the prefix common array.
- The prefix common array is an array of length `n`, where the `i-th` element is the length of the common prefix between the arrays `A` and `B` when considering the first `i` elements.
- Input format: Two integer arrays `A` and `B`.
- Expected output format: An integer array representing the prefix common array.
- Key requirements and edge cases to consider:
  - Both arrays have the same length `n`.
  - The length of the common prefix between `A` and `B` for the first `i` elements is the number of elements at the start of both arrays that are equal.
- Example test cases:
  - Input: `A = [1, 2, 3, 4], B = [1, 2, 3, 5]`
    Output: `[1, 2, 3, 0]`
  - Input: `A = [1, 1, 1], B = [1, 1, 1]`
    Output: `[1, 2, 3]`

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to iterate through both arrays simultaneously and check the common prefix length at each step.
- For each `i` from `1` to `n`, compare the first `i` elements of `A` and `B` to find the length of the common prefix.
- Store the length of the common prefix at each step in a result array.

```cpp
vector<int> prefixCommonArray(vector<int>& A, vector<int>& B) {
    int n = A.size();
    vector<int> result(n);
    for (int i = 0; i < n; i++) {
        int commonPrefixLength = 0;
        for (int j = 0; j <= i; j++) {
            if (A[j] == B[j]) {
                commonPrefixLength++;
            } else {
                break;
            }
        }
        result[i] = commonPrefixLength;
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ because for each element in the array, we are potentially comparing all previous elements.
> - **Space Complexity:** $O(n)$ for storing the result array.
> - **Why these complexities occur:** The nested loop structure leads to quadratic time complexity, and we need a linear amount of space to store the result.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to maintain a running comparison of the elements from `A` and `B` as we iterate through them, keeping track of the length of the common prefix seen so far.
- At each step `i`, compare `A[i]` with `B[i]`. If they are equal, the common prefix length increases by `1`. Otherwise, it resets to `0`.
- This approach avoids the need for nested loops, significantly improving efficiency.

```cpp
vector<int> prefixCommonArray(vector<int>& A, vector<int>& B) {
    int n = A.size();
    vector<int> result(n);
    int commonPrefixLength = 0;
    for (int i = 0; i < n; i++) {
        if (A[i] == B[i]) {
            commonPrefixLength++;
        } else {
            commonPrefixLength = 0;
        }
        result[i] = commonPrefixLength;
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ because we make a single pass through the arrays.
> - **Space Complexity:** $O(n)$ for storing the result array.
> - **Optimality proof:** This is the best possible time complexity because we must at least read the input once, and we achieve this with a single pass, making it optimal.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iterative approach, maintaining a running state (common prefix length).
- Problem-solving patterns identified: Avoiding nested loops when possible to improve efficiency.
- Optimization techniques learned: Using a single pass through the data to reduce time complexity.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling edge cases, such as when `A` and `B` have different lengths (though the problem statement guarantees they are the same).
- Edge cases to watch for: Handling arrays with zero length or arrays containing duplicate elements.
- Performance pitfalls: Using nested loops unnecessarily, leading to high time complexity.
- Testing considerations: Ensure to test with arrays of varying lengths and contents to cover different scenarios.