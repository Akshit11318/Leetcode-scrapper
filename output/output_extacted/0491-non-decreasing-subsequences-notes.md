## Non-Decreasing Subsequences

**Problem Link:** https://leetcode.com/problems/non-decreasing-subsequences/description

**Problem Statement:**
- Input: Given an integer array `nums`.
- Output: Return the number of non-decreasing subsequences.
- Key requirements: A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements.
- Edge cases: The array can be empty or contain duplicate elements.
- Example test cases:
  - Input: `nums = [1,3,5,4,7]`
  - Output: `16`
  - Explanation: The non-decreasing subsequences are `[1], [1,3], [1,3,4], [1,3,4,7], [1,3,5], [1,3,5,7], [1,4], [1,4,7], [1,5], [1,5,7], [1,7], [3], [3,4], [3,4,7], [3,5], [3,5,7], [4], [4,7], [5], [5,7], [7]`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible subsequences and check each one to see if it's non-decreasing.
- Step-by-step breakdown:
  1. Generate all possible subsequences using a recursive approach or bit manipulation.
  2. For each subsequence, check if it's non-decreasing by comparing adjacent elements.
  3. Count the number of non-decreasing subsequences.

```cpp
class Solution {
public:
    int findSubsequences(vector<int>& nums) {
        set<vector<int>> subsequences;
        vector<int> current;
        backtrack(nums, 0, current, subsequences);
        return subsequences.size();
    }
    
    void backtrack(vector<int>& nums, int start, vector<int>& current, set<vector<int>>& subsequences) {
        if (start == nums.size()) {
            if (current.size() > 1 && isNonDecreasing(current)) {
                subsequences.insert(current);
            }
            return;
        }
        // Include the current element
        current.push_back(nums[start]);
        backtrack(nums, start + 1, current, subsequences);
        current.pop_back();
        // Exclude the current element
        backtrack(nums, start + 1, current, subsequences);
    }
    
    bool isNonDecreasing(vector<int>& subsequence) {
        for (int i = 0; i < subsequence.size() - 1; i++) {
            if (subsequence[i] > subsequence[i + 1]) {
                return false;
            }
        }
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the input array. The reason is that we generate all possible subsequences using bit manipulation, which takes $O(2^n)$ time, and for each subsequence, we check if it's non-decreasing, which takes $O(n)$ time.
> - **Space Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the input array. The reason is that we store all non-decreasing subsequences in a set, which takes $O(2^n \cdot n)$ space in the worst case.
> - **Why these complexities occur:** The brute force approach generates all possible subsequences, which leads to exponential time and space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Use dynamic programming to store the count of non-decreasing subsequences ending at each position.
- Detailed breakdown:
  1. Initialize a dynamic programming array `dp` of size `n`, where `dp[i]` represents the count of non-decreasing subsequences ending at position `i`.
  2. For each position `i`, iterate over all previous positions `j` and check if the current element is greater than or equal to the element at position `j`.
  3. If it is, update `dp[i]` by adding the count of non-decreasing subsequences ending at position `j`.
  4. Return the sum of all elements in the `dp` array.

```cpp
class Solution {
public:
    int findSubsequences(vector<int>& nums) {
        unordered_set<string> subsequences;
        vector<int> current;
        backtrack(nums, 0, current, subsequences);
        return subsequences.size();
    }
    
    void backtrack(vector<int>& nums, int start, vector<int>& current, unordered_set<string>& subsequences) {
        if (start == nums.size()) {
            if (current.size() > 1) {
                string str;
                for (int num : current) {
                    str += to_string(num) + ",";
                }
                subsequences.insert(str);
            }
            return;
        }
        if (current.empty() || current.back() <= nums[start]) {
            current.push_back(nums[start]);
            backtrack(nums, start + 1, current, subsequences);
            current.pop_back();
        }
        backtrack(nums, start + 1, current, subsequences);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the input array. However, in practice, the time complexity is much less than this because we prune branches that do not lead to non-decreasing subsequences.
> - **Space Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the input array. The reason is that we store all non-decreasing subsequences in a set, which takes $O(2^n \cdot n)$ space in the worst case.
> - **Optimality proof:** The optimal approach is optimal because it uses a set to store unique non-decreasing subsequences, which eliminates duplicates and reduces the time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: backtracking, dynamic programming, and set operations.
- Problem-solving patterns identified: using a set to store unique solutions and pruning branches that do not lead to valid solutions.
- Optimization techniques learned: using a set to eliminate duplicates and reducing the time complexity by pruning branches.
- Similar problems to practice: finding the number of increasing subsequences, finding the longest increasing subsequence, and finding the number of non-decreasing subsequences with a given sum.

**Mistakes to Avoid:**
- Common implementation errors: not checking for duplicates, not pruning branches that do not lead to valid solutions, and not using a set to store unique solutions.
- Edge cases to watch for: empty input array, input array with duplicate elements, and input array with negative elements.
- Performance pitfalls: using a recursive approach without pruning branches, using a set without checking for duplicates, and not optimizing the time complexity.
- Testing considerations: testing with different input sizes, testing with different input types (e.g., empty array, array with duplicates), and testing with different edge cases (e.g., negative elements).