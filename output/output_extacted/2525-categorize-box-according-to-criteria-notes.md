## Categorize Box According to Criteria

**Problem Link:** https://leetcode.com/problems/categorize-box-according-to-criteria/description

**Problem Statement:**
- Input format: `length`, `width`, `height`, and `mass` of the box.
- Constraints: All dimensions and mass are positive integers.
- Expected output format: A string indicating whether the box is "Small", "Medium", or "Large" and whether it is "Light" or "Heavy".
- Key requirements: 
  - Volume = length * width * height.
  - If volume >= 10^5, the box is "Large".
  - If 10^4 <= volume < 10^5, the box is "Medium".
  - If volume < 10^4, the box is "Small".
  - If mass >= 100, the box is "Heavy".
  - If mass < 100, the box is "Light".
- Edge cases to consider: 
  - Boxes with dimensions or mass of 0 should be handled as invalid input.
  - Boxes with very large dimensions or mass should be handled correctly.

**Example Test Cases:**
- A box with dimensions (1000, 1000, 1000) and mass 50 is "Large" and "Light".
- A box with dimensions (100, 100, 100) and mass 50 is "Small" and "Light".
- A box with dimensions (1000, 1000, 1000) and mass 150 is "Large" and "Heavy".

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Calculate the volume of the box by multiplying its dimensions, then compare this volume to the given thresholds to determine if the box is "Small", "Medium", or "Large". Similarly, compare the mass to the threshold to determine if the box is "Light" or "Heavy".
- Step-by-step breakdown of the solution:
  1. Validate the input to ensure all dimensions and mass are positive.
  2. Calculate the volume of the box.
  3. Determine the size category of the box based on its volume.
  4. Determine the weight category of the box based on its mass.
  5. Combine the size and weight categories to form the final classification.

```cpp
#include <iostream>
#include <string>

std::string categorizeBox(int length, int width, int height, int mass) {
    // Validate input
    if (length <= 0 || width <= 0 || height <= 0 || mass <= 0) {
        throw std::invalid_argument("All dimensions and mass must be positive.");
    }

    // Calculate volume
    long long volume = static_cast<long long>(length) * width * height;

    // Determine size category
    std::string sizeCategory;
    if (volume >= 1e5) {
        sizeCategory = "Large";
    } else if (volume >= 1e4) {
        sizeCategory = "Medium";
    } else {
        sizeCategory = "Small";
    }

    // Determine weight category
    std::string weightCategory = (mass >= 100) ? "Heavy" : "Light";

    // Combine categories
    return sizeCategory + " " + weightCategory;
}

int main() {
    try {
        std::cout << categorizeBox(1000, 1000, 1000, 50) << std::endl;  // Large Light
        std::cout << categorizeBox(100, 100, 100, 50) << std::endl;      // Small Light
        std::cout << categorizeBox(1000, 1000, 1000, 150) << std::endl;  // Large Heavy
    } catch (const std::exception& e) {
        std::cerr << "Exception: " << e.what() << std::endl;
    }

    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ because all operations are constant time.
> - **Space Complexity:** $O(1)$ because only a constant amount of space is used to store the input and output.
> - **Why these complexities occur:** The solution involves only basic arithmetic operations and comparisons, which do not depend on the size of the input.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The problem does not require any complex algorithms or data structures. It can be solved directly by applying the given conditions.
- Detailed breakdown of the approach: The same steps as the brute force approach can be followed since they already represent the most straightforward and efficient way to solve the problem given the constraints.
- Proof of optimality: Since the problem requires checking each dimension and the mass once and performing a constant number of operations based on these values, the solution is inherently optimal with a time complexity of $O(1)$.
- Why further optimization is impossible: Given that all input values must be examined at least once to determine the box's category and that the number of operations does not grow with the size of the input, the current solution is already optimal.

The code for the optimal approach is identical to the brute force approach because it already represents the most efficient way to solve the problem under the given constraints.

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ because the number of operations does not grow with the size of the input.
> - **Space Complexity:** $O(1)$ because only a constant amount of space is used.
> - **Optimality proof:** The solution examines each input value once and performs a constant number of operations based on these values, making it optimal.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Basic arithmetic operations, conditional statements, and string manipulation.
- Problem-solving patterns identified: Direct application of problem constraints to determine the solution.
- Optimization techniques learned: Recognizing when a problem can be solved with constant time and space complexity.
- Similar problems to practice: Problems involving basic arithmetic, conditional statements, and string manipulation.

**Mistakes to Avoid:**
- Common implementation errors: Not validating input, incorrect calculation of volume, or misclassification of box size or weight.
- Edge cases to watch for: Boxes with dimensions or mass of 0, very large input values.
- Performance pitfalls: Assuming the need for complex algorithms or data structures when the problem can be solved more simply.
- Testing considerations: Ensure to test with various input sizes and edge cases to verify the correctness of the solution.