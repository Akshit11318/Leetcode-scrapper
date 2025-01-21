## Best Sightseeing Pair

**Problem Link:** https://leetcode.com/problems/best-sightseeing-pair/description

**Problem Statement:**
- Input format: An array of integers `values` where `values[i]` represents the beauty of the `i-th` sightseeing spot.
- Constraints: The length of the array is between 2 and 10^5, and each element is between 1 and 10^5.
- Expected output format: The maximum score that can be obtained by visiting two sightseeing spots.
- Key requirements and edge cases to consider: The score of a pair is calculated as `values[i] + values[j] + i - j` where `i < j`.
- Example test cases with explanations:
  - Example 1: Input: `[8,1,5,2,6]`, Output: `11`, Explanation: `i = 0`, `j = 2`, score = `8 + 5 + 0 - 2 = 11`.
  - Example 2: Input: `[1,2]`, Output: `2`, Explanation: `i = 0`, `j = 1`, score = `1 + 2 + 0 - 1 = 2`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach is to calculate the score for every pair of sightseeing spots and return the maximum score.
- Step-by-step breakdown of the solution:
  1. Initialize the maximum score to a negative infinity.
  2. Iterate over all pairs of sightseeing spots using two nested loops.
  3. For each pair, calculate the score using the formula `values[i] + values[j] + i - j`.
  4. Update the maximum score if the current score is higher.
- Why this approach comes to mind first: It is the most straightforward way to solve the problem, as it considers all possible pairs of sightseeing spots.

```cpp
int maxScoreSightseeingPair(vector<int>& values) {
    int maxScore = INT_MIN;
    for (int i = 0; i < values.size(); i++) {
        for (int j = i + 1; j < values.size(); j++) {
            int score = values[i] + values[j] + i - j;
            maxScore = max(maxScore, score);
        }
    }
    return maxScore;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of sightseeing spots. This is because we have two nested loops that iterate over all pairs of sightseeing spots.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum score.
> - **Why these complexities occur:** The time complexity is quadratic because we consider all pairs of sightseeing spots, and the space complexity is constant because we only use a fixed amount of space.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can observe that the score of a pair is determined by the sum of the beauty of the two sightseeing spots and the difference between their indices. This means that we can calculate the maximum score by considering each sightseeing spot as the first spot in the pair and keeping track of the maximum score we can get by visiting a second spot.
- Detailed breakdown of the approach:
  1. Initialize the maximum score to a negative infinity and the maximum score we can get by visiting a second spot to the beauty of the first sightseeing spot plus its index.
  2. Iterate over the sightseeing spots starting from the second spot.
  3. For each spot, calculate the score we can get by visiting this spot as the second spot in the pair with the current maximum score we can get by visiting a second spot.
  4. Update the maximum score if the current score is higher.
  5. Update the maximum score we can get by visiting a second spot by subtracting 1 from it, as we move to the next spot.
- Proof of optimality: This approach is optimal because it considers all possible pairs of sightseeing spots and keeps track of the maximum score we can get by visiting a second spot. The time complexity is linear, which is the best we can achieve for this problem.

```cpp
int maxScoreSightseeingPair(vector<int>& values) {
    int maxScore = INT_MIN;
    int maxScoreSoFar = values[0] + 0;
    for (int i = 1; i < values.size(); i++) {
        maxScore = max(maxScore, maxScoreSoFar + values[i] - i);
        maxScoreSoFar = max(maxScoreSoFar, values[i] + i);
    }
    return maxScore;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of sightseeing spots. This is because we only need to iterate over the sightseeing spots once.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum score and the maximum score we can get by visiting a second spot.
> - **Optimality proof:** The time complexity is linear, which is the best we can achieve for this problem. The space complexity is constant, which is optimal.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The optimal approach demonstrates the use of dynamic programming to solve the problem in linear time.
- Problem-solving patterns identified: The problem can be solved by considering each sightseeing spot as the first spot in the pair and keeping track of the maximum score we can get by visiting a second spot.
- Optimization techniques learned: The optimal approach uses a technique called "prefix sum" to calculate the maximum score we can get by visiting a second spot.
- Similar problems to practice: Other problems that involve calculating the maximum score or minimum cost by considering all possible pairs or combinations of elements.

**Mistakes to Avoid:**
- Common implementation errors: One common mistake is to use a brute force approach that has a time complexity of $O(n^2)$, which can be slow for large inputs.
- Edge cases to watch for: The problem statement assumes that the input array has at least two elements. We should add error checking to handle cases where the input array has less than two elements.
- Performance pitfalls: The optimal approach uses a constant amount of space, which is optimal. However, we should be aware of the time complexity of the approach and avoid using approaches that have a higher time complexity.
- Testing considerations: We should test the approach with different inputs, including edge cases, to ensure that it works correctly.