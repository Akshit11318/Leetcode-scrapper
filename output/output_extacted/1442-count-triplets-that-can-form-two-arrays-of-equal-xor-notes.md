## Count Triplets That Can Form Two Arrays of Equal XOR

**Problem Link:** https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/description

**Problem Statement:**
- Given an array of integers `arr`, count the number of triplets that can form two arrays of equal XOR.
- The input array `arr` will contain `n` integers, where `1 <= n <= 10^5`.
- The expected output is the number of triplets that satisfy the condition.
- Key requirements and edge cases to consider: handling duplicate elements, ensuring distinct triplets, and optimizing for large inputs.
- Example test cases with explanations: 
    - For `arr = [2,3,1,6,7]`, one triplet is `[2,3,1]` because `2 XOR 3 XOR 1 = 0` and `2 XOR 1 = 3`, `3 XOR 1 = 2`, thus `2 XOR 3 = 1`.
    - For `arr = [1,1,2,2]`, no such triplets exist.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking every possible triplet in the array to see if it can form two arrays of equal XOR.
- Step-by-step breakdown: 
    1. Generate all possible triplets from the input array.
    2. For each triplet, calculate the XOR of the three elements.
    3. Then, calculate the XOR of all possible pairs within the triplet and compare them to find pairs with equal XOR.
- Why this approach comes to mind first: It is straightforward and ensures that all possible combinations are considered.

```cpp
#include <iostream>
#include <vector>

int countTriplets(std::vector<int>& arr) {
    int n = arr.size();
    int count = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            for (int k = j + 1; k < n; k++) {
                int xorAll = arr[i] ^ arr[j] ^ arr[k];
                if (xorAll == 0) {
                    int xor12 = arr[i] ^ arr[j];
                    int xor13 = arr[i] ^ arr[k];
                    int xor23 = arr[j] ^ arr[k];
                    if (xor12 == xor13 || xor12 == xor23 || xor13 == xor23) {
                        count++;
                    }
                }
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the number of elements in the array, due to the three nested loops.
> - **Space Complexity:** $O(1)$, as no additional space that scales with input size is used.
> - **Why these complexities occur:** The brute force approach checks every possible triplet, resulting in cubic time complexity, but it does not require additional space that grows with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of generating all triplets and checking their XOR, we can use a hashmap to store the XOR of pairs and then check for triplets that satisfy the condition.
- Detailed breakdown: 
    1. Create a hashmap `xorMap` to store the XOR of pairs and their frequencies.
    2. Iterate through the array to generate all possible pairs and calculate their XOR, storing it in `xorMap`.
    3. Then, for each element in the array, calculate the XOR with every other element and check if this XOR exists in `xorMap`.
- Why further optimization is impossible: This approach reduces the time complexity significantly by avoiding the generation of all triplets and using a hashmap for efficient lookup.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>

int countTriplets(std::vector<int>& arr) {
    int n = arr.size();
    int count = 0;
    std::unordered_map<int, int> xorMap;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            int xorIJ = arr[i] ^ arr[j];
            xorMap[xorIJ]++;
        }
    }
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            for (int k = j + 1; k < n; k++) {
                int xorAll = arr[i] ^ arr[j] ^ arr[k];
                if (xorAll == 0) {
                    int xor12 = arr[i] ^ arr[j];
                    int xor13 = arr[i] ^ arr[k];
                    int xor23 = arr[j] ^ arr[k];
                    if (xor12 == xor13 || xor12 == xor23 || xor13 == xor23) {
                        count++;
                    }
                }
            }
        }
    }
    return count;
}
```

However, we realize that our initial optimal approach still has room for improvement as it does not fully utilize the hashmap to its potential for reducing the time complexity. Let's reconsider and refine our optimal approach:

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>

int countTriplets(std::vector<int>& arr) {
    int n = arr.size();
    int count = 0;
    std::unordered_map<int, int> xorMap;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            int xorIJ = arr[i] ^ arr[j];
            if (xorMap.find(xorIJ) != xorMap.end()) {
                count += xorMap[xorIJ];
            }
            xorMap[xorIJ]++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of elements in the array, due to the two nested loops.
> - **Space Complexity:** $O(n^2)$, for storing the XOR of pairs in the hashmap.
> - **Optimality proof:** This approach is optimal because it minimizes the number of operations required to find all triplets that can form two arrays of equal XOR, leveraging the hashmap for efficient storage and lookup of XOR values.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: hashmap usage, XOR properties, and optimization techniques.
- Problem-solving patterns identified: reducing time complexity by avoiding unnecessary operations and using data structures for efficient lookup.
- Optimization techniques learned: utilizing hashmaps to store intermediate results and reduce the number of operations.
- Similar problems to practice: other problems involving XOR, hashmap, and optimization.

**Mistakes to Avoid:**
- Common implementation errors: incorrect hashmap usage, missing edge cases, and inefficient algorithms.
- Edge cases to watch for: duplicate elements, empty arrays, and arrays with a single element.
- Performance pitfalls: using brute force approaches for large inputs and not optimizing for time complexity.
- Testing considerations: thoroughly testing with various inputs, including edge cases, to ensure correctness and efficiency.