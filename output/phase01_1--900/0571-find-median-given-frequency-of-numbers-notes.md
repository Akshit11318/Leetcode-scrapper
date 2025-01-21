## Find Median Given Frequency of Numbers

**Problem Link:** https://leetcode.com/problems/find-median-given-frequency-of-numbers/description

**Problem Statement:**
- Input format and constraints: The input is a list of pairs, where each pair contains a number and its frequency. The numbers are integers, and the frequencies are non-negative integers.
- Expected output format: The output is a double representing the median of the numbers considering their frequencies.
- Key requirements and edge cases to consider: The input list is not empty, and the total number of elements (numbers times their frequencies) is between $1$ and $10^5$.
- Example test cases with explanations: For example, given `[[1,3],[2,2],[3,1]]`, the median is $2.0$ because the sorted list is $[1,1,1,2,2,3]$.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first step is to understand that we need to calculate the median of a list where each number appears a certain number of times. The brute force approach involves expanding each number into its frequency, sorting the resulting list, and then finding the median.
- Step-by-step breakdown of the solution:
  1. Expand each number into its frequency.
  2. Combine all the numbers into a single list.
  3. Sort the list in ascending order.
  4. Calculate the median based on whether the total count of numbers is odd or even.
- Why this approach comes to mind first: It's straightforward and easy to understand, making it a natural first step in solving the problem.

```cpp
#include <vector>
#include <algorithm>

double findMedian(std::vector<std::vector<int>>& nums) {
    std::vector<int> expanded;
    for (const auto& num : nums) {
        int value = num[0];
        int frequency = num[1];
        for (int i = 0; i < frequency; ++i) {
            expanded.push_back(value);
        }
    }
    std::sort(expanded.begin(), expanded.end());
    int n = expanded.size();
    if (n % 2 == 0) {
        return (expanded[n / 2 - 1] + expanded[n / 2]) / 2.0;
    } else {
        return expanded[n / 2];
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(N \log N)$, where $N$ is the total number of elements after expansion. This is because we sort the list, which takes $O(N \log N)$ time.
> - **Space Complexity:** $O(N)$, as we store all the expanded numbers in a list.
> - **Why these complexities occur:** The sorting operation dominates the time complexity, and storing all the numbers in memory contributes to the space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can calculate the median without expanding all the numbers. Since we only need the middle value(s), we can use a data structure that allows us to find the median efficiently, such as a balanced binary search tree or a heap. However, given the constraints of this problem, a more straightforward approach is to use the fact that the median is the middle value in the sorted list. We can iterate through the numbers and their frequencies, keeping a running count of the total numbers seen so far. When we reach the middle index (or indices for an even total count), we can calculate the median.
- Detailed breakdown of the approach:
  1. Initialize variables to keep track of the total count and the current index.
  2. Iterate through the numbers and their frequencies.
  3. For each number, add its frequency to the total count and check if we've reached the middle index.
  4. If we have, calculate the median based on whether the total count is odd or even.
- Proof of optimality: This approach avoids the need to expand all the numbers and sort them, reducing the time complexity significantly.

```cpp
double findMedian(std::vector<std::vector<int>>& nums) {
    int total = 0;
    for (const auto& num : nums) {
        total += num[1];
    }
    int target = total / 2;
    int current = 0;
    int prev = 0;
    for (const auto& num : nums) {
        int value = num[0];
        int frequency = num[1];
        if (current + frequency > target) {
            if (total % 2 == 0) {
                if (current + frequency - target == 1) {
                    return (prev + value) / 2.0;
                } else {
                    return value;
                }
            } else {
                return value;
            }
        }
        current += frequency;
        prev = value;
    }
    return 0.0; // This line should not be reached
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(N)$, where $N$ is the number of input pairs, not the total number of elements after expansion. This is because we iterate through the input pairs once.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the variables.
> - **Optimality proof:** This approach is optimal because it minimizes the number of operations required to find the median, avoiding unnecessary expansions and sorting.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The importance of understanding the problem constraints and finding an approach that minimizes unnecessary operations.
- Problem-solving patterns identified: Looking for ways to avoid expanding data and using iterative approaches to find medians or other statistical measures.
- Optimization techniques learned: Avoiding sorting when possible and using running counts to track progress towards a target.
- Similar problems to practice: Other problems involving statistical measures, such as finding modes or quantiles, and optimizing algorithms for specific constraints.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly calculating the median for even or odd total counts.
- Edge cases to watch for: Handling cases where the input list is empty or contains only one element.
- Performance pitfalls: Using inefficient data structures or algorithms that scale poorly with the input size.
- Testing considerations: Thoroughly testing the function with various inputs, including edge cases and large datasets.