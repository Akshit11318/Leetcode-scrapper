## Baseball Game
**Problem Link:** https://leetcode.com/problems/baseball-game/description

**Problem Statement:**
- Input format and constraints: The input is a list of strings representing the operations in a baseball game. The operations can be one of the following: integer score, "C" to cancel the previous score, "D" to double the previous score, or "+" to add the last two scores.
- Expected output format: The total score after all operations have been applied.
- Key requirements and edge cases to consider: The input list is non-empty and contains at most 1000 operations. Each operation is either an integer score, "C", "D", or "+".
- Example test cases with explanations:
    - Input: `["5","-2","4","C","D","9","+","+""]`
    - Output: `27`
    - Explanation: 
        1. `5` is added to the score, making it `5`.
        2. `-2` is added to the score, making it `3`.
        3. `4` is added to the score, making it `7`.
        4. `C` cancels the previous score `4`, making it `3`.
        5. `D` doubles the previous score `5`, making it `10`.
        6. `9` is added to the score, making it `19`.
        7. `+` adds the last two scores `10` and `9`, making it `28`.
        8. `+` adds the last two scores `10` and `9`, making it `27`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can iterate over the list of operations, applying each operation to a running total.
- Step-by-step breakdown of the solution:
    1. Initialize an empty list to store the scores.
    2. Iterate over the list of operations.
    3. For each operation, check if it is an integer, "C", "D", or "+".
    4. If the operation is an integer, add it to the list of scores.
    5. If the operation is "C", remove the last score from the list if it exists.
    6. If the operation is "D", double the last score in the list if it exists.
    7. If the operation is "+", add the last two scores in the list if they exist.
- Why this approach comes to mind first: This approach is straightforward and follows the problem description closely.

```cpp
vector<int> scores;
int total = 0;
for (auto& operation : operations) {
    if (isdigit(operation[0])) {
        scores.push_back(stoi(operation));
    } else if (operation == "C") {
        if (!scores.empty()) {
            scores.pop_back();
        }
    } else if (operation == "D") {
        if (!scores.empty()) {
            scores.back() *= 2;
        }
    } else if (operation == "+") {
        if (scores.size() >= 2) {
            scores.push_back(scores[scores.size() - 1] + scores[scores.size() - 2]);
        }
    }
}
for (auto& score : scores) {
    total += score;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of operations. This is because we iterate over the list of operations once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of operations. This is because in the worst case, we store every operation in the list of scores.
> - **Why these complexities occur:** The time complexity occurs because we iterate over the list of operations once. The space complexity occurs because we store every operation in the list of scores.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a stack to store the scores, which allows us to efficiently apply the "C" operation.
- Detailed breakdown of the approach:
    1. Initialize an empty stack to store the scores.
    2. Iterate over the list of operations.
    3. For each operation, check if it is an integer, "C", "D", or "+".
    4. If the operation is an integer, push it onto the stack.
    5. If the operation is "C", pop the top element from the stack if it exists.
    6. If the operation is "D", double the top element in the stack if it exists.
    7. If the operation is "+", push the sum of the top two elements in the stack onto the stack if they exist.
- Why further optimization is impossible: This approach has a time complexity of $O(n)$ and a space complexity of $O(n)$, which is optimal for this problem.

```cpp
stack<int> scores;
for (auto& operation : operations) {
    if (isdigit(operation[0])) {
        scores.push(stoi(operation));
    } else if (operation == "C") {
        if (!scores.empty()) {
            scores.pop();
        }
    } else if (operation == "D") {
        if (!scores.empty()) {
            int top = scores.top();
            scores.pop();
            scores.push(2 * top);
        }
    } else if (operation == "+") {
        if (scores.size() >= 2) {
            int top1 = scores.top();
            scores.pop();
            int top2 = scores.top();
            scores.pop();
            scores.push(top2);
            scores.push(top1);
            scores.push(top1 + top2);
        }
    }
}
int total = 0;
while (!scores.empty()) {
    total += scores.top();
    scores.pop();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of operations. This is because we iterate over the list of operations once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of operations. This is because in the worst case, we store every operation in the stack.
> - **Optimality proof:** This approach is optimal because it has a time complexity of $O(n)$ and a space complexity of $O(n)$, which is the best we can achieve for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a stack to efficiently apply operations.
- Problem-solving patterns identified: Breaking down the problem into smaller sub-problems and solving each one individually.
- Optimization techniques learned: Using a stack to reduce the time complexity of the "C" operation.
- Similar problems to practice: Other problems that involve using a stack to solve a problem, such as evaluating postfix expressions.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle edge cases, such as an empty list of operations.
- Edge cases to watch for: An empty list of operations, or a list of operations that contains only "C" or "+".
- Performance pitfalls: Using a naive approach that has a high time complexity.
- Testing considerations: Testing the solution with a variety of inputs, including edge cases.