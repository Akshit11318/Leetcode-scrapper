## Find Top Scoring Students II
**Problem Link:** https://leetcode.com/problems/find-top-scoring-students-ii/description

**Problem Statement:**
- Input format and constraints: Given an array of `positive integers` representing the scores of students, and an array of `positive integers` representing the `thresholds`, find the number of students who have a score greater than or equal to each threshold.
- Expected output format: Return an array of integers representing the number of students who have a score greater than or equal to each threshold.
- Key requirements and edge cases to consider: The input arrays are non-empty, and the scores and thresholds are positive integers.
- Example test cases with explanations:
  - Example 1: scores = [10,20,30,40,50], thresholds = [15,20,30,40,50], output = [5,4,3,2,1]
  - Example 2: scores = [10,20,30,40,50], thresholds = [5,10,15,20,25], output = [5,5,5,4,3]

---

### Brute Force Approach
**Explanation:**
- Initial thought process: For each threshold, iterate over the scores array to count the number of scores greater than or equal to the threshold.
- Step-by-step breakdown of the solution:
  1. Initialize an empty array to store the results.
  2. Iterate over the thresholds array.
  3. For each threshold, initialize a counter to 0.
  4. Iterate over the scores array.
  5. If a score is greater than or equal to the threshold, increment the counter.
  6. Append the counter to the results array.
- Why this approach comes to mind first: It is a straightforward solution that checks each score against each threshold.

```cpp
vector<int> findTopScoringStudents(vector<int>& scores, vector<int>& thresholds) {
    vector<int> results;
    for (int threshold : thresholds) {
        int count = 0;
        for (int score : scores) {
            if (score >= threshold) {
                count++;
            }
        }
        results.push_back(count);
    }
    return results;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times m)$, where $n$ is the number of thresholds and $m$ is the number of scores. This is because we are iterating over the scores array for each threshold.
> - **Space Complexity:** $O(n)$, where $n$ is the number of thresholds. This is because we are storing the results in an array of size $n$.
> - **Why these complexities occur:** The brute force approach has a high time complexity because it checks each score against each threshold. The space complexity is relatively low because we only need to store the results.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can sort the scores array in descending order and then iterate over the thresholds array. For each threshold, we can use a binary search to find the index of the first score that is less than the threshold.
- Detailed breakdown of the approach:
  1. Sort the scores array in descending order.
  2. Initialize an empty array to store the results.
  3. Iterate over the thresholds array.
  4. For each threshold, use a binary search to find the index of the first score that is less than the threshold.
  5. The number of students who have a score greater than or equal to the threshold is equal to the index of the first score that is less than the threshold.
  6. Append the count to the results array.
- Proof of optimality: The optimal approach has a time complexity of $O(m \log m + n \log m)$, where $m$ is the number of scores and $n$ is the number of thresholds. This is because we are sorting the scores array and then using a binary search for each threshold.

```cpp
vector<int> findTopScoringStudents(vector<int>& scores, vector<int>& thresholds) {
    sort(scores.rbegin(), scores.rend());
    vector<int> results;
    for (int threshold : thresholds) {
        int count = upper_bound(scores.begin(), scores.end(), threshold) - scores.begin();
        results.push_back(count);
    }
    return results;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \log m + n \log m)$, where $m$ is the number of scores and $n$ is the number of thresholds. This is because we are sorting the scores array and then using a binary search for each threshold.
> - **Space Complexity:** $O(n)$, where $n$ is the number of thresholds. This is because we are storing the results in an array of size $n$.
> - **Optimality proof:** The optimal approach has a lower time complexity than the brute force approach because we are using a binary search to find the index of the first score that is less than the threshold.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: sorting, binary search, and upper bound.
- Problem-solving patterns identified: using a binary search to find the index of the first element that meets a condition.
- Optimization techniques learned: sorting the input array to enable binary search.
- Similar problems to practice: problems that involve finding the number of elements that meet a condition.

**Mistakes to Avoid:**
- Common implementation errors: not checking the bounds of the input arrays, not handling edge cases.
- Edge cases to watch for: empty input arrays, duplicate thresholds.
- Performance pitfalls: using a brute force approach for large input arrays.
- Testing considerations: testing with different input sizes, testing with duplicate thresholds.