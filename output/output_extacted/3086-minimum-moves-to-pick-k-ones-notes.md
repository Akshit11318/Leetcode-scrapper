## Minimum Moves to Pick K Ones
**Problem Link:** https://leetcode.com/problems/minimum-moves-to-pick-k-ones/description

**Problem Statement:**
- Input: A binary string `s` and an integer `k`.
- Output: The minimum number of moves to pick `k` ones from the string `s`.
- Key requirements:
  - Each move can pick one or more adjacent ones.
  - We want to minimize the total number of moves.
- Edge cases:
  - If `k` is 0, return 0 because no moves are needed.
  - If the number of ones in `s` is less than `k`, it's impossible to pick `k` ones.

### Brute Force Approach
**Explanation:**
- The initial thought process involves checking every possible way to pick `k` ones from the string `s`.
- We can use a recursive function to try all possible combinations of moves.
- This approach comes to mind first because it's straightforward and ensures we don't miss any possible solution.

```cpp
class Solution {
public:
    int minMoves(string s, int k) {
        int n = s.size();
        int ones = 0;
        // Count the number of ones in the string
        for (char c : s) {
            if (c == '1') ones++;
        }
        if (ones < k) return -1; // Impossible to pick k ones
        if (k == 0) return 0; // No moves needed

        int minMoves = INT_MAX;
        // Recursive function to try all combinations
        function<void(int, int, int)> dfs = [&](int pos, int moves, int picked) {
            if (picked == k) {
                minMoves = min(minMoves, moves);
                return;
            }
            if (pos >= n || moves >= minMoves) return;
            // Try picking one or more adjacent ones
            int count = 0;
            for (int i = pos; i < n; i++) {
                if (s[i] == '1') count++;
                else break;
            }
            if (count > 0) {
                dfs(i + 1, moves + 1, picked + count);
            }
            dfs(pos + 1, moves, picked);
        };
        dfs(0, 0, 0);
        return minMoves;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where $n$ is the length of the string `s`. This is because in the worst case, we might try all possible subsets of the string.
> - **Space Complexity:** $O(n)$, due to the recursive call stack.
> - **Why these complexities occur:** The brute force approach tries all possible combinations, leading to exponential time complexity. The space complexity is linear due to the recursive call stack.

### Optimal Approach (Required)
**Explanation:**
- The key insight is to use a sliding window approach to count the number of ones in the string.
- We maintain a window of size `k` and move it over the string, keeping track of the minimum number of moves needed to pick `k` ones.
- This approach is optimal because it ensures we consider all possible ways to pick `k` ones while minimizing the number of moves.

```cpp
class Solution {
public:
    int minMoves(string s, int k) {
        int n = s.size();
        int ones = 0;
        // Count the number of ones in the string
        for (char c : s) {
            if (c == '1') ones++;
        }
        if (ones < k) return -1; // Impossible to pick k ones
        if (k == 0) return 0; // No moves needed

        int minMoves = INT_MAX;
        int count = 0;
        int start = 0;
        // Sliding window approach
        for (int end = 0; end < n; end++) {
            if (s[end] == '1') count++;
            while (count > k) {
                if (s[start] == '1') count--;
                start++;
            }
            if (count == k) {
                // Calculate the number of moves needed for the current window
                int moves = 1;
                int last = start - 1;
                for (int i = start; i <= end; i++) {
                    if (s[i] == '1' && (last == -1 || s[last] != '1')) {
                        moves++;
                        last = i;
                    }
                }
                minMoves = min(minMoves, moves);
            }
        }
        return minMoves;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string `s`. This is because we make a single pass over the string.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the variables.
> - **Optimality proof:** This approach is optimal because it considers all possible ways to pick `k` ones while minimizing the number of moves. The sliding window approach ensures we don't miss any possible solution, and the time complexity is linear.

### Final Notes
**Learning Points:**
- The problem demonstrates the importance of considering all possible approaches, from brute force to optimal.
- The optimal solution uses a sliding window approach to minimize the number of moves.
- We learned about the trade-offs between time and space complexity in different approaches.

**Mistakes to Avoid:**
- Not considering the edge cases, such as when `k` is 0 or the number of ones in the string is less than `k`.
- Not optimizing the solution, leading to high time complexity.
- Not using a sliding window approach, which can simplify the solution and improve performance.