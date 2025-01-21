## Grid Illumination

**Problem Link:** https://leetcode.com/problems/grid-illumination/description

**Problem Statement:**
- Input format: An integer `n`, and a 2D array `lamps` where each lamp is represented as an array `[x, y]`, and another 2D array `queries` where each query is represented as an array `[x, y]`.
- Constraints: `1 <= n <= 10^5`, `0 <= x, y < n`.
- Expected output format: An array of integers where each integer represents whether the cell at the corresponding query is illuminated or not.
- Key requirements and edge cases to consider:
  - A cell is illuminated if it has at least one lamp in the same row, column, or diagonal.
  - Each lamp can be turned off at most once.
  - If a query cell is illuminated, return 1, otherwise return 0.
- Example test cases with explanations:
  - For `n = 5`, `lamps = [[0,0],[0,4],[1,2],[3,4],[4,3]]`, and `queries = [[0,0],[1,4],[1,1],[2,2],[3,3],[4,4]]`, the output should be `[1,1,0,1,1,0]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: For each query, check all lamps to see if any of them can illuminate the query cell.
- Step-by-step breakdown of the solution:
  1. Iterate over each query.
  2. For each query, iterate over each lamp.
  3. Check if the lamp can illuminate the query cell by checking if they are in the same row, column, or diagonal.
  4. If a lamp can illuminate the query cell, mark the query cell as illuminated and break the loop.
- Why this approach comes to mind first: It's a straightforward and intuitive solution, but it's inefficient due to the nested loops.

```cpp
#include <vector>
using namespace std;

vector<int> gridIllumination(int n, vector<vector<int>>& lamps, vector<vector<int>>& queries) {
    vector<int> res(queries.size());
    for (int i = 0; i < queries.size(); i++) {
        bool illuminated = false;
        for (auto& lamp : lamps) {
            if (lamp[0] == queries[i][0] || lamp[1] == queries[i][1] || 
                abs(lamp[0] - queries[i][0]) == abs(lamp[1] - queries[i][1])) {
                illuminated = true;
                break;
            }
        }
        res[i] = illuminated ? 1 : 0;
    }
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(q \cdot l)$ where $q$ is the number of queries and $l$ is the number of lamps.
> - **Space Complexity:** $O(1)$ as we only use a constant amount of space to store the result.
> - **Why these complexities occur:** The time complexity is due to the nested loops over queries and lamps, and the space complexity is due to the constant amount of space used to store the result.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a hash set to store the lamps and use four hash maps to store the count of lamps in each row, column, and diagonal.
- Detailed breakdown of the approach:
  1. Create a hash set to store the lamps.
  2. Create four hash maps to store the count of lamps in each row, column, and diagonal.
  3. Iterate over each lamp and update the count in the corresponding hash maps.
  4. Iterate over each query and check if the query cell is illuminated by checking the count in the corresponding hash maps.
- Proof of optimality: This approach is optimal because it uses hash sets and hash maps to reduce the time complexity to $O(n + q + l)$.

```cpp
#include <vector>
#include <unordered_set>
#include <unordered_map>
using namespace std;

vector<int> gridIllumination(int n, vector<vector<int>>& lamps, vector<vector<int>>& queries) {
    unordered_set<string> lampSet;
    unordered_map<int, int> rowCount, colCount, diagCount, antiDiagCount;
    
    for (auto& lamp : lamps) {
        string key = to_string(lamp[0]) + "," + to_string(lamp[1]);
        lampSet.insert(key);
        rowCount[lamp[0]]++;
        colCount[lamp[1]]++;
        diagCount[lamp[0] - lamp[1]]++;
        antiDiagCount[lamp[0] + lamp[1]]++;
    }
    
    vector<int> res(queries.size());
    for (int i = 0; i < queries.size(); i++) {
        bool illuminated = false;
        if (rowCount[queries[i][0]] > 0 || colCount[queries[i][1]] > 0 || 
            diagCount[queries[i][0] - queries[i][1]] > 0 || 
            antiDiagCount[queries[i][0] + queries[i][1]] > 0) {
            illuminated = true;
        }
        res[i] = illuminated ? 1 : 0;
        
        // Turn off the lamps that illuminate the current query cell
        for (int x = max(0, queries[i][0] - 1); x <= min(n - 1, queries[i][0] + 1); x++) {
            for (int y = max(0, queries[i][1] - 1); y <= min(n - 1, queries[i][1] + 1); y++) {
                string key = to_string(x) + "," + to_string(y);
                if (lampSet.find(key) != lampSet.end()) {
                    lampSet.erase(key);
                    rowCount[x]--;
                    colCount[y]--;
                    diagCount[x - y]--;
                    antiDiagCount[x + y]--;
                }
            }
        }
    }
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + q + l)$ where $n$ is the size of the grid, $q$ is the number of queries, and $l$ is the number of lamps.
> - **Space Complexity:** $O(n + q + l)$ as we use hash sets and hash maps to store the lamps and the count of lamps in each row, column, and diagonal.
> - **Optimality proof:** This approach is optimal because it uses hash sets and hash maps to reduce the time complexity to $O(n + q + l)$, and it only iterates over each lamp and query once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Hash sets and hash maps, iteration over queries and lamps.
- Problem-solving patterns identified: Using hash sets and hash maps to reduce time complexity.
- Optimization techniques learned: Using hash sets and hash maps to store the count of lamps in each row, column, and diagonal.
- Similar problems to practice: Other problems that involve using hash sets and hash maps to solve optimization problems.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, not using hash sets and hash maps to reduce time complexity.
- Edge cases to watch for: Empty input, invalid input, large input.
- Performance pitfalls: Not using hash sets and hash maps, using nested loops over queries and lamps.
- Testing considerations: Test for edge cases, test for large input, test for performance.