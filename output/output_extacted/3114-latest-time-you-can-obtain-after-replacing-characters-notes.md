## Latest Time by Replacing Hidden Digits
**Problem Link:** https://leetcode.com/problems/latest-time-you-can-obtain-after-replacing-characters/description

**Problem Statement:**
- Input format: `time` as a string in the format "HH:MM", and `replacementTime` as a string.
- Constraints: `time.length == 5`, `replacementTime.length == 5`, `time` is in the format "HH:MM", and `replacementTime` is in the format "HH:MM".
- Expected output format: Return the latest possible time you can obtain by replacing some of the hidden digits (`?`) in `time` with digits from `replacementTime`.
- Key requirements and edge cases to consider:
  - `replacementTime` can contain digits from 0 to 9.
  - If a digit in `time` is not hidden, it cannot be replaced.
  - If a digit in `time` is hidden, it must be replaced with a digit from `replacementTime`.
  - The resulting time must be valid (i.e., hours must be between 0 and 23, and minutes must be between 0 and 59).

**Example Test Cases:**
- `time = "2?:?0"`, `replacementTime = "2045"` -> Output: `"23:50"`
- `time = "0?:3?"`, `replacementTime = "105"` -> Output: `"09:35"`
- `time = "1?:22"`, `replacementTime = "123"` -> Output: `"12:22"`

---

### Brute Force Approach

**Explanation:**
- Try all possible combinations of replacing hidden digits with digits from `replacementTime`.
- For each combination, check if the resulting time is valid.
- Keep track of the latest valid time.

```cpp
#include <iostream>
#include <string>
using namespace std;

string maximumTime(string time, string replacementTime) {
    string maxTime = "";
    for (int h1 = 0; h1 < 10; h1++) {
        for (int h2 = 0; h2 < 10; h2++) {
            for (int m1 = 0; m1 < 10; m1++) {
                for (int m2 = 0; m2 < 10; m2++) {
                    string currentTime = to_string(h1) + to_string(h2) + ":" + to_string(m1) + to_string(m2);
                    if (isValidTime(currentTime, time, replacementTime) && currentTime > maxTime) {
                        maxTime = currentTime;
                    }
                }
            }
        }
    }
    return maxTime;
}

bool isValidTime(string time, string originalTime, string replacementTime) {
    for (int i = 0; i < 5; i++) {
        if (originalTime[i] != '?' && originalTime[i] != time[i]) {
            return false;
        }
    }
    int h1 = time[0] - '0';
    int h2 = time[1] - '0';
    int m1 = time[3] - '0';
    int m2 = time[4] - '0';
    if (h1 > 2 || (h1 == 2 && h2 > 3) || m1 > 5 || m2 > 9) {
        return false;
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(10^4)$, because we try all possible combinations of hours and minutes.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space.
> - **Why these complexities occur:** The brute force approach tries all possible combinations of hours and minutes, resulting in a high time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Start from the most significant digit (hours) and try to replace it with the largest possible digit from `replacementTime`.
- If the current digit is not hidden, we cannot replace it.
- If the current digit is hidden, we try to replace it with the largest possible digit from `replacementTime` that makes the time valid.
- We use a greedy approach to ensure that we get the latest possible time.

```cpp
string maximumTime(string time, string replacementTime) {
    string result = time;
    for (int i = 0; i < 5; i++) {
        if (time[i] == '?') {
            for (int j = 9; j >= 0; j--) {
                char c = j + '0';
                result[i] = c;
                if (isValidTime(result, replacementTime)) {
                    break;
                }
            }
        }
    }
    return result;
}

bool isValidTime(string time, string replacementTime) {
    int h1 = time[0] - '0';
    int h2 = time[1] - '0';
    int m1 = time[3] - '0';
    int m2 = time[4] - '0';
    if (h1 > 2 || (h1 == 2 && h2 > 3) || m1 > 5 || m2 > 9) {
        return false;
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(10 \cdot 5) = O(50)$, because we try at most 10 digits for each of the 5 positions.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space.
> - **Optimality proof:** This approach is optimal because it tries the largest possible digits first, ensuring that we get the latest possible time.

---

### Final Notes

**Learning Points:**
- The importance of using a greedy approach to solve problems that require maximizing or minimizing a value.
- How to use a brute force approach as a starting point and then optimize it.
- The importance of considering edge cases and validating inputs.

**Mistakes to Avoid:**
- Not considering edge cases, such as invalid times.
- Not validating inputs, such as checking if the replacement time is valid.
- Using a brute force approach without optimizing it.