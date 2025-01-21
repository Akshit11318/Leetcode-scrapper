## Find Minimum Time to Reach Last Room I
**Problem Link:** https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i/description

**Problem Statement:**
- Input: `n` rooms, `times` array representing time taken to reach each room, `targetRoom` as the last room to reach.
- Expected output: Minimum time required to reach the last room.
- Key requirements: Calculate the minimum time by considering the time taken to reach each room.
- Example test cases:
  - `n = 2, times = [1,2], targetRoom = 1` -> Output: `3`
  - `n = 3, times = [1,2,3], targetRoom = 2` -> Output: `6`

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to calculate the time taken to reach each room and sum them up to find the minimum time to reach the last room.
- This approach involves iterating through each room and adding the time taken to reach that room.
- However, this approach might not be efficient for large inputs.

```cpp
class Solution {
public:
    int minTimeToVisitAllRooms(vector<int>& times, int targetRoom) {
        int time = 0;
        for (int i = 0; i <= targetRoom; i++) {
            time += times[i];
        }
        return time;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of rooms. This is because we iterate through each room once.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the time variable.
> - **Why these complexities occur:** The time complexity is linear because we visit each room once, and the space complexity is constant because we only use a fixed amount of space.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to realize that we only need to sum the times of the rooms up to the target room.
- This approach is the same as the brute force approach, as the problem statement already implies a linear solution.
- We can prove that this is optimal because we must visit each room at least once, and the problem statement does not provide any additional information that could be used to optimize the solution further.

```cpp
class Solution {
public:
    int minTimeToVisitAllRooms(vector<int>& times, int targetRoom) {
        int time = 0;
        for (int i = 0; i <= targetRoom; i++) {
            time += times[i];
        }
        return time;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of rooms. This is because we iterate through each room once.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the time variable.
> - **Optimality proof:** This is the optimal solution because we must visit each room at least once, and the problem statement does not provide any additional information that could be used to optimize the solution further.

---

### Final Notes
**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, summation.
- Problem-solving patterns identified: Linear iteration, cumulative sum.
- Optimization techniques learned: None, as the problem statement already implies a linear solution.
- Similar problems to practice: Other problems involving iteration and summation.

**Mistakes to Avoid:**
- Common implementation errors: Off-by-one errors, incorrect indexing.
- Edge cases to watch for: Empty input arrays, negative times.
- Performance pitfalls: Using inefficient data structures or algorithms.
- Testing considerations: Test with different input sizes, edge cases, and boundary conditions.