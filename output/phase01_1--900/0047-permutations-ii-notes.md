## Permutations II
**Problem Link:** https://leetcode.com/problems/permutations-ii/description

**Problem Statement:**
- Input: An array of integers `nums` containing duplicates.
- Output: All unique permutations of the input array.
- Key requirements: 
    * The input array may contain duplicate elements.
    * The output should only include unique permutations.
- Example test cases:
    * Input: `nums = [1,1,2]`
    * Output: `[[1,1,2],[1,2,1],[2,1,1]]`
    * Explanation: The output includes all unique permutations of the input array.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all permutations of the input array and then remove duplicates.
- Step-by-step breakdown of the solution:
    1. Use a recursive function to generate all permutations of the input array.
    2. Store the generated permutations in a set to automatically remove duplicates.
- Why this approach comes to mind first: It is a straightforward and intuitive solution that leverages the concept of recursion to generate permutations.

```cpp
#include <vector>
#include <set>
#include <algorithm>

class Solution {
public:
    std::vector<std::vector<int>> permuteUnique(std::vector<int>& nums) {
        std::set<std::vector<int>> uniquePermutations;
        std::sort(nums.begin(), nums.end());
        permute(nums, 0, nums.size() - 1, uniquePermutations);
        std::vector<std::vector<int>> result(uniquePermutations.begin(), uniquePermutations.end());
        return result;
    }

private:
    void permute(std::vector<int>& nums, int left, int right, std::set<std::vector<int>>& uniquePermutations) {
        if (left == right) {
            uniquePermutations.insert(nums);
        } else {
            for (int i = left; i <= right; i++) {
                std::swap(nums[left], nums[i]);
                permute(nums, left + 1, right, uniquePermutations);
                std::swap(nums[left], nums[i]); // backtrack
            }
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(\frac{n!}{k!})$, where $n$ is the number of elements in the input array and $k$ is the number of duplicates for each element. This is because we are generating all permutations and then removing duplicates.
> - **Space Complexity:** $O(\frac{n!}{k!})$, as we need to store all unique permutations in the set.
> - **Why these complexities occur:** The brute force approach involves generating all permutations, which has a high time complexity. The space complexity is also high due to the need to store all unique permutations.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a recursive function with backtracking to generate permutations, and skip duplicates by sorting the input array and checking for duplicate elements.
- Detailed breakdown of the approach:
    1. Sort the input array to group duplicate elements together.
    2. Use a recursive function with backtracking to generate permutations.
    3. Skip duplicates by checking if the current element is the same as the previous one.
- Proof of optimality: This approach has a lower time complexity than the brute force approach because it avoids generating duplicate permutations.

```cpp
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> permuteUnique(std::vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        std::vector<std::vector<int>> result;
        std::vector<bool> visited(nums.size(), false);
        std::vector<int> currentPermutation;
        permute(nums, result, currentPermutation, visited);
        return result;
    }

private:
    void permute(std::vector<int>& nums, std::vector<std::vector<int>>& result, std::vector<int>& currentPermutation, std::vector<bool>& visited) {
        if (currentPermutation.size() == nums.size()) {
            result.push_back(currentPermutation);
        } else {
            for (int i = 0; i < nums.size(); i++) {
                if (visited[i] || (i > 0 && nums[i] == nums[i - 1] && !visited[i - 1])) {
                    continue;
                }
                visited[i] = true;
                currentPermutation.push_back(nums[i]);
                permute(nums, result, currentPermutation, visited);
                currentPermutation.pop_back();
                visited[i] = false;
            }
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(\frac{n!}{k!})$, where $n$ is the number of elements in the input array and $k$ is the number of duplicates for each element. This is because we are generating all unique permutations.
> - **Space Complexity:** $O(n)$, as we need to store the recursive call stack and the current permutation.
> - **Optimality proof:** This approach is optimal because it generates all unique permutations without generating duplicates, resulting in a lower time complexity than the brute force approach.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: recursion, backtracking, and duplicate skipping.
- Problem-solving patterns identified: sorting the input array to group duplicate elements together and using a recursive function with backtracking to generate permutations.
- Optimization techniques learned: skipping duplicates by checking for duplicate elements.

**Mistakes to Avoid:**
- Common implementation errors: not checking for duplicate elements, not sorting the input array, and not using a recursive function with backtracking.
- Edge cases to watch for: input arrays with duplicate elements, empty input arrays, and input arrays with a single element.
- Performance pitfalls: generating duplicate permutations, not using a recursive function with backtracking, and not skipping duplicates.