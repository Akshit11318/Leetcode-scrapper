## Binary Watch
**Problem Link:** https://leetcode.com/problems/binary-watch/description

**Problem Statement:**
- Input: An integer `num` representing the number of buttons to press.
- Output: A list of all possible times that can be displayed on the binary watch, where each time is represented in the format "h:mm".
- Constraints: The binary watch has `10` buttons, with the first `4` buttons representing the hours (`1`, `2`, `4`, `8`) and the last `6` buttons representing the minutes (`1`, `2`, `4`, `8`, `16`, `32`).
- Key requirements: Generate all possible times that can be displayed by pressing `num` buttons.
- Example test cases:
  - Input: `num = 1`
  - Output: `["1:00","2:00","4:00","8:00","0:01","0:02","0:04","0:08","0:16","0:32"]`
  - Explanation: All possible times that can be displayed by pressing `1` button.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through all possible combinations of pressing `num` buttons.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of `num` buttons.
  2. For each combination, calculate the time displayed on the binary watch.
  3. Add the time to the result list if it is a valid time.

```cpp
class Solution {
public:
    vector<string> readBinaryWatch(int num) {
        vector<string> result;
        for (int i = 0; i < (1 << 10); i++) {
            int count = __builtin_popcount(i);
            if (count == num) {
                int hour = (i >> 6) & 0xf;
                int minute = i & 0x3f;
                if (hour < 12 && minute < 60) {
                    string time = to_string(hour) + ":";
                    if (minute < 10) time += "0";
                    time += to_string(minute);
                    result.push_back(time);
                }
            }
        }
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{10}) = O(1024)$, because we iterate through all possible combinations of `10` buttons.
> - **Space Complexity:** $O(2^{10}) = O(1024)$, because in the worst case, we need to store all possible combinations of `10` buttons.
> - **Why these complexities occur:** The brute force approach requires iterating through all possible combinations of `10` buttons, resulting in exponential time and space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of generating all possible combinations of `10` buttons, we can iterate through all possible combinations of `4` hour buttons and `6` minute buttons separately.
- Detailed breakdown of the approach:
  1. Iterate through all possible combinations of `4` hour buttons.
  2. For each combination of hour buttons, iterate through all possible combinations of `6` minute buttons.
  3. Calculate the time displayed on the binary watch for each combination of hour and minute buttons.
  4. Add the time to the result list if it is a valid time.

```cpp
class Solution {
public:
    vector<string> readBinaryWatch(int num) {
        vector<string> result;
        for (int i = 0; i < (1 << 4); i++) {
            for (int j = 0; j < (1 << 6); j++) {
                if (__builtin_popcount(i) + __builtin_popcount(j) == num) {
                    int hour = i;
                    int minute = j;
                    if (hour < 12 && minute < 60) {
                        string time = to_string(hour) + ":";
                        if (minute < 10) time += "0";
                        time += to_string(minute);
                        result.push_back(time);
                    }
                }
            }
        }
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^4 \times 2^6) = O(1024)$, because we iterate through all possible combinations of `4` hour buttons and `6` minute buttons.
> - **Space Complexity:** $O(2^4 \times 2^6) = O(1024)$, because in the worst case, we need to store all possible combinations of `4` hour buttons and `6` minute buttons.
> - **Optimality proof:** This approach is optimal because we only iterate through the necessary combinations of hour and minute buttons, resulting in the minimum possible time and space complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Bit manipulation, iteration through combinations.
- Problem-solving patterns identified: Breaking down the problem into smaller sub-problems (hour and minute buttons).
- Optimization techniques learned: Iterating through necessary combinations only.
- Similar problems to practice: Other bit manipulation and combination problems.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect bit manipulation, incorrect iteration through combinations.
- Edge cases to watch for: Invalid times (hour >= 12 or minute >= 60).
- Performance pitfalls: Iterating through all possible combinations of `10` buttons.
- Testing considerations: Test with different inputs (e.g., `num = 0`, `num = 1`, `num = 10`).