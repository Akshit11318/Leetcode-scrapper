## Minimum Amount of Damage Dealt to Bob
**Problem Link:** https://leetcode.com/problems/minimum-amount-of-damage-dealt-to-bob/description

**Problem Statement:**
- Input format: A 2D array `damage` where each sub-array contains two elements representing the time and damage of a magical attack.
- Constraints: $1 \leq n \leq 10^5$, $1 \leq time_i \leq 10^5$, $1 \leq damage_i \leq 10^6$.
- Expected output format: The minimum amount of damage that can be dealt to Bob.
- Key requirements and edge cases to consider: The total number of attacks is $n$, and each attack can be cast at any time $t$ where $t \geq time_i$. We need to minimize the total damage dealt to Bob.
- Example test cases with explanations: 
    - `damage = [[2,10],[3,5],[4,8]]`, the minimum damage that can be dealt to Bob is $10 + 5 + 8 = 23$.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Try all possible combinations of attacks and calculate the total damage for each combination.
- Step-by-step breakdown of the solution:
    1. Generate all possible combinations of attacks.
    2. For each combination, calculate the total damage by summing up the damage of each attack.
    3. Keep track of the minimum total damage found so far.
- Why this approach comes to mind first: It is a straightforward approach that tries all possible solutions.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int minDamage(vector<vector<int>>& damage) {
    int n = damage.size();
    int minDamage = INT_MAX;
    
    // Generate all possible combinations of attacks
    for (int mask = 0; mask < (1 << n); mask++) {
        int totalDamage = 0;
        
        // Calculate the total damage for the current combination
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                totalDamage += damage[i][1];
            }
        }
        
        // Update the minimum total damage found so far
        minDamage = min(minDamage, totalDamage);
    }
    
    return minDamage;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the number of attacks. This is because we generate all possible combinations of attacks, which is $2^n$, and for each combination, we calculate the total damage, which takes $O(n)$ time.
> - **Space Complexity:** $O(1)$, which means the space required does not change with the size of the input, so it is constant. This is because we only use a constant amount of space to store the minimum total damage and the current combination.
> - **Why these complexities occur:** The time complexity is high because we try all possible combinations of attacks, which grows exponentially with the number of attacks. The space complexity is low because we only use a constant amount of space to store the minimum total damage and the current combination.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can use a greedy approach to solve this problem. We sort the attacks by their times and then iterate through the sorted attacks. For each attack, we check if it can be cast at the current time. If it can, we add its damage to the total damage.
- Detailed breakdown of the approach:
    1. Sort the attacks by their times.
    2. Initialize the total damage to 0 and the current time to 0.
    3. Iterate through the sorted attacks. For each attack, check if it can be cast at the current time. If it can, add its damage to the total damage and update the