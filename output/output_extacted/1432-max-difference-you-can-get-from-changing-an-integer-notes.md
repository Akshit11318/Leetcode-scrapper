## Max Difference You Can Get From Changing an Integer
**Problem Link:** https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/description

**Problem Statement:**
- Input format and constraints: The input is a single integer `num`. The constraints are that `num` is a positive integer.
- Expected output format: The output should be the maximum difference that can be achieved by changing one digit of the input integer.
- Key requirements and edge cases to consider: The integer can be large, and we need to consider all possible changes of one digit to maximize the difference.
- Example test cases with explanations: For example, if `num = 1234`, the maximum difference can be achieved by changing the first digit to `9`, resulting in `9234`, and the minimum number can be achieved by changing the first digit to `1`, resulting in `1234`. The difference is `9234 - 1234 = 8000`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: We can try all possible changes of one digit and calculate the difference for each change.
- Step-by-step breakdown of the solution:
  1. Convert the integer to a string to easily access and modify each digit.
  2. Iterate over each digit in the string.
  3. For each digit, try all possible changes (0-9) and calculate the new integer value.
  4. Calculate the difference between the new integer value and the original integer value.
  5. Keep track of the maximum and minimum differences found.
- Why this approach comes to mind first: It is a straightforward approach that tries all possible changes and calculates the differences.

```cpp
int maxDiff(int num) {
    int maxNum = num;
    int minNum = num;
    string str = to_string(num);
    for (int i = 0; i < str.length(); i++) {
        for (int j = 0; j <= 9; j++) {
            string newStr = str;
            newStr[i] = '0' + j;
            int newNum = stoi(newStr);
            maxNum = max(maxNum, newNum);
            minNum = min(minNum, newNum);
        }
    }
    return maxNum - minNum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot 10)$, where $n$ is the number of digits in the input integer. This is because we iterate over each digit and try all possible changes (0-9) for each digit.
> - **Space Complexity:** $O(n)$, where $n$ is the number of digits in the input integer. This is because we convert the integer to a string and store the new string for each change.
> - **Why these complexities occur:** The time complexity occurs because we try all possible changes for each digit, and the space complexity occurs because we store the new string for each change.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can observe that the maximum difference can be achieved by changing the first digit to `9` and the minimum number can be achieved by changing the first digit to `1` (if the first digit is not `1`) or `0` (if the first digit is `1`).
- Detailed breakdown of the approach:
  1. Convert the integer to a string to easily access and modify the first digit.
  2. If the first digit is not `1`, change it to `1` to get the minimum number.
  3. If the first digit is `1`, change it to `0` to get the minimum number.
  4. Change the first digit to `9` to get the maximum number.
  5. Calculate the difference between the maximum and minimum numbers.
- Proof of optimality: This approach is optimal because it tries the minimum number of changes to achieve the maximum difference.

```cpp
int maxDiff(int num) {
    string str = to_string(num);
    int maxNum = num;
    int minNum = num;
    for (int i = 0; i < str.length(); i++) {
        if (str[i] != '9') {
            string newStr = str;
            newStr[i] = '9';
            maxNum = max(maxNum, stoi(newStr));
            break;
        }
    }
    for (int i = 0; i < str.length(); i++) {
        if (str[i] != '1' && str[i] != '0') {
            string newStr = str;
            newStr[i] = '1';
            minNum = min(minNum, stoi(newStr));
            break;
        } else if (str[i] == '1') {
            string newStr = str;
            newStr[i] = '0';
            minNum = min(minNum, stoi(newStr));
            break;
        }
    }
    return maxNum - minNum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of digits in the input integer. This is because we iterate over each digit to find the first digit that is not `9` and the first digit that is not `1` or `0`.
> - **Space Complexity:** $O(n)$, where $n$ is the number of digits in the input integer. This is because we convert the integer to a string and store the new string for each change.
> - **Optimality proof:** This approach is optimal because it tries the minimum number of changes to achieve the maximum difference.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Trying all possible changes and calculating the differences.
- Problem-solving patterns identified: Observing the pattern that the maximum difference can be achieved by changing the first digit to `9` and the minimum number can be achieved by changing the first digit to `1` or `0`.
- Optimization techniques learned: Reducing the number of changes to achieve the maximum difference.
- Similar problems to practice: Other problems that involve trying all possible changes and calculating the differences.

**Mistakes to Avoid:**
- Common implementation errors: Not handling the case where the first digit is `1`.
- Edge cases to watch for: The case where the input integer is a single digit.
- Performance pitfalls: Trying all possible changes for each digit, which can result in a high time complexity.
- Testing considerations: Testing the function with different input integers, including single-digit integers and integers with multiple digits.