## Minimum White Tiles After Covering With Carpets

**Problem Link:** https://leetcode.com/problems/minimum-white-tiles-after-covering-with-carpets/description

**Problem Statement:**
- Input format and constraints: The problem takes a string `floor`, representing the floor as a string of '0's (white tiles) and '1's (black tiles), and an array of integers `carpet`, where `carpet[i]` is the length of the `i-th` carpet.
- Expected output format: The minimum number of white tiles after covering with carpets.
- Key requirements and edge cases to consider: The carpets can only cover white tiles, and we need to find the minimum number of white tiles that will remain after covering with the carpets.
- Example test cases with explanations:
  - Input: `floor = "10100101"`, `carpet = [1, 2]`
  - Output: `2`
  - Explanation: We can cover the white tiles at indices 1, 3, 5, and 7 with the two carpets of length 1 and 2.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of covering white tiles with carpets.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of covering white tiles with carpets.
  2. For each combination, calculate the number of white tiles that are not covered.
  3. Return the minimum number of white tiles that are not covered among all combinations.
- Why this approach comes to mind first: It's a straightforward approach that tries all possible solutions.

```cpp
class Solution {
public:
    int minimumWhiteTiles(string floor, vector<int>& carpet) {
        int n = floor.size();
        int m = carpet.size();
        int res = INT_MAX;
        
        // Generate all possible combinations of covering white tiles with carpets
        for (int mask = 0; mask < (1 << m); mask++) {
            int count = 0;
            vector<bool> covered(n, false);
            
            // Calculate the number of white tiles that are not covered
            for (int i = 0; i < m; i++) {
                if ((mask & (1 << i)) != 0) {
                    for (int j = 0; j < n; j++) {
                        if (!covered[j] && floor[j] == '0') {
                            for (int k = 0; k < carpet[i]; k++) {
                                if (j + k < n) {
                                    covered[j + k] = true;
                                }
                            }
                            break;
                        }
                    }
                }
            }
            
            for (int i = 0; i < n; i++) {
                if (floor[i] == '0' && !covered[i]) {
                    count++;
                }
            }
            
            res = min(res, count);
        }
        
        return res;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^m \cdot n \cdot m \cdot c)$, where $m$ is the number of carpets, $n$ is the length of the floor, and $c$ is the maximum length of a carpet.
> - **Space Complexity:** $O(n)$, for the `covered` array.
> - **Why these complexities occur:** The time complexity occurs because we generate all possible combinations of covering white tiles with carpets, and for each combination, we calculate the number of white tiles that are not covered. The space complexity occurs because we need to store the `covered` array.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a sliding window approach to cover the white tiles.
- Detailed breakdown of the approach:
  1. Sort the carpets in descending order of their lengths.
  2. Initialize a variable `res` to store the minimum number of white tiles that will remain after covering with the carpets.
  3. Initialize a variable `i` to store the current index in the `floor` string.
  4. Iterate over the `floor` string. For each white tile, try to cover it with the largest carpet that can cover it.
  5. If a carpet can cover the white tile, increment `i` by the length of the carpet and decrement the count of white tiles that can be covered by the carpet.
  6. If a carpet cannot cover the white tile, increment `res` by 1 and increment `i` by 1.
- Proof of optimality: This approach is optimal because it always tries to cover the white tiles with the largest carpet possible, which minimizes the number of white tiles that will remain after covering with the carpets.

```cpp
class Solution {
public:
    int minimumWhiteTiles(string floor, vector<int>& carpet) {
        int n = floor.size();
        int m = carpet.size();
        int res = 0;
        sort(carpet.rbegin(), carpet.rend());
        
        for (int i = 0; i < n; i++) {
            if (floor[i] == '0') {
                bool covered = false;
                for (int j = 0; j < m; j++) {
                    if (carpet[j] > 0) {
                        carpet[j]--;
                        covered = true;
                        break;
                    }
                }
                if (!covered) {
                    res++;
                }
            }
        }
        
        return res;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the length of the floor and $m$ is the number of carpets.
> - **Space Complexity:** $O(m)$, for the `carpet` array.
> - **Optimality proof:** This approach is optimal because it always tries to cover the white tiles with the largest carpet possible, which minimizes the number of white tiles that will remain after covering with the carpets.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sliding window approach, sorting, and greedy algorithm.
- Problem-solving patterns identified: Trying to cover the white tiles with the largest carpet possible.
- Optimization techniques learned: Using a sliding window approach to minimize the number of white tiles that will remain after covering with the carpets.
- Similar problems to practice: Problems that involve covering or painting objects with different sizes or colors.

**Mistakes to Avoid:**
- Common implementation errors: Not sorting the carpets in descending order of their lengths.
- Edge cases to watch for: The case where the number of carpets is 0, or the case where the length of the floor is 0.
- Performance pitfalls: Using a brute force approach that tries all possible combinations of covering white tiles with carpets.
- Testing considerations: Testing the solution with different inputs, such as different lengths of the floor and different numbers of carpets.