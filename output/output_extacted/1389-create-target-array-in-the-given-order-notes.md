## Create Target Array in the Given Order

**Problem Link:** https://leetcode.com/problems/create-target-array-in-the-given-order/description

**Problem Statement:**
- Input format: Given two arrays `nums` and `index`, where `nums` is an array of integers and `index` is an array of indices corresponding to the elements in `nums`.
- Constraints: The length of `nums` and `index` are the same, and the elements in `index` are distinct.
- Expected output format: Create a target array `target` where the elements from `nums` are inserted at the corresponding indices from `index`.
- Key requirements and edge cases to consider: The target array should be built from scratch, and the elements from `nums` should be inserted at the specified indices in the order they appear in `nums`.

### Brute Force Approach

**Explanation:**
- Initial thought process: Create an empty array and insert elements from `nums` at the specified indices from `index`.
- Step-by-step breakdown of the solution:
  1. Initialize an empty array `target`.
  2. Iterate over the `nums` and `index` arrays simultaneously.
  3. For each pair of `num` and `idx`, insert `num` at the `idx` position in the `target` array.
  4. If the `idx` is greater than the current length of the `target` array, append the `num` to the end of the `target` array.

```cpp
vector<int> createTargetArray(vector<int>& nums, vector<int>& index) {
    vector<int> target;
    for (int i = 0; i < nums.size(); i++) {
        if (index[i] < target.size()) {
            target.insert(target.begin() + index[i], nums[i]);
        } else {
            target.push_back(nums[i]);
        }
    }
    return target;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the `nums` array. This is because in the worst-case scenario, we are inserting an element at the beginning of the `target` array, which takes $O(n)$ time, and we are doing this $n$ times.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the `nums` array. This is because we are storing the `target` array, which has the same length as the `nums` array.
> - **Why these complexities occur:** The time complexity is $O(n^2)$ because of the insertion operation in the `target` array, and the space complexity is $O(n)$ because we are storing the `target` array.

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of inserting elements at the specified indices, we can build the `target` array by iterating over the `nums` and `index` arrays simultaneously and appending the elements to the `target` array in the correct order.
- Detailed breakdown of the approach:
  1. Initialize an empty array `target`.
  2. Iterate over the `nums` and `index` arrays simultaneously.
  3. For each pair of `num` and `idx`, append the `num` to the `target` array.
  4. After appending all the elements, use the `index` array to determine the correct order of the elements in the `target` array.
- Proof of optimality: This approach is optimal because it has a time complexity of $O(n)$, which is the best possible time complexity for this problem.

```cpp
vector<int> createTargetArray(vector<int>& nums, vector<int>& index) {
    vector<int> target;
    for (int i = 0; i < nums.size(); i++) {
        target.insert(target.begin() + index[i], nums[i]);
    }
    return target;
}
```
However, the optimal approach can be further optimized using the following code:

```cpp
vector<int> createTargetArray(vector<int>& nums, vector<int>& index) {
    vector<int> target;
    for (int i = 0; i < nums.size(); i++) {
        target.insert(target.begin() + index[i], nums[i]);
    }
    return target;
}
```
can be optimized as

```cpp
vector<int> createTargetArray(vector<int>& nums, vector<int>& index) {
    vector<int> target;
    for (int i = 0; i < nums.size(); i++) {
        target.insert(target.begin() + index[i], nums[i]);
    }
    return target;
}
```
The optimal solution can be implemented with a `deque` data structure which supports $O(1)$ insertion at any position.

```cpp
#include <deque>
vector<int> createTargetArray(vector<int>& nums, vector<int>& index) {
    deque<int> dq;
    for (int i = 0; i < nums.size(); i++) {
        dq.insert(dq.begin() + index[i], nums[i]);
    }
    vector<int> res(dq.begin(), dq.end());
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the `nums` array. This is because we are iterating over the `nums` and `index` arrays simultaneously, and each insertion operation takes $O(1)$ time on average.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the `nums` array. This is because we are storing the `target` array, which has the same length as the `nums` array.
> - **Optimality proof:** The time complexity is $O(n)$ because we are iterating over the `nums` and `index` arrays simultaneously, and each insertion operation takes $O(1)$ time on average.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, insertion, and deque data structure.
- Problem-solving patterns identified: Building an array by iterating over two arrays simultaneously and using the indices to determine the correct order of the elements.
- Optimization techniques learned: Using a deque data structure to optimize the insertion operation.
- Similar problems to practice: Other problems that involve building an array by iterating over two arrays simultaneously, such as the "Target Array" problem.

**Mistakes to Avoid:**
- Common implementation errors: Not checking the bounds of the `target` array before inserting an element, or not handling the case where the `index` array contains duplicate indices.
- Edge cases to watch for: The case where the `index` array contains indices that are out of bounds of the `target` array, or the case where the `nums` array contains duplicate elements.
- Performance pitfalls: Using a data structure that has a high insertion time complexity, such as a vector, instead of a deque.
- Testing considerations: Testing the function with different inputs, such as arrays of different lengths, and arrays with duplicate elements or indices.