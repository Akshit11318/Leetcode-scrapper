## Maximum 69 Number
**Problem Link:** https://leetcode.com/problems/maximum-69-number/description

**Problem Statement:**
- Input: An integer `num`.
- Constraints: $1 \leq num \leq 10^4$.
- Output: The maximum possible integer that can be obtained by changing at most one digit of `num` to get the maximum possible integer.
- Key requirements: The input integer is non-negative and may have leading zeros when considered as a string.
- Edge cases: Single-digit numbers, numbers with all digits being 6 or 9.

### Brute Force Approach

**Explanation:**
- Convert the integer into a string to easily access and modify each digit.
- Iterate through each character (digit) in the string, and for each character, create a new string where the current character is replaced with '9' if it's '6'.
- Convert each modified string back to an integer and keep track of the maximum integer found.

```cpp
class Solution {
public:
    int maximum69Number (int num) {
        string str = to_string(num);
        int maxNum = num;
        for(int i = 0; i < str.length(); i++) {
            if(str[i] == '6') {
                str[i] = '9';
                maxNum = max(maxNum, stoi(str));
                str[i] = '6'; // Restore the original digit for the next iteration
            }
        }
        return maxNum;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of digits in the input number, because we are iterating through each digit once. The conversion to and from string also takes $O(n)$ time.
> - **Space Complexity:** $O(n)$, as we are storing the string representation of the number, which requires $n$ characters (where $n$ is the number of digits in the input number).
> - **Why these complexities occur:** The iteration through each digit and the string conversions are the primary causes of these complexities.

### Optimal Approach (Required)

**Explanation:**
- Since we only need to replace the first occurrence of '6' with '9' to get the maximum possible number, we can stop as soon as we find and replace the first '6'.
- This approach avoids unnecessary iterations and conversions.

```cpp
class Solution {
public:
    int maximum69Number (int num) {
        string str = to_string(num);
        for(int i = 0; i < str.length(); i++) {
            if(str[i] == '6') {
                str[i] = '9';
                return stoi(str); // We can return immediately after replacing the first '6'
            }
        }
        return num; // If no '6' is found, return the original number
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of digits in the input number, because in the worst case, we still have to iterate through all digits if there's no '6' or if the first '6' is the last digit.
> - **Space Complexity:** $O(n)$, for the same reasons as the brute force approach.
> - **Optimality proof:** This is optimal because we are only doing the necessary work to find and replace the first '6', which directly leads to the maximum possible integer without unnecessary iterations or conversions.

### Final Notes

**Learning Points:**
- The importance of understanding the problem constraints and the impact of data type conversions.
- How to approach string manipulation problems, especially when dealing with digits.
- The value of optimizing the algorithm to stop as soon as the goal is achieved.

**Mistakes to Avoid:**
- Not considering the impact of leading zeros when converting between integers and strings.
- Failing to validate the input range and handling edge cases.
- Overlooking the possibility of optimizing the algorithm by stopping early when the desired outcome is achieved.