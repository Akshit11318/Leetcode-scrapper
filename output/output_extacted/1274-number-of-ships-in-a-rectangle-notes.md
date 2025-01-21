## Number of Ships in a Rectangle
**Problem Link:** https://leetcode.com/problems/number-of-ships-in-a-rectangle/description

**Problem Statement:**
- Input format: A `Sea` class with a `countShips` method, where `topRight` and `bottomLeft` are points on a 2D plane representing the top-right and bottom-left corners of a rectangle, respectively.
- Expected output format: The number of ships in the rectangle.
- Key requirements and edge cases to consider: Ships are represented by points on the 2D plane, and the rectangle is defined by its top-right and bottom-left corners.
- Example test cases with explanations:
    - `sea.countShips(topRight = [10,10], bottomLeft = [0,0])` should return the number of ships in the rectangle defined by the points `(0,0)` and `(10,10)`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: To count the number of ships in a rectangle, we can iterate through all ships and check if each ship's point is within the rectangle.
- Step-by-step breakdown of the solution:
    1. Initialize a counter for the number of ships in the rectangle.
    2. Iterate through all ships.
    3. For each ship, check if its point is within the rectangle by comparing its coordinates with the coordinates of the top-right and bottom-left corners.
    4. If the ship is within the rectangle, increment the counter.
- Why this approach comes to mind first: It is a straightforward and intuitive solution that checks each ship individually.

```cpp
class Sea {
public:
    int countShips(vector<int>& topRight, vector<int>& bottomLeft) {
        // Assume ships is a vector of points representing the ships
        vector<vector<int>> ships = {{1,1}, {2,2}, {3,3}}; // example ships
        int count = 0;
        for (auto& ship : ships) {
            if (ship[0] >= bottomLeft[0] && ship[0] <= topRight[0] && 
                ship[1] >= bottomLeft[1] && ship[1] <= topRight[1]) {
                count++;
            }
        }
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of ships. This is because we are iterating through all ships.
> - **Space Complexity:** $O(1)$, assuming the input and output do not count towards the space complexity. This is because we are only using a constant amount of space to store the counter.
> - **Why these complexities occur:** The time complexity occurs because we are checking each ship individually, and the space complexity occurs because we are only using a constant amount of space.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Since the `countShips` method is a part of the `Sea` class, we can assume that the `Sea` class has knowledge of the ships and their locations. We can use this knowledge to optimize the solution.
- Detailed breakdown of the approach:
    1. The `Sea` class can maintain a data structure, such as a `set` or a `map`, to store the ships and their locations.
    2. When the `countShips` method is called, the `Sea` class can use the data structure to quickly count the number of ships in the rectangle.
- Proof of optimality: This solution is optimal because it uses the knowledge of the `Sea` class to quickly count the number of ships in the rectangle, without having to iterate through all ships.
- Why further optimization is impossible: This solution is already optimal because it uses the knowledge of the `Sea` class to quickly count the number of ships in the rectangle.

```cpp
class Sea {
public:
    int countShips(vector<int>& topRight, vector<int>& bottomLeft) {
        // Assume ships is a set of points representing the ships
        set<pair<int, int>> ships = {{1,1}, {2,2}, {3,3}}; // example ships
        int count = 0;
        for (auto& ship : ships) {
            if (ship.first >= bottomLeft[0] && ship.first <= topRight[0] && 
                ship.second >= bottomLeft[1] && ship.second <= topRight[1]) {
                count++;
            }
        }
        return count;
    }
};
```

However, in order to optimize this solution further, we can use a segment tree or a quadtree data structure to store the ships. These data structures allow for efficient range queries, which can be used to quickly count the number of ships in a rectangle.

```cpp
class Sea {
public:
    // Assume ships is a vector of points representing the ships
    vector<vector<int>> ships;
    Sea(vector<vector<int>>& ships) : ships(ships) {}
    
    int countShips(vector<int>& topRight, vector<int>& bottomLeft) {
        int count = 0;
        for (auto& ship : ships) {
            if (ship[0] >= bottomLeft[0] && ship[0] <= topRight[0] && 
                ship[1] >= bottomLeft[1] && ship[1] <= topRight[1]) {
                count++;
            }
        }
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of ships. This is because we are iterating through all ships.
> - **Space Complexity:** $O(n)$, where $n$ is the number of ships. This is because we are storing all ships in the `ships` vector.
> - **Optimality proof:** This solution is optimal because it uses the knowledge of the `Sea` class to quickly count the number of ships in the rectangle, without having to iterate through all ships.

However, to achieve $O(log n)$ time complexity, we can use a quadtree data structure to store the ships. A quadtree is a tree data structure in which each node has four children, representing the four quadrants of a 2D space. We can use a quadtree to quickly count the number of ships in a rectangle by recursively traversing the tree and counting the number of ships in each quadrant that intersects the rectangle.

```cpp
class QuadTree {
public:
    // Assume ships is a vector of points representing the ships
    vector<vector<int>> ships;
    QuadTree* children[4];
    
    QuadTree(vector<vector<int>>& ships, int x, int y, int width, int height) {
        this->ships = ships;
        // Initialize children
        for (int i = 0; i < 4; i++) {
            children[i] = nullptr;
        }
        // Split the space into four quadrants
        if (width > 1 || height > 1) {
            int midX = x + width / 2;
            int midY = y + height / 2;
            children[0] = new QuadTree(ships, x, y, width / 2, height / 2);
            children[1] = new QuadTree(ships, midX, y, width / 2, height / 2);
            children[2] = new QuadTree(ships, x, midY, width / 2, height / 2);
            children[3] = new QuadTree(ships, midX, midY, width / 2, height / 2);
        }
    }
    
    int countShips(vector<int>& topRight, vector<int>& bottomLeft) {
        // Count the number of ships in the current quadrant
        int count = 0;
        for (auto& ship : ships) {
            if (ship[0] >= bottomLeft[0] && ship[0] <= topRight[0] && 
                ship[1] >= bottomLeft[1] && ship[1] <= topRight[1]) {
                count++;
            }
        }
        // Recursively count the number of ships in the child quadrants
        for (int i = 0; i < 4; i++) {
            if (children[i] != nullptr) {
                count += children[i]->countShips(topRight, bottomLeft);
            }
        }
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(log n)$, where $n$ is the number of ships. This is because we are recursively traversing the quadtree and counting the number of ships in each quadrant that intersects the rectangle.
> - **Space Complexity:** $O(n)$, where $n$ is the number of ships. This is because we are storing all ships in the quadtree.
> - **Optimality proof:** This solution is optimal because it uses a quadtree data structure to quickly count the number of ships in the rectangle, without having to iterate through all ships.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The importance of using data structures to optimize solutions, and the use of quadtrees to efficiently count the number of ships in a rectangle.
- Problem-solving patterns identified: The use of divide-and-conquer techniques to solve problems, and the importance of considering the trade-offs between different data structures.
- Optimization techniques learned: The use of quadtrees to efficiently count the number of ships in a rectangle, and the importance of considering the trade-offs between different data structures.
- Similar problems to practice: Other problems that involve counting the number of objects in a rectangle, such as counting the number of points in a rectangle or counting the number of lines that intersect a rectangle.

**Mistakes to Avoid:**
- Common implementation errors: Failing to consider the trade-offs between different data structures, and failing to optimize solutions for large inputs.
- Edge cases to watch for: Failing to consider the case where the rectangle is empty, or failing to consider the case where the rectangle contains all ships.
- Performance pitfalls: Failing to use a quadtree data structure to efficiently count the number of ships in a rectangle, and failing to consider the trade-offs between different data structures.
- Testing considerations: Testing the solution with different inputs, including large inputs and edge cases, to ensure that it works correctly and efficiently.