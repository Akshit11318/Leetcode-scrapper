## Number Container System Design

**Problem Link:** https://leetcode.com/problems/design-a-number-container-system/description

**Problem Statement:**
- Input format and constraints: Design a number container system with two operations: `change` and `findPrefix`. The `change` operation takes a number and a new index, and the `findPrefix` operation takes a number and returns the index where this number is currently located.
- Expected output format: Return the index where the number is currently located.
- Key requirements and edge cases to consider: 
  - A number can be moved multiple times, so the index may change.
  - A number may not exist in the system.
- Example test cases with explanations:
  - `change(1, 0)`: Move the number 1 to index 0.
  - `findPrefix(1)`: Return the index where the number 1 is currently located.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Use a `vector` to store the numbers and their indices. When `change` is called, update the index of the number in the `vector`. When `findPrefix` is called, iterate over the `vector` to find the index of the number.
- Step-by-step breakdown of the solution:
  1. Create a `vector` to store the numbers and their indices.
  2. Implement the `change` operation:
    - Iterate over the `vector` to find the current index of the number.
    - Update the index of the number in the `vector`.
  3. Implement the `findPrefix` operation:
    - Iterate over the `vector` to find the index of the number.
    - Return the index of the number.
- Why this approach comes to mind first: It is a simple and straightforward solution that uses basic data structures.

```cpp
class NumberContainer {
public:
    vector<pair<int, int>> nums;
    NumberContainer() {}

    void change(int index, int number) {
        for (auto& p : nums) {
            if (p.first == number) {
                p.second = index;
                return;
            }
        }
        nums.push_back({number, index});
    }

    int findPrefix(int number) {
        for (auto& p : nums) {
            if (p.first == number) {
                return p.second;
            }
        }
        return -1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of numbers in the system. This is because we are iterating over the `vector` in both `change` and `findPrefix` operations.
> - **Space Complexity:** $O(n)$, where $n$ is the number of numbers in the system. This is because we are storing all numbers in the `vector`.
> - **Why these complexities occur:** The `vector` operations (iteration and insertion) cause these complexities.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a `map` to store the numbers and their indices. This allows for $O(1)$ lookups and updates.
- Detailed breakdown of the approach:
  1. Create a `map` to store the numbers and their indices.
  2. Implement the `change` operation:
    - Update the index of the number in the `map`.
  3. Implement the `findPrefix` operation:
    - Return the index of the number from the `map`.
- Proof of optimality: The $O(1)$ lookup and update operations in the `map` make this solution optimal.

```cpp
class NumberContainer {
public:
    unordered_map<int, int> numToIndex;
    NumberContainer() {}

    void change(int index, int number) {
        numToIndex[number] = index;
    }

    int findPrefix(int number) {
        if (numToIndex.find(number) != numToIndex.end()) {
            return numToIndex[number];
        }
        return -1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, where $n$ is the number of numbers in the system. This is because we are using $O(1)$ lookup and update operations in the `map`.
> - **Space Complexity:** $O(n)$, where $n$ is the number of numbers in the system. This is because we are storing all numbers in the `map`.
> - **Optimality proof:** The $O(1)$ lookup and update operations in the `map` make this solution optimal.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a `map` for $O(1)$ lookups and updates.
- Problem-solving patterns identified: Using the right data structure to solve a problem efficiently.
- Optimization techniques learned: Using a `map` instead of a `vector` to reduce the time complexity.
- Similar problems to practice: Problems that involve frequent lookups and updates, such as a phonebook or a database.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle edge cases, such as an empty `map`.
- Edge cases to watch for: When the number is not in the system, or when the index is out of bounds.
- Performance pitfalls: Using a `vector` instead of a `map` for lookups and updates.
- Testing considerations: Test the solution with different inputs, such as an empty system, or a system with multiple numbers.