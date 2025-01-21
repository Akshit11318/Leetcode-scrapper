## Brace Expansion II
**Problem Link:** https://leetcode.com/problems/brace-expansion-ii/description

**Problem Statement:**
- Input format: A string `expression` containing `{}`, `(`, `)`, and characters.
- Constraints: The length of `expression` is at most 50.
- Expected output format: A list of all unique strings that can be formed by expanding the given expression.
- Key requirements and edge cases to consider: Handling nested expressions, avoiding duplicates, and considering all possible expansions.
- Example test cases with explanations: 
  - Input: `"({a,b}{c,d})"`, Output: `["ac","ad","bc","bd"]`.
  - Input: `"z{a,b}"`, Output: `["za","zb"]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To generate all possible expansions by recursively exploring each branch of the expression and combining the results.
- Step-by-step breakdown of the solution:
  1. Identify the `{` character to split the expression into parts.
  2. Recursively expand each part within `{}`.
  3. Combine the results from each recursive call to form all possible expansions.
- Why this approach comes to mind first: It directly addresses the problem by exploring all possible paths of expansion.

```cpp
class Solution {
public:
    vector<string> braceExpansionII(string expression) {
        unordered_set<string> result;
        vector<string> temp;
        dfs(expression, 0, "", result, temp);
        vector<string> res(result.begin(), result.end());
        return res;
    }
    
    void dfs(string& expression, int index, string path, unordered_set<string>& result, vector<string>& temp) {
        if (index == expression.size()) {
            result.insert(path);
            return;
        }
        if (expression[index] == '{') {
            int j = index + 1;
            int count = 1;
            while (count != 0) {
                if (expression[j] == '{') count++;
                if (expression[j] == '}') count--;
                j++;
            }
            string sub = expression.substr(index + 1, j - index - 2);
            vector<string> subs = split(sub, ',');
            for (string s : subs) {
                dfs(expression, j, path + s, result, temp);
            }
        } else {
            dfs(expression, index + 1, path + expression[index], result, temp);
        }
    }
    
    vector<string> split(string& str, char delimiter) {
        vector<string> tokens;
        string token;
        for (char c : str) {
            if (c == delimiter) {
                tokens.push_back(token);
                token.clear();
            } else {
                token += c;
            }
        }
        tokens.push_back(token);
        return tokens;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot m)$, where $n$ is the number of `{` characters and $m$ is the average length of the strings within each `{}`. This is because in the worst case, each `{}` could potentially double the number of paths to explore.
> - **Space Complexity:** $O(2^n \cdot m)$, due to the storage of all unique expanded strings.
> - **Why these complexities occur:** The recursive nature of exploring all branches of the expression tree leads to exponential time complexity, and storing all unique expansions leads to exponential space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Utilizing a `set` to store unique expansions and leveraging recursion to efficiently explore all branches of the expression.
- Detailed breakdown of the approach:
  1. Start with an empty `set` to store unique expansions and an empty string to build the current expansion.
  2. Iterate through the expression. When encountering a `{`, split the expression into parts and recursively expand each part.
  3. When encountering a `}`, combine the results from the recursive calls.
  4. If the character is not a `{` or `}`, simply append it to the current expansion.
- Proof of optimality: This approach ensures all possible expansions are considered while avoiding duplicates through the use of a `set`.

```cpp
class Solution {
public:
    vector<string> braceExpansionII(string expression) {
        unordered_set<string> result;
        dfs(expression, result);
        vector<string> res(result.begin(), result.end());
        return res;
    }
    
    void dfs(string expression, unordered_set<string>& result) {
        int i = expression.find('{');
        if (i == string::npos) {
            result.insert(expression);
            return;
        }
        int j = i + 1;
        int count = 1;
        while (count != 0) {
            if (expression[j] == '{') count++;
            if (expression[j] == '}') count--;
            j++;
        }
        string prefix = expression.substr(0, i);
        string sub = expression.substr(i + 1, j - i - 2);
        string suffix = expression.substr(j);
        vector<string> subs = split(sub, ',');
        for (string s : subs) {
            string newStr = prefix + s + suffix;
            dfs(newStr, result);
        }
    }
    
    vector<string> split(string& str, char delimiter) {
        vector<string> tokens;
        string token;
        for (char c : str) {
            if (c == delimiter) {
                tokens.push_back(token);
                token.clear();
            } else {
                token += c;
            }
        }
        tokens.push_back(token);
        return tokens;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot m)$, where $n$ is the number of `{` characters and $m$ is the average length of the strings within each `{}`. This is because in the worst case, each `{}` could potentially double the number of paths to explore.
> - **Space Complexity:** $O(2^n \cdot m)$, due to the storage of all unique expanded strings.
> - **Optimality proof:** This approach is optimal because it explores all possible expansions exactly once, using a `set` to eliminate duplicates, thus achieving the best possible time and space complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Recursion, use of `set` for uniqueness, and string manipulation.
- Problem-solving patterns identified: Breaking down complex expressions into simpler parts and recombining them.
- Optimization techniques learned: Using a `set` to avoid duplicate calculations and leveraging recursion to efficiently explore all branches of the expression.
- Similar problems to practice: Other string manipulation and recursion problems, such as generating permutations or combinations.

**Mistakes to Avoid:**
- Common implementation errors: Failing to handle edge cases, such as empty strings or expressions without `{}`.
- Edge cases to watch for: Nested `{}`, consecutive `{}`, and `{}` at the start or end of the expression.
- Performance pitfalls: Not using a `set` to store unique expansions, leading to exponential time complexity due to duplicate calculations.
- Testing considerations: Thoroughly testing with various inputs, including edge cases, to ensure the solution covers all possible scenarios.