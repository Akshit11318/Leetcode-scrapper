## Largest Rectangle in Histogram
**Problem Link:** https://leetcode.com/problems/largest-rectangle-in-histogram/description

**Problem Statement:**
- Input format: An array of integers `heights` representing the histogram's bar heights.
- Constraints: `1 <= heights.length <= 1000`, `0 <= heights[i] <= 10^4`.
- Expected output format: The area of the largest rectangle in the histogram.
- Key requirements and edge cases to consider: Handling empty input, single-element input, and ensuring the solution works for all possible input combinations.
- Example test cases with explanations:
  - Input: `heights = [2,1,5,6,2,3]`, Output: `10`
  - Input: `heights = [2,4]`, Output: `2`

---

### Brute Force Approach
**Explanation:**
- Initial thought process: For each bar in the histogram, calculate the area of the rectangle that can be formed by extending the bar to the left and right as far as possible without going below the bar's height.
- Step-by-step breakdown of the solution:
  1. Iterate over each bar in the histogram.
  2. For each bar, extend to the left and right to find the maximum area rectangle that can be formed with the current bar as the smallest bar.
  3. Keep track of the maximum area found so far.
- Why this approach comes to mind first: It directly addresses the problem by considering each bar's potential to form the largest rectangle.

```cpp
class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int maxArea = 0;
        for (int i = 0; i < heights.size(); i++) {
            int minHeight = heights[i];
            for (int j = i; j >= 0; j--) {
                minHeight = min(minHeight, heights[j]);
                maxArea = max(maxArea, (i - j + 1) * minHeight);
            }
            minHeight = heights[i];
            for (int j = i; j < heights.size(); j++) {
                minHeight = min(minHeight, heights[j]);
                maxArea = max(maxArea, (j - i + 1) * minHeight);
            }
        }
        return maxArea;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of bars in the histogram, because for each bar, we potentially iterate over the entire histogram.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum area and the current bar's height.
> - **Why these complexities occur:** The nested loops over the histogram cause the quadratic time complexity, while the constant space complexity is due to not using any data structures that scale with input size.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Using a stack to keep track of the indices of the bars. When a bar is encountered that is smaller than the bar at the top of the stack, we calculate the area of the rectangle with the bar at the top of the stack as the smallest bar.
- Detailed breakdown of the approach:
  1. Initialize an empty stack and a variable `maxArea` to 0.
  2. Iterate over the histogram. For each bar:
     - While the stack is not empty and the current bar is smaller than the bar at the top of the stack, calculate the area of the rectangle with the bar at the top of the stack as the smallest bar and update `maxArea` if necessary.
     - Push the current index onto the stack.
  3. After iterating over the histogram, calculate the areas for the remaining bars in the stack.
- Proof of optimality: This approach ensures that we consider all possible rectangles in a single pass through the histogram, avoiding the need for nested loops and thus reducing the time complexity to linear.

```cpp
class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int n = heights.size();
        vector<int> stack;
        int maxArea = 0;
        for (int i = 0; i <= n; i++) {
            int h = (i == n) ? 0 : heights[i];
            while (!stack.empty() && heights[stack.back()] > h) {
                int height = heights[stack.back()];
                stack.pop_back();
                int width = stack.empty() ? i : i - stack.back() - 1;
                maxArea = max(maxArea, height * width);
            }
            stack.push_back(i);
        }
        return maxArea;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of bars in the histogram, because we make a single pass through the histogram.
> - **Space Complexity:** $O(n)$, as in the worst case, we might push all indices onto the stack.
> - **Optimality proof:** The linear time complexity is optimal because we must at least read the input once, and the single pass through the histogram ensures we consider all possible rectangles without unnecessary repetition.

---

### Final Notes
**Learning Points:**
- Key algorithmic concepts demonstrated: Using a stack to efficiently track and calculate areas of rectangles in a histogram.
- Problem-solving patterns identified: Reducing time complexity by avoiding nested loops and using a single pass approach.
- Optimization techniques learned: Utilizing a stack to keep track of indices and calculate areas only when necessary.
- Similar problems to practice: Other problems involving histograms or arrays where a single pass approach can be beneficial.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly calculating the width of the rectangle or forgetting to update the `maxArea` variable.
- Edge cases to watch for: Handling empty input or single-element input correctly.
- Performance pitfalls: Using nested loops or other inefficient algorithms that lead to high time complexity.
- Testing considerations: Thoroughly testing the solution with various input combinations, including edge cases.