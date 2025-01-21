## First Bad Version
**Problem Link:** https://leetcode.com/problems/first-bad-version/description

**Problem Statement:**
- Input format and constraints: The problem involves finding the first bad version of a product given a range of versions, where the `isBadVersion` function can be used to check if a version is bad.
- Expected output format: The function should return the first bad version.
- Key requirements and edge cases to consider: The function should be efficient and handle large inputs.
- Example test cases with explanations: 
    - `n = 5`, `bad = 4` should return `4` because version `4` is the first bad version.
    - `n = 1`, `bad = 1` should return `1` because version `1` is the first bad version.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The simplest way to solve this problem is to iterate through each version and check if it's bad using the `isBadVersion` function.
- Step-by-step breakdown of the solution:
    1. Start from version `1`.
    2. Check if the current version is bad using `isBadVersion`.
    3. If it's bad, return the current version.
    4. If it's not bad, move to the next version.
- Why this approach comes to mind first: It's straightforward and easy to implement.

```cpp
class Solution {
public:
    int firstBadVersion(int n) {
        for (int i = 1; i <= n; i++) {
            if (isBadVersion(i)) {
                return i;
            }
        }
        return n; // This line should never be reached
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the total number of versions, because we're potentially checking each version once.
> - **Space Complexity:** $O(1)$, as we're using a constant amount of space.
> - **Why these complexities occur:** The time complexity is linear because we're iterating through each version, and the space complexity is constant because we're not using any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking each version linearly, we can use a binary search approach to find the first bad version more efficiently.
- Detailed breakdown of the approach:
    1. Initialize two pointers, `left` and `right`, to the start and end of the version range, respectively.
    2. While `left` is less than or equal to `right`, calculate the middle version `mid`.
    3. Check if `mid` is bad using `isBadVersion`.
    4. If `mid` is bad, update `right` to `mid - 1` to search in the left half.
    5. If `mid` is not bad, update `left` to `mid + 1` to search in the right half.
    6. Repeat steps 2-5 until `left` is greater than `right`.
    7. Return `left` as the first bad version.
- Proof of optimality: Binary search is known to be the most efficient algorithm for finding an element in a sorted list, with a time complexity of $O(\log n)$.
- Why further optimization is impossible: This is because we must check at least $\log n$ versions to find the first bad one, due to the nature of binary search.

```cpp
class Solution {
public:
    int firstBadVersion(int n) {
        int left = 1, right = n;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (isBadVersion(mid)) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log n)$, where $n$ is the total number of versions, because we're using binary search.
> - **Space Complexity:** $O(1)$, as we're using a constant amount of space.
> - **Optimality proof:** The time complexity is logarithmic because we're dividing the search space in half with each iteration, and the space complexity is constant because we're not using any data structures that scale with the input size.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Binary search.
- Problem-solving patterns identified: Using a more efficient algorithm to solve a problem that initially seems to require a brute force approach.
- Optimization techniques learned: Applying binary search to reduce the time complexity of a problem.
- Similar problems to practice: Other problems that involve finding an element in a sorted list, such as finding the first element that meets a certain condition.

**Mistakes to Avoid:**
- Common implementation errors: Not updating the `left` and `right` pointers correctly, or not checking the base case of the recursion (if using recursive binary search).
- Edge cases to watch for: When `n` is `1`, or when the first bad version is the first version.
- Performance pitfalls: Using a linear search instead of binary search, which can lead to a significant increase in time complexity for large inputs.
- Testing considerations: Testing the function with different inputs, including edge cases, to ensure it works correctly.