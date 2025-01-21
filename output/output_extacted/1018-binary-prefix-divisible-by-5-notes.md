## Binary Prefix Divisible by 5

**Problem Link:** https://leetcode.com/problems/binary-prefix-divisible-by-5/description

**Problem Statement:**
- Input: A binary array `nums`.
- Constraints: `1 <= nums.length <= 10^5`.
- Expected output: An array `ans` of the same length as `nums`, where `ans[i]` is `true` if the binary number represented by the prefix `nums[0..i]` is divisible by 5, and `false` otherwise.
- Key requirements: The output should be computed in-place, without using any additional space that scales with the input size.

### Brute Force Approach

**Explanation:**
- Initial thought process: Convert the binary prefix to decimal and check divisibility by 5 for each prefix.
- Step-by-step breakdown of the solution:
  1. Iterate over the binary array.
  2. For each position, convert the prefix to a decimal number.
  3. Check if the decimal number is divisible by 5.
  4. Store the result in the output array.

```cpp
vector<bool> prefixesDivBy5(vector<int>& nums) {
    vector<bool> ans;
    int decimal = 0;
    for (int i = 0; i < nums.size(); i++) {
        decimal = decimal * 2 + nums[i];
        ans.push_back(decimal % 5 == 0);
    }
    return ans;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input array, because we perform a constant amount of work for each element in the array.
> - **Space Complexity:** $O(n)$, because we need to store the output array of the same length as the input array.
> - **Why these complexities occur:** The time complexity is linear because we iterate over the array once, and the space complexity is linear because we store the result for each prefix.

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of converting the binary prefix to decimal and checking divisibility by 5, we can directly manipulate the binary number in a way that allows us to check divisibility by 5 more efficiently.
- Detailed breakdown of the approach:
  1. Initialize a variable `decimal` to 0.
  2. For each bit in the binary array:
     - Shift the current decimal value to the left (multiply by 2).
     - Add the new bit to the decimal value.
     - Check if the decimal value is divisible by 5 by using the modulo operator (`%`).
     - Store the result in the output array.
- Proof of optimality: This solution has the same time complexity as the brute force approach but avoids the overhead of explicit decimal conversion, making it more efficient in practice.

```cpp
vector<bool> prefixesDivBy5(vector<int>& nums) {
    vector<bool> ans;
    int decimal = 0;
    for (int num : nums) {
        decimal = (decimal * 2 + num) % 10;
        ans.push_back(decimal == 0 || decimal == 5);
    }
    return ans;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input array, because we perform a constant amount of work for each element in the array.
> - **Space Complexity:** $O(n)$, because we need to store the output array of the same length as the input array.
> - **Optimality proof:** This solution is optimal because it achieves the minimum possible time complexity for this problem, which is linear, and it does so with a constant amount of extra space (not counting the output), making it efficient in both time and space.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Manipulation of binary numbers, divisibility checks, and efficient use of modulo arithmetic.
- Problem-solving patterns identified: The importance of directly manipulating the input data type (in this case, binary numbers) to avoid unnecessary conversions.
- Optimization techniques learned: Using properties of arithmetic operations (like the distributive property of modulo) to simplify computations.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling the modulo operation or forgetting to update the decimal value correctly.
- Edge cases to watch for: The first element of the array (since it's the simplest case and can be a common source of errors).
- Performance pitfalls: Using explicit decimal conversion when working with binary numbers, which can be slower and less efficient than direct manipulation.
- Testing considerations: Ensure that the solution works correctly for arrays of varying lengths and for different patterns of binary numbers.