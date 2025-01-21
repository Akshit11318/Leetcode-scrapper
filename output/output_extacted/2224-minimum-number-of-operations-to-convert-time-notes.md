## Minimum Number of Operations to Convert Time
**Problem Link:** https://leetcode.com/problems/minimum-number-of-operations-to-convert-time/description

**Problem Statement:**
- Input: Two strings `current` and `correct`, representing time in the format "HH:MM".
- Constraints: Both strings are in the format "HH:MM" and represent valid times.
- Expected Output: The minimum number of operations required to convert `current` to `correct`. An operation is defined as either adding 1 minute or 60 minutes to the time.
- Key Requirements: Find the minimum number of operations to convert one time to another, considering the wrap-around of hours and minutes.
- Example Test Cases:
  - Input: `current = "02:30", correct = "04:35"`; Output: `3` (Explanation: Convert "02:30" to "04:30" by adding 60 minutes twice, then add 5 minutes to get "04:35".)

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of adding 1 minute or 60 minutes to `current` until we reach `correct`.
- Step-by-step breakdown:
  1. Convert both times to minutes past midnight.
  2. Calculate the absolute difference between the two times in minutes.
  3. Try all possible combinations of adding 1 or 60 minutes to `current` to reach `correct`, counting the minimum number of operations.
- Why this approach comes to mind first: It directly attempts to solve the problem by considering all possible operations.

```cpp
#include <iostream>
#include <string>
using namespace std;

int convertTime(string current, string correct) {
    int currTime = stoi(current.substr(0, 2)) * 60 + stoi(current.substr(3));
    int corrTime = stoi(correct.substr(0, 2)) * 60 + stoi(correct.substr(3));
    int diff = abs(corrTime - currTime);
    int minOps = diff;
    for (int i = 0; i <= diff / 60; i++) {
        int ops = i + (diff - i * 60);
        minOps = min(minOps, ops);
    }
    return minOps;
}

int main() {
    string current, correct;
    current = "02:30";
    correct = "04:35";
    cout << convertTime(current, correct) << endl;
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the difference in minutes between the two times, because we potentially iterate through all possible minute differences.
> - **Space Complexity:** $O(1)$, as we use a constant amount of space.
> - **Why these complexities occur:** The brute force approach requires iterating through all possible minute differences to find the minimum number of operations, leading to a linear time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: The problem can be solved by finding the minimum number of operations (either adding 1 minute or 60 minutes) needed to bridge the time difference between `current` and `correct`.
- Detailed breakdown:
  1. Calculate the absolute difference in minutes between `current` and `correct`.
  2. The minimum number of operations is the minimum between the difference itself (if we only add 1 minute at a time) and the remainder when the difference is divided by 60 plus the quotient (if we add 60 minutes when possible and 1 minute otherwise).
- Proof of optimality: This approach considers the optimal division between adding 1 minute and 60 minutes to minimize the total number of operations.

```cpp
#include <iostream>
#include <string>
using namespace std;

int convertTime(string current, string correct) {
    int currTime = stoi(current.substr(0, 2)) * 60 + stoi(current.substr(3));
    int corrTime = stoi(correct.substr(0, 2)) * 60 + stoi(correct.substr(3));
    int diff = abs(corrTime - currTime);
    // Considering the wrap-around
    diff = min(diff, 24 * 60 - diff);
    return (diff / 60) + (diff % 60);
}

int main() {
    string current, correct;
    current = "02:30";
    correct = "04:35";
    cout << convertTime(current, correct) << endl;
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, as we perform a constant number of operations regardless of the input size.
> - **Space Complexity:** $O(1)$, for the same reason as the time complexity.
> - **Optimality proof:** This solution directly calculates the minimum number of operations required, considering both the addition of 1 minute and 60 minutes, and accounts for the wrap-around of time, making it optimal.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Optimal division of operations to minimize the total count.
- Problem-solving patterns identified: Considering the wrap-around of time and the optimal use of operations.
- Optimization techniques learned: Direct calculation of the minimum number of operations based on the time difference.
- Similar problems to practice: Other problems involving minimum operations to achieve a target state.

**Mistakes to Avoid:**
- Common implementation errors: Not considering the wrap-around of time.
- Edge cases to watch for: When the time difference is exactly divisible by 60.
- Performance pitfalls: Using inefficient algorithms that iterate through all possible time differences.
- Testing considerations: Ensure to test cases with different time differences, including those that require wrapping around and those that do not.