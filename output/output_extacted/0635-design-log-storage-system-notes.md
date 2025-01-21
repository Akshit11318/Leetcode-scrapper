## Design Log Storage System
**Problem Link:** https://leetcode.com/problems/design-log-storage-system/description

**Problem Statement:**
- Input format and constraints: The system will receive `put`, `get`, and `retrieve` operations. `put` stores a `log_id` and `timestamp`, `get` retrieves a `log_id` by `id`, and `retrieve` retrieves logs by `start` and `end` timestamps and `start_val` and `end_val` values.
- Expected output format: For `put`, there's no return value; for `get`, return the `log_id`; for `retrieve`, return a list of `log_id`s within the specified range.
- Key requirements and edge cases to consider: Handling duplicate `log_id`s, validating input timestamps and values, and optimizing the `retrieve` operation.
- Example test cases with explanations:
  - `put(1, 5, "hello world")`: Store a log with `id=1`, `timestamp=5`, and `value="hello world"`.
  - `get(1)`: Retrieve the `id` associated with `id=1`.
  - `retrieve(5, 10, "hello", "world")`: Retrieve `id`s of logs with timestamps between 5 and 10 and values between "hello" and "world".

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Store logs in a simple data structure like a list or map, where each log is associated with its `id`, `timestamp`, and `value`.
- Step-by-step breakdown of the solution:
  1. For `put`, iterate through the list to check for existing `log_id`s and update or append accordingly.
  2. For `get`, iterate through the list to find the `log_id` by `id`.
  3. For `retrieve`, iterate through the list, checking each log's `timestamp` and `value` against the specified ranges.
- Why this approach comes to mind first: It's the simplest way to implement the required operations without considering efficiency.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class LogSystem {
public:
    unordered_map<int, pair<int, string>> logs;

    void put(int id, int timestamp, string value) {
        logs[id] = {timestamp, value};
    }

    int get(int id) {
        if (logs.find(id) != logs.end()) {
            return id;
        }
        return -1; // Assuming -1 for not found
    }

    vector<int> retrieve(int start, int end, string start_val, string end_val) {
        vector<int> result;
        for (auto& log : logs) {
            if (log.second.first >= start && log.second.first <= end && 
                log.second.second >= start_val && log.second.second <= end_val) {
                result.push_back(log.first);
            }
        }
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ for `put`, `get`, and `retrieve` operations, where $n$ is the number of logs, because in the worst case, we might need to iterate through all logs for each operation.
> - **Space Complexity:** $O(n)$, as we store each log in the `logs` map.
> - **Why these complexities occur:** The brute force approach involves linear scans for most operations, leading to $O(n)$ time complexity. Space complexity is also $O(n)$ because we store all logs.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Utilize a combination of data structures to optimize each operation. For `retrieve`, a more efficient data structure like a `set` or a balanced binary search tree can be used to store logs based on their timestamps and values.
- Detailed breakdown of the approach:
  1. For `put`, use a `map` to store `log_id` and its corresponding `timestamp` and `value` for efficient lookup and update.
  2. For `get`, the `map` allows for $O(1)$ lookup by `id`.
  3. For `retrieve`, use a data structure that allows for range queries, such as a balanced BST (like `set` in C++) or an interval tree, to efficiently find logs within the specified `timestamp` and `value` ranges.
- Proof of optimality: The use of a `map` for `put` and `get` operations achieves $O(1)$ time complexity, which is optimal for these operations. For `retrieve`, using a data structure optimized for range queries achieves the best possible time complexity for this operation.

```cpp
#include <iostream>
#include <vector>
#include <map>
#include <set>

using namespace std;

class LogSystem {
public:
    map<int, pair<int, string>> logs;
    set<tuple<int, string, int>> retrieveSet; // For efficient retrieval

    void put(int id, int timestamp, string value) {
        logs[id] = {timestamp, value};
        retrieveSet.emplace(timestamp, value, id);
    }

    int get(int id) {
        if (logs.find(id) != logs.end()) {
            return id;
        }
        return -1;
    }

    vector<int> retrieve(int start, int end, string start_val, string end_val) {
        vector<int> result;
        for (auto it = retrieveSet.lower_bound({start, start_val, -1}); 
             it != retrieveSet.end() && get<0>(*it) <= end && get<1>(*it) <= end_val; ++it) {
            if (get<0>(*it) >= start && get<1>(*it) >= start_val) {
                result.push_back(get<2>(*it));
            }
        }
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for `put` and `get`, $O(k)$ for `retrieve` where $k$ is the number of logs in the range, because we use efficient data structures for each operation.
> - **Space Complexity:** $O(n)$, as we store each log in both the `logs` map and the `retrieveSet`.
> - **Optimality proof:** This approach optimizes each operation by using the most suitable data structures, achieving the best possible time complexity for the given problem constraints.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Efficient use of data structures for specific operations, optimization of range queries.
- Problem-solving patterns identified: Breaking down problems into smaller, manageable parts and choosing the right data structure for each part.
- Optimization techniques learned: Using balanced BSTs or interval trees for range queries, leveraging `map` for fast lookup and update.
- Similar problems to practice: Other problems involving range queries, efficient data structure usage, and optimization techniques.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect usage of data structures, failure to handle edge cases.
- Edge cases to watch for: Duplicate `log_id`s, invalid input timestamps and values.
- Performance pitfalls: Using inefficient data structures or algorithms for operations, leading to high time or space complexity.
- Testing considerations: Thoroughly testing with various inputs, including edge cases, to ensure correctness and performance.