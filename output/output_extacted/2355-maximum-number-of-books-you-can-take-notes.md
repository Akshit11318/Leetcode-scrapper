## Maximum Number of Books You Can Take
**Problem Link:** https://leetcode.com/problems/maximum-number-of-books-you-can-take/description

**Problem Statement:**
- Input format: You are given a 2D integer array `books` where `books[i] = [thickness, height]` represents a book.
- Constraints: The number of books is between 1 and 10^5.
- Expected output format: Return the maximum number of books you can take.
- Key requirements and edge cases to consider: The total thickness of the books must not exceed `shelf_width`, and the height of the books must be in non-decreasing order.
- Example test cases with explanations:
  - `books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]]`, `shelf_width = 4` returns `9`.
  - `books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]]`, `shelf_width = 3` returns `5`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of books to find the maximum number that can fit on the shelf.
- Step-by-step breakdown of the solution:
  1. Generate all possible subsets of books.
  2. For each subset, calculate the total thickness and check if it is within the shelf width.
  3. If it is, update the maximum number of books if the current subset has more books.
- Why this approach comes to mind first: It is a straightforward way to solve the problem by trying all possibilities.

```cpp
class Solution {
public:
    int maxHeightShelves(vector<vector<int>>& books, int shelf_width) {
        int n = books.size();
        vector<int> dp(n + 1, 0);
        dp[0] = 0;
        for (int i = 1; i <= n; i++) {
            int max_height = 0;
            int max_width = 0;
            for (int j = i - 1; j >= 0; j--) {
                max_width += books[j][0];
                if (max_width > shelf_width) break;
                max_height = max(max_height, books[j][1]);
                dp[i] = max(dp[i], dp[j] + max_height);
            }
        }
        return dp[n];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ where $n$ is the number of books. This is because we have two nested loops.
> - **Space Complexity:** $O(n)$ where $n$ is the number of books. This is because we use a dynamic programming array of size $n + 1$.
> - **Why these complexities occur:** The time complexity occurs because we are trying all possible subsets of books, and the space complexity occurs because we are storing the maximum height for each subset.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use dynamic programming to store the maximum height for each prefix of books and update it as we add more books.
- Detailed breakdown of the approach:
  1. Initialize a dynamic programming array `dp` of size `n + 1` where `dp[i]` represents the maximum height for the first `i` books.
  2. For each book, calculate the maximum height if we add it to the current shelf and update `dp[i]` accordingly.
- Proof of optimality: This approach is optimal because it considers all possible ways to place the books on the shelves and uses the maximum height for each prefix to make the decision.

```cpp
class Solution {
public:
    int maxHeightShelves(vector<vector<int>>& books, int shelf_width) {
        int n = books.size();
        vector<int> dp(n + 1, 0);
        dp[0] = 0;
        for (int i = 1; i <= n; i++) {
            int max_height = books[i - 1][1];
            int width = books[i - 1][0];
            dp[i] = dp[i - 1] + max_height;
            for (int j = i - 1; j >= 1; j--) {
                if (width + books[j - 1][0] > shelf_width) break;
                width += books[j - 1][0];
                max_height = max(max_height, books[j - 1][1]);
                dp[i] = max(dp[i], dp[j - 1] + max_height);
            }
        }
        return dp[n];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ where $n$ is the number of books. This is because we have two nested loops.
> - **Space Complexity:** $O(n)$ where $n$ is the number of books. This is because we use a dynamic programming array of size $n + 1$.
> - **Optimality proof:** This approach is optimal because it considers all possible ways to place the books on the shelves and uses the maximum height for each prefix to make the decision.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, prefix sums.
- Problem-solving patterns identified: Using dynamic programming to store the maximum height for each prefix and updating it as we add more books.
- Optimization techniques learned: Using a dynamic programming array to store the maximum height for each prefix.
- Similar problems to practice: Other dynamic programming problems, such as the 0/1 knapsack problem.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the dynamic programming array correctly, not updating the maximum height correctly.
- Edge cases to watch for: Books with zero thickness or height, shelves with zero width.
- Performance pitfalls: Using a brute force approach, not using dynamic programming to store the maximum height for each prefix.
- Testing considerations: Test the function with different inputs, including edge cases, to ensure it is working correctly.