## Maximum Points After Enemy Battles
**Problem Link:** https://leetcode.com/problems/maximum-points-after-enemy-battles/description

**Problem Statement:**
- Input: A 2D vector `points` where each sub-vector contains two integers representing the points that can be obtained if the player wins or loses a battle.
- Constraints: The input will contain at least one battle and each battle is represented by a sub-vector of length 2.
- Expected Output: The maximum points the player can obtain after all battles.
- Key Requirements:
  - The player can choose to win or lose each battle independently.
  - The goal is to maximize the total points obtained.
- Edge Cases:
  - If there is only one battle, the player should choose the action that gives the most points.
  - If all battles result in the same points whether the player wins or loses, the total points will be the same regardless of the player's actions.
- Example Test Cases:
  - `points = [[1,3],[3,6],[2,1],[2,4],[3,5],[3,2]]`
  - `points = [[2,2],[3,7],[2,5],[2,3]]`

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to try all possible combinations of winning and losing each battle.
- This involves generating all possible sequences of wins and losses for the battles and calculating the total points for each sequence.
- The sequence that results in the maximum points is the solution.

```cpp
#include <vector>
#include <algorithm>

int maxPoints(std::vector<std::vector<int>>& points) {
    int n = points.size();
    int maxPoints = 0;
    
    // Generate all possible sequences of wins and losses
    for (int mask = 0; mask < (1 << n); mask++) {
        int pointsForSequence = 0;
        
        // Calculate points for the current sequence
        for (int i = 0; i < n; i++) {
            if (mask & (1 << i)) {
                // If the ith bit is set, the player wins the ith battle
                pointsForSequence += points[i][0];
            } else {
                // If the ith bit is not set, the player loses the ith battle
                pointsForSequence += points[i][1];
            }
        }
        
        // Update the maximum points found so far
        maxPoints = std::max(maxPoints, pointsForSequence);
    }
    
    return maxPoints;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the number of battles. This is because we generate $2^n$ sequences and for each sequence, we calculate the points in $O(n)$ time.
> - **Space Complexity:** $O(1)$, as we use a constant amount of space to store the maximum points and the current sequence's points.
> - **Why these complexities occur:** The exponential time complexity comes from generating all possible sequences of wins and losses, which is $2^n$ for $n$ battles. The linear factor in the time complexity is due to calculating the points for each sequence.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is that the problem can be solved using dynamic programming.
- The idea is to maintain two variables: one for the maximum points obtained so far by winning the current battle and another for the maximum points obtained so far by losing the current battle.
- We update these variables iteratively for each battle, considering the maximum points that can be obtained by winning or losing the previous battle.

```cpp
#include <vector>
#include <algorithm>

int maxPoints(std::vector<std::vector<int>>& points) {
    int n = points.size();
    std::vector<int> win(n), lose(n);
    
    // Initialize the first battle's points
    win[0] = points[0][0];
    lose[0] = points[0][1];
    
    // Calculate the maximum points for each battle
    for (int i = 1; i < n; i++) {
        win[i] = std::max(win[i-1], lose[i-1]) + points[i][0];
        lose[i] = std::max(win[i-1], lose[i-1]) + points[i][1];
    }
    
    // The maximum points are the maximum of the points obtained by winning or losing the last battle
    return std::max(win[n-1], lose[n-1]);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of battles. This is because we make a single pass through the battles.
> - **Space Complexity:** $O(n)$, as we use two arrays of size $n$ to store the maximum points for winning and losing each battle.
> - **Optimality proof:** This approach is optimal because it considers all possible sequences of wins and losses implicitly through the dynamic programming formulation, but does so in linear time by avoiding the explicit generation of all sequences.

---

### Final Notes

**Learning Points:**
- Dynamic programming can be used to solve problems that involve making a sequence of choices to maximize or minimize some objective.
- It's essential to identify the key variables that need to be tracked and updated iteratively.
- The time and space complexities of dynamic programming solutions can be significantly better than brute force approaches.

**Mistakes to Avoid:**
- Failing to consider all possible sequences of choices.
- Not updating the key variables correctly in the dynamic programming formulation.
- Not optimizing the space usage by only keeping the necessary information from previous iterations.