## Smallest Subsequence of Distinct Characters

**Problem Link:** https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/description

**Problem Statement:**
- Input format: A string `s` containing lowercase English letters.
- Constraints: `1 <= s.length <= 10^4`.
- Expected output format: The lexicographically smallest subsequence of distinct characters.
- Key requirements and edge cases to consider:
  - The subsequence must be lexicographically smallest.
  - Characters in the subsequence must be distinct.
- Example test cases with explanations:
  - Input: `s = "bcabc"`
    Output: `"abc"`
    Explanation: The lexicographically smallest subsequence of distinct characters is `"abc"`.
  - Input: `s = "cbacdcbc"`
    Output: `"acdb"`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible subsequences of the input string and check if they contain distinct characters. Then, find the lexicographically smallest one among them.
- Step-by-step breakdown of the solution:
  1. Generate all possible subsequences of the input string.
  2. For each subsequence, check if it contains distinct characters.
  3. If a subsequence contains distinct characters, compare it with the current lexicographically smallest subsequence found so far.
  4. Update the lexicographically smallest subsequence if a smaller one is found.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

std::string smallestSubsequence(const std::string& s) {
    int n = s.size();
    std::vector<std::string> subsequences;
    
    // Generate all possible subsequences
    for (int mask = 0; mask < (1 << n); ++mask) {
        std::string subsequence;
        for (int i = 0; i < n; ++i) {
            if ((mask & (1 << i)) != 0) {
                subsequence += s[i];
            }
        }
        subsequences.push_back(subsequence);
    }
    
    // Find the lexicographically smallest subsequence with distinct characters
    std::string result;
    for (const auto& subsequence : subsequences) {
        if (std::set<char>(subsequence.begin(), subsequence.end()).size() == subsequence.size()) {
            if (result.empty() || subsequence < result) {
                result = subsequence;
            }
        }
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the input string. This is because we generate all possible subsequences, which takes $O(2^n)$ time, and then for each subsequence, we check if it contains distinct characters, which takes $O(n)$ time.
> - **Space Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the input string. This is because we store all possible subsequences, which takes $O(2^n \cdot n)$ space.
> - **Why these complexities occur:** These complexities occur because the brute force approach generates all possible subsequences and checks each one, resulting in exponential time and space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a stack to keep track of the lexicographically smallest subsequence with distinct characters.
- Detailed breakdown of the approach:
  1. Initialize an empty stack to store the lexicographically smallest subsequence with distinct characters.
  2. Iterate through the input string. For each character, check if it is already in the stack.
  3. If the character is not in the stack, pop all characters from the stack that are greater than the current character and appear later in the input string.
  4. Push the current character onto the stack.
  5. After iterating through the entire input string, the stack will contain the lexicographically smallest subsequence with distinct characters.

```cpp
#include <iostream>
#include <stack>
#include <string>
#include <unordered_set>

std::string smallestSubsequence(const std::string& s) {
    int n = s.size();
    std::stack<char> stack;
    std::unordered_set<char> seen;
    
    for (int i = 0; i < n; ++i) {
        if (seen.find(s[i]) != seen.end()) {
            continue;
        }
        
        while (!stack.empty() && stack.top() > s[i] && s.find(stack.top(), i) != std::string::npos) {
            seen.erase(stack.top());
            stack.pop();
        }
        
        stack.push(s[i]);
        seen.insert(s[i]);
    }
    
    std::string result;
    while (!stack.empty()) {
        result = stack.top() + result;
        stack.pop();
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string. This is because we iterate through the input string once and perform constant-time operations for each character.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input string. This is because we use a stack to store the lexicographically smallest subsequence with distinct characters, which takes $O(n)$ space in the worst case.
> - **Optimality proof:** This is the optimal solution because we use a stack to keep track of the lexicographically smallest subsequence with distinct characters, which allows us to avoid generating all possible subsequences and checking each one. This results in a significant reduction in time and space complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a stack to keep track of the lexicographically smallest subsequence with distinct characters.
- Problem-solving patterns identified: Using a greedy approach to find the lexicographically smallest subsequence with distinct characters.
- Optimization techniques learned: Avoiding unnecessary work by using a stack to keep track of the lexicographically smallest subsequence with distinct characters.
- Similar problems to practice: Finding the lexicographically smallest subsequence with distinct characters in a string with duplicate characters.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if a character is already in the stack before pushing it.
- Edge cases to watch for: Handling duplicate characters in the input string.
- Performance pitfalls: Generating all possible subsequences and checking each one, resulting in exponential time and space complexity.
- Testing considerations: Testing the solution with different input strings, including those with duplicate characters.