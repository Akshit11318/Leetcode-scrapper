## Insert Delete GetRandom O(1)

**Problem Link:** https://leetcode.com/problems/insert-delete-getrandom-o1/description

**Problem Statement:**
- Input format: The problem requires implementing a class `RandomizedSet` that supports the following methods:
  - `insert(int val)`: Inserts a value to the set if not already present.
  - `remove(int val)`: Removes a value from the set if present.
  - `getRandom()`: Returns a random element from the set.
- Constraints:
  - The set will contain at most $10^5$ elements.
  - The input array will contain unique integers in the range $[-10^9, 10^9]$.
- Expected output format:
  - The `insert`, `remove`, and `getRandom` operations should be performed in O(1) time complexity.
- Key requirements and edge cases to consider:
  - Handling duplicates during insertion.
  - Removing elements that are not present in the set.
  - Returning a random element when the set is empty.
- Example test cases with explanations:
  - Inserting a value that is already present in the set should return `false`.
  - Removing a value that is not present in the set should return `false`.
  - The `getRandom` method should return a random element from the set.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach would involve using a vector to store the elements and then implementing the `insert`, `remove`, and `getRandom` methods.
- Step-by-step breakdown of the solution:
  1. Create a vector to store the elements.
  2. For the `insert` method, iterate through the vector to check if the element is already present. If not, add it to the vector.
  3. For the `remove` method, iterate through the vector to find the element and remove it.
  4. For the `getRandom` method, use a random number generator to select an index from the vector.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it has a high time complexity for the `insert` and `remove` methods.

```cpp
class RandomizedSet {
public:
    vector<int> elements;
    bool insert(int val) {
        for (int i = 0; i < elements.size(); i++) {
            if (elements[i] == val) {
                return false;
            }
        }
        elements.push_back(val);
        return true;
    }
    bool remove(int val) {
        for (int i = 0; i < elements.size(); i++) {
            if (elements[i] == val) {
                elements.erase(elements.begin() + i);
                return true;
            }
        }
        return false;
    }
    int getRandom() {
        int index = rand() % elements.size();
        return elements[index];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ for `insert` and `remove`, where $n$ is the number of elements in the set. $O(1)$ for `getRandom`.
> - **Space Complexity:** $O(n)$, where $n$ is the number of elements in the set.
> - **Why these complexities occur:** The brute force approach has a high time complexity for `insert` and `remove` because it involves iterating through the vector to find or add elements.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Using an unordered map to store the elements and their indices in the vector, and a vector to store the elements.
- Detailed breakdown of the approach:
  1. Create an unordered map `elementIndex` to store the elements and their indices in the vector.
  2. Create a vector `elements` to store the elements.
  3. For the `insert` method, check if the element is already present in the map. If not, add it to the map and the vector.
  4. For the `remove` method, check if the element is present in the map. If it is, swap the element with the last element in the vector, update the map, and remove the last element from the vector.
  5. For the `getRandom` method, use a random number generator to select an index from the vector.
- Proof of optimality: This approach has a time complexity of O(1) for all methods, making it optimal.

```cpp
class RandomizedSet {
public:
    unordered_map<int, int> elementIndex;
    vector<int> elements;
    bool insert(int val) {
        if (elementIndex.find(val) != elementIndex.end()) {
            return false;
        }
        elementIndex[val] = elements.size();
        elements.push_back(val);
        return true;
    }
    bool remove(int val) {
        if (elementIndex.find(val) == elementIndex.end()) {
            return false;
        }
        int index = elementIndex[val];
        int lastElement = elements.back();
        elementIndex[lastElement] = index;
        elements[index] = lastElement;
        elements.pop_back();
        elementIndex.erase(val);
        return true;
    }
    int getRandom() {
        int index = rand() % elements.size();
        return elements[index];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for all methods.
> - **Space Complexity:** $O(n)$, where $n$ is the number of elements in the set.
> - **Optimality proof:** This approach is optimal because it uses an unordered map to store the elements and their indices, allowing for constant time complexity for all methods.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using an unordered map to store elements and their indices, and a vector to store the elements.
- Problem-solving patterns identified: Using a combination of data structures to achieve optimal time complexity.
- Optimization techniques learned: Using an unordered map to reduce the time complexity of the `insert` and `remove` methods.
- Similar problems to practice: Implementing a set with O(1) time complexity for `insert`, `remove`, and `contains` methods.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for duplicates during insertion, not updating the map correctly during removal.
- Edge cases to watch for: Removing elements that are not present in the set, returning a random element when the set is empty.
- Performance pitfalls: Using a vector alone to store the elements, resulting in high time complexity for the `insert` and `remove` methods.
- Testing considerations: Testing the `insert`, `remove`, and `getRandom` methods with different inputs and edge cases to ensure correctness.