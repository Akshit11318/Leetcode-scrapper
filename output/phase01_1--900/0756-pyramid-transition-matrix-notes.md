## Pyramid Transition Matrix

**Problem Link:** https://leetcode.com/problems/pyramid-transition-matrix/description

**Problem Statement:**
- Input: A list of strings `bottom` and a list of strings `allowed`.
- Constraints: `1 <= bottom.length <= 1000` and `1 <= allowed.length <= 1000`.
- Expected Output: A boolean indicating whether a pyramid can be formed using the `allowed` transitions.
- Key Requirements: 
  - The pyramid must start with the `bottom` row and end with a single block.
  - Each row must be formed using the `allowed` transitions.
- Edge Cases:
  - If the `bottom` row is empty, return `false`.
  - If the `allowed` list is empty, return `false`.
- Example Test Cases:
  - `bottom = ["XYZ","NO","ONM"]`, `allowed = ["IXZ","IXO","IXM","IYN","IYZ","IYO","IYM","INZ","INX","INM","ONO","NOX","NOZ","NON","NOY","INY","INZ","INX","INM","ION","IOZ","IOM","IOP","IPZ","IPX","IPM","IPO","IYP","IYM","IYP","IYX","IYM","IYP","IYX","IYP"]`, return `true`.
  - `bottom = ["XXYX","XXYY","XYXY","XYYY","YYXY","YYYY"]`, `allowed = ["XXX","XXY","XYX","XYY","YXX","YYX","YYY","YYZ"]`, return `false`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves trying all possible transitions for each block in the `bottom` row and checking if a pyramid can be formed.
- We can use a recursive approach to try all possible transitions.
- However, this approach is inefficient due to the large number of possible transitions.

```cpp
bool pyramidTransition(string bottom, vector<string>& allowed) {
    unordered_map<string, vector<char>> transitions;
    for (string s : allowed) {
        transitions[s.substr(0, 2)].push_back(s[2]);
    }

    function<bool(string)> dfs = [&](string row) {
        if (row.size() == 1) return true;
        vector<char> nextRow(row.size() - 1, '.');
        function<bool(int)> fillNextRow = [&](int index) {
            if (index == row.size() - 1) return dfs(string(nextRow.begin(), nextRow.end()));
            string key = row.substr(index, 2);
            if (transitions.find(key) == transitions.end()) return false;
            for (char c : transitions[key]) {
                nextRow[index] = c;
                if (fillNextRow(index + 1)) return true;
            }
            return false;
        };
        return fillNextRow(0);
    };

    return dfs(bottom);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where $n$ is the length of the `bottom` row. This is because we try all possible transitions for each block in the `bottom` row.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the `bottom` row. This is because we need to store the recursive call stack.
> - **Why these complexities occur:** The brute force approach tries all possible transitions, resulting in exponential time complexity. The recursive call stack requires linear space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to use memoization to store the results of subproblems.
- We can use a `unordered_map` to store the results of subproblems, where the key is the current row and the value is a boolean indicating whether a pyramid can be formed.
- We can use a recursive approach with memoization to try all possible transitions.

```cpp
bool pyramidTransition(string bottom, vector<string>& allowed) {
    unordered_map<string, vector<char>> transitions;
    for (string s : allowed) {
        transitions[s.substr(0, 2)].push_back(s[2]);
    }

    unordered_map<string, bool> memo;
    function<bool(string)> dfs = [&](string row) {
        if (memo.find(row) != memo.end()) return memo[row];
        if (row.size() == 1) return memo[row] = true;
        vector<char> nextRow(row.size() - 1, '.');
        function<bool(int)> fillNextRow = [&](int index) {
            if (index == row.size() - 1) return dfs(string(nextRow.begin(), nextRow.end()));
            string key = row.substr(index, 2);
            if (transitions.find(key) == transitions.end()) return false;
            for (char c : transitions[key]) {
                nextRow[index] = c;
                if (fillNextRow(index + 1)) return true;
            }
            return false;
        };
        return memo[row] = fillNextRow(0);
    };

    return dfs(bottom);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where $n$ is the length of the `bottom` row. However, the actual time complexity is much less than this due to memoization.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the `bottom` row. This is because we need to store the recursive call stack and the memoization table.
> - **Optimality proof:** The optimal approach uses memoization to store the results of subproblems, resulting in a significant reduction in time complexity. This is the best possible complexity for this problem.

---

### Final Notes

**Learning Points:**
- The key algorithmic concept demonstrated in this problem is memoization, which is used to store the results of subproblems.
- The problem-solving pattern identified is to use recursive approaches with memoization to solve problems with overlapping subproblems.
- The optimization technique learned is to use memoization to reduce the time complexity of recursive approaches.

**Mistakes to Avoid:**
- A common implementation error is to forget to initialize the memoization table.
- An edge case to watch for is when the `bottom` row is empty or the `allowed` list is empty.
- A performance pitfall is to use a recursive approach without memoization, resulting in exponential time complexity.