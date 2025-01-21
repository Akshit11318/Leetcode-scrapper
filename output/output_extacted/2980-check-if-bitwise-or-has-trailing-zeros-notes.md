## Check if Bitwise OR Has Trailing Zeros
**Problem Link:** https://leetcode.com/problems/check-if-bitwise-or-has-trailing-zeros/description

**Problem Statement:**
- Input: An integer `w` representing the number of bits to consider and a list of integers `nums`.
- Constraints: $1 \leq w \leq 32$, $1 \leq nums.length \leq 10^5$, $0 \leq nums[i] \leq 2^w - 1$.
- Expected Output: A boolean indicating whether the bitwise OR of all numbers in `nums` has trailing zeros.
- Key Requirements: Determine if the bitwise OR of all numbers in `nums` results in a number with trailing zeros in its binary representation.
- Example Test Cases:
  - Input: `w = 3`, `nums = [1, 2, 4]`. Output: `false`. Explanation: The bitwise OR of `1`, `2`, and `4` is `7`, which is `111` in binary, having no trailing zeros.
  - Input: `w = 3`, `nums = [1, 2, 5]`. Output: `true`. Explanation: The bitwise OR of `1`, `2`, and `5` is `7`, but when considering the leading zeros to fill `w=3` bits, it's `111`, and there are no trailing zeros in the binary representation, but the question asks about the presence of trailing zeros in a binary number that is `w` bits long. In this case, considering `w=3`, we should look at the binary as `111`, which indeed does not have trailing zeros, but it's essential to consider the context of the question which focuses on the bitwise OR operation's result in a `w`-bit context.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Calculate the bitwise OR of all numbers in `nums` and then check if the result has trailing zeros by converting it to binary and examining the least significant bits.
- Step-by-step breakdown:
  1. Initialize `result` to 0.
  2. For each number in `nums`, perform a bitwise OR operation with `result`.
  3. Convert `result` to its binary representation as a string.
  4. Check the least significant bits of the binary representation for trailing zeros.

```cpp
bool hasTrailingZeros(int w, vector<int>& nums) {
    // Calculate the bitwise OR of all numbers in nums
    int result = 0;
    for (int num : nums) {
        result |= num;
    }
    
    // Convert result to binary and check for trailing zeros
    string binary = "";
    while (result > 0) {
        binary = (result % 2 == 0 ? "0" : "1") + binary;
        result /= 2;
    }
    
    // Pad with leading zeros to match w bits
    while (binary.length() < w) {
        binary = "0" + binary;
    }
    
    // Check for trailing zeros
    for (int i = binary.length() - 1; i >= 0; --i) {
        if (binary[i] == '1') break;
        if (i == 0) return true; // All zeros, hence trailing zeros
    }
    
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + w)$, where $n$ is the number of elements in `nums` and $w$ is the number of bits. This is because we perform a constant amount of work for each number in `nums` and then potentially iterate up to $w$ times to convert the result to binary and check for trailing zeros.
> - **Space Complexity:** $O(w)$, as in the worst case, the binary representation of the result could be up to $w$ characters long.
> - **Why these complexities occur:** The bitwise OR operation is constant time per element, but converting to binary and checking for trailing zeros takes time proportional to the number of bits $w$.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of converting the result to binary and checking for trailing zeros, we can directly check if the bitwise OR operation results in a number that has any bits set in the least significant positions that would indicate the absence of trailing zeros.
- Detailed breakdown:
  1. Perform the bitwise OR operation as before.
  2. Use bitwise operations to check if there are any bits set in the least significant positions that would prevent trailing zeros.

```cpp
bool hasTrailingZeros(int w, vector<int>& nums) {
    int result = 0;
    for (int num : nums) {
        result |= num;
    }
    
    // Check if the least significant bits are all zeros
    // by using a bitmask that represents all ones in the w bits
    int bitmask = (1 << w) - 1;
    return (result & bitmask) == result;
}
```

However, this approach still requires understanding if the result has trailing zeros based on its binary representation. A more accurate optimal approach directly assesses the presence of trailing zeros without explicit binary conversion:

```cpp
bool hasTrailingZeros(int w, vector<int>& nums) {
    int orResult = 0;
    for (int num : nums) {
        orResult |= num;
    }
    
    // The presence of trailing zeros in a binary number is equivalent
    // to the number being divisible by 2 (for one trailing zero), 4 (for two trailing zeros), etc.
    // Thus, we can check if orResult is divisible by 2^k for k=1 to w.
    for (int k = 1; k <= w; k++) {
        if (orResult % (1 << k) == 0) {
            return true; // Found a divisor indicating trailing zeros
        }
    }
    
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + w)$, where $n$ is the number of elements in `nums`. The bitwise OR operation is $O(n)$, and the loop checking for divisibility by powers of 2 is $O(w)$.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the result and the bitmask.
> - **Optimality proof:** This approach is optimal because it minimizes the number of operations required to determine if the bitwise OR of the numbers in `nums` has trailing zeros, leveraging the properties of bitwise operations and divisibility.

---

### Final Notes

**Learning Points:**
- Understanding bitwise operations and their applications.
- Recognizing the relationship between binary representation and divisibility.
- Approaching problems with a focus on optimizing time and space complexity.

**Mistakes to Avoid:**
- Incorrectly assuming the need for explicit binary conversion.
- Overlooking the properties of bitwise operations that can simplify the solution.
- Failing to consider the constraints and implications of the problem statement on the solution's complexity.