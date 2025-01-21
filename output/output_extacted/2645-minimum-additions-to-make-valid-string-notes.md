## Minimum Additions to Make Valid String

**Problem Link:** https://leetcode.com/problems/minimum-additions-to-make-valid-string/description

**Problem Statement:**
- Input: A string `s` consisting of only the characters `(` and `)`.
- Output: The minimum number of additions required to make the string valid.
- Key requirements and edge cases:
  - The input string can be empty.
  - The input string can have unbalanced parentheses.
- Example test cases:
  - `s = "())"`, the output should be `1`.
  - `s = "((("`, the output should be `3`.
  - `s = ")"`, the output should be `1`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking all possible combinations of adding parentheses to the string.
- Step-by-step breakdown:
  1. Generate all possible strings by adding `(` or `)` at each position in the input string.
  2. For each generated string, check if it is valid.
  3. Keep track of the minimum number of additions required to make a string valid.
- Why this approach comes to mind first: It is a straightforward, exhaustive approach that guarantees finding the minimum number of additions if the string is not too long.

```cpp
int minAdditionsToMakeValid(string s) {
    int minAdditions = INT_MAX;
    int n = s.length();
    for (int mask = 0; mask < (1 << (2 * n)); mask++) {
        string temp = s;
        int additions = 0;
        for (int i = 0; i < 2 * n; i++) {
            if ((mask & (1 << i)) != 0) {
                if (i < n) {
                    temp.insert(i, "(");
                    i++;
                    additions++;
                } else {
                    temp.insert(i - n + 1, ")");
                    i++;
                    additions++;
                }
            }
        }
        if (isValid(temp)) {
            minAdditions = min(minAdditions, additions);
        }
    }
    return minAdditions;
}

bool isValid(string s) {
    stack<char> st;
    for (char c : s) {
        if (c == '(') {
            st.push(c);
        } else if (c == ')') {
            if (st.empty()) return false;
            st.pop();
        }
    }
    return st.empty();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{2n} \cdot n)$, where $n$ is the length of the input string. This is because we generate $2^{2n}$ possible strings and for each string, we perform $n$ operations.
> - **Space Complexity:** $O(2n)$, for storing the generated strings.
> - **Why these complexities occur:** These complexities occur because we are generating all possible combinations of adding parentheses to the string, which results in exponential time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: We can maintain a balance of open and close parentheses as we iterate through the string.
- Detailed breakdown:
  1. Initialize a counter for the balance of open and close parentheses.
  2. Iterate through the string. For each character:
    - If the character is `(`, increment the balance counter.
    - If the character is `)`, decrement the balance counter.
    - If the balance counter is negative, increment the result counter and reset the balance counter to 0.
- Why further optimization is impossible: This approach has a linear time complexity, which is the best we can achieve because we must at least read the input string once.

```cpp
int minAdditionsToMakeValid(string s) {
    int balance = 0;
    int result = 0;
    for (char c : s) {
        if (c == '(') {
            balance++;
        } else {
            balance--;
            if (balance < 0) {
                result++;
                balance = 0;
            }
        }
    }
    return result + balance;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string. This is because we make a single pass through the string.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the balance and result counters.
> - **Optimality proof:** This approach is optimal because it has a linear time complexity, which is the best we can achieve for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a balance counter to keep track of the balance of open and close parentheses.
- Problem-solving patterns identified: Maintaining a balance counter is a common pattern in problems involving balanced parentheses.
- Optimization techniques learned: Avoiding unnecessary operations by using a simple balance counter instead of generating all possible strings.
- Similar problems to practice: Other problems involving balanced parentheses, such as checking if a string is valid or finding the minimum number of deletions to make a string valid.

**Mistakes to Avoid:**
- Common implementation errors: Not resetting the balance counter when it becomes negative.
- Edge cases to watch for: Handling empty strings or strings with unbalanced parentheses.
- Performance pitfalls: Using an exponential time complexity approach when a linear time complexity approach is possible.
- Testing considerations: Testing the function with different inputs, including empty strings and strings with unbalanced parentheses.