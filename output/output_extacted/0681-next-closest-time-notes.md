## Next Closest Time
**Problem Link:** https://leetcode.com/problems/next-closest-time/description

**Problem Statement:**
- Input format: Given a time in string format `time`, where `time` is in the format `"HH:MM"`.
- Constraints: The input time is between `00:00` and `23:59`.
- Expected output format: The next closest time in the format `"HH:MM"`.
- Key requirements and edge cases to consider: The next closest time should be the smallest time that is greater than the given time and can be formed using the digits of the given time. If the next closest time is less than the given time, return the next closest time on the next day.
- Example test cases with explanations:
    - Input: `time = "19:39"`
      Output: `"19:39"`
      Explanation: The next closest time is the same as the given time because we cannot form a smaller time using the digits `1`, `9`, `3`, and `9`.
    - Input: `time = "23:59"`
      Output: `"00:00"`
      Explanation: The next closest time is on the next day.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Generate all possible times that can be formed using the digits of the given time, and then find the smallest time that is greater than the given time.
- Step-by-step breakdown of the solution:
  1. Generate all possible times that can be formed using the digits of the given time.
  2. Filter out the times that are not valid (i.e., the hour is greater than 23 or the minute is greater than 59).
  3. Find the smallest time that is greater than the given time.
- Why this approach comes to mind first: It is a straightforward approach that involves generating all possible combinations of the given digits and then filtering out the invalid ones.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

string nextClosestTime(string time) {
    vector<int> digits;
    for (char c : time) {
        if (c != ':') {
            digits.push_back(c - '0');
        }
    }
    
    vector<string> possibleTimes;
    for (int h1 : digits) {
        for (int h2 : digits) {
            for (int m1 : digits) {
                for (int m2 : digits) {
                    string hour = to_string(h1) + to_string(h2);
                    string minute = to_string(m1) + to_string(m2);
                    if (stoi(hour) < 24 && stoi(minute) < 60) {
                        possibleTimes.push_back(hour + ":" + minute);
                    }
                }
            }
        }
    }
    
    sort(possibleTimes.begin(), possibleTimes.end());
    for (string t : possibleTimes) {
        if (t > time) {
            return t;
        }
    }
    
    return possibleTimes[0];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^4 \log n)$, where $n$ is the number of unique digits in the given time. The reason is that we generate $n^4$ possible times and then sort them.
> - **Space Complexity:** $O(n^4)$, where $n$ is the number of unique digits in the given time. The reason is that we store all possible times in a vector.
> - **Why these complexities occur:** The brute force approach involves generating all possible combinations of the given digits, which results in a high time and space complexity.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Instead of generating all possible times, we can iterate through the possible hours and minutes and check if they can be formed using the given digits.
- Detailed breakdown of the approach:
  1. Iterate through the possible hours (from 0 to 23).
  2. For each hour, iterate through the possible minutes (from 0 to 59).
  3. Check if the hour and minute can be formed using the given digits.
  4. If they can be formed, calculate the time difference between the current time and the given time.
  5. Update the result if the time difference is smaller than the current minimum time difference.
- Proof of optimality: This approach is optimal because it only iterates through the possible hours and minutes once, and it checks if each time can be formed using the given digits in constant time.
- Why further optimization is impossible: This approach already has a time complexity of $O(1)$, which is the best possible time complexity for this problem.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

string nextClosestTime(string time) {
    int h1 = time[0] - '0';
    int h2 = time[1] - '0';
    int m1 = time[3] - '0';
    int m2 = time[4] - '0';
    
    vector<int> digits = {h1, h2, m1, m2};
    sort(digits.begin(), digits.end());
    
    vector<int> uniqueDigits;
    for (int d : digits) {
        if (uniqueDigits.empty() || uniqueDigits.back() != d) {
            uniqueDigits.push_back(d);
        }
    }
    
    int minutes = h1 * 10 * 60 + h2 * 60 + m1 * 10 + m2;
    int minDiff = 1440;
    int result = minutes;
    
    for (int i = 0; i < 24 * 60; i++) {
        int h = i / 60;
        int m = i % 60;
        int h1New = h / 10;
        int h2New = h % 10;
        int m1New = m / 10;
        int m2New = m % 10;
        
        if (find(uniqueDigits.begin(), uniqueDigits.end(), h1New) != uniqueDigits.end() &&
            find(uniqueDigits.begin(), uniqueDigits.end(), h2New) != uniqueDigits.end() &&
            find(uniqueDigits.begin(), uniqueDigits.end(), m1New) != uniqueDigits.end() &&
            find(uniqueDigits.begin(), uniqueDigits.end(), m2New) != uniqueDigits.end()) {
            int diff = (i - minutes + 1440) % 1440;
            if (diff < minDiff) {
                minDiff = diff;
                result = i;
            }
        }
    }
    
    string hour = to_string(result / 60);
    if (hour.length() == 1) {
        hour = "0" + hour;
    }
    string minute = to_string(result % 60);
    if (minute.length() == 1) {
        minute = "0" + minute;
    }
    
    return hour + ":" + minute;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, because we only iterate through the possible hours and minutes once, and the number of hours and minutes is constant.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the unique digits and the result.
> - **Optimality proof:** This approach is optimal because it only iterates through the possible hours and minutes once, and it checks if each time can be formed using the given digits in constant time.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, sorting, and checking if a time can be formed using given digits.
- Problem-solving patterns identified: The problem can be solved by iterating through the possible hours and minutes and checking if each time can be formed using the given digits.
- Optimization techniques learned: The optimal approach uses a constant amount of space and time, which is the best possible complexity for this problem.
- Similar problems to practice: Problems that involve iterating through possible combinations and checking if they satisfy certain conditions.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if the hour and minute can be formed using the given digits, or not handling the case where the time difference is negative.
- Edge cases to watch for: The case where the given time is 23:59, or the case where the given time is 00:00.
- Performance pitfalls: Using a brute force approach that generates all possible combinations of the given digits, which can result in a high time and space complexity.
- Testing considerations: Testing the function with different inputs, including edge cases, to ensure that it works correctly.