## Stickers to Spell Word
**Problem Link:** https://leetcode.com/problems/stickers-to-spell-word/description

**Problem Statement:**
- Input format and constraints: Given an array of strings `stickers` and a string `target`, find the minimum number of stickers to spell out `target`. Each sticker can only be used once.
- Expected output format: Return the minimum number of stickers. If it is impossible to spell out `target`, return -1.
- Key requirements and edge cases to consider: 
  - Each sticker can only be used once.
  - The stickers can contain duplicate characters.
  - The target string can contain duplicate characters.
- Example test cases with explanations:
  - `stickers = ["with","example","science"], target = "theexample"`: The minimum number of stickers to spell out `target` is 2.
  - `stickers = ["with","example","science"], target = "theexamplescience"`: The minimum number of stickers to spell out `target` is 3.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of stickers to spell out the target string.
- Step-by-step breakdown of the solution:
  1. Generate all possible subsets of stickers.
  2. For each subset, check if it can spell out the target string.
  3. If a subset can spell out the target string, update the minimum number of stickers.
- Why this approach comes to mind first: It is a straightforward approach to try all possible combinations of stickers.

```cpp
class Solution {
public:
    int minStickers(vector<string>& stickers, string target) {
        int n = target.size();
        vector<int> dp(1 << n, -1);
        dp[0] = 0;
        for (int mask = 0; mask < (1 << n); mask++) {
            if (dp[mask] == -1) continue;
            for (string& sticker : stickers) {
                int next_mask = mask;
                for (char c : sticker) {
                    for (int i = 0; i < n; i++) {
                        if ((next_mask >> i) & 1) continue;
                        if (target[i] == c) {
                            next_mask |= (1 << i);
                        }
                    }
                }
                if (dp[next_mask] == -1 || dp[next_mask] > dp[mask] + 1) {
                    dp[next_mask] = dp[mask] + 1;
                }
            }
        }
        return dp[(1 << n) - 1];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot m \cdot k)$, where $n$ is the length of the target string, $m$ is the number of stickers, and $k$ is the average length of a sticker. This is because we generate all possible subsets of stickers and for each subset, we check if it can spell out the target string.
> - **Space Complexity:** $O(2^n)$, where $n$ is the length of the target string. This is because we need to store the minimum number of stickers for each subset of the target string.
> - **Why these complexities occur:** The time complexity occurs because we generate all possible subsets of stickers and for each subset, we check if it can spell out the target string. The space complexity occurs because we need to store the minimum number of stickers for each subset of the target string.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use dynamic programming to store the minimum number of stickers for each subset of the target string.
- Detailed breakdown of the approach:
  1. Initialize a dynamic programming array `dp` of size $2^n$, where $n$ is the length of the target string.
  2. For each sticker, update the dynamic programming array `dp` by checking if the sticker can spell out any character in the target string.
  3. Return the minimum number of stickers for the full target string.
- Proof of optimality: This approach is optimal because it uses dynamic programming to store the minimum number of stickers for each subset of the target string, which avoids redundant computation.

```cpp
class Solution {
public:
    int minStickers(vector<string>& stickers, string target) {
        int n = target.size();
        vector<int> dp(1 << n, -1);
        dp[0] = 0;
        for (int mask = 0; mask < (1 << n); mask++) {
            if (dp[mask] == -1) continue;
            for (string& sticker : stickers) {
                int next_mask = mask;
                for (char c : sticker) {
                    for (int i = 0; i < n; i++) {
                        if ((next_mask >> i) & 1) continue;
                        if (target[i] == c) {
                            next_mask |= (1 << i);
                        }
                    }
                }
                if (dp[next_mask] == -1 || dp[next_mask] > dp[mask] + 1) {
                    dp[next_mask] = dp[mask] + 1;
                }
            }
        }
        return dp[(1 << n) - 1];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot m \cdot k)$, where $n$ is the length of the target string, $m$ is the number of stickers, and $k$ is the average length of a sticker.
> - **Space Complexity:** $O(2^n)$, where $n$ is the length of the target string.
> - **Optimality proof:** This approach is optimal because it uses dynamic programming to store the minimum number of stickers for each subset of the target string, which avoids redundant computation.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, bitmasking.
- Problem-solving patterns identified: Using dynamic programming to store the minimum number of stickers for each subset of the target string.
- Optimization techniques learned: Avoiding redundant computation by using dynamic programming.
- Similar problems to practice: Other dynamic programming problems, such as the `0/1 Knapsack Problem`.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the dynamic programming array correctly, not updating the dynamic programming array correctly.
- Edge cases to watch for: The target string is empty, the stickers are empty.
- Performance pitfalls: Not using dynamic programming to store the minimum number of stickers for each subset of the target string, which can lead to redundant computation.
- Testing considerations: Test the function with different inputs, such as an empty target string, an empty stickers array, and a target string that cannot be spelled out by the stickers.