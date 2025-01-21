## Bulb Switcher II
**Problem Link:** https://leetcode.com/problems/bulb-switcher-ii/description

**Problem Statement:**
- Input format: `n`, the number of `bulbs` to initialize, and `queries`, a list of operations where each operation is an array of two integers: `time` and `event` (either 0 for off or 1 for on).
- Constraints: `1 <= n <= 3` and `1 <= queries.length <= 100`.
- Expected output format: An array of integers where each integer represents the state of a bulb after all operations have been applied.
- Key requirements and edge cases to consider: The `bulbs` start in the off state, and each operation toggles the corresponding bulb.
- Example test cases with explanations:
  - For `n = 3` and `queries = [[2,1],[1,1],[4,0],[3,1],[4,0],[6,1],[4,1],[1,0],[4,0]]`, the output should be `[0,1,1]`.
  - For `n = 2` and `queries = [[1,1],[1,0]]`, the output should be `[0,1]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To solve this problem, we can simulate each operation on the `bulbs`.
- Step-by-step breakdown of the solution:
  1. Initialize an array `bulbs` of size `n` with all elements set to 0 (off).
  2. Iterate over each operation in `queries`.
  3. For each operation, toggle the corresponding bulb in the `bulbs` array.
- Why this approach comes to mind first: It's a straightforward way to simulate the problem.

```cpp
vector<int> flipLights(int n, vector<vector<int>>& queries) {
    vector<int> bulbs(n, 0);
    for (auto& query : queries) {
        int time = query[0];
        int event = query[1];
        if (event == 1) {
            // Toggle all bulbs
            for (int i = 0; i < n; ++i) {
                bulbs[i] = !bulbs[i];
            }
        }
    }
    return bulbs;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot q)$, where $n$ is the number of bulbs and $q$ is the number of queries.
> - **Space Complexity:** $O(n)$, for the `bulbs` array.
> - **Why these complexities occur:** The time complexity is due to the nested loop structure, and the space complexity is due to the `bulbs` array.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The state of the bulbs can be represented by a bit mask, where each bit corresponds to the state of a bulb.
- Detailed breakdown of the approach:
  1. Initialize a set `states` to store unique states of the bulbs.
  2. Iterate over each operation in `queries`.
  3. For each operation, apply the operation to the current state and add the new state to the `states` set.
- Proof of optimality: This approach ensures that we only consider unique states of the bulbs, reducing the number of iterations.

```cpp
vector<int> flipLights(int n, vector<vector<int>>& queries) {
    vector<int> bulbs(n, 0);
    unordered_set<int> states;
    states.insert(0); // Initial state
    for (auto& query : queries) {
        int time = query[0];
        int event = query[1];
        unordered_set<int> newStates;
        for (int state : states) {
            int newState = state;
            if (event == 1) {
                // Toggle all bulbs
                for (int i = 0; i < n; ++i) {
                    newState ^= (1 << i);
                }
            }
            newStates.insert(newState);
        }
        states = newStates;
    }
    vector<int> result(n, 0);
    for (int state : states) {
        for (int i = 0; i < n; ++i) {
            if ((state >> i) & 1) {
                result[i] = 1;
            }
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot q)$, where $n$ is the number of bulbs and $q$ is the number of queries.
> - **Space Complexity:** $O(2^n)$, for the `states` set.
> - **Optimality proof:** This approach ensures that we only consider unique states of the bulbs, reducing the number of iterations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Bit manipulation, set operations.
- Problem-solving patterns identified: Using a set to store unique states.
- Optimization techniques learned: Reducing the number of iterations by considering unique states.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, not using a set to store unique states.
- Edge cases to watch for: `n = 1`, `queries` is empty.
- Performance pitfalls: Using a brute force approach, not optimizing the solution.
- Testing considerations: Test with different values of `n` and `queries`.