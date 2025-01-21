## Logger Rate Limiter

**Problem Link:** https://leetcode.com/problems/logger-rate-limiter/description

**Problem Statement:**
- Input format and constraints: The problem requires designing a logger system that can handle a stream of messages. Each message has a unique identifier and a timestamp. The system should prevent the same message from being printed more than once within a certain time window (in this case, 10 seconds).
- Expected output format: The system should return a boolean value indicating whether the message can be printed or not.
- Key requirements and edge cases to consider: 
    *   Messages with the same content should not be printed more than once within the time window.
    *   Messages with different content can be printed at any time.
    *   The system should handle a high volume of messages efficiently.
- Example test cases with explanations:
    *   If the system receives two identical messages within the time window, it should return `false` for the second message.
    *   If the system receives two different messages, it should return `true` for both messages.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The most straightforward way to solve this problem is to store all the messages in a data structure and check for duplicates before printing a message.
- Step-by-step breakdown of the solution:
    1.  Create a data structure (e.g., a vector or list) to store all the messages.
    2.  For each new message, iterate through the data structure to check if the message already exists within the time window.
    3.  If the message is found, return `false`. Otherwise, add the message to the data structure and return `true`.
- Why this approach comes to mind first: It is the most intuitive way to solve the problem, as it directly addresses the requirement of preventing duplicate messages within a certain time window.

```cpp
class Logger {
public:
    vector<pair<string, int>> messages;

    bool shouldPrintMessage(int timestamp, string message) {
        for (auto it = messages.begin(); it != messages.end();) {
            if (timestamp - it->second >= 10) {
                it = messages.erase(it);
            } else {
                ++it;
            }
        }

        for (const auto& msg : messages) {
            if (msg.first == message) {
                return false;
            }
        }

        messages.emplace_back(message, timestamp);
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of messages in the data structure. In the worst case, we need to iterate through all the messages to check for duplicates.
> - **Space Complexity:** $O(n)$, where $n$ is the number of messages in the data structure. We need to store all the messages in the data structure.
> - **Why these complexities occur:** These complexities occur because we are using a linear data structure (vector or list) to store the messages and iterating through it to check for duplicates. This results in a time complexity that is directly proportional to the number of messages.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of storing all the messages in a data structure, we can use an unordered map to store the last timestamp for each message. This allows us to check for duplicates in constant time.
- Detailed breakdown of the approach:
    1.  Create an unordered map to store the last timestamp for each message.
    2.  For each new message, check the unordered map to see if the message already exists and if the last timestamp is within the time window.
    3.  If the message is found and the last timestamp is within the time window, return `false`. Otherwise, update the last timestamp for the message in the unordered map and return `true`.
- Why further optimization is impossible: This approach has the best possible time complexity for this problem, as we are using an unordered map to store the messages, which allows for constant-time lookups.

```cpp
class Logger {
public:
    unordered_map<string, int> messageTimestamps;

    bool shouldPrintMessage(int timestamp, string message) {
        if (messageTimestamps.find(message) != messageTimestamps.end() && timestamp - messageTimestamps[message] < 10) {
            return false;
        }

        messageTimestamps[message] = timestamp;
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, where $1$ is the constant time it takes to perform a lookup in the unordered map. In the worst case, we need to perform a constant number of operations to check for duplicates and update the last timestamp.
> - **Space Complexity:** $O(n)$, where $n$ is the number of unique messages. We need to store the last timestamp for each unique message in the unordered map.
> - **Optimality proof:** This approach is optimal because it has the best possible time complexity for this problem. We are using an unordered map to store the messages, which allows for constant-time lookups, and we are only storing the necessary information (the last timestamp for each message). This results in a time complexity that is constant and does not depend on the number of messages.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the importance of choosing the right data structure for the problem at hand. In this case, using an unordered map allows for constant-time lookups and updates.
- Problem-solving patterns identified: The problem illustrates the pattern of using a data structure to store information and checking for duplicates before performing an action.
- Optimization techniques learned: The problem demonstrates the technique of using an unordered map to store information and perform constant-time lookups.
- Similar problems to practice: Other problems that involve checking for duplicates or performing constant-time lookups, such as the "Least Recently Used (LRU) Cache" problem.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for duplicates correctly or not updating the last timestamp correctly.
- Edge cases to watch for: Messages with the same content but different timestamps, or messages with different content but the same timestamp.
- Performance pitfalls: Using a data structure that has a high time complexity for lookups or updates, such as a linear data structure.
- Testing considerations: Testing the implementation with different scenarios, such as duplicate messages, messages with different content, and messages with different timestamps.