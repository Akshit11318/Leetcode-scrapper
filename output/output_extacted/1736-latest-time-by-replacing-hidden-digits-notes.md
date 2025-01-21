## Latest Time by Replacing Hidden Digits

**Problem Link:** https://leetcode.com/problems/latest-time-by-replacing-hidden-digits/description

**Problem Statement:**
- Input: A string `time` representing a time in the format `HH:MM`, where some digits are replaced with `?`.
- Constraints: `time` is a string of length 5, with the first two characters representing hours, the third character being a colon `:`, and the last two characters representing minutes.
- Expected output: The latest possible time that can be obtained by replacing the hidden digits, in the format `HH:MM`.
- Key requirements and edge cases:
  - The time must be in 24-hour format.
  - Hours range from `00` to `23`.
  - Minutes range from `00` to `59`.
- Example test cases:
  - Input: `"0?:3?"`, Output: `"09:39"`
  - Input: `"1?:22"`, Output: `"19:22"`

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to iterate over all possible combinations of hours and minutes, and then replace the hidden digits with the maximum possible value that still forms a valid time.
- Step-by-step breakdown:
  1. Iterate over all possible hours (00-23) and minutes (00-59).
  2. For each hour and minute, convert them to strings and compare with the input time.
  3. If a digit in the input time is hidden (represented by `?`), try to replace it with the corresponding digit from the current hour or minute.
  4. If the replacement results in a valid time, update the latest possible time.

```cpp
#include <string>
using namespace std;

string maximumTime(string time) {
    string maxTime = "00:00";
    for (int h = 0; h < 24; h++) {
        for (int m = 0; m < 60; m++) {
            string hour = to_string(h);
            string minute = to_string(m);
            if (hour.length() == 1) hour = "0" + hour;
            if (minute.length() == 1) minute = "0" + minute;
            string currentTime = hour + ":" + minute;
            bool isValid = true;
            for (int i = 0; i < 5; i++) {
                if (time[i] != '?' && time[i] != currentTime[i]) {
                    isValid = false;
                    break;
                }
            }
            if (isValid) {
                if (currentTime > maxTime) maxTime = currentTime;
            }
        }
    }
    return maxTime;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, since we are iterating over a fixed range of hours and minutes.
> - **Space Complexity:** $O(1)$, since we are using a constant amount of space to store the input and output strings.
> - **Why these complexities occur:** The time complexity is constant because we are iterating over a fixed range of hours and minutes, and the space complexity is constant because we are using a fixed amount of space to store the input and output strings.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to directly construct the latest possible time by replacing the hidden digits with the maximum possible value that still forms a valid time.
- Step-by-step breakdown:
  1. Initialize the latest possible time as an empty string.
  2. Iterate over each character in the input time.
  3. If the character is a hidden digit (represented by `?`), replace it with the maximum possible digit that still forms a valid time.
  4. If the character is not a hidden digit, append it to the latest possible time as is.

```cpp
#include <string>
using namespace std;

string maximumTime(string time) {
    if (time[0] == '?') {
        time[0] = (time[1] == '?' || time[1] < '4') ? '2' : '1';
    }
    if (time[1] == '?') {
        time[1] = (time[0] == '2') ? '3' : '9';
    }
    if (time[3] == '?') {
        time[3] = '5';
    }
    if (time[4] == '?') {
        time[4] = '9';
    }
    return time;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, since we are iterating over a fixed range of characters in the input time.
> - **Space Complexity:** $O(1)$, since we are using a constant amount of space to store the input and output strings.
> - **Optimality proof:** This approach is optimal because we are directly constructing the latest possible time by replacing the hidden digits with the maximum possible value that still forms a valid time, without iterating over all possible combinations of hours and minutes.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: direct construction, replacement of hidden digits.
- Problem-solving patterns identified: constructing the latest possible time by replacing hidden digits with the maximum possible value that still forms a valid time.
- Optimization techniques learned: avoiding unnecessary iterations over all possible combinations of hours and minutes.
- Similar problems to practice: problems involving direct construction and replacement of hidden digits.

**Mistakes to Avoid:**
- Common implementation errors: iterating over all possible combinations of hours and minutes instead of directly constructing the latest possible time.
- Edge cases to watch for: handling hidden digits in the hours and minutes, ensuring that the constructed time is valid.
- Performance pitfalls: using unnecessary iterations or recursive calls.
- Testing considerations: testing the function with different input strings, including those with hidden digits in the hours and minutes.