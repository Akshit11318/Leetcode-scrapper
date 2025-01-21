## The Latest Time to Catch a Bus
**Problem Link:** https://leetcode.com/problems/the-latest-time-to-catch-a-bus/description

**Problem Statement:**
- Given a list of `buses` where each bus is represented as a time in the format `HH:MM`, and a time `arrivalTime` in the same format, find the latest time to catch a bus.
- The input `buses` will be in ascending order, and there will be no duplicate times.
- The `arrivalTime` will be in the format `HH:MM`, and it will be earlier than or equal to the last bus time.
- Return the latest time to catch a bus in the format `HH:MM`.

**Example Test Cases:**
- For `buses = ["10:00","10:01","10:02"]` and `arrivalTime = "09:59"`, the output will be `"10:01"`.
- For `buses = ["23:00","23:59"]` and `arrivalTime = "23:00"`, the output will be `"23:00"`.

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to iterate through each bus time and compare it with the arrival time.
- If the bus time is greater than the arrival time, we can return the previous bus time as the latest time to catch a bus.
- If the bus time is less than or equal to the arrival time, we continue to the next bus time.

```cpp
#include <vector>
#include <string>

class Solution {
public:
    string latestTimeCatchBus(vector<string>& buses, string arrivalTime) {
        int arrivalTimeInMinutes = stoi(arrivalTime.substr(0, 2)) * 60 + stoi(arrivalTime.substr(3));
        for (int i = buses.size() - 1; i >= 0; --i) {
            int busTimeInMinutes = stoi(buses[i].substr(0, 2)) * 60 + stoi(buses[i].substr(3));
            if (busTimeInMinutes <= arrivalTimeInMinutes) {
                return buses[i];
            }
        }
        return "";
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of buses. This is because in the worst case, we need to iterate through all the buses.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the arrival time and bus times in minutes.
> - **Why these complexities occur:** The time complexity occurs because we are iterating through the buses, and the space complexity occurs because we are only using a constant amount of space.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to convert the arrival time and bus times into minutes since the start of the day.
- We can then iterate through the buses in reverse order and return the first bus time that is less than or equal to the arrival time.
- This approach is optimal because we are only iterating through the buses once, and we are using a constant amount of space.

```cpp
#include <vector>
#include <string>

class Solution {
public:
    string latestTimeCatchBus(vector<string>& buses, string arrivalTime) {
        int arrivalTimeInMinutes = stoi(arrivalTime.substr(0, 2)) * 60 + stoi(arrivalTime.substr(3));
        for (int i = buses.size() - 1; i >= 0; --i) {
            int busTimeInMinutes = stoi(buses[i].substr(0, 2)) * 60 + stoi(buses[i].substr(3));
            if (busTimeInMinutes <= arrivalTimeInMinutes) {
                return buses[i];
            }
        }
        return "";
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of buses. This is because in the worst case, we need to iterate through all the buses.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the arrival time and bus times in minutes.
> - **Optimality proof:** This approach is optimal because we are only iterating through the buses once, and we are using a constant amount of space.

---

### Final Notes
**Learning Points:**
- The key algorithmic concept demonstrated is the use of iteration to find the latest time to catch a bus.
- The problem-solving pattern identified is the use of a brute force approach and then optimizing it to achieve the optimal solution.
- The optimization technique learned is the use of iteration in reverse order to find the first bus time that is less than or equal to the arrival time.

**Mistakes to Avoid:**
- A common implementation error is to iterate through the buses in the wrong order.
- An edge case to watch for is when the arrival time is earlier than the first bus time.
- A performance pitfall is to use an inefficient algorithm that has a high time complexity.
- A testing consideration is to test the solution with different input scenarios, including edge cases.