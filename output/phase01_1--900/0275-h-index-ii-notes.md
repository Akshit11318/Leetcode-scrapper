## H-Index II
**Problem Link:** [https://leetcode.com/problems/h-index-ii/description](https://leetcode.com/problems/h-index-ii/description)

**Problem Statement:**
- Input: A sorted array of integers `citations` where `citations[i]` is the number of citations the `i-th` paper received.
- Constraints: `1 <= citations.length <= 10^5`, `0 <= citations[i] <= 10^9`.
- Expected Output: The H-Index of the researcher.
- Key Requirements: The H-Index is calculated as the maximum value of `h` such that the given `h` papers have at least `h` citations.
- Edge Cases: An empty array or an array with all zeros.

### Brute Force Approach

**Explanation:**
- The initial thought process involves iterating over all possible `h` values from 1 to the length of the `citations` array.
- For each `h`, we check if there are at least `h` papers with at least `h` citations.
- This approach comes to mind first because it directly implements the definition of the H-Index.

```cpp
class Solution {
public:
    int hIndex(vector<int>& citations) {
        int n = citations.size();
        int maxH = 0;
        
        for (int h = 1; h <= n; h++) {
            int count = 0;
            for (int i = 0; i < n; i++) {
                if (citations[i] >= h) {
                    count++;
                }
            }
            if (count >= h) {
                maxH = max(maxH, h);
            }
        }
        
        return maxH;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of papers. This is because for each possible `h`, we iterate through all papers.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum H-Index and the current count of papers with at least `h` citations.
> - **Why these complexities occur:** The nested loop structure leads to quadratic time complexity, making this approach inefficient for large inputs.

---

### Optimal Approach (Required)

**Explanation:**
- Since the `citations` array is sorted in ascending order, we can start from the end of the array to find the maximum H-Index.
- For each paper, we calculate its potential H-Index as the minimum between the number of papers and the number of citations it has.
- This approach is optimal because it leverages the sorted nature of the input array, allowing us to find the maximum H-Index in a single pass.

```cpp
class Solution {
public:
    int hIndex(vector<int>& citations) {
        int n = citations.size();
        int maxH = 0;
        
        for (int i = n - 1; i >= 0; i--) {
            int h = min(n - i, citations[i]);
            maxH = max(maxH, h);
        }
        
        return maxH;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of papers. This is because we make a single pass through the array.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum H-Index.
> - **Optimality proof:** This approach is optimal because it has a linear time complexity, which is the best we can achieve given that we must examine each element at least once.

---

### Final Notes

**Learning Points:**
- The importance of leveraging the properties of the input data, such as the sorted order of the `citations` array.
- How to calculate the H-Index efficiently by considering the minimum between the number of papers and the number of citations.
- The trade-off between brute force approaches and more efficient algorithms that exploit specific characteristics of the problem.

**Mistakes to Avoid:**
- Failing to consider the sorted nature of the input array, leading to inefficient solutions.
- Not optimizing the calculation of the H-Index for each paper.
- Not testing the solution with edge cases, such as an empty array or an array with all zeros.