## Building Boxes
**Problem Link:** https://leetcode.com/problems/building-boxes/description

**Problem Statement:**
- Input format and constraints: The function takes an integer `boxTypes` as input, where each element `boxTypes[i]` is an array of two integers, `numberOfBoxes` and `boxSize`. `numberOfBoxes` is the number of boxes of size `boxSize`.
- Expected output format: The function returns the maximum number of units that can be put in the boxes.
- Key requirements and edge cases to consider: The total number of units that can be put in a box is the number of boxes multiplied by the size of each box.
- Example test cases with explanations: For example, if `boxTypes = [[5,1],[2,5],[4,6],[3,7],[4,8]]`, the maximum number of units is `23`, which is achieved by taking `5` boxes of size `1`, `2` boxes of size `5`, `4` boxes of size `6`, `3` boxes of size `7`, and `4` boxes of size `8`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves iterating over each possible combination of boxes and calculating the total number of units for each combination.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of boxes.
  2. For each combination, calculate the total number of units by multiplying the number of boxes by the size of each box and summing these products.
  3. Keep track of the maximum total number of units seen so far.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it is not efficient for large inputs because it generates all possible combinations of boxes.

```cpp
class Solution {
public:
    int maximumUnits(vector<vector<int>>& boxTypes, int truckSize) {
        int maxUnits = 0;
        for (int mask = 0; mask < (1 << boxTypes.size()); mask++) {
            int currentUnits = 0;
            int currentSize = 0;
            for (int i = 0; i < boxTypes.size(); i++) {
                if ((mask & (1 << i)) != 0) {
                    currentSize += boxTypes[i][0];
                    currentUnits += boxTypes[i][0] * boxTypes[i][1];
                }
            }
            if (currentSize <= truckSize) {
                maxUnits = max(maxUnits, currentUnits);
            }
        }
        return maxUnits;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the number of box types. This is because we generate all possible combinations of boxes and iterate over each box type for each combination.
> - **Space Complexity:** $O(1)$, which means the space required does not change with the size of the input, so it is constant. This is because we only use a constant amount of space to store the current combination and the maximum units seen so far.
> - **Why these complexities occur:** The time complexity is exponential because we generate all possible combinations of boxes, and the space complexity is constant because we only use a constant amount of space to store the current combination and the maximum units seen so far.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The key insight is to sort the box types in descending order of their sizes and then fill the truck with the largest boxes first.
- Detailed breakdown of the approach:
  1. Sort the box types in descending order of their sizes.
  2. Initialize the maximum units and the current size of the truck.
  3. Iterate over the sorted box types and fill the truck with the largest boxes first.
  4. For each box type, calculate the number of boxes that can be filled and update the maximum units and the current size of the truck.
- Proof of optimality: This approach is optimal because it fills the truck with the largest boxes first, which maximizes the total number of units.

```cpp
class Solution {
public:
    int maximumUnits(vector<vector<int>>& boxTypes, int truckSize) {
        sort(boxTypes.begin(), boxTypes.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[1] > b[1];
        });
        int maxUnits = 0;
        for (const auto& boxType : boxTypes) {
            int boxes = min(truckSize, boxType[0]);
            maxUnits += boxes * boxType[1];
            truckSize -= boxes;
            if (truckSize == 0) {
                break;
            }
        }
        return maxUnits;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of box types. This is because we sort the box types in descending order of their sizes.
> - **Space Complexity:** $O(1)$, which means the space required does not change with the size of the input, so it is constant. This is because we only use a constant amount of space to store the maximum units and the current size of the truck.
> - **Optimality proof:** This approach is optimal because it fills the truck with the largest boxes first, which maximizes the total number of units.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting, greedy algorithm.
- Problem-solving patterns identified: The problem can be solved by sorting the box types in descending order of their sizes and then filling the truck with the largest boxes first.
- Optimization techniques learned: The optimal approach is to fill the truck with the largest boxes first, which maximizes the total number of units.
- Similar problems to practice: Other problems that involve sorting and greedy algorithms.

**Mistakes to Avoid:**
- Common implementation errors: Not sorting the box types in descending order of their sizes, not filling the truck with the largest boxes first.
- Edge cases to watch for: The case where the truck size is 0, the case where there are no box types.
- Performance pitfalls: Using a brute force approach, which has an exponential time complexity.
- Testing considerations: Test the function with different inputs, including edge cases.