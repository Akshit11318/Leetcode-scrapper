## Maximize the Minimum Powered City

**Problem Link:** https://leetcode.com/problems/maximize-the-minimum-powered-city/description

**Problem Statement:**
- Input format and constraints: The problem involves `n` houses and `m` power plants. Each house has a `houses[i]` value representing its position, and each power plant has a `powerPlants[j]` value representing its position and a `radius` value representing its coverage area. The goal is to maximize the minimum powered city by determining the optimal position for each power plant.
- Expected output format: The output should be the maximum minimum powered city.
- Key requirements and edge cases to consider: The problem requires finding the optimal positions for the power plants to maximize the minimum powered city. Edge cases include handling duplicate house positions and power plant positions.
- Example test cases with explanations: 
    - For example, given `houses = [1, 2, 3, 4]`, `powerPlants = [5, 6]`, and `radius = 2`, the output should be `3` because the power plants can cover the houses at positions `3` and `4`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The initial thought process involves trying all possible positions for the power plants and calculating the minimum powered city for each position.
- Step-by-step breakdown of the solution: 
    1. Iterate over all possible positions for the power plants.
    2. For each position, calculate the minimum powered city by finding the maximum distance between the power plant and the houses it covers.
    3. Update the maximum minimum powered city if the current position results in a higher value.
- Why this approach comes to mind first: This approach comes to mind first because it involves trying all possible solutions and selecting the best one.

```cpp
int maxMinPoweredCity(vector<int>& houses, vector<int>& powerPlants, int radius) {
    int maxMinPoweredCity = INT_MIN;
    for (int i = 0; i <= houses.back(); i++) {
        int minPoweredCity = INT_MAX;
        for (int house : houses) {
            int distance = INT_MAX;
            for (int powerPlant : powerPlants) {
                if (abs(powerPlant - house) <= radius) {
                    distance = min(distance, abs(powerPlant - house));
                }
            }
            minPoweredCity = min(minPoweredCity, distance);
        }
        maxMinPoweredCity = max(maxMinPoweredCity, minPoweredCity);
    }
    return maxMinPoweredCity;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot k)$, where $n$ is the number of houses, $m$ is the number of power plants, and $k$ is the maximum house position.
> - **Space Complexity:** $O(1)$, as the space usage does not grow with the input size.
> - **Why these complexities occur:** The time complexity occurs because the algorithm iterates over all possible positions for the power plants and calculates the minimum powered city for each position. The space complexity is constant because the algorithm only uses a fixed amount of space to store the maximum minimum powered city and the minimum powered city for each position.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The key insight is to use a binary search approach to find the optimal position for the power plants. This involves finding the maximum distance between the power plants and the houses they cover.
- Detailed breakdown of the approach: 
    1. Initialize the search range to the minimum and maximum possible positions for the power plants.
    2. Perform a binary search within the search range to find the optimal position.
    3. For each position in the search range, calculate the minimum powered city by finding the maximum distance between the power plant and the houses it covers.
    4. Update the search range based on whether the current position results in a higher or lower minimum powered city.
- Proof of optimality: The binary search approach is optimal because it reduces the search space by half at each step, resulting in a time complexity of $O(n \log k)$.

```cpp
int maxMinPoweredCity(vector<int>& houses, vector<int>& powerPlants, int radius) {
    int low = 0, high = *max_element(houses.begin(), houses.end());
    while (low < high) {
        int mid = (low + high + 1) / 2;
        if (canCover(houses, powerPlants, radius, mid)) {
            low = mid;
        } else {
            high = mid - 1;
        }
    }
    return low;
}

bool canCover(vector<int>& houses, vector<int>& powerPlants, int radius, int mid) {
    int covered = 0;
    for (int house : houses) {
        bool isCovered = false;
        for (int powerPlant : powerPlants) {
            if (abs(powerPlant - house) <= radius && abs(powerPlant - house) <= mid) {
                isCovered = true;
                break;
            }
        }
        if (!isCovered) return false;
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log k)$, where $n$ is the number of houses and $k$ is the maximum house position.
> - **Space Complexity:** $O(1)$, as the space usage does not grow with the input size.
> - **Optimality proof:** The binary search approach is optimal because it reduces the search space by half at each step, resulting in a time complexity of $O(n \log k)$. This is the best possible time complexity for this problem because it involves finding the optimal position for the power plants.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Binary search, greedy algorithm.
- Problem-solving patterns identified: Reducing the search space by half at each step.
- Optimization techniques learned: Using binary search to find the optimal position.
- Similar problems to practice: Problems involving finding the optimal position or minimum/maximum value.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as duplicate house positions or power plant positions.
- Edge cases to watch for: Duplicate house positions, power plant positions, and minimum/maximum values.
- Performance pitfalls: Using a brute force approach, which can result in a high time complexity.
- Testing considerations: Testing the algorithm with different input sizes and edge cases to ensure correctness and performance.