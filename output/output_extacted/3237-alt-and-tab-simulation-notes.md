## Alt and Tab Simulation
**Problem Link:** https://leetcode.com/problems/alt-and-tab-simulation/description

**Problem Statement:**
- Input format: A list of `commands` where each command is either `C` for creating a new window or `S` for switching to a specific window.
- Constraints: The number of commands and the total number of windows.
- Expected output format: A list of the window order after executing all commands.
- Key requirements and edge cases to consider: Handling the creation of new windows, switching between windows, and maintaining the order of windows.

Example test cases with explanations:
- Input: `commands = ["C", "S", "C", "S", "C", "S", "S"]`
- Output: `[2, 0, 3, 1]`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through each command and update the window order accordingly.
- Step-by-step breakdown of the solution:
  1. Initialize an empty list to store the window order.
  2. Iterate through each command in the `commands` list.
  3. If the command is `C`, append a new window to the end of the list.
  4. If the command is `S`, switch the last two windows in the list.
- Why this approach comes to mind first: It's a straightforward, intuitive approach that directly implements the problem statement.

```cpp
vector<int> altAndTabSimulation(vector<string>& commands) {
    vector<int> windows;
    for (const auto& command : commands) {
        if (command == "C") {
            windows.push_back(windows.size());
        } else if (command == "S" && windows.size() > 1) {
            int temp = windows.back();
            windows.pop_back();
            if (!windows.empty()) {
                int last = windows.back();
                windows.pop_back();
                windows.push_back(temp);
                windows.push_back(last);
            } else {
                windows.push_back(temp);
            }
        }
    }
    return windows;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of commands. This is because we're iterating through each command once.
> - **Space Complexity:** $O(n)$ for storing the window order. In the worst case, we might have to store a window for each command.
> - **Why these complexities occur:** The iteration through commands and the storage of window order contribute to these complexities.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Realizing that we only need to keep track of the current window order, and we can optimize the switching process by directly manipulating the indices.
- Detailed breakdown of the approach:
  1. Initialize an empty list to store the window order, starting with the first window.
  2. Iterate through each command in the `commands` list, starting from the second command (index 1).
  3. If the command is `C`, append a new window to the end of the list.
  4. If the command is `S`, switch the last window with the second last window if there are at least two windows.
- Proof of optimality: This approach is optimal because it directly addresses the problem statement with the minimum necessary operations, avoiding any unnecessary complexity.

```cpp
vector<int> altAndTabSimulation(vector<string>& commands) {
    vector<int> windows = {0};
    for (int i = 1; i < commands.size(); ++i) {
        if (commands[i] == "C") {
            windows.push_back(windows.size());
        } else if (commands[i] == "S" && windows.size() > 1) {
            int temp = windows.back();
            windows.pop_back();
            if (!windows.empty()) {
                int last = windows.back();
                windows.pop_back();
                windows.push_back(temp);
                windows.push_back(last);
            } else {
                windows.push_back(temp);
            }
        }
    }
    return windows;
}
```

However, the code can be optimized by using a more straightforward approach to switch the windows:

```cpp
vector<int> altAndTabSimulation(vector<string>& commands) {
    vector<int> windows = {0};
    for (int i = 1; i < commands.size(); ++i) {
        if (commands[i] == "C") {
            windows.push_back(windows.size());
        } else if (commands[i] == "S" && windows.size() > 1) {
            swap(windows[windows.size() - 1], windows[windows.size() - 2]);
        }
    }
    return windows;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of commands.
> - **Space Complexity:** $O(n)$ for storing the window order.
> - **Optimality proof:** This approach directly implements the problem statement with the minimum necessary operations, making it optimal.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Direct implementation, iteration, and list manipulation.
- Problem-solving patterns identified: Breaking down the problem into smaller, manageable parts.
- Optimization techniques learned: Simplifying the switching process by directly swapping indices.
- Similar problems to practice: Other simulation-based problems that involve list manipulation.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling edge cases, such as an empty list of commands.
- Edge cases to watch for: Handling the creation of new windows and switching between windows.
- Performance pitfalls: Using unnecessary complex data structures or algorithms.
- Testing considerations: Thoroughly testing the implementation with different inputs and edge cases.