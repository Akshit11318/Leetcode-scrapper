## Button with Longest Push Time
**Problem Link:** https://leetcode.com/problems/button-with-longest-push-time/description

**Problem Statement:**
- Input format and constraints: The problem takes a string `current` representing the current time on a digital clock and a string `target` representing the target time. The `current` and `target` strings are in the format "HHMM", where the first two characters represent the hour and the last two characters represent the minutes.
- Expected output format: The function should return the button with the longest push time, which is the maximum number of times a button can be pressed to change the current time to the target time.
- Key requirements and edge cases to consider: The clock wraps around, meaning that if the hour or minute exceeds 23 or 59, respectively, it wraps around to 0. The function should handle edge cases such as when the current time is equal to the target time or when the target time is not reachable.
- Example test cases with explanations: For example, if the current time is "00:00" and the target time is "00:00", the function should return 0. If the current time is "00:00" and the target time is "23:59", the function should return 1439.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves simulating all possible button presses and checking if the current time matches the target time after each press.
- Step-by-step breakdown of the solution: 
  1. Convert the `current` and `target` strings to integers representing the total minutes since 00:00.
  2. Initialize a variable `max_time` to 0, which will store the maximum number of times a button can be pressed.
  3. Simulate all possible button presses by iterating over all possible hours and minutes.
  4. For each possible hour and minute, check if pressing the corresponding button would result in the target time.
  5. If pressing the button would result in the target time, update `max_time` with the maximum number of times the button can be pressed.

```cpp
int findMaxTime(const string& current, const string& target) {
    int currTime = stoi(current.substr(0, 2)) * 60 + stoi(current.substr(2));
    int targetTime = stoi(target.substr(0, 2)) * 60 + stoi(target.substr(2));
    int maxTime = 0;
    for (int i = 0; i <= 1439; i++) {
        int newTime = (currTime + i) % 1440;
        if (newTime == targetTime) {
            maxTime = i;
            break;
        }
    }
    return maxTime;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the maximum number of times a button can be pressed (1439 in this case).
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the variables.
> - **Why these complexities occur:** The time complexity occurs because we simulate all possible button presses, and the space complexity occurs because we only use a constant amount of space to store the variables.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution involves using the modulo operator to calculate the minimum number of times a button needs to be pressed to reach the target time.
- Detailed breakdown of the approach: 
  1. Calculate the difference between the target time and the current time.
  2. Use the modulo operator to calculate the minimum number of times a button needs to be pressed to reach the target time.
  3. Return the minimum number of times a button needs to be pressed.

```cpp
int findMaxTime(const string& current, const string& target) {
    int currTime = stoi(current.substr(0, 2)) * 60 + stoi(current.substr(2));
    int targetTime = stoi(target.substr(0, 2)) * 60 + stoi(target.substr(2));
    int diff = abs(targetTime - currTime);
    return min(diff, 1440 - diff);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, as we only perform a constant number of operations.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the variables.
> - **Optimality proof:** This solution is optimal because it directly calculates the minimum number of times a button needs to be pressed to reach the target time, without simulating all possible button presses.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the use of the modulo operator to calculate the minimum number of times a button needs to be pressed to reach the target time.
- Problem-solving patterns identified: The problem involves using a brute force approach and then optimizing it to find the optimal solution.
- Optimization techniques learned: The problem involves using the modulo operator to optimize the solution.
- Similar problems to practice: Similar problems to practice include problems that involve using the modulo operator to optimize solutions.

**Mistakes to Avoid:**
- Common implementation errors: A common implementation error is to simulate all possible button presses, which can result in a time complexity of $O(n)$.
- Edge cases to watch for: Edge cases to watch for include when the current time is equal to the target time or when the target time is not reachable.
- Performance pitfalls: A performance pitfall is to use a brute force approach, which can result in a time complexity of $O(n)$.
- Testing considerations: Testing considerations include testing the function with different inputs, such as when the current time is equal to the target time or when the target time is not reachable.