## Remove Invalid Parentheses
**Problem Link:** [https://leetcode.com/problems/remove-invalid-parentheses/description](https://leetcode.com/problems/remove-invalid-parentheses/description)

**Problem Statement:**
- Input format and constraints: The input is a string `s` containing parentheses, and the goal is to remove the minimum number of invalid parentheses to make the string valid.
- Expected output format: Return all possible results of removing the minimum number of parentheses to make the string valid.
- Key requirements and edge cases to consider: The string may contain other characters besides parentheses, and the removal of parentheses should be minimal.
- Example test cases with explanations:
  - Input: `s = "()())()"`
  - Output: `["()()()", "(())()"]`
  - Explanation: By removing one parenthesis, we can get two valid strings.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to generate all possible strings by removing different combinations of parentheses and then check if each string is valid.
- Step-by-step breakdown of the solution:
  1. Generate all possible strings by removing different combinations of parentheses.
  2. Check if each string is valid by using a stack or a counter to keep track of the balance of parentheses.
  3. If a string is valid, add it to the result list.
- Why this approach comes to mind first: It's a straightforward approach that considers all possibilities.

```cpp
#include <iostream>
#include <vector>
#include <string>
using namespace std;

bool isValid(string s) {
    int count = 0;
    for (char c : s) {
        if (c == '(') count++;
        if (c == ')') count--;
        if (count < 0) return false;
    }
    return count == 0;
}

void generate(vector<string>& res, string s, int start, int removed) {
    if (removed == 0) {
        if (isValid(s)) res.push_back(s);
        return;
    }
    for (int i = start; i < s.size(); i++) {
        if (s[i] == '(' || s[i] == ')') {
            string temp = s.substr(0, i) + s.substr(i + 1);
            generate(res, temp, i, removed - 1);
        }
    }
}

vector<string> removeInvalidParentheses(string s) {
    vector<string> res;
    generate(res, s, 0, 1);
    if (res.empty()) {
        generate(res, s, 0, 2);
    }
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the string. This is because we generate all possible strings by removing different combinations of parentheses, and for each string, we check if it's valid.
> - **Space Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the string. This is because we store all possible strings in the result list.
> - **Why these complexities occur:** The brute force approach generates all possible strings, which leads to exponential time and space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a level-based approach to generate all possible strings by removing different combinations of parentheses. We start with the original string and remove one parenthesis at a time, checking if the resulting string is valid.
- Detailed breakdown of the approach:
  1. Initialize a set to store the strings at each level.
  2. Start with the original string and remove one parenthesis at a time.
  3. Check if the resulting string is valid. If it is, add it to the result list.
  4. If no valid strings are found at the current level, increment the level and repeat the process.
- Proof of optimality: This approach is optimal because it generates all possible strings by removing different combinations of parentheses, and it stops as soon as it finds valid strings.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_set>
using namespace std;

bool isValid(string s) {
    int count = 0;
    for (char c : s) {
        if (c == '(') count++;
        if (c == ')') count--;
        if (count < 0) return false;
    }
    return count == 0;
}

vector<string> removeInvalidParentheses(string s) {
    vector<string> res;
    unordered_set<string> level = {s};
    while (true) {
        for (const string& str : level) {
            if (isValid(str)) {
                res.push_back(str);
            }
        }
        if (!res.empty()) break;
        unordered_set<string> nextLevel;
        for (const string& str : level) {
            for (int i = 0; i < str.size(); i++) {
                if (str[i] == '(' || str[i] == ')') {
                    nextLevel.insert(str.substr(0, i) + str.substr(i + 1));
                }
            }
        }
        level = nextLevel;
    }
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the string. This is because we generate all possible strings by removing different combinations of parentheses, and for each string, we check if it's valid.
> - **Space Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the string. This is because we store all possible strings in the level set.
> - **Optimality proof:** This approach is optimal because it generates all possible strings by removing different combinations of parentheses, and it stops as soon as it finds valid strings.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the use of a level-based approach to generate all possible strings by removing different combinations of parentheses.
- Problem-solving patterns identified: The problem requires a systematic approach to generate all possible strings and check if they are valid.
- Optimization techniques learned: The optimal approach uses a level-based approach to generate all possible strings, which reduces the number of strings that need to be checked.
- Similar problems to practice: Other problems that involve generating all possible strings by removing different combinations of characters, such as the "Generate Parentheses" problem.

**Mistakes to Avoid:**
- Common implementation errors: A common mistake is to generate all possible strings and then check if they are valid, which leads to exponential time and space complexity.
- Edge cases to watch for: The problem requires handling edge cases, such as an empty string or a string with no parentheses.
- Performance pitfalls: The brute force approach can lead to performance issues due to its exponential time and space complexity.
- Testing considerations: The problem requires testing with different input strings to ensure that the solution works correctly.