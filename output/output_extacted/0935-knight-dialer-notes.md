## Knight Dialer

**Problem Link:** [https://leetcode.com/problems/knight-dialer/description](https://leetcode.com/problems/knight-dialer/description)

**Problem Statement:**
- Input format and constraints: The problem requires finding the number of distinct sequences of length `n` that can be formed using a knight on a dialer. The knight can move from one number to another if the two numbers are a knight's move apart on the dialer. The dialer has 10 numbers (0-9) arranged in a circular manner.
- Expected output format: The function should return the total number of distinct sequences of length `n`.
- Key requirements and edge cases to consider: The function should handle edge cases such as `n = 1`, where the number of distinct sequences is equal to the number of possible starting positions (10). Another edge case is when `n = 0`, where the function should return 1, since there is only one way to form an empty sequence.
- Example test cases with explanations:
  - For `n = 1`, the function should return 10, since there are 10 possible starting positions.
  - For `n = 2`, the function should return 20, since each of the 10 starting positions has 2 possible next positions.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves generating all possible sequences of length `n` and counting the distinct ones.
- Step-by-step breakdown of the solution:
  1. Generate all possible sequences of length `n` using a recursive function.
  2. Count the distinct sequences using a `set` data structure.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it is inefficient due to the large number of possible sequences.

```cpp
#include <iostream>
#include <set>
#include <vector>

std::set<std::vector<int>> generateSequences(int n, int current, std::vector<int> sequence) {
    if (n == 0) {
        std::set<std::vector<int>> result;
        result.insert(sequence);
        return result;
    }

    std::set<std::vector<int>> result;
    std::vector<int> moves = {{-2, -1}, {-2, 1}, {-1, -2}, {-1, 2}, {1, -2}, {1, 2}, {2, -1}, {2, 1}};
    for (int i = 0; i < moves.size(); i++) {
        int next = (current + moves[i][0] * 3 + moves[i][1]) % 10;
        if (next < 0) next += 10;
        sequence.push_back(next);
        std::set<std::vector<int>> temp = generateSequences(n - 1, next, sequence);
        for (auto it = temp.begin(); it != temp.end(); it++) {
            result.insert(*it);
        }
        sequence.pop_back();
    }
    return result;
}

int knightDialer(int n) {
    std::set<std::vector<int>> result;
    for (int i = 0; i < 10; i++) {
        std::vector<int> sequence;
        sequence.push_back(i);
        std::set<std::vector<int>> temp = generateSequences(n - 1, i, sequence);
        for (auto it = temp.begin(); it != temp.end(); it++) {
            result.insert(*it);
        }
    }
    return result.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(8^n)$, where $n$ is the length of the sequence. This is because each recursive call generates 8 new sequences.
> - **Space Complexity:** $O(8^n)$, where $n$ is the length of the sequence. This is because we need to store all the generated sequences in the `set`.
> - **Why these complexities occur:** The brute force approach generates all possible sequences, which results in an exponential time and space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution involves using dynamic programming to store the number of distinct sequences of length `i` ending at each position.
- Detailed breakdown of the approach:
  1. Create a 2D array `dp` of size `(n + 1) x 10`, where `dp[i][j]` represents the number of distinct sequences of length `i` ending at position `j`.
  2. Initialize the base case `dp[1][j] = 1` for all `j`, since there is only one way to form a sequence of length 1 ending at each position.
  3. For each length `i` from 2 to `n`, calculate `dp[i][j]` by summing the number of distinct sequences of length `i - 1` ending at each position that can move to position `j`.
- Proof of optimality: The dynamic programming approach ensures that we only calculate each subproblem once, resulting in a time complexity of $O(n \cdot 10^2)$.
- Why further optimization is impossible: The dynamic programming approach is optimal because it has a time complexity that is linear in the input size `n` and polynomial in the number of positions `10`.

```cpp
int knightDialer(int n) {
    int dp[2][10] = {{1, 1, 1, 1, 1, 1, 1, 1, 1, 1}, {0}};
    int moves[10][8] = {
        {4, 6}, {6, 8}, {7, 9}, {4, 8}, {3, 9, 0}, {}, {1, 7, 0}, {2, 6}, {1, 3}, {2, 4}
    };

    for (int i = 2; i <= n; i++) {
        for (int j = 0; j < 10; j++) {
            for (int k = 0; k < 8; k++) {
                if (moves[j][k] != 0) {
                    dp[i % 2][j] += dp[(i - 1) % 2][moves[j][k]];
                }
            }
        }
    }

    int sum = 0;
    for (int i = 0; i < 10; i++) {
        sum += dp[n % 2][i];
    }
    return sum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot 10^2)$, where $n$ is the length of the sequence. This is because we need to calculate the number of distinct sequences for each length up to `n` and for each position.
> - **Space Complexity:** $O(10)$, where `10` is the number of positions. This is because we only need to store the number of distinct sequences for each position.
> - **Optimality proof:** The dynamic programming approach ensures that we only calculate each subproblem once, resulting in a time complexity that is linear in the input size `n` and polynomial in the number of positions `10`.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, memoization, and optimization techniques.
- Problem-solving patterns identified: The problem can be solved using a dynamic programming approach by storing the number of distinct sequences for each length and position.
- Optimization techniques learned: The dynamic programming approach ensures that we only calculate each subproblem once, resulting in a significant reduction in time complexity.
- Similar problems to practice: Other problems that can be solved using dynamic programming, such as the Fibonacci sequence, Longest Common Subsequence, and Shortest Path problems.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the base case correctly, not updating the dynamic programming table correctly, and not handling edge cases properly.
- Edge cases to watch for: The problem has edge cases such as `n = 1` and `n = 0`, which need to be handled separately.
- Performance pitfalls: The brute force approach has a high time complexity, which can result in performance issues for large inputs.
- Testing considerations: The problem requires testing for different inputs, including edge cases and large inputs, to ensure that the solution works correctly and efficiently.