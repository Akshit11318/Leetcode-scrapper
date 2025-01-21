## Total Traveled Distance
**Problem Link:** https://leetcode.com/problems/total-traveled-distance/description

**Problem Statement:**
- Input format and constraints: Given an integer `n`, representing the number of `steps`, and two integers `left` and `right`, representing the maximum steps that can be taken to the left and right respectively.
- Expected output format: The total distance traveled, assuming the person starts at the origin (0,0) and takes `n` steps, moving either `left` or `right` steps in each move.
- Key requirements and edge cases to consider: The person cannot move more steps to the left than `left`, nor more steps to the right than `right`. The total number of steps must be exactly `n`.
- Example test cases with explanations: For example, if `n = 4`, `left = 2`, `right = 3`, one possible sequence could be `[1,1,1,1]`, resulting in a total distance of `4`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to generate all possible sequences of `left` and `right` steps that add up to `n` steps.
- Step-by-step breakdown of the solution: 
  1. Generate all possible sequences of `left` and `right` steps.
  2. For each sequence, calculate the total distance traveled.
  3. Keep track of the maximum distance traveled across all sequences.
- Why this approach comes to mind first: It's a straightforward way to ensure that all possible sequences are considered.

```cpp
#include <vector>
#include <algorithm>

int totalTraveledDistance(int n, int left, int right) {
    int maxDistance = 0;
    std::vector<int> sequence(n);
    
    // Function to generate all possible sequences
    std::function<void(int)> generateSequence = [&](int step) {
        if (step == n) {
            int distance = 0;
            for (int i = 0; i < n; i++) {
                if (sequence[i] == 1) distance += left;
                else distance += right;
            }
            maxDistance = std::max(maxDistance, distance);
        } else {
            sequence[step] = 1; // left step
            if (step + left <= n) generateSequence(step + left);
            sequence[step] = 2; // right step
            if (step + right <= n) generateSequence(step + right);
        }
    };
    
    generateSequence(0);
    return maxDistance;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, as in the worst case, we might have to generate all possible sequences of `left` and `right` steps.
> - **Space Complexity:** $O(n)$, as we need to store the current sequence of steps.
> - **Why these complexities occur:** The brute force approach involves generating all possible sequences, which leads to exponential time complexity. The space complexity is linear because we only need to store the current sequence.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Since the person can only move `left` or `right` steps, the total distance traveled is determined by the number of `left` and `right` steps taken. We can use a mathematical approach to calculate the maximum distance.
- Detailed breakdown of the approach: 
  1. Calculate the maximum number of `right` steps that can be taken.
  2. Calculate the remaining steps, which must be `left` steps.
  3. Calculate the total distance traveled by multiplying the number of `right` steps by `right` and the number of `left` steps by `left`.
- Proof of optimality: This approach is optimal because it directly calculates the maximum distance traveled based on the given constraints.

```cpp
int totalTraveledDistance(int n, int left, int right) {
    int rightSteps = std::min(n, right);
    int leftSteps = n - rightSteps;
    return rightSteps * right + leftSteps * left;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, as we only need to perform a constant number of operations.
> - **Space Complexity:** $O(1)$, as we only need to use a constant amount of space.
> - **Optimality proof:** This approach is optimal because it directly calculates the maximum distance traveled based on the given constraints, without generating all possible sequences.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Mathematical approach to optimization problems.
- Problem-solving patterns identified: Using mathematical insights to simplify complex problems.
- Optimization techniques learned: Direct calculation of maximum distance traveled based on given constraints.
- Similar problems to practice: Other optimization problems that can be solved using mathematical insights.

**Mistakes to Avoid:**
- Common implementation errors: Not considering the constraints of the problem, such as the maximum number of `left` and `right` steps.
- Edge cases to watch for: Handling cases where `n` is 0 or negative.
- Performance pitfalls: Using brute force approaches for large inputs, which can lead to exponential time complexity.
- Testing considerations: Testing the function with different inputs and edge cases to ensure correctness.