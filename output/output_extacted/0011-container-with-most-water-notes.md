## Container With Most Water

**Problem Link:** [https://leetcode.com/problems/container-with-most-water/description](https://leetcode.com/problems/container-with-most-water/description)

**Problem Statement:**
- Input: `height`, an array of integers representing the height of each line.
- Constraints: `2 <= height.length <= 10^5`, `0 <= height[i] <= 10^4`.
- Expected Output: The maximum area of water that can be trapped between two lines.
- Key Requirements: The area of water is calculated as `min(height[i], height[j]) * (j - i)`, where `i` and `j` are the indices of the two lines.
- Edge Cases: If the input array has less than two elements, return `0`.

**Example Test Cases:**
- `height = [1,8,6,2,5,4,8,3,7]`, expected output: `49`
- `height = [1,1]`, expected output: `1`

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to calculate the area of water for every possible pair of lines and keep track of the maximum area found.
- This approach involves iterating over the array and for each element, iterating over the rest of the array to calculate the area.
- This approach comes to mind first because it's a straightforward way to ensure that all possible pairs are considered.

```cpp
int maxArea(vector<int>& height) {
    int maxArea = 0;
    for (int i = 0; i < height.size(); i++) {
        for (int j = i + 1; j < height.size(); j++) {
            int area = min(height[i], height[j]) * (j - i);
            maxArea = max(maxArea, area);
        }
    }
    return maxArea;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of lines, because for each line, we're iterating over the rest of the lines.
> - **Space Complexity:** $O(1)$, because we're only using a constant amount of space to store the maximum area.
> - **Why these complexities occur:** The nested loops cause the time complexity to be quadratic, while the space complexity remains constant because we're not using any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a two-pointer technique, starting from both ends of the array and moving towards the center.
- The area of water is determined by the shorter line, so if we move the pointer of the shorter line towards the center, we might find a taller line that can hold more water.
- This approach ensures that we consider all possible pairs of lines in a more efficient manner.
- Proof of optimality: This approach has a linear time complexity, which is the best we can achieve because we must at least look at each line once.

```cpp
int maxArea(vector<int>& height) {
    int maxArea = 0;
    int left = 0, right = height.size() - 1;
    while (left < right) {
        int area = min(height[left], height[right]) * (right - left);
        maxArea = max(maxArea, area);
        if (height[left] < height[right]) {
            left++;
        } else {
            right--;
        }
    }
    return maxArea;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of lines, because we're only iterating over the array once.
> - **Space Complexity:** $O(1)$, because we're only using a constant amount of space to store the maximum area and the two pointers.
> - **Optimality proof:** This approach is optimal because it has a linear time complexity, and we must at least look at each line once to determine the maximum area.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: two-pointer technique, area calculation.
- Problem-solving patterns identified: using a two-pointer technique to reduce the time complexity.
- Optimization techniques learned: starting from both ends of the array and moving towards the center.
- Similar problems to practice: other problems that involve finding the maximum or minimum area, such as the `Trapping Rain Water` problem.

**Mistakes to Avoid:**
- Common implementation errors: forgetting to update the maximum area, incorrect pointer movement.
- Edge cases to watch for: arrays with less than two elements, arrays with identical elements.
- Performance pitfalls: using a brute force approach, which can lead to a time limit exceeded error.
- Testing considerations: test the function with different input arrays, including edge cases.