## Tallest Billboard
**Problem Link:** https://leetcode.com/problems/tallest-billboard/description

**Problem Statement:**
- Input: A list of integers representing the width and height of each brick.
- Constraints: 
  - The length of the list is in the range [1, 1000].
  - The sum of the absolute values of the heights is less than 1000.
- Expected Output: The maximum height of the billboard.
- Key Requirements: The difference in height between the two columns must be less than or equal to 1.
- Edge Cases:
  - Empty list: return 0.
  - Single element: return the absolute value of the height.
- Example Test Cases:
  - Input: [[1,1],[1,1],[1,1]]
    - Output: 3
  - Input: [[1,2],[3,4],[5,6]]
    - Output: 4

---

### Brute Force Approach

**Explanation:**
- Generate all possible subsets of bricks.
- Calculate the total height and difference in height for each subset.
- Keep track of the maximum height where the difference is less than or equal to 1.

```cpp
int tallestBillboard(vector<vector<int>>& bricks) {
    int n = bricks.size();
    int max_height = 0;
    for (int mask = 0; mask < (1 << n); mask++) {
        int sum1 = 0, sum2 = 0;
        for (int i = 0; i < n; i++) {
            if ((mask >> i) & 1) {
                sum1 += bricks[i][1];
            } else if ((mask >> i) & 2) {
                sum2 += bricks[i][1];
            }
        }
        if (abs(sum1 - sum2) <= 1) {
            max_height = max(max_height, sum1);
        }
    }
    return max_height;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where n is the number of bricks. This is because we are generating all possible subsets.
> - **Space Complexity:** $O(1)$, as we are not using any extra space that scales with the input size.
> - **Why these complexities occur:** The brute force approach has exponential time complexity due to the generation of all possible subsets. The space complexity is constant because we are only using a fixed amount of space to store the maximum height.

---

### Optimal Approach (Required)

**Explanation:**
- Use a hashmap to store the differences in height and their corresponding maximum heights.
- Iterate through the bricks and update the hashmap accordingly.
- Keep track of the maximum height where the difference is less than or equal to 1.

```cpp
int tallestBillboard(vector<vector<int>>& bricks) {
    unordered_map<int, int> dp;
    dp[0] = 0;
    for (auto& b : bricks) {
        int x = b[0], y = b[1];
        unordered_map<int, int> temp;
        for (auto& p : dp) {
            int diff = p.first, height = p.second;
            temp[diff + y - x] = max(temp[diff + y - x], height + min(x, y));
            temp[diff] = max(temp[diff], height + y);
            temp[diff + x - y] = max(temp[diff + x - y], height + x);
        }
        dp = temp;
    }
    return dp[0];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot sum)$, where n is the number of bricks and sum is the sum of the absolute values of the heights.
> - **Space Complexity:** $O(sum)$, as we are using a hashmap to store the differences in height and their corresponding maximum heights.
> - **Optimality proof:** This approach is optimal because it uses dynamic programming to avoid redundant calculations and has a polynomial time complexity.

---

### Final Notes

**Learning Points:**
- The importance of using dynamic programming to avoid redundant calculations.
- How to use a hashmap to store and update the differences in height and their corresponding maximum heights.
- The need to consider all possible differences in height and their corresponding maximum heights.

**Mistakes to Avoid:**
- Not considering all possible differences in height and their corresponding maximum heights.
- Not using dynamic programming to avoid redundant calculations.
- Not using a hashmap to store and update the differences in height and their corresponding maximum heights.

---

Note: This problem can be solved using a more efficient approach with a time complexity of $O(n \cdot sum)$, where n is the number of bricks and sum is the sum of the absolute values of the heights. The optimal approach uses dynamic programming to avoid redundant calculations and has a polynomial time complexity.