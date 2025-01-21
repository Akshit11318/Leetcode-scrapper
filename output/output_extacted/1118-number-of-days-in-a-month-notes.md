## Number of Days in a Month

**Problem Link:** https://leetcode.com/problems/number-of-days-in-a-month/description

**Problem Statement:**
- Input format and constraints: The function takes two integers, `year` and `month`, as input. The year is in the range [1, 9999] and the month is in the range [1, 12].
- Expected output format: The function returns the number of days in the month for the given year.
- Key requirements and edge cases to consider: The problem requires handling of leap years, where February has 29 days instead of the usual 28.
- Example test cases with explanations:
  - `numberOfDays(1999, 1)` returns 31, because January has 31 days.
  - `numberOfDays(2000, 2)` returns 29, because 2000 is a leap year and February has 29 days.
  - `numberOfDays(1900, 2)` returns 28, because 1900 is not a leap year and February has 28 days.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The most straightforward way to solve this problem is to write a series of if-else statements to check each month and return the corresponding number of days.
- Step-by-step breakdown of the solution:
  1. Check if the month is February.
  2. If it is February, check if the year is a leap year.
  3. If the year is a leap year, return 29.
  4. If the year is not a leap year, return 28.
  5. If the month is not February, use another series of if-else statements to check the month and return the corresponding number of days.
- Why this approach comes to mind first: This approach is intuitive because it directly checks each possible case and returns the correct answer.

```cpp
class Solution {
public:
    int numberOfDays(int year, int month) {
        if (month == 2) {
            if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0) {
                return 29;
            } else {
                return 28;
            }
        } else if (month == 4 || month == 6 || month == 9 || month == 11) {
            return 30;
        } else {
            return 31;
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, because the function only performs a constant number of operations regardless of the input.
> - **Space Complexity:** $O(1)$, because the function only uses a constant amount of space to store the input and output.
> - **Why these complexities occur:** These complexities occur because the function only checks a few conditions and returns the answer, without using any loops or recursive calls that could increase the time or space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution is to use a lookup table to store the number of days in each month, and then use the month as an index to look up the correct answer.
- Detailed breakdown of the approach:
  1. Create a lookup table with 12 entries, one for each month.
  2. Initialize the lookup table with the correct number of days for each month, assuming a non-leap year.
  3. Check if the year is a leap year.
  4. If the year is a leap year, update the lookup table to reflect the correct number of days for February.
  5. Use the month as an index to look up the correct answer in the lookup table.
- Proof of optimality: This approach is optimal because it only requires a constant number of operations, regardless of the input.

```cpp
class Solution {
public:
    int numberOfDays(int year, int month) {
        int days[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0) {
            days[1] = 29;
        }
        return days[month - 1];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, because the function only performs a constant number of operations regardless of the input.
> - **Space Complexity:** $O(1)$, because the function only uses a constant amount of space to store the lookup table and the input and output.
> - **Optimality proof:** This approach is optimal because it only requires a constant number of operations, regardless of the input.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the use of lookup tables and conditional statements to solve a problem efficiently.
- Problem-solving patterns identified: The problem requires identifying the key conditions that affect the answer, and using those conditions to look up the correct answer in a table.
- Optimization techniques learned: The problem demonstrates the use of a lookup table to reduce the number of operations required to solve the problem.
- Similar problems to practice: Other problems that involve looking up values in a table or using conditional statements to solve a problem.

**Mistakes to Avoid:**
- Common implementation errors: One common error is to forget to update the lookup table for leap years.
- Edge cases to watch for: The problem requires handling of leap years, which can be easy to overlook.
- Performance pitfalls: One potential performance pitfall is to use a recursive function to solve the problem, which could lead to a stack overflow for large inputs.
- Testing considerations: The problem requires testing for a variety of inputs, including different months and years, to ensure that the function works correctly in all cases.