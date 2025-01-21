## Minimum Number of Refueling Stops
**Problem Link:** https://leetcode.com/problems/minimum-number-of-refueling-stops/description

**Problem Statement:**
- Input format and constraints: The problem involves a car that starts at a certain position with a given `target` distance to reach. The car has a `startFuel` amount. There are also stations along the way, each with its own `position` and `capacity`. The goal is to determine the minimum number of refueling stops needed to reach the target.
- Expected output format: The minimum number of refueling stops required to reach the target distance. If it's impossible to reach the target, return `-1`.
- Key requirements and edge cases to consider: 
  - Handling cases where the target is within the initial fuel range.
  - Dealing with scenarios where no refueling stops are necessary.
  - Ensuring the algorithm can handle a large number of stations.
- Example test cases with explanations:
  - Example 1: `target = 1, startFuel = 1, stations = []` - In this case, no refueling stops are needed because the target is within the initial fuel range.
  - Example 2: `target = 100, startFuel = 1, stations = [[10,100]]` - Here, one refueling stop at the station with capacity 100 is sufficient to reach the target.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: The first instinct might be to try all possible combinations of refueling stops and see which one leads to the minimum number of stops.
- Step-by-step breakdown of the solution:
  1. Generate all permutations of refueling stops.
  2. For each permutation, calculate the total fuel after visiting each station.
  3. Check if the target distance can be reached with the given fuel and refueling stops.
- Why this approach comes to mind first: It's a straightforward way to ensure all possibilities are considered, but it's inefficient due to its exponential time complexity.

```cpp
class Solution {
public:
    int minRefuelStops(int target, int startFuel, vector<vector<int>>& stations) {
        int n = stations.size();
        vector<int> fuel(n + 1, 0);
        fuel[0] = startFuel;
        int minStops = INT_MAX;
        
        function<void(int, int, int)> dfs = [&](int idx, int stops, int curFuel) {
            if (idx == n) {
                if (curFuel >= target) minStops = min(minStops, stops);
                return;
            }
            // Skip current station
            dfs(idx + 1, stops, max(0, curFuel - stations[idx][0]));
            
            // Refuel at current station
            if (curFuel >= stations[idx][0]) {
                dfs(idx + 1, stops + 1, curFuel - stations[idx][0] + stations[idx][1]);
            }
        };
        
        dfs(0, 0, startFuel);
        return minStops == INT_MAX ? -1 : minStops;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$ due to the brute force exploration of all possible refueling stop combinations.
> - **Space Complexity:** $O(n)$ for the recursive call stack.
> - **Why these complexities occur:** The exponential time complexity arises from exploring all possible subsets of refueling stops, and the space complexity is due to the recursive call stack.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: The problem can be solved using a priority queue to keep track of the stations with the most fuel that can be reached.
- Detailed breakdown of the approach:
  1. Initialize a priority queue with the initial fuel and 0 stops.
  2. Iterate through each station, and for each station, check if the current fuel is enough to reach it.
  3. If it is, update the current fuel by subtracting the distance to the station and add the station's fuel capacity.
  4. If not, pop the station with the most fuel from the priority queue and add its fuel to the current fuel until the current station can be reached.
  5. Repeat this process until all stations have been considered or the target distance is reached.
- Proof of optimality: This approach ensures that the minimum number of refueling stops is found by always choosing the station with the most fuel when refueling is necessary.

```cpp
class Solution {
public:
    int minRefuelStops(int target, int startFuel, vector<vector<int>>& stations) {
        priority_queue<int> pq;
        int curFuel = startFuel;
        int stops = 0;
        
        for (auto& station : stations) {
            int pos = station[0], fuel = station[1];
            while (!pq.empty() && curFuel < pos) {
                curFuel += pq.top();
                pq.pop();
                stops++;
            }
            if (curFuel < pos) return -1;
            pq.push(fuel);
            curFuel -= pos;
        }
        
        while (!pq.empty() && curFuel < target) {
            curFuel += pq.top();
            pq.pop();
            stops++;
        }
        
        return curFuel >= target ? stops : -1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the priority queue operations.
> - **Space Complexity:** $O(n)$ for storing the stations in the priority queue.
> - **Optimality proof:** This solution is optimal because it uses a greedy strategy to always choose the station with the most fuel when refueling is necessary, ensuring the minimum number of refueling stops.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Greedy algorithms, priority queues.
- Problem-solving patterns identified: Breaking down complex problems into simpler, more manageable parts.
- Optimization techniques learned: Using priority queues to efficiently manage resources.
- Similar problems to practice: Other problems involving resource allocation and optimization.

**Mistakes to Avoid:**
- Common implementation errors: Failing to handle edge cases, such as when the target distance is within the initial fuel range.
- Edge cases to watch for: Handling scenarios where no refueling stops are necessary or where the target distance cannot be reached.
- Performance pitfalls: Using inefficient data structures or algorithms, such as brute force approaches.
- Testing considerations: Thoroughly testing the solution with various input scenarios to ensure correctness.