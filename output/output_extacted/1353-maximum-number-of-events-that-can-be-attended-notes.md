## Maximum Number of Events That Can Be Attended
**Problem Link:** https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/description

**Problem Statement:**
- Input format: An array of pairs representing events, where each pair contains the start and end day of the event.
- Constraints: The input array is non-empty and contains at most 100,000 events. Each event's start day is less than or equal to its end day.
- Expected output format: The maximum number of events that can be attended.
- Key requirements and edge cases to consider: The goal is to find the maximum number of non-overlapping events that can be attended. Events are considered non-overlapping if they do not share any common day.
- Example test cases with explanations:
  - For the input `[[1,2],[2,3],[3,4]]`, the output should be `3` because we can attend all three events.
  - For the input `[[1,2],[2,3],[3,4],[1,3]]`, the output should be `3` because we can attend the first three events.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: The first approach that comes to mind is to check every possible subset of events to see if they are non-overlapping.
- Step-by-step breakdown of the solution: Generate all possible subsets of events, then for each subset, check if any two events overlap. If not, count this subset as a valid set of non-overlapping events.
- Why this approach comes to mind first: It's the most straightforward way to ensure we don't miss any possible combinations of events.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int maxEvents(vector<vector<int>>& events) {
    int n = events.size();
    int maxEvents = 0;
    
    // Generate all subsets of events
    for (int mask = 0; mask < (1 << n); ++mask) {
        vector<vector<int>> subset;
        for (int i = 0; i < n; ++i) {
            if (mask & (1 << i)) {
                subset.push_back(events[i]);
            }
        }
        
        // Check if the subset contains non-overlapping events
        bool isNonOverlapping = true;
        for (int i = 0; i < subset.size(); ++i) {
            for (int j = i + 1; j < subset.size(); ++j) {
                if (!(subset[i][1] < subset[j][0] || subset[j][1] < subset[i][0])) {
                    isNonOverlapping = false;
                    break;
                }
            }
            if (!isNonOverlapping) break;
        }
        
        if (isNonOverlapping) {
            maxEvents = max(maxEvents, (int)subset.size());
        }
    }
    
    return maxEvents;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n^2)$, where $n$ is the number of events. This is because we generate all subsets of events (which takes $O(2^n)$ time) and then for each subset, we check for non-overlapping events in $O(n^2)$ time.
> - **Space Complexity:** $O(n)$, for storing the current subset of events.
> - **Why these complexities occur:** The brute force approach is inherently expensive because it considers all possible subsets of events, leading to exponential time complexity.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can use a priority queue to keep track of the events that can be attended on the current day and the following days. This way, we can efficiently select the event that ends earliest and thus has the least chance of conflicting with future events.
- Detailed breakdown of the approach: Sort the events by their start days. Then, iterate through each day from the earliest start day to the latest end day. For each day, add all events that start on or before this day to a priority queue (sorted by their end days). Then, pop events from the queue that end on or before the current day (since they cannot be attended anymore), and attend the event that ends earliest among the remaining events in the queue.
- Proof of optimality: This greedy approach is optimal because attending the event that ends earliest minimizes the chance of conflicting with future events, thus maximizing the number of events that can be attended.

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int maxEvents(vector<vector<int>>& events) {
    sort(events.begin(), events.end());
    priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> pq;
    int day = 1, i = 0, count = 0;
    
    while (i < events.size() || !pq.empty()) {
        if (pq.empty()) {
            day = events[i][0];
        }
        
        while (i < events.size() && events[i][0] <= day) {
            pq.push({events[i][1], events[i][0]});
            i++;
        }
        
        while (!pq.empty() && pq.top()[0] < day) {
            pq.pop();
        }
        
        if (!pq.empty()) {
            pq.pop();
            count++;
        }
        
        day++;
    }
    
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of events. This is because we sort the events and use a priority queue, both of which have logarithmic time complexity.
> - **Space Complexity:** $O(n)$, for storing the events in the priority queue.
> - **Optimality proof:** The greedy strategy ensures that we always choose the event that has the least chance of conflicting with future events, thus maximizing the number of events that can be attended.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Greedy algorithms, priority queues, and sorting.
- Problem-solving patterns identified: The use of priority queues to efficiently manage events based on their end days.
- Optimization techniques learned: The greedy approach and the use of data structures like priority queues to reduce time complexity.
- Similar problems to practice: Other problems involving scheduling or selecting non-overlapping intervals.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly implementing the priority queue or sorting the events.
- Edge cases to watch for: Events with the same start or end day, or events that span multiple days.
- Performance pitfalls: Using inefficient data structures or algorithms, such as the brute force approach.
- Testing considerations: Thoroughly testing the solution with various inputs, including edge cases and large datasets.