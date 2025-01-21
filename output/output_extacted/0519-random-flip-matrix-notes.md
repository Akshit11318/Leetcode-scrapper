## Random Flip Matrix
**Problem Link:** [https://leetcode.com/problems/random-flip-matrix/description](https://leetcode.com/problems/random-flip-matrix/description)

**Problem Statement:**
- Input format: An integer `n`, representing the size of the matrix.
- Constraints: `1 <= n <= 100`
- Expected output format: A class with methods `flip()` and `reset()`.
- Key requirements and edge cases to consider:
  - `flip()`: Returns a list of `[row, col]` representing a random available cell in the matrix.
  - `reset()`: Resets the matrix to its original state.
- Example test cases with explanations:
  - `RandomFlipMatrix flip(2)`: Initializes a 2x2 matrix.
  - `flip.flip()`: Returns a random available cell, e.g., `[0, 0]`.
  - `flip.flip()`: Returns another random available cell, e.g., `[1, 1]`.
  - `flip.reset()`: Resets the matrix to its original state.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Create a 2D matrix and mark cells as flipped or not.
- Step-by-step breakdown of the solution:
  1. Initialize a 2D matrix of size `n x n`.
  2. Create a set to store the flipped cells.
  3. In the `flip()` method, iterate over the matrix to find an available cell.
  4. Mark the cell as flipped and add it to the set.
  5. In the `reset()` method, clear the set and reset the matrix.

```cpp
class RandomFlipMatrix {
public:
    RandomFlipMatrix(int n) : n(n) {}

    vector<int> flip() {
        vector<int> result;
        while (true) {
            int row = rand() % n;
            int col = rand() % n;
            if (flipped.find({row, col}) == flipped.end()) {
                flipped.insert({row, col});
                result = {row, col};
                break;
            }
        }
        return result;
    }

    void reset() {
        flipped.clear();
    }

private:
    int n;
    set<pair<int, int>> flipped;
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ in the worst case, where we need to iterate over the entire matrix to find an available cell.
> - **Space Complexity:** $O(n^2)$, where we store the flipped cells in a set.
> - **Why these complexities occur:** The brute force approach requires iterating over the matrix to find an available cell, leading to high time and space complexities.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Use a vector to store the available cells and shuffle it to ensure randomness.
- Detailed breakdown of the approach:
  1. Initialize a vector to store the available cells.
  2. In the `flip()` method, remove the last cell from the vector and return it.
  3. In the `reset()` method, reinitialize the vector with all cells.
- Proof of optimality: This approach ensures $O(1)$ time complexity for the `flip()` method and $O(n^2)$ time complexity for the `reset()` method.

```cpp
class RandomFlipMatrix {
public:
    RandomFlipMatrix(int n) : n(n) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cells.push_back({i, j});
            }
        }
        shuffle(cells.begin(), cells.end(), rng);
    }

    vector<int> flip() {
        vector<int> result = {cells.back().first, cells.back().second};
        cells.pop_back();
        return result;
    }

    void reset() {
        cells.clear();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cells.push_back({i, j});
            }
        }
        shuffle(cells.begin(), cells.end(), rng);
    }

private:
    int n;
    vector<pair<int, int>> cells;
    random_device rd;
    mt19937 rng{rd()};
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for the `flip()` method and $O(n^2)$ for the `reset()` method.
> - **Space Complexity:** $O(n^2)$, where we store the available cells in a vector.
> - **Optimality proof:** This approach ensures optimal time complexity for the `flip()` method and efficient space usage.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Randomization, shuffling, and vector operations.
- Problem-solving patterns identified: Using a vector to store available cells and shuffling it to ensure randomness.
- Optimization techniques learned: Reducing time complexity by using a vector and shuffling it.

**Mistakes to Avoid:**
- Common implementation errors: Not shuffling the vector properly or not checking for available cells.
- Edge cases to watch for: Handling the case where the matrix is fully flipped.
- Performance pitfalls: Using a brute force approach with high time complexity.
- Testing considerations: Testing the `flip()` and `reset()` methods with different inputs and edge cases.