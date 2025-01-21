## H-Index
**Problem Link:** https://leetcode.com/problems/h-index/description

**Problem Statement:**
- Input: A list of integers `citations` representing the number of citations for each paper.
- Constraints: `1 <= citations.length <= 1000`, `0 <= citations[i] <= 1000`.
- Expected output: The maximum H-Index.
- Key requirements: Calculate the H-Index for each paper and return the maximum value.
- Edge cases: Handle empty input, single-element input, and cases where all citations are zero.

**Example Test Cases:**
- Input: `citations = [3,0,6,1,5]`
- Output: `3`
- Explanation: The H-Index for each paper is calculated as the minimum between the number of papers and the number of citations. The maximum H-Index is `3`.
- Input: `citations = [1,3,1]`
- Output: `1`
- Explanation: The H-Index for each paper is calculated as the minimum between the number of papers and the number of citations. The maximum H-Index is `1`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Sort the citations in descending order and calculate the H-Index for each paper.
- Step-by-step breakdown:
  1. Sort the citations in descending order.
  2. Iterate over the sorted citations and calculate the H-Index for each paper.
  3. Keep track of the maximum H-Index encountered.
- Why this approach comes to mind first: It is a straightforward approach that involves sorting and iterating over the citations.

```cpp
#include <algorithm>
#include <vector>

int hIndex(std::vector<int>& citations) {
    // Sort the citations in descending order
    std::sort(citations.rbegin(), citations.rend());
    
    int maxHIndex = 0;
    for (int i = 0; i < citations.size(); i++) {
        // Calculate the H-Index for each paper
        int hIndex = std::min(i + 1, citations[i]);
        // Update the maximum H-Index
        maxHIndex = std::max(maxHIndex, hIndex);
    }
    return maxHIndex;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting operation, where $n$ is the number of citations.
> - **Space Complexity:** $O(1)$ if the input vector is allowed to be modified, $O(n)$ otherwise.
> - **Why these complexities occur:** The sorting operation dominates the time complexity, while the space complexity depends on whether the input vector is modified.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: The H-Index for each paper is the minimum between the number of papers and the number of citations.
- Detailed breakdown:
  1. Initialize an array `buckets` of size `n + 1`, where `n` is the number of citations.
  2. Iterate over the citations and update the corresponding bucket.
  3. Iterate over the buckets in reverse order and calculate the maximum H-Index.
- Proof of optimality: This approach has a time complexity of $O(n)$, which is optimal for this problem.

```cpp
#include <vector>

int hIndex(std::vector<int>& citations) {
    int n = citations.size();
    std::vector<int> buckets(n + 1);
    
    // Update the buckets
    for (int citation : citations) {
        if (citation >= n) {
            buckets[n]++;
        } else {
            buckets[citation]++;
        }
    }
    
    int maxHIndex = 0;
    int papers = 0;
    // Calculate the maximum H-Index
    for (int i = n; i >= 0; i--) {
        papers += buckets[i];
        maxHIndex = std::max(maxHIndex, std::min(papers, i));
    }
    return maxHIndex;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of citations.
> - **Space Complexity:** $O(n)$ for the `buckets` array.
> - **Optimality proof:** This approach has a linear time complexity, which is optimal for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: Bucket sort, H-Index calculation.
- Problem-solving patterns: Using buckets to count frequencies, iterating over buckets to calculate the maximum H-Index.
- Optimization techniques: Using a bucket array to reduce the time complexity.

**Mistakes to Avoid:**
- Not handling edge cases: Empty input, single-element input, cases where all citations are zero.
- Not optimizing the solution: Using a brute force approach with a high time complexity.
- Not validating the input: Assuming the input is always valid, which may not be the case in real-world scenarios.