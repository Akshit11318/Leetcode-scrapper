## Find Indices with Index and Value Difference I

**Problem Link:** https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/description

**Problem Statement:**
- Input format: An array of integers `nums`.
- Constraints: The array contains at least one element.
- Expected output format: A vector of integers representing the indices where the difference between the index and the value is equal to `k`.
- Key requirements and edge cases to consider: Handling cases where no such indices exist, ensuring the solution scales for large inputs, and correctly calculating the difference.
- Example test cases with explanations:
  - Example 1: `nums = [1,2,3,4,5], k = 0`, the output should be `[0,1,2,3,4]`.
  - Example 2: `nums = [2,5,8,13], k = -2`, the output should be `[0,2]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through the array and check each element to see if its index minus its value equals `k`.
- Step-by-step breakdown of the solution:
  1. Initialize an empty vector to store the indices that meet the condition.
  2. Loop through the array, considering each index and value pair.
  3. For each pair, calculate the difference between the index and the value.
  4. If the difference equals `k`, add the index to the result vector.
- Why this approach comes to mind first: It directly addresses the problem statement by checking every possible index and value pair.

```cpp
vector<int> findIndices(vector<int>& nums, int k) {
    vector<int> result;
    for (int i = 0; i < nums.size(); i++) {
        if (i - nums[i] == k) {
            result.push_back(i);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the input array, because we potentially check every element once.
> - **Space Complexity:** $O(n)$, as in the worst-case scenario (when every index meets the condition), the size of the output vector could be equal to the size of the input array.
> - **Why these complexities occur:** The linear time complexity is due to the single loop through the array, and the space complexity is due to storing the result in a new vector.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The brute force approach is already optimal for this problem because it must check every element at least once to ensure all indices that meet the condition are found.
- Detailed breakdown of the approach: Same as the brute force approach.
- Proof of optimality: Any algorithm must at least read the input, which takes $O(n)$ time. Since the brute force approach already achieves this, it is optimal.
- Why further optimization is impossible: Given the requirement to check every element, any optimization would not improve the time complexity beyond $O(n)$.

```cpp
vector<int> findIndices(vector<int>& nums, int k) {
    vector<int> result;
    for (int i = 0; i < nums.size(); i++) {
        if (i - nums[i] == k) {
            result.push_back(i);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the input array.
> - **Space Complexity:** $O(n)$, for storing the result in a new vector.
> - **Optimality proof:** This solution is optimal because it checks every element exactly once, which is necessary to solve the problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Linear search, iteration through an array.
- Problem-solving patterns identified: Checking every element in an array to find those that meet a certain condition.
- Optimization techniques learned: Recognizing when a brute force approach is already optimal due to the nature of the problem.
- Similar problems to practice: Other problems involving linear searches or checking conditions across an array.

**Mistakes to Avoid:**
- Common implementation errors: Off-by-one errors when indexing arrays, incorrect conditional statements.
- Edge cases to watch for: Empty input arrays, arrays with a single element, cases where no indices meet the condition.
- Performance pitfalls: Assuming a more complex solution is necessary when a simple iteration suffices.
- Testing considerations: Thoroughly testing with various input sizes, edge cases, and expected outputs to ensure correctness.