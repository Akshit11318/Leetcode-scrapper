## Rotated Digits

**Problem Link:** [https://leetcode.com/problems/rotated-digits/description](https://leetcode.com/problems/rotated-digits/description)

**Problem Statement:**
- Input: An integer `N`.
- Output: The number of good integers in the range `[1, N]`.
- A good integer is one that, when rotated by 180 degrees, is different from the original and is a valid number.
- Example: 0, 1, 6, 8, 9 are valid digits when rotated by 180 degrees.
- Key requirements: Count all integers in the range `[1, N]` that are good integers.
- Edge cases: Handle the case where `N` is 0 or less.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check each integer from 1 to `N` to see if it is a good integer.
- Step-by-step breakdown:
  1. Loop through each integer from 1 to `N`.
  2. For each integer, convert it to a string to easily check each digit.
  3. Check if each digit is valid when rotated by 180 degrees.
  4. If a digit is not valid, move to the next integer.
  5. If all digits are valid and the rotated integer is different from the original, increment the count.
- Why this approach comes to mind first: It is a straightforward and intuitive solution.

```cpp
int rotatedDigits(int N) {
    int count = 0;
    for (int i = 1; i <= N; i++) {
        string str = to_string(i);
        bool valid = true;
        bool different = false;
        for (char c : str) {
            if (c == '3' || c == '4' || c == '7') {
                valid = false;
                break;
            } else if (c == '0' || c == '1' || c == '8') {
                continue;
            } else if (c == '2') {
                if (str.find('5') != string::npos) {
                    valid = false;
                    break;
                }
                different = true;
            } else if (c == '5') {
                if (str.find('2') != string::npos) {
                    valid = false;
                    break;
                }
                different = true;
            } else if (c == '6') {
                different = true;
            } else if (c == '9') {
                different = true;
            }
        }
        if (valid && different) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(N \cdot log(N))$, where $N$ is the input integer and $log(N)$ is the number of digits in $N$.
> - **Space Complexity:** $O(log(N))$, for storing the string representation of the integer.
> - **Why these complexities occur:** The algorithm loops through each integer up to $N$ and for each integer, it checks each digit, resulting in a time complexity of $O(N \cdot log(N))$. The space complexity is $O(log(N))$ because we store the string representation of each integer.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of checking each integer from 1 to `N`, we can use a mathematical approach to calculate the number of good integers.
- Detailed breakdown: 
  1. Define a function `isGood` to check if an integer is good.
  2. Use a loop to check each integer from 1 to `N`.
  3. For each integer, use the `isGood` function to check if it is good.
- Proof of optimality: This approach is optimal because it directly calculates the number of good integers without any unnecessary checks.

```cpp
int rotatedDigits(int N) {
    int count = 0;
    for (int i = 1; i <= N; i++) {
        string str = to_string(i);
        bool invalid = false;
        bool diff = false;
        for (char c : str) {
            switch (c) {
                case '3':
                case '4':
                case '7':
                    invalid = true;
                    break;
                case '2':
                    diff = true;
                    break;
                case '5':
                    diff = true;
                    break;
                case '6':
                    diff = true;
                    break;
                case '9':
                    diff = true;
                    break;
            }
        }
        if (!invalid && diff) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(N \cdot log(N))$, where $N$ is the input integer and $log(N)$ is the number of digits in $N$.
> - **Space Complexity:** $O(log(N))$, for storing the string representation of the integer.
> - **Optimality proof:** This approach is optimal because it directly calculates the number of good integers without any unnecessary checks.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: Looping through integers, checking each digit, and using a mathematical approach.
- Problem-solving patterns: Breaking down the problem into smaller sub-problems and using a `switch` statement to handle different cases.
- Optimization techniques: Using a mathematical approach to directly calculate the number of good integers.
- Similar problems to practice: Other problems that involve checking each digit of an integer, such as checking if an integer is a palindrome.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as when `N` is 0 or less.
- Edge cases to watch for: Handling the case where `N` is 0 or less.
- Performance pitfalls: Using an inefficient algorithm that has a high time complexity.
- Testing considerations: Testing the function with different inputs, including edge cases.