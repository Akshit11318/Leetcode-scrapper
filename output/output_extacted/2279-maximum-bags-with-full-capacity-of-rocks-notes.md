## Maximum Bags With Full Capacity of Rocks
**Problem Link:** https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/description

**Problem Statement:**
- Input format and constraints: The function takes two parameters: `capacity` and `rocks`, where `capacity` is an array of integers representing the capacity of each bag, and `rocks` is an array of integers representing the number of rocks in each bag.
- Expected output format: The function should return the maximum number of bags that can be filled with rocks.
- Key requirements and edge cases to consider: The number of rocks in each bag should not exceed its capacity.
- Example test cases with explanations:
  - Example 1: `capacity = [10,20,30,40,50], rocks = [1,2,3,4,5], additionalRocks = 100`, the function should return `3` because we can fill the first three bags with rocks.
  - Example 2: `capacity = [10,20,30,40,50], rocks = [1,2,3,4,5], additionalRocks = 0`, the function should return `0` because we cannot fill any bags with rocks.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: The brute force approach involves trying all possible combinations of filling the bags with rocks.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of filling the bags with rocks.
  2. For each combination, check if the number of rocks in each bag does not exceed its capacity.
  3. If a combination is valid, calculate the number of bags that can be filled with rocks.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it is not efficient for large inputs.

```cpp
class Solution {
public:
    int maximumBags(vector<int>& capacity, vector<int>& rocks, int additionalRocks) {
        int n = capacity.size();
        int maxBags = 0;
        for (int i = 0; i < (1 << n); i++) {
            int currentBags = 0;
            int currentRocks = 0;
            for (int j = 0; j < n; j++) {
                if ((i & (1 << j)) != 0) {
                    currentBags++;
                    currentRocks += capacity[j] - rocks[j];
                }
            }
            if (currentRocks <= additionalRocks) {
                maxBags = max(maxBags, currentBags);
            }
        }
        return maxBags;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the number of bags. This is because we generate all possible combinations of filling the bags with rocks, and for each combination, we check if it is valid.
> - **Space Complexity:** $O(1)$, which means the space required does not grow with the size of the input.
> - **Why these complexities occur:** The time complexity occurs because we use a nested loop to generate all possible combinations of filling the bags with rocks. The space complexity occurs because we only use a constant amount of space to store the variables.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can sort the bags based on the remaining capacity and fill the bags with the smallest remaining capacity first.
- Detailed breakdown of the approach:
  1. Calculate the remaining capacity of each bag by subtracting the number of rocks from the capacity.
  2. Sort the bags based on the remaining capacity.
  3. Fill the bags with the smallest remaining capacity first using the additional rocks.
- Proof of optimality: This approach is optimal because it ensures that we fill the maximum number of bags with the smallest remaining capacity.

```cpp
class Solution {
public:
    int maximumBags(vector<int>& capacity, vector<int>& rocks, int additionalRocks) {
        int n = capacity.size();
        vector<int> remainingCapacity(n);
        for (int i = 0; i < n; i++) {
            remainingCapacity[i] = capacity[i] - rocks[i];
        }
        vector<pair<int, int>> bags(n);
        for (int i = 0; i < n; i++) {
            bags[i] = {remainingCapacity[i], i};
        }
        sort(bags.begin(), bags.end());
        int maxBags = 0;
        for (int i = 0; i < n; i++) {
            if (bags[i].first <= additionalRocks) {
                maxBags++;
                additionalRocks -= bags[i].first;
            } else {
                break;
            }
        }
        return maxBags;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of bags. This is because we sort the bags based on the remaining capacity.
> - **Space Complexity:** $O(n)$, which means the space required grows linearly with the size of the input.
> - **Optimality proof:** This approach is optimal because it ensures that we fill the maximum number of bags with the smallest remaining capacity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting, greedy algorithm.
- Problem-solving patterns identified: Filling the bags with the smallest remaining capacity first.
- Optimization techniques learned: Using a greedy approach to fill the bags.
- Similar problems to practice: Other problems that involve sorting and greedy algorithms.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if the number of rocks in each bag does not exceed its capacity.
- Edge cases to watch for: The number of rocks in each bag should not exceed its capacity.
- Performance pitfalls: Using a brute force approach for large inputs.
- Testing considerations: Testing the function with different inputs and edge cases.