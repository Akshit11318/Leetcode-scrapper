## Plus One
**Problem Link:** https://leetcode.com/problems/plus-one/description

**Problem Statement:**
- Input format: a non-empty array of digits `digits` representing a non-negative integer.
- Constraints: `1 <= digits.length <= 200`, `0 <= digits[i] <= 9`.
- Expected output format: an array of digits representing the incremented integer.
- Key requirements: increment the integer represented by the input array by 1.
- Edge cases: handle cases where the input array represents the maximum value for a given length (e.g., `[9, 9, 9]`).

**Example Test Cases:**
- Input: `digits = [1, 2, 3]`, Output: `[1, 2, 4]`.
- Input: `digits = [4, 3, 2, 1]`, Output: `[4, 3, 2, 2]`.
- Input: `digits = [9]`, Output: `[1, 0]`.
- Input: `digits = [9, 9, 9]`, Output: `[1, 0, 0, 0]`.

---

### Brute Force Approach
**Explanation:**
- Convert the input array into an integer, increment it by 1, and then convert it back into an array.
- This approach seems straightforward but is not efficient for large inputs due to potential overflow issues.

```cpp
class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        // Convert vector to integer
        int num = 0;
        for (int digit : digits) {
            num = num * 10 + digit;
        }
        
        // Increment by 1
        num += 1;
        
        // Convert back to vector
        vector<int> result;
        while (num > 0) {
            result.push_back(num % 10);
            num /= 10;
        }
        
        // Reverse the vector since we appended in reverse order
        reverse(result.begin(), result.end());
        
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of digits. This is because we iterate through the digits twice: once to convert to an integer and once to convert back to a vector.
> - **Space Complexity:** $O(n)$, as in the worst case, we might need to store $n+1$ digits (e.g., when all digits are 9).
> - **Why these complexities occur:** The conversion between the vector and integer requires iterating over each digit, and the space complexity is due to the potential need for an extra digit in the output.

---

### Optimal Approach (Required)
**Explanation:**
- Start from the end of the array and increment the last digit by 1.
- If the last digit is 9, it will become 0, and we need to carry over the increment to the next digit.
- Continue this process until we find a digit that is not 9 or until we reach the beginning of the array.
- If all digits are 9, we need to add an extra digit at the beginning (which will be 1).

```cpp
class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        for (int i = digits.size() - 1; i >= 0; --i) {
            if (digits[i] == 9) {
                digits[i] = 0;
            } else {
                digits[i] += 1;
                return digits;
            }
        }
        // If all digits were 9, add a new digit at the beginning
        digits.insert(digits.begin(), 1);
        return digits;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of digits. This is because in the worst case, we need to iterate over all digits.
> - **Space Complexity:** $O(1)$ for the case when the input does not consist entirely of 9s. However, if all digits are 9, we need to add one more digit, resulting in $O(n)$ space complexity in that specific scenario.
> - **Optimality proof:** This solution is optimal because it only iterates over the digits once and modifies them in-place, except for the rare case where an additional digit is needed at the beginning.

---

### Final Notes

**Learning Points:**
- Handling edge cases, such as when the input array consists entirely of 9s.
- Understanding the importance of iterating from the end of the array to handle carry-over correctly.
- Recognizing that direct conversion to and from integers can lead to inefficiencies and potential overflows for large inputs.

**Mistakes to Avoid:**
- Not considering the case where all digits are 9.
- Not iterating from the end of the array to handle carry-over correctly.
- Using integer conversion for large inputs, which can lead to overflow issues.