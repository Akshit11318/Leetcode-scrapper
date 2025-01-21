## Stepping Numbers
**Problem Link:** https://leetcode.com/problems/stepping-numbers/description

**Problem Statement:**
- Input format and constraints: Given two integers `low` and `high`, find all the `stepping numbers` in the range `[low, high]`.
- Expected output format: Return a list of all `stepping numbers` in the range `[low, high]`.
- Key requirements and edge cases to consider: A `stepping number` is a positive integer that can be reached by taking a certain number of steps from the number 0. A single step is defined as incrementing or decrementing the number by 1. For example, starting from 0, we can reach 1 and 9 in one step, 10 and 8 in two steps, and so on.
- Example test cases with explanations:
  - Input: `low = 0`, `high = 21`
  - Output: `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 21]`
  - Explanation: The `stepping numbers` in the range `[0, 21]` are `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 21]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find all `stepping numbers` in the range `[low, high]`, we can start from 0 and perform a breadth-first search (BFS) to explore all possible `stepping numbers`.
- Step-by-step breakdown of the solution:
  1. Initialize a queue with the starting number 0.
  2. Perform BFS to explore all possible `stepping numbers`.
  3. For each `stepping number`, check if it is within the range `[low, high]`. If it is, add it to the result list.
- Why this approach comes to mind first: This approach is straightforward and easy to understand. It involves exploring all possible `stepping numbers` and checking if they are within the given range.

```cpp
#include <vector>
#include <queue>
using namespace std;

vector<int> findSteppingNumbers(int low, int high) {
    vector<int> result;
    queue<int> q;
    q.push(0);
    
    while (!q.empty()) {
        int num = q.front();
        q.pop();
        
        if (num >= low && num <= high) {
            result.push_back(num);
        }
        
        if (num == 0 || num > high) {
            continue;
        }
        
        int lastDigit = num % 10;
        int nextNum1 = num * 10 + lastDigit - 1;
        int nextNum2 = num * 10 + lastDigit + 1;
        
        if (lastDigit != 0) {
            q.push(nextNum1);
        }
        
        if (lastDigit != 9) {
            q.push(nextNum2);
        }
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of `stepping numbers` and $m$ is the average number of digits in a `stepping number`.
> - **Space Complexity:** $O(n \cdot m)$, where $n$ is the number of `stepping numbers` and $m$ is the average number of digits in a `stepping number`.
> - **Why these complexities occur:** The time and space complexities occur because we are exploring all possible `stepping numbers` and storing them in the result list.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of performing BFS from 0, we can start from the `low` and perform DFS to explore all possible `stepping numbers`.
- Detailed breakdown of the approach:
  1. Initialize an empty result list.
  2. Perform DFS from `low` to `high` to explore all possible `stepping numbers`.
  3. For each `stepping number`, check if it is within the range `[low, high]`. If it is, add it to the result list.
- Proof of optimality: This approach is optimal because we are only exploring the necessary `stepping numbers` within the given range.

```cpp
#include <vector>
using namespace std;

void dfs(int num, int low, int high, vector<int>& result) {
    if (num >= low && num <= high) {
        result.push_back(num);
    }
    
    if (num == 0 || num > high) {
        return;
    }
    
    int lastDigit = num % 10;
    int nextNum1 = num * 10 + lastDigit - 1;
    int nextNum2 = num * 10 + lastDigit + 1;
    
    if (lastDigit != 0) {
        dfs(nextNum1, low, high, result);
    }
    
    if (lastDigit != 9) {
        dfs(nextNum2, low, high, result);
    }
}

vector<int> findSteppingNumbers(int low, int high) {
    vector<int> result;
    
    for (int i = max(low, 0); i <= high; i++) {
        dfs(i, low, high, result);
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of `stepping numbers` and $m$ is the average number of digits in a `stepping number`.
> - **Space Complexity:** $O(n \cdot m)$, where $n$ is the number of `stepping numbers` and $m$ is the average number of digits in a `stepping number`.
> - **Optimality proof:** This approach is optimal because we are only exploring the necessary `stepping numbers` within the given range.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: BFS, DFS, and `stepping numbers`.
- Problem-solving patterns identified: Exploring all possible solutions and checking if they are within the given range.
- Optimization techniques learned: Starting from the `low` and performing DFS to explore all possible `stepping numbers`.
- Similar problems to practice: Other problems involving `stepping numbers` and BFS/DFS.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if a `stepping number` is within the given range before adding it to the result list.
- Edge cases to watch for: Handling the case where `low` is greater than `high`.
- Performance pitfalls: Exploring all possible `stepping numbers` without checking if they are within the given range.
- Testing considerations: Testing the solution with different ranges and edge cases.