## Score of Parentheses
**Problem Link:** https://leetcode.com/problems/score-of-parentheses/description

**Problem Statement:**
- Input: A string `S` containing only parentheses `(` and `)`.
- Constraints: The input string is non-empty and contains only parentheses.
- Expected Output: The score of the string, which is the sum of scores for each set of balanced parentheses.
- Key Requirements: The score of an empty substring is 0, the score of `()` is 1, and the score of `(A)` is twice the score of `A`, where `A` is a substring.
- Example Test Cases:
  - Input: `S = "()"` Output: `1`
  - Input: `S = "(())"` Output: `2`

---

### Brute Force Approach
**Explanation:**
- The initial thought process involves iterating over all possible substrings of `S` to find balanced parentheses and calculate their scores.
- This approach comes to mind first because it directly addresses the requirement to find the score of all sets of balanced parentheses.

```cpp
int scoreOfParentheses(string S) {
    int score = 0;
    for (int i = 0; i < S.size(); i++) {
        for (int j = i + 1; j <= S.size(); j++) {
            string substr = S.substr(i, j - i);
            if (isValid(substr)) {
                score += calculateScore(substr);
            }
        }
    }
    return score;
}

bool isValid(string S) {
    int balance = 0;
    for (char c : S) {
        if (c == '(') balance++;
        else balance--;
        if (balance < 0) return false;
    }
    return balance == 0;
}

int calculateScore(string S) {
    if (S == "()") return 1;
    int balance = 0, score = 0;
    for (int i = 0; i < S.size(); i++) {
        if (S[i] == '(') balance++;
        else {
            balance--;
            if (balance == 0) {
                score *= 2;
            }
        }
    }
    return score;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of `S`. This is because for each character in `S`, we potentially generate all substrings and then check each for validity and calculate its score.
> - **Space Complexity:** $O(n)$, as in the worst case, we might store a substring of length $n$.
> - **Why these complexities occur:** The brute force approach involves nested loops to generate substrings and then additional operations to validate and score each substring, leading to high time complexity. The space complexity is due to storing substrings.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to use a stack to track the score of each set of parentheses as we iterate through `S`.
- When we encounter `(`, we push the current score onto the stack and reset the current score to 0.
- When we encounter `)`, if the current score is 0, we set it to 1 (for `()`); otherwise, we multiply it by 2 (for `(A)` where `A` is a substring). Then, we add the current score to the top of the stack (which represents the score of the outer parentheses set) and pop the top of the stack to update the current score.
- This approach ensures we correctly calculate the score for all sets of balanced parentheses in a single pass.

```cpp
int scoreOfParentheses(string S) {
    int score = 0;
    stack<int> st;
    for (char c : S) {
        if (c == '(') {
            st.push(score);
            score = 0;
        } else {
            if (score == 0) score = 1;
            else score *= 2;
            if (!st.empty()) {
                score += st.top();
                st.pop();
            }
        }
    }
    return score;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of `S`, as we make a single pass through the string.
> - **Space Complexity:** $O(n)$, as in the worst case (a string of all `(`), the size of the stack can grow up to $n$.
> - **Optimality proof:** This is the best possible time complexity because we must at least read the input once. The space complexity is also optimal because we need to store the scores of the parentheses sets, and in the worst case, we have $n$ sets.

---

### Final Notes
**Learning Points:**
- Using a stack to track scores of parentheses sets.
- The importance of understanding the scoring rules for balanced parentheses.
- Optimizing the solution by avoiding unnecessary operations and using a single pass through the input.

**Mistakes to Avoid:**
- Incorrectly handling the scoring for `()` and `(A)`.
- Not resetting the score when encountering a new set of parentheses.
- Failing to consider the impact of nested parentheses on the score calculation.

**Similar Problems to Practice:**
- Implementing a stack to solve other string or array problems that involve nested structures or recursive patterns.
- Practicing problems that require calculating scores or sums based on specific rules and patterns in the input.