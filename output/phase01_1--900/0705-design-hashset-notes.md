## Design Hashset
**Problem Link:** [https://leetcode.com/problems/design-hashset/description](https://leetcode.com/problems/design-hashset/description)

**Problem Statement:**
- Design a `HashSet` class that supports the following operations: `add(value)`, `remove(value)`, and `contains(value)`.
- The `add(value)` operation adds the `value` to the set if it is not already present.
- The `remove(value)` operation removes the `value` from the set if it is present.
- The `contains(value)` operation returns `true` if the `value` is in the set, otherwise returns `false`.
- Key requirements and edge cases to consider:
  - Handling duplicate values
  - Handling values that are not in the set
  - Handling an empty set
- Example test cases with explanations:
  - `add(1)`, `add(2)`, `contains(1)` should return `true`, `contains(3)` should return `false`
  - `add(1)`, `remove(1)`, `contains(1)` should return `false`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Use a linear search to find the value in the set.
- Step-by-step breakdown of the solution:
  1. Create an array to store the values in the set.
  2. In the `add(value)` operation, iterate through the array to check if the value is already present. If not, add it to the array.
  3. In the `remove(value)` operation, iterate through the array to find the value and remove it if present.
  4. In the `contains(value)` operation, iterate through the array to check if the value is present.
- Why this approach comes to mind first: It is a straightforward approach that does not require any complex data structures or algorithms.

```cpp
class MyHashSet {
public:
    vector<int> values;
    MyHashSet() {}
    void add(int key) {
        for (int i = 0; i < values.size(); i++) {
            if (values[i] == key) return;
        }
        values.push_back(key);
    }
    void remove(int key) {
        for (int i = 0; i < values.size(); i++) {
            if (values[i] == key) {
                values.erase(values.begin() + i);
                return;
            }
        }
    }
    bool contains(int key) {
        for (int i = 0; i < values.size(); i++) {
            if (values[i] == key) return true;
        }
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the set. This is because we are using a linear search to find the value in the set.
> - **Space Complexity:** $O(n)$, where $n$ is the number of elements in the set. This is because we are storing all the elements in the set in an array.
> - **Why these complexities occur:** The linear search operation is the main contributor to the time complexity, and the storage of all elements in the set contributes to the space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a hash table (unordered set in C++) to store the values in the set. This allows for constant time complexity for the `add`, `remove`, and `contains` operations.
- Detailed breakdown of the approach:
  1. Create an unordered set to store the values in the set.
  2. In the `add(value)` operation, use the `insert` method to add the value to the set if it is not already present.
  3. In the `remove(value)` operation, use the `erase` method to remove the value from the set if it is present.
  4. In the `contains(value)` operation, use the `find` method to check if the value is present in the set.
- Proof of optimality: The hash table allows for constant time complexity for the `add`, `remove`, and `contains` operations, making it the most efficient solution.

```cpp
class MyHashSet {
public:
    unordered_set<int> values;
    MyHashSet() {}
    void add(int key) {
        values.insert(key);
    }
    void remove(int key) {
        values.erase(key);
    }
    bool contains(int key) {
        return values.find(key) != values.end();
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, where $n$ is the number of elements in the set. This is because we are using a hash table to store the values, which allows for constant time complexity for the `add`, `remove`, and `contains` operations.
> - **Space Complexity:** $O(n)$, where $n$ is the number of elements in the set. This is because we are storing all the elements in the set in the hash table.
> - **Optimality proof:** The use of a hash table allows for constant time complexity for the `add`, `remove`, and `contains` operations, making it the most efficient solution.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Hash tables and unordered sets.
- Problem-solving patterns identified: Using the right data structure to solve the problem efficiently.
- Optimization techniques learned: Using a hash table to reduce the time complexity of the `add`, `remove`, and `contains` operations.
- Similar problems to practice: Other problems that involve using hash tables or unordered sets, such as the `LRU Cache` problem.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for duplicate values when adding to the set.
- Edge cases to watch for: Handling an empty set, handling values that are not in the set.
- Performance pitfalls: Using a linear search instead of a hash table.
- Testing considerations: Testing the `add`, `remove`, and `contains` operations with different inputs and edge cases.