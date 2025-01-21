## Next Day
**Problem Link:** https://leetcode.com/problems/next-day/description

**Problem Statement:**
- Input format: Given a date string in the format `day month year` where `day` is a 1-based index of the day of the month (01 to 31), `month` is the full English name of the month (e.g., January to December), and `year` is a 4-digit year.
- Constraints: The input date is valid and within the range 1971 to 2038 (inclusive).
- Expected output format: The date of the next day in the same format.
- Key requirements and edge cases to consider:
  - Handling month changes (e.g., from January 31 to February 1).
  - Handling year changes (e.g., from December 31 to January 1).
  - Accounting for leap years.
- Example test cases:
  - Input: `"2022-01-01"` should output `"2022-01-02"`.
  - Input: `"2022-12-31"` should output `"2023-01-01"`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves directly manipulating the date string to increment the day, handling month and year changes as necessary.
- This approach comes to mind first because it directly addresses the requirement to find the next day without considering the underlying date logic.

```cpp
#include <iostream>
#include <string>
#include <sstream>

std::string nextDay(std::string date) {
    int day, month, year;
    std::istringstream iss(date);
    std::string token;
    std::getline(iss, token, '-');
    day = std::stoi(token);
    std::getline(iss, token, '-');
    month = std::stoi(token);
    std::getline(iss, token, '-');
    year = std::stoi(token);

    // Increment day
    day++;

    // Handle month and year changes
    if (month == 2) { // February
        if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)) { // Leap year
            if (day > 29) {
                day = 1;
                month++;
            }
        } else {
            if (day > 28) {
                day = 1;
                month++;
            }
        }
    } else if (month == 4 || month == 6 || month == 9 || month == 11) { // April, June, September, November
        if (day > 30) {
            day = 1;
            month++;
        }
    } else { // January, March, May, July, August, October, December
        if (day > 31) {
            day = 1;
            month++;
        }
    }

    // Handle year change
    if (month > 12) {
        month = 1;
        year++;
    }

    // Format the next day
    std::ostringstream oss;
    oss << day << "-" << month << "-" << year;
    return oss.str();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ because we are performing a constant number of operations regardless of the input size.
> - **Space Complexity:** $O(1)$ because we are using a constant amount of space to store the input and output.
> - **Why these complexities occur:** These complexities occur because the operations (incrementing the day, handling month and year changes) are constant time and do not depend on the input size.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal approach involves using the `<ctime>` library in C++ to handle dates and calculate the next day efficiently.
- This approach is optimal because it leverages the existing library functionality to handle date logic, reducing the chance of errors and improving readability.

```cpp
#include <iostream>
#include <ctime>
#include <sstream>

std::string nextDay(std::string date) {
    // Parse the input date
    std::tm time = {};
    std::istringstream iss(date);
    iss >> std::get_time(&time, "%Y-%m-%d");
    if (iss.fail()) {
        // Handle parsing error
        return "";
    }

    // Increment the day
    time.tm_mday++;

    // Normalize the date
    std::time_t t = std::mktime(&time);

    // Format the next day
    std::tm* nextDay = std::localtime(&t);
    char buffer[11];
    std::strftime(buffer, sizeof(buffer), "%Y-%m-%d", nextDay);
    return std::string(buffer);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ because the operations (parsing the date, incrementing the day, normalizing the date, and formatting the output) are constant time.
> - **Space Complexity:** $O(1)$ because we are using a constant amount of space to store the input and output.
> - **Optimality proof:** This approach is optimal because it uses the existing library functionality to handle date logic efficiently, reducing the chance of errors and improving readability.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Date manipulation and library usage.
- Problem-solving patterns identified: Using existing library functionality to handle complex logic.
- Optimization techniques learned: Leveraging library functionality to improve efficiency and readability.
- Similar problems to practice: Other date-related problems, such as calculating the difference between two dates or finding the first day of the month.

**Mistakes to Avoid:**
- Common implementation errors: Failing to handle edge cases (e.g., leap years, month changes).
- Edge cases to watch for: Leap years, month changes, and year changes.
- Performance pitfalls: Using inefficient algorithms or not leveraging library functionality.
- Testing considerations: Thoroughly testing the solution with various input dates, including edge cases.