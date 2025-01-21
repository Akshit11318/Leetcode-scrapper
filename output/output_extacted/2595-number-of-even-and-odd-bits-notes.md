## Number of Even and Odd Bits
**Problem Link:** https://leetcode.com/problems/number-of-even-and-odd-bits/description

**Problem Statement:**
- Given an integer array `bits` of size `n`, the task is to return an array `answer` where `answer[0]` is the number of even bits and `answer[1]` is the number of odd bits in the binary representation of the integers in the array.
- Input format and constraints: `bits` is an integer array of size `n`, where `1 <= n <= 500`, and each integer in `bits` is either `0` or `1`.
- Expected output format: An integer array of size `2`, where the first element is the number of even bits and the second element is the number of odd bits.
- Key requirements and edge cases to consider: The input array will only contain integers that are either `0` or `1`. The binary representation of these integers will always be a single bit.
- Example test cases with explanations:
  - For the input `[0,1,0]`, the output should be `[2,1]` because there are two even bits (two `0`s) and one odd bit (one `1`).
  - For the input `[1,1,0]`, the output should be `[1,2]` because there is one even bit (one `0`) and two odd bits (two `1`s).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We need to count the number of even and odd bits in the binary representation of the integers in the array. Since the integers in the array are either `0` or `1`, we can directly count the occurrences of `0` and `1`.
- Step-by-step breakdown of the solution:
  1. Initialize two counters, `even` and `odd`, to zero.
  2. Iterate over the array `bits`.
  3. For each integer `bit` in the array, check if it is `0` or `1`.
  4. If `bit` is `0`, increment the `even` counter.
  5. If `bit` is `1`, increment the `odd` counter.
  6. After iterating over the entire array, return an array containing the `even` and `odd` counts.

```cpp
vector<int> evenOddBitCount(vector<int>& bits) {
    int even = 0;
    int odd = 0;
    for (int bit : bits) {
        if (bit == 0) {
            even++;
        } else {
            odd++;
        }
    }
    return {even, odd};
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of the input array `bits`, because we are iterating over the array once.
> - **Space Complexity:** $O(1)$, because we are using a constant amount of space to store the counters and the output array.
> - **Why these complexities occur:** The time complexity is linear because we are iterating over the array once. The space complexity is constant because we are not using any data structures that grow with the size of the input.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution is the same as the brute force approach because we need to iterate over the entire array to count the even and odd bits. However, we can make a minor optimization by using a single loop and eliminating the conditional statement inside the loop.
- Detailed breakdown of the approach:
  1. Initialize two counters, `even` and `odd`, to zero.
  2. Iterate over the array `bits`.
  3. For each integer `bit` in the array, increment the `even` counter if `bit` is `0`, and increment the `odd` counter if `bit` is `1`.
  4. After iterating over the entire array, return an array containing the `even` and `odd` counts.

```cpp
vector<int> evenOddBitCount(vector<int>& bits) {
    int even = 0;
    int odd = 0;
    for (int bit : bits) {
        even += 1 - bit;
        odd += bit;
    }
    return {even, odd};
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of the input array `bits`, because we are iterating over the array once.
> - **Space Complexity:** $O(1)$, because we are using a constant amount of space to store the counters and the output array.
> - **Optimality proof:** This solution is optimal because we need to iterate over the entire array to count the even and odd bits. We cannot do better than linear time complexity because we need to examine each element in the array at least once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, counting, and basic arithmetic operations.
- Problem-solving patterns identified: The problem can be solved by iterating over the array and counting the occurrences of `0` and `1`.
- Optimization techniques learned: Eliminating conditional statements inside loops can improve performance.
- Similar problems to practice: Counting the occurrences of specific elements in an array, finding the maximum or minimum element in an array.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to initialize counters, using incorrect indexing, or forgetting to return the result.
- Edge cases to watch for: Empty input arrays, arrays with only one element, or arrays with all elements being the same.
- Performance pitfalls: Using unnecessary conditional statements or loops.
- Testing considerations: Test the function with different input arrays, including edge cases, to ensure it produces the correct output.