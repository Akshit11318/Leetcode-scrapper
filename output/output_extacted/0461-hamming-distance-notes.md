## Hamming Distance

**Problem Link:** https://leetcode.com/problems/hamming-distance/description

**Problem Statement:**
- Input format and constraints: The problem takes two integers `x` and `y` as input and returns the Hamming distance between them. The Hamming distance is the number of positions at which the corresponding bits are different.
- Expected output format: The function should return an integer representing the Hamming distance between `x` and `y`.
- Key requirements and edge cases to consider: The function should handle all possible integer values of `x` and `y`, including negative numbers and zero.
- Example test cases with explanations: 
  - For `x = 1` and `y = 4`, the binary representations are `1` and `100`, respectively. The Hamming distance is `2`.
  - For `x = 0` and `y = 0`, the binary representations are `0` and `0`, respectively. The Hamming distance is `0`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves converting the integers to binary strings, iterating over each bit, and counting the number of positions where the bits are different.
- Step-by-step breakdown of the solution: 
  1. Convert `x` and `y` to binary strings.
  2. Initialize a counter for the Hamming distance.
  3. Iterate over each bit in the binary strings.
  4. If the bits at the current position are different, increment the counter.
  5. Return the counter as the Hamming distance.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it may not be the most efficient solution.

```cpp
class Solution {
public:
    int hammingDistance(int x, int y) {
        // Convert x and y to binary strings
        string x_str = bitset<32>(x).to_string();
        string y_str = bitset<32>(y).to_string();
        
        // Initialize a counter for the Hamming distance
        int distance = 0;
        
        // Iterate over each bit in the binary strings
        for (int i = 0; i < 32; i++) {
            // If the bits at the current position are different, increment the counter
            if (x_str[i] != y_str[i]) {
                distance++;
            }
        }
        
        // Return the counter as the Hamming distance
        return distance;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, because we are iterating over a fixed number of bits (32 bits for integers).
> - **Space Complexity:** $O(1)$, because we are using a fixed amount of space to store the binary strings and the counter.
> - **Why these complexities occur:** The time complexity is constant because we are iterating over a fixed number of bits, and the space complexity is constant because we are using a fixed amount of space to store the binary strings and the counter.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use bitwise operations to calculate the Hamming distance.
- Detailed breakdown of the approach: 
  1. Calculate the bitwise XOR of `x` and `y`. This will give us a binary number where each bit is `1` if the corresponding bits in `x` and `y` are different, and `0` otherwise.
  2. Count the number of `1` bits in the result. This will give us the Hamming distance.
- Proof of optimality: This approach is optimal because it uses a single bitwise operation to calculate the XOR, and then a single loop to count the number of `1` bits.
- Why further optimization is impossible: This approach is already optimal because it uses the minimum number of operations required to calculate the Hamming distance.

```cpp
class Solution {
public:
    int hammingDistance(int x, int y) {
        // Calculate the bitwise XOR of x and y
        int xor_result = x ^ y;
        
        // Initialize a counter for the Hamming distance
        int distance = 0;
        
        // Count the number of 1 bits in the result
        while (xor_result) {
            // If the least significant bit is 1, increment the counter
            distance += xor_result & 1;
            // Right shift the result to remove the least significant bit
            xor_result >>= 1;
        }
        
        // Return the counter as the Hamming distance
        return distance;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log n)$, where $n$ is the number of bits in the integer. This is because we are iterating over the bits of the integer in the while loop.
> - **Space Complexity:** $O(1)$, because we are using a fixed amount of space to store the XOR result and the counter.
> - **Optimality proof:** This approach is optimal because it uses the minimum number of operations required to calculate the Hamming distance.

---

### Alternative Approach

**Explanation:**
- Different perspective or technique: We can use the built-in `__builtin_popcount` function in C++ to count the number of `1` bits in the XOR result.
- Unique trade-offs: This approach is more concise and easier to read, but it may not be as efficient as the optimal approach.
- Scenarios where this approach might be preferred: This approach might be preferred when readability and conciseness are more important than performance.
- Comparison with optimal approach: This approach is less efficient than the optimal approach because it uses a function call to count the number of `1` bits, whereas the optimal approach uses a simple loop.

```cpp
class Solution {
public:
    int hammingDistance(int x, int y) {
        // Calculate the bitwise XOR of x and y
        int xor_result = x ^ y;
        
        // Count the number of 1 bits in the result using __builtin_popcount
        return __builtin_popcount(xor_result);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, because the `__builtin_popcount` function is typically implemented in hardware or using a single instruction.
> - **Space Complexity:** $O(1)$, because we are using a fixed amount of space to store the XOR result.
> - **Trade-off analysis:** This approach is less efficient than the optimal approach because it uses a function call to count the number of `1` bits, but it is more concise and easier to read.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Bitwise operations, counting the number of `1` bits in a binary number.
- Problem-solving patterns identified: Using bitwise operations to solve problems involving binary numbers.
- Optimization techniques learned: Using a simple loop to count the number of `1` bits instead of a function call.
- Similar problems to practice: Other problems involving bitwise operations, such as calculating the bitwise AND or OR of two numbers.

**Mistakes to Avoid:**
- Common implementation errors: Using a function call to count the number of `1` bits instead of a simple loop.
- Edge cases to watch for: Handling negative numbers and zero correctly.
- Performance pitfalls: Using a function call to count the number of `1` bits instead of a simple loop.
- Testing considerations: Testing the function with different input values, including negative numbers and zero.