## Number of Music Playlists

**Problem Link:** https://leetcode.com/problems/number-of-music-playlists/description

**Problem Statement:**
- Input: `n` (number of unique songs), `goal` (number of songs to include in the playlist), `k` (number of songs to repeat in the playlist)
- Expected output: The number of unique music playlists that can be created
- Key requirements and edge cases to consider:
  - The order of songs matters
  - Each song can be included in the playlist more than once
  - At most `k` songs can be repeated
- Example test cases with explanations:
  - `n = 3`, `goal = 3`, `k = 1`: There are 6 unique playlists that can be created
  - `n = 3`, `goal = 3`, `k = 2`: There are 6 unique playlists that can be created

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to generate all possible playlists and count the unique ones
- Step-by-step breakdown of the solution:
  1. Generate all possible playlists of length `goal`
  2. For each playlist, check if it contains at most `k` repeated songs
  3. Count the unique playlists that meet the condition
- Why this approach comes to mind first: It is a straightforward and intuitive approach, but it has high time complexity due to the large number of possible playlists

```cpp
int numMusicPlaylists(int n, int goal, int k) {
    int count = 0;
    vector<vector<int>> playlists;
    // Generate all possible playlists
    generatePlaylists(playlists, n, goal);
    // Count unique playlists with at most k repeated songs
    for (auto& playlist : playlists) {
        if (isValidPlaylist(playlist, k)) {
            count++;
        }
    }
    return count;
}

void generatePlaylists(vector<vector<int>>& playlists, int n, int goal) {
    vector<int> currentPlaylist;
    generatePlaylistsHelper(playlists, currentPlaylist, n, goal);
}

void generatePlaylistsHelper(vector<vector<int>>& playlists, vector<int>& currentPlaylist, int n, int goal) {
    if (currentPlaylist.size() == goal) {
        playlists.push_back(currentPlaylist);
        return;
    }
    for (int i = 1; i <= n; i++) {
        currentPlaylist.push_back(i);
        generatePlaylistsHelper(playlists, currentPlaylist, n, goal);
        currentPlaylist.pop_back();
    }
}

bool isValidPlaylist(vector<int>& playlist, int k) {
    unordered_map<int, int> songCount;
    for (int song : playlist) {
        songCount[song]++;
    }
    int repeatedSongs = 0;
    for (auto& pair : songCount) {
        if (pair.second > 1) {
            repeatedSongs++;
        }
    }
    return repeatedSongs <= k;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^goal)$ (generating all possible playlists) + $O(goal \cdot n)$ (counting unique playlists) = $O(n^goal)$
> - **Space Complexity:** $O(n^goal)$ (storing all possible playlists)
> - **Why these complexities occur:** The brute force approach generates all possible playlists, which results in high time and space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use dynamic programming to store the number of unique playlists for each subproblem
- Detailed breakdown of the approach:
  1. Initialize a 2D array `dp` to store the number of unique playlists for each subproblem
  2. Fill the `dp` array using the following recurrence relation:
    - `dp[i][j]` = number of unique playlists with `i` songs and `j` repeated songs
    - `dp[i][j]` = `dp[i-1][j-1]` + `dp[i-1][j]` \* `(i-1-j)`
  3. The final answer is stored in `dp[goal][k]`
- Why further optimization is impossible: The optimal approach has a time complexity of $O(goal \cdot k)$, which is the minimum required to solve the problem

```cpp
int numMusicPlaylists(int n, int goal, int k) {
    vector<vector<int>> dp(goal + 1, vector<int>(k + 1, 0));
    dp[0][0] = 1;
    for (int i = 1; i <= goal; i++) {
        for (int j = 0; j <= min(i, k); j++) {
            if (j > 0) {
                dp[i][j] += dp[i-1][j-1] * (n - j);
            }
            if (j < i) {
                dp[i][j] += dp[i-1][j] * j;
            }
        }
    }
    return dp[goal][k];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(goal \cdot k)$ (filling the `dp` array)
> - **Space Complexity:** $O(goal \cdot k)$ (storing the `dp` array)
> - **Optimality proof:** The optimal approach has a time complexity of $O(goal \cdot k)$, which is the minimum required to solve the problem. This is because we need to consider all possible subproblems to find the optimal solution.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: dynamic programming, recurrence relations
- Problem-solving patterns identified: breaking down the problem into subproblems and solving them recursively
- Optimization techniques learned: using dynamic programming to store the results of subproblems
- Similar problems to practice: problems that involve counting the number of unique solutions, such as permutations and combinations

**Mistakes to Avoid:**
- Common implementation errors: not initializing the `dp` array correctly, not handling the base cases correctly
- Edge cases to watch for: when `n` is small, when `goal` is small, when `k` is large
- Performance pitfalls: not using dynamic programming, not using memoization
- Testing considerations: testing the function with different inputs, testing the function with edge cases