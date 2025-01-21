## Day of the Week
**Problem Link:** https://leetcode.com/problems/day-of-the-week/description

**Problem Statement:**
- Input: `day`, `month`, and `year` representing a date in the Gregorian calendar.
- Constraints: `1971 <= year <= 2100`, `1 <= month <= 12`, and `1 <= day <= 31`.
- Expected Output: The day of the week for the given date, with the output being one of the following strings: `"Monday"`, `"Tuesday"`, `"Wednesday"`, `"Thursday"`, `"Friday"`, `"Saturday"`, or `"Sunday"`.
- Key Requirements: Calculate the day of the week based on the given date.
- Edge Cases: Consider the varying number of days in months and leap years.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through each year from 1971 to the given year, accounting for leap years and the number of days in each month to calculate the total number of days elapsed. Then, use the modulo operator to find the remainder when divided by 7 to determine the day of the week.
- Step-by-step breakdown:
  1. Initialize the total number of days.
  2. Iterate through each year from 1971 to the given year, considering leap years.
  3. For each year, iterate through each month, adding the number of days in that month to the total.
  4. Once the given month is reached, add the given day to the total.
  5. Calculate the day of the week based on the total number of days modulo 7.

```cpp
#include <iostream>
#include <vector>
#include <string>

std::string dayOfTheWeek(int day, int month, int year) {
    std::vector<std::string> days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"};
    int totalDays = 0;
    
    for (int y = 1971; y < year; y++) {
        if ((y % 4 == 0 && y % 100 != 0) || y % 400 == 0) {
            totalDays += 366; // Leap year
        } else {
            totalDays += 365; // Non-leap year
        }
    }
    
    std::vector<int> daysInMonth = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0) {
        daysInMonth[1] = 29; // Account for leap year in the given year
    }
    
    for (int m = 0; m < month - 1; m++) {
        totalDays += daysInMonth[m];
    }
    
    totalDays += day - 1; // Subtract 1 because the day is 1-indexed
    
    return days[totalDays % 7];
}

int main() {
    std::cout << dayOfTheWeek(3, 1, 2022) << std::endl;
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(year \times month)$, because in the worst case, we iterate through each year and each month.
> - **Space Complexity:** $O(1)$, as we use a constant amount of space to store the days of the week and the total number of days.
> - **Why these complexities occur:** The brute force approach involves iterating through each year and month, leading to a time complexity that is linear in the number of years and months. The space complexity is constant because we only use a fixed amount of space to store the necessary variables.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Zeller's Congruence formula can be used to calculate the day of the week directly without needing to iterate through each year and month.
- Detailed breakdown:
  1. Adjust the month and year according to Zeller's Congruence formula.
  2. Apply the formula to calculate the day of the week.
  3. Use the result to determine the day of the week.

```cpp
std::string dayOfTheWeek(int day, int month, int year) {
    std::vector<std::string> days = {"Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"};
    if (month < 3) {
        month += 12;
        year--;
    }
    int h = (day + (13 * (month + 1)) / 5 + year + year / 4 - year / 100 + year / 400) % 7;
    return days[h];
}

int main() {
    std::cout << dayOfTheWeek(3, 1, 2022) << std::endl;
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, because we perform a constant number of operations.
> - **Space Complexity:** $O(1)$, as we use a constant amount of space to store the days of the week and the variables needed for the calculation.
> - **Optimality proof:** Zeller's Congruence formula provides a direct calculation of the day of the week, eliminating the need for iteration and resulting in a constant time complexity.

---

### Final Notes

**Learning Points:**
- The importance of understanding the problem constraints and applying relevant mathematical formulas.
- The use of Zeller's Congruence formula for efficient calculation of the day of the week.
- The difference in complexity between brute force and optimal approaches.

**Mistakes to Avoid:**
- Not considering the problem constraints and overcomplicating the solution.
- Failing to account for leap years and the varying number of days in months.
- Not optimizing the solution for better performance.