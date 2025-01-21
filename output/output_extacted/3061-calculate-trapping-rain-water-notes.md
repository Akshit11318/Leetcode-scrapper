## Trapping Rain Water
**Problem Link:** https://leetcode.com/problems/calculate-trapping-rain-water/description

**Problem Statement:**
- Input format: An array of non-negative integers representing an elevation map where the width of each bar is 1.
- Constraints: The input array is not null and contains at least one element.
- Expected output format: The amount of water that can be trapped between the bars.
- Key requirements and edge cases to consider: The water can be trapped between two bars if there is a bar on both sides that is higher than the current bar, and the water level is determined by the minimum height of the two higher bars.
- Example test cases:
  - Input: `[0,1,0,2,1,0,1,3,2,1,2,1]`
  - Output: `6`
  - Explanation: The above elevation map is represented by the array `[0,1,0,2,1,0,1,3,2,1,2,1]`. In this case, 6 units of water can be trapped.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: For each bar, find the maximum height of bars on both sides and calculate the trapped water based on the minimum of these two heights.
- Step-by-step breakdown of the solution:
  1. Iterate through the array for each bar.
  2. For each bar, find the maximum height of bars on the left and right sides.
  3. Calculate the trapped water for the current bar by taking the minimum of the left and right maximum heights and subtracting the height of the current bar.
  4. Sum up the trapped water for all bars.
- Why this approach comes to mind first: It's a straightforward approach that directly addresses the problem statement by considering each bar individually and calculating the water that can be trapped.

```cpp
int trap(vector<int>& height) {
    int n = height.size();
    int water = 0;
    for (int i = 0; i < n; i++) {
        int leftMax = 0, rightMax = 0;
        for (int j = i; j >= 0; j--) {
            leftMax = max(leftMax, height[j]);
        }
        for (int j = i; j < n; j++) {
            rightMax = max(rightMax, height[j]);
        }
        water += max(0, min(leftMax, rightMax) - height[i]);
    }
    return water;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of bars. This is because for each bar, we potentially iterate through the entire array to find the maximum heights on both sides.
> - **Space Complexity:** $O(1)$, excluding the space required for the input array, as we only use a constant amount of space to store variables.
> - **Why these complexities occur:** The nested loops for finding the maximum heights on both sides of each bar cause the quadratic time complexity. The space complexity is constant because we don't use any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of calculating the maximum heights on both sides for each bar, we can maintain two arrays, one for the maximum height of bars on the left and one for the maximum height of bars on the right, up to each position.
- Detailed breakdown of the approach:
  1. Initialize two arrays, `leftMax` and `rightMax`, of the same size as the input array, to store the maximum heights of bars on the left and right of each position, respectively.
  2. Iterate through the input array from left to right to fill `leftMax`.
  3. Iterate through the input array from right to left to fill `rightMax`.
  4. Calculate the trapped water for each bar by taking the minimum of `leftMax` and `rightMax` at that position and subtracting the height of the bar, then sum these values.
- Proof of optimality: This approach is optimal because it only requires two passes through the input array to calculate the necessary maximum heights, reducing the time complexity significantly.
- Why further optimization is impossible: Given the nature of the problem, where we must consider the maximum heights on both sides of each bar, any solution must at least examine each bar once, leading to a linear time complexity in the best case.

```cpp
int trap(vector<int>& height) {
    int n = height.size();
    if (n == 0) return 0;
    
    vector<int> leftMax(n), rightMax(n);
    leftMax[0] = height[0];
    rightMax[n-1] = height[n-1];
    
    // Calculate leftMax
    for (int i = 1; i < n; i++) {
        leftMax[i] = max(leftMax[i-1], height[i]);
    }
    
    // Calculate rightMax
    for (int i = n - 2; i >= 0; i--) {
        rightMax[i] = max(rightMax[i+1], height[i]);
    }
    
    int water = 0;
    for (int i = 0; i < n; i++) {
        water += max(0, min(leftMax[i], rightMax[i]) - height[i]);
    }
    
    return water;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of bars. This is because we make three passes through the array: one to calculate `leftMax`, one to calculate `rightMax`, and one to calculate the trapped water.
> - **Space Complexity:** $O(n)$, because we use two additional arrays of the same size as the input array to store `leftMax` and `rightMax`.
> - **Optimality proof:** This approach is optimal because it reduces the time complexity to linear by avoiding the nested loop structure of the brute force approach, while the space complexity is also linear due to the need to store the maximum heights on both sides for each bar.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Two-pointer technique, dynamic programming (implicitly in maintaining `leftMax` and `rightMax` arrays).
- Problem-solving patterns identified: Breaking down a problem into smaller, more manageable parts (calculating `leftMax` and `rightMax` separately).
- Optimization techniques learned: Avoiding nested loops by precomputing necessary values.
- Similar problems to practice: Other problems involving arrays and dynamic programming, such as the `Container With Most Water` problem.

**Mistakes to Avoid:**
- Common implementation errors: Not properly initializing arrays or variables, incorrect loop bounds.
- Edge cases to watch for: Empty input array, single-element input array.
- Performance pitfalls: Using nested loops when a linear solution is possible.
- Testing considerations: Ensure to test with various input sizes, including edge cases like empty or single-element arrays.