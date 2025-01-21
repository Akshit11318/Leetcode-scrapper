## Relocate Marbles

**Problem Link:** https://leetcode.com/problems/relocate-marbles/description

**Problem Statement:**
- Input format and constraints: Given an array `nums` of size `n`, each element is either 0 or 1, representing a marble of different colors. You need to relocate the marbles to one side of the array, such that the number of marbles of different colors adjacent to each other is minimized.
- Expected output format: Return the minimum number of marbles of different colors adjacent to each other.
- Key requirements and edge cases to consider: The input array will not be empty, and all elements will be either 0 or 1.
- Example test cases with explanations:
  - For the input `[1, 0, 1, 0, 1]`, the output will be 2, as we can relocate the marbles to one side of the array with two marbles of different colors adjacent to each other.
  - For the input `[1, 1, 0, 0, 1]`, the output will be 1, as we can relocate the marbles to one side of the array with one marble of different colors adjacent to each other.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves checking all possible ways to relocate the marbles and counting the number of marbles of different colors adjacent to each other in each case.
- Step-by-step breakdown of the solution:
  1. Generate all possible permutations of the input array.
  2. For each permutation, count the number of marbles of different colors adjacent to each other.
  3. Keep track of the minimum count found so far.
- Why this approach comes to mind first: The brute force approach is often the most straightforward way to solve a problem, as it involves checking all possible solutions and selecting the best one.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int minAdjacentMarbles(std::vector<int>& nums) {
    int n = nums.size();
    int minCount = n;

    // Generate all permutations of the input array
    do {
        int count = 0;
        for (int i = 0; i < n - 1; i++) {
            if (nums[i] != nums[i + 1]) {
                count++;
            }
        }

        // Update the minimum count
        minCount = std::min(minCount, count);
    } while (std::next_permutation(nums.begin(), nums.end()));

    return minCount;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n!)$, where $n$ is the size of the input array. This is because we are generating all permutations of the input array.
> - **Space Complexity:** $O(1)$, as we are not using any additional space that scales with the input size.
> - **Why these complexities occur:** The brute force approach has a high time complexity due to the generation of all permutations, but it has a low space complexity since we are not using any additional space.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of generating all permutations, we can use a sliding window approach to count the number of marbles of different colors adjacent to each other.
- Detailed breakdown of the approach:
  1. Initialize two pointers, one at the start and one at the end of the array.
  2. Count the number of marbles of different colors adjacent to each other within the window.
  3. Move the window to the right by one step and update the count.
  4. Keep track of the minimum count found so far.
- Proof of optimality: The sliding window approach has a time complexity of $O(n)$, which is optimal for this problem.

```cpp
int minAdjacentMarbles(std::vector<int>& nums) {
    int n = nums.size();
    int minCount = n;

    for (int i = 0; i < n; i++) {
        int count = 0;
        for (int j = i; j < n - 1; j++) {
            if (nums[j] != nums[j + 1]) {
                count++;
            }
        }

        // Update the minimum count
        minCount = std::min(minCount, count);
    }

    return minCount;
}
```

However, there is a better approach using the concept of `0s` and `1s` in the array.

```cpp
int minAdjacentMarbles(std::vector<int>& nums) {
    int n = nums.size();
    int ones = 0;
    int zeros = 0;

    // Count the number of ones and zeros
    for (int i = 0; i < n; i++) {
        if (nums[i] == 1) {
            ones++;
        } else {
            zeros++;
        }
    }

    return std::min(ones, zeros);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of the input array. This is because we are counting the number of ones and zeros in the array.
> - **Space Complexity:** $O(1)$, as we are not using any additional space that scales with the input size.
> - **Optimality proof:** The optimal approach has a time complexity of $O(n)$, which is the best possible time complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sliding window approach, counting of ones and zeros.
- Problem-solving patterns identified: Using a simple counting approach to solve the problem.
- Optimization techniques learned: Avoiding unnecessary permutations and using a simple counting approach.
- Similar problems to practice: Other problems that involve counting and sliding window approaches.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing variables correctly, not checking for edge cases.
- Edge cases to watch for: Empty input array, array with only ones or zeros.
- Performance pitfalls: Using unnecessary permutations, not optimizing the counting approach.
- Testing considerations: Testing the function with different input arrays, checking for correct output.