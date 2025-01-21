## Activity Participants
**Problem Link:** https://leetcode.com/problems/activity-participants/description

**Problem Statement:**
- Input format and constraints: The problem statement requires finding the names of all participants who participated in all activities. The input is a table `Activities` with columns `name` and `activity`. The constraints are that the activities are distinct for each participant.
- Expected output format: The output should be a list of names of participants who participated in all activities.
- Key requirements and edge cases to consider: The key requirement is to find participants who participated in all activities. An edge case is when there are no participants who participated in all activities.
- Example test cases with explanations: For example, if the input table is:

| name | activity |
|------|----------|
| John | A        |
| John | B        |
| John | C        |
| Jane | A        |
| Jane | B        |

The output should be `John` because John participated in all activities A, B, and C.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The initial thought process is to iterate over all participants and check if they participated in all activities.
- Step-by-step breakdown of the solution: 
  1. First, we need to find all unique activities.
  2. Then, we iterate over all participants and check if they participated in all activities.
  3. If a participant participated in all activities, we add their name to the result list.
- Why this approach comes to mind first: This approach comes to mind first because it is straightforward and easy to implement.

```cpp
#include <iostream>
#include <vector>
#include <unordered_set>
#include <unordered_map>

struct Activity {
    std::string name;
    std::string activity;
};

std::vector<std::string> activityParticipants(std::vector<Activity>& activities) {
    // Find all unique activities
    std::unordered_set<std::string> allActivities;
    for (const auto& activity : activities) {
        allActivities.insert(activity.activity);
    }

    // Initialize result list
    std::vector<std::string> result;

    // Iterate over all participants and check if they participated in all activities
    std::unordered_map<std::string, std::unordered_set<std::string>> participantActivities;
    for (const auto& activity : activities) {
        participantActivities[activity.name].insert(activity.activity);
    }

    for (const auto& participant : participantActivities) {
        if (participant.second.size() == allActivities.size()) {
            result.push_back(participant.first);
        }
    }

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of activities and $m$ is the number of participants. The reason for this complexity is that we iterate over all activities and participants once.
> - **Space Complexity:** $O(n + m)$, where $n$ is the number of activities and $m$ is the number of participants. The reason for this complexity is that we store all activities and participants in hash sets and maps.
> - **Why these complexities occur:** These complexities occur because we need to iterate over all activities and participants to find the participants who participated in all activities.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The key insight is to use a hash map to store the activities for each participant and a hash set to store all unique activities.
- Detailed breakdown of the approach: 
  1. First, we find all unique activities and store them in a hash set.
  2. Then, we iterate over all activities and store the activities for each participant in a hash map.
  3. Finally, we iterate over the hash map and check if the number of activities for each participant is equal to the number of unique activities. If it is, we add the participant to the result list.
- Proof of optimality: This approach is optimal because we only iterate over all activities and participants once, resulting in a time complexity of $O(n + m)$.

```cpp
#include <iostream>
#include <vector>
#include <unordered_set>
#include <unordered_map>

struct Activity {
    std::string name;
    std::string activity;
};

std::vector<std::string> activityParticipants(std::vector<Activity>& activities) {
    // Find all unique activities
    std::unordered_set<std::string> allActivities;
    for (const auto& activity : activities) {
        allActivities.insert(activity.activity);
    }

    // Initialize result list
    std::vector<std::string> result;

    // Iterate over all participants and check if they participated in all activities
    std::unordered_map<std::string, std::unordered_set<std::string>> participantActivities;
    for (const auto& activity : activities) {
        participantActivities[activity.name].insert(activity.activity);
    }

    for (const auto& participant : participantActivities) {
        if (participant.second.size() == allActivities.size()) {
            result.push_back(participant.first);
        }
    }

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of activities and $m$ is the number of participants. The reason for this complexity is that we iterate over all activities and participants once.
> - **Space Complexity:** $O(n + m)$, where $n$ is the number of activities and $m$ is the number of participants. The reason for this complexity is that we store all activities and participants in hash sets and maps.
> - **Optimality proof:** This approach is optimal because we only iterate over all activities and participants once, resulting in a time complexity of $O(n + m)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The key algorithmic concept demonstrated is the use of hash sets and maps to efficiently store and retrieve data.
- Problem-solving patterns identified: The problem-solving pattern identified is the use of a hash map to store the activities for each participant and a hash set to store all unique activities.
- Optimization techniques learned: The optimization technique learned is to use hash sets and maps to reduce the time complexity of the algorithm.
- Similar problems to practice: Similar problems to practice include finding the participants who participated in at least one activity, finding the activities that were participated in by at least one participant, and finding the participants who participated in all activities and the activities that were participated in by all participants.

**Mistakes to Avoid:**
- Common implementation errors: A common implementation error is to use a nested loop to iterate over all activities and participants, resulting in a time complexity of $O(n^2)$.
- Edge cases to watch for: An edge case to watch for is when there are no participants who participated in all activities.
- Performance pitfalls: A performance pitfall is to use a data structure that has a high time complexity for insertion and retrieval operations, such as a linked list.
- Testing considerations: A testing consideration is to test the algorithm with a large number of activities and participants to ensure that it scales well.