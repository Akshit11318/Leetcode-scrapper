## Count Sorted Vowel Strings

**Problem Link:** https://leetcode.com/problems/count-sorted-vowel-strings/description

**Problem Statement:**
- Input: An integer `n`, representing the number of characters in the string.
- Output: The number of sorted vowel strings of length `n`.
- Key requirements: A sorted vowel string is one where the vowels are in non-decreasing order. The vowels are 'a', 'e', 'i', 'o', 'u'.
- Example test cases:
  - Input: `n = 1`, Output: `5` (Each vowel can be used as a single character string).
  - Input: `n = 2`, Output: `15` (Combinations like "aa", "ae", "ai", ..., "uu" are valid).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible strings of length `n` using the vowels 'a', 'e', 'i', 'o', 'u', and then check each string to see if it's sorted.
- Step-by-step breakdown:
  1. Generate all possible strings of length `n`.
  2. For each string, check if the vowels are in non-decreasing order.
  3. Count the number of strings that are sorted.

```cpp
#include <iostream>
#include <vector>
#include <string>

int countSortedVowelStringsBrute(int n) {
    std::vector<char> vowels = {'a', 'e', 'i', 'o', 'u'};
    int count = 0;

    // Generate all possible strings
    std::vector<std::string> allStrings;
    std::string temp;
    temp.resize(n);
    generateAllStrings(allStrings, temp, vowels, 0);

    // Count sorted strings
    for (const auto& str : allStrings) {
        if (isSorted(str)) {
            count++;
        }
    }

    return count;
}

void generateAllStrings(std::vector<std::string>& allStrings, std::string& temp, std::vector<char> vowels, int index) {
    if (index == temp.size()) {
        allStrings.push_back(temp);
        return;
    }

    for (char vowel : vowels) {
        temp[index] = vowel;
        generateAllStrings(allStrings, temp, vowels, index + 1);
    }
}

bool isSorted(const std::string& str) {
    for (int i = 1; i < str.size(); i++) {
        if (str[i - 1] > str[i]) {
            return false;
        }
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(5^n \cdot n)$, where $n$ is the length of the string. This is because we generate $5^n$ possible strings and for each string, we check if it's sorted, which takes $O(n)$ time.
> - **Space Complexity:** $O(5^n \cdot n)$, because we store all generated strings.
> - **Why these complexities occur:** The brute force approach is inefficient because it generates all possible strings and then filters them, resulting in exponential time and space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Realize that the problem can be solved using combinatorics, specifically a concept similar to "stars and bars" or using dynamic programming to track the count of sorted strings up to each length.
- Detailed breakdown:
  - We can use dynamic programming where `dp[i][j]` represents the number of sorted vowel strings of length `i` ending with the `j`-th vowel ('a' is 0, 'e' is 1, ..., 'u' is 4).
  - For each vowel, we can append it to all previously sorted strings of length `i-1` that end with a vowel not greater than the current vowel.

```cpp
int countSortedVowelStrings(int n) {
    std::vector<std::vector<int>> dp(n + 1, std::vector<int>(5, 0));
    
    // Base case: For n = 1, each vowel can be used as a single character string.
    for (int i = 0; i < 5; i++) {
        dp[1][i] = 1;
    }
    
    // Fill up dp table
    for (int i = 2; i <= n; i++) {
        for (int j = 0; j < 5; j++) {
            for (int k = 0; k <= j; k++) {
                dp[i][j] += dp[i - 1][k];
            }
        }
    }
    
    // The total number of sorted vowel strings of length n
    int total = 0;
    for (int i = 0; i < 5; i++) {
        total += dp[n][i];
    }
    
    return total;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot 5^2)$, where $n$ is the length of the string. This is because we have two nested loops that run up to `n` and `5` respectively.
> - **Space Complexity:** $O(n \cdot 5)$, because we use a 2D array of size $n \times 5$ to store the dynamic programming table.
> - **Optimality proof:** This approach is optimal because it directly calculates the number of sorted vowel strings without generating all possible strings, thus avoiding the exponential complexity of the brute force approach.

---

### Final Notes

**Learning Points:**
- The importance of recognizing when a problem can be solved using combinatorial methods or dynamic programming.
- How to apply dynamic programming to track the count of specific patterns (in this case, sorted vowel strings).
- The trade-off between the brute force approach (simple to understand but inefficient) and the optimal approach (more complex but efficient).

**Mistakes to Avoid:**
- Not considering the combinatorial or dynamic programming aspects of the problem.
- Incorrectly implementing the dynamic programming table.
- Failing to optimize the solution, leading to inefficient algorithms.