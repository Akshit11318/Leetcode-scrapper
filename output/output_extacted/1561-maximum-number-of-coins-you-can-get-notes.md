## Maximum Number of Coins You Can Get
**Problem Link:** https://leetcode.com/problems/maximum-number-of-coins-you-can-get/description

**Problem Statement:**
- Input: `piles`, an array of integers representing the number of coins in each pile.
- Input format and constraints: `1 <= piles.length <= 1000`, `1 <= piles[i] <= 1000`.
- Expected output format: The maximum number of coins that can be obtained by Alice.
- Key requirements and edge cases to consider:
  - Alice takes the first turn.
  - Players can only take one pile per turn.
  - The game ends when all piles are taken.
- Example test cases with explanations:
  - Example 1: `piles = [2,4,1,2,7,8]`, Alice can take the largest pile first and then Bob takes a pile, and so on.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible combinations of moves and calculate the maximum coins that can be obtained by Alice.
- Step-by-step breakdown of the solution:
  1. Initialize the maximum coins that can be obtained by Alice to 0.
  2. Generate all possible combinations of moves.
  3. For each combination, calculate the coins that can be obtained by Alice.
  4. Update the maximum coins if the current combination results in more coins.
- Why this approach comes to mind first: It's a straightforward approach to try all possible combinations and see which one results in the maximum coins.

```cpp
class Solution {
public:
    int maxCoins(vector<int>& piles) {
        int n = piles.size();
        int maxCoins = 0;
        for (int mask = 0; mask < (1 << n); mask++) {
            int coins = 0;
            vector<bool> taken(n, false);
            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) != 0) {
                    taken[i] = true;
                    coins += piles[i];
                }
            }
            if (count(taken.begin(), taken.end(), true) % 2 == 1) {
                maxCoins = max(maxCoins, coins);
            }
        }
        return maxCoins;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the number of piles. This is because we generate all possible combinations of moves and calculate the coins for each combination.
> - **Space Complexity:** $O(n)$, where $n$ is the number of piles. This is because we need to store the `taken` array to keep track of the piles that have been taken.
> - **Why these complexities occur:** The brute force approach tries all possible combinations of moves, resulting in exponential time complexity. The space complexity is linear because we only need to store the `taken` array.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a greedy approach to solve this problem. Since Alice takes the first turn, she can always take the largest pile first.
- Detailed breakdown of the approach:
  1. Sort the piles in descending order.
  2. Alice takes the first $n/3$ piles.
  3. Calculate the sum of the coins in the piles taken by Alice.
- Proof of optimality: This approach is optimal because Alice takes the largest piles first, maximizing her chances of getting the most coins.

```cpp
class Solution {
public:
    int maxCoins(vector<int>& piles) {
        int n = piles.size();
        sort(piles.begin(), piles.end());
        int coins = 0;
        for (int i = n - 2; i >= n - 2 * n / 3; i--) {
            coins += piles[i];
        }
        return coins;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of piles. This is because we sort the piles in descending order.
> - **Space Complexity:** $O(1)$, where $n$ is the number of piles. This is because we only need to use a constant amount of space to store the `coins` variable.
> - **Optimality proof:** This approach is optimal because Alice takes the largest piles first, maximizing her chances of getting the most coins.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Greedy algorithm, sorting.
- Problem-solving patterns identified: Using a greedy approach to solve optimization problems.
- Optimization techniques learned: Sorting the input to solve optimization problems.
- Similar problems to practice: Other optimization problems that can be solved using a greedy approach.

**Mistakes to Avoid:**
- Common implementation errors: Not sorting the input correctly.
- Edge cases to watch for: Handling the case where the number of piles is not a multiple of 3.
- Performance pitfalls: Using a brute force approach to solve the problem.
- Testing considerations: Testing the solution with different inputs to ensure it works correctly.