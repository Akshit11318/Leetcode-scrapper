## Identify the Largest Outlier in an Array

**Problem Link:** https://leetcode.com/problems/identify-the-largest-outlier-in-an-array/description

**Problem Statement:**
- Input format and constraints: Given an array of integers `nums`, identify the largest outlier in the array. An outlier is an integer that is not part of a sequence of consecutive integers of length at least 3.
- Expected output format: Return the largest outlier in the array. If no such outlier exists, return -1.
- Key requirements and edge cases to consider: Handle arrays with less than 3 elements, arrays with no outliers, and arrays with multiple outliers.
- Example test cases with explanations:
    - Input: `nums = [1, 2, 3, 4, 5, 6]`, Output: `-1` (no outlier exists)
    - Input: `nums = [1, 2, 4, 5, 6]`, Output: `4` (4 is the largest outlier)
    - Input: `nums = [1, 3, 5, 7, 9]`, Output: `9` (9 is the largest outlier)

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check every possible sequence of consecutive integers in the array to find outliers.
- Step-by-step breakdown of the solution:
    1. Sort the array in ascending order.
    2. Iterate through the array to find sequences of consecutive integers.
    3. Keep track of the largest outlier found so far.
- Why this approach comes to mind first: It is a straightforward and intuitive solution that checks all possible sequences.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int largestOutlier(std::vector<int>& nums) {
    std::sort(nums.begin(), nums.end());
    int largestOutlier = -1;

    for (int i = 0; i < nums.size(); i++) {
        bool isOutlier = true;
        for (int j = i - 2; j <= i + 2; j++) {
            if (j >= 0 && j < nums.size() && nums[j] == nums[i] - 2) {
                isOutlier = false;
                break;
            }
            if (j >= 0 && j < nums.size() && nums[j] == nums[i] - 1) {
                isOutlier = false;
                break;
            }
            if (j >= 0 && j < nums.size() && nums[j] == nums[i] + 1) {
                isOutlier = false;
                break;
            }
            if (j >= 0 && j < nums.size() && nums[j] == nums[i] + 2) {
                isOutlier = false;
                break;
            }
        }
        if (isOutlier && nums[i] > largestOutlier) {
            largestOutlier = nums[i];
        }
    }

    return largestOutlier;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of elements in the array. This is because we are iterating through the array and for each element, we are checking its neighbors.
> - **Space Complexity:** $O(1)$, excluding the space required for the input array. This is because we are only using a constant amount of space to store the largest outlier.
> - **Why these complexities occur:** The time complexity is high because we are using nested loops to check all possible sequences, and the space complexity is low because we are only using a constant amount of space.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a `set` data structure to store the elements in the array, and then iterate through the array to find sequences of consecutive integers.
- Detailed breakdown of the approach:
    1. Create a `set` from the array to remove duplicates and have $O(1)$ lookup time.
    2. Iterate through the array and for each element, check if it is part of a sequence of consecutive integers.
    3. Keep track of the largest outlier found so far.
- Proof of optimality: This approach is optimal because it uses a `set` data structure to reduce the time complexity of checking if an element is part of a sequence.

```cpp
#include <iostream>
#include <vector>
#include <unordered_set>

int largestOutlier(std::vector<int>& nums) {
    std::unordered_set<int> numSet(nums.begin(), nums.end());
    int largestOutlier = -1;

    for (int num : nums) {
        bool isOutlier = true;
        for (int i = 1; i <= 2; i++) {
            if (numSet.find(num - i) != numSet.end()) {
                isOutlier = false;
                break;
            }
            if (numSet.find(num + i) != numSet.end()) {
                isOutlier = false;
                break;
            }
        }
        if (isOutlier && num > largestOutlier) {
            largestOutlier = num;
        }
    }

    return largestOutlier;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array. This is because we are iterating through the array once to create the `set` and once to find the largest outlier.
> - **Space Complexity:** $O(n)$, where $n$ is the number of elements in the array. This is because we are storing all elements in the `set`.
> - **Optimality proof:** This approach is optimal because it uses a `set` data structure to reduce the time complexity of checking if an element is part of a sequence, and it only iterates through the array twice.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a `set` data structure to reduce time complexity, iterating through an array to find sequences of consecutive integers.
- Problem-solving patterns identified: Breaking down the problem into smaller sub-problems, using a `set` data structure to reduce time complexity.
- Optimization techniques learned: Using a `set` data structure to reduce time complexity, iterating through an array only once to find the largest outlier.
- Similar problems to practice: Finding the longest sequence of consecutive integers in an array, finding the largest outlier in a linked list.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, not using a `set` data structure to reduce time complexity.
- Edge cases to watch for