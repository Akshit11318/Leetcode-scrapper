## Active Businesses
**Problem Link:** https://leetcode.com/problems/active-businesses/description

**Problem Statement:**
- Input format: `events` table with columns `event_type`, `business_id`, and `event_date`.
- Constraints: `events` table will have rows in the range of $[1, 10^5]$.
- Expected output format: A list of `business_id`s that are active on or after the current date.
- Key requirements: Identify active businesses by counting the number of events for each business, considering the event type as either 'start' or 'end'.
- Edge cases: Handle cases where the event date is earlier than the current date.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through the `events` table, counting the number of 'start' and 'end' events for each business.
- Step-by-step breakdown:
  1. Create a dictionary to store the count of 'start' and 'end' events for each business.
  2. Iterate through the `events` table, updating the count of 'start' and 'end' events for each business.
  3. For each business, calculate the net count of 'start' events by subtracting the count of 'end' events from the count of 'start' events.
  4. Filter businesses with a positive net count of 'start' events.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>

using namespace std;

struct Event {
    string event_type;
    int business_id;
    string event_date;
};

vector<int> activeBusinesses(vector<Event>& events, string current_date) {
    unordered_map<int, int> business_count;
    for (const auto& event : events) {
        if (event.event_type == "start") {
            business_count[event.business_id]++;
        } else if (event.event_type == "end") {
            business_count[event.business_id]--;
        }
    }

    vector<int> active_businesses;
    for (const auto& pair : business_count) {
        if (pair.second > 0) {
            active_businesses.push_back(pair.first);
        }
    }
    return active_businesses;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of rows in the `events` table, since we iterate through the table once.
> - **Space Complexity:** $O(n)$, as in the worst case, we might store all businesses in the dictionary.
> - **Why these complexities occur:** The brute force approach has a linear time complexity due to the single pass through the `events` table, and the space complexity is also linear due to the storage of business counts in the dictionary.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Utilize a dictionary to store the count of 'start' and 'end' events for each business, and filter businesses with a positive net count of 'start' events.
- Detailed breakdown:
  1. Create a dictionary to store the count of 'start' and 'end' events for each business.
  2. Iterate through the `events` table, updating the count of 'start' and 'end' events for each business.
  3. For each business, calculate the net count of 'start' events by subtracting the count of 'end' events from the count of 'start' events.
  4. Filter businesses with a positive net count of 'start' events.
- Proof of optimality: This approach is optimal because it only requires a single pass through the `events` table, resulting in a linear time complexity.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>

using namespace std;

struct Event {
    string event_type;
    int business_id;
    string event_date;
};

vector<int> activeBusinesses(vector<Event>& events, string current_date) {
    unordered_map<int, int> business_count;
    for (const auto& event : events) {
        if (event.event_type == "start") {
            business_count[event.business_id]++;
        } else if (event.event_type == "end") {
            business_count[event.business_id]--;
        }
    }

    vector<int> active_businesses;
    for (const auto& pair : business_count) {
        if (pair.second > 0) {
            active_businesses.push_back(pair.first);
        }
    }
    return active_businesses;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of rows in the `events` table, since we iterate through the table once.
> - **Space Complexity:** $O(n)$, as in the worst case, we might store all businesses in the dictionary.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the `events` table, resulting in a linear time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dictionary usage, event counting, and business filtering.
- Problem-solving patterns identified: Utilizing dictionaries for efficient data storage and retrieval.
- Optimization techniques learned: Reducing the number of passes through the data to achieve optimal time complexity.
- Similar problems to practice: Other problems involving data filtering and counting, such as finding the most frequent element in an array.

**Mistakes to Avoid:**
- Common implementation errors: Failing to initialize the dictionary, incorrect event type comparisons, and not handling edge cases.
- Edge cases to watch for: Businesses with no events, events with invalid types, and events with dates earlier than the current date.
- Performance pitfalls: Using inefficient data structures, such as arrays or linked lists, instead of dictionaries.
- Testing considerations: Thoroughly testing the function with various input scenarios, including edge cases and large datasets.