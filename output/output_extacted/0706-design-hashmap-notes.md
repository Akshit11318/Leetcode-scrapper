## Design Hashmap

**Problem Link:** [https://leetcode.com/problems/design-hashmap/description](https://leetcode.com/problems/design-hashmap/description)

**Problem Statement:**
- Input format and constraints: The problem requires designing a `MyHashMap` class that supports the following operations:
  - `void put(int key, int value)`: Inserts or updates the value for a given key.
  - `int get(int key)`: Returns the value for a given key if it exists; otherwise, returns -1.
  - `void remove(int key)`: Removes the key-value pair for a given key if it exists.
- Expected output format: The output of each operation should be as specified above.
- Key requirements and edge cases to consider: Handling collisions, ensuring efficient insertion, retrieval, and removal of key-value pairs, and handling cases where keys do not exist.
- Example test cases with explanations:
  - `MyHashMap myHashMap = new MyHashMap();`
  - `myHashMap.put(1, 1); // myHashMap now contains [1,1]`
  - `myHashMap.put(2, 2); // myHashMap now contains [1,1], [2,2]`
  - `myHashMap.get(1); // returns 1`
  - `myHashMap.get(3); // returns -1 (not found)`
  - `myHashMap.put(2, 1); // myHashMap now contains [1,1], [2,1]`
  - `myHashMap.get(2); // returns 1`
  - `myHashMap.remove(2); // myHashMap now contains [1,1]`
  - `myHashMap.get(2); // returns -1 (not found)`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: One might start by considering a simple array to store key-value pairs, where each index represents a unique key, and the value at that index is the corresponding value. However, this approach quickly becomes impractical for large ranges of keys or sparse key distributions due to memory inefficiency and potential for collisions.
- Step-by-step breakdown of the solution: 
  1. Initialize an array of size equal to the maximum possible key value plus one, assuming keys are non-negative integers.
  2. For `put(key, value)`, simply assign `value` to the array at index `key`.
  3. For `get(key)`, return the value at the array index `key`.
  4. For `remove(key)`, set the value at index `key` to a special value indicating removal, such as `-1`.
- Why this approach comes to mind first: It's straightforward and aligns with basic array manipulation. However, it's inefficient for large or sparse key sets due to excessive memory usage and doesn't handle negative keys or non-integer keys.

```cpp
class MyHashMap {
public:
    vector<int> data;
    MyHashMap() {
        data.resize(1000001, -1); // Assuming keys are in range [0, 1000000]
    }
    void put(int key, int value) {
        data[key] = value;
    }
    int get(int key) {
        return data[key];
    }
    void remove(int key) {
        data[key] = -1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for all operations, as array access is constant time.
> - **Space Complexity:** $O(n)$, where $n$ is the size of the array, which could be very large and inefficient.
> - **Why these complexities occur:** The time complexity is constant because array operations are $O(1)$, but the space complexity is linear due to the potentially large array size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Using a hash table (or unordered_map in C++) to store key-value pairs. This allows for efficient insertion, retrieval, and removal of pairs with an average time complexity of $O(1)$, making it suitable for a wide range of key distributions.
- Detailed breakdown of the approach:
  1. Utilize an `unordered_map<int, int>` to store key-value pairs.
  2. For `put(key, value)`, insert or update the value for the given key in the map.
  3. For `get(key)`, return the value associated with the key if it exists in the map; otherwise, return -1.
  4. For `remove(key)`, remove the key-value pair from the map if the key exists.
- Proof of optimality: This approach is optimal because it leverages the hash table's average case $O(1)$ time complexity for insertion, search, and deletion operations, making it highly efficient for managing key-value pairs.

```cpp
class MyHashMap {
public:
    unordered_map<int, int> data;
    MyHashMap() {}
    void put(int key, int value) {
        data[key] = value;
    }
    int get(int key) {
        if (data.find(key) != data.end()) {
            return data[key];
        }
        return -1;
    }
    void remove(int key) {
        data.erase(key);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ on average for all operations, thanks to the hash table.
> - **Space Complexity:** $O(n)$, where $n$ is the number of key-value pairs stored, which is more efficient than the brute force approach for sparse key sets.
> - **Optimality proof:** The use of an `unordered_map` provides the best average-case performance for the required operations, making this solution optimal for practical purposes.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Hash tables and their application in solving problems that require efficient key-value pair management.
- Problem-solving patterns identified: Recognizing the need for a data structure that supports fast insertion, search, and deletion, such as a hash table.
- Optimization techniques learned: Choosing the right data structure for the problem at hand can significantly improve performance.
- Similar problems to practice: Other problems involving key-value pair management, such as implementing a Least Recently Used (LRU) cache.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle edge cases, such as non-existent keys or removal of non-existent keys.
- Edge cases to watch for: Negative keys, keys outside the expected range, and handling collisions in hash tables.
- Performance pitfalls: Using data structures that do not support $O(1)$ operations for insertion, search, and deletion, such as linear search in an array.
- Testing considerations: Thoroughly testing the implementation with various key distributions and edge cases to ensure correctness and performance.