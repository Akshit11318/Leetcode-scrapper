## Two Furthest Houses With Different Colors
**Problem Link:** https://leetcode.com/problems/two-furthest-houses-with-different-colors/description

**Problem Statement:**
- Input format: An array of integers `houses` where `houses[i]` is the color of the house at position `i`.
- Constraints: `2 <= houses.length <= 100`, `1 <= houses[i] <= 100`, All elements of `houses` are distinct.
- Expected output format: The maximum distance between two houses of different colors.
- Key requirements and edge cases to consider: The distance between two houses is the absolute difference between their indices. If there are multiple pairs of houses with the maximum distance, return any one of them.
- Example test cases with explanations:
  - Example 1: Input: `houses = [1,1,4,8,3,2,1,4,5,3]`, Output: `3`, Explanation: The two furthest houses with different colors are houses at indices `1` and `4`.
  - Example 2: Input: `houses = [4,3,5,3,3]`, Output: `2`, Explanation: The two furthest houses with different colors are houses at indices `0` and `2`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through each pair of houses and calculate the distance between them if they have different colors.
- Step-by-step breakdown of the solution:
  1. Iterate through each house in the `houses` array.
  2. For each house, iterate through the remaining houses in the array.
  3. If the current house and the compared house have different colors, calculate the distance between them.
  4. Keep track of the maximum distance found so far.
- Why this approach comes to mind first: It is a straightforward approach that considers all possible pairs of houses.

```cpp
int maxDistance(vector<int>& houses) {
    int maxDist = 0;
    for (int i = 0; i < houses.size(); i++) {
        for (int j = i + 1; j < houses.size(); j++) {
            if (houses[i] != houses[j]) {
                maxDist = max(maxDist, abs(j - i));
            }
        }
    }
    return maxDist;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of houses, because we are using two nested loops to iterate through each pair of houses.
> - **Space Complexity:** $O(1)$, because we are only using a constant amount of space to store the maximum distance.
> - **Why these complexities occur:** The time complexity is quadratic because we are iterating through each pair of houses, and the space complexity is constant because we are not using any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We only need to consider the first and last occurrence of each color to find the maximum distance between two houses of different colors.
- Detailed breakdown of the approach:
  1. Create a map to store the first and last occurrence of each color.
  2. Iterate through the `houses` array to populate the map.
  3. Initialize the maximum distance to 0.
  4. Iterate through the map and calculate the distance between the first occurrence of the current color and the last occurrence of the previous color.
  5. Update the maximum distance if the calculated distance is greater.
- Proof of optimality: This approach is optimal because it only considers the first and last occurrence of each color, which are the only possible candidates for the maximum distance.

```cpp
int maxDistance(vector<int>& houses) {
    map<int, pair<int, int>> colorMap;
    for (int i = 0; i < houses.size(); i++) {
        if (colorMap.find(houses[i]) == colorMap.end()) {
            colorMap[houses[i]] = {i, i};
        } else {
            colorMap[houses[i]].second = i;
        }
    }
    int maxDist = 0;
    for (auto it = colorMap.begin(); it != colorMap.end(); ++it) {
        for (auto it2 = it; it2 != colorMap.end(); ++it2) {
            if (it->first != it2->first) {
                maxDist = max(maxDist, max(abs(it->second.first - it2->second.second), abs(it->second.second - it2->second.first)));
            }
        }
    }
    return maxDist;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of houses, because we are iterating through the `houses` array once to populate the map, and then iterating through the map to calculate the maximum distance.
> - **Space Complexity:** $O(n)$, because in the worst case, we might have a different color for each house, and we are storing the first and last occurrence of each color in the map.
> - **Optimality proof:** This approach is optimal because it only considers the first and last occurrence of each color, which are the only possible candidates for the maximum distance, and it does so in linear time.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a map to store the first and last occurrence of each color, and iterating through the map to calculate the maximum distance.
- Problem-solving patterns identified: Considering the first and last occurrence of each color to find the maximum distance.
- Optimization techniques learned: Using a map to reduce the time complexity from quadratic to linear.
- Similar problems to practice: Problems that involve finding the maximum distance between two elements of different types.

**Mistakes to Avoid:**
- Common implementation errors: Not handling the case where two houses have the same color.
- Edge cases to watch for: The case where there are only two houses, and the case where all houses have the same color.
- Performance pitfalls: Using a quadratic approach when a linear approach is possible.
- Testing considerations: Testing the function with different inputs, including edge cases, to ensure it returns the correct result.