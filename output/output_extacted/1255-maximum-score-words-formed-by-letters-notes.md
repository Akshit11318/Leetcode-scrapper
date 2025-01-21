## Maximum Score Words Formed by Letters
**Problem Link:** https://leetcode.com/problems/maximum-score-words-formed-by-letters/description

**Problem Statement:**
- Input format: You are given a list of words `words` and a list of letters `letters` along with their corresponding scores `score`.
- Constraints: The words can only be formed using the letters provided, and each letter can only be used as many times as it appears in the `letters` list.
- Expected output format: The maximum score that can be achieved by forming words from the given letters.
- Key requirements and edge cases to consider: 
    - The score of a word is the sum of the scores of its letters.
    - The goal is to find the combination of words that results in the highest total score.
    - If a word cannot be formed from the available letters, it should not be included in the solution.
- Example test cases with explanations:
    - `words = ["dog","cat","dad","good","god","bad","cad","dod"], letters = ["a","a","a","f","f","f","f","f","f","f","f"], score = [1,0,9,5,0,0,0,0,0,0,0]`
    - The maximum score can be achieved by forming the words "dad" and "god" or other combinations that result in the highest score.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Try all possible combinations of words to find the one that results in the highest score.
- Step-by-step breakdown of the solution: 
    1. Generate all possible subsets of the given words.
    2. For each subset, check if it can be formed using the available letters.
    3. Calculate the total score for each valid subset.
    4. Keep track of the subset with the highest score.
- Why this approach comes to mind first: It is a straightforward and intuitive way to solve the problem, but it can be inefficient for large inputs due to its exponential time complexity.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

using namespace std;

int maxScoreWords(vector<string>& words, vector<char>& letters, vector<int>& score) {
    int n = words.size();
    int maxScore = 0;
    for (int mask = 0; mask < (1 << n); mask++) {
        unordered_map<char, int> letterCount;
        for (char c : letters) {
            letterCount[c]++;
        }
        int currentScore = 0;
        bool valid = true;
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                for (char c : words[i]) {
                    if (--letterCount[c] < 0) {
                        valid = false;
                        break;
                    }
                    currentScore += score[c - 'a'];
                }
                if (!valid) break;
            }
        }
        if (valid) maxScore = max(maxScore, currentScore);
    }
    return maxScore;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot m \cdot k)$, where $n$ is the number of words, $m$ is the maximum length of a word, and $k$ is the number of letters. This is because we generate all possible subsets of words and for each subset, we check if it can be formed using the available letters.
> - **Space Complexity:** $O(m)$, where $m$ is the maximum length of a word. This is because we use an unordered map to store the count of each letter.
> - **Why these complexities occur:** The time complexity is exponential due to the generation of all possible subsets of words, and the space complexity is linear due to the use of an unordered map to store the count of each letter.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Use a bitmask to represent the presence or absence of each word in the current combination, and use a recursive approach with memoization to avoid redundant calculations.
- Detailed breakdown of the approach: 
    1. Initialize a bitmask `mask` to represent the presence or absence of each word in the current combination.
    2. Use a recursive function to try all possible combinations of words.
    3. For each recursive call, check if the current combination can be formed using the available letters.
    4. Calculate the total score for the current combination and update the maximum score if necessary.
    5. Use memoization to store the results of subproblems and avoid redundant calculations.
- Proof of optimality: The recursive approach with memoization ensures that we try all possible combinations of words and avoid redundant calculations, resulting in an optimal solution.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

using namespace std;

int maxScoreWords(vector<string>& words, vector<char>& letters, vector<int>& score) {
    int n = words.size();
    unordered_map<char, int> letterCount;
    for (char c : letters) {
        letterCount[c]++;
    }
    int maxScore = 0;
    vector<int> wordScores(n);
    for (int i = 0; i < n; i++) {
        for (char c : words[i]) {
            wordScores[i] += score[c - 'a'];
        }
    }
    vector<vector<int>> memo(1 << n, vector<int>(26, -1));
    function<int(int, vector<int>)> dfs = [&](int mask, vector<int> letterCounts) {
        if (mask == 0) return 0;
        if (memo[mask][0] != -1) return memo[mask][0];
        int maxScore = 0;
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                bool valid = true;
                vector<int> newLetterCounts = letterCounts;
                for (char c : words[i]) {
                    newLetterCounts[c - 'a']--;
                    if (newLetterCounts[c - 'a'] < 0) {
                        valid = false;
                        break;
                    }
                }
                if (valid) {
                    maxScore = max(maxScore, wordScores[i] + dfs(mask ^ (1 << i), newLetterCounts));
                }
            }
        }
        memo[mask][0] = maxScore;
        return maxScore;
    };
    return dfs((1 << n) - 1, vector<int>(26, 0));
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot m)$, where $n$ is the number of words and $m$ is the maximum length of a word. This is because we use a recursive approach with memoization to try all possible combinations of words.
> - **Space Complexity:** $O(2^n \cdot m)$, where $n$ is the number of words and $m$ is the maximum length of a word. This is because we use memoization to store the results of subproblems.
> - **Optimality proof:** The recursive approach with memoization ensures that we try all possible combinations of words and avoid redundant calculations, resulting in an optimal solution.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Recursive approach with memoization, bitmasking, and dynamic programming.
- Problem-solving patterns identified: Using a recursive approach to try all possible combinations of words and using memoization to avoid redundant calculations.
- Optimization techniques learned: Using memoization to store the results of subproblems and avoid redundant calculations.
- Similar problems to practice: Word Break, Word Ladder, and other problems that involve trying all possible combinations of words or strings.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the memoization table correctly, not handling the base case of the recursive function correctly, and not updating the maximum score correctly.
- Edge cases to watch for: Handling the case where the input list of words is empty, handling the case where the input list of letters is empty, and handling the case where the input list of scores is empty.
- Performance pitfalls: Not using memoization to avoid redundant calculations, not using a recursive approach to try all possible combinations of words, and not handling the base case of the recursive function correctly.
- Testing considerations: Testing the function with different input lists of words, letters, and scores, testing the function with edge cases, and testing the function with large input lists to ensure that it runs efficiently.