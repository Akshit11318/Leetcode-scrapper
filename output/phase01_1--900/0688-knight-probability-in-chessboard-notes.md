## Knight Probability in Chessboard
**Problem Link:** https://leetcode.com/problems/knight-probability-in-chessboard/description

**Problem Statement:**
- Input format: `int n, int k, int row, int column`
- Constraints: `1 <= n <= 25`, `0 <= k <= 100`
- Expected output format: The probability that the knight will stay on the board after `k` moves.
- Key requirements and edge cases to consider: Handling out-of-bounds moves, calculating probabilities for each possible move.
- Example test cases with explanations: 
    - `n = 3, k = 2, row = 0, column = 0`: The knight can move to `(2,1)` or `(1,2)` and then move back to `(0,0)`, so the probability is `0.0625`.
    - `n = 1, k = 0, row = 0, column = 0`: The knight is already out of the board, so the probability is `0`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Simulate all possible moves of the knight and calculate the probability of staying on the board.
- Step-by-step breakdown of the solution:
    1. Define the possible moves of the knight.
    2. Simulate all possible moves for `k` steps.
    3. Calculate the probability of staying on the board.
- Why this approach comes to mind first: It is a straightforward and intuitive approach.

```cpp
double knightProbability(int n, int k, int row, int column) {
    // Define the possible moves of the knight
    vector<vector<int>> moves = {{-2, -1}, {-1, -2}, {1, -2}, {2, -1}, {-2, 1}, {-1, 2}, {1, 2}, {2, 1}};
    
    // Function to check if a position is on the board
    auto onBoard = [&](int x, int y) {
        return x >= 0 && x < n && y >= 0 && y < n;
    };
    
    // Function to simulate a move
    auto simulateMove = [&](int x, int y, int k) {
        if (k == 0) return 1;
        double count = 0;
        for (auto& move : moves) {
            int nx = x + move[0], ny = y + move[1];
            if (onBoard(nx, ny)) {
                count += simulateMove(nx, ny, k - 1);
            }
        }
        return count;
    };
    
    // Simulate all possible moves for k steps
    double total = pow(8, k);
    double count = simulateMove(row, column, k);
    
    // Calculate the probability of staying on the board
    return count / total;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(8^k)$, where $k$ is the number of moves. This is because we simulate all possible moves for $k$ steps.
> - **Space Complexity:** $O(k)$, where $k$ is the number of moves. This is because we use a recursive function to simulate the moves.
> - **Why these complexities occur:** The time complexity occurs because we simulate all possible moves, and the space complexity occurs because we use a recursive function.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Use dynamic programming to store the probabilities of staying on the board for each position.
- Detailed breakdown of the approach:
    1. Initialize a 2D array to store the probabilities of staying on the board for each position.
    2. Fill in the probabilities for the base case (i.e., $k = 0$).
    3. Use dynamic programming to fill in the probabilities for each position and each number of moves.
- Proof of optimality: This approach has a time complexity of $O(k \cdot n^2)$, which is optimal because we need to consider all possible positions and all possible numbers of moves.

```cpp
double knightProbability(int n, int k, int row, int column) {
    // Define the possible moves of the knight
    vector<vector<int>> moves = {{-2, -1}, {-1, -2}, {1, -2}, {2, -1}, {-2, 1}, {-1, 2}, {1, 2}, {2, 1}};
    
    // Function to check if a position is on the board
    auto onBoard = [&](int x, int y) {
        return x >= 0 && x < n && y >= 0 && y < n;
    };
    
    // Initialize a 2D array to store the probabilities of staying on the board for each position
    vector<vector<double>> dp(n, vector<double>(n, 0));
    
    // Fill in the probabilities for the base case (i.e., k = 0)
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            dp[i][j] = 1;
        }
    }
    
    // Use dynamic programming to fill in the probabilities for each position and each number of moves
    for (int step = 1; step <= k; step++) {
        vector<vector<double>> temp(n, vector<double>(n, 0));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                for (auto& move : moves) {
                    int ni = i + move[0], nj = j + move[1];
                    if (onBoard(ni, nj)) {
                        temp[i][j] += dp[ni][nj] / 8;
                    }
                }
            }
        }
        dp = temp;
    }
    
    // Return the probability of staying on the board for the given position and number of moves
    return dp[row][column];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(k \cdot n^2)$, where $k$ is the number of moves and $n$ is the size of the board. This is because we use dynamic programming to fill in the probabilities for each position and each number of moves.
> - **Space Complexity:** $O(n^2)$, where $n$ is the size of the board. This is because we use a 2D array to store the probabilities of staying on the board for each position.
> - **Optimality proof:** This approach has a time complexity of $O(k \cdot n^2)$, which is optimal because we need to consider all possible positions and all possible numbers of moves.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, simulation.
- Problem-solving patterns identified: Using dynamic programming to store probabilities, simulating all possible moves.
- Optimization techniques learned: Using dynamic programming to reduce time complexity.
- Similar problems to practice: Other dynamic programming problems, such as the Fibonacci sequence or the longest common subsequence.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for out-of-bounds moves, not initializing the 2D array correctly.
- Edge cases to watch for: Handling the base case (i.e., $k = 0$), handling the case where the knight is already out of the board.
- Performance pitfalls: Not using dynamic programming, simulating all possible moves without using dynamic programming.
- Testing considerations: Testing the function with different inputs, including edge cases and large inputs.