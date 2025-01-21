## Insert Delete GetRandom O(1) - Duplicates allowed

**Problem Link:** https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/description

**Problem Statement:**
- Input format and constraints: The problem requires designing a data structure that supports `insert`, `remove`, and `getRandom` operations. The data structure should be able to handle duplicates and perform all operations in O(1) time complexity. The input will be a sequence of these operations, and the output should be the result of the `getRandom` operation.
- Expected output format: The output should be the result of the `getRandom` operation, which returns a random element from the data structure.
- Key requirements and edge cases to consider: The data structure should be able to handle duplicates, and all operations should be performed in O(1) time complexity. The `remove` operation should remove one occurrence of the specified element if it exists in the data structure.
- Example test cases with explanations:
  - Example 1:
    - Input: `["RandomizedCollection","insert","insert","insert","getRandom","remove","getRandom"]`
    - Output: `[null,true,true,true,2,true,1]`
    - Explanation: The data structure is initialized, and then the elements 1, 2, and 2 are inserted. The `getRandom` operation returns a random element, which is 2. Then, the `remove` operation removes one occurrence of the element 2, and the `getRandom` operation returns a random element again.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves using a vector to store the elements and performing the `insert`, `remove`, and `getRandom` operations on the vector.
- Step-by-step breakdown of the solution:
  1. Insert operation: Simply push the element onto the vector.
  2. Remove operation: Iterate through the vector to find the first occurrence of the element and remove it.
  3. GetRandom operation: Use the `rand()` function to generate a random index and return the element at that index.
- Why this approach comes to mind first: The brute force approach is straightforward and easy to implement, but it does not meet the O(1) time complexity requirement for the `remove` operation.

```cpp
class RandomizedCollection {
public:
    vector<int> nums;
    RandomizedCollection() {}
    
    bool insert(int val) {
        nums.push_back(val);
        return true;
    }
    
    bool remove(int val) {
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == val) {
                nums.erase(nums.begin() + i);
                return true;
            }
        }
        return false;
    }
    
    int getRandom() {
        return nums[rand() % nums.size()];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for `insert`, $O(n)$ for `remove`, and $O(1)$ for `getRandom`.
> - **Space Complexity:** $O(n)$, where $n$ is the number of elements in the data structure.
> - **Why these complexities occur:** The `remove` operation has a time complexity of $O(n)$ because it involves iterating through the vector to find the first occurrence of the element.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution involves using an unordered map to store the indices of the elements in the vector. This allows for O(1) time complexity for the `remove` operation.
- Detailed breakdown of the approach:
  1. Insert operation: Push the element onto the vector and update the unordered map with the index of the element.
  2. Remove operation: Use the unordered map to find the index of the element and remove it from the vector. Update the unordered map accordingly.
  3. GetRandom operation: Use the `rand()` function to generate a random index and return the element at that index.
- Proof of optimality: The optimal solution meets the O(1) time complexity requirement for all operations.

```cpp
class RandomizedCollection {
public:
    vector<int> nums;
    unordered_map<int, unordered_set<int>> indices;
    RandomizedCollection() {}
    
    bool insert(int val) {
        nums.push_back(val);
        indices[val].insert(nums.size() - 1);
        return indices[val].size() == 1;
    }
    
    bool remove(int val) {
        if (indices.find(val) == indices.end()) {
            return false;
        }
        int index = *indices[val].begin();
        if (index != nums.size() - 1) {
            int last = nums.back();
            nums[index] = last;
            indices[last].erase(nums.size() - 1);
            indices[last].insert(index);
        }
        nums.pop_back();
        indices[val].erase(index);
        if (indices[val].empty()) {
            indices.erase(val);
        }
        return true;
    }
    
    int getRandom() {
        return nums[rand() % nums.size()];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for all operations.
> - **Space Complexity:** $O(n)$, where $n$ is the number of elements in the data structure.
> - **Optimality proof:** The optimal solution meets the O(1) time complexity requirement for all operations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using an unordered map to store the indices of the elements in the vector allows for O(1) time complexity for the `remove` operation.
- Problem-solving patterns identified: The problem requires using a combination of data structures to meet the O(1) time complexity requirement for all operations.
- Optimization techniques learned: Using an unordered map to store the indices of the elements in the vector is an optimization technique that allows for O(1) time complexity for the `remove` operation.
- Similar problems to practice: Other problems that involve designing data structures to meet specific time complexity requirements.

**Mistakes to Avoid:**
- Common implementation errors: Not updating the unordered map correctly when removing an element.
- Edge cases to watch for: Handling the case where the element to be removed is not in the data structure.
- Performance pitfalls: Not using an unordered map to store the indices of the elements in the vector, which can result in O(n) time complexity for the `remove` operation.
- Testing considerations: Testing the data structure with different sequences of operations to ensure that it meets the O(1) time complexity requirement for all operations.