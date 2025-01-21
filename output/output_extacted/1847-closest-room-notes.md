## Closest Room
**Problem Link:** [https://leetcode.com/problems/closest-room/description](https://leetcode.com/problems/closest-room/description)

**Problem Statement:**
- Input format: `int isOccupied[][]`, `int size[]`, and `int` `k`.
- Constraints: `1 <= isOccupied.length <= k <= 1000`, `1 <= isOccupied[i].length <= 2`, `1 <= size.length <= 1000`, `1 <= size[i] <= 1000`.
- Expected output format: `int[]`.
- Key requirements: Find the `k` closest rooms to the given size.
- Example test cases with explanations:
  - Input: `isOccupied = [[1,1],[2,2],[3,2]], size = [3,4,5], k = 2`.
  - Output: `[2,3]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Calculate the absolute difference between each room size and the given size, then sort the rooms based on this difference.
- Step-by-step breakdown of the solution:
  1. Create a `vector<pair<int, int>>` to store the room id and its corresponding size difference.
  2. Iterate over each room and calculate the size difference.
  3. Store the room id and size difference in the `vector`.
  4. Sort the `vector` based on the size difference.
  5. Return the `k` closest room ids.

```cpp
#include <vector>
#include <algorithm>
#include <utility>

vector<int> closestRoom(vector<vector<int>>& isOccupied, vector<int>& size, int k) {
    vector<pair<int, int>> diff;
    for (int i = 0; i < isOccupied.size(); i++) {
        int sz = isOccupied[i][1];
        int id = isOccupied[i][0];
        int minDiff = INT_MAX;
        for (int j = 0; j < size.size(); j++) {
            int d = abs(sz - size[j]);
            minDiff = min(minDiff, d);
        }
        diff.push_back({id, minDiff});
    }
    sort(diff.begin(), diff.end(), [](const pair<int, int>& a, const pair<int, int>& b) {
        return a.second < b.second;
    });
    vector<int> result;
    for (int i = 0; i < k; i++) {
        result.push_back(diff[i].first);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot log(n))$, where $n$ is the number of rooms and $m$ is the number of sizes.
> - **Space Complexity:** $O(n)$, where $n$ is the number of rooms.
> - **Why these complexities occur:** The time complexity occurs due to the sorting of the `vector`, and the space complexity occurs due to the storage of the room id and size difference in the `vector`.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a priority queue to store the room id and its corresponding size difference.
- Detailed breakdown of the approach:
  1. Create a `priority_queue` to store the room id and its corresponding size difference.
  2. Iterate over each room and calculate the size difference.
  3. Store the room id and size difference in the `priority_queue`.
  4. Return the `k` closest room ids.

```cpp
#include <queue>
#include <vector>
#include <utility>

vector<int> closestRoom(vector<vector<int>>& isOccupied, vector<int>& size, int k) {
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    for (int i = 0; i < isOccupied.size(); i++) {
        int sz = isOccupied[i][1];
        int id = isOccupied[i][0];
        int minDiff = INT_MAX;
        for (int j = 0; j < size.size(); j++) {
            int d = abs(sz - size[j]);
            minDiff = min(minDiff, d);
        }
        pq.push({minDiff, id});
    }
    vector<int> result;
    for (int i = 0; i < k; i++) {
        result.push_back(pq.top().second);
        pq.pop();
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot log(k))$, where $n$ is the number of rooms and $m$ is the number of sizes.
> - **Space Complexity:** $O(k)$, where $k$ is the number of closest rooms.
> - **Optimality proof:** This is the optimal solution because we are using a priority queue to store the room id and its corresponding size difference, which allows us to efficiently retrieve the `k` closest room ids.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Priority queues, sorting, and iteration.
- Problem-solving patterns identified: Using data structures to efficiently solve problems.
- Optimization techniques learned: Using priority queues to reduce time complexity.
- Similar problems to practice: Problems involving priority queues and sorting.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect usage of priority queues and sorting algorithms.
- Edge cases to watch for: Handling cases where the number of rooms is less than `k`.
- Performance pitfalls: Using inefficient data structures and algorithms.
- Testing considerations: Testing the solution with different inputs and edge cases.