## Two Sum

**Problem Link:** [https://leetcode.com/problems/two-sum/description](https://leetcode.com/problems/two-sum/description)

**Problem Statement:**
- Input format: An array of integers `nums` and an integer `target`.
- Constraints: `2 <= nums.length <= 10^4`, `-10^9 <= nums[i] <= 10^9`, `-10^9 <= target <= 10^9`.
- Expected output format: An array of two integers representing the indices of the two numbers that add up to the `target`.
- Key requirements and edge cases to consider: 
  - Each input would have exactly one solution.
  - You may not use the same element twice.
  - You can return the answer in any order.
- Example test cases with explanations: 
  - Input: `nums = [2, 7, 11, 15], target = 9`
    Output: `[0, 1]` because `nums[0] + nums[1] == 2 + 7 == 9`.
  - Input: `nums = [3, 2, 4], target = 6`
    Output: `[1, 2]` because `nums[1] + nums[2] == 2 + 4 == 6`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find two numbers that add up to the `target`, we can compare each number with every other number in the array.
- Step-by-step breakdown of the solution: 
  1. Iterate over the array with the first pointer.
  2. For each element, iterate over the rest of the array with a second pointer.
  3. Check if the sum of the elements at the current positions of the two pointers equals the `target`.
  4. If it does, return the indices of these elements.
- Why this approach comes to mind first: It is straightforward and simple to understand, as it directly checks all possible pairs of numbers in the array.

```cpp
vector<int> twoSum(vector<int>& nums, int target) {
    for (int i = 0; i < nums.size(); i++) {
        for (int j = i + 1; j < nums.size(); j++) {
            if (nums[i] + nums[j] == target) {
                return {i, j};
            }
        }
    }
    // This should not happen according to the problem statement
    return {};
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ where $n$ is the number of elements in the `nums` array. This is because for each element, we potentially check every other element.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input and output, as we only use a constant amount of space to store the indices.
> - **Why these complexities occur:** The nested loops cause the quadratic time complexity, while the constant space complexity comes from only using a fixed amount of space regardless of the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a `unordered_map` (hash map) to store the numbers we have seen so far and their indices. This allows us to check if a number's complement (the value needed to reach the `target`) has been seen in constant time.
- Detailed breakdown of the approach:
  1. Create an empty `unordered_map` to store numbers and their indices.
  2. Iterate over the `nums` array.
  3. For each number, calculate its complement.
  4. Check if the complement is in the map.
  5. If it is, return the current index and the index of the complement.
  6. If not, add the current number and its index to the map.
- Proof of optimality: This solution has a linear time complexity because we make a single pass through the array, and looking up an element in the map takes constant time on average.

```cpp
vector<int> twoSum(vector<int>& nums, int target) {
    unordered_map<int, int> numToIndex;
    for (int i = 0; i < nums.size(); i++) {
        int complement = target - nums[i];
        if (numToIndex.find(complement) != numToIndex.end()) {
            return {numToIndex[complement], i};
        }
        numToIndex[nums[i]] = i;
    }
    // This should not happen according to the problem statement
    return {};
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of elements in the `nums` array, as we perform a constant amount of work for each element.
> - **Space Complexity:** $O(n)$, as in the worst case, we might store every element in the map.
> - **Optimality proof:** This is the most efficient solution because we only need to look at each element once, and we use a data structure that allows us to check for the existence of an element in constant time.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a hash map to store and quickly look up elements.
- Problem-solving patterns identified: Reducing the time complexity of a problem by using a more efficient data structure.
- Optimization techniques learned: Trading off space for time by using extra memory to speed up the computation.
- Similar problems to practice: Other problems that can be solved using hash maps, such as finding duplicates in an array or solving the "3Sum" problem.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle edge cases, such as an empty input array.
- Edge cases to watch for: Ensuring the solution works correctly when there are duplicate numbers in the array, or when the target sum is zero.
- Performance pitfalls: Using a data structure with poor lookup performance, such as a linked list, instead of a hash map.
- Testing considerations: Thoroughly testing the solution with a variety of inputs, including edge cases, to ensure it works correctly in all scenarios.