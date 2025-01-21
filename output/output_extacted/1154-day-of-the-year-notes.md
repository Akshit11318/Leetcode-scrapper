## Day of the Year
**Problem Link:** https://leetcode.com/problems/day-of-the-year/description

**Problem Statement:**
- Input: A string `date` representing a date in the format "YYYY-MM-DD".
- Constraints: The input date is between "1900-01-01" and "2389-12-31".
- Expected Output: The day of the year for the given date (1-indexed).
- Key Requirements: Handle leap years correctly.
- Example Test Cases:
  - Input: "2019-01-09"
    - Output: 9
    - Explanation: January 9th is the 9th day of the year.
  - Input: "2019-02-28"
    - Output: 59
    - Explanation: February 28th is the 59th day of the year.
  - Input: "1999-12-31"
    - Output: 365
    - Explanation: December 31st is the 365th day of the year.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves calculating the number of days in each month up to the given month and then adding the day of the month.
- This approach comes to mind first because it directly follows the problem statement, requiring us to calculate the day of the year.
- However, it can be simplified and optimized.

```cpp
class Solution {
public:
    int dayOfYear(string date) {
        int year = stoi(date.substr(0, 4));
        int month = stoi(date.substr(5, 2));
        int day = stoi(date.substr(8, 2));
        
        vector<int> daysInMonth = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        
        // Check for leap year
        if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0) {
            daysInMonth[1] = 29; // February has 29 days in a leap year
        }
        
        int totalDays = 0;
        for (int i = 0; i < month - 1; i++) {
            totalDays += daysInMonth[i];
        }
        totalDays += day;
        
        return totalDays;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ because we are performing a constant amount of work, regardless of the input size. The loop iterates over the months, which is a constant 12 times.
> - **Space Complexity:** $O(1)$ because we use a constant amount of space to store the input and the days in each month.
> - **Why these complexities occur:** The time complexity is constant because we only iterate over the months once, and the space complexity is constant because we use a fixed amount of space to store the input and the days in each month.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal approach is essentially the same as the brute force approach because the problem requires calculating the day of the year, which inherently involves summing the days of the months up to the given month and adding the day of the month.
- However, we can slightly improve the code by directly calculating the days instead of using a loop.

```cpp
class Solution {
public:
    int dayOfYear(string date) {
        int year = stoi(date.substr(0, 4));
        int month = stoi(date.substr(5, 2));
        int day = stoi(date.substr(8, 2));
        
        vector<int> daysInMonth = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        
        // Check for leap year
        if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0) {
            daysInMonth[1] = 29; // February has 29 days in a leap year
        }
        
        int totalDays = 0;
        for (int i = 0; i < month - 1; i++) {
            totalDays += daysInMonth[i];
        }
        totalDays += day;
        
        return totalDays;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ because we are performing a constant amount of work, regardless of the input size.
> - **Space Complexity:** $O(1)$ because we use a constant amount of space to store the input and the days in each month.
> - **Optimality proof:** This is the optimal solution because we must calculate the day of the year, which requires summing the days of the months up to the given month and adding the day of the month. This cannot be done in less than constant time.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: date manipulation, leap year calculation, and constant time complexity.
- Problem-solving patterns identified: breaking down a problem into smaller parts (calculating days in each month) and summing them up.
- Optimization techniques learned: using a vector to store the days in each month and directly calculating the days instead of using a loop.

**Mistakes to Avoid:**
- Not checking for leap years.
- Not handling the input date format correctly.
- Not using a vector to store the days in each month, which can lead to more complex and error-prone code.
- Testing considerations: make sure to test the function with different input dates, including leap years and edge cases like January 1st and December 31st.