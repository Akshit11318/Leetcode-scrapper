## Sort Array by Moving Items to Empty Space

**Problem Link:** https://leetcode.com/problems/sort-array-by-moving-items-to-empty-space/description

**Problem Statement:**
- Input: `nums` - an array of integers, and `space` - an integer representing the number of empty spaces.
- Expected Output: The modified array with the smallest numbers moved to the empty spaces.
- Key Requirements: 
  - The input array can contain both positive and negative integers, as well as zeros.
  - The `space` variable is always non-negative and represents the number of empty spaces that can be used to move items.
  - The goal is to move the smallest numbers to the empty spaces in a way that minimizes the total number of moves.
- Example Test Cases:
  - Input: `nums = [1, 3, 2], space = 2`
    - Output: `[1, 2, 3]`
    - Explanation: We can move the 2 to the empty space, resulting in the array `[1, 2, 3]`.
  - Input: `nums = [6, 4, 8], space = 1`
    - Output: `[4, 6, 8]`
    - Explanation: We can move the 4 to the empty space, resulting in the array `[4, 6, 8]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The most straightforward approach is to try all possible combinations of moves and select the one that results in the smallest numbers being moved to the empty spaces.
- Step-by-step breakdown of the solution:
  1. Generate all permutations of the input array.
  2. For each permutation, calculate the number of moves required to move the smallest numbers to the empty spaces.
  3. Select the permutation with the minimum number of moves.
- Why this approach comes to mind first: This approach is intuitive because it involves trying all possible solutions and selecting the best one.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

void generatePermutations(std::vector<int>& nums, int start, int end) {
    if (start == end) {
        // Calculate the number of moves for the current permutation
        int moves = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] != i + 1) {
                moves++;
            }
        }
        // Update the result if the current permutation has fewer moves
        // ...
    } else {
        for (int i = start; i <= end; i++) {
            std::swap(nums[start], nums[i]);
            generatePermutations(nums, start + 1, end);
            std::swap(nums[start], nums[i]);
        }
    }
}

void bruteForceApproach(std::vector<int>& nums, int space) {
    generatePermutations(nums, 0, nums.size() - 1);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n!)$, where $n$ is the length of the input array. This is because we are generating all permutations of the array.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input array. This is because we need to store the current permutation.
> - **Why these complexities occur:** The time complexity is high because we are trying all possible permutations, and the space complexity is relatively low because we only need to store the current permutation.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: The problem can be solved by sorting the array and then moving the smallest numbers to the empty spaces.
- Detailed breakdown of the approach:
  1. Sort the input array in ascending order.
  2. Move the smallest numbers to the empty spaces.
- Proof of optimality: This approach is optimal because it minimizes the number of moves required to move the smallest numbers to the empty spaces.

```cpp
void optimalApproach(std::vector<int>& nums, int space) {
    std::sort(nums.begin(), nums.end());
    for (int i = 0; i < space; i++) {
        // Move the smallest number to the empty space
        std::swap(nums[i], nums[nums.size() - space + i]);
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the length of the input array. This is because we are sorting the array.
> - **Space Complexity:** $O(1)$, where $n$ is the length of the input array. This is because we are not using any extra space.
> - **Optimality proof:** This approach is optimal because it minimizes the number of moves required to move the smallest numbers to the empty spaces.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: sorting, permutation generation.
- Problem-solving patterns identified: trying all possible solutions, using a more efficient algorithm to solve the problem.
- Optimization techniques learned: minimizing the number of moves required to solve the problem.
- Similar problems to practice: other problems involving permutation generation and optimization.

**Mistakes to Avoid:**
- Common implementation errors: not checking for edge cases, not validating input.
- Edge cases to watch for: empty input array, zero empty spaces.
- Performance pitfalls: using an inefficient algorithm, not optimizing the solution.
- Testing considerations: testing the solution with different input sizes, testing the solution with different edge cases.