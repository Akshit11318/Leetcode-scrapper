## Plates Between Candles
**Problem Link:** [https://leetcode.com/problems/plates-between-candles/description](https://leetcode.com/problems/plates-between-candles/description)

**Problem Statement:**
- Input format: A string `s` and a list of integers `queries`.
- Constraints: `n` is the length of `s`, `q` is the length of `queries`, `1 <= n <= 10^5`, `1 <= q <= 10^5`.
- Expected output format: A list of integers, where each integer is the number of plates between the two candles in the corresponding query.
- Key requirements and edge cases to consider: 
    - There are two types of characters in `s`: '*' and '|'. '*' represents an empty plate and '|' represents a candle.
    - The queries are given as pairs of indices, where the first index is inclusive and the second index is exclusive.
- Example test cases with explanations:
    - Input: `s = "**|**|***|", queries = [[1, 17], [4, 5], [14, 17], [5, 11], [15, 16]]`
    - Output: `[2, 0, 0, 0, 0]`
    - Explanation: 
        - In the first query, the candles are at indices 3 and 5. There are 2 plates between them.
        - In the second query, the candles are at indices 4 and 5. There are 0 plates between them.
        - In the third query, the candles are at indices 3 and 8. There are 0 plates between them.
        - In the fourth query, the candles are at indices 5 and 7. There are 0 plates between them.
        - In the fifth query, the candles are at indices 8 and 9. There are 0 plates between them.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over each query and count the number of '*' characters between the two candles.
- Step-by-step breakdown of the solution:
    1. Iterate over each query.
    2. For each query, find the indices of the candles.
    3. Count the number of '*' characters between the two candles.
- Why this approach comes to mind first: This is the most straightforward approach and it is easy to understand.

```cpp
vector<int> platesBetweenCandles(string s, vector<vector<int>>& queries) {
    int n = s.size();
    vector<int> result;
    for (auto& query : queries) {
        int left = query[0];
        int right = query[1];
        int count = 0;
        while (left < right) {
            if (s[left] == '|') {
                break;
            }
            left++;
        }
        while (right > left) {
            if (s[right - 1] == '|') {
                break;
            }
            right--;
        }
        for (int i = left + 1; i < right; i++) {
            if (s[i] == '*') {
                count++;
            }
        }
        result.push_back(count);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(q \cdot n)$, where $q$ is the number of queries and $n$ is the length of the string.
> - **Space Complexity:** $O(q)$, where $q$ is the number of queries.
> - **Why these complexities occur:** The time complexity is $O(q \cdot n)$ because we are iterating over each query and for each query, we are iterating over the string to find the candles and count the number of '*' characters. The space complexity is $O(q)$ because we are storing the result for each query.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can pre-process the string and store the indices of the candles in a vector. Then, for each query, we can use binary search to find the indices of the candles.
- Detailed breakdown of the approach:
    1. Pre-process the string and store the indices of the candles in a vector.
    2. For each query, use binary search to find the indices of the candles.
    3. Count the number of '*' characters between the two candles.
- Proof of optimality: This is the optimal solution because we are using binary search to find the indices of the candles, which reduces the time complexity from $O(q \cdot n)$ to $O(q \log m)$, where $m$ is the number of candles.

```cpp
vector<int> platesBetweenCandles(string s, vector<vector<int>>& queries) {
    int n = s.size();
    vector<int> candles;
    for (int i = 0; i < n; i++) {
        if (s[i] == '|') {
            candles.push_back(i);
        }
    }
    vector<int> result;
    for (auto& query : queries) {
        int left = query[0];
        int right = query[1];
        int l = lower_bound(candles.begin(), candles.end(), left) - candles.begin();
        int r = upper_bound(candles.begin(), candles.end(), right - 1) - candles.begin() - 1;
        if (l <= r) {
            result.push_back(candles[r] - candles[l] - 1 - (r - l));
        } else {
            result.push_back(0);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(q \log m + n)$, where $q$ is the number of queries, $m$ is the number of candles, and $n$ is the length of the string.
> - **Space Complexity:** $O(m)$, where $m$ is the number of candles.
> - **Optimality proof:** This is the optimal solution because we are using binary search to find the indices of the candles, which reduces the time complexity from $O(q \cdot n)$ to $O(q \log m)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Binary search, pre-processing.
- Problem-solving patterns identified: Using pre-processing to reduce the time complexity, using binary search to find the indices of the candles.
- Optimization techniques learned: Using binary search instead of linear search, using pre-processing to reduce the time complexity.
- Similar problems to practice: Problems that involve pre-processing and binary search.

**Mistakes to Avoid:**
- Common implementation errors: Not checking the boundaries of the array, not handling the case where the query is out of range.
- Edge cases to watch for: The case where the query is out of range, the case where the string is empty.
- Performance pitfalls: Using linear search instead of binary search, not using pre-processing to reduce the time complexity.
- Testing considerations: Testing the function with different inputs, testing the function with edge cases.