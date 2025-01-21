## Longest Well-Performing Interval

**Problem Link:** https://leetcode.com/problems/longest-well-performing-interval/description

**Problem Statement:**
- Input: `scores` - an array of integers representing scores of a player in different intervals.
- Constraints: $1 \leq n \leq 10^5$, where $n$ is the number of intervals.
- Expected Output: The length of the longest well-performing interval.
- Key Requirements:
  - A well-performing interval is defined as an interval where the total score is positive.
  - We need to find the longest interval that satisfies this condition.
- Example Test Cases:
  - Input: `scores = [9, -3, 9, 3, 7]`
    - Output: `4`
    - Explanation: The longest well-performing interval is from index 0 to 3, with a total score of $9 - 3 + 9 + 3 = 18$, which is positive.
  - Input: `scores = [-1, -2, -3, -4]`
    - Output: `0`
    - Explanation: There is no well-performing interval in this case, as all intervals have a negative total score.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can calculate the total score for all possible intervals and check if they are well-performing.
- Step-by-step breakdown:
  1. Generate all possible intervals.
  2. For each interval, calculate the total score.
  3. Check if the total score is positive.
  4. If it is, update the maximum length of the well-performing interval.
- Why this approach comes to mind first: It is straightforward and easy to understand, but it may not be efficient for large inputs.

```cpp
int longestWPI(vector<int>& scores) {
    int n = scores.size();
    int maxLength = 0;
    for (int i = 0; i < n; i++) {
        int score = 0;
        for (int j = i; j < n; j++) {
            score += scores[j];
            if (score > 0) {
                maxLength = max(maxLength, j - i + 1);
            }
        }
    }
    return maxLength;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of intervals. This is because we are generating all possible intervals and calculating the total score for each one.
> - **Space Complexity:** $O(1)$, as we are only using a constant amount of space to store the maximum length and the current score.
> - **Why these complexities occur:** The time complexity is quadratic because we are using two nested loops to generate all possible intervals. The space complexity is constant because we are not using any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: We can use a prefix sum array to efficiently calculate the total score for each interval.
- Detailed breakdown:
  1. Calculate the prefix sum array.
  2. Use a hashmap to store the prefix sum values and their corresponding indices.
  3. Iterate through the prefix sum array and check if the current prefix sum is greater than 0. If it is, update the maximum length.
  4. If the current prefix sum is not greater than 0, check if we have seen a prefix sum that is equal to the current prefix sum minus 1. If we have, update the maximum length.
- Why this approach is optimal: It allows us to calculate the total score for each interval in constant time, reducing the overall time complexity to linear.

```cpp
int longestWPI(vector<int>& scores) {
    int n = scores.size();
    int maxLength = 0;
    int score = 0;
    unordered_map<int, int> seen;
    for (int i = 0; i < n; i++) {
        score += scores[i] > 0 ? 1 : -1;
        if (score > 0) {
            maxLength = max(maxLength, i + 1);
        } else if (seen.find(score - 1) != seen.end()) {
            maxLength = max(maxLength, i - seen[score - 1]);
        }
        if (seen.find(score) == seen.end()) {
            seen[score] = i;
        }
    }
    return maxLength;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of intervals. This is because we are iterating through the prefix sum array once.
> - **Space Complexity:** $O(n)$, as we are using a hashmap to store the prefix sum values and their corresponding indices.
> - **Optimality proof:** This approach is optimal because it allows us to calculate the total score for each interval in constant time, reducing the overall time complexity to linear. We are also using a hashmap to store the prefix sum values, which allows us to efficiently check if we have seen a prefix sum before.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: prefix sum arrays, hashmap usage, and interval calculation.
- Problem-solving patterns: using a hashmap to store prefix sum values and their corresponding indices, and iterating through the prefix sum array to calculate the total score for each interval.
- Optimization techniques: using a prefix sum array to efficiently calculate the total score for each interval, and using a hashmap to store prefix sum values and their corresponding indices.

**Mistakes to Avoid:**
- Common implementation errors: not initializing the hashmap correctly, or not checking if a prefix sum value has been seen before.
- Edge cases to watch for: handling the case where the input array is empty, or where all intervals have a negative total score.
- Performance pitfalls: using a brute force approach with a quadratic time complexity, or not using a hashmap to store prefix sum values and their corresponding indices.