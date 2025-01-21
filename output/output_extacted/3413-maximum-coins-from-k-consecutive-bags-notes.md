## Maximum Coins from K Consecutive Bags
**Problem Link:** https://leetcode.com/problems/maximum-coins-from-k-consecutive-bags/description

**Problem Statement:**
- Input: A list of integers `piles` representing the number of coins in each bag and an integer `k` representing the number of consecutive bags to choose.
- Constraints: $1 \leq k \leq \text{length of piles} \leq 1000$, $1 \leq \text{piles[i]} \leq 1000$.
- Expected Output: The maximum number of coins that can be obtained from `k` consecutive bags.
- Key Requirements: Choose `k` consecutive bags from the given list to maximize the sum of coins.

**Example Test Cases:**
- For `piles = [1,3,1,4,5]` and `k = 3`, the maximum coins that can be obtained is `4 + 5 + 3 = 12`.
- For `piles = [2,4,1,2,5,3,5,1,3,1]` and `k = 4`, the maximum coins that can be obtained is `5 + 3 + 5 + 1 = 14`.

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to check every possible combination of `k` consecutive bags and calculate the sum of coins for each combination.
- This approach involves iterating through the list of bags and for each starting point, calculating the sum of coins for the next `k` bags.

```cpp
class Solution {
public:
    int maxCoins(vector<int>& piles, int k) {
        int maxCoins = 0;
        for (int i = 0; i <= piles.size() - k; i++) {
            int sum = 0;
            for (int j = i; j < i + k; j++) {
                sum += piles[j];
            }
            maxCoins = max(maxCoins, sum);
        }
        return maxCoins;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k)$, where $n$ is the number of bags. This is because for each starting point, we are calculating the sum of the next `k` bags.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum sum of coins and the current sum.
> - **Why these complexities occur:** The time complexity is high because we are iterating through the list of bags and for each starting point, we are calculating the sum of the next `k` bags. The space complexity is low because we only use a constant amount of space.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight that leads to the optimal solution is to use a sliding window approach. Instead of recalculating the sum of coins for each starting point, we can maintain a running sum and update it as we slide the window.
- This approach involves initializing a window of size `k` and then sliding it through the list of bags, updating the maximum sum of coins at each step.

```cpp
class Solution {
public:
    int maxCoins(vector<int>& piles, int k) {
        int maxCoins = 0;
        int windowSum = 0;
        for (int i = 0; i < piles.size(); i++) {
            windowSum += piles[i];
            if (i >= k) {
                windowSum -= piles[i - k];
            }
            if (i >= k - 1) {
                maxCoins = max(maxCoins, windowSum);
            }
        }
        return maxCoins;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of bags. This is because we are iterating through the list of bags once.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum sum of coins and the current window sum.
> - **Optimality proof:** This approach is optimal because it has a linear time complexity, which is the best possible time complexity for this problem. We are only iterating through the list of bags once and updating the maximum sum of coins at each step.

---

### Final Notes
**Learning Points:**
- Key algorithmic concepts demonstrated: sliding window approach, maintaining a running sum.
- Problem-solving patterns identified: using a window to reduce the number of calculations.
- Optimization techniques learned: reducing the number of iterations, using a running sum to update the maximum sum.
- Similar problems to practice: problems that involve finding the maximum sum of a subarray, problems that involve using a sliding window approach.

**Mistakes to Avoid:**
- Common implementation errors: not updating the window sum correctly, not checking for the maximum sum of coins at each step.
- Edge cases to watch for: when `k` is equal to the number of bags, when `k` is greater than the number of bags.
- Performance pitfalls: using a brute force approach, not optimizing the solution for large inputs.
- Testing considerations: testing the solution with different inputs, testing the solution with edge cases.