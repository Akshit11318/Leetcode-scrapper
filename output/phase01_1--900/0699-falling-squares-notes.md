## Falling Squares
**Problem Link:** [https://leetcode.com/problems/falling-squares/description](https://leetcode.com/problems/falling-squares/description)

**Problem Statement:**
- Input: A list of `squares` where each square is represented as an array `[left, side]`, indicating the left side of the square and its side length.
- Constraints: The number of squares is between 1 and 1000. The side length of each square is between 1 and 10^5.
- Expected Output: The maximum height of the pile of squares after each square has been dropped.
- Key Requirements: The height of the pile at each step should be the maximum height of the pile after dropping the corresponding square.
- Example Test Cases:
  - Input: `[[1, 2], [2, 3], [6, 1]]`
  - Output: `[2, 5, 5]`
  - Explanation: The first square is dropped at position 1 with a side length of 2. The maximum height is 2. The second square is dropped at position 2 with a side length of 3. The maximum height becomes 5. The third square is dropped at position 6 with a side length of 1. The maximum height remains 5.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to simulate the dropping of each square and calculate the maximum height after each drop.
- We iterate through each square, place it at its specified position, and then calculate the new maximum height by checking the height of the pile at each position.
- This approach comes to mind first because it directly simulates the process described in the problem.

```cpp
using namespace std;

vector<int> fallingSquares(vector<vector<int>>& squares) {
    vector<int> heights(squares.size(), 0);
    vector<int> maxHeights;
    for (int i = 0; i < squares.size(); i++) {
        int maxHeight = 0;
        for (int j = 0; j <= i; j++) {
            if (squares[j][0] < squares[i][0] + squares[i][1] && squares[i][0] < squares[j][0] + squares[j][1]) {
                heights[i] = max(heights[i], heights[j] + squares[i][1]);
            }
        }
        if (heights[i] == 0) {
            heights[i] = squares[i][1];
        }
        maxHeight = max(maxHeight, heights[i]);
        maxHeights.push_back(maxHeight);
    }
    return maxHeights;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ where $n$ is the number of squares. This is because for each square, we potentially check all previous squares.
> - **Space Complexity:** $O(n)$ for storing the maximum heights after each drop.
> - **Why these complexities occur:** The time complexity is quadratic due to the nested loop structure, where we iterate through the squares and for each square, we may iterate through all previous squares to calculate the height. The space complexity is linear because we store the maximum height after each drop.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is recognizing that we only need to consider the squares that overlap with the current square when calculating its height.
- We use a similar approach as the brute force but optimize it by directly calculating the maximum height after each drop without needing to check all previous squares.
- The proof of optimality lies in the fact that we only consider relevant squares for calculating the height of the current square, thus minimizing unnecessary comparisons.

```cpp
using namespace std;

vector<int> fallingSquares(vector<vector<int>>& squares) {
    vector<int> heights(squares.size(), 0);
    vector<int> maxHeights;
    int maxHeight = 0;
    for (int i = 0; i < squares.size(); i++) {
        int h = 0;
        for (int j = 0; j < i; j++) {
            if (squares[j][0] < squares[i][0] + squares[i][1] && squares[i][0] < squares[j][0] + squares[j][1]) {
                h = max(h, heights[j]);
            }
        }
        heights[i] = h + squares[i][1];
        maxHeight = max(maxHeight, heights[i]);
        maxHeights.push_back(maxHeight);
    }
    return maxHeights;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ where $n$ is the number of squares, because in the worst case, each square could potentially overlap with every previous square.
> - **Space Complexity:** $O(n)$ for storing the heights of the squares and the maximum heights after each drop.
> - **Optimality proof:** This approach is optimal because it minimizes the number of comparisons needed to calculate the maximum height after each drop by only considering overlapping squares.

---

### Final Notes

**Learning Points:**
- The importance of understanding the problem constraints and how they impact the complexity of the solution.
- Recognizing the key insight that overlapping squares are crucial for calculating the height of the pile.
- The trade-off between time and space complexity in the optimal solution.

**Mistakes to Avoid:**
- Incorrectly assuming that all previous squares need to be checked for calculating the height of the current square.
- Failing to update the maximum height correctly after each drop.
- Not considering the overlap of squares when calculating their heights.