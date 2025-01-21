## Maximum Swap
**Problem Link:** [https://leetcode.com/problems/maximum-swap/description](https://leetcode.com/problems/maximum-swap/description)

**Problem Statement:**
- Input format: An integer `num`
- Constraints: $0 \leq num \leq 10^8$
- Expected output format: The maximum possible integer after swapping two digits
- Key requirements and edge cases to consider:
  - Swapping can only occur between two digits.
  - The integer should be maximized after the swap.
- Example test cases with explanations:
  - `num = 2736`, the maximum swap would result in `7236`.
  - `num = 9973`, the maximum swap would result in `9973`, as no swap is needed.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible swaps of two digits and see which one yields the maximum integer.
- Step-by-step breakdown of the solution:
  1. Convert the integer into a string to easily access and swap digits.
  2. Iterate through all pairs of digits in the string.
  3. For each pair, swap the digits and convert the string back into an integer.
  4. Keep track of the maximum integer found after all swaps.

```cpp
class Solution {
public:
    int maximumSwap(int num) {
        string str = to_string(num);
        int maxNum = num;
        
        for (int i = 0; i < str.length(); i++) {
            for (int j = i + 1; j < str.length(); j++) {
                swap(str[i], str[j]);
                maxNum = max(maxNum, stoi(str));
                swap(str[i], str[j]); // Swap back
            }
        }
        
        return maxNum;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot \log(n))$, where $n$ is the number of digits in the input integer. The $\log(n)$ factor comes from the conversion of the string back to an integer using `stoi`.
> - **Space Complexity:** $O(n)$, where $n$ is the number of digits in the input integer, due to the conversion of the integer to a string.
> - **Why these complexities occur:** The brute force approach requires iterating through all pairs of digits and performing a swap for each pair, leading to the quadratic time complexity. The space complexity arises from storing the string representation of the integer.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of trying all possible swaps, we can find the first digit from the right that is smaller than the maximum digit to its right. Then, we find the maximum digit to the right of this digit and swap them.
- Detailed breakdown of the approach:
  1. Convert the integer to a string to easily access and manipulate digits.
  2. Iterate from right to left through the string to find the first digit that is smaller than the maximum digit to its right.
  3. Once found, iterate from right to left again to find the maximum digit that is greater than the found digit.
  4. Swap these two digits.
  5. Convert the string back to an integer for the result.

```cpp
class Solution {
public:
    int maximumSwap(int num) {
        string str = to_string(num);
        
        for (int i = str.length() - 1; i > 0; i--) {
            if (str[i - 1] < str[i]) {
                // Find the maximum digit to the right of i - 1
                int maxIdx = i;
                for (int j = i + 1; j < str.length(); j++) {
                    if (str[j] > str[maxIdx]) {
                        maxIdx = j;
                    }
                }
                // Swap str[i - 1] and str[maxIdx]
                swap(str[i - 1], str[maxIdx]);
                break;
            }
        }
        
        return stoi(str);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of digits in the input integer. This is because we potentially make two passes through the string: one to find the digit to swap and another to find the maximum digit to its right.
> - **Space Complexity:** $O(n)$, where $n$ is the number of digits in the input integer, due to the conversion of the integer to a string.
> - **Optimality proof:** This approach is optimal because it directly finds the swap that maximizes the integer without trying all possible swaps, thus reducing the time complexity from quadratic to linear.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Greedy algorithm, string manipulation.
- Problem-solving patterns identified: Looking for the first opportunity to improve the solution (in this case, finding the first digit from the right that can be swapped to a larger digit).
- Optimization techniques learned: Reducing the search space by directly targeting the part of the input that can be improved.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling edge cases (e.g., when the input integer has less than two digits).
- Performance pitfalls: Using inefficient algorithms (like the brute force approach) for large inputs.
- Testing considerations: Ensuring that the solution works correctly for various inputs, including edge cases like single-digit integers and integers with repeated digits.