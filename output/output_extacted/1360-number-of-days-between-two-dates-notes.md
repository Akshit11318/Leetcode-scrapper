## Number of Days Between Two Dates
**Problem Link:** https://leetcode.com/problems/number-of-days-between-two-dates/description

**Problem Statement:**
- Input format: Two strings representing dates in the format "YYYY-MM-DD".
- Constraints: The given dates are valid dates between the years 1971 and 2038.
- Expected output format: The number of days between the two given dates.
- Key requirements and edge cases to consider:
  - Leap years and their impact on the number of days in February.
  - Different numbers of days in each month.
  - The possibility of the two dates being in the same year, month, or day.
- Example test cases with explanations:
  - "2020-01-01" and "2020-01-15" should return 14.
  - "2019-01-01" and "2020-01-01" should return 365.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Convert the given dates to a standard format that can be easily compared, such as the number of days since a fixed starting point (e.g., "1970-01-01").
- Step-by-step breakdown of the solution:
  1. Parse the input dates into their year, month, and day components.
  2. Calculate the number of days since the starting point for each date, considering leap years and the varying number of days in each month.
  3. Subtract the two totals to find the difference in days between the two dates.
- Why this approach comes to mind first: It's straightforward to understand and implement, as it directly calculates the difference based on the dates' components.

```cpp
int daysBetweenDates(string date1, string date2) {
    int isLeapYear(int year) {
        return (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);
    }

    int daysInMonth[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    int days = 0;

    int year1 = stoi(date1.substr(0, 4));
    int month1 = stoi(date1.substr(5, 2));
    int day1 = stoi(date1.substr(8, 2));

    int year2 = stoi(date2.substr(0, 4));
    int month2 = stoi(date2.substr(5, 2));
    int day2 = stoi(date2.substr(8, 2));

    for (int y = 1971; y < year1; y++) {
        days += isLeapYear(y) ? 366 : 365;
    }
    for (int m = 0; m < month1 - 1; m++) {
        days += (m == 1 && isLeapYear(year1)) ? 29 : daysInMonth[m];
    }
    days += day1;

    int days2 = 0;
    for (int y = 1971; y < year2; y++) {
        days2 += isLeapYear(y) ? 366 : 365;
    }
    for (int m = 0; m < month2 - 1; m++) {
        days2 += (m == 1 && isLeapYear(year2)) ? 29 : daysInMonth[m];
    }
    days2 += day2;

    return abs(days - days2);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ because we are iterating over a fixed range of years and months, and the number of operations does not depend on the input size.
> - **Space Complexity:** $O(1)$ as we are using a constant amount of space to store the dates and the intermediate results.
> - **Why these complexities occur:** The brute force approach involves a fixed number of operations regardless of the input size, leading to constant time and space complexities.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Utilize the existing `tm` struct from the `ctime` library in C++ to simplify date calculations. The `mktime` function can convert a `tm` object to seconds since the Unix epoch, allowing for straightforward date comparisons.
- Detailed breakdown of the approach:
  1. Parse the input dates into `tm` structs.
  2. Use `mktime` to convert these structs into seconds since the Unix epoch.
  3. Calculate the absolute difference between the two epoch times to find the difference in seconds, then convert this to days.
- Proof of optimality: This approach is optimal because it leverages optimized library functions for date calculations, minimizing manual computation and potential for error.

```cpp
#include <ctime>

int daysBetweenDates(string date1, string date2) {
    tm t1 = {};
    t1.tm_year = stoi(date1.substr(0, 4)) - 1900;
    t1.tm_mon = stoi(date1.substr(5, 2)) - 1;
    t1.tm_mday = stoi(date1.substr(8, 2));

    tm t2 = {};
    t2.tm_year = stoi(date2.substr(0, 4)) - 1900;
    t2.tm_mon = stoi(date2.substr(5, 2)) - 1;
    t2.tm_mday = stoi(date2.substr(8, 2));

    time_t time1 = mktime(&t1);
    time_t time2 = mktime(&t2);

    return abs(difftime(time1, time2) / (60 * 60 * 24));
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ because the operations performed by `mktime` and `difftime` are constant time, and the number of operations does not depend on the input size.
> - **Space Complexity:** $O(1)$ as we are using a constant amount of space to store the `tm` structs and the intermediate results.
> - **Optimality proof:** This approach is optimal because it uses optimized library functions for date calculations, ensuring that the time complexity is constant and no further optimization is possible.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Date calculations, use of library functions for optimized performance.
- Problem-solving patterns identified: Breaking down complex problems into simpler components, leveraging existing library functions for optimized solutions.
- Optimization techniques learned: Using optimized library functions to minimize manual computation and potential for error.
- Similar problems to practice: Other date-related problems, such as finding the next or previous day, week, or month.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect handling of leap years, incorrect conversion between date formats.
- Edge cases to watch for: Dates at the beginning or end of the month, year, or century.
- Performance pitfalls: Manual computation of date differences instead of using optimized library functions.
- Testing considerations: Thoroughly test the function with different input dates, including edge cases and boundary values.