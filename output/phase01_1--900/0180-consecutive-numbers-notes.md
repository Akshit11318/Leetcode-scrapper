## Consecutive Numbers
**Problem Link:** https://leetcode.com/problems/consecutive-numbers/description

**Problem Statement:**
- Input format and constraints: The problem involves a `logs` table with columns `id`, `num`, and `type`, where `type` can be either `start` or `end`. The goal is to find all `num` values that are consecutive.
- Expected output format: The output should be a list of distinct `num` values that have a `start` type but no corresponding `end` type, indicating a sequence that was started but not ended.
- Key requirements and edge cases to consider: Handling cases where a number is started and ended multiple times, ensuring that only numbers with a `start` type and no corresponding `end` type are counted.
- Example test cases with explanations:
  - If a number is started but not ended, it should be included in the result.
  - If a number is both started and ended, it should not be included in the result.
  - If a number is started multiple times but ended less than it was started, it should be included in the result.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Iterate over each log entry, tracking the count of `start` and `end` types for each number. Then, identify numbers with more `start` than `end` types.
- Step-by-step breakdown of the solution:
  1. Create a map to store the count of `start` and `end` types for each number.
  2. Iterate over each log entry, updating the count in the map based on the `type`.
  3. After iterating over all logs, filter the map to find numbers with more `start` counts than `end` counts.

```cpp
#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

struct Log {
    int id;
    int num;
    string type;
};

vector<int> findConsecutiveNumbers(vector<Log>& logs) {
    unordered_map<int, int> numCount;
    
    // Count start and end types for each number
    for (auto& log : logs) {
        if (log.type == "start") {
            numCount[log.num]++;
        } else if (log.type == "end") {
            numCount[log.num]--;
        }
    }
    
    // Find numbers with more start than end types
    vector<int> result;
    for (auto& pair : numCount) {
        if (pair.second > 0) {
            result.push_back(pair.first);
        }
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of log entries, because we iterate over each log entry once.
> - **Space Complexity:** $O(n)$, because in the worst case, we might store every log entry in the map.
> - **Why these complexities occur:** The iteration over log entries causes the linear time complexity, and storing counts in the map leads to the space complexity.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: The same as the brute force, but with an emphasis on efficient data structure usage and minimizing iterations.
- Detailed breakdown of the approach:
  1. Utilize an unordered map for efficient lookups and updates of counts.
  2. Ensure the map is properly cleared or reused if the function is called multiple times to avoid memory leaks.
- Proof of optimality: This approach is optimal because it only requires a single pass through the data and uses a data structure that allows for constant time lookups and updates.

```cpp
#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

struct Log {
    int id;
    int num;
    string type;
};

vector<int> findConsecutiveNumbers(vector<Log>& logs) {
    unordered_map<int, int> numCount;
    
    // Count start and end types for each number efficiently
    for (auto& log : logs) {
        numCount[log.num] += (log.type == "start") ? 1 : -1;
    }
    
    // Find numbers with more start than end types efficiently
    vector<int> result;
    for (auto& pair : numCount) {
        if (pair.second > 0) {
            result.push_back(pair.first);
        }
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of log entries, due to the single pass through the data.
> - **Space Complexity:** $O(n)$, because we store counts for each unique number in the map.
> - **Optimality proof:** This is the best possible time complexity because we must at least read the input once. The space complexity is also optimal because we need to store the counts for each number.

---

### Final Notes
**Learning Points:**
- Key algorithmic concepts demonstrated: Efficient use of data structures like unordered maps for fast lookups and updates.
- Problem-solving patterns identified: Iterating over data once to minimize time complexity, using maps to track counts.
- Optimization techniques learned: Minimizing iterations and using efficient data structures.
- Similar problems to practice: Other problems involving counting and tracking elements in a list or array.

**Mistakes to Avoid:**
- Common implementation errors: Failing to initialize variables, not checking for edge cases like empty input.
- Edge cases to watch for: Handling cases where a number is started or ended multiple times, ensuring correct counts.
- Performance pitfalls: Using inefficient data structures or algorithms that lead to higher than necessary time or space complexity.
- Testing considerations: Thoroughly testing the function with various inputs, including edge cases, to ensure correctness.