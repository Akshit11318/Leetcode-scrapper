## Campus Bikes

**Problem Link:** https://leetcode.com/problems/campus-bikes/description

**Problem Statement:**
- Input format: `workers` and `bikes` arrays, each containing pairs of coordinates representing worker locations and bike locations respectively.
- Constraints: `1 <= workers.length <= 10`, `1 <= bikes.length <= 10`.
- Expected output format: An array of bike assignments for each worker, where the index represents the worker and the value represents the bike assigned.
- Key requirements and edge cases to consider: Each worker should be assigned to the closest bike, and if there are multiple bikes at the same distance from a worker, the bike with the smallest index should be assigned.
- Example test cases with explanations:
  - `workers = [[1,2],[3,4]]`, `bikes = [[1,0],[2,1],[2,0]]`, expected output: `[0,2]`.
  - `workers = [[0,0],[2,1]]`, `bikes = [[1,2],[0,1]]`, expected output: `[0,1]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over each worker and calculate the distance to each bike, then assign the bike with the minimum distance to the worker.
- Step-by-step breakdown of the solution:
  1. Initialize an empty array to store the bike assignments for each worker.
  2. Iterate over each worker and calculate the distance to each bike.
  3. Find the bike with the minimum distance for each worker and assign it.
- Why this approach comes to mind first: It is a straightforward and intuitive solution that directly addresses the problem statement.

```cpp
vector<int> assignBikes(vector<vector<int>>& workers, vector<vector<int>>& bikes) {
    int n = workers.size();
    vector<int> res(n, -1);
    for (int i = 0; i < n; i++) {
        int minDist = INT_MAX;
        int minIndex = -1;
        for (int j = 0; j < bikes.size(); j++) {
            int dist = abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1]);
            if (dist < minDist) {
                minDist = dist;
                minIndex = j;
            } else if (dist == minDist) {
                minIndex = min(minIndex, j);
            }
        }
        res[i] = minIndex;
    }
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times m)$, where $n$ is the number of workers and $m$ is the number of bikes, because we iterate over each worker and each bike.
> - **Space Complexity:** $O(n)$, because we store the bike assignments for each worker in an array of size $n$.
> - **Why these complexities occur:** The time complexity is due to the nested loops, and the space complexity is due to the storage of the bike assignments.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a similar approach to the brute force solution, but we need to ensure that we handle the case where multiple bikes are at the same distance from a worker.
- Detailed breakdown of the approach:
  1. Initialize an empty array to store the bike assignments for each worker.
  2. Iterate over each worker and calculate the distance to each bike.
  3. Find the bike with the minimum distance for each worker and assign it, ensuring that if there are multiple bikes at the same distance, the bike with the smallest index is assigned.
- Proof of optimality: This solution is optimal because it directly addresses the problem statement and ensures that each worker is assigned to the closest bike.

```cpp
vector<int> assignBikes(vector<vector<int>>& workers, vector<vector<int>>& bikes) {
    int n = workers.size();
    vector<int> res(n, -1);
    vector<bool> used(n, false);
    for (int i = 0; i < n; i++) {
        int minDist = INT_MAX;
        int minIndex = -1;
        for (int j = 0; j < bikes.size(); j++) {
            if (used[j]) continue;
            int dist = abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1]);
            if (dist < minDist) {
                minDist = dist;
                minIndex = j;
            } else if (dist == minDist) {
                minIndex = min(minIndex, j);
            }
        }
        res[i] = minIndex;
        used[minIndex] = true;
    }
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times m)$, where $n$ is the number of workers and $m$ is the number of bikes, because we iterate over each worker and each bike.
> - **Space Complexity:** $O(n + m)$, because we store the bike assignments for each worker in an array of size $n$ and a boolean array of size $m$ to track used bikes.
> - **Optimality proof:** This solution is optimal because it directly addresses the problem statement and ensures that each worker is assigned to the closest bike, handling the case where multiple bikes are at the same distance.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, conditional statements, and distance calculation.
- Problem-solving patterns identified: Directly addressing the problem statement and handling edge cases.
- Optimization techniques learned: Ensuring that each worker is assigned to the closest bike and handling the case where multiple bikes are at the same distance.

**Mistakes to Avoid:**
- Common implementation errors: Not handling the case where multiple bikes are at the same distance from a worker.
- Edge cases to watch for: Ensuring that the solution handles the case where there are multiple workers and bikes.
- Performance pitfalls: Not using an efficient data structure to store the bike assignments and used bikes.
- Testing considerations: Ensuring that the solution is tested with different inputs and edge cases.