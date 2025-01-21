## Kth Smallest Instructions
**Problem Link:** https://leetcode.com/problems/kth-smallest-instructions/description

**Problem Statement:**
- Input format and constraints: The problem takes in two integers, `k` and `n`, where `1 <= k <= n <= 10^5`.
- Expected output format: The function should return a string of length `n` consisting of only 'N', 'S', 'E', and 'W' representing the `kth` smallest instruction.
- Key requirements and edge cases to consider: The instructions are in lexicographical order and the robot starts at the origin (0,0).
- Example test cases with explanations: For `k = 3` and `n = 3`, the output should be "NES" because the instructions in lexicographical order are "NES", "NSW", "NNN", and "NES" is the 3rd smallest instruction.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible instructions of length `n` and sort them in lexicographical order.
- Step-by-step breakdown of the solution:
  1. Generate all possible instructions of length `n` using a recursive function or by using bit manipulation.
  2. Sort the generated instructions in lexicographical order.
  3. Return the `kth` smallest instruction.
- Why this approach comes to mind first: It is a straightforward approach that generates all possible solutions and then selects the `kth` smallest one.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

void generateInstructions(std::vector<std::string>& instructions, std::string current, int n) {
    if (current.size() == n) {
        instructions.push_back(current);
        return;
    }
    generateInstructions(instructions, current + "N", n);
    generateInstructions(instructions, current + "S", n);
    generateInstructions(instructions, current + "E", n);
    generateInstructions(instructions, current + "W", n);
}

std::string kthSmallestPath(int k, int n) {
    std::vector<std::string> instructions;
    generateInstructions(instructions, "", n);
    std::sort(instructions.begin(), instructions.end());
    return instructions[k - 1];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(4^n \log 4^n)$ due to generating all possible instructions and sorting them.
> - **Space Complexity:** $O(4^n)$ for storing all possible instructions.
> - **Why these complexities occur:** The brute force approach generates all possible instructions, which results in an exponential time and space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of generating all possible instructions, we can use a combinatorial approach to calculate the `kth` smallest instruction.
- Detailed breakdown of the approach:
  1. Calculate the number of instructions that start with each direction ('N', 'S', 'E', 'W').
  2. Determine the `kth` smallest instruction by iterating over the directions and calculating the number of instructions that start with each direction.
- Proof of optimality: The optimal approach has a time complexity of $O(n)$, which is much faster than the brute force approach.
- Why further optimization is impossible: The optimal approach already has a linear time complexity, which is the best possible time complexity for this problem.

```cpp
std::string kthSmallestPath(int k, int n) {
    std::string result;
    int north = n - (n / 2);
    int east = n / 2;
    for (int i = 0; i < n; i++) {
        if (north > 0 && k <= (east > 0 ? east : 1)) {
            result += 'N';
            north--;
        } else {
            result += 'E';
            east--;
            k -= (east > 0 ? east : 1);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ due to iterating over the instructions once.
> - **Space Complexity:** $O(n)$ for storing the `kth` smallest instruction.
> - **Optimality proof:** The optimal approach has a linear time complexity, which is the best possible time complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Combinatorial approach, iteration over directions.
- Problem-solving patterns identified: Calculating the number of instructions that start with each direction.
- Optimization techniques learned: Avoiding generating all possible solutions, using a combinatorial approach.
- Similar problems to practice: Other problems that involve combinatorial approaches and iteration over directions.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, not handling overflow.
- Edge cases to watch for: When `k` is 1 or `n`, when `n` is 1.
- Performance pitfalls: Generating all possible solutions, not using a combinatorial approach.
- Testing considerations: Test for edge cases, test for performance.