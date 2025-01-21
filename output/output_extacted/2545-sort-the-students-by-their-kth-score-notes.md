## Sort the Students by Their Kth Score
**Problem Link:** https://leetcode.com/problems/sort-the-students-by-their-kth-score/description

**Problem Statement:**
- Input format: A 2D array `scores` where each subarray represents a student's scores in different subjects and an integer `k` representing the subject to sort by.
- Constraints: `1 <= scores.length <= 10^4`, `1 <= scores[i].length <= 10^4`, `1 <= k <= scores[i].length`.
- Expected output format: A 2D array with the students sorted by their `kth` score in descending order.
- Key requirements and edge cases to consider:
  - Handling cases where `k` is larger than the number of subjects for a student.
  - Sorting students with equal `kth` scores.
- Example test cases:
  - `scores = [[10,6,9,1],[7,5,11,2],[4,8,3,15]]`, `k = 2`
  - `scores = [[3,4],[5,6]]`, `k = 1`

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to iterate through each student's scores, compare the `kth` score, and sort the students based on these scores.
- This approach involves using a sorting algorithm (like bubble sort or insertion sort) with a custom comparison function that compares the `kth` score of each student.

```cpp
#include <vector>
#include <algorithm>

vector<vector<int>> sortStudents(vector<vector<int>>& scores, int k) {
    // Use std::sort with a custom comparison function
    std::sort(scores.begin(), scores.end(), 
              [&k](const vector<int>& a, const vector<int>& b) {
                  return a[k-1] > b[k-1]; // Sort in descending order
              });
    return scores;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting, where $n$ is the number of students. The comparison function itself takes constant time, $O(1)$.
> - **Space Complexity:** $O(1)$ for the sorting algorithm if it's implemented in-place, otherwise $O(n)$ for auxiliary space.
> - **Why these complexities occur:** The sorting algorithm dominates the time complexity. The space complexity depends on the sorting algorithm's implementation.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal approach is essentially the same as the brute force approach because we must sort the students based on their `kth` score, and sorting algorithms have a lower bound of $O(n \log n)$ for comparison-based sorting.
- The key insight is recognizing that the problem requires a comparison-based sorting, which cannot be improved beyond $O(n \log n)$ in the general case.

```cpp
#include <vector>
#include <algorithm>

vector<vector<int>> sortStudents(vector<vector<int>>& scores, int k) {
    // Use std::sort with a custom comparison function
    std::sort(scores.begin(), scores.end(), 
              [&k](const vector<int>& a, const vector<int>& b) {
                  return a[k-1] > b[k-1]; // Sort in descending order
              });
    return scores;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting.
> - **Space Complexity:** $O(1)$ if the sorting is in-place, otherwise $O(n)$.
> - **Optimality proof:** Since we must compare each student's `kth` score to determine the sorted order, and comparison-based sorting has a lower bound of $O(n \log n)$, this approach is optimal.

---

### Final Notes

**Learning Points:**
- Understanding the time and space complexity of sorting algorithms.
- Recognizing when a problem requires comparison-based sorting and its implications on complexity.
- Using custom comparison functions with `std::sort`.

**Mistakes to Avoid:**
- Not validating the input `k` to ensure it's within bounds of the scores array.
- Not handling edge cases where students have equal `kth` scores.
- Incorrectly implementing the comparison function, leading to incorrect sorting.

**Similar Problems to Practice:**
- Sorting arrays or lists based on specific criteria.
- Implementing comparison-based sorting algorithms.
- Analyzing time and space complexity of algorithms.