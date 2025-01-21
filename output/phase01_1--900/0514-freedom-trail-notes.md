## Freedom Trail

**Problem Link:** https://leetcode.com/problems/freedom-trail/description

**Problem Statement:**
- Input format and constraints: The problem involves finding the maximum number of `#` characters that can be freed in a `ring` and a `key` string, with the given constraint that the ring can only be rotated in a clockwise direction and the key string must be matched from left to right.
- Expected output format: The output should be the maximum number of `#` characters that can be freed.
- Key requirements and edge cases to consider: The key string must be matched from left to right, and the ring can only be rotated in a clockwise direction.
- Example test cases with explanations: 
    - `ring = "godding"`, `key = "godding"`: The maximum number of `#` characters that can be freed is `5`.
    - `ring = "godding"`, `key = "god"`: The maximum number of `#` characters that can be freed is `3`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can start by trying all possible rotations of the ring and checking if the key string can be matched from left to right.
- Step-by-step breakdown of the solution:
    1. Generate all possible rotations of the ring.
    2. For each rotation, try to match the key string from left to right.
    3. If a match is found, calculate the number of `#` characters that can be freed.
- Why this approach comes to mind first: It is a straightforward approach that tries all possible solutions.

```cpp
class Solution {
public:
    int findRotateSteps(string ring, string key) {
        int n = ring.size();
        int m = key.size();
        int minSteps = INT_MAX;
        
        for (int i = 0; i < n; i++) {
            string rotatedRing = ring.substr(i) + ring.substr(0, i);
            int steps = 0;
            int j = 0;
            
            for (char c : key) {
                int k;
                for (k = j; k < n; k++) {
                    if (rotatedRing[k] == c) {
                        break;
                    }
                }
                steps += min(k - j, n - k + j + 1);
                j = k;
            }
            
            minSteps = min(minSteps, steps);
        }
        
        return minSteps;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot m)$, where $n$ is the length of the ring and $m$ is the length of the key.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the ring.
> - **Why these complexities occur:** The time complexity is due to the nested loops over the ring and the key, and the space complexity is due to the storage of the rotated ring.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use dynamic programming to store the minimum steps required to match the key string up to each character in the ring.
- Detailed breakdown of the approach:
    1. Create a 2D array `dp` where `dp[i][j]` stores the minimum steps required to match the key string up to the `j`-th character in the ring, starting from the `i`-th character.
    2. Initialize the base case where the key string is empty.
    3. Fill in the `dp` array using the recurrence relation: `dp[i][j] = min(dp[i-1][j-1] + 1, dp[i-1][j] + 1)`.
- Proof of optimality: The dynamic programming approach ensures that we consider all possible rotations of the ring and match the key string from left to right, resulting in the minimum number of steps.

```cpp
class Solution {
public:
    int findRotateSteps(string ring, string key) {
        int n = ring.size();
        int m = key.size();
        vector<vector<int>> dp(n, vector<int>(m, INT_MAX));
        
        for (int i = 0; i < n; i++) {
            if (ring[i] == key[0]) {
                dp[i][0] = min(i, n - i);
            }
        }
        
        for (int j = 1; j < m; j++) {
            for (int i = 0; i < n; i++) {
                if (ring[i] == key[j]) {
                    for (int k = 0; k < n; k++) {
                        if (ring[k] == key[j-1]) {
                            dp[i][j] = min(dp[i][j], dp[k][j-1] + min(abs(i-k), n-abs(i-k)));
                        }
                    }
                }
            }
        }
        
        int minSteps = INT_MAX;
        for (int i = 0; i < n; i++) {
            minSteps = min(minSteps, dp[i][m-1]);
        }
        
        return minSteps;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot m)$, where $n$ is the length of the ring and $m$ is the length of the key.
> - **Space Complexity:** $O(n \cdot m)$, where $n$ is the length of the ring and $m$ is the length of the key.
> - **Optimality proof:** The dynamic programming approach ensures that we consider all possible rotations of the ring and match the key string from left to right, resulting in the minimum number of steps.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, string matching.
- Problem-solving patterns identified: Using dynamic programming to store the minimum steps required to match the key string up to each character in the ring.
- Optimization techniques learned: Using the recurrence relation to fill in the `dp` array.
- Similar problems to practice: String matching, dynamic programming.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the base case correctly, not filling in the `dp` array correctly.
- Edge cases to watch for: When the key string is empty, when the ring is empty.
- Performance pitfalls: Using a brute force approach, not using dynamic programming to store the minimum steps required.
- Testing considerations: Testing the function with different inputs, including edge cases.