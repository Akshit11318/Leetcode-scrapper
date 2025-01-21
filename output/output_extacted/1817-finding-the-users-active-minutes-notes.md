## Finding the Users Active Minutes

**Problem Link:** https://leetcode.com/problems/finding-the-users-active-minutes/description

**Problem Statement:**
- Input: A list of integers `logs` where each integer is a user ID and a minute.
- Constraints: $1 \leq \text{number of users} \leq 10^5$, $1 \leq \text{number of logs} \leq 10^6$, $1 \leq \text{user ID} \leq 10^9$, $1 \leq \text{minute} \leq 60$.
- Expected Output: A list of integers representing the number of users with 1, 2, ..., 60 active minutes.
- Key Requirements:
  - Count the number of unique minutes each user is active.
  - Return the count of users with each possible number of active minutes.
- Edge Cases:
  - Empty input list.
  - Users with no active minutes.

**Example Test Cases:**
- `logs = [[0,5],[1,2],[0,2],[0,5],[1,3]]`: User 0 is active in minutes 2 and 5, and user 1 is active in minutes 2 and 3. The output should be `[0,2,0,0,1,0,0,0,...]`.
- `logs = [[1,1],[2,2],[2,3]]`: User 1 is active in minute 1, and user 2 is active in minutes 2 and 3. The output should be `[1,1,0,0,0,...]`.

---

### Brute Force Approach

**Explanation:**
- The initial thought is to iterate over each log, keep track of the minutes each user is active, and then count the number of users with each possible number of active minutes.
- This approach involves using a map to store the active minutes for each user and then iterating over the map to count the users with each possible number of active minutes.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>

std::vector<int> findingUsersActiveMinutes(std::vector<std::vector<int>>& logs) {
    // Map to store the active minutes for each user
    std::unordered_map<int, std::unordered_set<int>> userMinutes;
    
    // Iterate over each log
    for (const auto& log : logs) {
        int userId = log[0];
        int minute = log[1];
        
        // Add the minute to the user's set of active minutes
        userMinutes[userId].insert(minute);
    }
    
    // Vector to store the count of users with each possible number of active minutes
    std::vector<int> result(60);
    
    // Iterate over each user's active minutes
    for (const auto& user : userMinutes) {
        // Get the number of active minutes for the user
        int activeMinutes = user.second.size();
        
        // Increment the count of users with this number of active minutes
        if (activeMinutes <= 60) {
            result[activeMinutes - 1]++;
        }
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of logs and $m$ is the number of unique users. This is because we iterate over each log once and then iterate over each user's active minutes.
> - **Space Complexity:** $O(n + m)$, where $n$ is the number of logs and $m$ is the number of unique users. This is because we store the active minutes for each user in a map.
> - **Why these complexities occur:** The time complexity occurs because we need to iterate over each log and each user's active minutes. The space complexity occurs because we need to store the active minutes for each user.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal approach is the same as the brute force approach, as we need to iterate over each log and each user's active minutes to count the number of users with each possible number of active minutes.
- However, we can use a more efficient data structure, such as a `std::unordered_set`, to store the active minutes for each user.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>

std::vector<int> findingUsersActiveMinutes(std::vector<std::vector<int>>& logs) {
    // Map to store the active minutes for each user
    std::unordered_map<int, std::unordered_set<int>> userMinutes;
    
    // Iterate over each log
    for (const auto& log : logs) {
        int userId = log[0];
        int minute = log[1];
        
        // Add the minute to the user's set of active minutes
        userMinutes[userId].insert(minute);
    }
    
    // Vector to store the count of users with each possible number of active minutes
    std::vector<int> result(60);
    
    // Iterate over each user's active minutes
    for (const auto& user : userMinutes) {
        // Get the number of active minutes for the user
        int activeMinutes = user.second.size();
        
        // Increment the count of users with this number of active minutes
        if (activeMinutes <= 60) {
            result[activeMinutes - 1]++;
        }
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of logs and $m$ is the number of unique users. This is because we iterate over each log once and then iterate over each user's active minutes.
> - **Space Complexity:** $O(n + m)$, where $n$ is the number of logs and $m$ is the number of unique users. This is because we store the active minutes for each user in a map.
> - **Optimality proof:** This approach is optimal because we need to iterate over each log and each user's active minutes to count the number of users with each possible number of active minutes.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: iteration, mapping, and counting.
- Problem-solving patterns identified: using a map to store the active minutes for each user and then iterating over the map to count the users with each possible number of active minutes.
- Optimization techniques learned: using a more efficient data structure, such as a `std::unordered_set`, to store the active minutes for each user.

**Mistakes to Avoid:**
- Common implementation errors: not checking if the user ID is valid, not checking if the minute is within the valid range.
- Edge cases to watch for: empty input list, users with no active minutes.
- Performance pitfalls: using a less efficient data structure, such as a `std::vector`, to store the active minutes for each user.
- Testing considerations: testing with different input sizes, testing with different user IDs and minutes.