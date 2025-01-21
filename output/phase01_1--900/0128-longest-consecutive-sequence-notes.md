## Longest Consecutive Sequence

**Problem Link:** [https://leetcode.com/problems/longest-consecutive-sequence/description](https://leetcode.com/problems/longest-consecutive-sequence/description)

**Problem Statement:**
- Input format: An array of integers `nums`.
- Constraints: The input array may contain duplicates and negative numbers.
- Expected output format: The length of the longest consecutive sequence.
- Key requirements and edge cases to consider: 
  - Handling duplicates and negative numbers, 
  - Identifying sequences of varying lengths, 
  - Dealing with an empty input array.
- Example test cases with explanations:
  - `nums = [100, 4, 200, 1, 3, 2]`, the output should be `4` because the longest consecutive sequence is `[1, 2, 3, 4]`.
  - `nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]`, the output should be `9` because the longest consecutive sequence is `[0, 1, 2, 3, 4, 5, 6, 7, 8]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to sort the array and then iterate through it to find the longest consecutive sequence.
- Step-by-step breakdown of the solution:
  1. Sort the input array in ascending order.
  2. Initialize variables to keep track of the current sequence length and the longest sequence found so far.
  3. Iterate through the sorted array, checking for consecutive numbers.
  4. If a number is consecutive to the previous one, increment the current sequence length.
  5. If a number is not consecutive, update the longest sequence length if necessary and reset the current sequence length.
- Why this approach comes to mind first: It's straightforward and easy to understand, making it a natural first step.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int longestConsecutive(std::vector<int>& nums) {
    if (nums.empty()) return 0;
    
    std::sort(nums.begin(), nums.end());
    
    int longestStreak = 1;
    int currentStreak = 1;
    
    for (int i = 1; i < nums.size(); ++i) {
        if (nums[i] != nums[i - 1]) { // Skip duplicates
            if (nums[i] == nums[i - 1] + 1) {
                currentStreak += 1;
            } else {
                longestStreak = std::max(longestStreak, currentStreak);
                currentStreak = 1;
            }
        }
    }
    
    return std::max(longestStreak, currentStreak);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting operation, where $n$ is the number of elements in the input array.
> - **Space Complexity:** $O(1)$ if we consider the sorting to be in-place, otherwise $O(n)$ for a sorting algorithm that requires extra space.
> - **Why these complexities occur:** The time complexity is dominated by the sorting operation, which has a logarithmic factor due to the comparison-based sorting algorithm used by `std::sort`. The space complexity depends on the sorting algorithm's implementation.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Using a `std::unordered_set` to store the numbers allows for constant time complexity when checking if a number exists, enabling a more efficient algorithm.
- Detailed breakdown of the approach:
  1. Insert all numbers into a `std::unordered_set`.
  2. Iterate through the set, for each number, check if it's the start of a sequence (i.e., `num - 1` is not in the set).
  3. If it's the start of a sequence, then check numbers that are consecutive to it and keep a count of the sequence length.
  4. Update the longest sequence length found so far.
- Proof of optimality: This approach has a linear time complexity because each number is processed at most twice (once in the outer loop and once in the inner loop), making it optimal for this problem.
- Why further optimization is impossible: The problem requires checking each number at least once to determine if it's part of a sequence, so a linear time complexity is the best achievable.

```cpp
#include <iostream>
#include <vector>
#include <unordered_set>

int longestConsecutive(std::vector<int>& nums) {
    std::unordered_set<int> numSet(nums.begin(), nums.end());
    int longestStreak = 0;
    
    for (const int num : numSet) {
        if (numSet.find(num - 1) == numSet.end()) { // Check if it's the start of a sequence
            int currentNum = num;
            int currentStreak = 1;
            
            while (numSet.find(currentNum + 1) != numSet.end()) {
                currentNum += 1;
                currentStreak += 1;
            }
            
            longestStreak = std::max(longestStreak, currentStreak);
        }
    }
    
    return longestStreak;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the input array, because each element is processed at most twice.
> - **Space Complexity:** $O(n)$ for storing the numbers in the `std::unordered_set`.
> - **Optimality proof:** The algorithm checks each number at most twice (once in the outer loop and once in the inner loop if it's the start of a sequence), ensuring a linear time complexity, which is the best achievable for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a `std::unordered_set` for efficient lookups, iterating through a set to find sequences.
- Problem-solving patterns identified: Checking for the start of a sequence, then extending it as long as possible.
- Optimization techniques learned: Reducing time complexity by using a set for constant time lookups.
- Similar problems to practice: Finding the longest increasing subsequence, longest common subsequence.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for the start of a sequence before extending it, not handling duplicates correctly.
- Edge cases to watch for: Empty input array, array with a single element, array with all elements being the same.
- Performance pitfalls: Using a sorting algorithm with a high time complexity, not using a set for efficient lookups.
- Testing considerations: Testing with arrays of varying sizes, testing with arrays containing duplicates and negative numbers.