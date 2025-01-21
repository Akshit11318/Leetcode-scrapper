## Convert Date Format

**Problem Link:** https://leetcode.com/problems/convert-date-format/description

**Problem Statement:**
- Input: A string representing a date in the format "Day Month dd, yyyy" (e.g., "Monday January 01, 2024").
- Expected output: The date in the format "yyyy-MM-dd" (e.g., "2024-01-01").
- Key requirements:
  - The input date string is in a specific format that needs to be parsed and converted into a standard format.
  - The output should be in the "yyyy-MM-dd" format.
- Edge cases:
  - Handling different months and their corresponding numerical values.
  - Ensuring the day and year are correctly extracted and formatted.
- Example test cases:
  - "Monday January 01, 2024" should return "2024-01-01".
  - "Tuesday February 28, 2023" should return "2023-02-28".

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to manually parse the input string, identify the day, month, and year, and then format them according to the required output.
- This involves using string manipulation functions to extract the necessary parts of the date.
- It comes to mind first because it directly addresses the problem without considering optimizations.

```cpp
#include <iostream>
#include <string>
#include <unordered_map>

string reformatDate(string date) {
    unordered_map<string, string> months = {
        {"Jan", "01"}, {"Feb", "02"}, {"Mar", "03"}, {"Apr", "04"},
        {"May", "05"}, {"Jun", "06"}, {"Jul", "07"}, {"Aug", "08"},
        {"Sep", "09"}, {"Oct", "10"}, {"Nov", "11"}, {"Dec", "12"}
    };

    int dayStart = date.find(" ") + 1;
    int monthStart = date.find(" ", dayStart) + 1;
    int yearStart = date.find(" ", monthStart) + 1;

    string day = date.substr(dayStart, date.find(" ", dayStart) - dayStart);
    string month = date.substr(monthStart, date.find(" ", monthStart) - monthStart);
    string year = date.substr(yearStart, date.find(",", yearStart) - yearStart);

    // Remove the comma from the year
    year = year.substr(0, year.size() - 1);

    // Handle day formatting
    if (day.size() == 1) {
        day = "0" + day;
    }

    return year + "-" + months[month] + "-" + day;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ because the operations are constant time, regardless of the input size.
> - **Space Complexity:** $O(1)$ as the space used does not grow with the size of the input, aside from the output string.
> - **Why these complexities occur:** The operations are limited to string manipulation and do not depend on the input size in a way that would increase complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal solution involves directly parsing the input string and using an efficient method to extract and format the date components.
- Utilizing a map for month names to their numerical equivalents is efficient for handling different months.
- The rest of the logic remains similar to the brute force approach, focusing on extracting and formatting the day and year.

```cpp
#include <iostream>
#include <string>
#include <unordered_map>

string reformatDate(string date) {
    unordered_map<string, string> months = {
        {"Jan", "01"}, {"Feb", "02"}, {"Mar", "03"}, {"Apr", "04"},
        {"May", "05"}, {"Jun", "06"}, {"Jul", "07"}, {"Aug", "08"},
        {"Sep", "09"}, {"Oct", "10"}, {"Nov", "11"}, {"Dec", "12"},
        {"January", "01"}, {"February", "02"}, {"March", "03"}, {"April", "04"},
        {"May", "05"}, {"June", "06"}, {"July", "07"}, {"August", "08"},
        {"September", "09"}, {"October", "10"}, {"November", "11"}, {"December", "12"}
    };

    size_t firstSpace = date.find(" ");
    size_t secondSpace = date.find(" ", firstSpace + 1);
    size_t comma = date.find(",");

    string day = date.substr(firstSpace + 1, secondSpace - firstSpace - 1);
    string month = date.substr(secondSpace + 1, comma - secondSpace - 1);
    string year = date.substr(comma + 2);

    // Handle day formatting
    if (day.size() == 1) {
        day = "0" + day;
    }

    return year + "-" + months[month] + "-" + day;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ because the string operations (find, substr) are performed a constant number of times.
> - **Space Complexity:** $O(1)$ as the space used does not grow with the size of the input, aside from the output string.
> - **Optimality proof:** This solution is optimal because it minimizes the number of operations required to parse and format the date, utilizing efficient string manipulation and a lookup table for months.

---

### Final Notes

**Learning Points:**
- **String manipulation:** Understanding how to efficiently use string operations like `find` and `substr` to extract parts of a string.
- **Lookup tables:** Utilizing maps or dictionaries to quickly look up values, such as month names to their numerical equivalents.
- **Date and time formatting:** Recognizing the importance of handling different date formats and how to convert between them efficiently.

**Mistakes to Avoid:**
- Incorrectly handling edge cases, such as single-digit days or varying month name lengths.
- Failing to optimize string operations, leading to unnecessary complexity.
- Not considering the use of lookup tables for efficient data retrieval.