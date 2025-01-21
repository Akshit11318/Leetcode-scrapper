## Ant on the Boundary
**Problem Link:** https://leetcode.com/problems/ant-on-the-boundary/description

**Problem Statement:**
- Input format: A string `s` representing the boundary where the ant is moving.
- Constraints: The string `s` consists of '0's and '1's, representing the inside and outside of the boundary, respectively.
- Expected output format: The number of boundaries the ant crosses.
- Key requirements and edge cases to consider:
  - The ant can only move to the right.
  - The ant starts at the leftmost character of the string.
  - The ant is considered to be inside the boundary if it is currently on a '0' character and outside if it is on a '1' character.
- Example test cases with explanations:
  - For the input "10", the ant starts on the '1' (outside), then moves to the '0' (inside), crossing one boundary.
  - For the input "110", the ant starts on the '1' (outside), moves to the next '1' (still outside), then moves to the '0' (inside), crossing one boundary.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The simplest approach is to iterate through the string and keep track of the current state of the ant (inside or outside) and the number of boundaries crossed.
- Step-by-step breakdown of the solution:
  1. Initialize variables to keep track of the current state and the number of boundaries crossed.
  2. Iterate through each character in the string.
  3. For each character, check if the ant is moving from inside to outside or vice versa.
  4. If the ant is moving across a boundary, increment the boundary counter.
- Why this approach comes to mind first: It is straightforward and directly addresses the problem statement.

```cpp
int antOnBoundary(string s) {
    int boundaries = 0;
    bool inside = (s[0] == '0');
    for (int i = 1; i < s.size(); i++) {
        bool newInside = (s[i] == '0');
        if (inside != newInside) {
            boundaries++;
        }
        inside = newInside;
    }
    return boundaries;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string `s`, because we iterate through the string once.
> - **Space Complexity:** $O(1)$, because we use a constant amount of space to store the state of the ant and the number of boundaries crossed.
> - **Why these complexities occur:** The iteration through the string is linear, and we only use a fixed amount of memory regardless of the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The problem does not require us to keep track of the ant's state after it crosses a boundary, just the number of crossings.
- Detailed breakdown of the approach:
  1. Initialize a counter for the number of boundaries crossed.
  2. Iterate through the string, comparing each character with the previous one to determine if a boundary is crossed.
- Proof of optimality: This approach is optimal because it only requires a single pass through the input string and uses constant additional space, making it as efficient as possible in terms of both time and space complexity.
- Why further optimization is impossible: Any solution must at least read the input, making $O(n)$ the best possible time complexity for this problem.

```cpp
int antOnBoundary(string s) {
    int boundaries = 0;
    for (int i = 1; i < s.size(); i++) {
        if (s[i-1] != s[i]) {
            boundaries++;
        }
    }
    return boundaries;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string `s`, because we iterate through the string once.
> - **Space Complexity:** $O(1)$, because we use a constant amount of space to store the number of boundaries crossed.
> - **Optimality proof:** This solution is optimal because it achieves the minimum possible time complexity by only reading the input once and uses the minimum possible space by only storing the count of boundary crossings.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, state tracking, and boundary detection.
- Problem-solving patterns identified: Using a single pass through the input to solve the problem efficiently.
- Optimization techniques learned: Minimizing the number of iterations and the amount of additional memory used.
- Similar problems to practice: Other problems involving string iteration and state tracking, such as detecting specific patterns or counting occurrences.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing variables properly, incorrect boundary conditions in loops, and not considering all possible states of the ant.
- Edge cases to watch for: Empty strings, strings of a single character, and strings with alternating characters.
- Performance pitfalls: Using more complex data structures or algorithms than necessary, leading to increased time or space complexity.
- Testing considerations: Thoroughly testing the solution with a variety of inputs, including edge cases, to ensure correctness.