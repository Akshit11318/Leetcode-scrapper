## Best Position for a Service Centre
**Problem Link:** https://leetcode.com/problems/best-position-for-a-service-centre/description

**Problem Statement:**
- Input format: An array of integers representing the positions of houses.
- Constraints: The input array will not be empty, and all elements will be distinct.
- Expected output format: The position of the service centre that minimizes the sum of distances to all houses.
- Key requirements and edge cases to consider: The service centre can only be placed at a position that is an integer, and the positions of the houses are given in the input array.
- Example test cases with explanations: 
  - For the input `[1, 2, 3]`, the output should be `2` because the service centre can be placed at position `2` to minimize the sum of distances.
  - For the input `[4, 8]`, the output should be `6` because the service centre can be placed at position `6` to minimize the sum of distances.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible positions for the service centre and calculate the sum of distances to all houses for each position.
- Step-by-step breakdown of the solution: 
  1. Iterate over all possible positions for the service centre.
  2. For each position, calculate the sum of distances to all houses.
  3. Keep track of the position that results in the minimum sum of distances.
- Why this approach comes to mind first: It is a straightforward and intuitive solution that tries all possible options.

```cpp
int getMinDistSum(vector<int>& positions) {
    int n = positions.size();
    double minSum = INT_MAX;
    double minPosition = 0.0;
    
    // Try all possible positions
    for (double position = positions[0]; position <= positions[n - 1]; position += 0.001) {
        double sum = 0.0;
        
        // Calculate the sum of distances for the current position
        for (int i = 0; i < n; i++) {
            sum += abs(position - positions[i]);
        }
        
        // Update the minimum sum and position if necessary
        if (sum < minSum) {
            minSum = sum;
            minPosition = position;
        }
    }
    
    return round(minPosition);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot \frac{max\_position - min\_position}{step\_size})$, where $n$ is the number of houses and $step\_size$ is the increment between positions.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the minimum sum and position.
> - **Why these complexities occur:** The time complexity occurs because we iterate over all possible positions and calculate the sum of distances for each position. The space complexity occurs because we only use a constant amount of space to store the minimum sum and position.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal position for the service centre is the median of the positions of the houses.
- Detailed breakdown of the approach: 
  1. Sort the positions of the houses in ascending order.
  2. If the number of houses is odd, the optimal position is the middle position.
  3. If the number of houses is even, the optimal position is the average of the two middle positions.
- Proof of optimality: This approach is optimal because the median is the value that minimizes the sum of absolute deviations from all other values in a dataset.
- Why further optimization is impossible: This approach is already optimal because it uses the median, which is the value that minimizes the sum of absolute deviations.

```cpp
int getMinDistSum(vector<int>& positions) {
    int n = positions.size();
    
    // Sort the positions in ascending order
    sort(positions.begin(), positions.end());
    
    // Calculate the median position
    if (n % 2 == 1) {
        return positions[n / 2];
    } else {
        return (positions[n / 2 - 1] + positions[n / 2]) / 2;
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of houses.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the median position.
> - **Optimality proof:** This approach is optimal because it uses the median, which is the value that minimizes the sum of absolute deviations from all other values in a dataset.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The importance of the median in minimizing the sum of absolute deviations.
- Problem-solving patterns identified: The use of sorting and median calculation to solve optimization problems.
- Optimization techniques learned: The use of the median to minimize the sum of absolute deviations.
- Similar problems to practice: Other optimization problems that involve minimizing the sum of absolute deviations.

**Mistakes to Avoid:**
- Common implementation errors: Not sorting the positions correctly or not calculating the median correctly.
- Edge cases to watch for: Handling the cases where the number of houses is odd or even.
- Performance pitfalls: Not using the median calculation, which can lead to inefficient solutions.
- Testing considerations: Testing the solution with different inputs and edge cases to ensure correctness.