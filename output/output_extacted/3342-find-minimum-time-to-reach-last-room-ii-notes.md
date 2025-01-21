## Find Minimum Time to Reach Last Room II
**Problem Link:** https://leetcode.com/problems/find-minimum-time-to-reach-last-room-ii/description

**Problem Statement:**
- Input: A list of integers `rooms` where `rooms[i]` is the time it takes to clean the `i-th` room, and an integer `k` representing the number of keys available.
- Constraints: `1 <= rooms.length <= 10^5`, `1 <= rooms[i] <= 10^5`, `1 <= k <= 10^5`.
- Expected output: The minimum time required to clean all rooms.
- Key requirements: Minimize the total time by using the available keys to clean rooms in parallel.
- Example test cases:
  - `rooms = [1,2,3], k = 1` -> `6` because we clean one room at a time.
  - `rooms = [1,2,3], k = 2` -> `3` because we can clean two rooms at the same time.

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to try all possible combinations of rooms and keys to find the minimum time.
- Step-by-step breakdown:
  1. Sort the rooms in descending order of their cleaning times.
  2. Initialize the minimum time to infinity.
  3. Use recursion or backtracking to try all possible combinations of rooms and keys.
  4. For each combination, calculate the total time required to clean all rooms.
  5. Update the minimum time if the current combination results in a smaller time.

```cpp
#include <vector>
#include <algorithm>

using namespace std;

int findMinimumTimeToReachLastRoomII(vector<int>& rooms, int k) {
    // Sort rooms in descending order
    sort(rooms.begin(), rooms.end(), greater<int>());
    
    int n = rooms.size();
    int minTime = INT_MAX;
    
    // Recursive function to try all combinations
    function<void(int, int, int)> tryCombinations = 
        [&](int index, int currentTime, int keysUsed) {
            if (index == n) {
                minTime = min(minTime, currentTime);
                return;
            }
            
            // Try using a key for the current room
            if (keysUsed < k) {
                tryCombinations(index + 1, max(currentTime, rooms[index]), keysUsed + 1);
            }
            
            // Try not using a key for the current room
            tryCombinations(index + 1, currentTime + rooms[index], keysUsed);
        };
    
    tryCombinations(0, 0, 0);
    
    return minTime;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where $n$ is the number of rooms, because we try all possible combinations of rooms and keys.
> - **Space Complexity:** $O(n)$, where $n$ is the number of rooms, because of the recursive call stack.
> - **Why these complexities occur:** The brute force approach tries all possible combinations of rooms and keys, resulting in an exponential time complexity.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to use a priority queue to keep track of the rooms that are being cleaned.
- Detailed breakdown:
  1. Initialize a priority queue with the cleaning times of the first `k` rooms.
  2. Initialize the total time to 0.
  3. While there are still rooms to be cleaned:
    - Extract the room with the smallest cleaning time from the priority queue.
    - Add the cleaning time of the extracted room to the total time.
    - If there are still rooms to be cleaned, add the next room to the priority queue.
  4. Return the total time as the minimum time required to clean all rooms.

```cpp
#include <vector>
#include <queue>

using namespace std;

int findMinimumTimeToReachLastRoomII(vector<int>& rooms, int k) {
    // Initialize priority queue with the first k rooms
    priority_queue<int> pq;
    for (int i = 0; i < min(k, (int)rooms.size()); i++) {
        pq.push(rooms[i]);
    }
    
    int totalTime = 0;
    int index = k;
    
    // Continue cleaning rooms until all rooms are done
    while (index < rooms.size() || !pq.empty()) {
        // Extract the room with the smallest cleaning time
        int currentTime = pq.top();
        pq.pop();
        
        // Add the cleaning time to the total time
        totalTime += currentTime;
        
        // Add the next room to the priority queue if available
        if (index < rooms.size()) {
            pq.push(rooms[index]);
            index++;
        }
    }
    
    return totalTime;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log k)$, where $n$ is the number of rooms and $k$ is the number of keys, because we use a priority queue to keep track of the rooms.
> - **Space Complexity:** $O(k)$, where $k$ is the number of keys, because of the priority queue.
> - **Optimality proof:** This approach is optimal because it minimizes the total time by using the available keys to clean rooms in parallel, and it uses a priority queue to efficiently select the room with the smallest cleaning time.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: priority queues, greedy algorithms.
- Problem-solving patterns identified: minimizing total time by using available resources (keys) efficiently.
- Optimization techniques learned: using priority queues to select the most efficient option (room with smallest cleaning time).
- Similar problems to practice: other problems involving priority queues and resource allocation.

**Mistakes to Avoid:**
- Common implementation errors: forgetting to update the total time correctly, not handling edge cases (e.g., when `k` is greater than the number of rooms).
- Edge cases to watch for: when `k` is 0 or 1, when the number of rooms is 0.
- Performance pitfalls: using an inefficient data structure (e.g., a list instead of a priority queue) to keep track of the rooms.
- Testing considerations: testing with different values of `k` and room cleaning times to ensure the algorithm works correctly in all scenarios.