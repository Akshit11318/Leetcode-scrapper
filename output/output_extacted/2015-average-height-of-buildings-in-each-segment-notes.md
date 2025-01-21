## Average Height of Buildings in Each Segment
**Problem Link:** https://leetcode.com/problems/average-height-of-buildings-in-each-segment/description

**Problem Statement:**
- Input format and constraints: The input will be a list of integers representing the heights of buildings in a city and an integer `segmentWidth` representing the width of each segment.
- Expected output format: The function should return a list of doubles representing the average height of buildings in each segment.
- Key requirements and edge cases to consider: The average height should be calculated by summing the heights of all buildings in a segment and dividing by the number of buildings in that segment.
- Example test cases with explanations:
  - Example 1: Input: `buildings = [1,2,3,4,5,6,7]`, `segmentWidth = 3`, Output: `[2.0,5.0]`
  - Example 2: Input: `buildings = [1,2,3,4,5,6,7]`, `segmentWidth = 4`, Output: `[2.5,5.5]`

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Calculate the average height of buildings in each segment by iterating over the list of buildings and summing the heights of buildings in each segment.
- Step-by-step breakdown of the solution:
  1. Initialize an empty list to store the average heights of buildings in each segment.
  2. Iterate over the list of buildings with a step size of `segmentWidth`.
  3. For each segment, sum the heights of buildings in that segment and divide by the number of buildings in the segment.
  4. Append the calculated average height to the list of average heights.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it may not be the most efficient solution.

```cpp
vector<double> averageOfSegments(vector<int>& buildings, int segmentWidth) {
    vector<double> averageHeights;
    for (int i = 0; i <= buildings.size() - segmentWidth; i++) {
        double sum = 0;
        for (int j = i; j < i + segmentWidth; j++) {
            sum += buildings[j];
        }
        averageHeights.push_back(sum / segmentWidth);
    }
    return averageHeights;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times segmentWidth)$, where $n$ is the number of buildings. This is because we are iterating over the list of buildings and for each segment, we are summing the heights of buildings in that segment.
> - **Space Complexity:** $O(n)$, where $n$ is the number of buildings. This is because we are storing the average heights of buildings in each segment in a list.
> - **Why these complexities occur:** These complexities occur because we are using nested loops to calculate the average heights of buildings in each segment.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Instead of summing the heights of buildings in each segment using nested loops, we can use a single loop to calculate the sum of heights of buildings in each segment.
- Detailed breakdown of the approach:
  1. Initialize an empty list to store the average heights of buildings in each segment.
  2. Initialize a variable to store the sum of heights of buildings in the current segment.
  3. Iterate over the list of buildings.
  4. For each segment, add the height of the current building to the sum of heights and subtract the height of the building that is no longer in the segment.
  5. Calculate the average height of buildings in the current segment by dividing the sum of heights by the number of buildings in the segment.
  6. Append the calculated average height to the list of average heights.
- Proof of optimality: This approach is optimal because it uses a single loop to calculate the average heights of buildings in each segment, resulting in a time complexity of $O(n)$.

```cpp
vector<double> averageOfSegments(vector<int>& buildings, int segmentWidth) {
    vector<double> averageHeights;
    double sum = 0;
    for (int i = 0; i < buildings.size(); i++) {
        sum += buildings[i];
        if (i >= segmentWidth) {
            sum -= buildings[i - segmentWidth];
        }
        if (i >= segmentWidth - 1) {
            averageHeights.push_back(sum / segmentWidth);
        }
    }
    return averageHeights;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of buildings. This is because we are using a single loop to calculate the average heights of buildings in each segment.
> - **Space Complexity:** $O(n)$, where $n$ is the number of buildings. This is because we are storing the average heights of buildings in each segment in a list.
> - **Optimality proof:** This approach is optimal because it uses a single loop to calculate the average heights of buildings in each segment, resulting in a time complexity of $O(n)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the use of a sliding window approach to calculate the average heights of buildings in each segment.
- Problem-solving patterns identified: The problem requires the use of a single loop to calculate the average heights of buildings in each segment, resulting in an optimal time complexity.
- Optimization techniques learned: The problem demonstrates the use of a sliding window approach to optimize the calculation of average heights.
- Similar problems to practice: Similar problems include calculating the maximum sum of a subarray, calculating the minimum sum of a subarray, and calculating the average of a subarray.

**Mistakes to Avoid:**
- Common implementation errors: One common implementation error is using nested loops to calculate the average heights of buildings in each segment, resulting in a time complexity of $O(n \times segmentWidth)$.
- Edge cases to watch for: One edge case to watch for is when the segment width is greater than the number of buildings, resulting in an empty list of average heights.
- Performance pitfalls: One performance pitfall is using a brute force approach to calculate the average heights of buildings in each segment, resulting in a time complexity of $O(n \times segmentWidth)$.
- Testing considerations: The problem requires testing with different segment widths and lists of buildings to ensure that the solution works correctly in all cases.