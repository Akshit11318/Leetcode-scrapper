## LeetCode Problem: Sleep
**Problem Link:** https://leetcode.com/problems/sleep/description

**Problem Statement:**
- The problem asks you to return the number of milliseconds until the next scheduled wake-up time, given the current time in milliseconds and a list of wake-up times in milliseconds.
- Input format and constraints: 
  - The current time is a non-negative integer.
  - The list of wake-up times is a list of non-negative integers.
- Expected output format: 
  - The number of milliseconds until the next scheduled wake-up time.
- Key requirements and edge cases to consider: 
  - If the current time is already a wake-up time, return 0.
  - If the current time is greater than all wake-up times, return the time until the next day's first wake-up time.

**Example Test Cases:**
- If the current time is 1 and the wake-up times are [1, 3, 5], return 0.
- If the current time is 2 and the wake-up times are [1, 3, 5], return 1.
- If the current time is 6 and the wake-up times are [1, 3, 5], return 1 (until the next day's first wake-up time).

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to iterate through the list of wake-up times and find the next wake-up time that is greater than the current time.
- If no such wake-up time is found, we need to consider the wake-up times for the next day.

```cpp
class Solution {
public:
    int sleep(int current, vector<int>& times) {
        // Sort the wake-up times
        sort(times.begin(), times.end());
        
        // Initialize the next wake-up time
        int nextWakeUp = INT_MAX;
        
        // Iterate through the wake-up times
        for (int time : times) {
            // If the current time is already a wake-up time, return 0
            if (time == current) {
                return 0;
            }
            // If the current time is less than a wake-up time, update the next wake-up time
            else if (time > current && time < nextWakeUp) {
                nextWakeUp = time;
            }
        }
        
        // If no next wake-up time is found, consider the wake-up times for the next day
        if (nextWakeUp == INT_MAX) {
            // Find the first wake-up time for the next day
            nextWakeUp = times[0];
            // Calculate the time until the next day's first wake-up time
            return nextWakeUp - current;
        }
        
        // Calculate the time until the next wake-up time
        return nextWakeUp - current;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting of the wake-up times, where $n$ is the number of wake-up times.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input and output.
> - **Why these complexities occur:** The sorting operation dominates the time complexity, while the space complexity is constant since we only use a fixed amount of space to store the next wake-up time.

---

### Optimal Approach (Required)
**Explanation:**
- We can improve the solution by using a more efficient data structure, such as a `set`, to store the wake-up times. This allows us to find the next wake-up time in $O(\log n)$ time.
- We can also eliminate the need for sorting by using a `set` to store the wake-up times.

```cpp
class Solution {
public:
    int sleep(int current, vector<int>& times) {
        // Create a set of wake-up times
        set<int> timeSet(times.begin(), times.end());
        
        // Initialize the next wake-up time
        int nextWakeUp = INT_MAX;
        
        // Find the next wake-up time
        auto it = timeSet.lower_bound(current);
        if (it != timeSet.end()) {
            nextWakeUp = *it;
        }
        
        // If no next wake-up time is found, consider the wake-up times for the next day
        if (nextWakeUp == INT_MAX) {
            // Find the first wake-up time for the next day
            nextWakeUp = *timeSet.begin();
            // Calculate the time until the next day's first wake-up time
            return nextWakeUp - current;
        }
        
        // Calculate the time until the next wake-up time
        return nextWakeUp - current;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log n)$, where $n$ is the number of wake-up times.
> - **Space Complexity:** $O(n)$, where $n$ is the number of wake-up times.
> - **Optimality proof:** This solution is optimal because it uses a `set` to store the wake-up times, allowing us to find the next wake-up time in $O(\log n)$ time. This is the best possible time complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: using a `set` to store wake-up times, finding the next wake-up time using `lower_bound`.
- Problem-solving patterns identified: using a more efficient data structure to improve the solution.
- Optimization techniques learned: eliminating the need for sorting by using a `set`.
- Similar problems to practice: finding the next occurrence of a given time, finding the closest pair of times.

**Mistakes to Avoid:**
- Common implementation errors: not handling the case where the current time is already a wake-up time, not considering the wake-up times for the next day.
- Edge cases to watch for: the current time being greater than all wake-up times, the list of wake-up times being empty.
- Performance pitfalls: using a inefficient data structure, such as a `vector`, to store the wake-up times.
- Testing considerations: testing the solution with different input cases, including edge cases and large inputs.