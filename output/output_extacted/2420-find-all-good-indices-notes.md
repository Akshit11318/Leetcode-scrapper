## Find All Good Indices
**Problem Link:** https://leetcode.com/problems/find-all-good-indices/description

**Problem Statement:**
- Input: `nums`, `k`
- Constraints: `1 <= nums.length <= 10^5`, `1 <= nums[i] <= 10^9`, `1 <= k <= nums.length`
- Expected output: A list of indices where `nums[i]` is a good index
- Key requirements and edge cases: 
  - A good index is an index `i` such that `i - k + 1 >= 0` and `nums[i]` is not equal to any of the numbers from `nums[i - k + 1]` to `nums[i - 1]`.
  - The output should be in ascending order
- Example test cases with explanations:
  - Input: `nums = [2,1,1,1,3], k = 3`, Output: `[2,3]`
  - Input: `nums = [2,1,1,2], k = 2`, Output: `[]`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check each index in the array and verify if it's a good index by comparing it with the previous `k` elements
- Step-by-step breakdown of the solution:
  1. Iterate over the array from index `k-1` to the end
  2. For each index `i`, create a set of elements from `nums[i - k + 1]` to `nums[i - 1]`
  3. Check if `nums[i]` is in the set
  4. If not, add `i` to the result list
- Why this approach comes to mind first: It's a straightforward and intuitive way to solve the problem, but it may not be efficient for large inputs

```cpp
vector<int> goodIndices(vector<int>& nums, int k) {
    vector<int> result;
    for (int i = k - 1; i < nums.size(); i++) {
        unordered_set<int> prevElements;
        for (int j = i - k + 1; j < i; j++) {
            prevElements.insert(nums[j]);
        }
        if (prevElements.find(nums[i]) == prevElements.end()) {
            result.push_back(i);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k)$, where $n$ is the length of the input array, because for each index, we're iterating over the previous `k` elements
> - **Space Complexity:** $O(k)$, because in the worst case, the set of previous elements will contain `k` elements
> - **Why these complexities occur:** The brute force approach has a high time complexity because it involves nested loops, and the space complexity is due to the use of a set to store the previous elements

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of creating a set of previous elements for each index, we can use a sliding window approach to keep track of the previous `k` elements
- Detailed breakdown of the approach:
  1. Initialize an empty set to store the previous `k` elements
  2. Iterate over the array, and for each index `i`, add `nums[i - k]` to the set if `i >= k`
  3. Remove `nums[i - 1]` from the set
  4. Check if `nums[i]` is in the set, and if not, add `i` to the result list
- Proof of optimality: This approach has a linear time complexity, which is the best possible complexity for this problem

```cpp
vector<int> goodIndices(vector<int>& nums, int k) {
    vector<int> result;
    unordered_set<int> prevElements;
    for (int i = 0; i < nums.size(); i++) {
        if (i >= k) {
            prevElements.insert(nums[i - k]);
        }
        if (i > 0) {
            prevElements.erase(nums[i - 1]);
        }
        if (prevElements.find(nums[i]) == prevElements.end() && i >= k - 1) {
            result.push_back(i);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input array, because we're iterating over the array only once
> - **Space Complexity:** $O(k)$, because in the worst case, the set of previous elements will contain `k` elements
> - **Optimality proof:** This approach is optimal because it has a linear time complexity, which is the best possible complexity for this problem

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sliding window approach, set data structure
- Problem-solving patterns identified: Using a set to keep track of previous elements, optimizing the brute force approach by reducing the number of iterations
- Optimization techniques learned: Reducing the time complexity from $O(n \cdot k)$ to $O(n)$ by using a sliding window approach
- Similar problems to practice: Problems that involve finding good indices or optimal solutions using a sliding window approach

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, not optimizing the brute force approach
- Edge cases to watch for: Empty input array, `k` greater than the length of the input array
- Performance pitfalls: Using a brute force approach with a high time complexity
- Testing considerations: Testing the solution with different input sizes, testing the solution with edge cases