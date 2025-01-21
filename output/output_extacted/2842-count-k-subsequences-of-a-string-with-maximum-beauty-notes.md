## Count K-Subsequences of a String with Maximum Beauty

**Problem Link:** https://leetcode.com/problems/count-k-subsequences-of-a-string-with-maximum-beauty/description

**Problem Statement:**
- Input format and constraints: The input consists of a string `s` and an integer `k`. The goal is to count the number of subsequences of `s` with maximum beauty.
- Expected output format: The output should be the count of subsequences with maximum beauty.
- Key requirements and edge cases to consider: The beauty of a subsequence is determined by the frequency of each character, and we need to find the maximum beauty and count the subsequences that achieve this maximum beauty.
- Example test cases with explanations: For example, given `s = "abab"` and `k = 2`, the maximum beauty is 2, and there are 6 subsequences that achieve this maximum beauty.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible subsequences of the string `s` and calculate the beauty of each subsequence.
- Step-by-step breakdown of the solution: 
  1. Generate all possible subsequences of `s`.
  2. For each subsequence, calculate its beauty by counting the frequency of each character.
  3. Keep track of the maximum beauty and count the number of subsequences that achieve this maximum beauty.
- Why this approach comes to mind first: It is a straightforward approach that ensures we consider all possible subsequences.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

int countKSubsequences(const std::string& s, int k) {
    int n = s.size();
    int maxBeauty = 0;
    int count = 0;
    std::vector<std::string> subsequences;

    // Generate all possible subsequences
    std::function<void(int, std::string)> generateSubsequences = [&](int start, std::string sub) {
        if (start == n) {
            subsequences.push_back(sub);
            return;
        }
        generateSubsequences(start + 1, sub);
        generateSubsequences(start + 1, sub + s[start]);
    };
    generateSubsequences(0, "");

    // Calculate the beauty of each subsequence and count the maximum beauty
    for (const auto& sub : subsequences) {
        std::unordered_map<char, int> freq;
        for (char c : sub) {
            freq[c]++;
        }
        int beauty = 0;
        for (const auto& pair : freq) {
            beauty = std::max(beauty, pair.second);
        }
        if (beauty > maxBeauty) {
            maxBeauty = beauty;
            count = 1;
        } else if (beauty == maxBeauty) {
            count++;
        }
    }

    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n \cdot k)$, where $n$ is the length of the string `s` and $k$ is the maximum frequency of a character in a subsequence. The reason for this complexity is that we generate all possible subsequences of `s`, which takes $O(2^n)$ time, and for each subsequence, we calculate its beauty, which takes $O(n \cdot k)$ time.
> - **Space Complexity:** $O(2^n \cdot n)$, as we need to store all possible subsequences of `s`.
> - **Why these complexities occur:** The brute force approach generates all possible subsequences of `s`, which leads to exponential time and space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of generating all possible subsequences, we can use dynamic programming to calculate the maximum beauty and count the number of subsequences that achieve this maximum beauty.
- Detailed breakdown of the approach: 
  1. Initialize a 2D array `dp` of size $(n + 1) \times (k + 1)$, where `dp[i][j]` represents the number of subsequences of the first `i` characters of `s` with maximum beauty `j`.
  2. Iterate over the string `s` and for each character, update the `dp` array accordingly.
  3. Finally, return the value of `dp[n][k]`, which represents the count of subsequences with maximum beauty `k`.
- Proof of optimality: This approach is optimal because it avoids generating all possible subsequences and instead uses dynamic programming to calculate the maximum beauty and count the number of subsequences that achieve this maximum beauty.

```cpp
#include <iostream>
#include <vector>
#include <string>

int countKSubsequences(const std::string& s, int k) {
    int n = s.size();
    std::vector<std::vector<int>> dp(n + 1, std::vector<int>(k + 1, 0));
    dp[0][0] = 1;

    for (int i = 1; i <= n; i++) {
        for (int j = 0; j <= k; j++) {
            dp[i][j] = dp[i - 1][j];
            if (j > 0) {
                dp[i][j] += dp[i - 1][j - 1];
            }
        }
    }

    return dp[n][k];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k)$, where $n$ is the length of the string `s` and $k$ is the maximum frequency of a character in a subsequence. The reason for this complexity is that we use a 2D array `dp` of size $(n + 1) \times (k + 1)$ and iterate over it once.
> - **Space Complexity:** $O(n \cdot k)$, as we need to store the `dp` array.
> - **Optimality proof:** This approach is optimal because it avoids generating all possible subsequences and instead uses dynamic programming to calculate the maximum beauty and count the number of subsequences that achieve this maximum beauty.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, string manipulation, and combinatorics.
- Problem-solving patterns identified: Avoiding brute force approaches by using dynamic programming to reduce time and space complexity.
- Optimization techniques learned: Using dynamic programming to calculate the maximum beauty and count the number of subsequences that achieve this maximum beauty.
- Similar problems to practice: Other problems involving string manipulation, combinatorics, and dynamic programming.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect initialization of the `dp` array, incorrect update of the `dp` array, and incorrect return value.
- Edge cases to watch for: Handling the case where the input string is empty or the maximum frequency is 0.
- Performance pitfalls: Using a brute force approach that generates all possible subsequences, which leads to exponential time and space complexity.
- Testing considerations: Testing the function with different input strings and maximum frequencies to ensure correctness.