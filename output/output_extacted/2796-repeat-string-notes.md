## Repeat String
**Problem Link:** https://leetcode.com/problems/repeat-string/description

**Problem Statement:**
- Input format and constraints: Given a string `s` and an integer `n`, return the string `s` repeated `n` times.
- Expected output format: The repeated string.
- Key requirements and edge cases to consider: Handling cases where `n` is 0 or negative, and ensuring the output is a string.
- Example test cases with explanations: 
    - Input: `s = "hello", n = 3`, Output: `"hellohellohello"`
    - Input: `s = "hello", n = 0`, Output: `""`
    - Input: `s = "hello", n = -1`, Output: This case is not defined in the problem, but we can assume it should return an error or handle it according to the specific requirements.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The most straightforward way to solve this problem is to use a loop to append the string `s` to a result string `n` times.
- Step-by-step breakdown of the solution:
    1. Initialize an empty string `result`.
    2. Loop `n` times, appending `s` to `result` in each iteration.
    3. Return `result`.
- Why this approach comes to mind first: It's a simple and intuitive solution that directly addresses the problem statement.

```cpp
string repeatString(string s, int n) {
    string result = "";
    for (int i = 0; i < n; i++) {
        result += s;
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times m)$, where $m$ is the length of string `s`, because in the worst case, we are appending `s` to `result` `n` times, and each append operation takes $O(m)$ time.
> - **Space Complexity:** $O(n \times m)$, because we are storing the repeated string in `result`, which can grow up to `n` times the size of `s`.
> - **Why these complexities occur:** The time complexity is due to the loop that runs `n` times and the string append operation inside it. The space complexity is due to the storage required for the result string.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can utilize the `std::string` constructor that takes a string and a count to repeat the string, which is more efficient than appending the string in a loop.
- Detailed breakdown of the approach:
    1. Directly use the `std::string` constructor to create the repeated string.
- Proof of optimality: This approach is optimal because it avoids the overhead of a loop and the repeated append operations, directly constructing the desired output string.
- Why further optimization is impossible: This approach directly utilizes a specialized constructor for repeating a string, which is implemented in the standard library and is likely to be the most efficient method available.

```cpp
string repeatString(string s, int n) {
    return string(n, s);
}
```

However, the above code does not work as expected because the `std::string` constructor that repeats a character does not repeat a string. 

The correct optimal approach is to use the `std::string` constructor in combination with a loop to repeat the string `s` `n` times, but this would essentially be the same as the brute force approach. Alternatively, we can use the `std::string::operator+=` in a loop, but again, this would be similar to the brute force approach.

A more optimal approach would be to reserve space for the result string before the loop to avoid reallocations during the append operations:

```cpp
string repeatString(string s, int n) {
    string result;
    result.reserve(n * s.size()); // Reserve space to avoid reallocations
    for (int i = 0; i < n; i++) {
        result += s;
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times m)$, where $m$ is the length of string `s`, because we are still appending `s` to `result` `n` times, but with the optimization of reserving space beforehand.
> - **Space Complexity:** $O(n \times m)$, because we are storing the repeated string in `result`.
> - **Optimality proof:** This approach is more optimal than the brute force because it minimizes the number of reallocations needed for the result string, reducing the overall time complexity in practice.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: String manipulation, loop optimization, and space reservation.
- Problem-solving patterns identified: Using built-in functions or constructors for efficiency, optimizing loop operations, and considering space complexity.
- Optimization techniques learned: Reserving space for strings to avoid reallocations during append operations.
- Similar problems to practice: Other string manipulation problems, such as substring extraction or string reversal.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases like `n` being 0 or negative.
- Edge cases to watch for: Handling cases where `s` is an empty string or `n` is very large.
- Performance pitfalls: Not reserving space for the result string, leading to inefficient reallocations during the append operations.
- Testing considerations: Testing with various inputs, including edge cases, to ensure the function behaves as expected.