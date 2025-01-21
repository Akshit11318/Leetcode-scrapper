## Convert the Temperature

**Problem Link:** https://leetcode.com/problems/convert-the-temperature/description

**Problem Statement:**
- Input: A temperature in `celsius` or `fahrenheit`.
- Expected Output: The temperature in both `celsius` and `fahrenheit`.
- Key requirements: Handle temperatures given in either `celsius` or `fahrenheit` and convert them to the other unit.
- Edge cases: Consider temperatures that might cause integer overflow when converted.

### Brute Force Approach

**Explanation:**
- Initial thought process: Directly apply the conversion formulas for temperatures given in `celsius` or `fahrenheit`.
- Step-by-step breakdown:
  1. Check if the input temperature is in `celsius` or `fahrenheit`.
  2. Apply the appropriate conversion formula to get the temperature in the other unit.
- Why this approach comes to mind first: The problem directly asks for temperature conversions, which are straightforward calculations.

```cpp
class Solution {
public:
    vector<double> convertTemperature(double celsius) {
        vector<double> result;
        double fahrenheit = (celsius * 9 / 5) + 32;
        result.push_back(celsius);
        result.push_back(fahrenheit);
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ because we perform a constant number of operations regardless of the input size.
> - **Space Complexity:** $O(1)$ as we use a constant amount of space to store the result.
> - **Why these complexities occur:** The conversion involves simple arithmetic operations that do not depend on the input size.

### Optimal Approach (Required)

**Explanation:**
- Key insight: Realize that the conversion formulas are already optimized for direct computation. No further optimization is needed beyond what's provided in the brute force approach.
- Detailed breakdown: Since the formulas are straightforward and do not depend on the size of the input, the optimal approach remains the same as the brute force.
- Proof of optimality: Given the nature of the problem, which involves simple arithmetic operations, it's not possible to improve upon the $O(1)$ time complexity.

```cpp
class Solution {
public:
    vector<double> convertTemperature(double celsius) {
        vector<double> result;
        double fahrenheit = (celsius * 9 / 5) + 32;
        result.push_back(celsius);
        result.push_back(fahrenheit);
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, proving this is optimal for the given problem.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space.
> - **Optimality proof:** The operation count does not increase with the input size, making the solution optimal.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: Direct application of mathematical formulas.
- Problem-solving patterns: Recognizing when a problem can be solved with simple arithmetic operations.
- Optimization techniques: Understanding that sometimes, the initial straightforward approach is already optimal.
- Similar problems to practice: Other conversion problems or simple arithmetic operations.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly applying conversion formulas or forgetting to handle edge cases.
- Edge cases to watch for: Extremely high or low temperatures that might cause integer overflow.
- Performance pitfalls: Overcomplicating the solution with unnecessary loops or recursive calls.
- Testing considerations: Ensure to test with a variety of temperatures, including edge cases like 0 degrees and very high or low temperatures.