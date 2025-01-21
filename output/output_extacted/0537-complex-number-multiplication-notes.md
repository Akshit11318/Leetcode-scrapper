## Complex Number Multiplication
**Problem Link:** https://leetcode.com/problems/complex-number-multiplication/description

**Problem Statement:**
- Input format: Two complex numbers `num1` and `num2` as strings.
- Constraints: Each complex number is in the form `"a+bi"` or `"a-bi"`, where `a` and `b` are integers.
- Expected output format: The product of `num1` and `num2` as a string in the form `"a+bi"` or `"a-bi"`.
- Key requirements and edge cases to consider: Handling negative numbers, zero, and large inputs.
- Example test cases:
  - Input: `num1 = "1+1i", num2 = "1+1i"`
    Output: `"0+2i"`
  - Input: `num1 = "1+1i", num2 = "1-1i"`
    Output: `"2+0i"`

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Directly parse the complex numbers from the input strings, multiply them using the formula for complex number multiplication, and then construct the result string.
- Step-by-step breakdown of the solution:
  1. Parse the input strings into real and imaginary parts.
  2. Apply the complex number multiplication formula: `(a+bi)*(c+di) = (ac-bd) + (ad+bc)i`.
  3. Construct the result string in the required format.

```cpp
class Solution {
public:
    string complexNumberMultiply(string num1, string num2) {
        int a, b, c, d;
        // Parse num1
        a = stoi(num1.substr(0, num1.find('+')));
        b = stoi(num1.substr(num1.find('+')+1, num1.find('i')-num1.find('+')-1));
        
        // Parse num2
        c = stoi(num2.substr(0, num2.find('+')));
        d = stoi(num2.substr(num2.find('+')+1, num2.find('i')-num2.find('+')-1));
        
        // Calculate real and imaginary parts
        int realPart = a*c - b*d;
        int imagPart = a*d + b*c;
        
        // Construct result string
        string result = to_string(realPart) + "+" + to_string(imagPart) + "i";
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the total number of digits in the input complex numbers, because we are parsing each digit once.
> - **Space Complexity:** $O(n)$, as we need to store the parsed numbers and the result.
> - **Why these complexities occur:** The parsing and multiplication operations are linear with respect to the input size, and we store the result in a string that can grow linearly with the input size.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: The same as the brute force approach, because the problem essentially requires parsing and then applying a fixed formula. However, we can refine the parsing step for better readability and robustness.
- Detailed breakdown of the approach:
  1. Use `find` and `substr` to extract the real and imaginary parts from the input strings.
  2. Apply the complex number multiplication formula.
  3. Use `to_string` to convert the result into a string and concatenate with the appropriate signs and 'i'.
- Proof of optimality: This approach is optimal because it directly addresses the problem requirements without unnecessary overhead. Parsing and multiplication are unavoidable steps, and we perform them with minimal operations.

```cpp
class Solution {
public:
    string complexNumberMultiply(string num1, string num2) {
        int a, b, c, d;
        // Parse num1
        a = stoi(num1.substr(0, num1.find('+')));
        b = stoi(num1.substr(num1.find('+')+1, num1.find('i')-num1.find('+')-1));
        
        // Parse num2
        c = stoi(num2.substr(0, num2.find('+')));
        d = stoi(num2.substr(num2.find('+')+1, num2.find('i')-num2.find('+')-1));
        
        // Calculate real and imaginary parts
        int realPart = a*c - b*d;
        int imagPart = a*d + b*c;
        
        // Construct result string
        return to_string(realPart) + "+" + to_string(imagPart) + "i";
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the total number of digits in the input complex numbers.
> - **Space Complexity:** $O(n)$, for storing the parsed numbers and the result string.
> - **Optimality proof:** The solution has the same time and space complexity as the brute force approach because it performs the same essential operations. However, it is more refined and directly addresses the problem without unnecessary steps, making it the optimal approach.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Parsing strings, applying mathematical formulas, and constructing result strings.
- Problem-solving patterns identified: Directly addressing problem requirements with minimal overhead.
- Optimization techniques learned: Avoiding unnecessary steps and using built-in functions like `stoi` and `to_string` for efficiency.
- Similar problems to practice: Other string manipulation and mathematical problems.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect parsing, sign handling, and string construction.
- Edge cases to watch for: Negative numbers, zero, and large inputs.
- Performance pitfalls: Unnecessary loops or recursive calls.
- Testing considerations: Thoroughly test with various inputs, including edge cases.