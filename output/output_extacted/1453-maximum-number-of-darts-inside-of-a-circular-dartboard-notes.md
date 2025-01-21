## Maximum Number of Darts Inside of a Circular Dartboard

**Problem Link:** https://leetcode.com/problems/maximum-number-of-darts-inside-of-a-circular-dartboard/description

**Problem Statement:**
- Input format: You are given a `radius` of a circular dartboard and an array of `darts` where each dart is represented by its coordinates `(x, y)`.
- Constraints: The number of darts is denoted by `n`, and `1 <= n <= 1000`.
- Expected output format: The maximum number of darts that can be thrown inside the circular dartboard.
- Key requirements and edge cases to consider:
  - A dart is considered inside the dartboard if its distance from the center of the dartboard is less than or equal to the radius.
  - The coordinates of the darts can be negative, zero, or positive.
- Example test cases with explanations:
  - For `radius = 1` and `darts = [[-2, -2], [1, 1], [2, 2], [4, 4]]`, the maximum number of darts that can be thrown inside the circular dartboard is `1` because only one dart is within the circle.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over each dart and calculate its distance from the center of the dartboard.
- Step-by-step breakdown of the solution:
  1. Define a function to calculate the Euclidean distance between two points.
  2. Initialize a counter to store the number of darts inside the dartboard.
  3. Iterate over each dart and calculate its distance from the center using the function defined in step 1.
  4. If the distance is less than or equal to the radius, increment the counter.
- Why this approach comes to mind first: It is straightforward and directly addresses the problem statement.

```cpp
int numPoints(vector<vector<int>>& points, int radius) {
    int count = 0;
    for (auto& point : points) {
        int x = point[0];
        int y = point[1];
        double distance = sqrt(x * x + y * y);
        if (distance <= radius) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of darts. This is because we iterate over each dart once.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input, as we only use a constant amount of space to store the count.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each dart. The space complexity is constant because we do not use any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The same insight as the brute force approach, as it is already optimal for this problem.
- Detailed breakdown of the approach: The approach remains the same as the brute force, as it is already optimal.
- Proof of optimality: This approach is optimal because we must check each dart at least once to determine if it is within the dartboard. Therefore, the time complexity cannot be better than $O(n)$.
- Why further optimization is impossible: Further optimization is impossible because we cannot reduce the number of darts we need to check.

```cpp
int numPoints(vector<vector<int>>& points, int radius) {
    int count = 0;
    for (auto& point : points) {
        int x = point[0];
        int y = point[1];
        double distance = sqrt(x * x + y * y);
        if (distance <= radius) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of darts.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input.
> - **Optimality proof:** The time complexity is optimal because we must check each dart at least once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, distance calculation, and conditional checks.
- Problem-solving patterns identified: Directly addressing the problem statement and using basic mathematical concepts.
- Optimization techniques learned: Recognizing when an approach is already optimal.
- Similar problems to practice: Other problems involving geometric calculations and iteration.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly calculating the distance or not checking the radius condition correctly.
- Edge cases to watch for: Darts with coordinates that result in a distance exactly equal to the radius.
- Performance pitfalls: Using inefficient data structures or algorithms that scale poorly with the input size.
- Testing considerations: Thoroughly testing the function with a variety of inputs, including edge cases.