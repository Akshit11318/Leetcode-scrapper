## Type of Triangle
**Problem Link:** https://leetcode.com/problems/type-of-triangle/description

**Problem Statement:**
- Input format: Three integers `a`, `b`, and `c` representing the sides of a triangle.
- Constraints: `1 <= a, b, c <= 10^4`.
- Expected output format: A string indicating the type of triangle (`"Equilateral"`, `"Isosceles"`, or `"Scalene"`).
- Key requirements and edge cases to consider:
  - The input sides must form a valid triangle (i.e., the sum of the lengths of any two sides must be greater than the length of the third side).
- Example test cases with explanations:
  - Input: `a = 2, b = 2, c = 2`, Output: `"Equilateral"`.
  - Input: `a = 2, b = 2, c = 3`, Output: `"Isosceles"`.
  - Input: `a = 2, b = 3, c = 4`, Output: `"Scalene"`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check all possible combinations of sides to determine the type of triangle.
- Step-by-step breakdown of the solution:
  1. Sort the sides in ascending order.
  2. Check if the triangle is valid by ensuring the sum of the lengths of any two sides is greater than the length of the third side.
  3. Compare the lengths of the sides to determine the type of triangle.
- Why this approach comes to mind first: It is a straightforward and intuitive solution.

```cpp
class Solution {
public:
    string triangleType(int a, int b, int c) {
        // Check if the triangle is valid
        if (a + b <= c || a + c <= b || b + c <= a) {
            return "Not a triangle";
        }
        
        // Sort the sides
        vector<int> sides = {a, b, c};
        sort(sides.begin(), sides.end());
        
        // Determine the type of triangle
        if (sides[0] == sides[1] && sides[1] == sides[2]) {
            return "Equilateral";
        } else if (sides[0] == sides[1] || sides[1] == sides[2]) {
            return "Isosceles";
        } else {
            return "Scalene";
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, since we are performing a constant number of operations.
> - **Space Complexity:** $O(1)$, since we are using a constant amount of space to store the sides and the result.
> - **Why these complexities occur:** The operations are simple and do not depend on the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can determine the type of triangle without sorting the sides.
- Detailed breakdown of the approach:
  1. Check if the triangle is valid by ensuring the sum of the lengths of any two sides is greater than the length of the third side.
  2. Compare the lengths of the sides to determine the type of triangle.
- Proof of optimality: This approach has the same time complexity as the brute force approach but reduces the number of operations.

```cpp
class Solution {
public:
    string triangleType(int a, int b, int c) {
        // Check if the triangle is valid
        if (a + b <= c || a + c <= b || b + c <= a) {
            return "Not a triangle";
        }
        
        // Determine the type of triangle
        if (a == b && b == c) {
            return "Equilateral";
        } else if (a == b || b == c || a == c) {
            return "Isosceles";
        } else {
            return "Scalene";
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, since we are performing a constant number of operations.
> - **Space Complexity:** $O(1)$, since we are using a constant amount of space to store the sides and the result.
> - **Optimality proof:** This approach is optimal because it has the same time complexity as the brute force approach but reduces the number of operations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Simple comparison and conditional statements.
- Problem-solving patterns identified: Checking for validity and comparing values.
- Optimization techniques learned: Reducing the number of operations.
- Similar problems to practice: Other problems involving geometric shapes and comparisons.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for validity or comparing values correctly.
- Edge cases to watch for: Invalid triangles or equal side lengths.
- Performance pitfalls: Using unnecessary operations or data structures.
- Testing considerations: Test with different input values and edge cases.