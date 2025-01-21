## Filling Bookcase Shelves
**Problem Link:** [https://leetcode.com/problems/filling-bookcase-shelves/description](https://leetcode.com/problems/filling-bookcase-shelves/description)

**Problem Statement:**
- Input: `books` (vector of pairs representing the width and height of each book), `shelf_width` (the width of the shelf)
- Constraints: Each book can be placed on a shelf, and books on a shelf must be next to each other.
- Expected Output: The minimum possible height of the shelves.
- Key Requirements: The total width of the books on a shelf must not exceed `shelf_width`.
- Example Test Cases:
    - Input: `books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]]`, `shelf_width = 4`
      Output: `6`
    - Input: `books = [[1,1]]`, `shelf_width = 1`
      Output: `1`

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves trying all possible combinations of placing books on shelves and calculating the total height of the shelves for each combination.
- This approach is a straightforward application of the concept of recursion and backtracking.

```cpp
#include <vector>
using namespace std;

int min_height(vector<vector<int>>& books, int shelf_width) {
    int n = books.size();
    vector<int> dp(n + 1, INT_MAX);
    dp[0] = 0;
    
    for (int i = 1; i <= n; i++) {
        int width = 0, height = 0;
        for (int j = i - 1; j >= 0; j--) {
            width += books[j][0];
            if (width > shelf_width) break;
            height = max(height, books[j][1]);
            dp[i] = min(dp[i], dp[j] + height);
        }
    }
    
    return dp[n];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of books. This is because we have two nested loops that iterate over the books.
> - **Space Complexity:** $O(n)$, where $n$ is the number of books. This is because we use a dynamic programming array of size $n + 1$.
> - **Why these complexities occur:** The time complexity is due to the nested loops, and the space complexity is due to the dynamic programming array.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is using dynamic programming to store the minimum height of the shelves for each subproblem.
- We use a dynamic programming array `dp` where `dp[i]` represents the minimum height of the shelves for the first `i` books.
- We iterate over the books and for each book, we try to place it on the current shelf or on a new shelf.
- We update the `dp` array with the minimum height of the shelves for each subproblem.

```cpp
#include <vector>
#include <climits>
using namespace std;

int minHeightShelves(vector<vector<int>>& books, int shelf_width) {
    int n = books.size();
    vector<int> dp(n + 1, INT_MAX);
    dp[0] = 0;
    
    for (int i = 1; i <= n; i++) {
        int width = 0, height = 0;
        for (int j = i; j >= 1; j--) {
            width += books[j - 1][0];
            if (width > shelf_width) break;
            height = max(height, books[j - 1][1]);
            dp[i] = min(dp[i], dp[j - 1] + height);
        }
    }
    
    return dp[n];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of books. This is because we have two nested loops that iterate over the books.
> - **Space Complexity:** $O(n)$, where $n$ is the number of books. This is because we use a dynamic programming array of size $n + 1$.
> - **Optimality proof:** This is the optimal solution because we use dynamic programming to store the minimum height of the shelves for each subproblem, and we try all possible combinations of placing books on shelves.

---

### Final Notes

**Learning Points:**
- The key algorithmic concept demonstrated is dynamic programming.
- The problem-solving pattern identified is using dynamic programming to solve optimization problems.
- The optimization technique learned is using a dynamic programming array to store the minimum height of the shelves for each subproblem.

**Mistakes to Avoid:**
- A common implementation error is not initializing the dynamic programming array correctly.
- An edge case to watch for is when the width of a book is greater than the shelf width.
- A performance pitfall is using a naive recursive approach that does not use dynamic programming.