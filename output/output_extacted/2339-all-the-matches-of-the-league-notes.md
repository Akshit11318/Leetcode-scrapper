## All the Matches of the League

**Problem Link:** https://leetcode.com/problems/all-the-matches-of-the-league/description

**Problem Statement:**
- Input format: A string `matches` where each character represents a match between two teams.
- Constraints: 
  - The length of `matches` is even.
  - Each character is a lowercase letter.
- Expected output format: A list of strings representing the matches in the format "team1:team2".
- Key requirements and edge cases to consider: 
  - Ensure each match is unique.
  - The input string is well-formed and does not contain any invalid characters.
- Example test cases with explanations:
  - For the input "abc", the output should be ["a:b", "a:c", "b:c"].
  - For the input "abcd", the output should be ["a:b", "a:c", "a:d", "b:c", "b:d", "c:d"].

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To generate all possible matches between the teams, we can use a brute force approach where we compare each character (team) in the input string with every other character.
- Step-by-step breakdown of the solution:
  1. Initialize an empty list to store the matches.
  2. Iterate over each character in the input string.
  3. For each character, iterate over the remaining characters in the string.
  4. Create a match in the format "team1:team2" and add it to the list.
- Why this approach comes to mind first: It is straightforward and ensures that all possible matches are generated.

```cpp
#include <iostream>
#include <vector>
#include <string>

std::vector<std::string> find_matches(const std::string& matches) {
    std::vector<std::string> result;
    for (int i = 0; i < matches.size(); i++) {
        for (int j = i + 1; j < matches.size(); j++) {
            std::string match = matches[i] + ':' + matches[j];
            result.push_back(match);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the input string, because we have two nested loops that iterate over the string.
> - **Space Complexity:** $O(n^2)$, because in the worst case, we store all possible matches in the result list.
> - **Why these complexities occur:** The brute force approach has a quadratic time complexity due to the nested loops, and the space complexity is also quadratic because we store all matches.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The problem can be solved using a similar approach to the brute force method, but we can optimize it by recognizing that the order of the teams in a match does not matter.
- Detailed breakdown of the approach:
  1. Initialize an empty list to store the matches.
  2. Iterate over each character in the input string.
  3. For each character, iterate over the remaining characters in the string.
  4. Create a match in the format "team1:team2" and add it to the list.
- Proof of optimality: This approach is optimal because it generates all possible matches between the teams in a single pass, without any unnecessary comparisons or computations.

```cpp
#include <iostream>
#include <vector>
#include <string>

std::vector<std::string> find_matches(const std::string& matches) {
    std::vector<std::string> result;
    for (int i = 0; i < matches.size(); i++) {
        for (int j = i + 1; j < matches.size(); j++) {
            std::string match = std::min(matches[i], matches[j]) + ':' + std::max(matches[i], matches[j]);
            result.push_back(match);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the input string, because we have two nested loops that iterate over the string.
> - **Space Complexity:** $O(n^2)$, because in the worst case, we store all possible matches in the result list.
> - **Optimality proof:** This approach is optimal because it generates all possible matches between the teams in a single pass, without any unnecessary comparisons or computations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Nested loops, string manipulation, and optimization techniques.
- Problem-solving patterns identified: Recognizing the need for a brute force approach and optimizing it.
- Optimization techniques learned: Using `std::min` and `std::max` to ensure consistent ordering of teams in matches.
- Similar problems to practice: Generating all possible combinations of a given set of elements.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect loop indices, missing checks for invalid input, and incorrect ordering of teams in matches.
- Edge cases to watch for: Empty input string, input string with a single character, and input string with duplicate characters.
- Performance pitfalls: Using unnecessary computations or comparisons, and not optimizing the solution for the given constraints.
- Testing considerations: Test the solution with various input strings, including edge cases, to ensure correctness and performance.