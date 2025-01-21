## Find Longest Calls
**Problem Link:** https://leetcode.com/problems/find-longest-calls/description

**Problem Statement:**
- Input format and constraints: Given a list of `calls` where each call is represented as a pair of start and end times, find the longest call in the list.
- Expected output format: Return the longest call.
- Key requirements and edge cases to consider: 
    - The input list may be empty.
    - There may be multiple calls with the same maximum duration.
    - The calls are represented as pairs of integers, where the first integer is the start time and the second integer is the end time.
- Example test cases with explanations:
    - If the input is `[[0, 3], [1, 2], [2, 4]]`, the output should be `[2, 4]`.
    - If the input is `[[0, 3], [1, 2], [2, 4], [3, 5]]`, the output should be `[3, 5]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find the longest call, we can iterate through each call in the list and calculate its duration.
- Step-by-step breakdown of the solution:
    1. Initialize the maximum duration to 0 and the longest call to an empty list.
    2. Iterate through each call in the list.
    3. For each call, calculate its duration by subtracting the start time from the end time.
    4. If the duration of the current call is greater than the maximum duration, update the maximum duration and the longest call.
- Why this approach comes to mind first: This approach is straightforward and easy to understand. It simply involves iterating through each call and keeping track of the call with the maximum duration.

```cpp
#include <vector>
#include <algorithm>

std::vector<int> findLongestCalls(std::vector<std::vector<int>>& calls) {
    if (calls.empty()) {
        return {};
    }

    int maxDuration = 0;
    std::vector<int> longestCall;

    for (const auto& call : calls) {
        int duration = call[1] - call[0];
        if (duration > maxDuration) {
            maxDuration = duration;
            longestCall = call;
        }
    }

    return longestCall;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of calls. This is because we iterate through each call once.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the maximum duration and the longest call.
> - **Why these complexities occur:** The time complexity is linear because we only iterate through the list of calls once. The space complexity is constant because we only use a fixed amount of space to store the maximum duration and the longest call.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The brute force approach is already optimal because it only requires a single pass through the list of calls.
- Detailed breakdown of the approach: The optimal approach is the same as the brute force approach.
- Proof of optimality: This approach is optimal because it only requires a single pass through the list of calls, and it uses a constant amount of space.
- Why further optimization is impossible: Further optimization is impossible because we must at least read the input once to find the longest call.

```cpp
#include <vector>
#include <algorithm>

std::vector<int> findLongestCalls(std::vector<std::vector<int>>& calls) {
    if (calls.empty()) {
        return {};
    }

    int maxDuration = 0;
    std::vector<int> longestCall;

    for (const auto& call : calls) {
        int duration = call[1] - call[0];
        if (duration > maxDuration) {
            maxDuration = duration;
            longestCall = call;
        }
    }

    return longestCall;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of calls.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the maximum duration and the longest call.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the list of calls.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, comparison, and updating of maximum values.
- Problem-solving patterns identified: Finding the maximum or minimum value in a list.
- Optimization techniques learned: Using a single pass through the list to find the maximum value.
- Similar problems to practice: Finding the maximum or minimum value in a list, finding the longest or shortest string in a list.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for an empty input list, not initializing the maximum duration to 0.
- Edge cases to watch for: An empty input list, multiple calls with the same maximum duration.
- Performance pitfalls: Using more than a single pass through the list, using more than a constant amount of space.
- Testing considerations: Test with an empty input list, test with multiple calls with the same maximum duration, test with a large input list.