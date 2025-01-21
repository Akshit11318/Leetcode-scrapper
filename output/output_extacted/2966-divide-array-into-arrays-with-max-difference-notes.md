## Divide Array into Arrays with Max Difference
**Problem Link:** https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/description

**Problem Statement:**
- Input format and constraints: The problem requires dividing an array into the maximum number of non-empty subarrays such that each subarray has a unique difference between adjacent elements.
- Expected output format: The maximum number of subarrays that can be formed under the given conditions.
- Key requirements and edge cases to consider: The input array can contain duplicate elements, and the difference between adjacent elements in each subarray must be unique.
- Example test cases with explanations: 
  - For the array `[1, 2, 3, 4, 5]`, the maximum number of subarrays is 1 because the entire array has a constant difference of 1 between adjacent elements.
  - For the array `[1, 2, 1]`, the maximum number of subarrays is 2 because we can divide it into `[1, 2]` and `[1]`, each having a unique difference.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves checking all possible divisions of the array and verifying if each division satisfies the condition of having a unique difference between adjacent elements.
- Step-by-step breakdown of the solution:
  1. Generate all possible divisions of the array.
  2. For each division, calculate the differences between adjacent elements in each subarray.
  3. Check if all differences in each subarray are unique.
  4. If a division satisfies the condition, count it as a valid division.
- Why this approach comes to mind first: It's the most straightforward way to solve the problem, involving checking all possibilities.

```cpp
#include <iostream>
#include <vector>

int maxDivisions(std::vector<int>& nums) {
    int n = nums.size();
    int maxDiv = 0;
    
    // Generate all possible divisions
    for (int mask = 1; mask < (1 << (n - 1)); ++mask) {
        int divCount = 0;
        int prev = nums[0];
        std::vector<int> diffs;
        
        for (int i = 1; i < n; ++i) {
            if ((mask & (1 << (i - 1))) != 0) {
                // Check unique differences in current subarray
                bool uniqueDiffs = true;
                for (int diff : diffs) {
                    if (diff == (nums[i] - prev)) {
                        uniqueDiffs = false;
                        break;
                    }
                }
                if (uniqueDiffs) {
                    divCount++;
                    diffs.clear();
                } else {
                    break;
                }
            }
            diffs.push_back(nums[i] - prev);
            prev = nums[i];
        }
        
        // Update max divisions if current division is valid
        if (divCount > maxDiv) {
            maxDiv = divCount;
        }
    }
    
    return maxDiv;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{n-1} \cdot n)$, where $n$ is the size of the input array. This is because we generate all possible divisions of the array, which is $2^{n-1}$, and for each division, we perform operations that take $O(n)$ time.
> - **Space Complexity:** $O(n)$, as we need to store the differences between adjacent elements for each subarray.
> - **Why these complexities occur:** The exponential time complexity comes from generating all possible divisions, and the linear space complexity comes from storing the differences for each subarray.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of generating all possible divisions, we can use a greedy approach to divide the array into subarrays with unique differences.
- Detailed breakdown of the approach:
  1. Initialize an empty result vector to store the subarrays.
  2. Iterate through the input array, maintaining a set of differences seen so far in the current subarray.
  3. When a new difference is encountered that is not in the set, add the current subarray to the result and start a new subarray.
- Proof of optimality: This approach is optimal because it ensures that each subarray has unique differences between adjacent elements and maximizes the number of subarrays by greedily dividing the array as soon as a repeated difference is found.

```cpp
#include <iostream>
#include <vector>
#include <unordered_set>

int maxDivisions(std::vector<int>& nums) {
    int n = nums.size();
    int maxDiv = 0;
    std::unordered_set<int> diffs;
    
    for (int i = 0; i < n; ++i) {
        diffs.clear();
        for (int j = i + 1; j < n; ++j) {
            int diff = nums[j] - nums[j - 1];
            if (diffs.find(diff) != diffs.end()) {
                break;
            }
            diffs.insert(diff);
        }
        maxDiv++;
        i += diffs.size();
    }
    
    return maxDiv;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of the input array. This is because we make a single pass through the array, and the operations inside the loop take constant time on average due to the use of an unordered set.
> - **Space Complexity:** $O(n)$, as in the worst case, we might need to store all elements in the set of differences.
> - **Optimality proof:** This approach is optimal because it ensures that each subarray has unique differences between adjacent elements and maximizes the number of subarrays by greedily dividing the array as soon as a repeated difference is found.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Greedy algorithms, set operations for efficient lookups.
- Problem-solving patterns identified: Using a set to keep track of unique elements, greedy division of the array based on the problem's constraints.
- Optimization techniques learned: Reducing the number of divisions by using a greedy approach, utilizing data structures like unordered sets for efficient operations.
- Similar problems to practice: Problems involving array divisions, unique differences, or greedy algorithms.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling edge cases, such as an empty input array or an array with a single element.
- Edge cases to watch for: Arrays with duplicate elements, arrays with a constant difference between adjacent elements.
- Performance pitfalls: Using inefficient data structures or algorithms that lead to high time or space complexity.
- Testing considerations: Thoroughly testing the solution with various input cases, including edge cases and large inputs to ensure correctness and efficiency.