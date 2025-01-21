## Calculator with Method Chaining

**Problem Link:** https://leetcode.com/problems/calculator-with-method-chaining/description

**Problem Statement:**
- Input format and constraints: The problem involves implementing a calculator that supports addition, subtraction, multiplication, and division operations. The calculator should allow method chaining, meaning that operations can be performed in a sequence without needing to call a separate function for each operation.
- Expected output format: The calculator should return the result of the operations as a floating-point number.
- Key requirements and edge cases to consider: The calculator should handle division by zero, and it should also handle cases where the input is not a number.
- Example test cases with explanations:
  - `Calculator calculator;`
  - `calculator.add(2).multiply(3).divide(1).subtract(1);` should return `5`.
  - `calculator.add(1).add(2).subtract(1);` should return `2`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves creating a class with methods for each operation. Each method would perform the operation and return the result.
- Step-by-step breakdown of the solution:
  1. Create a class `Calculator` with a private member variable `result` to store the current result.
  2. Implement methods for each operation (add, subtract, multiply, divide).
  3. In each method, perform the operation and update the `result` variable.
  4. Return the `result` variable after each operation.
- Why this approach comes to mind first: This approach is straightforward and easy to implement. However, it does not support method chaining.

```cpp
class Calculator {
private:
    double result;

public:
    Calculator() : result(0) {}

    double add(double num) {
        result += num;
        return result;
    }

    double subtract(double num) {
        result -= num;
        return result;
    }

    double multiply(double num) {
        result *= num;
        return result;
    }

    double divide(double num) {
        if (num == 0) {
            throw runtime_error("Division by zero");
        }
        result /= num;
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for each operation, since we are simply performing a constant amount of work for each operation.
> - **Space Complexity:** $O(1)$, since we are using a constant amount of space to store the `result` variable.
> - **Why these complexities occur:** These complexities occur because we are not using any data structures that grow with the input size, and we are not performing any loops that depend on the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: To support method chaining, we need to return the `Calculator` object itself after each operation. This way, we can chain multiple operations together.
- Detailed breakdown of the approach:
  1. Modify the `add`, `subtract`, `multiply`, and `divide` methods to return the `Calculator` object itself.
  2. Update the `result` variable as before, but return `*this` instead of `result`.
- Proof of optimality: This approach is optimal because it supports method chaining while still maintaining a constant time and space complexity for each operation.
- Why further optimization is impossible: We cannot further optimize the time or space complexity because we are already performing a constant amount of work for each operation, and we are not using any data structures that grow with the input size.

```cpp
class Calculator {
private:
    double result;

public:
    Calculator() : result(0) {}

    Calculator& add(double num) {
        result += num;
        return *this;
    }

    Calculator& subtract(double num) {
        result -= num;
        return *this;
    }

    Calculator& multiply(double num) {
        result *= num;
        return *this;
    }

    Calculator& divide(double num) {
        if (num == 0) {
            throw runtime_error("Division by zero");
        }
        result /= num;
        return *this;
    }

    double getResult() {
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for each operation, since we are simply performing a constant amount of work for each operation.
> - **Space Complexity:** $O(1)$, since we are using a constant amount of space to store the `result` variable.
> - **Optimality proof:** This approach is optimal because it supports method chaining while still maintaining a constant time and space complexity for each operation.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Method chaining, operator overloading, and exception handling.
- Problem-solving patterns identified: Using a class to encapsulate data and behavior, and using methods to perform operations.
- Optimization techniques learned: Returning the object itself to support method chaining.
- Similar problems to practice: Implementing a stack or queue using a linked list, and implementing a calculator with a more complex syntax.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to update the `result` variable, or returning the wrong value.
- Edge cases to watch for: Division by zero, and handling cases where the input is not a number.
- Performance pitfalls: Using a data structure that grows with the input size, or performing operations that depend on the input size.
- Testing considerations: Testing the calculator with different inputs and operations, and testing for edge cases.