## Minimum Number of Taps to Open to Water a Garden

**Problem Link:** https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/description

**Problem Statement:**
- Input: An integer array `ranges` of size `n`, where `ranges[i]` represents the garden that the `i-th` tap can water.
- Constraints: `1 <= n <= 10^5`, `0 <= ranges[i] <= 5 * 10^4`.
- Expected output: The minimum number of taps that need to be opened to water the entire garden.
- Key requirements: The garden can be considered as a range from 0 to the maximum end of all ranges in `ranges`.
- Edge cases: If it's impossible to water the entire garden, return `-1`.
- Example test cases:
  - Input: `ranges = [3,4,1,1,0,0]`
    - Output: `1`
    - Explanation: Tap at index `0` can water the entire garden.
  - Input: `ranges = [1,2,3,4]`
    - Output: `2`
    - Explanation: Taps at indices `0` and `1` can water the entire garden.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of taps to see if they can water the entire garden.
- Step-by-step breakdown:
  1. Generate all possible subsets of taps.
  2. For each subset, check if the union of the ranges of the taps in the subset covers the entire garden.
  3. If a subset is found that covers the entire garden, update the minimum number of taps.
- Why this approach comes to mind first: It's a straightforward way to solve the problem, but it's inefficient due to the large number of subsets.

```cpp
class Solution {
public:
    int minTaps(int n, vector<int>& ranges) {
        int maxRange = 0;
        for (int range : ranges) {
            maxRange = max(maxRange, range);
        }
        int gardenSize = maxRange + 1;
        
        vector<int> canReach(gardenSize, false);
        for (int i = 0; i < n; i++) {
            int start = max(0, i - ranges[i]);
            int end = min(gardenSize, i + ranges[i] + 1);
            for (int j = start; j < end; j++) {
                canReach[j] = true;
            }
        }
        
        if (!canReach.back()) {
            return -1;
        }
        
        vector<vector<int>> subsets;
        for (int i = 0; i < (1 << n); i++) {
            vector<int> subset;
            for (int j = 0; j < n; j++) {
                if (i & (1 << j)) {
                    subset.push_back(j);
                }
            }
            subsets.push_back(subset);
        }
        
        int minTaps = INT_MAX;
        for (vector<int> subset : subsets) {
            vector<int> canReachSubset(gardenSize, false);
            for (int i : subset) {
                int start = max(0, i - ranges[i]);
                int end = min(gardenSize, i + ranges[i] + 1);
                for (int j = start; j < end; j++) {
                    canReachSubset[j] = true;
                }
            }
            if (canReachSubset.back()) {
                minTaps = min(minTaps, subset.size());
            }
        }
        
        return minTaps == INT_MAX ? -1 : minTaps;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n \cdot maxRange)$, where $n$ is the number of taps and $maxRange$ is the maximum range of a tap.
> - **Space Complexity:** $O(2^n \cdot n + n \cdot maxRange)$, for storing all subsets and the `canReach` array.
> - **Why these complexities occur:** The brute force approach generates all possible subsets of taps, which results in exponential time complexity. The space complexity is also high due to storing all subsets and the `canReach` array.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Use a greedy approach to find the minimum number of taps. At each step, choose the tap that can cover the most new area.
- Detailed breakdown:
  1. Initialize a `canReach` array to keep track of the area that can be covered by the taps.
  2. Initialize a `taps` variable to store the minimum number of taps.
  3. Iterate over the garden, and for each position, check if it can be covered by any tap.
  4. If a position cannot be covered, find the tap that can cover the most new area and add it to the `taps` count.
- Proof of optimality: The greedy approach ensures that the minimum number of taps is used to cover the entire garden.

```cpp
class Solution {
public:
    int minTaps(int n, vector<int>& ranges) {
        vector<int> canReach(n + 1, 0);
        for (int i = 0; i < n; i++) {
            int start = max(0, i - ranges[i]);
            int end = min(n, i + ranges[i] + 1);
            canReach[start] = max(canReach[start], end);
        }
        
        int taps = 0;
        int curEnd = 0;
        int farEnd = 0;
        for (int i = 0; i < n; i++) {
            farEnd = max(farEnd, canReach[i]);
            if (i == curEnd) {
                if (farEnd <= i) {
                    return -1;
                }
                curEnd = farEnd;
                taps++;
            }
        }
        
        return taps;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot maxRange)$, where $n$ is the number of taps and $maxRange$ is the maximum range of a tap.
> - **Space Complexity:** $O(n)$, for storing the `canReach` array.
> - **Optimality proof:** The greedy approach ensures that the minimum number of taps is used to cover the entire garden. The time complexity is linear with respect to the number of taps, and the space complexity is also linear.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: Greedy approach, array manipulation.
- Problem-solving patterns: Using a `canReach` array to keep track of the area that can be covered by the taps.
- Optimization techniques: Using a greedy approach to find the minimum number of taps.
- Similar problems to practice: [Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/), [Minimum Number of Taps to Open to Water a Garden](https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/).

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the `canReach` array correctly, not updating the `taps` count correctly.
- Edge cases: Not checking if the garden can be covered by any tap, not handling the case where the garden cannot be covered.
- Performance pitfalls: Using a brute force approach, not optimizing the solution using a greedy approach.
- Testing considerations: Testing the solution with different inputs, including edge cases and large inputs.