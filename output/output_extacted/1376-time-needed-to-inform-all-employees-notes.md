## Time Needed to Inform All Employees

**Problem Link:** https://leetcode.com/problems/time-needed-to-inform-all-employees/description

**Problem Statement:**
- Input format: `n` (number of employees), `headID` (ID of the head of the company), `manager` (array of managers where `manager[i]` is the manager of `i`), `informTime` (array where `informTime[i]` is the time it takes for `i` to inform all their direct subordinates).
- Constraints: `1 <= n <= 10^5`, `0 <= headID < n`, `manager.length == n`, `informTime.length == n`.
- Expected output format: The minimum number of minutes needed to inform all employees about the updates.
- Key requirements and edge cases to consider: Handling the case where an employee has no manager (i.e., they are the head of the company), ensuring that all employees are informed, and optimizing the solution to handle large inputs efficiently.
- Example test cases with explanations:
    - Example 1: `n = 6`, `headID = 2`, `manager = [2,2,-1,2,2,2]`, `informTime = [0,0,1,0,0,0]`. The minimum time needed to inform all employees is 1.
    - Example 2: `n = 7`, `headID = 6`, `manager = [1,3,3,4,3,3,7]`, `informTime = [0,6,1,1,2,0,0]`. The minimum time needed to inform all employees is 21.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Start from the head of the company and manually calculate the time it takes to inform each employee, considering the hierarchy and inform times.
- Step-by-step breakdown of the solution:
    1. Initialize a queue with the head of the company.
    2. For each employee in the queue, add their subordinates to the queue if they haven't been processed yet.
    3. For each subordinate, calculate the time it takes for their manager to inform them and update the total time.
- Why this approach comes to mind first: It's a straightforward way to traverse the hierarchy and calculate the inform time, but it's inefficient due to repeated calculations and lack of optimization.

```cpp
#include <vector>
#include <queue>
using namespace std;

int numOfMinutes(int n, int headID, vector<int>& manager, vector<int>& informTime) {
    queue<pair<int, int>> q; // (employee ID, time to inform this employee)
    q.push({headID, 0});
    int maxTime = 0;
    
    while (!q.empty()) {
        auto [currEmp, currTime] = q.front();
        q.pop();
        maxTime = max(maxTime, currTime);
        
        for (int emp = 0; emp < n; ++emp) {
            if (manager[emp] == currEmp) {
                q.push({emp, currTime + informTime[currEmp]});
            }
        }
    }
    
    return maxTime;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ due to the nested loop structure.
> - **Space Complexity:** $O(n)$ for the queue in the worst case.
> - **Why these complexities occur:** The brute force approach has a high time complexity because it involves nested loops to traverse the hierarchy and calculate the inform time for each employee. This results in repeated calculations and inefficient use of time.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a depth-first search (DFS) approach to traverse the hierarchy and calculate the inform time for each employee. This allows for efficient calculation and avoids repeated work.
- Detailed breakdown of the approach:
    1. Create a graph to represent the hierarchy, where each employee is a node, and the edges represent the manager-subordinate relationships.
    2. Perform a DFS traversal from the head of the company, calculating the inform time for each employee based on their manager's inform time and their own inform time.
- Proof of optimality: The DFS approach ensures that each employee is visited exactly once, and the inform time is calculated correctly based on the hierarchy. This results in a significant reduction in time complexity compared to the brute force approach.

```cpp
#include <vector>
using namespace std;

int numOfMinutes(int n, int headID, vector<int>& manager, vector<int>& informTime) {
    vector<vector<int>> graph(n);
    for (int i = 0; i < n; ++i) {
        if (manager[i] != -1) {
            graph[manager[i]].push_back(i);
        }
    }
    
    int maxTime = 0;
    function<int(int)> dfs = [&](int node) {
        int time = 0;
        for (int child : graph[node]) {
            time = max(time, dfs(child));
        }
        return time + informTime[node];
    };
    
    return dfs(headID);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of employees.
> - **Space Complexity:** $O(n)$, where $n$ is the number of employees.
> - **Optimality proof:** The DFS approach ensures that each employee is visited exactly once, and the inform time is calculated correctly based on the hierarchy. This results in a significant reduction in time complexity compared to the brute force approach.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Depth-first search (DFS), graph traversal, and dynamic programming.
- Problem-solving patterns identified: Using DFS to traverse a hierarchy and calculate values based on the relationships between nodes.
- Optimization techniques learned: Avoiding repeated work by using a DFS approach and calculating values based on the hierarchy.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling the base case for the recursion or failing to update the maximum time correctly.
- Edge cases to watch for: Handling the case where an employee has no manager (i.e., they are the head of the company) and ensuring that all employees are informed.
- Performance pitfalls: Using an inefficient algorithm, such as the brute force approach, which can result in high time complexity and poor performance for large inputs.
- Testing considerations: Thoroughly testing the solution with different inputs and edge cases to ensure correctness and efficiency.