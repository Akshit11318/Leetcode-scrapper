## The Number of Full Rounds You Have Played

**Problem Link:** https://leetcode.com/problems/the-number-of-full-rounds-you-have-played/description

**Problem Statement:**
- Input format: Two integers `initialEnergy` and `currentEnergy` representing the initial energy level and the current energy level of the player.
- Constraints: `1 <= initialEnergy, currentEnergy <= 10^6`.
- Expected output format: The number of full rounds the player has played.
- Key requirements and edge cases to consider:
  - A full round is considered when the player's energy level decreases by at least `initialEnergy`.
  - The player cannot play a fraction of a round.

**Example Test Cases:**
- `initialEnergy = 100, currentEnergy = 100`, expected output: `0`.
- `initialEnergy = 100, currentEnergy = 50`, expected output: `0`.
- `initialEnergy = 100, currentEnergy = 0`, expected output: `1`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves calculating the difference in energy levels and checking how many times the initial energy level can fit into this difference.
- This approach comes to mind first because it directly addresses the requirement of finding full rounds played.

```cpp
class Solution {
public:
    int numberOfRounds(int initialEnergy, int currentEnergy) {
        int diff = currentEnergy - initialEnergy;
        if (diff >= 0) return 0; // If energy increased or remained the same
        diff = abs(diff);
        return diff / initialEnergy;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, as we perform a constant number of operations regardless of the input size.
> - **Space Complexity:** $O(1)$, since we use a constant amount of space to store the variables.
> - **Why these complexities occur:** The operations are basic arithmetic and do not depend on the input size.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to realize that we only need to calculate the difference in energy levels and then divide by the initial energy to find the number of full rounds.
- This approach is optimal because it uses the least number of operations necessary to solve the problem.
- Further optimization is impossible because we must perform at least one subtraction and one division to calculate the number of full rounds.

```cpp
class Solution {
public:
    int numberOfRounds(int initialEnergy, int currentEnergy) {
        int diff = currentEnergy - initialEnergy;
        if (diff >= 0) return 0; // If energy increased or remained the same
        diff = abs(diff);
        return diff / initialEnergy;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, as we perform a constant number of operations regardless of the input size.
> - **Space Complexity:** $O(1)$, since we use a constant amount of space to store the variables.
> - **Optimality proof:** This is the best possible complexity because we must perform at least the operations described, and no further simplification is possible without changing the problem's requirements.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: basic arithmetic operations and division.
- Problem-solving patterns identified: calculating differences and using division to find the number of full rounds.
- Optimization techniques learned: minimizing the number of operations necessary to solve the problem.
- Similar problems to practice: other problems involving basic arithmetic operations and division.

**Mistakes to Avoid:**
- Common implementation errors: forgetting to handle the case where energy increases or remains the same.
- Edge cases to watch for: energy levels that are equal or where the difference is not a multiple of the initial energy.
- Performance pitfalls: using unnecessary loops or recursive functions.
- Testing considerations: testing with different input values to ensure correctness.