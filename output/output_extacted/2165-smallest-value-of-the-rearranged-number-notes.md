## Smallest Value of the Rearranged Number
**Problem Link:** https://leetcode.com/problems/smallest-value-of-the-rearranged-number/description

**Problem Statement:**
- Input: A non-negative integer `num`.
- Output: The smallest possible integer that can be obtained by rearranging the digits of `num`.
- Key requirements: 
  - The input integer `num` is non-negative.
  - The output should be the smallest possible integer that can be obtained by rearranging the digits of `num`.
- Edge cases to consider: 
  - When `num` is a single-digit number, the output should be the same as `num`.
  - When `num` is zero, the output should be zero.

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible permutations of the digits of `num` and find the smallest one.
- Step-by-step breakdown of the solution:
  1. Convert the integer `num` to a string to easily access and manipulate its digits.
  2. Generate all permutations of the digits in the string.
  3. For each permutation, convert it back to an integer and compare it with the current smallest integer found.
  4. Update the smallest integer if a smaller one is found.

```cpp
#include <algorithm>
#include <string>
using namespace std;

int smallestNumber(int num) {
    string str = to_string(num);
    sort(str.begin(), str.end());
    int index = 0;
    while (index < str.size() && str[index] == '0') {
        index++;
    }
    if (index == str.size()) {
        return 0;
    }
    if (index > 0) {
        swap(str[0], str[index]);
    }
    return stoi(str);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ where $n$ is the number of digits in `num`, due to the sorting operation.
> - **Space Complexity:** $O(n)$ for storing the string representation of `num`.
> - **Why these complexities occur:** The sorting operation dominates the time complexity, and the space complexity is due to the string representation of `num`.

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: 
  - The smallest number can be obtained by sorting the digits in ascending order and then moving the first non-zero digit to the front if the first digit is zero.
- Detailed breakdown of the approach:
  1. Convert the integer `num` to a string to easily access and manipulate its digits.
  2. Sort the digits in ascending order.
  3. If the first digit is zero, find the first non-zero digit and swap it with the first digit.
- Proof of optimality: 
  - This approach ensures that the smallest possible integer is obtained by rearranging the digits of `num`.

```cpp
int smallestNumber(int num) {
    string str = to_string(num);
    sort(str.begin(), str.end());
    int index = 0;
    while (index < str.size() && str[index] == '0') {
        index++;
    }
    if (index == str.size()) {
        return 0;
    }
    if (index > 0) {
        swap(str[0], str[index]);
    }
    return stoi(str);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ where $n$ is the number of digits in `num`, due to the sorting operation.
> - **Space Complexity:** $O(n)$ for storing the string representation of `num`.
> - **Optimality proof:** The approach ensures that the smallest possible integer is obtained by rearranging the digits of `num`, and no further optimization is possible.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: sorting, string manipulation.
- Problem-solving patterns identified: finding the smallest possible integer by rearranging digits.
- Optimization techniques learned: using sorting to find the smallest possible integer.

**Mistakes to Avoid:**
- Common implementation errors: not handling the case where the first digit is zero.
- Edge cases to watch for: single-digit numbers, zero.
- Performance pitfalls: using inefficient sorting algorithms.
- Testing considerations: testing with different inputs, including edge cases.