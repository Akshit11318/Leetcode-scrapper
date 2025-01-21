## Sum of Distances
**Problem Link:** [https://leetcode.com/problems/sum-of-distances/description](https://leetcode.com/problems/sum-of-distances/description)

**Problem Statement:**
- Input format and constraints: The input is a 2D grid where each cell is either 1 (representing a city) or 0 (representing an empty cell). The grid size is `m x n`, and `m` and `n` are integers. The task is to calculate the sum of distances from each city to every other city.
- Expected output format: The output should be the sum of distances between all pairs of cities.
- Key requirements and edge cases to consider: The grid can contain multiple cities, and the distance between two cities is the Manhattan distance (the sum of the absolute differences of their Cartesian coordinates).
- Example test cases with explanations: For example, given a grid `[[1,0,0],[0,0,1],[1,0,1]]`, the sum of distances between all pairs of cities is `1 + 2 + 3 + 1 + 1 + 2 = 10`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The most straightforward approach is to iterate over each city in the grid, calculate the Manhattan distance to every other city, and sum up these distances.
- Step-by-step breakdown of the solution:
  1. Initialize the sum of distances to 0.
  2. Iterate over each cell in the grid.
  3. If the cell represents a city, iterate over the rest of the grid to find other cities.
  4. For each pair of cities, calculate the Manhattan distance and add it to the sum.
- Why this approach comes to mind first: It directly addresses the problem statement by considering all possible pairs of cities and calculating their distances.

```cpp
int sumOfDistances(vector<vector<int>>& grid) {
    int m = grid.size();
    int n = grid[0].size();
    int sum = 0;
    
    // Iterate over each cell in the grid
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            // If the cell represents a city
            if (grid[i][j] == 1) {
                // Iterate over the rest of the grid to find other cities
                for (int x = 0; x < m; x++) {
                    for (int y = 0; y < n; y++) {
                        // If the cell represents another city and it's not the same city
                        if (grid[x][y] == 1 && (x != i || y != j)) {
                            // Calculate the Manhattan distance and add it to the sum
                            sum += abs(x - i) + abs(y - j);
                        }
                    }
                }
            }
        }
    }
    
    return sum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m^2 \cdot n^2)$, where $m$ and $n$ are the dimensions of the grid. This is because for each city, we potentially iterate over the entire grid again to find other cities.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the sum and loop variables.
> - **Why these complexities occur:** The brute force approach involves nested loops over the grid, leading to a high time complexity. However, it uses minimal extra space, resulting in a low space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of calculating the distance between each pair of cities multiple times, we can calculate it once for each pair by iterating over the cities only once.
- Detailed breakdown of the approach:
  1. First, collect the coordinates of all cities in the grid.
  2. Then, for each city, calculate its distance to every other city.
  3. Sum up these distances to get the total sum of distances between all pairs of cities.
- Proof of optimality: This approach is optimal because it ensures each pair of cities is considered exactly once, minimizing the number of distance calculations needed.
- Why further optimization is impossible: Given that we must consider each pair of cities at least once to calculate their distance, this approach achieves the minimum number of operations required to solve the problem.

```cpp
int sumOfDistances(vector<vector<int>>& grid) {
    int m = grid.size();
    int n = grid[0].size();
    vector<pair<int, int>> cities;
    
    // Collect the coordinates of all cities
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (grid[i][j] == 1) {
                cities.emplace_back(i, j);
            }
        }
    }
    
    int sum = 0;
    int numCities = cities.size();
    
    // For each city, calculate its distance to every other city
    for (int i = 0; i < numCities; i++) {
        for (int j = i + 1; j < numCities; j++) {
            // Calculate the Manhattan distance and add it to the sum
            sum += abs(cities[i].first - cities[j].first) + abs(cities[i].second - cities[j].second);
        }
    }
    
    // Since we only counted each pair once, we need to multiply by 2 to account for both directions
    return sum * 2;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n + k^2)$, where $m$ and $n$ are the dimensions of the grid, and $k$ is the number of cities. The first term accounts for finding all cities, and the second term accounts for calculating distances between all pairs of cities.
> - **Space Complexity:** $O(k)$, where $k$ is the number of cities, as we store their coordinates.
> - **Optimality proof:** This approach ensures each pair of cities is considered exactly once, minimizing the number of distance calculations needed, thus achieving optimality.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, distance calculation, and optimization by reducing redundant calculations.
- Problem-solving patterns identified: The importance of identifying and avoiding redundant work in algorithms.
- Optimization techniques learned: Reducing the number of iterations and calculations by considering each pair of elements only once.
- Similar problems to practice: Other problems involving distance calculations and optimizations, such as finding the closest pair of points in a set.

**Mistakes to Avoid:**
- Common implementation errors: Failing to consider all pairs of cities or incorrectly calculating distances.
- Edge cases to watch for: Grids with no cities, grids with a single city, and grids with cities positioned at the edges or corners.
- Performance pitfalls: Using inefficient algorithms that result in high time complexities, such as the brute force approach for large inputs.
- Testing considerations: Thoroughly testing the algorithm with various grid sizes, city distributions, and edge cases to ensure correctness and efficiency.