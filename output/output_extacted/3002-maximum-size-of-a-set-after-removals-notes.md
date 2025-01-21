## Maximum Size of a Set After Removals
**Problem Link:** https://leetcode.com/problems/maximum-size-of-a-set-after-removals/description

**Problem Statement:**
- Input format and constraints: The problem takes a set of integers `nums` and an array of integers `removes` as input. The goal is to find the maximum size of a subset of `nums` after removing all elements present in `removes`.
- Expected output format: The function should return an integer representing the maximum size of the subset.
- Key requirements and edge cases to consider: 
    - The input set `nums` can contain duplicate elements.
    - The `removes` array may also contain duplicates.
    - The function should handle cases where `nums` or `removes` are empty.
- Example test cases with explanations: 
    - If `nums = [1, 2, 3, 4]` and `removes = [3, 4]`, the function should return `2` because after removing `3` and `4`, the subset `[1, 2]` has the maximum size.
    - If `nums = [1, 1, 1, 1]` and `removes = [1]`, the function should return `0` because all elements in `nums` are removed.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to iterate through each element in `nums` and check if it exists in `removes`. If it does, we skip it; otherwise, we include it in our subset.
- Step-by-step breakdown of the solution:
    1. Initialize an empty subset.
    2. Iterate through each element in `nums`.
    3. For each element, check if it exists in `removes`.
    4. If the element is not found in `removes`, add it to the subset.
    5. Return the size of the subset.
- Why this approach comes to mind first: It's a straightforward, intuitive method that directly addresses the problem statement without requiring complex data structures or algorithms.

```cpp
int maximumSizeOfASet(vector<int>& nums, vector<int>& removes) {
    unordered_set<int> removeSet(removes.begin(), removes.end());
    int count = 0;
    for (int num : nums) {
        if (removeSet.find(num) == removeSet.end()) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the size of `nums` and $m$ is the size of `removes`. This is because we're doing a constant amount of work for each element in both `nums` and `removes`.
> - **Space Complexity:** $O(m)$, for storing the elements of `removes` in a set. This allows for efficient lookups.
> - **Why these complexities occur:** The time complexity is linear because we're iterating through each element in both arrays once. The space complexity is due to the storage required for the set of removed elements.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal approach is essentially the same as the brute force approach but with a slight optimization. We use an `unordered_set` to store the elements of `removes`, allowing for constant time complexity lookups.
- Detailed breakdown of the approach: 
    1. Convert the `removes` array into an `unordered_set` for efficient lookups.
    2. Initialize a counter to keep track of the elements in `nums` that are not in `removes`.
    3. Iterate through each element in `nums`. For each element, check if it exists in the `removes` set.
    4. If an element is not found in the `removes` set, increment the counter.
    5. Return the counter as the maximum size of the subset.
- Proof of optimality: This approach is optimal because it achieves a linear time complexity, which is the best we can do given that we must at least read the input once.

```cpp
int maximumSizeOfASet(vector<int>& nums, vector<int>& removes) {
    unordered_set<int> removeSet(removes.begin(), removes.end());
    int count = 0;
    for (int num : nums) {
        if (removeSet.find(num) == removeSet.end()) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the size of `nums` and $m$ is the size of `removes`.
> - **Space Complexity:** $O(m)$, for storing the elements of `removes` in a set.
> - **Optimality proof:** The linear time complexity is optimal because we must examine each element at least once to determine if it should be included in the subset.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Efficient use of data structures like `unordered_set` for fast lookups.
- Problem-solving patterns identified: The importance of choosing the right data structure to achieve optimal complexity.
- Optimization techniques learned: Converting arrays to sets for faster lookups.
- Similar problems to practice: Other problems involving set operations and efficient lookups.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle edge cases like empty inputs.
- Edge cases to watch for: Duplicates in `nums` or `removes`, and cases where `nums` or `removes` are empty.
- Performance pitfalls: Using linear search instead of a set for lookups, leading to higher time complexity.
- Testing considerations: Thoroughly test with various inputs, including edge cases and large datasets.