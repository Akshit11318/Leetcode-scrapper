## Last Moment Before All Ants Fall Out of a Plank

**Problem Link:** https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank/description

**Problem Statement:**
- Input: An integer `n` representing the length of the plank and a list of integers `left` and `right` representing the positions of ants on the plank.
- Constraints: The length of the plank `n` is a positive integer, and the positions of ants are integers within the range `[0, n]`.
- Expected output: The last moment before all ants fall out of the plank.
- Key requirements: Determine the last moment when all ants will fall off the plank, considering they move at a constant speed of 1 unit per second.
- Example test cases:
  - Input: `n = 4`, `left = [4,3]`, `right = [0,1]`
  - Output: `4`
  - Explanation: The ants at positions 4 and 3 will fall off the plank at time 4, and the ants at positions 0 and 1 will fall off the plank at time 4 as well.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Simulate the movement of ants on the plank and track the time it takes for each ant to fall off.
- Step-by-step breakdown:
  1. Initialize a variable to store the maximum time.
  2. Iterate over the positions of ants on the left and right sides of the plank.
  3. For each ant, calculate the time it takes to fall off the plank based on its position and direction of movement.
  4. Update the maximum time if the calculated time is greater.
- Why this approach comes to mind first: It directly simulates the problem statement and is easy to understand.

```cpp
class Solution {
public:
    int getLastMoment(int n, vector<int>& left, vector<int>& right) {
        int maxTime = 0;
        for (int pos : left) {
            maxTime = max(maxTime, pos);
        }
        for (int pos : right) {
            maxTime = max(maxTime, n - pos);
        }
        return maxTime;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m + k)$, where $m$ and $k$ are the sizes of the `left` and `right` vectors, respectively. This is because we iterate over each vector once.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum time.
> - **Why these complexities occur:** The time complexity is linear because we perform a single pass over the input data, and the space complexity is constant because we do not allocate any additional space that scales with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: The last moment before all ants fall off the plank is determined by the ant that takes the longest time to reach the edge of the plank.
- Detailed breakdown:
  1. For ants on the left side, the time it takes to fall off is equal to their position.
  2. For ants on the right side, the time it takes to fall off is equal to the length of the plank minus their position.
  3. The maximum of these times represents the last moment before all ants fall off the plank.
- Proof of optimality: This approach is optimal because it directly calculates the last moment based on the positions of the ants, without any unnecessary computations or simulations.
- Why further optimization is impossible: The problem requires considering each ant's position at least once to determine the last moment, making this approach the most efficient possible solution.

```cpp
class Solution {
public:
    int getLastMoment(int n, vector<int>& left, vector<int>& right) {
        int maxTime = 0;
        for (int pos : left) {
            maxTime = max(maxTime, pos);
        }
        for (int pos : right) {
            maxTime = max(maxTime, n - pos);
        }
        return maxTime;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m + k)$, where $m$ and $k$ are the sizes of the `left` and `right` vectors, respectively.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum time.
> - **Optimality proof:** This approach is optimal because it has a linear time complexity and only requires a single pass over the input data, making it the most efficient possible solution.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: Simulating the movement of ants, calculating the time it takes for each ant to fall off the plank, and determining the maximum time.
- Problem-solving patterns: Directly addressing the problem statement and considering the positions of ants on both sides of the plank.
- Optimization techniques: Eliminating unnecessary computations and simulations to achieve the most efficient solution.
- Similar problems to practice: Problems involving simulations, maximum/minimum calculations, and optimization.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly calculating the time it takes for ants to fall off the plank, failing to consider ants on both sides, or using inefficient algorithms.
- Edge cases to watch for: Ants at positions 0 or `n`, empty input vectors, or negative input values.
- Performance pitfalls: Using excessive memory or computations, or failing to optimize the solution for large input sizes.
- Testing considerations: Thoroughly testing the solution with various input scenarios, including edge cases and large input sizes.