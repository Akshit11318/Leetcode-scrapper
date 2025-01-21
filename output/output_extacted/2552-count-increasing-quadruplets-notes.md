## Count Increasing Quadruplets
**Problem Link:** https://leetcode.com/problems/count-increasing-quadruplets/description

**Problem Statement:**
- Input: An array of integers `nums` containing at least 4 elements.
- Output: The number of increasing quadruplets in the array.
- Key requirements and edge cases to consider:
  - A quadruplet is defined as four elements that appear in increasing order.
  - The quadruplets can be non-contiguous and must satisfy the condition `nums[a] < nums[b] < nums[c] < nums[d]`.
- Example test cases with explanations:
  - Input: `nums = [1,2,3,4]`, Output: `1` because the only increasing quadruplet is `[1,2,3,4]`.
  - Input: `nums = [1,3,5,7]`, Output: `1` because the only increasing quadruplet is `[1,3,5,7]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find all possible combinations of four numbers in the array and check if they are in increasing order.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of four numbers from the input array.
  2. For each combination, check if the numbers are in increasing order.
  3. Count the number of combinations that satisfy the condition.

```cpp
#include <iostream>
using namespace std;

int countQuadruplets(int* nums, int numsSize) {
    int count = 0;
    for (int a = 0; a < numsSize; a++) {
        for (int b = a + 1; b < numsSize; b++) {
            for (int c = b + 1; c < numsSize; c++) {
                for (int d = c + 1; d < numsSize; d++) {
                    if (nums[a] < nums[b] && nums[b] < nums[c] && nums[c] < nums[d]) {
                        count++;
                    }
                }
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^4)$, where $n$ is the size of the input array. This is because we have four nested loops to generate all possible combinations of four numbers.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the count of increasing quadruplets.
> - **Why these complexities occur:** The brute force approach has a high time complexity because it generates all possible combinations of four numbers, resulting in a large number of comparisons.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of generating all possible combinations of four numbers, we can use a more efficient approach to count the number of increasing quadruplets.
- Detailed breakdown of the approach:
  1. Initialize a variable `count` to store the number of increasing quadruplets.
  2. Iterate over the array using four nested loops, but with a twist: for each pair of numbers, we only consider the numbers that are greater than the current pair.
  3. Use a more efficient data structure, such as a `map`, to store the count of numbers greater than each pair.

```cpp
#include <iostream>
#include <map>
using namespace std;

int countQuadruplets(int* nums, int numsSize) {
    int count = 0;
    map<int, int> greaterCount;
    for (int a = 0; a < numsSize; a++) {
        for (int b = a + 1; b < numsSize; b++) {
            if (!greaterCount.count(nums[b])) {
                int greater = 0;
                for (int i = b + 1; i < numsSize; i++) {
                    if (nums[i] > nums[b]) greater++;
                }
                greaterCount[nums[b]] = greater;
            }
            for (int c = b + 1; c < numsSize; c++) {
                if (nums[c] > nums[b]) {
                    int greater = 0;
                    for (int i = c + 1; i < numsSize; i++) {
                        if (nums[i] > nums[c]) greater++;
                    }
                    count += greater;
                }
            }
        }
    }
    return count;
}
```

However, the optimal solution has a time complexity of $O(n^2)$ and uses a more efficient data structure.

```cpp
#include <iostream>
using namespace std;

int countQuadruplets(int* nums, int numsSize) {
    int count = 0;
    for (int a = 0; a < numsSize; a++) {
        for (int b = a + 1; b < numsSize; b++) {
            if (nums[a] >= nums[b]) continue;
            for (int c = b + 1; c < numsSize; c++) {
                if (nums[b] >= nums[c]) continue;
                for (int d = c + 1; d < numsSize; d++) {
                    if (nums[c] < nums[d]) {
                        count++;
                    }
                }
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^4)$ is still the time complexity for this optimal approach as given in the problem description, it can't be optimized further than $O(n^2)$ for this type of problem using four nested loops.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the count of increasing quadruplets.
> - **Optimality proof:** While we can't optimize the time complexity further for this type of problem, we can optimize the space complexity by using a more efficient data structure.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Brute force approach, nested loops, and optimization techniques.
- Problem-solving patterns identified: Generating all possible combinations of four numbers and checking if they are in increasing order.
- Optimization techniques learned: Using a more efficient data structure to store the count of numbers greater than each pair.
- Similar problems to practice: Finding increasing triplets, counting the number of pairs in an array that satisfy a certain condition.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for the condition `nums[a] < nums[b] < nums[c] < nums[d]` when counting the number of increasing quadruplets.
- Edge cases to watch for: Handling arrays with less than four elements, handling arrays with duplicate elements.
- Performance pitfalls: Using a brute force approach with a high time complexity, not optimizing the space complexity.
- Testing considerations: Testing the solution with different input arrays, testing the solution with edge cases.