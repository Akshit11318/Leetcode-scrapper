## Convert Date to Binary
**Problem Link:** https://leetcode.com/problems/convert-date-to-binary/description

**Problem Statement:**
- Input: A string representing a date in the format "YYYY-MM-DD".
- Output: A string representing the binary format of the date.
- Key requirements and edge cases: The input date must be in the format "YYYY-MM-DD" and the output should be a string representing the binary format of the date.
- Example test cases:
  - Input: "2022-09-01"
  - Output: "10011110010"
  - Explanation: The binary representation of the year "2022" is "11111101110", the binary representation of the month "09" is "1001", and the binary representation of the day "01" is "1". The output is the concatenation of these binary representations.

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to convert each part of the date (year, month, day) into its binary representation and then concatenate them.
- Step-by-step breakdown:
  1. Split the input string into year, month, and day.
  2. Convert each part into its binary representation using a loop to check each bit.
  3. Concatenate the binary representations of year, month, and day.

```cpp
class Solution {
public:
    string dayOfTheWeek(int day, int month, int year) {
        // Not needed for this problem
    }

    string convertDateToBinary(string date) {
        istringstream iss(date);
        string year, month, day;
        getline(iss, year, '-');
        getline(iss, month, '-');
        getline(iss, day);
        
        string binaryYear, binaryMonth, binaryDay;
        // Convert year to binary
        int yearInt = stoi(year);
        while (yearInt > 0) {
            binaryYear = (yearInt % 2 == 0 ? "0" : "1") + binaryYear;
            yearInt /= 2;
        }
        
        // Convert month to binary
        int monthInt = stoi(month);
        while (monthInt > 0) {
            binaryMonth = (monthInt % 2 == 0 ? "0" : "1") + binaryMonth;
            monthInt /= 2;
        }
        
        // Convert day to binary
        int dayInt = stoi(day);
        while (dayInt > 0) {
            binaryDay = (dayInt % 2 == 0 ? "0" : "1") + binaryDay;
            dayInt /= 2;
        }
        
        return binaryYear + binaryMonth + binaryDay;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log(year) + \log(month) + \log(day))$ because we are converting each part of the date to binary.
> - **Space Complexity:** $O(\log(year) + \log(month) + \log(day))$ because we are storing the binary representation of each part.
> - **Why these complexities occur:** The time complexity occurs because we are using a loop to convert each part of the date to binary. The space complexity occurs because we are storing the binary representation of each part.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to use bitwise operators to convert each part of the date to binary, which is more efficient than using a loop.
- Detailed breakdown:
  1. Split the input string into year, month, and day.
  2. Convert each part to an integer.
  3. Use `bitset` to convert each integer to binary.

```cpp
class Solution {
public:
    string convertDateToBinary(string date) {
        istringstream iss(date);
        string year, month, day;
        getline(iss, year, '-');
        getline(iss, month, '-');
        getline(iss, day);
        
        int yearInt = stoi(year);
        int monthInt = stoi(month);
        int dayInt = stoi(day);
        
        bitset<32> binaryYear(yearInt);
        bitset<32> binaryMonth(monthInt);
        bitset<32> binaryDay(dayInt);
        
        return binaryYear.to_string() + binaryMonth.to_string() + binaryDay.to_string();
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log(year) + \log(month) + \log(day))$ because we are converting each part of the date to binary.
> - **Space Complexity:** $O(\log(year) + \log(month) + \log(day))$ because we are storing the binary representation of each part.
> - **Optimality proof:** This approach is optimal because we are using the most efficient method to convert each part of the date to binary.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: bitwise operators, `bitset`.
- Problem-solving patterns identified: using bitwise operators to convert integers to binary.
- Optimization techniques learned: using `bitset` to convert integers to binary.
- Similar problems to practice: converting integers to binary, using bitwise operators.

**Mistakes to Avoid:**
- Common implementation errors: not checking for invalid input, not handling edge cases.
- Edge cases to watch for: invalid input, overflow.
- Performance pitfalls: using inefficient methods to convert integers to binary.
- Testing considerations: testing with different input values, testing for edge cases.