## Finding the Number of Visible Mountains

**Problem Link:** https://leetcode.com/problems/finding-the-number-of-visible-mountains/description

**Problem Statement:**
- Input: A list of mountain heights represented as integers.
- Constraints: The input list is non-empty and contains only positive integers.
- Expected output: The number of visible mountains, where a mountain is considered visible if it is not blocked by a taller mountain to its left.
- Key requirements and edge cases to consider: The problem requires counting the visible mountains by iterating through the list of heights.
- Example test cases with explanations:
  - Input: `[1, 2, 3, 4, 5]`
  - Expected output: `5`
  - Explanation: All mountains are visible because there are no taller mountains to their left.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to compare each mountain with all the mountains to its left to check if it is blocked by a taller mountain.
- Step-by-step breakdown of the solution:
  1. Initialize a counter for visible mountains.
  2. Iterate through the list of mountain heights.
  3. For each mountain, compare its height with the heights of all the mountains to its left.
  4. If a mountain is not blocked by a taller mountain to its left, increment the counter for visible mountains.
- Why this approach comes to mind first: It directly addresses the problem statement by checking each mountain's visibility based on the heights of the mountains to its left.

```cpp
int visibleMountains(vector<int>& heights) {
    int count = 0;
    for (int i = 0; i < heights.size(); i++) {
        bool isVisible = true;
        for (int j = 0; j < i; j++) {
            if (heights[j] >= heights[i]) {
                isVisible = false;
                break;
            }
        }
        if (isVisible) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of mountains. This is because for each mountain, we are potentially comparing it with all the mountains to its left.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input, because we are using a constant amount of space to store the count of visible mountains.
> - **Why these complexities occur:** The nested loop structure causes the quadratic time complexity, while the constant space usage is due to only needing a single variable to keep track of the count of visible mountains.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of comparing each mountain with all the mountains to its left, we can keep track of the maximum height of the mountains seen so far. If the current mountain's height is greater than the maximum height seen, it is visible and we update the maximum height.
- Detailed breakdown of the approach:
  1. Initialize a variable to keep track of the maximum height seen so far and a counter for visible mountains.
  2. Iterate through the list of mountain heights.
  3. For each mountain, check if its height is greater than the maximum height seen so far.
  4. If it is, increment the counter for visible mountains and update the maximum height seen.
- Proof of optimality: This approach is optimal because it only requires a single pass through the list of mountain heights, resulting in a linear time complexity.
- Why further optimization is impossible: Given that we must examine each mountain at least once to determine its visibility, a linear time complexity is the best we can achieve.

```cpp
int visibleMountains(vector<int>& heights) {
    int maxSoFar = 0;
    int count = 0;
    for (int height : heights) {
        if (height > maxSoFar) {
            count++;
            maxSoFar = height;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of mountains. This is because we make a single pass through the list of heights.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input, because we use a constant amount of space to store the maximum height seen and the count of visible mountains.
> - **Optimality proof:** The linear time complexity is optimal because we must at least read the input once, and our algorithm achieves this lower bound.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The importance of keeping track of relevant information (in this case, the maximum height seen so far) to avoid redundant comparisons and achieve a more efficient solution.
- Problem-solving patterns identified: The use of a single pass through the data to solve the problem, which is indicative of a linear time complexity.
- Optimization techniques learned: Reducing the number of comparisons needed by maintaining a running maximum or minimum, which can significantly reduce the time complexity of an algorithm.
- Similar problems to practice: Other problems that involve iterating through a list and keeping track of some form of maximum or minimum value to solve the problem efficiently.

**Mistakes to Avoid:**
- Common implementation errors: Failing to initialize variables correctly, not handling edge cases properly (e.g., an empty input list), and not validating inputs.
- Edge cases to watch for: Empty lists, lists with a single element, and lists where all elements are the same.
- Performance pitfalls: Using nested loops when a single pass will suffice, and not considering the implications of the algorithm's time and space complexity on large inputs.
- Testing considerations: Thoroughly testing the function with various inputs, including edge cases, to ensure it behaves as expected.