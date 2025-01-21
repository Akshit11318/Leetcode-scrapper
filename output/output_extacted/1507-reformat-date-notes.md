## Reformat Date

**Problem Link:** https://leetcode.com/problems/reformat-date/description

**Problem Statement:**
- Input: A string representing a date in the format "day month year" (e.g., "1st January 2022").
- Expected output: The date in the format "year-month-day" (e.g., "2022-01-01").
- Key requirements:
  - Handle different day formats (e.g., "1st", "2nd", "3rd", "4th", etc.).
  - Handle month names (e.g., "January", "February", etc.).
- Edge cases:
  - Invalid input format.
  - Missing or extra information.

### Brute Force Approach

**Explanation:**
- The initial thought process involves directly parsing the input string and manually converting it into the desired format.
- This approach requires manually handling the different day formats, month names, and year.

```cpp
#include <iostream>
#include <string>
#include <unordered_map>

std::string reformatDate(const std::string& date) {
    std::unordered_map<std::string, std::string> months = {
        {"Jan", "01"}, {"Feb", "02"}, {"Mar", "03"}, {"Apr", "04"},
        {"May", "05"}, {"Jun", "06"}, {"Jul", "07"}, {"Aug", "08"},
        {"Sep", "09"}, {"Oct", "10"}, {"Nov", "11"}, {"Dec", "12"}
    };

    size_t pos = 0;
    std::string day, month, year;

    // Extract day
    while (date[pos] != ' ') {
        day += date[pos];
        pos++;
    }
    pos++; // Skip space

    // Remove suffix from day
    if (day.size() > 2) {
        day = day.substr(0, day.size() - 2);
    }

    // Extract month
    while (date[pos] != ' ') {
        month += date[pos];
        pos++;
    }
    pos++; // Skip space

    // Extract year
    while (pos < date.size()) {
        year += date[pos];
        pos++;
    }

    // Convert month to number
    std::string monthNum;
    for (const auto& m : months) {
        if (month.find(m.first) == 0) {
            monthNum = m.second;
            break;
        }
    }

    // Format day
    if (day.size() == 1) {
        day = "0" + day;
    }

    return year + "-" + monthNum + "-" + day;
}

int main() {
    std::string date = "1st January 2022";
    std::cout << reformatDate(date) << std::endl;
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string, due to the string operations.
> - **Space Complexity:** $O(1)$, since we use a fixed-size map to store the months.
> - **Why these complexities occur:** The time complexity is linear due to the string operations, and the space complexity is constant because we use a fixed-size map.

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use `std::istringstream` to parse the input string and extract the day, month, and year.
- We then use `std::unordered_map` to map the month names to their corresponding numbers.

```cpp
#include <iostream>
#include <string>
#include <sstream>
#include <unordered_map>

std::string reformatDate(const std::string& date) {
    std::istringstream iss(date);
    std::string day, month, year;

    iss >> day >> month >> year;

    // Remove suffix from day
    if (day.size() > 2) {
        day = day.substr(0, day.size() - 2);
    }

    std::unordered_map<std::string, std::string> months = {
        {"Jan", "01"}, {"Feb", "02"}, {"Mar", "03"}, {"Apr", "04"},
        {"May", "05"}, {"Jun", "06"}, {"Jul", "07"}, {"Aug", "08"},
        {"Sep", "09"}, {"Oct", "10"}, {"Nov", "11"}, {"Dec", "12"},
        {"January", "01"}, {"February", "02"}, {"March", "03"}, {"April", "04"},
        {"May", "05"}, {"June", "06"}, {"July", "07"}, {"August", "08"},
        {"September", "09"}, {"October", "10"}, {"November", "11"}, {"December", "12"}
    };

    // Convert month to number
    std::string monthNum;
    for (const auto& m : months) {
        if (month.find(m.first) == 0) {
            monthNum = m.second;
            break;
        }
    }

    // Format day
    if (day.size() == 1) {
        day = "0" + day;
    }

    return year + "-" + monthNum + "-" + day;
}

int main() {
    std::string date = "1st January 2022";
    std::cout << reformatDate(date) << std::endl;
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string, due to the string operations.
> - **Space Complexity:** $O(1)$, since we use a fixed-size map to store the months.
> - **Optimality proof:** This solution is optimal because it uses a single pass through the input string and a fixed-size map to store the months.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: string parsing, mapping month names to numbers.
- Problem-solving patterns: using `std::istringstream` to parse input strings, using `std::unordered_map` to store mappings.
- Optimization techniques: using a fixed-size map to store the months, using a single pass through the input string.

**Mistakes to Avoid:**
- Not removing the suffix from the day.
- Not handling the different month formats (e.g., "Jan", "January").
- Not formatting the day correctly (e.g., adding a leading zero for single-digit days).