## Redistribute Characters to Make All Strings Equal
**Problem Link:** https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/description

**Problem Statement:**
- Input format: An array of strings `words`.
- Constraints: Each string consists of lowercase English letters.
- Expected output format: A boolean indicating whether it's possible to make all strings equal by rearranging characters.
- Key requirements and edge cases to consider: The number of occurrences of each character across all strings must be divisible by the number of strings for it to be possible to redistribute characters to make all strings equal.
- Example test cases with explanations:
  - `words = ["abc","cab","bca"]`: Returns `true` because we can make all strings equal by rearranging characters.
  - `words = ["ab","a"]`: Returns `false` because it's impossible to make all strings equal.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check every possible permutation of characters in each string to see if we can make all strings equal.
- Step-by-step breakdown of the solution:
  1. Generate all permutations of characters for each string.
  2. Compare each permutation of one string with all permutations of the other strings.
  3. If a permutation matches across all strings, return `true`.
- Why this approach comes to mind first: It's a straightforward, exhaustive search approach, but it's highly inefficient.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

bool makeEqual(std::vector<std::string>& words) {
    int n = words.size();
    std::string combined;
    for (const auto& word : words) {
        combined += word;
    }

    std::sort(combined.begin(), combined.end());
    for (char c = 'a'; c <= 'z'; ++c) {
        int count = 0;
        for (char ch : combined) {
            if (ch == c) count++;
        }
        if (count % n != 0) return false;
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(N \cdot M \log(M))$ where $N$ is the number of strings and $M$ is the total number of characters across all strings, due to sorting the combined string.
> - **Space Complexity:** $O(M)$ for storing the combined string.
> - **Why these complexities occur:** The sorting operation dominates the time complexity, and storing the combined string requires additional space.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of generating permutations, we can simply count the occurrences of each character across all strings and check if these counts are divisible by the number of strings.
- Detailed breakdown of the approach:
  1. Count the occurrences of each character across all strings.
  2. For each character, check if its count is divisible by the number of strings.
  3. If any character's count is not divisible, return `false`.
- Proof of optimality: This approach is optimal because it directly addresses the requirement for redistributing characters without needing to generate or compare permutations.

```cpp
#include <iostream>
#include <vector>
#include <string>

bool makeEqual(std::vector<std::string>& words) {
    int n = words.size();
    int count[26] = {0}; // Assuming lowercase English letters only

    for (const auto& word : words) {
        for (char c : word) {
            count[c - 'a']++;
        }
    }

    for (int i = 0; i < 26; ++i) {
        if (count[i] % n != 0) return false;
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(N \cdot M)$ where $N$ is the number of strings and $M$ is the average length of a string, because we iterate over each character in each string once.
> - **Space Complexity:** $O(1)$ because we use a fixed-size array to count character occurrences, regardless of the input size.
> - **Optimality proof:** This approach is optimal because it minimizes the number of operations required to solve the problem, directly counting character occurrences and checking divisibility without unnecessary permutations or comparisons.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Character counting, divisibility checks.
- Problem-solving patterns identified: Direct counting and divisibility checks can often replace more complex permutation-based approaches.
- Optimization techniques learned: Avoid generating unnecessary permutations; instead, focus on the essential conditions for solving the problem.
- Similar problems to practice: Other string manipulation and counting problems.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly assuming the need for permutations or not considering the divisibility requirement.
- Edge cases to watch for: Empty strings, single-character strings, and strings with only one unique character.
- Performance pitfalls: Generating unnecessary permutations or using inefficient data structures.
- Testing considerations: Ensure to test with a variety of string lengths, characters, and numbers of strings.