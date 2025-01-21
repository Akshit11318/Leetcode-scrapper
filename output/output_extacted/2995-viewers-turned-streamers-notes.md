## Viewers Turned Streamers
**Problem Link:** https://leetcode.com/problems/viewers-turned-streamers/description

**Problem Statement:**
- Input format and constraints: Given an integer array `viewers` of length `n`, where `viewers[i]` is the number of viewers for the `i-th` stream.
- Expected output format: Return the maximum number of viewers after all possible viewers-turned-streamers operations.
- Key requirements and edge cases to consider: Each viewer can either watch the stream or start their own stream, and the number of viewers for each stream is equal to the number of viewers for the original stream.
- Example test cases with explanations:
  - Example 1: `viewers = [1, 3, 5, 4, 3]`, the maximum number of viewers is `5 + 4 = 9`.
  - Example 2: `viewers = [3, 1, 1, 1, 1]`, the maximum number of viewers is `3 + 1 + 1 + 1 + 1 = 7`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of viewers-turned-streamers operations and calculate the maximum number of viewers for each combination.
- Step-by-step breakdown of the solution:
  1. Initialize a variable `max_viewers` to store the maximum number of viewers.
  2. Iterate over all possible combinations of viewers-turned-streamers operations.
  3. For each combination, calculate the number of viewers after the operation.
  4. Update `max_viewers` if the current number of viewers is greater than `max_viewers`.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it has an exponential time complexity due to the number of possible combinations.

```cpp
class Solution {
public:
    int maxViewers(vector<int>& viewers) {
        int n = viewers.size();
        int max_viewers = 0;
        for (int i = 0; i < (1 << n); i++) {
            int current_viewers = 0;
            for (int j = 0; j < n; j++) {
                if ((i & (1 << j)) != 0) {
                    current_viewers += viewers[j];
                }
            }
            max_viewers = max(max_viewers, current_viewers);
        }
        return max_viewers;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the number of streams.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum number of viewers.
> - **Why these complexities occur:** The time complexity is exponential because we try all possible combinations of viewers-turned-streamers operations, and the space complexity is constant because we only use a constant amount of space to store the maximum number of viewers.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The maximum number of viewers is achieved when we choose the stream with the most viewers to turn into a streamer.
- Detailed breakdown of the approach:
  1. Sort the `viewers` array in descending order.
  2. Initialize a variable `max_viewers` to store the maximum number of viewers.
  3. Iterate over the sorted `viewers` array and add each viewer count to `max_viewers`.
  4. Return `max_viewers` as the maximum number of viewers.
- Proof of optimality: This approach is optimal because we choose the stream with the most viewers to turn into a streamer, which maximizes the number of viewers.

```cpp
class Solution {
public:
    int maxViewers(vector<int>& viewers) {
        int n = viewers.size();
        sort(viewers.rbegin(), viewers.rend());
        int max_viewers = 0;
        for (int i = 0; i < n; i++) {
            max_viewers += viewers[i];
        }
        return max_viewers;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of streams.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum number of viewers.
> - **Optimality proof:** This approach is optimal because we choose the stream with the most viewers to turn into a streamer, which maximizes the number of viewers.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting, iteration, and optimization.
- Problem-solving patterns identified: Choosing the maximum value to maximize the result.
- Optimization techniques learned: Sorting the input array to choose the maximum value.
- Similar problems to practice: Other optimization problems that involve choosing the maximum value.

**Mistakes to Avoid:**
- Common implementation errors: Not sorting the input array, not choosing the maximum value.
- Edge cases to watch for: Empty input array, single-element input array.
- Performance pitfalls: Using an exponential-time algorithm instead of an optimal algorithm.
- Testing considerations: Test the algorithm with different input sizes and values to ensure correctness and performance.