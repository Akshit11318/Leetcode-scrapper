## Minimum Number of Chairs in a Waiting Room
**Problem Link:** https://leetcode.com/problems/minimum-number-of-chairs-in-a-waiting-room/description

**Problem Statement:**
- Input format: `times` array, where each element is a pair of integers representing the arrival and departure time of a person.
- Constraints: Arrival times are strictly increasing, and the length of `times` is at least 1.
- Expected output format: The minimum number of chairs needed.
- Key requirements: The waiting room should accommodate all people, and the number of chairs should be minimized.
- Edge cases: Consider the scenario where a person departs immediately after another person arrives.

**Example Test Cases:**
- `times = [[1,2],[2,3],[3,4]]`, the minimum number of chairs needed is 2.
- `times = [[1,4],[2,3],[3,4]]`, the minimum number of chairs needed is 2.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: We can simulate the waiting room by iterating through each time interval and keeping track of the number of people in the room.
- Step-by-step breakdown:
  1. Sort the `times` array by arrival time.
  2. Initialize a variable `chairs` to 0, representing the current number of chairs needed.
  3. Iterate through the `times` array:
     - For each person, increment `chairs` by 1 when they arrive.
     - When a person departs, decrement `chairs` by 1.
     - Update the maximum value of `chairs` seen so far.
- Why this approach comes to mind first: It's a straightforward simulation of the waiting room scenario.

```cpp
int minChairs(vector<vector<int>>& times) {
    int chairs = 0, maxChairs = 0;
    vector<pair<int, int>> events; // <time, 1 for arrival, -1 for departure>
    
    for (auto& time : times) {
        events.push_back({time[0], 1});
        events.push_back({time[1], -1});
    }
    
    sort(events.begin(), events.end());
    
    for (auto& event : events) {
        chairs += event.second;
        maxChairs = max(maxChairs, chairs);
    }
    
    return maxChairs;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of people. This is due to sorting the `events` array.
> - **Space Complexity:** $O(n)$, as we need to store all events in the `events` array.
> - **Why these complexities occur:** The sorting operation dominates the time complexity, while the space complexity is linear due to storing all events.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: We can use a `multiset` to store the departure times of people currently in the room. This allows us to efficiently find the earliest departure time when a new person arrives.
- Detailed breakdown:
  1. Initialize a `multiset` `departureTimes` to store the departure times of people in the room.
  2. Initialize a variable `chairs` to 0, representing the current number of chairs needed.
  3. Iterate through the `times` array:
     - For each person, if the `departureTimes` set is not empty and the earliest departure time is earlier than or equal to the current arrival time, remove the earliest departure time from the set and decrement `chairs`.
     - Increment `chairs` by 1 for the new person.
     - Add the departure time of the new person to the `departureTimes` set.
- Proof of optimality: This approach ensures that we always have the minimum number of chairs needed, as we reuse chairs as soon as possible.

```cpp
int minChairs(vector<vector<int>>& times) {
    multiset<int> departureTimes;
    int chairs = 0, maxChairs = 0;
    
    for (auto& time : times) {
        if (!departureTimes.empty() && *departureTimes.begin() <= time[0]) {
            departureTimes.erase(departureTimes.begin());
            chairs--;
        }
        chairs++;
        departureTimes.insert(time[1]);
        maxChairs = max(maxChairs, chairs);
    }
    
    return maxChairs;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of people. This is due to inserting and removing elements from the `departureTimes` set.
> - **Space Complexity:** $O(n)$, as we need to store all departure times in the `departureTimes` set.
> - **Optimality proof:** This approach ensures that we always have the minimum number of chairs needed, as we reuse chairs as soon as possible.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: Using a `multiset` to efficiently manage departure times.
- Problem-solving patterns: Reusing resources (chairs) as soon as possible to minimize the total number needed.
- Optimization techniques: Using a `multiset` to reduce the time complexity of finding the earliest departure time.

**Mistakes to Avoid:**
- Not considering the scenario where a person departs immediately after another person arrives.
- Not using a data structure like a `multiset` to efficiently manage departure times.
- Not reusing chairs as soon as possible to minimize the total number needed.