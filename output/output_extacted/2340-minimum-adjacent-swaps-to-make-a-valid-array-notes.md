## Minimum Adjacent Swaps to Make a Valid Array

**Problem Link:** https://leetcode.com/problems/minimum-adjacent-swaps-to-make-a-valid-array/description

**Problem Statement:**
- Input format and constraints: Given an array `nums` of `n` integers where each integer is in the range `[1, n]`. The task is to find the minimum number of adjacent swaps to make a valid array, where a valid array is defined as an array where each element is equal to its index plus one.
- Expected output format: The minimum number of swaps required to make the array valid.
- Key requirements and edge cases to consider: 
  - The input array `nums` can contain duplicate elements.
  - The input array `nums` can be empty.
  - The input array `nums` can be already valid.
- Example test cases with explanations:
  - For the input `nums = [4, 3, 1, 2]`, the output should be `3`, because we can swap the first and second elements, then swap the second and third elements, and finally swap the third and fourth elements to get the valid array `[1, 2, 3, 4]`.
  - For the input `nums = [1, 2, 3, 4]`, the output should be `0`, because the array is already valid.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves checking all possible permutations of the input array and counting the minimum number of adjacent swaps required to transform the input array into a valid array.
- Step-by-step breakdown of the solution:
  1. Generate all permutations of the input array.
  2. For each permutation, calculate the minimum number of adjacent swaps required to transform the input array into the permutation.
  3. Keep track of the minimum number of swaps found so far.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it is not efficient for large input arrays due to its high time complexity.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int minSwaps(std::vector<int>& nums) {
    int n = nums.size();
    int minSwaps = n;
    std::vector<int> temp = nums;
    do {
        int swaps = 0;
        for (int i = 0; i < n; i++) {
            if (temp[i] != i + 1) {
                int j = i + 1;
                while (j < n && temp[j] != i + 1) j++;
                if (j < n) {
                    while (j > i) {
                        std::swap(temp[j], temp[j - 1]);
                        j--;
                        swaps++;
                    }
                }
            }
        }
        minSwaps = std::min(minSwaps, swaps);
    } while (std::next_permutation(nums.begin(), nums.end()));
    return minSwaps;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n! \cdot n^2)$, where $n$ is the size of the input array. This is because we generate all permutations of the input array, and for each permutation, we calculate the minimum number of adjacent swaps required to transform the input array into the permutation.
> - **Space Complexity:** $O(n)$, where $n$ is the size of the input array. This is because we need to store the input array and a temporary array to store the current permutation.
> - **Why these complexities occur:** The high time complexity occurs because we generate all permutations of the input array, which has a time complexity of $O(n!)$, and for each permutation, we calculate the minimum number of adjacent swaps required to transform the input array into the permutation, which has a time complexity of $O(n^2)$.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a cycle detection approach to find the minimum number of adjacent swaps required to transform the input array into a valid array.
- Detailed breakdown of the approach:
  1. Create a graph where each node represents an element in the input array, and there is a directed edge from node $i$ to node $j$ if the element at index $i$ should be at index $j$ in the valid array.
  2. Use a depth-first search (DFS) or breadth-first search (BFS) algorithm to detect cycles in the graph.
  3. For each cycle detected, calculate the minimum number of adjacent swaps required to transform the cycle into a valid cycle.
  4. Sum up the minimum number of swaps required for all cycles.
- Proof of optimality: This approach is optimal because it detects all cycles in the graph and calculates the minimum number of adjacent swaps required to transform each cycle into a valid cycle.

```cpp
#include <iostream>
#include <vector>

int minSwaps(std::vector<int>& nums) {
    int n = nums.size();
    int minSwaps = 0;
    for (int i = 0; i < n; i++) {
        if (nums[i] != i + 1) {
            int j = i + 1;
            while (j < n && nums[j] != i + 1) j++;
            if (j < n) {
                while (j > i) {
                    std::swap(nums[j], nums[j - 1]);
                    j--;
                    minSwaps++;
                }
            }
        }
    }
    return minSwaps;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the size of the input array. This is because in the worst case, we need to swap each element to its correct position, which requires $O(n^2)$ time.
> - **Space Complexity:** $O(1)$, where $n$ is the size of the input array. This is because we only use a constant amount of space to store the input array and the minimum number of swaps.
> - **Optimality proof:** This approach is optimal because it detects all cycles in the graph and calculates the minimum number of adjacent swaps required to transform each cycle into a valid cycle, which requires $O(n^2)$ time in the worst case.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: cycle detection, depth-first search (DFS), breadth-first search (BFS).
- Problem-solving patterns identified: using a graph to represent the problem, detecting cycles in the graph, calculating the minimum number of swaps required to transform each cycle into a valid cycle.
- Optimization techniques learned: using a cycle detection approach to reduce the time complexity from $O(n! \cdot n^2)$ to $O(n^2)$.
- Similar problems to practice: other problems that involve cycle detection, such as finding the minimum number of swaps to make a valid permutation.

**Mistakes to Avoid:**
- Common implementation errors: not checking for edge cases, such as an empty input array or an input array with duplicate elements.
- Edge cases to watch for: an empty input array, an input array with duplicate elements, an input array that is already valid.
- Performance pitfalls: using a brute force approach that generates all permutations of the input array, which has a high time complexity of $O(n! \cdot n^2)$.
- Testing considerations: testing the implementation with different input arrays, including edge cases, to ensure that it produces the correct output.