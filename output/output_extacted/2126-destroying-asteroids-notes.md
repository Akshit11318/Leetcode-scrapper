## Destroying Asteroids

**Problem Link:** https://leetcode.com/problems/destroying-asteroids/description

**Problem Statement:**
- Input format and constraints: The problem takes an integer `mass` as input, representing the mass of the spaceship, and an array `asteroids` of integers, representing the masses of the asteroids. The goal is to destroy as many asteroids as possible using the spaceship.
- Expected output format: The function should return the maximum number of asteroids that can be destroyed.
- Key requirements and edge cases to consider:
  - The spaceship can only destroy asteroids with masses less than or equal to its own mass.
  - If the spaceship's mass is greater than or equal to an asteroid's mass, it can destroy the asteroid and increase its mass by the asteroid's mass.
  - If the spaceship's mass is less than an asteroid's mass, it cannot destroy the asteroid.
- Example test cases with explanations:
  - Input: `mass = 10`, `asteroids = [3,5,7,11]`
    - Output: `2`
    - Explanation: The spaceship can destroy the asteroids with masses 3 and 5, increasing its mass to 18. However, it cannot destroy the asteroid with mass 7, so it can only destroy two asteroids.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves checking all possible combinations of asteroids to determine the maximum number that can be destroyed.
- Step-by-step breakdown of the solution:
  1. Initialize a variable to store the maximum number of asteroids that can be destroyed.
  2. Iterate over all possible combinations of asteroids.
  3. For each combination, check if the spaceship can destroy all the asteroids in the combination.
  4. If the spaceship can destroy all the asteroids in the combination, update the maximum number of asteroids that can be destroyed.
- Why this approach comes to mind first: The brute force approach is often the first approach that comes to mind because it is simple and straightforward. However, it is not efficient for large inputs because it has a high time complexity.

```cpp
#include <vector>
#include <algorithm>

int destroyAsteroids(int mass, std::vector<int>& asteroids) {
    int maxDestroyed = 0;
    for (int i = 0; i < (1 << asteroids.size()); i++) {
        int currentMass = mass;
        int currentDestroyed = 0;
        for (int j = 0; j < asteroids.size(); j++) {
            if ((i & (1 << j)) && asteroids[j] <= currentMass) {
                currentMass += asteroids[j];
                currentDestroyed++;
            }
        }
        maxDestroyed = std::max(maxDestroyed, currentDestroyed);
    }
    return maxDestroyed;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the number of asteroids. This is because we are iterating over all possible combinations of asteroids, and for each combination, we are iterating over all the asteroids.
> - **Space Complexity:** $O(1)$, because we are not using any additional space that scales with the input size.
> - **Why these complexities occur:** The high time complexity occurs because we are using a brute force approach that checks all possible combinations of asteroids. The low space complexity occurs because we are not using any additional space that scales with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The key insight is to use a greedy approach. We can sort the asteroids in ascending order of their masses and then iterate over them. For each asteroid, we can check if the spaceship can destroy it. If it can, we destroy the asteroid and increase the spaceship's mass.
- Detailed breakdown of the approach:
  1. Sort the asteroids in ascending order of their masses.
  2. Initialize a variable to store the maximum number of asteroids that can be destroyed.
  3. Iterate over the sorted asteroids.
  4. For each asteroid, check if the spaceship can destroy it. If it can, destroy the asteroid and increase the spaceship's mass.
- Proof of optimality: The greedy approach is optimal because it always chooses the asteroid with the smallest mass that the spaceship can destroy. This ensures that the spaceship can destroy the maximum number of asteroids.

```cpp
#include <vector>
#include <algorithm>

int destroyAsteroids(int mass, std::vector<int>& asteroids) {
    std::sort(asteroids.begin(), asteroids.end());
    int destroyed = 0;
    for (int asteroid : asteroids) {
        if (asteroid <= mass) {
            mass += asteroid;
            destroyed++;
        }
    }
    return destroyed;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of asteroids. This is because we are sorting the asteroids, which takes $O(n \log n)$ time.
> - **Space Complexity:** $O(1)$, because we are not using any additional space that scales with the input size.
> - **Optimality proof:** The greedy approach is optimal because it always chooses the asteroid with the smallest mass that the spaceship can destroy. This ensures that the spaceship can destroy the maximum number of asteroids.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the use of greedy algorithms and sorting.
- Problem-solving patterns identified: The problem requires the use of a greedy approach to solve it efficiently.
- Optimization techniques learned: The problem requires the use of sorting to optimize the solution.
- Similar problems to practice: Other problems that involve greedy algorithms and sorting, such as the `h-index` problem.

**Mistakes to Avoid:**
- Common implementation errors: One common implementation error is to use a brute force approach instead of a greedy approach.
- Edge cases to watch for: One edge case to watch for is when the input array is empty.
- Performance pitfalls: One performance pitfall is to use a sorting algorithm with a high time complexity, such as bubble sort.
- Testing considerations: The solution should be tested with different input cases, including edge cases and large inputs.