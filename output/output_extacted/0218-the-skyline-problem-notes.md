## The Skyline Problem
**Problem Link:** [https://leetcode.com/problems/the-skyline-problem/description](https://leetcode.com/problems/the-skyline-problem/description)

**Problem Statement:**
- Input format: A list of buildings, where each building is represented by a list of three integers `[left, right, height]`.
- Constraints: `0 <= left < right <= 2^31 - 1`, `1 <= height <= 2^31 - 1`, and `1 <= buildings.length <= 1000`.
- Expected output format: A list of lists, where each sublist contains two integers representing the x-coordinate and the height of a key point in the skyline.
- Key requirements and edge cases to consider: The output should be sorted by the x-coordinate, and there should be no duplicate key points.
- Example test cases with explanations:
  - Example 1: `[[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]`. The output should be `[[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]`.
  - Example 2: `[[0, 2, 3], [2, 5, 3]]`. The output should be `[[0, 3], [5, 0]]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To solve this problem, we can first create a list of all events (start and end of each building) and then process them one by one to update the skyline.
- Step-by-step breakdown of the solution:
  1. Create a list of events, where each event is a tuple of `(x, type, height)`, where `type` is 0 for start and 1 for end.
  2. Sort the events by the x-coordinate.
  3. Initialize an empty list to store the key points of the skyline.
  4. Initialize a variable `curr_height` to 0, which represents the current height of the skyline.
  5. Process each event one by one. If the event is a start event, add the height of the building to the current height. If the event is an end event, subtract the height of the building from the current height.
  6. If the current height is different from the previous height, add a new key point to the skyline.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Event {
    int x, type, height;
};

bool compareEvents(const Event& a, const Event& b) {
    if (a.x == b.x) {
        return a.type < b.type;
    }
    return a.x < b.x;
}

vector<vector<int>> getSkyline(vector<vector<int>>& buildings) {
    vector<Event> events;
    for (const auto& building : buildings) {
        events.push_back({building[0], 0, building[2]});
        events.push_back({building[1], 1, building[2]});
    }
    sort(events.begin(), events.end(), compareEvents);
    vector<vector<int>> skyline;
    int curr_height = 0;
    for (const auto& event : events) {
        if (event.type == 0) {
            curr_height += event.height;
        } else {
            curr_height -= event.height;
        }
        if (skyline.empty() || curr_height != skyline.back()[1]) {
            skyline.push_back({event.x, curr_height});
        }
    }
    return skyline;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of buildings. This is because in the worst case, we have $2n$ events, and sorting them takes $O(n \log n)$ time. However, the inner loop that updates the current height and adds new key points to the skyline takes $O(n)$ time in the worst case, resulting in an overall time complexity of $O(n^2)$.
> - **Space Complexity:** $O(n)$, where $n$ is the number of buildings. This is because we need to store all the events in the `events` vector.
> - **Why these complexities occur:** The time complexity occurs because we are using a naive approach to update the current height and add new key points to the skyline. The space complexity occurs because we need to store all the events in the `events` vector.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a priority queue to keep track of the current height of the skyline. We can also use a `multiset` to store the heights of the buildings that are currently active.
- Detailed breakdown of the approach:
  1. Create a list of events, where each event is a tuple of `(x, type, height)`, where `type` is 0 for start and 1 for end.
  2. Sort the events by the x-coordinate.
  3. Initialize an empty list to store the key points of the skyline.
  4. Initialize a `multiset` to store the heights of the buildings that are currently active.
  5. Process each event one by one. If the event is a start event, add the height of the building to the `multiset`. If the event is an end event, remove the height of the building from the `multiset`.
  6. If the `multiset` is not empty, add a new key point to the skyline with the current x-coordinate and the maximum height in the `multiset`.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

struct Event {
    int x, type, height;
};

bool compareEvents(const Event& a, const Event& b) {
    if (a.x == b.x) {
        return a.type > b.type;
    }
    return a.x < b.x;
}

vector<vector<int>> getSkyline(vector<vector<int>>& buildings) {
    vector<Event> events;
    for (const auto& building : buildings) {
        events.push_back({building[0], 0, building[2]});
        events.push_back({building[1], 1, building[2]});
    }
    sort(events.begin(), events.end(), compareEvents);
    vector<vector<int>> skyline;
    multiset<int> heights;
    heights.insert(0);
    for (const auto& event : events) {
        if (event.type == 0) {
            heights.insert(event.height);
        } else {
            heights.erase(heights.find(event.height));
        }
        if (skyline.empty() || *heights.rbegin() != skyline.back()[1]) {
            skyline.push_back({event.x, *heights.rbegin()});
        }
    }
    return skyline;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of buildings. This is because we are using a `multiset` to store the heights of the buildings that are currently active, and inserting and removing elements from the `multiset` takes $O(\log n)$ time.
> - **Space Complexity:** $O(n)$, where $n$ is the number of buildings. This is because we need to store all the events in the `events` vector and all the heights in the `multiset`.
> - **Optimality proof:** This solution is optimal because we are using a `multiset` to keep track of the current height of the skyline, which allows us to efficiently update the current height and add new key points to the skyline.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a `multiset` to keep track of the current height of the skyline, and using a priority queue to efficiently update the current height and add new key points to the skyline.
- Problem-solving patterns identified: Using a `multiset` to store the heights of the buildings that are currently active, and using a priority queue to efficiently update the current height and add new key points to the skyline.
- Optimization techniques learned: Using a `multiset` to keep track of the current height of the skyline, and using a priority queue to efficiently update the current height and add new key points to the skyline.
- Similar problems to practice: Problems that involve using a `multiset` or a priority queue to efficiently update the current state and add new key points to the output.

**Mistakes to Avoid:**
- Common implementation errors: Not using a `multiset` or a priority queue to keep track of the current height of the skyline, and not efficiently updating the current height and adding new key points to the skyline.
- Edge cases to watch for: Not handling the case where the input is empty, and not handling the case where the input contains duplicate buildings.
- Performance pitfalls: Not using a `multiset` or a priority queue to keep track of the current height of the skyline, and not efficiently updating the current height and adding new key points to the skyline.
- Testing considerations: Testing the solution with different inputs, including empty input and input with duplicate buildings, and testing the solution with different edge cases, such as input with negative heights or input with heights that are not integers.