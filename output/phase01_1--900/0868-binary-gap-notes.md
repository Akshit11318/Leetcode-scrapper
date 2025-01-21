## Binary Gap

**Problem Link:** [https://leetcode.com/problems/binary-gap/description](https://leetcode.com/problems/binary-gap/description)

**Problem Statement:**
- Input format: An integer `n` representing a binary number.
- Constraints: `1 <= n <= 10^6`.
- Expected output format: The binary gap, which is the length of the longest sequence of `1`s in the binary representation of `n`, separated by `0`s.
- Key requirements and edge cases to consider:
  - Handling numbers with leading zeros in their binary representation.
  - Identifying the longest sequence of `1`s separated by `0`s.
- Example test cases with explanations:
  - Input: `5` (Binary: `101`), Output: `2` (The longest sequence is `1` followed by `1` with a `0` in between).
  - Input: `6` (Binary: `110`), Output: `1` (The longest sequence is `1` followed by `1` with no `0`s in between, but since we're looking for sequences separated by `0`s, the answer is `1` for the sequence `1` itself).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Convert the number to its binary representation, then iterate through each character to find sequences of `1`s separated by `0`s.
- Step-by-step breakdown of the solution:
  1. Convert the integer to a binary string.
  2. Initialize variables to keep track of the current gap and the maximum gap found so far.
  3. Iterate through the binary string. When a `1` is found, check if the previous character was a `0` (indicating the start of a new sequence). If so, start a new sequence count. If not, it means we're still counting the same sequence.
  4. When a `0` is found after a sequence of `1`s, update the maximum gap if the current sequence is longer.
- Why this approach comes to mind first: It directly addresses the problem by examining each character in the binary representation and keeping track of the sequences of `1`s separated by `0`s.

```cpp
#include <string>
using namespace std;

int binaryGap(int n) {
    string binary = "";
    while (n > 0) {
        binary = (n % 2 == 0 ? "0" : "1") + binary;
        n /= 2;
    }

    int maxGap = 0, currentGap = 0;
    bool sequenceStarted = false;

    for (char c : binary) {
        if (c == '1') {
            if (sequenceStarted) {
                currentGap++;
            } else {
                sequenceStarted = true;
                currentGap = 1;
            }
        } else if (sequenceStarted) {
            maxGap = max(maxGap, currentGap);
            sequenceStarted = false;
        }
    }

    return maxGap;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(log(n))$, because we're converting the number to binary and then iterating through it. The number of digits in the binary representation of `n` is $log_2(n)$.
> - **Space Complexity:** $O(log(n))$, for storing the binary representation of `n`.
> - **Why these complexities occur:** The time complexity is due to the conversion and iteration through the binary string, and the space complexity is due to storing this string.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can find the binary gap without explicitly converting the number to a binary string. Instead, we can use bitwise operations to check each bit and keep track of the distance between `1`s.
- Detailed breakdown of the approach:
  1. Initialize variables to keep track of the last seen `1` and the maximum gap.
  2. Iterate through the bits of the number from right to left using a bitwise right shift operation.
  3. When a `1` is found, update the maximum gap if the distance from the last `1` is greater than the current maximum gap.
  4. Update the position of the last seen `1`.
- Proof of optimality: This approach is optimal because it only requires a single pass through the bits of the number and uses constant space, resulting in a time complexity of $O(log(n))$ and a space complexity of $O(1)$.

```cpp
int binaryGap(int n) {
    int maxGap = 0, lastOne = -1, currentOne = 0;

    while (n > 0) {
        if (n & 1) {
            if (lastOne != -1) {
                maxGap = max(maxGap, currentOne - lastOne);
            }
            lastOne = currentOne;
        }
        currentOne++;
        n >>= 1;
    }

    return maxGap;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(log(n))$, because we're iterating through the bits of the number once.
> - **Space Complexity:** $O(1)$, because we're using a constant amount of space to store our variables.
> - **Optimality proof:** This is the optimal solution because it minimizes both time and space complexity by avoiding the conversion to a binary string and using bitwise operations directly.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Bit manipulation, iteration through binary representation.
- Problem-solving patterns identified: Using bitwise operations for efficient binary manipulation.
- Optimization techniques learned: Avoiding unnecessary conversions (like to string) and using bitwise operations.
- Similar problems to practice: Other problems involving binary representation and manipulation.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect use of bitwise operations, not handling edge cases (like numbers with leading zeros in binary).
- Edge cases to watch for: Numbers with no gaps between `1`s, numbers with only one `1`.
- Performance pitfalls: Using string conversion instead of bitwise operations.
- Testing considerations: Test with numbers having different binary representations to ensure the solution works for all cases.