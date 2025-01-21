## User Activities Within Time Bounds

**Problem Link:** https://leetcode.com/problems/user-activities-within-time-bounds/description

**Problem Statement:**
- Input format and constraints: The problem takes in a 2D array `logs` where each log is an array of two integers, representing the `userId` and `timestamp` of an activity. The problem also takes in two integers `startTime` and `endTime`, representing the time bounds.
- Expected output format: The function should return a list of user IDs that have performed at least one activity within the time bounds.
- Key requirements and edge cases to consider:
  - The time bounds are inclusive.
  - The input array `logs` is not sorted.
  - The function should return a list of unique user IDs.
- Example test cases with explanations:
  - `logs = [[0,5],[1,2],[0,2],[0,5],[1,6]], startTime = 3, endTime = 4` should return `[0]` because user 0 has an activity with timestamp 5, which is within the time bounds.
  - `logs = [[1,1],[2,2],[3,3]], startTime = 2, endTime = 3` should return `[2,3]` because users 2 and 3 have activities within the time bounds.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves iterating over each log in the `logs` array and checking if the timestamp is within the time bounds.
- Step-by-step breakdown of the solution:
  1. Initialize an empty set to store unique user IDs that have performed at least one activity within the time bounds.
  2. Iterate over each log in the `logs` array.
  3. For each log, check if the timestamp is within the time bounds.
  4. If the timestamp is within the time bounds, add the user ID to the set.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it has a time complexity of O(n), where n is the number of logs.

```cpp
#include <vector>
#include <unordered_set>

vector<int> findingUsersActiveMinutes(vector<vector<int>>& logs, int startTime, int endTime) {
    unordered_set<int> userIds;
    for (auto& log : logs) {
        if (log[1] >= startTime && log[1] <= endTime) {
            userIds.insert(log[0]);
        }
    }
    vector<int> result(userIds.begin(), userIds.end());
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** O(n), where n is the number of logs. This is because we iterate over each log in the `logs` array once.
> - **Space Complexity:** O(n), where n is the number of unique user IDs. This is because we store unique user IDs in a set.
> - **Why these complexities occur:** These complexities occur because we use a set to store unique user IDs, and we iterate over each log in the `logs` array.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a hash map to store the user IDs and their corresponding timestamps, and then iterate over the hash map to find user IDs that have performed at least one activity within the time bounds.
- Detailed breakdown of the approach:
  1. Initialize a hash map to store user IDs and their corresponding timestamps.
  2. Iterate over each log in the `logs` array and update the hash map.
  3. Initialize an empty set to store unique user IDs that have performed at least one activity within the time bounds.
  4. Iterate over the hash map and check if each user ID has performed at least one activity within the time bounds.
  5. If a user ID has performed at least one activity within the time bounds, add it to the set.
- Proof of optimality: This approach is optimal because it has a time complexity of O(n), where n is the number of logs, and it uses a hash map to store user IDs and their corresponding timestamps, which allows for efficient lookup and update.

```cpp
#include <vector>
#include <unordered_set>
#include <unordered_map>

vector<int> findingUsersActiveMinutes(vector<vector<int>>& logs, int startTime, int endTime) {
    unordered_map<int, unordered_set<int>> userTimestamps;
    for (auto& log : logs) {
        userTimestamps[log[0]].insert(log[1]);
    }
    unordered_set<int> userIds;
    for (auto& user : userTimestamps) {
        for (auto& timestamp : user.second) {
            if (timestamp >= startTime && timestamp <= endTime) {
                userIds.insert(user.first);
                break;
            }
        }
    }
    vector<int> result(userIds.begin(), userIds.end());
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** O(n), where n is the number of logs. This is because we iterate over each log in the `logs` array once.
> - **Space Complexity:** O(n), where n is the number of unique user IDs. This is because we store unique user IDs in a hash map and a set.
> - **Optimality proof:** This approach is optimal because it has a time complexity of O(n), where n is the number of logs, and it uses a hash map to store user IDs and their corresponding timestamps, which allows for efficient lookup and update.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Hash maps, sets, and iteration over arrays.
- Problem-solving patterns identified: Using a hash map to store user IDs and their corresponding timestamps, and iterating over the hash map to find user IDs that have performed at least one activity within the time bounds.
- Optimization techniques learned: Using a hash map to store user IDs and their corresponding timestamps, and iterating over the hash map to find user IDs that have performed at least one activity within the time bounds.
- Similar problems to practice: Problems that involve iterating over arrays and using hash maps to store data.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if a user ID has already been added to the set before adding it again.
- Edge cases to watch for: Not checking if the input array is empty or if the time bounds are invalid.
- Performance pitfalls: Not using a hash map to store user IDs and their corresponding timestamps, which can lead to a time complexity of O(n^2).
- Testing considerations: Testing the function with different input arrays and time bounds to ensure that it returns the correct result.