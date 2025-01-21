## Operations on Tree

**Problem Link:** https://leetcode.com/problems/operations-on-tree/description

**Problem Statement:**
- Input format: `class Tree` with methods `insert(val)`, `getMax()`, `remove(val)`, and `contains(val)`
- Expected output format: N/A, implement class methods
- Key requirements and edge cases to consider: 
    - Handling duplicate values
    - Removing a value that doesn't exist
    - Getting the maximum value in an empty tree
- Example test cases with explanations:
    - `tree.insert(5)`, `tree.insert(3)`, `tree.insert(7)`, `tree.getMax()`, `tree.remove(3)`, `tree.contains(5)`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Use a basic data structure like a `vector` to store the values and perform operations on it.
- Step-by-step breakdown of the solution:
    1. Insert: Append the value to the end of the vector.
    2. GetMax: Iterate through the vector to find the maximum value.
    3. Remove: Iterate through the vector to find the value and remove it.
    4. Contains: Iterate through the vector to check if the value exists.
- Why this approach comes to mind first: It's a simple and straightforward approach, but not efficient for large inputs.

```cpp
class Tree {
public:
    vector<int> values;

    void insert(int val) {
        values.push_back(val);
    }

    int getMax() {
        if (values.empty()) {
            return -1; // or throw an exception
        }
        int maxVal = values[0];
        for (int i = 1; i < values.size(); i++) {
            if (values[i] > maxVal) {
                maxVal = values[i];
            }
        }
        return maxVal;
    }

    void remove(int val) {
        for (int i = 0; i < values.size(); i++) {
            if (values[i] == val) {
                values.erase(values.begin() + i);
                return;
            }
        }
    }

    bool contains(int val) {
        for (int i = 0; i < values.size(); i++) {
            if (values[i] == val) {
                return true;
            }
        }
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ for `insert`, $O(n)$ for `getMax`, $O(n)$ for `remove`, and $O(n)$ for `contains`, where $n$ is the number of values in the tree.
> - **Space Complexity:** $O(n)$ for storing the values.
> - **Why these complexities occur:** The brute force approach uses a linear search for most operations, resulting in high time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a `set` data structure to store the values, which allows for efficient insertion, removal, and searching.
- Detailed breakdown of the approach:
    1. Insert: Use the `insert` method of the set.
    2. GetMax: Use the `rbegin` method of the set to get the maximum value.
    3. Remove: Use the `erase` method of the set to remove the value.
    4. Contains: Use the `find` method of the set to check if the value exists.
- Proof of optimality: The set data structure provides an average time complexity of $O(\log n)$ for most operations, making it the most efficient solution.

```cpp
class Tree {
public:
    set<int> values;

    void insert(int val) {
        values.insert(val);
    }

    int getMax() {
        if (values.empty()) {
            return -1; // or throw an exception
        }
        return *values.rbegin();
    }

    void remove(int val) {
        values.erase(val);
    }

    bool contains(int val) {
        return values.find(val) != values.end();
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log n)$ for `insert`, $O(1)$ for `getMax`, $O(\log n)$ for `remove`, and $O(\log n)$ for `contains`, where $n$ is the number of values in the tree.
> - **Space Complexity:** $O(n)$ for storing the values.
> - **Optimality proof:** The set data structure provides the most efficient solution, with a time complexity that is optimal for most operations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a set data structure for efficient insertion, removal, and searching.
- Problem-solving patterns identified: Choosing the right data structure for the problem.
- Optimization techniques learned: Using a set instead of a vector for efficient operations.
- Similar problems to practice: Implementing a stack or queue using a set.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for empty sets before accessing elements.
- Edge cases to watch for: Handling duplicate values, removing a value that doesn't exist.
- Performance pitfalls: Using a vector instead of a set for large inputs.
- Testing considerations: Testing the implementation with different inputs and edge cases.