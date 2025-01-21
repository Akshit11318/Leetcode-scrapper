## Distribute Repeating Integers
**Problem Link:** https://leetcode.com/problems/distribute-repeating-integers/description

**Problem Statement:**
- Input format: `n` (the number of bags) and `maxOperations` (the maximum number of operations allowed).
- Constraints: `1 <= n <= 9`, `1 <= maxOperations <= 100`.
- Expected output format: The maximum number of bags that can be filled.
- Key requirements: We need to find the maximum number of bags that can be filled by distributing repeating integers.
- Edge cases to consider: When `maxOperations` is less than `n`, we cannot fill all bags.

### Brute Force Approach
**Explanation:**
- Initial thought process: Try all possible combinations of distributing integers into bags.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of integers that can be distributed into bags.
  2. For each combination, calculate the total number of operations required to distribute the integers.
  3. If the total number of operations is less than or equal to `maxOperations`, update the maximum number of bags that can be filled.
- Why this approach comes to mind first: It is a straightforward approach that tries all possible solutions.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int distributeRepeatingIntegers(int n, int maxOperations) {
    int maxBags = 0;
    // Generate all possible combinations of integers
    for (int i = 1; i <= maxOperations; i++) {
        std::vector<int> bags(n, 0);
        int operations = 0;
        for (int j = 0; j < i; j++) {
            for (int k = 0; k < n; k++) {
                bags[k]++;
                operations++;
                if (operations > maxOperations) break;
            }
            if (operations > maxOperations) break;
        }
        int filledBags = 0;
        for (int k = 0; k < n; k++) {
            if (bags[k] > 0) filledBags++;
        }
        maxBags = std::max(maxBags, filledBags);
    }
    return maxBags;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot maxOperations^2)$, where $n$ is the number of bags and $maxOperations$ is the maximum number of operations allowed. This is because we generate all possible combinations of integers and calculate the total number of operations for each combination.
> - **Space Complexity:** $O(n)$, where $n$ is the number of bags. This is because we need to store the current state of the bags.
> - **Why these complexities occur:** The brute force approach tries all possible combinations of integers, resulting in a high time complexity. The space complexity is relatively low because we only need to store the current state of the bags.

### Optimal Approach (Required)
**Explanation:**
- Key insight: We can use a greedy approach to fill the bags. We should always try to fill the bag with the smallest number of integers first.
- Detailed breakdown of the approach:
  1. Initialize the number of bags filled to 0.
  2. Initialize the number of operations performed to 0.
  3. While the number of operations performed is less than `maxOperations`, try to fill the next bag.
  4. If we can fill the next bag without exceeding `maxOperations`, increment the number of bags filled and the number of operations performed.
- Proof of optimality: This approach is optimal because it always tries to fill the bag with the smallest number of integers first, which minimizes the number of operations required.

```cpp
int distributeRepeatingIntegers(int n, int maxOperations) {
    int maxBags = 0;
    int operations = 0;
    for (int i = 1; i <= n; i++) {
        int ops = (i * (i + 1)) / 2;
        if (operations + ops <= maxOperations) {
            maxBags = i;
            operations += ops;
        } else {
            break;
        }
    }
    return maxBags;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of bags. This is because we only need to iterate over the bags once.
> - **Space Complexity:** $O(1)$, where $n$ is the number of bags. This is because we only need to store a constant amount of information.
> - **Optimality proof:** This approach is optimal because it always tries to fill the bag with the smallest number of integers first, which minimizes the number of operations required.

### Final Notes
**Learning Points:**
- Key algorithmic concepts demonstrated: Greedy approach, optimization techniques.
- Problem-solving patterns identified: Always try to fill the bag with the smallest number of integers first.
- Optimization techniques learned: Use a greedy approach to minimize the number of operations required.
- Similar problems to practice: Other optimization problems that require a greedy approach.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for the base case, not handling edge cases correctly.
- Edge cases to watch for: When `maxOperations` is less than `n`, we cannot fill all bags.
- Performance pitfalls: Using a brute force approach, which can result in a high time complexity.
- Testing considerations: Test the function with different inputs, including edge cases.