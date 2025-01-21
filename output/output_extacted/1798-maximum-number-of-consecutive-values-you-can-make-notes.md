## Maximum Number of Consecutive Values You Can Make

**Problem Link:** https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/description

**Problem Statement:**
- Input: An array of integers `coins` representing different denominations of coins.
- Output: The maximum number of consecutive values that can be made using these coins.
- Key requirements: The function should return the maximum number of consecutive values starting from 1 that can be made by combining the given coins.
- Example test cases:
  - Input: `coins = [1, 2, 5]`
  - Output: `30`
  - Explanation: We can make the following consecutive values: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to generate all possible combinations of the given coins and check if they can make consecutive values.
- However, this approach is inefficient and not scalable for large inputs.

```cpp
class Solution {
public:
    int getMaximumConsecutive(vector<int>& coins) {
        int maxConsecutive = 0;
        unordered_set<int> made;
        made.insert(0);
        for (int coin : coins) {
            unordered_set<int> temp = made;
            for (int value : temp) {
                if (!made.count(value + coin)) {
                    made.insert(value + coin);
                }
            }
        }
        while (made.count(maxConsecutive)) {
            maxConsecutive++;
        }
        return maxConsecutive;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times m)$, where $n$ is the number of coins and $m$ is the maximum consecutive value that can be made.
> - **Space Complexity:** $O(m)$, where $m$ is the maximum consecutive value that can be made.
> - **Why these complexities occur:** The brute force approach generates all possible combinations of coins and checks if they can make consecutive values, resulting in high time and space complexities.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a `greedy` approach. We can make all values from 1 to the sum of the coins if we have a coin of denomination 1.
- We can then sort the coins in ascending order and try to make the maximum consecutive value.

```cpp
class Solution {
public:
    int getMaximumConsecutive(vector<int>& coins) {
        sort(coins.begin(), coins.end());
        int sum = 1;
        for (int coin : coins) {
            if (coin > sum) {
                break;
            }
            sum += coin;
        }
        return sum;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of coins.
> - **Space Complexity:** $O(1)$, as we are not using any extra space.
> - **Optimality proof:** This approach is optimal because we are using the smallest coin to make the largest possible consecutive value.

---

### Final Notes

**Learning Points:**
- The key algorithmic concept demonstrated is the use of a greedy approach to solve the problem.
- The problem-solving pattern identified is to use sorting to arrange the coins in ascending order.
- The optimization technique learned is to use the smallest coin to make the largest possible consecutive value.

**Mistakes to Avoid:**
- A common implementation error is to use a brute force approach that generates all possible combinations of coins.
- An edge case to watch for is when the input array is empty or contains only one coin.
- A performance pitfall is to use a high-time-complexity algorithm that is not scalable for large inputs.