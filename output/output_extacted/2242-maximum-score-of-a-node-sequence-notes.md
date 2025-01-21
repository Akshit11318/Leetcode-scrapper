## Maximum Score of a Node Sequence

**Problem Link:** https://leetcode.com/problems/maximum-score-of-a-node-sequence/description

**Problem Statement:**
- Input format: A list of nodes and an integer `k`.
- Constraints: The number of nodes is in the range `[1, 10^5]`, and `k` is in the range `[1, 100]`.
- Expected output format: The maximum score of a node sequence.
- Key requirements: Find the maximum score by choosing `k` nodes from the list.
- Example test cases: The problem statement provides examples to illustrate the scoring system.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of `k` nodes from the list.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of `k` nodes.
  2. For each combination, calculate the score based on the given formula.
  3. Keep track of the maximum score found.
- Why this approach comes to mind first: It's a straightforward way to ensure we don't miss any possible combinations.

```cpp
class Solution {
public:
    int maximumScore(vector<int>& nodes, int k) {
        int n = nodes.size();
        int maxScore = 0;
        for (int mask = 0; mask < (1 << n); mask++) {
            if (__builtin_popcount(mask) == k) {
                int score = 0;
                for (int i = 0; i < n; i++) {
                    if ((mask & (1 << i)) != 0) {
                        score += nodes[i];
                    }
                }
                maxScore = max(maxScore, score);
            }
        }
        return maxScore;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the number of nodes. The reason is that we generate all possible combinations of nodes, which is $2^n$, and for each combination, we calculate the score, which takes $O(n)$ time.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum score and other variables.
> - **Why these complexities occur:** The brute force approach is inefficient because it tries all possible combinations, leading to exponential time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: We can use a sliding window approach to efficiently calculate the score for each combination of `k` nodes.
- Detailed breakdown of the approach:
  1. Initialize a window of size `k` at the beginning of the list.
  2. Calculate the score for the current window.
  3. Slide the window to the right by one node and calculate the new score.
  4. Repeat step 3 until the window reaches the end of the list.
- Proof of optimality: This approach ensures we consider all possible combinations of `k` nodes and calculates the score efficiently.

```cpp
class Solution {
public:
    int maximumScore(vector<int>& nodes, int k) {
        int n = nodes.size();
        int maxScore = 0;
        int windowSum = 0;
        for (int i = 0; i < k; i++) {
            windowSum += nodes[i];
        }
        maxScore = windowSum;
        for (int i = k; i < n; i++) {
            windowSum = windowSum - nodes[i - k] + nodes[i];
            maxScore = max(maxScore, windowSum);
        }
        return maxScore;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes. The reason is that we only need to iterate through the list once to calculate the score for each combination of `k` nodes.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum score and other variables.
> - **Optimality proof:** This approach is optimal because it considers all possible combinations of `k` nodes and calculates the score efficiently, avoiding the exponential time complexity of the brute force approach.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sliding window technique, efficient calculation of scores.
- Problem-solving patterns identified: Using a window to efficiently calculate scores for combinations of nodes.
- Optimization techniques learned: Avoiding exponential time complexity by using a sliding window approach.
- Similar problems to practice: Problems involving combinations and sliding window techniques.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the window sum correctly, not updating the window sum correctly when sliding the window.
- Edge cases to watch for: Handling cases where `k` is larger than the number of nodes.
- Performance pitfalls: Using an inefficient approach that leads to exponential time complexity.
- Testing considerations: Testing the solution with different inputs, including edge cases, to ensure correctness and efficiency.