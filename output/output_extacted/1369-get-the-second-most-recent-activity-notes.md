## Get the Second Most Recent Activity
**Problem Link:** https://leetcode.com/problems/get-the-second-most-recent-activity/description

**Problem Statement:**
- Input format and constraints: The input is a list of activities with their corresponding timestamps. Each activity is represented by a unique `username` and a `timestamp` in seconds since the epoch.
- Expected output format: The function should return the second most recent activity for each user. If a user has less than two activities, return `null`.
- Key requirements and edge cases to consider:
  - Handling users with less than two activities.
  - Sorting activities by timestamp in descending order.
  - Returning the second most recent activity for each user.
- Example test cases with explanations:
  - For a list of activities with the same user and different timestamps, the function should return the second most recent activity.
  - For a list of activities with different users and different timestamps, the function should return the second most recent activity for each user.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves iterating over the list of activities, sorting them by user and timestamp, and then selecting the second most recent activity for each user.
- Step-by-step breakdown of the solution:
  1. Create a hashmap to store the activities for each user.
  2. Iterate over the list of activities and add them to the hashmap.
  3. For each user, sort the activities by timestamp in descending order.
  4. Select the second most recent activity for each user.
- Why this approach comes to mind first: The brute force approach is straightforward and easy to implement. It involves iterating over the list of activities and sorting them, which are common operations in programming.

```cpp
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

struct Activity {
    string username;
    int timestamp;
};

vector<Activity> getSecondMostRecentActivity(vector<Activity>& activities) {
    map<string, vector<Activity>> userActivities;
    for (const auto& activity : activities) {
        userActivities[activity.username].push_back(activity);
    }

    vector<Activity> secondMostRecentActivities;
    for (auto& [user, activities] : userActivities) {
        if (activities.size() < 2) {
            secondMostRecentActivities.push_back({"", 0}); // or return null
        } else {
            sort(activities.begin(), activities.end(), [](const Activity& a, const Activity& b) {
                return a.timestamp > b.timestamp;
            });
            secondMostRecentActivities.push_back(activities[1]);
        }
    }
    return secondMostRecentActivities;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of activities for each user. This is because we are sorting the activities for each user.
> - **Space Complexity:** $O(n)$, where $n$ is the total number of activities. This is because we are storing the activities in a hashmap.
> - **Why these complexities occur:** The time complexity occurs because we are sorting the activities for each user, which takes $O(n \log n)$ time. The space complexity occurs because we are storing the activities in a hashmap, which takes $O(n)$ space.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution involves using a priority queue to store the activities for each user. This allows us to efficiently select the second most recent activity for each user.
- Detailed breakdown of the approach:
  1. Create a hashmap to store the activities for each user.
  2. For each user, create a priority queue to store the activities.
  3. Iterate over the list of activities and add them to the priority queue for each user.
  4. For each user, select the second most recent activity from the priority queue.
- Proof of optimality: The optimal solution has a time complexity of $O(n \log k)$, where $n$ is the total number of activities and $k$ is the number of activities for each user. This is because we are using a priority queue to select the second most recent activity for each user.

```cpp
#include <vector>
#include <map>
#include <queue>

using namespace std;

struct Activity {
    string username;
    int timestamp;
};

vector<Activity> getSecondMostRecentActivity(vector<Activity>& activities) {
    map<string, priority_queue<int>> userActivities;
    for (const auto& activity : activities) {
        userActivities[activity.username].push(activity.timestamp);
    }

    vector<Activity> secondMostRecentActivities;
    for (auto& [user, activities] : userActivities) {
        if (activities.size() < 2) {
            secondMostRecentActivities.push_back({"", 0}); // or return null
        } else {
            int mostRecent = activities.top();
            activities.pop();
            int secondMostRecent = activities.top();
            secondMostRecentActivities.push_back({user, secondMostRecent});
        }
    }
    return secondMostRecentActivities;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log k)$, where $n$ is the total number of activities and $k$ is the number of activities for each user. This is because we are using a priority queue to select the second most recent activity for each user.
> - **Space Complexity:** $O(n)$, where $n$ is the total number of activities. This is because we are storing the activities in a hashmap.
> - **Optimality proof:** The optimal solution has a time complexity of $O(n \log k)$, which is the best possible time complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a priority queue to select the second most recent activity for each user.
- Problem-solving patterns identified: Using a hashmap to store the activities for each user and a priority queue to select the second most recent activity.
- Optimization techniques learned: Using a priority queue to reduce the time complexity of the solution.
- Similar problems to practice: Problems that involve selecting the top k elements from a list or finding the second most recent activity.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if the user has less than two activities before selecting the second most recent activity.
- Edge cases to watch for: Handling users with less than two activities.
- Performance pitfalls: Not using a priority queue to select the second most recent activity, which can result in a higher time complexity.
- Testing considerations: Testing the solution with different inputs, including users with less than two activities and users with multiple activities.