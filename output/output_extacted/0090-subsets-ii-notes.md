## Subsets II
**Problem Link:** [https://leetcode.com/problems/subsets-ii/description](https://leetcode.com/problems/subsets-ii/description)

**Problem Statement:**
- Input format and constraints: Given a collection of integers `nums` that may contain duplicates, return all possible subsets (the power set). The input array `nums` will contain integers in the range `[1, 100]`, and the length of `nums` will be between `1` and `100`.
- Expected output format: The output should be a vector of vectors, where each inner vector represents a subset of the input array.
- Key requirements and edge cases to consider: The input array may contain duplicate elements, and the output should not contain duplicate subsets.
- Example test cases with explanations:
  - Example 1: Input: `nums = [1, 2, 2]`. Output: `[[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]`.
  - Example 2: Input: `nums = [2, 1, 1]`. Output: `[[], [1], [1, 1], [1, 1, 2], [1, 2], [2]]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves generating all possible subsets of the input array and then removing duplicates.
- Step-by-step breakdown of the solution:
  1. Generate all possible subsets of the input array using bit manipulation or recursion.
  2. Store each subset in a set to automatically remove duplicates.
  3. Convert the set of subsets back to a vector of vectors and return it.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it may not be efficient for large input arrays due to the overhead of generating all possible subsets and removing duplicates.

```cpp
void backtrack(vector<int>& nums, int start, vector<int>& subset, vector<vector<int>>& result) {
    result.push_back(subset);
    for (int i = start; i < nums.size(); i++) {
        // Skip duplicates
        if (i > start && nums[i] == nums[i - 1]) continue;
        subset.push_back(nums[i]);
        backtrack(nums, i + 1, subset, result);
        subset.pop_back();
    }
}

vector<vector<int>> subsetsWithDup(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    vector<vector<int>> result;
    vector<int> subset;
    backtrack(nums, 0, subset, result);
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where $n$ is the length of the input array, because we generate all possible subsets.
> - **Space Complexity:** $O(2^n)$, where $n$ is the length of the input array, because we store all possible subsets in the result.
> - **Why these complexities occur:** The brute force approach generates all possible subsets of the input array, which results in exponential time and space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal approach involves using a recursive backtracking algorithm to generate all possible subsets of the input array while skipping duplicates.
- Detailed breakdown of the approach:
  1. Sort the input array to group duplicate elements together.
  2. Use a recursive backtracking function to generate all possible subsets of the input array.
  3. In the backtracking function, skip duplicate elements by checking if the current element is the same as the previous one.
  4. Store each subset in the result vector.
- Proof of optimality: The optimal approach has a time complexity of $O(2^n)$, which is the best possible time complexity for this problem because we must generate all possible subsets of the input array.

```cpp
void backtrack(vector<int>& nums, int start, vector<int>& subset, vector<vector<int>>& result) {
    result.push_back(subset);
    for (int i = start; i < nums.size(); i++) {
        // Skip duplicates
        if (i > start && nums[i] == nums[i - 1]) continue;
        subset.push_back(nums[i]);
        backtrack(nums, i + 1, subset, result);
        subset.pop_back();
    }
}

vector<vector<int>> subsetsWithDup(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    vector<vector<int>> result;
    vector<int> subset;
    backtrack(nums, 0, subset, result);
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where $n$ is the length of the input array, because we generate all possible subsets.
> - **Space Complexity:** $O(2^n)$, where $n$ is the length of the input array, because we store all possible subsets in the result.
> - **Optimality proof:** The optimal approach has a time complexity of $O(2^n)$, which is the best possible time complexity for this problem because we must generate all possible subsets of the input array.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Backtracking, recursion, and duplicate handling.
- Problem-solving patterns identified: Using recursion to generate all possible subsets of an array.
- Optimization techniques learned: Skipping duplicates to improve efficiency.
- Similar problems to practice: Generating all possible permutations of an array, finding all possible combinations of an array.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to skip duplicates, incorrect recursion termination conditions.
- Edge cases to watch for: Empty input array, input array with all duplicate elements.
- Performance pitfalls: Generating all possible subsets of a large input array without skipping duplicates.
- Testing considerations: Test the solution with input arrays of different sizes and duplicate patterns.