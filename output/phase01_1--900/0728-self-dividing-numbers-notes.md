## Self Dividing Numbers

**Problem Link:** [https://leetcode.com/problems/self-dividing-numbers/description](https://leetcode.com/problems/self-dividing-numbers/description)

**Problem Statement:**
- Input format and constraints: The function takes two integers `left` and `right` as input, representing the range of numbers to check.
- Expected output format: A vector of integers representing the self-dividing numbers within the given range.
- Key requirements and edge cases to consider: 
  - A self-dividing number is a number that is divisible by every digit it contains.
  - For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
  - Also, the input range is `1 <= left <= right <= 10^4`.
- Example test cases with explanations:
  - For `left = 1` and `right = 22`, the output should be `[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To check each number within the given range to see if it is self-dividing.
- Step-by-step breakdown of the solution:
  1. Loop through each number from `left` to `right`.
  2. For each number, convert it to a string to easily access its digits.
  3. Then, loop through each digit of the number.
  4. Check if the digit is zero or if the number is not divisible by the digit. If either condition is true, the number is not self-dividing.
  5. If the number passes the check for all its digits, add it to the result vector.
- Why this approach comes to mind first: It directly addresses the problem statement by checking each number against the criteria for being self-dividing.

```cpp
vector<int> selfDividingNumbers(int left, int right) {
    vector<int> result;
    for (int num = left; num <= right; num++) {
        bool isSelfDividing = true;
        string strNum = to_string(num);
        for (char digit : strNum) {
            if (digit == '0' || num % (digit - '0') != 0) {
                isSelfDividing = false;
                break;
            }
        }
        if (isSelfDividing) {
            result.push_back(num);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the range of numbers (`right - left + 1`) and $m$ is the average number of digits in a number within the range. This is because for each number, we are potentially checking each of its digits.
> - **Space Complexity:** $O(n)$ for storing the result vector in the worst case, where all numbers in the range are self-dividing.
> - **Why these complexities occur:** The brute force approach involves checking each number within the given range, which leads to a linear time complexity with respect to the range size. The additional factor of $m$ comes from checking each digit of each number.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The same as the brute force approach, since we must check each number and its digits. However, we can slightly optimize by avoiding the string conversion for each number, instead directly checking the digits.
- Detailed breakdown of the approach:
  1. Loop through each number from `left` to `right`.
  2. For each number, check each of its digits by using arithmetic operations to extract the digits.
  3. If any digit is zero or the number is not divisible by the digit, mark the number as not self-dividing and move on to the next number.
  4. If the number is self-dividing, add it to the result vector.
- Proof of optimality: This approach is optimal because it still checks each number and its digits but does so in a more efficient manner by avoiding string conversions.

```cpp
vector<int> selfDividingNumbers(int left, int right) {
    vector<int> result;
    for (int num = left; num <= right; num++) {
        bool isSelfDividing = true;
        int temp = num;
        while (temp > 0) {
            int digit = temp % 10;
            if (digit == 0 || num % digit != 0) {
                isSelfDividing = false;
                break;
            }
            temp /= 10;
        }
        if (isSelfDividing) {
            result.push_back(num);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the range of numbers and $m$ is the average number of digits in a number within the range. This remains the same as the brute force approach because the core operation of checking each digit of each number is unchanged.
> - **Space Complexity:** $O(n)$ for storing the result vector in the worst case.
> - **Optimality proof:** This approach is optimal because it minimizes the operations required to check if a number is self-dividing, avoiding unnecessary string conversions and directly accessing digits through arithmetic operations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Looping through a range of numbers, checking divisibility, and optimizing code by reducing unnecessary operations.
- Problem-solving patterns identified: Directly addressing the problem statement and optimizing the solution by considering the properties of numbers and their digits.
- Optimization techniques learned: Avoiding unnecessary conversions (like string conversion) and using arithmetic operations to extract digits.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for division by zero, not properly handling the range of numbers, and not optimizing the solution.
- Edge cases to watch for: Numbers with zeros as digits and numbers at the boundaries of the given range.
- Performance pitfalls: Using inefficient methods to extract digits or check divisibility.
- Testing considerations: Ensuring the solution works correctly for different ranges and edge cases.