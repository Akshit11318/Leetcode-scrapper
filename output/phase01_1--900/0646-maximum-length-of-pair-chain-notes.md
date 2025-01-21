## Maximum Length of Pair Chain

**Problem Link:** https://leetcode.com/problems/maximum-length-of-pair-chain/description

**Problem Statement:**
- Input: A list of pairs of integers `pairs` where each pair represents the start and end of a pair chain.
- Constraints: $1 \leq n \leq 10^5$ where $n$ is the number of pairs.
- Expected Output: The maximum length of a pair chain that can be formed from the given pairs.
- Key Requirements:
  - A pair chain can be formed by selecting pairs such that for any two consecutive pairs, the end of the first pair is less than the start of the second pair.
- Edge Cases:
  - If the input list is empty, return 0.
  - If no pair chain can be formed, return 0.

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible combinations of pairs and check if they can form a valid pair chain.
- Step-by-step breakdown:
  1. Generate all possible combinations of pairs.
  2. For each combination, check if it forms a valid pair chain by verifying that the end of each pair is less than the start of the next pair.
  3. Keep track of the maximum length of a valid pair chain found so far.
- Why this approach comes to mind first: It's a straightforward approach that considers all possibilities.

```cpp
#include <vector>
#include <algorithm>

int findLongestChain(std::vector<std::vector<int>>& pairs) {
    std::sort(pairs.begin(), pairs.end(), [](const std::vector<int>& a, const std::vector<int>& b) {
        return a[1] < b[1];
    });

    int count = 0;
    int prevEnd = INT_MIN;

    for (const auto& pair : pairs) {
        if (pair[0] > prevEnd) {
            count++;
            prevEnd = pair[1];
        }
    }

    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to sorting the pairs.
> - **Space Complexity:** $O(1)$ excluding the input and output, as we only use a constant amount of space.
> - **Why these complexities occur:** The time complexity is dominated by the sorting operation, which is necessary to ensure that we consider pairs in the order of their end values.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: We can use a greedy approach to find the maximum length of a pair chain. The idea is to always choose the pair with the smallest end value that does not conflict with the previously chosen pair.
- Detailed breakdown:
  1. Sort the pairs by their end values.
  2. Initialize the count of pairs in the chain to 0 and the end of the previous pair to negative infinity.
  3. Iterate over the sorted pairs. For each pair, if its start value is greater than the end of the previous pair, increment the count and update the end of the previous pair.
- Proof of optimality: This approach is optimal because it ensures that we always choose the pair that allows us to extend the chain the most. By sorting the pairs by their end values, we guarantee that we consider all possible pairs in the order that maximizes the length of the chain.

```cpp
int findLongestChain(std::vector<std::vector<int>>& pairs) {
    std::sort(pairs.begin(), pairs.end(), [](const std::vector<int>& a, const std::vector<int>& b) {
        return a[1] < b[1];
    });

    int count = 0;
    int prevEnd = INT_MIN;

    for (const auto& pair : pairs) {
        if (pair[0] > prevEnd) {
            count++;
            prevEnd = pair[1];
        }
    }

    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to sorting the pairs.
> - **Space Complexity:** $O(1)$ excluding the input and output, as we only use a constant amount of space.
> - **Optimality proof:** This approach is optimal because it uses a greedy strategy that always chooses the pair that maximizes the length of the chain, and it does so in a way that considers all possible pairs.

---

### Final Notes

**Learning Points:**
- Key algorithmic concept: Greedy algorithm.
- Problem-solving pattern: Sorting and iterating over the sorted data to find the optimal solution.
- Optimization technique: Using a greedy approach to reduce the time complexity.

**Mistakes to Avoid:**
- Not sorting the pairs by their end values, which can lead to incorrect results.
- Not updating the end of the previous pair correctly, which can lead to incorrect results.
- Not considering all possible pairs, which can lead to incorrect results.