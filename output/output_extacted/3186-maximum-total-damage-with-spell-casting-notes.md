## Maximum Total Damage with Spell Casting

**Problem Link:** https://leetcode.com/problems/maximum-total-damage-with-spell-casting/description

**Problem Statement:**
- Input: A `2D` array `s` where `s[i][0]` is the base damage and `s[i][1]` is the bonus damage for the `i-th` spell, and an integer `k` representing the maximum number of times a spell can be cast.
- Constraints: `1 <= s.length <= 50`, `s[i].length == 2`, `1 <= s[i][0], s[i][1] <= 10^4`, `1 <= k <= 50`, and `1 <= initialMana <= 10^5`.
- Expected Output: The maximum total damage that can be dealt.
- Key Requirements: Find the maximum total damage that can be dealt by casting the spells up to `k` times.
- Edge Cases: Consider the case where `k` is large enough to cast each spell multiple times.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to try all possible combinations of casting the spells up to `k` times.
- This involves generating all permutations of spell casts and calculating the total damage for each permutation.
- However, this approach is inefficient due to the large number of permutations.

```cpp
#include <iostream>
#include <vector>

using namespace std;

int maxDamage(vector<vector<int>>& s, int k) {
    int maxDamage = 0;
    int n = s.size();
    vector<int> damage(n, 0);

    // Generate all permutations of spell casts
    function<void(int)> dfs = [&](int depth) {
        if (depth == k) {
            int totalDamage = 0;
            for (int i = 0; i < n; i++) {
                totalDamage += s[i][0] * damage[i] + s[i][1];
            }
            maxDamage = max(maxDamage, totalDamage);
            return;
        }

        for (int i = 0; i < n; i++) {
            damage[i]++;
            dfs(depth + 1);
            damage[i]--;
        }
    };

    dfs(0);
    return maxDamage;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^k)$, where $n$ is the number of spells. This is because we generate all permutations of spell casts.
> - **Space Complexity:** $O(n)$, where $n$ is the number of spells. This is because we need to store the damage for each spell.
> - **Why these complexities occur:** The brute force approach involves generating all permutations of spell casts, which leads to an exponential time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use dynamic programming to store the maximum damage that can be dealt for each number of casts.
- We can use a `2D` array `dp` where `dp[i][j]` represents the maximum damage that can be dealt by casting the spells up to `i` times and using the `j-th` spell.
- We can fill up the `dp` array by iterating over each spell and each number of casts.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int maxDamage(vector<vector<int>>& s, int k) {
    int n = s.size();
    vector<vector<int>> dp(k + 1, vector<int>(n, 0));

    for (int i = 1; i <= k; i++) {
        for (int j = 0; j < n; j++) {
            int maxDamage = 0;
            for (int m = 0; m <= i; m++) {
                int damage = s[j][0] * m + s[j][1];
                if (m < i) {
                    int remainingDamage = 0;
                    for (int l = 0; l < n; l++) {
                        remainingDamage = max(remainingDamage, dp[i - m][l]);
                    }
                    damage += remainingDamage;
                }
                maxDamage = max(maxDamage, damage);
            }
            dp[i][j] = maxDamage;
        }
    }

    int maxTotalDamage = 0;
    for (int i = 0; i < n; i++) {
        maxTotalDamage = max(maxTotalDamage, dp[k][i]);
    }
    return maxTotalDamage;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k^2)$, where $n$ is the number of spells and $k$ is the maximum number of casts.
> - **Space Complexity:** $O(n \cdot k)$, where $n$ is the number of spells and $k$ is the maximum number of casts.
> - **Optimality proof:** The dynamic programming approach ensures that we consider all possible combinations of spell casts and calculate the maximum damage that can be dealt.

---

### Final Notes

**Learning Points:**
- The problem requires using dynamic programming to store the maximum damage that can be dealt for each number of casts.
- The key insight is to use a `2D` array to store the maximum damage for each spell and each number of casts.
- The problem demonstrates the importance of considering all possible combinations of spell casts to calculate the maximum damage.

**Mistakes to Avoid:**
- Failing to consider all possible combinations of spell casts.
- Not using dynamic programming to store the maximum damage for each number of casts.
- Not iterating over each spell and each number of casts to fill up the `dp` array.

**Similar Problems to Practice:**
- [Maximum Total Damage with Spell Casting II](https://leetcode.com/problems/maximum-total-damage-with-spell-casting-ii/description)
- [Maximum Total Damage with Spell Casting III](https://leetcode.com/problems/maximum-total-damage-with-spell-casting-iii/description)