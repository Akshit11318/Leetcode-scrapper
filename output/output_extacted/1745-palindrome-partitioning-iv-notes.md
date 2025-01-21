## Palindrome Partitioning IV

**Problem Link:** https://leetcode.com/problems/palindrome-partitioning-iv/description

**Problem Statement:**
- Input format: The problem takes a string `s` as input and asks to determine if it can be partitioned into an odd number of non-empty substrings such that every substring is a palindrome.
- Constraints: The length of `s` is between 1 and 1000.
- Expected output format: A boolean value indicating whether the string can be partitioned as required.
- Key requirements and edge cases to consider:
  - Handling strings of length 1.
  - Dealing with strings that cannot be partitioned into palindromes.
  - Considering the requirement for an odd number of substrings.

**Example Test Cases:**
- For `s = "abc"`, the function should return `false` because there's no way to partition it into an odd number of palindromes.
- For `s = "abba"`, the function should return `true` because it can be partitioned into `["a", "b", "b", "a"]`, which are all palindromes.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking every possible way to partition the string into substrings and verifying if each substring is a palindrome.
- This approach involves generating all possible partitions of the string and then checking each partition to see if all its substrings are palindromes.

```cpp
#include <vector>
#include <string>

bool checkPartitioning(std::string s) {
    int n = s.size();
    
    // Function to check if a substring is a palindrome
    auto isPalindrome = [&](const std::string& str) {
        int left = 0, right = str.size() - 1;
        while (left < right) {
            if (str[left] != str[right]) return false;
            left++, right--;
        }
        return true;
    };
    
    // Generate all possible partitions and check if they consist of only palindromes
    for (int mask = 0; mask < (1 << (n - 1)); mask++) {
        int count = 0; // Count of substrings
        std::string substr = "";
        for (int i = 0; i < n; i++) {
            substr += s[i];
            if ((mask & (1 << i)) || i == n - 1) {
                if (isPalindrome(substr)) {
                    count++;
                } else {
                    break; // Move to next partition if not palindrome
                }
                substr = "";
            }
        }
        // Check if total count of substrings is odd and all were palindromes
        if (count > 0 && (count & 1) && i == n) return true;
    }
    
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{n-1} \cdot n^2)$, where $n$ is the length of the string. The $2^{n-1}$ factor comes from generating all possible partitions, and the $n^2$ factor comes from checking each substring to see if it's a palindrome.
> - **Space Complexity:** $O(n)$, for storing the substrings and other variables.
> - **Why these complexities occur:** The brute force approach is inherently inefficient because it involves checking every possible partition of the string, which results in exponential time complexity. The palindrome check for each substring adds a quadratic factor due to the nested loop structure.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal solution involves using dynamic programming to efficiently check for palindromes and store the results to avoid redundant computations.
- We create a 2D table `dp` where `dp[i][j]` is `true` if the substring from index `i` to `j` is a palindrome.
- Then, we use another dynamic programming approach to check if the string can be partitioned into an odd number of palindromes.

```cpp
#include <vector>
#include <string>

bool checkPartitioning(std::string s) {
    int n = s.size();
    
    // Create a 2D table to store if a substring is a palindrome
    std::vector<std::vector<bool>> dp(n, std::vector<bool>(n, false));
    for (int i = n - 1; i >= 0; i--) {
        dp[i][i] = true; // Single character is always a palindrome
        for (int j = i + 1; j < n; j++) {
            if (s[i] == s[j]) {
                if (j - i == 1 || dp[i + 1][j - 1]) {
                    dp[i][j] = true;
                }
            }
        }
    }
    
    // Check if the string can be partitioned into an odd number of palindromes
    std::vector<bool> canPartition(n + 1, false);
    canPartition[0] = true;
    for (int i = 1; i <= n; i++) {
        for (int j = 0; j < i; j++) {
            if (canPartition[j] && dp[j][i - 1]) {
                canPartition[i] = true;
            }
        }
    }
    
    // Check for an odd number of partitions
    for (int i = 1; i <= n; i += 2) {
        if (canPartition[i]) return true;
    }
    
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the string. This comes from the nested loops used to fill the `dp` table and to check for partitions.
> - **Space Complexity:** $O(n^2)$, for the 2D `dp` table and the `canPartition` array.
> - **Optimality proof:** This approach is optimal because it minimizes the number of computations required to check for palindromes and partitions. The use of dynamic programming avoids redundant calculations, leading to a significant improvement over the brute force approach.

---

### Final Notes

**Learning Points:**
- The importance of dynamic programming in solving problems that involve overlapping subproblems or optimal substructure.
- How to efficiently check for palindromes in a string using a 2D table.
- The value of breaking down complex problems into simpler subproblems and solving them iteratively.

**Mistakes to Avoid:**
- Failing to consider the exponential number of partitions in the brute force approach.
- Not using dynamic programming to store and reuse the results of subproblems.
- Overlooking the requirement for an odd number of partitions in the final check.