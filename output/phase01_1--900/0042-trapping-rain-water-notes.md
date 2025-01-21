## Trapping Rain Water

**Problem Link:** https://leetcode.com/problems/trapping-rain-water/description

**Problem Statement:**
- Input format and constraints: Given an array of non-negative integers representing the height of bars in a histogram, find the amount of water that can be trapped between the bars.
- Expected output format: Return the total amount of water that can be trapped.
- Key requirements and edge cases to consider:
  - The input array may be empty or contain only one element.
  - The input array may contain duplicate heights.
- Example test cases with explanations:
  - Input: `height = [0,1,0,2,1,0,1,3,2,1,2,1]`
  - Output: `6`
  - Explanation: The above elevation map is represented by an array `[0,1,0,2,1,0,1,3,2,1,2,1]`. In this case, 6 units of water (blue section) are being trapped.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: For each bar in the histogram, calculate the maximum height of the bars to its left and right. The amount of water that can be trapped above the current bar is the minimum of these two maximum heights minus the height of the current bar.
- Step-by-step breakdown of the solution:
  1. Iterate over each bar in the histogram.
  2. For each bar, iterate over the bars to its left and find the maximum height.
  3. For each bar, iterate over the bars to its right and find the maximum height.
  4. Calculate the amount of water that can be trapped above the current bar using the minimum of the two maximum heights.
- Why this approach comes to mind first: It is a straightforward approach that directly calculates the amount of water that can be trapped above each bar by considering all possible pairs of bars.

```cpp
class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        int totalWater = 0;
        
        for (int i = 0; i < n; i++) {
            int leftMax = 0, rightMax = 0;
            
            // Find the maximum height to the left
            for (int j = 0; j < i; j++) {
                leftMax = max(leftMax, height[j]);
            }
            
            // Find the maximum height to the right
            for (int j = i + 1; j < n; j++) {
                rightMax = max(rightMax, height[j]);
            }
            
            // Calculate the amount of water that can be trapped
            int water = min(leftMax, rightMax) - height[i];
            if (water > 0) {
                totalWater += water;
            }
        }
        
        return totalWater;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of bars in the histogram. This is because for each bar, we are iterating over all the bars to its left and right to find the maximum heights.
> - **Space Complexity:** $O(1)$, as we are only using a constant amount of space to store the maximum heights and the total amount of water.
> - **Why these complexities occur:** The brute force approach has a high time complexity due to the nested loops used to find the maximum heights to the left and right of each bar.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use two pointers, one starting from the left and one from the right, to keep track of the maximum heights to the left and right of each bar. This way, we can avoid iterating over all the bars for each bar.
- Detailed breakdown of the approach:
  1. Initialize two pointers, `left` and `right`, to the start and end of the histogram, respectively.
  2. Initialize two variables, `leftMax` and `rightMax`, to keep track of the maximum heights to the left and right of the current bar.
  3. Iterate over the histogram, moving the pointer that points to the shorter bar towards the other pointer.
  4. Update the maximum height and calculate the amount of water that can be trapped at each step.
- Proof of optimality: This approach has a time complexity of $O(n)$, which is optimal because we need to visit each bar at least once to calculate the amount of water that can be trapped.

```cpp
class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        int left = 0, right = n - 1;
        int leftMax = 0, rightMax = 0;
        int totalWater = 0;
        
        while (left <= right) {
            if (height[left] < height[right]) {
                if (height[left] >= leftMax) {
                    leftMax = height[left];
                } else {
                    totalWater += leftMax - height[left];
                }
                left++;
            } else {
                if (height[right] >= rightMax) {
                    rightMax = height[right];
                } else {
                    totalWater += rightMax - height[right];
                }
                right--;
            }
        }
        
        return totalWater;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of bars in the histogram. This is because we are iterating over the histogram only once.
> - **Space Complexity:** $O(1)$, as we are only using a constant amount of space to store the maximum heights and the total amount of water.
> - **Optimality proof:** This approach is optimal because we are visiting each bar only once and calculating the amount of water that can be trapped at each step.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Two-pointer technique, dynamic programming.
- Problem-solving patterns identified: Using pointers to keep track of maximum heights, iterating over the histogram only once.
- Optimization techniques learned: Avoiding nested loops, using dynamic programming to store intermediate results.
- Similar problems to practice: Container With Most Water, Minimum Window Substring.

**Mistakes to Avoid:**
- Common implementation errors: Not updating the maximum heights correctly, not handling edge cases properly.
- Edge cases to watch for: Empty histogram, histogram with only one bar, histogram with duplicate heights.
- Performance pitfalls: Using nested loops, not using dynamic programming to store intermediate results.
- Testing considerations: Test the solution with different input sizes, test the solution with different input patterns (e.g., increasing, decreasing, random).