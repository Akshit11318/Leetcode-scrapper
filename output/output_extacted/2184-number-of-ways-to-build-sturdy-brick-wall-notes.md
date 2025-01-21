## Number of Ways to Build Sturdy Brick Wall

**Problem Link:** https://leetcode.com/problems/number-of-ways-to-build-sturdy-brick-wall/description

**Problem Statement:**
- Input format and constraints: The input consists of two integers, `width` and `height`, where `width` represents the width of the wall and `height` represents the number of layers. The wall is built using bricks of different lengths, and the goal is to find the number of ways to build a sturdy brick wall.
- Expected output format: The output should be an integer representing the number of ways to build a sturdy brick wall.
- Key requirements and edge cases to consider: The wall must be built using bricks of different lengths, and each layer must be sturdy, meaning that it must not have any gaps.
- Example test cases with explanations:
  - For `width = 10` and `height = 2`, the output should be `12`, because there are 12 ways to build a sturdy brick wall with a width of 10 and a height of 2.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to try all possible combinations of bricks to build the wall.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of bricks for each layer.
  2. Check if each combination is sturdy.
  3. Count the number of sturdy combinations for each layer.
  4. Multiply the number of sturdy combinations for each layer to get the total number of ways to build the wall.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it is not efficient because it has a high time complexity.

```cpp
class Solution {
public:
    int buildWall(int width, int height) {
        vector<int> bricks = {1, 2, 3, 4};
        int count = 0;
        vector<vector<int>> layers(height);
        buildWallHelper(width, height, bricks, layers, count, 0);
        return count;
    }

    void buildWallHelper(int width, int height, vector<int> &bricks, vector<vector<int>> &layers, int &count, int layerIndex) {
        if (layerIndex == height) {
            count++;
            return;
        }
        vector<int> combination;
        buildWallHelperRecursive(width, bricks, combination, layers, count, layerIndex);
    }

    void buildWallHelperRecursive(int width, vector<int> &bricks, vector<int> &combination, vector<vector<int>> &layers, int &count, int layerIndex) {
        if (width == 0) {
            layers[layerIndex] = combination;
            buildWallHelper(width, layers.size(), bricks, layers, count, layerIndex + 1);
            return;
        }
        for (int brick : bricks) {
            if (width - brick >= 0) {
                combination.push_back(brick);
                buildWallHelperRecursive(width - brick, bricks, combination, layers, count, layerIndex);
                combination.pop_back();
            }
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(4^{width \times height})$, because in the worst case, we need to try all possible combinations of bricks for each layer.
> - **Space Complexity:** $O(width \times height)$, because we need to store the combinations for each layer.
> - **Why these complexities occur:** The high time complexity occurs because we are trying all possible combinations of bricks for each layer, and the space complexity occurs because we need to store the combinations for each layer.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use dynamic programming to store the number of ways to build a sturdy brick wall for each width and height.
- Detailed breakdown of the approach:
  1. Create a 2D array `dp` where `dp[i][j]` represents the number of ways to build a sturdy brick wall with a width of `i` and a height of `j`.
  2. Initialize `dp[0][0] = 1`, because there is one way to build a sturdy brick wall with a width of 0 and a height of 0.
  3. For each `i` from 1 to `width`, and for each `j` from 1 to `height`, calculate `dp[i][j]` by summing up the number of ways to build a sturdy brick wall with a width of `i - brick` and a height of `j - 1`, where `brick` ranges from 1 to 4.
- Proof of optimality: This approach is optimal because it uses dynamic programming to store the number of ways to build a sturdy brick wall for each width and height, which avoids redundant calculations and reduces the time complexity.

```cpp
class Solution {
public:
    int buildWall(int width, int height) {
        vector<int> bricks = {1, 2, 3, 4};
        vector<vector<int>> dp(height + 1, vector<int>(width + 1));
        dp[0][0] = 1;
        for (int i = 1; i <= height; i++) {
            for (int j = 1; j <= width; j++) {
                for (int brick : bricks) {
                    if (j - brick >= 0) {
                        dp[i][j] += dp[i - 1][j - brick];
                    }
                }
            }
        }
        return dp[height][width];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(width \times height \times 4)$, because we need to calculate `dp[i][j]` for each `i` and `j`, and for each `brick`.
> - **Space Complexity:** $O(width \times height)$, because we need to store the `dp` array.
> - **Optimality proof:** This approach is optimal because it uses dynamic programming to store the number of ways to build a sturdy brick wall for each width and height, which avoids redundant calculations and reduces the time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: dynamic programming, memoization.
- Problem-solving patterns identified: using dynamic programming to store the number of ways to build a sturdy brick wall for each width and height.
- Optimization techniques learned: avoiding redundant calculations by using dynamic programming.
- Similar problems to practice: problems that involve building or constructing something, such as building a bridge or a house.

**Mistakes to Avoid:**
- Common implementation errors: not initializing the `dp` array correctly, not handling the base case correctly.
- Edge cases to watch for: when `width` or `height` is 0, when `width` or `height` is negative.
- Performance pitfalls: not using dynamic programming, using a brute force approach.
- Testing considerations: testing with different inputs, such as different `width` and `height` values, testing with edge cases.