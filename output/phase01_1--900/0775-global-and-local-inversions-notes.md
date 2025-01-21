## Global and Local Inversions
**Problem Link:** https://leetcode.com/problems/global-and-local-inversions/description

**Problem Statement:**
- Input format and constraints: The problem takes an array of integers as input, where each integer is in the range `[1, n]` and `n` is the number of elements in the array.
- Expected output format: The function should return `true` if the array has the same number of global and local inversions, and `false` otherwise.
- Key requirements and edge cases to consider: Local inversions occur when `i < j` and `A[i] > A[j]`, and `j - i == 1`. Global inversions occur when `i < j` and `A[i] > A[j]`, regardless of the difference between `i` and `j`.
- Example test cases with explanations:
  - For the input `[1, 2, 3, 4]`, the function should return `true` because there are no inversions.
  - For the input `[1, 3, 2, 4]`, the function should return `true` because there is one local inversion and one global inversion.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can calculate the number of local and global inversions by iterating over the array and comparing each element with every other element.
- Step-by-step breakdown of the solution:
  1. Initialize two counters, one for local inversions and one for global inversions.
  2. Iterate over the array, comparing each element with every other element.
  3. If an element is greater than another element that comes after it, increment the global inversion counter.
  4. If an element is greater than the element that comes immediately after it, increment the local inversion counter.
  5. After iterating over the entire array, compare the number of local and global inversions.
- Why this approach comes to mind first: It is a straightforward and intuitive solution that checks every possible pair of elements.

```cpp
bool isIdealPermutation(vector<int>& A) {
    int n = A.size();
    int localInversions = 0;
    int globalInversions = 0;

    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (A[i] > A[j]) {
                globalInversions++;
                if (j - i == 1) {
                    localInversions++;
                }
            }
        }
    }

    return localInversions == globalInversions;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of elements in the array. This is because we have two nested loops that iterate over the array.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the counters.
> - **Why these complexities occur:** The time complexity occurs because we are comparing every pair of elements in the array, resulting in a quadratic number of comparisons. The space complexity is constant because we only use a fixed amount of space to store the counters.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can observe that if the array has the same number of local and global inversions, then the array must be an ideal permutation, which means that every element is at most one position away from its ideal position.
- Detailed breakdown of the approach:
  1. Iterate over the array and check if each element is within one position of its ideal position.
  2. If any element is more than one position away from its ideal position, return `false`.
  3. If we finish iterating over the array without finding any element that is more than one position away from its ideal position, return `true`.
- Proof of optimality: This solution is optimal because it only requires a single pass over the array, resulting in a linear time complexity.
- Why further optimization is impossible: We must check every element in the array at least once to determine if it is an ideal permutation, so we cannot do better than a linear time complexity.

```cpp
bool isIdealPermutation(vector<int>& A) {
    int n = A.size();

    for (int i = 0; i < n; i++) {
        if (abs(A[i] - (i + 1)) > 1) {
            return false;
        }
    }

    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array. This is because we only need to make a single pass over the array.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the index and the absolute difference.
> - **Optimality proof:** This solution is optimal because it only requires a single pass over the array, resulting in a linear time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The importance of understanding the problem and identifying key insights that can lead to an optimal solution.
- Problem-solving patterns identified: The use of a single pass over the array to solve the problem in linear time.
- Optimization techniques learned: The importance of avoiding unnecessary comparisons and using a simple, intuitive solution.
- Similar problems to practice: Other problems that involve checking if an array satisfies certain properties, such as being sorted or having a certain pattern.

**Mistakes to Avoid:**
- Common implementation errors: Failing to check for edge cases, such as an empty array or an array with a single element.
- Edge cases to watch for: Arrays with duplicate elements or arrays that are not permutations of the numbers from 1 to n.
- Performance pitfalls: Using a brute force approach that has a high time complexity, such as comparing every pair of elements in the array.
- Testing considerations: Testing the function with a variety of inputs, including edge cases and large arrays, to ensure that it works correctly and efficiently.