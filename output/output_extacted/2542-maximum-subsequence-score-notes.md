## Maximum Subsequence Score

**Problem Link:** https://leetcode.com/problems/maximum-subsequence-score/description

**Problem Statement:**
- Given two sequences `seq1` and `seq2`, calculate the maximum score that can be achieved by taking a subsequence from both sequences and summing their corresponding scores.
- The score of a subsequence is the sum of the scores of its elements.
- The goal is to find the maximum score that can be achieved by taking a subsequence from both sequences.
- The input consists of two sequences `seq1` and `seq2`, and two scores `score1` and `score2`.
- The output should be the maximum score that can be achieved.

**Example Test Cases:**
- `seq1 = [2,3,1]`, `seq2 = [3,1,2]`, `score1 = [10,5,8]`, `score2 = [5,8,12]`
- The maximum score is `10 + 8 + 12 = 30`, which is achieved by taking the subsequence `[2,1]` from `seq1` and `[3,2]` from `seq2`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to generate all possible subsequences from both sequences and calculate their scores.
- Then, we can find the maximum score among all possible subsequences.
- This approach comes to mind first because it is a straightforward way to solve the problem.

```cpp
int maxScore(vector<int>& seq1, vector<int>& seq2, vector<int>& score1, vector<int>& score2) {
    int n = seq1.size();
    int m = seq2.size();
    int maxScore = 0;
    
    // Generate all possible subsequences from seq1
    for (int i = 0; i < (1 << n); i++) {
        vector<int> subseq1;
        for (int j = 0; j < n; j++) {
            if ((i & (1 << j)) != 0) {
                subseq1.push_back(seq1[j]);
            }
        }
        
        // Generate all possible subsequences from seq2
        for (int k = 0; k < (1 << m); k++) {
            vector<int> subseq2;
            for (int l = 0; l < m; l++) {
                if ((k & (1 << l)) != 0) {
                    subseq2.push_back(seq2[l]);
                }
            }
            
            // Calculate the score of the current subsequences
            int score = 0;
            for (int p = 0; p < subseq1.size(); p++) {
                for (int q = 0; q < subseq2.size(); q++) {
                    if (subseq1[p] == subseq2[q]) {
                        score += score1[p] + score2[q];
                    }
                }
            }
            
            // Update the maximum score
            maxScore = max(maxScore, score);
        }
    }
    
    return maxScore;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot 2^m \cdot n \cdot m)$, where $n$ and $m$ are the lengths of the input sequences.
> - **Space Complexity:** $O(n + m)$, where $n$ and $m$ are the lengths of the input sequences.
> - **Why these complexities occur:** The brute force approach generates all possible subsequences from both sequences, which results in exponential time complexity. The space complexity is linear because we only need to store the current subsequences.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use dynamic programming to calculate the maximum score.
- We can create a 2D table `dp` where `dp[i][j]` represents the maximum score that can be achieved by taking a subsequence from the first `i` elements of `seq1` and the first `j` elements of `seq2`.
- We can fill up the table using the following recurrence relation: `dp[i][j] = max(dp[i-1][j-1] + score1[i-1] + score2[j-1], dp[i-1][j], dp[i][j-1])`.
- This approach is optimal because it avoids redundant calculations and has a polynomial time complexity.

```cpp
int maxScore(vector<int>& seq1, vector<int>& seq2, vector<int>& score1, vector<int>& score2) {
    int n = seq1.size();
    int m = seq2.size();
    vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));
    
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            if (seq1[i-1] == seq2[j-1]) {
                dp[i][j] = dp[i-1][j-1] + score1[i-1] + score2[j-1];
            } else {
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
            }
        }
    }
    
    return dp[n][m];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ and $m$ are the lengths of the input sequences.
> - **Space Complexity:** $O(n \cdot m)$, where $n$ and $m$ are the lengths of the input sequences.
> - **Optimality proof:** The dynamic programming approach avoids redundant calculations and has a polynomial time complexity, making it the optimal solution.

---

### Final Notes

**Learning Points:**
- The importance of dynamic programming in solving problems with overlapping subproblems.
- The use of 2D tables to store intermediate results.
- The avoidance of redundant calculations to improve time complexity.

**Mistakes to Avoid:**
- Using brute force approaches for problems with exponential time complexity.
- Not considering the use of dynamic programming for problems with overlapping subproblems.
- Not optimizing the space complexity of the solution.