## Count Vowels Permutation

**Problem Link:** https://leetcode.com/problems/count-vowels-permutation/description

**Problem Statement:**
- Input format: An integer `n` representing the number of steps in the permutation.
- Constraints: `1 <= n <= 5 * 10^4`.
- Expected output format: The number of possible permutations of vowels where each step is chosen from the set of vowels `{a, e, i, o, u}` and each vowel can be followed by a specific set of vowels.
- Key requirements and edge cases to consider: The permutation should adhere to the rules of vowel succession (e.g., 'a' can be followed by 'e').
- Example test cases with explanations: For `n = 1`, there are 5 possible permutations since each vowel can be the first in the sequence. For `n = 2`, the permutations are more restricted due to the rules of vowel succession.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible sequences of vowels of length `n` and then filter those sequences based on the rules of vowel succession.
- Step-by-step breakdown of the solution:
  1. Generate all possible sequences of vowels of length `n`.
  2. For each sequence, check if it adheres to the rules of vowel succession.
  3. Count the sequences that pass the check.
- Why this approach comes to mind first: It directly addresses the problem by considering all possibilities and then applying the constraints.

```cpp
#include <iostream>
#include <vector>
#include <string>

void generatePermutations(std::vector<std::string>& permutations, std::string current, int n) {
    if (current.length() == n) {
        permutations.push_back(current);
        return;
    }
    std::string vowels = "aeiou";
    for (char c : vowels) {
        if (current.empty() || isValidSuccession(current.back(), c)) {
            generatePermutations(permutations, current + c, n);
        }
    }
}

bool isValidSuccession(char a, char b) {
    // Define the valid successions here
    // For example, 'a' can be followed by 'e'
    // This function should check if 'a' can be followed by 'b'
    // Based on the problem statement, implement the logic here
    // For simplicity, let's assume we have a map or a function that tells us if a can be followed by b
    // For this example, we'll use a simplified version
    std::vector<std::pair<char, char>> validSuccessions = {{'a', 'e'}, {'e', 'a'}, {'e', 'i'}, {'a', 'i'}, {'i', 'a'}, {'i', 'e'}, {'i', 'o'}, {'i', 'u'}, {'o', 'i'}, {'o', 'u'}, {'u', 'a'}};
    for (auto& pair : validSuccessions) {
        if (a == pair.first && b == pair.second) return true;
    }
    return false;
}

int countVowelPermutation(int n) {
    std::vector<std::string> permutations;
    generatePermutations(permutations, "", n);
    int count = 0;
    for (const auto& permutation : permutations) {
        bool isValid = true;
        for (int i = 0; i < n - 1; ++i) {
            if (!isValidSuccession(permutation[i], permutation[i + 1])) {
                isValid = false;
                break;
            }
        }
        if (isValid) count++;
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(5^n)$ because we generate all possible sequences of length `n` from a set of 5 elements (vowels).
> - **Space Complexity:** $O(5^n)$ for storing all permutations.
> - **Why these complexities occur:** The brute force approach generates all possible permutations and then filters them, leading to exponential time and space complexity due to the number of possible sequences.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use dynamic programming to keep track of the number of valid permutations ending at each vowel at each step, rather than generating all permutations.
- Detailed breakdown of the approach:
  1. Initialize a DP table where `dp[i][j]` represents the number of valid permutations of length `i` ending with vowel `j`.
  2. Fill the DP table iteratively, considering the valid successions from one vowel to another.
  3. The final answer is the sum of all valid permutations of length `n` ending with any vowel.
- Proof of optimality: This approach avoids generating unnecessary permutations and directly calculates the number of valid ones, reducing the time complexity significantly.

```cpp
int countVowelPermutation(int n) {
    const int MOD = 1e9 + 7;
    long long dp[5] = {1, 1, 1, 1, 1}; // Initialize with 1 for each vowel for length 1
    std::vector<std::vector<int>> transitions = {{1}, {0, 2}, {0, 1, 3, 4}, {2, 4}, {0, 3}}; // Valid transitions for each vowel
    
    for (int i = 2; i <= n; ++i) {
        long long next[5] = {0};
        for (int j = 0; j < 5; ++j) {
            for (int k : transitions[j]) {
                next[j] += dp[k];
                next[j] %= MOD;
            }
        }
        std::copy(next, next + 5, dp);
    }
    
    long long total = 0;
    for (int i = 0; i < 5; ++i) {
        total += dp[i];
        total %= MOD;
    }
    return total;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the length of the permutation and $m$ is the number of vowels (5 in this case), because we fill the DP table iteratively.
> - **Space Complexity:** $O(m)$ for the DP table.
> - **Optimality proof:** This approach directly calculates the number of valid permutations without generating them, reducing the time complexity from exponential to linear with respect to the length of the permutation.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic Programming for solving problems with overlapping subproblems and optimal substructure.
- Problem-solving patterns identified: Avoiding brute force by identifying patterns and using more efficient algorithms.
- Optimization techniques learned: Using DP to reduce time complexity.
- Similar problems to practice: Other permutation and sequence problems that can be solved using DP.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect initialization of DP tables, forgetting to consider all possible transitions between states.
- Edge cases to watch for: Handling the base case correctly (e.g., when `n = 1`).
- Performance pitfalls: Using brute force or inefficient algorithms for large inputs.
- Testing considerations: Ensure to test with various inputs, including edge cases like `n = 1` and larger values of `n`.