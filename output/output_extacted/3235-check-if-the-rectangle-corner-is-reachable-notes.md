## Check if the Rectangle Corner is Reachable
**Problem Link:** https://leetcode.com/problems/check-if-the-rectangle-corner-is-reachable/description

**Problem Statement:**
- Input format: You are given a rectangle with integer side lengths `x` and `y` and a target point with integer coordinates `(x1, y1)`.
- Constraints: `1 <= x, y <= 10^9`, `1 <= x1, y1 <= 10^9`.
- Expected output format: Return `true` if the target point `(x1, y1)` is reachable from the bottom left corner of the rectangle, and `false` otherwise.
- Key requirements and edge cases to consider: The rectangle's sides are aligned with the axes, and the target point can only be reached by moving in the positive `x` or `y` direction.

**Example Test Cases:**
- Input: `x = 2, y = 2, x1 = 1, y1 = 1`, Output: `true`
- Input: `x = 2, y = 2, x1 = 3, y1 = 3`, Output: `false`

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Check all possible paths from the bottom left corner to the target point.
- Step-by-step breakdown of the solution:
  1. Start at the bottom left corner `(0, 0)`.
  2. Try moving in the positive `x` or `y` direction.
  3. If the target point is reached, return `true`.
  4. If all possible paths have been tried and the target point has not been reached, return `false`.
- Why this approach comes to mind first: It is a straightforward and intuitive solution.

```cpp
bool isReachable(int x, int y, int x1, int y1) {
    // Initialize the current position
    int currentX = 0;
    int currentY = 0;
    
    // Try moving in the positive x or y direction
    while (currentX < x1 && currentY < y1) {
        if (currentX < x) {
            currentX = x;
        } else if (currentY < y) {
            currentY = y;
        } else {
            break;
        }
    }
    
    // Check if the target point is reached
    return currentX == x1 && currentY == y1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(min(x, y))$ because we are moving in the positive `x` or `y` direction until we reach the target point or the boundary of the rectangle.
> - **Space Complexity:** $O(1)$ because we are using a constant amount of space to store the current position.
> - **Why these complexities occur:** The time complexity occurs because we are trying all possible paths from the bottom left corner to the target point, and the space complexity occurs because we are using a constant amount of space to store the current position.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: The target point is reachable if and only if the greatest common divisor (GCD) of `x` and `y` divides both `x1` and `y1`.
- Detailed breakdown of the approach:
  1. Calculate the GCD of `x` and `y`.
  2. Check if the GCD divides both `x1` and `y1`.
- Proof of optimality: This approach is optimal because it uses the mathematical property that the GCD of two numbers divides both numbers if and only if the two numbers are multiples of the GCD.
- Why further optimization is impossible: This approach is already optimal because it uses a mathematical property to solve the problem in constant time.

```cpp
bool isReachable(int x, int y, int x1, int y1) {
    // Calculate the GCD of x and y
    int gcd = __gcd(x, y);
    
    // Check if the GCD divides both x1 and y1
    return x1 % gcd == 0 && y1 % gcd == 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(log\ min(x, y))$ because we are using the `__gcd` function to calculate the GCD of `x` and `y`.
> - **Space Complexity:** $O(1)$ because we are using a constant amount of space to store the GCD.
> - **Optimality proof:** This approach is optimal because it uses a mathematical property to solve the problem in constant time.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: GCD calculation and mathematical properties.
- Problem-solving patterns identified: Using mathematical properties to solve problems.
- Optimization techniques learned: Using the `__gcd` function to calculate the GCD.
- Similar problems to practice: Problems involving GCD calculation and mathematical properties.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if the GCD divides both `x1` and `y1`.
- Edge cases to watch for: When `x` or `y` is 0.
- Performance pitfalls: Using a non-optimal algorithm to calculate the GCD.
- Testing considerations: Testing the function with different inputs to ensure it works correctly.