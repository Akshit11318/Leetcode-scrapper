## Maximum Units on a Truck
**Problem Link:** https://leetcode.com/problems/maximum-units-on-a-truck/description

**Problem Statement:**
- Input format and constraints: You are given a 2D array `boxTypes`, where `boxTypes[i] = [numberOfBoxes, unitsPerBox]`, representing the number of boxes of a specific type and the number of units in each box of that type. Additionally, you are given an integer `truckSize`, representing the maximum number of boxes that can be put on a truck. The goal is to find the maximum number of units that can be put on the truck.
- Expected output format: The function should return an integer representing the maximum number of units that can be put on the truck.
- Key requirements and edge cases to consider:
  - The number of boxes of each type is non-negative.
  - The number of units in each box is non-negative.
  - The truck size is non-negative.
  - If the truck size is 0, the function should return 0.
- Example test cases with explanations:
  - `boxTypes = [[5,10],[2,5],[4,7],[3,9]]`, `truckSize = 10`: The function should return `91`.
  - `boxTypes = [[1,3],[2,2],[3,1]]`, `truckSize = 4`: The function should return `8`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves trying all possible combinations of boxes to find the maximum number of units that can be put on the truck.
- Step-by-step breakdown of the solution:
  1. Sort the boxes in descending order based on the number of units per box.
  2. Initialize a variable `maxUnits` to 0.
  3. Iterate over each box type.
  4. For each box type, calculate the number of boxes that can be put on the truck without exceeding the truck size.
  5. Update `maxUnits` by adding the number of units in the current box type multiplied by the number of boxes that can be put on the truck.
- Why this approach comes to mind first: This approach is straightforward and involves trying all possible combinations of boxes to find the maximum number of units.

```cpp
int maximumUnits(vector<vector<int>>& boxTypes, int truckSize) {
    // Sort the boxes in descending order based on the number of units per box
    sort(boxTypes.begin(), boxTypes.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[1] > b[1];
    });
    
    int maxUnits = 0;
    for (const auto& box : boxTypes) {
        int numberOfBoxes = min(box[0], truckSize);
        maxUnits += numberOfBoxes * box[1];
        truckSize -= numberOfBoxes;
        if (truckSize == 0) break;
    }
    
    return maxUnits;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of box types, due to the sorting operation.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the `maxUnits` variable and the `truckSize` variable.
> - **Why these complexities occur:** The time complexity occurs due to the sorting operation, and the space complexity occurs because we only use a constant amount of space.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution involves sorting the boxes in descending order based on the number of units per box and then iterating over each box type to calculate the maximum number of units that can be put on the truck.
- Detailed breakdown of the approach:
  1. Sort the boxes in descending order based on the number of units per box.
  2. Initialize a variable `maxUnits` to 0.
  3. Iterate over each box type.
  4. For each box type, calculate the number of boxes that can be put on the truck without exceeding the truck size.
  5. Update `maxUnits` by adding the number of units in the current box type multiplied by the number of boxes that can be put on the truck.
- Proof of optimality: This approach is optimal because it involves trying all possible combinations of boxes to find the maximum number of units that can be put on the truck, and it does so in the most efficient way possible by sorting the boxes in descending order based on the number of units per box.

```cpp
int maximumUnits(vector<vector<int>>& boxTypes, int truckSize) {
    // Sort the boxes in descending order based on the number of units per box
    sort(boxTypes.begin(), boxTypes.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[1] > b[1];
    });
    
    int maxUnits = 0;
    for (const auto& box : boxTypes) {
        int numberOfBoxes = min(box[0], truckSize);
        maxUnits += numberOfBoxes * box[1];
        truckSize -= numberOfBoxes;
        if (truckSize == 0) break;
    }
    
    return maxUnits;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of box types, due to the sorting operation.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the `maxUnits` variable and the `truckSize` variable.
> - **Optimality proof:** This approach is optimal because it involves trying all possible combinations of boxes to find the maximum number of units that can be put on the truck, and it does so in the most efficient way possible by sorting the boxes in descending order based on the number of units per box.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: sorting, iteration, and optimization.
- Problem-solving patterns identified: trying all possible combinations of boxes to find the maximum number of units that can be put on the truck.
- Optimization techniques learned: sorting the boxes in descending order based on the number of units per box to reduce the number of iterations.
- Similar problems to practice: other optimization problems involving sorting and iteration.

**Mistakes to Avoid:**
- Common implementation errors: not sorting the boxes in descending order based on the number of units per box, not iterating over each box type, and not updating the `maxUnits` variable correctly.
- Edge cases to watch for: the truck size being 0, the number of boxes of each type being 0, and the number of units in each box being 0.
- Performance pitfalls: not using the most efficient sorting algorithm, not iterating over each box type in the most efficient way possible, and not updating the `maxUnits` variable correctly.
- Testing considerations: testing the function with different inputs, including edge cases, and verifying that the output is correct.