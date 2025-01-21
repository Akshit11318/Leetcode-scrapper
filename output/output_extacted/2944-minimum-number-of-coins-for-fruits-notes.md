## Minimum Number of Coins for Fruits
**Problem Link:** https://leetcode.com/problems/minimum-number-of-coins-for-fruits/description

**Problem Statement:**
- Input format: `fruits` array of integers and `coins` array of integers.
- Constraints: $1 \leq n \leq 10^5$, where $n$ is the number of fruits.
- Expected output format: The minimum number of coins needed to buy all fruits.
- Key requirements: Each fruit can be bought with a specific number of coins.
- Edge cases: Consider cases where the number of fruits is large, and the number of coins is limited.

Example test cases:
- `fruits = [1,2,3,4,5]`, `coins = [3,2,1,4,5]`, output: `14`.
- `fruits = [10,20,30]`, `coins = [5,10,15]`, output: `60`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to try all possible combinations of coins for each fruit.
- Step-by-step breakdown:
  1. For each fruit, calculate the minimum number of coins needed to buy it.
  2. Try all possible combinations of coins for each fruit.
  3. Calculate the total number of coins needed for each combination.
  4. Return the minimum total number of coins.

```cpp
int minCoins(vector<int>& fruits, vector<int>& coins) {
    int n = fruits.size();
    int minCoins = INT_MAX;
    for (int mask = 0; mask < (1 << n); mask++) {
        int totalCoins = 0;
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                totalCoins += coins[i];
            }
        }
        minCoins = min(minCoins, totalCoins);
    }
    return minCoins;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where $n$ is the number of fruits. This is because we are trying all possible combinations of coins for each fruit.
> - **Space Complexity:** $O(1)$, as we are not using any additional space that scales with input size.
> - **Why these complexities occur:** The brute force approach tries all possible combinations of coins for each fruit, resulting in exponential time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use dynamic programming to calculate the minimum number of coins needed for each fruit.
- Detailed breakdown:
  1. Create a dynamic programming table `dp` of size `n + 1`, where `dp[i]` represents the minimum number of coins needed to buy the first `i` fruits.
  2. Initialize `dp[0] = 0`, as we need 0 coins to buy 0 fruits.
  3. For each fruit `i` from 1 to `n`, calculate `dp[i]` by trying all possible combinations of coins for the current fruit and taking the minimum.

```cpp
int minCoins(vector<int>& fruits, vector<int>& coins) {
    int n = fruits.size();
    vector<int> dp(n + 1, INT_MAX);
    dp[0] = 0;
    for (int i = 1; i <= n; i++) {
        for (int j = 0; j < i; j++) {
            dp[i] = min(dp[i], dp[j] + coins[i - 1]);
        }
    }
    return dp[n];
}
```

However, the above solution does not consider the actual problem constraints. A more accurate solution would involve using a `map` to store the frequency of each fruit and then calculating the minimum number of coins needed.

```cpp
int minCoins(vector<int>& fruits, vector<int>& coins) {
    unordered_map<int, int> fruitCount;
    for (int fruit : fruits) {
        fruitCount[fruit]++;
    }
    int totalCoins = 0;
    for (auto& pair : fruitCount) {
        int fruit = pair.first;
        int count = pair.second;
        int coin = coins[fruit - 1];
        totalCoins += coin * count;
    }
    return totalCoins;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of fruits. This is because we are iterating over the fruits to calculate the frequency of each fruit.
> - **Space Complexity:** $O(n)$, as we are using a `map` to store the frequency of each fruit.
> - **Optimality proof:** This solution is optimal because it directly calculates the minimum number of coins needed to buy all fruits based on their frequencies.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, frequency counting.
- Problem-solving patterns identified: Using a `map` to store frequency of each fruit.
- Optimization techniques learned: Avoiding unnecessary iterations, using a `map` to store frequency.
- Similar problems to practice: Problems involving frequency counting, dynamic programming.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the dynamic programming table correctly.
- Edge cases to watch for: Cases where the number of fruits is large, and the number of coins is limited.
- Performance pitfalls: Using a brute force approach for large inputs.
- Testing considerations: Test the solution with different inputs, including edge cases.