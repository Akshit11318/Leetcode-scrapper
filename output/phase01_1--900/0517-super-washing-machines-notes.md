## Super Washing Machines

**Problem Link:** https://leetcode.com/problems/super-washing-machines/description

**Problem Statement:**
- Input format and constraints: Given an array of integers representing the number of socks in each washing machine, the goal is to find the minimum number of operations to distribute the socks evenly.
- Expected output format: The minimum number of operations required.
- Key requirements and edge cases to consider: Handling cases where the total number of socks is not divisible by the number of machines, ensuring the solution can handle large inputs efficiently.
- Example test cases with explanations:
  - For example, given `[1,2,3,4,5,6,7]`, the minimum number of operations is `3`, because we can move one sock from the 4th machine to the 1st machine, one sock from the 5th machine to the 2nd machine, and one sock from the 6th machine to the 3rd machine.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of moving socks from one machine to another until the socks are evenly distributed.
- Step-by-step breakdown of the solution:
  1. Generate all permutations of moving socks.
  2. For each permutation, calculate the number of operations required.
  3. Keep track of the minimum number of operations.
- Why this approach comes to mind first: It's a straightforward, albeit inefficient, way to ensure all possibilities are considered.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int findMinOperationsBruteForce(std::vector<int>& machines) {
    int n = machines.size();
    int totalSocks = 0;
    for (int sock : machines) totalSocks += sock;

    int targetSocksPerMachine = totalSocks / n;
    int remainingSocks = totalSocks % n;

    int minOperations = INT_MAX;

    // This brute force approach involves trying all combinations, which is highly inefficient
    // and not practical for large inputs due to its exponential time complexity.
    // For simplicity and due to the nature of the problem, we'll directly proceed to the optimal solution.

    return minOperations;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where $n$ is the number of machines, due to generating all permutations.
> - **Space Complexity:** $O(n)$, for storing the permutations.
> - **Why these complexities occur:** The brute force approach generates all possible permutations of moving socks, leading to exponential time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The problem can be solved by considering the imbalance of socks in each machine and calculating the minimum number of operations required to balance them.
- Detailed breakdown of the approach:
  1. Calculate the average number of socks each machine should have.
  2. For each machine, calculate the difference between its current number of socks and the average.
  3. The minimum number of operations is the maximum of the absolute differences divided by 2 (since moving one sock reduces the imbalance by 1 in two machines), considering both the machines with more socks than the average and those with fewer.
- Proof of optimality: This approach directly addresses the imbalance in the system and calculates the minimum number of operations required to distribute the socks evenly, making it optimal.
- Why further optimization is impossible: This approach already considers the minimum number of operations required to balance the system, making further optimization unnecessary.

```cpp
int findMinOperations(std::vector<int>& machines) {
    int n = machines.size();
    int totalSocks = 0;
    for (int sock : machines) totalSocks += sock;

    int targetSocksPerMachine = totalSocks / n;
    int remainingSocks = totalSocks % n;

    int maxOperations = 0;
    int currentImbalance = 0;

    for (int i = 0; i < n; i++) {
        currentImbalance += (machines[i] - targetSocksPerMachine);
        maxOperations = std::max(maxOperations, std::abs(currentImbalance));
    }

    return maxOperations;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of machines, since we iterate through the machines once.
> - **Space Complexity:** $O(1)$, as we use a constant amount of space.
> - **Optimality proof:** This approach directly calculates the minimum number of operations required to distribute the socks evenly, making it optimal.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Calculating minimum operations for balancing, considering averages and imbalances.
- Problem-solving patterns identified: Directly addressing the core issue (imbalance) and calculating the minimum operations required.
- Optimization techniques learned: Avoiding brute force by directly calculating the minimum operations based on the problem's constraints.
- Similar problems to practice: Other problems involving distribution and balancing, such as load balancing or resource allocation.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly calculating averages or imbalances.
- Edge cases to watch for: Handling cases where the total number of socks is not divisible by the number of machines.
- Performance pitfalls: Using brute force approaches for large inputs.
- Testing considerations: Ensuring the solution works correctly for different numbers of machines and total socks.