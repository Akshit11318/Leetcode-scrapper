## Classifying Triangles by Lengths

**Problem Link:** https://leetcode.com/problems/classifying-triangles-by-lengths/description

**Problem Statement:**
- Input: Three integers representing the lengths of the sides of a triangle.
- Constraints: The lengths are positive integers.
- Expected Output: A string indicating whether the triangle is equilateral, isosceles, or scalene, and whether it is valid or not.
- Key Requirements:
  - A triangle is valid if the sum of the lengths of any two sides is greater than the length of the third side.
  - A triangle is equilateral if all sides have the same length.
  - A triangle is isosceles if two sides have the same length.
  - A triangle is scalene if all sides have different lengths.
- Edge Cases:
  - All sides are equal (equilateral).
  - Two sides are equal (isosceles).
  - All sides are different (scalene).
  - The sum of the lengths of any two sides is not greater than the length of the third side (invalid).
- Example Test Cases:
  - Input: [3, 3, 3], Output: "Equilateral"
  - Input: [3, 3, 4], Output: "Isosceles"
  - Input: [3, 4, 5], Output: "Scalene"
  - Input: [1, 2, 3], Output: "Invalid"

---

### Brute Force Approach

**Explanation:**
- Check all possible combinations of side lengths to determine if a triangle is valid.
- Use conditional statements to classify the triangle as equilateral, isosceles, or scalene.
- This approach is straightforward but may not be the most efficient.

```cpp
class Solution {
public:
    string triangleType(vector<int>& sides) {
        // Sort the sides in ascending order
        sort(sides.begin(), sides.end());
        
        // Check if the triangle is valid
        if (sides[0] + sides[1] <= sides[2]) {
            return "Invalid";
        }
        
        // Check if the triangle is equilateral
        if (sides[0] == sides[1] && sides[1] == sides[2]) {
            return "Equilateral";
        }
        
        // Check if the triangle is isosceles
        if (sides[0] == sides[1] || sides[1] == sides[2]) {
            return "Isosceles";
        }
        
        // If none of the above conditions are met, the triangle is scalene
        return "Scalene";
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ because we are performing a constant number of operations.
> - **Space Complexity:** $O(1)$ because we are not using any additional space that scales with the input size.
> - **Why these complexities occur:** The time and space complexities are constant because we are only checking a few conditions to classify the triangle.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal approach is the same as the brute force approach because we need to check all possible combinations of side lengths to determine if a triangle is valid and classify it.
- However, we can simplify the code by combining some of the conditional statements.

```cpp
class Solution {
public:
    string triangleType(vector<int>& sides) {
        // Sort the sides in ascending order
        sort(sides.begin(), sides.end());
        
        // Check if the triangle is valid
        if (sides[0] + sides[1] <= sides[2]) {
            return "Invalid";
        }
        
        // Check if the triangle is equilateral
        if (sides[0] == sides[2]) {
            return "Equilateral";
        }
        
        // Check if the triangle is isosceles
        if (sides[0] == sides[1] || sides[1] == sides[2]) {
            return "Isosceles";
        }
        
        // If none of the above conditions are met, the triangle is scalene
        return "Scalene";
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ because we are performing a constant number of operations.
> - **Space Complexity:** $O(1)$ because we are not using any additional space that scales with the input size.
> - **Optimality proof:** This is the optimal solution because we need to check all possible combinations of side lengths to determine if a triangle is valid and classify it.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: conditional statements, sorting.
- Problem-solving patterns identified: checking all possible combinations of side lengths.
- Optimization techniques learned: simplifying code by combining conditional statements.
- Similar problems to practice: other geometry problems, such as calculating the area of a triangle.

**Mistakes to Avoid:**
- Not checking if the triangle is valid before classifying it.
- Not considering all possible combinations of side lengths.
- Not using conditional statements correctly.
- Not testing the code with different inputs to ensure it works correctly.