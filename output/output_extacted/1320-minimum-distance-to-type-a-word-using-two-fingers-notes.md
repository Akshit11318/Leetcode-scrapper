## Minimum Distance to Type a Word Using Two Fingers
**Problem Link:** https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers/description

**Problem Statement:**
- Input: A string `word` representing the word to be typed.
- Constraints: The length of `word` is between 1 and 100.
- Expected Output: The minimum distance to type the word using two fingers.
- Key Requirements: Calculate the minimum distance based on the positions of the characters on a standard keyboard layout.
- Edge Cases: Consider cases where the word has a length of 1, and cases where the word has repeated characters.

**Example Test Cases:**
- Input: `word = "abcd"`
- Output: `6`
- Explanation: The minimum distance is calculated based on the positions of the characters on the keyboard.

---

### Brute Force Approach
**Explanation:**
- The brute force approach involves calculating the distance between each pair of characters in the word and summing them up.
- This approach considers all possible combinations of fingers for each character.
- The distance between two characters is calculated based on the Manhattan distance (L1 distance) between their positions on the keyboard.

```cpp
int minimumDistance(string word) {
    vector<vector<int>> keyboard = {{'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'},
                                    {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'},
                                    {'z', 'x', 'c', 'v', 'b', 'n', 'm'}};
    unordered_map<char, pair<int, int>> charPos;
    for (int i = 0; i < keyboard.size(); i++) {
        for (int j = 0; j < keyboard[i].size(); j++) {
            charPos[keyboard[i][j]] = {i, j};
        }
    }
    int n = word.size();
    vector<int> dp(n + 1, INT_MAX);
    dp[0] = 0;
    for (int i = 1; i <= n; i++) {
        for (int j = 0; j < i; j++) {
            int dist = abs(charPos[word[j - 1]].first - charPos[word[i - 1]].first) + abs(charPos[word[j - 1]].second - charPos[word[i - 1]].second);
            dp[i] = min(dp[i], dp[j] + dist);
        }
    }
    return dp[n];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the word. This is because we have two nested loops iterating over the word.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the word. This is because we use a dynamic programming array of size $n + 1$.
> - **Why these complexities occur:** The brute force approach has high time complexity due to the nested loops, and high space complexity due to the dynamic programming array.

---

### Optimal Approach (Required)
**Explanation:**
- The optimal approach involves using dynamic programming to calculate the minimum distance.
- We use a 2D array `dp` where `dp[i][j]` represents the minimum distance to type the first `i` characters of the word, with the last character typed by finger `j`.
- We initialize the `dp` array with infinity and set `dp[0][0]` and `dp[0][1]` to 0.
- We then iterate over the word and update the `dp` array based on the minimum distance to type the current character with each finger.

```cpp
int minimumDistance(string word) {
    vector<vector<int>> keyboard = {{'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'},
                                    {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'},
                                    {'z', 'x', 'c', 'v', 'b', 'n', 'm'}};
    unordered_map<char, pair<int, int>> charPos;
    for (int i = 0; i < keyboard.size(); i++) {
        for (int j = 0; j < keyboard[i].size(); j++) {
            charPos[keyboard[i][j]] = {i, j};
        }
    }
    int n = word.size();
    vector<vector<int>> dp(n + 1, vector<int>(2, INT_MAX));
    dp[0][0] = dp[0][1] = 0;
    for (int i = 1; i <= n; i++) {
        for (int j = 0; j < 2; j++) {
            for (int k = 0; k < 2; k++) {
                if (i == 1 || word[i - 1] != word[i - 2]) {
                    int dist = (i == 1) ? 0 : abs(charPos[word[i - 2]].first - charPos[word[i - 1]].first) + abs(charPos[word[i - 2]].second - charPos[word[i - 1]].second);
                    dp[i][j] = min(dp[i][j], dp[i - 1][k] + dist);
                }
            }
        }
    }
    return min(dp[n][0], dp[n][1]);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the word. This is because we have a single loop iterating over the word.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the word. This is because we use a 2D dynamic programming array of size $(n + 1) \times 2$.
> - **Optimality proof:** This approach is optimal because it considers all possible combinations of fingers for each character and uses dynamic programming to avoid redundant calculations.

---

### Final Notes

**Learning Points:**
- Dynamic programming can be used to solve problems with overlapping subproblems.
- The optimal approach uses a 2D array to store the minimum distance to type the first `i` characters of the word, with the last character typed by finger `j`.
- The time complexity of the optimal approach is $O(n)$, where $n$ is the length of the word.

**Mistakes to Avoid:**
- Not considering all possible combinations of fingers for each character.
- Not using dynamic programming to avoid redundant calculations.
- Not handling edge cases correctly, such as when the word has a length of 1 or has repeated characters.