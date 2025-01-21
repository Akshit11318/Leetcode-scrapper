## Maximum Total Beauty of the Gardens
**Problem Link:** https://leetcode.com/problems/maximum-total-beauty-of-the-gardens/description

**Problem Statement:**
- Input format and constraints: Given an array of integers `flowers` and an integer `newFlowers`, and `maxPollen`, `minPollen`, and `totalPollen`, find the maximum total beauty of the gardens after planting `newFlowers` flowers.
- Expected output format: The maximum total beauty.
- Key requirements and edge cases to consider: The beauty of a garden is determined by the amount of pollen it has. The total beauty of all gardens is the sum of the beauty of each garden.
- Example test cases with explanations: 
    - For example, if `flowers = [1, 2, 3, 4]`, `newFlowers = 2`, `maxPollen = 5`, `minPollen = 1`, `totalPollen = 10`, the maximum total beauty is `10`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of planting `newFlowers` flowers in the gardens.
- Step-by-step breakdown of the solution:
    1. Generate all possible combinations of planting `newFlowers` flowers in the gardens.
    2. For each combination, calculate the total beauty of the gardens.
    3. Keep track of the maximum total beauty found so far.
- Why this approach comes to mind first: It is a straightforward approach that tries all possible solutions.

```cpp
class Solution {
public:
    int maximumBeauty(vector<int>& flowers, int newFlowers, int maxPollen, int minPollen, int totalPollen) {
        int n = flowers.size();
        int maxBeauty = 0;
        // Generate all possible combinations of planting newFlowers flowers in the gardens
        for (int mask = 0; mask < (1 << n); mask++) {
            int remainingPollen = totalPollen;
            int beauty = 0;
            vector<int> pollen = flowers;
            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) != 0) {
                    // Plant a flower in the current garden
                    pollen[i]++;
                    remainingPollen--;
                }
            }
            // Calculate the beauty of each garden
            for (int i = 0; i < n; i++) {
                beauty += min(pollen[i], maxPollen);
            }
            // Update the maximum total beauty
            maxBeauty = max(maxBeauty, beauty);
            if (remainingPollen == 0) break;
        }
        return maxBeauty;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the number of gardens.
> - **Space Complexity:** $O(n)$, where $n$ is the number of gardens.
> - **Why these complexities occur:** The brute force approach generates all possible combinations of planting `newFlowers` flowers in the gardens, which has a time complexity of $O(2^n)$. For each combination, it calculates the total beauty of the gardens, which has a time complexity of $O(n)$.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The problem can be solved using a greedy approach. We should plant flowers in the gardens with the least pollen first.
- Detailed breakdown of the approach:
    1. Sort the gardens by the amount of pollen they have.
    2. Plant flowers in the gardens with the least pollen first.
    3. For each garden, calculate the maximum beauty it can have by planting flowers.
    4. Update the total beauty.
- Proof of optimality: The greedy approach is optimal because it always plants flowers in the gardens with the least pollen, which maximizes the total beauty.

```cpp
class Solution {
public:
    int maximumBeauty(vector<int>& flowers, int newFlowers, int maxPollen, int minPollen, int totalPollen) {
        int n = flowers.size();
        sort(flowers.begin(), flowers.end());
        int totalBeauty = 0;
        for (int i = 0; i < n; i++) {
            int beauty = min(flowers[i] + newFlowers, maxPollen);
            totalBeauty += beauty;
            newFlowers -= max(0, beauty - flowers[i]);
        }
        return totalBeauty;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of gardens.
> - **Space Complexity:** $O(n)$, where $n$ is the number of gardens.
> - **Optimality proof:** The greedy approach is optimal because it always plants flowers in the gardens with the least pollen, which maximizes the total beauty.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Greedy algorithm, sorting.
- Problem-solving patterns identified: The problem can be solved using a greedy approach.
- Optimization techniques learned: Sorting the gardens by the amount of pollen they have.
- Similar problems to practice: Other problems that can be solved using a greedy approach.

**Mistakes to Avoid:**
- Common implementation errors: Not sorting the gardens by the amount of pollen they have.
- Edge cases to watch for: The case where the total pollen is less than the number of gardens.
- Performance pitfalls: Using a brute force approach instead of a greedy approach.
- Testing considerations: Test the solution with different inputs, including edge cases.