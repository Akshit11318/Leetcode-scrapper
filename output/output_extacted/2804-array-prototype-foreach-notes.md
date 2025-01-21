## Array Prototype Foreach

**Problem Link:** https://leetcode.com/problems/array-prototype-foreach/description

**Problem Statement:**
- Input format and constraints: Implement the `Array.prototype.forEach()` method in JavaScript, which executes a provided function once for each array element.
- Expected output format: There is no output; instead, the function modifies the array or performs side effects as desired.
- Key requirements and edge cases to consider:
  - The function should handle arrays of any size.
  - It should execute the provided function for each element in the array.
  - If the provided function takes an index as an argument, it should be passed the index of the current element.
  - If the provided function takes a `this` context as an argument, it should be passed the context object.
- Example test cases with explanations:
  - Basic usage: `forEach` should iterate over the array and execute the provided function for each element.
  - Index and context: `forEach` should pass the correct index and context to the provided function.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over the array using a simple loop and execute the provided function for each element.
- Step-by-step breakdown of the solution:
  1. Loop through the array using a `for` loop.
  2. For each element, execute the provided function, passing the current element, index, and array as arguments.
- Why this approach comes to mind first: It's a straightforward and intuitive way to iterate over an array and execute a function for each element.

```cpp
// Note: This is a C++ implementation for educational purposes.
// In a real-world scenario, you would implement this in JavaScript.
void forEach(int arr[], int size, void (*func)(int, int, int*), int context) {
    for (int i = 0; i < size; i++) {
        func(arr[i], i, arr);
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of the array, because we're iterating over the array once.
> - **Space Complexity:** $O(1)$, because we're not using any additional space that scales with the input size.
> - **Why these complexities occur:** The time complexity is linear because we're executing the provided function for each element in the array. The space complexity is constant because we're not allocating any additional memory.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution is similar to the brute force approach, but with additional error checking and handling for edge cases.
- Detailed breakdown of the approach:
  1. Check if the input array is valid.
  2. Check if the provided function is valid.
  3. Loop through the array using a `for` loop.
  4. For each element, execute the provided function, passing the current element, index, and array as arguments.
- Proof of optimality: This solution is optimal because it has a linear time complexity and constant space complexity, which is the best we can achieve for this problem.

```cpp
// Note: This is a C++ implementation for educational purposes.
// In a real-world scenario, you would implement this in JavaScript.
void forEach(int arr[], int size, void (*func)(int, int, int*), int context) {
    if (arr == nullptr || func == nullptr) {
        throw std::invalid_argument("Invalid input");
    }
    for (int i = 0; i < size; i++) {
        func(arr[i], i, arr);
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of the array, because we're iterating over the array once.
> - **Space Complexity:** $O(1)$, because we're not using any additional space that scales with the input size.
> - **Optimality proof:** The time complexity is linear because we're executing the provided function for each element in the array. The space complexity is constant because we're not allocating any additional memory. This solution is optimal because it has the best possible time and space complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, function execution, and error handling.
- Problem-solving patterns identified: Checking for invalid input, handling edge cases, and optimizing for performance.
- Optimization techniques learned: Using a simple loop to iterate over the array and executing the provided function for each element.
- Similar problems to practice: Implementing other array methods, such as `map`, `filter`, and `reduce`.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for invalid input, not handling edge cases, and not optimizing for performance.
- Edge cases to watch for: Null or empty input arrays, invalid provided functions, and incorrect index or context passing.
- Performance pitfalls: Using unnecessary loops or recursive function calls, which can lead to exponential time complexity.
- Testing considerations: Testing the implementation with different input sizes, edge cases, and provided functions to ensure correctness and performance.