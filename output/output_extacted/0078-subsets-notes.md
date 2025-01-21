## Subsets
**Problem Link:** https://leetcode.com/problems/subsets/description

**Problem Statement:**
- Input format and constraints: Given an integer array `nums` of size `n`, where `n` is between `1` and `20`, generate all possible subsets of `nums`.
- Expected output format: Return a list of lists, where each sublist is a subset of `nums`.
- Key requirements and edge cases to consider:
  - The input array may contain duplicates, but the output should not contain duplicate subsets.
  - The order of subsets in the output does not matter.
- Example test cases with explanations:
  - Input: `nums = [1, 2, 3]`
    - Output: `[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]`
  - Input: `nums = [0]`
    - Output: `[[], [0]]`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: One way to generate all subsets is to use a brute force approach, where we consider each element in the input array and decide whether to include it in the current subset or not.
- Step-by-step breakdown of the solution:
  1. Start with an empty subset.
  2. Iterate over each element in the input array.
  3. For each element, create a new subset by including the current element in the current subset.
  4. Add both the current subset and the new subset to the list of subsets.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, as it involves simple iteration and subset creation.

```cpp
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> subset;
        generateSubsets(nums, 0, subset, result);
        return result;
    }
    
    void generateSubsets(vector<int>& nums, int start, vector<int>& subset, vector<vector<int>>& result) {
        result.push_back(subset);
        for (int i = start; i < nums.size(); i++) {
            subset.push_back(nums[i]);
            generateSubsets(nums, i + 1, subset, result);
            subset.pop_back();
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where $n$ is the size of the input array. This is because we generate $2^n$ subsets in the worst case.
> - **Space Complexity:** $O(2^n)$, where $n$ is the size of the input array. This is because we store $2^n$ subsets in the result list.
> - **Why these complexities occur:** The brute force approach involves generating all possible subsets, which results in exponential time and space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use bit manipulation to generate all subsets. Each subset can be represented as a binary number, where a `1` at the $i^{th}$ position indicates that the $i^{th}$ element is included in the subset.
- Detailed breakdown of the approach:
  1. Iterate over all numbers from $0$ to $2^n - 1$, where $n$ is the size of the input array.
  2. For each number, use bit manipulation to generate the corresponding subset.
  3. Add the subset to the result list.
- Proof of optimality: This approach is optimal because it generates all subsets in $O(2^n)$ time complexity, which is the minimum required to generate all subsets.

```cpp
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> result;
        int n = nums.size();
        for (int i = 0; i < (1 << n); i++) {
            vector<int> subset;
            for (int j = 0; j < n; j++) {
                if ((i & (1 << j)) != 0) {
                    subset.push_back(nums[j]);
                }
            }
            result.push_back(subset);
        }
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the size of the input array. This is because we generate $2^n$ subsets, and each subset takes $O(n)$ time to generate.
> - **Space Complexity:** $O(2^n \cdot n)$, where $n$ is the size of the input array. This is because we store $2^n$ subsets in the result list, and each subset takes $O(n)$ space.
> - **Optimality proof:** This approach is optimal because it generates all subsets in $O(2^n \cdot n)$ time complexity, which is the minimum required to generate all subsets.

---

### Alternative Approach

**Explanation:**
- Different perspective or technique: We can use recursion to generate all subsets. This approach is similar to the brute force approach but uses recursion instead of iteration.
- Unique trade-offs: This approach has the same time and space complexity as the optimal approach but uses recursion instead of iteration.
- Scenarios where this approach might be preferred: This approach might be preferred when working with recursive data structures or when the problem requires a recursive solution.

```cpp
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> subset;
        generateSubsets(nums, 0, subset, result);
        return result;
    }
    
    void generateSubsets(vector<int>& nums, int start, vector<int>& subset, vector<vector<int>>& result) {
        result.push_back(subset);
        for (int i = start; i < nums.size(); i++) {
            subset.push_back(nums[i]);
            generateSubsets(nums, i + 1, subset, result);
            subset.pop_back();
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the size of the input array. This is because we generate $2^n$ subsets, and each subset takes $O(n)$ time to generate.
> - **Space Complexity:** $O(2^n \cdot n)$, where $n$ is the size of the input array. This is because we store $2^n$ subsets in the result list, and each subset takes $O(n)$ space.
> - **Trade-off analysis:** This approach has the same time and space complexity as the optimal approach but uses recursion instead of iteration. This approach might be preferred when working with recursive data structures or when the problem requires a recursive solution.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Bit manipulation, recursion, and subset generation.
- Problem-solving patterns identified: Using bit manipulation to generate all subsets, using recursion to generate all subsets.
- Optimization techniques learned: Using bit manipulation to reduce the time complexity of generating all subsets.
- Similar problems to practice: Generating all permutations of a given array, generating all combinations of a given array.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, not checking for duplicate subsets.
- Edge cases to watch for: Empty input array, input array with duplicates.
- Performance pitfalls: Using inefficient algorithms to generate all subsets, not optimizing the solution for large input arrays.
- Testing considerations: Testing the solution with different input arrays, testing the solution with edge cases.