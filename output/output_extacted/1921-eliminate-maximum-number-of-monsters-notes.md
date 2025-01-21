## Eliminate Maximum Number of Monsters
**Problem Link:** https://leetcode.com/problems/eliminate-maximum-number-of-monsters/description

**Problem Statement:**
- Input format: An array of integers `monsters` where `monsters[i]` represents the time it takes for the `i-th` monster to reach the city, and an integer `a` representing the time it takes to eliminate a monster.
- Expected output format: The maximum number of monsters that can be eliminated.
- Key requirements and edge cases to consider:
  - Monsters are eliminated one at a time.
  - Eliminating a monster takes `a` time units.
  - If a monster reaches the city before it can be eliminated, it cannot be eliminated.
- Example test cases with explanations:
  - `monsters = [1, 3, 2], a = 2` should return `2` because we can eliminate the first and third monsters.
  - `monsters = [1, 1], a = 1` should return `1` because we can only eliminate one monster.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible orders of eliminating monsters and see which order eliminates the most monsters.
- Step-by-step breakdown of the solution:
  1. Generate all permutations of the monsters.
  2. For each permutation, try to eliminate the monsters one by one.
  3. If a monster reaches the city before it can be eliminated, stop trying to eliminate monsters in this permutation.
  4. Keep track of the maximum number of monsters eliminated in any permutation.
- Why this approach comes to mind first: It is a straightforward way to solve the problem, but it is not efficient for large inputs.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int eliminateMaximum(std::vector<int>& monsters, int a) {
    int n = monsters.size();
    int maxEliminated = 0;
    std::vector<int> permutation(n);
    for (int i = 0; i < n; i++) {
        permutation[i] = i;
    }
    do {
        int eliminated = 0;
        int currentTime = 0;
        for (int i = 0; i < n; i++) {
            int monsterIndex = permutation[i];
            if (currentTime + a <= monsters[monsterIndex]) {
                eliminated++;
                currentTime += a;
            } else {
                break;
            }
        }
        maxEliminated = std::max(maxEliminated, eliminated);
    } while (std::next_permutation(permutation.begin(), permutation.end()));
    return maxEliminated;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n! \cdot n)$ where $n$ is the number of monsters, because we generate all permutations of the monsters and try to eliminate them one by one in each permutation.
> - **Space Complexity:** $O(n)$ because we need to store the permutation of the monsters.
> - **Why these complexities occur:** The time complexity is high because we try all possible orders of eliminating monsters, and the space complexity is low because we only need to store the current permutation of the monsters.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can sort the monsters by the time it takes for them to reach the city, and then try to eliminate them one by one.
- Detailed breakdown of the approach:
  1. Sort the monsters by the time it takes for them to reach the city.
  2. Try to eliminate the monsters one by one in the sorted order.
  3. If a monster reaches the city before it can be eliminated, stop trying to eliminate monsters.
- Proof of optimality: This approach is optimal because we try to eliminate the monsters in the order that they reach the city, which maximizes the number of monsters eliminated.
- Why further optimization is impossible: We have already optimized the approach by trying to eliminate the monsters in the order that they reach the city.

```cpp
int eliminateMaximum(std::vector<int>& monsters, int a) {
    int n = monsters.size();
    std::sort(monsters.begin(), monsters.end());
    int eliminated = 0;
    int currentTime = 0;
    for (int i = 0; i < n; i++) {
        if (currentTime + a <= monsters[i]) {
            eliminated++;
            currentTime += a;
        } else {
            break;
        }
    }
    return eliminated;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ where $n$ is the number of monsters, because we sort the monsters by the time it takes for them to reach the city.
> - **Space Complexity:** $O(1)$ because we only need to use a constant amount of space to store the current time and the number of eliminated monsters.
> - **Optimality proof:** This approach is optimal because we try to eliminate the monsters in the order that they reach the city, which maximizes the number of monsters eliminated.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting, greedy algorithms.
- Problem-solving patterns identified: Trying to eliminate monsters in the order that they reach the city maximizes the number of monsters eliminated.
- Optimization techniques learned: Sorting the monsters by the time it takes for them to reach the city.
- Similar problems to practice: Other problems that involve trying to maximize or minimize something by trying different orders or combinations.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if a monster reaches the city before it can be eliminated.
- Edge cases to watch for: Monsters reaching the city at the same time.
- Performance pitfalls: Trying all possible orders of eliminating monsters, which has a high time complexity.
- Testing considerations: Test the function with different inputs, including edge cases and large inputs.