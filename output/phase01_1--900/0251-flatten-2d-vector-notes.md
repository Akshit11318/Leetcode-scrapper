## Flattening a 2D Vector

**Problem Link:** https://leetcode.com/problems/flatten-2d-vector/description

**Problem Statement:**
- Input format and constraints: The input is a 2D vector of integers, and the constraints are that the vector can be empty, and the inner vectors can also be empty.
- Expected output format: The output should be a class with `next()`, `hasNext()`, and `flatten(vector<vector<int>> vec)` methods.
- Key requirements and edge cases to consider: The class should be able to handle empty vectors and inner vectors, and the `next()` and `hasNext()` methods should work correctly.
- Example test cases with explanations:
  - `vector<vector<int>> vec = {{1,2}, {3}, {4,5,6}};` The output should be `1, 2, 3, 4, 5, 6`.
  - `vector<vector<int>> vec = {{1,2}, {}, {3}};` The output should be `1, 2, 3`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Create a class with the required methods, and in the `flatten` method, create a new 1D vector by iterating over the 2D vector.
- Step-by-step breakdown of the solution:
  1. Create a new 1D vector.
  2. Iterate over the 2D vector and add all elements to the 1D vector.
  3. Implement the `next()` and `hasNext()` methods to work with the 1D vector.
- Why this approach comes to mind first: This is the most straightforward way to solve the problem, and it works, but it may not be the most efficient.

```cpp
class Vector2D {
public:
    vector<int> vec;
    int index = 0;

    Vector2D(vector<vector<int>>& vec) {
        for (auto v : vec) {
            for (auto i : v) {
                this->vec.push_back(i);
            }
        }
    }

    int next() {
        return vec[index++];
    }

    bool hasNext() {
        return index < vec.size();
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the number of inner vectors and $m$ is the average size of the inner vectors, because we iterate over all elements in the 2D vector.
> - **Space Complexity:** $O(n \cdot m)$ because we create a new 1D vector with all elements from the 2D vector.
> - **Why these complexities occur:** These complexities occur because we need to iterate over all elements in the 2D vector to create the 1D vector.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of creating a new 1D vector, we can use two pointers to keep track of the current inner vector and the current element in that vector.
- Detailed breakdown of the approach:
  1. Initialize two pointers, one for the current inner vector and one for the current element in that vector.
  2. In the `hasNext()` method, check if the current element is within the bounds of the current inner vector. If not, move to the next inner vector.
  3. In the `next()` method, return the current element and move to the next element.
- Proof of optimality: This solution is optimal because we only iterate over the elements that are actually needed, and we don't create any extra data structures.

```cpp
class Vector2D {
public:
    vector<vector<int>>& vec;
    int row = 0;
    int col = 0;

    Vector2D(vector<vector<int>>& vec) : vec(vec) {}

    int next() {
        int val = vec[row][col];
        col++;
        return val;
    }

    bool hasNext() {
        while (row < vec.size() && col == vec[row].size()) {
            row++;
            col = 0;
        }
        return row < vec.size();
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for the `next()` method and $O(n)$ for the `hasNext()` method in the worst case where we need to move to the next inner vector, where $n$ is the number of inner vectors.
> - **Space Complexity:** $O(1)$ because we only use a constant amount of space to store the two pointers.
> - **Optimality proof:** This solution is optimal because we only iterate over the elements that are actually needed, and we don't create any extra data structures.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Two pointers, iteration over 2D vectors.
- Problem-solving patterns identified: Using two pointers to keep track of the current element in a 2D vector.
- Optimization techniques learned: Avoiding the creation of extra data structures.
- Similar problems to practice: Problems that involve iterating over 2D vectors or using two pointers.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for empty inner vectors, not handling the case where the current element is out of bounds.
- Edge cases to watch for: Empty vectors, inner vectors with different sizes.
- Performance pitfalls: Creating extra data structures that are not needed.
- Testing considerations: Testing with different input sizes and edge cases.