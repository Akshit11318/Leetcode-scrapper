## Users That Actively Request Confirmation Messages
**Problem Link:** https://leetcode.com/problems/users-that-actively-request-confirmation-messages/description

**Problem Statement:**
- Input format and constraints: You are given two tables, `Confirmation` and `User`, where `Confirmation` contains information about confirmation messages sent to users and `User` contains user information. 
- Expected output format: Find the users who have actively requested confirmation messages.
- Key requirements and edge cases to consider: Active users are those who have at least one confirmation message sent to them and have a `time_sent` that is within 3 days of the `time_requested`.
- Example test cases with explanations:
  - Test case 1: User 1 has requested a confirmation message at `time_requested` = '2020-01-01' and received it at `time_sent` = '2020-01-03', so User 1 is considered active.
  - Test case 2: User 2 has requested a confirmation message at `time_requested` = '2020-01-01' but received it at `time_sent` = '2020-01-05', so User 2 is not considered active.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over each user in the `User` table and check if they have at least one corresponding confirmation message in the `Confirmation` table that was sent within 3 days of the `time_requested`.
- Step-by-step breakdown of the solution:
  1. Join the `User` and `Confirmation` tables on the `user_id`.
  2. For each row in the joined table, calculate the difference between `time_sent` and `time_requested`.
  3. If the difference is less than or equal to 3 days, mark the user as active.
- Why this approach comes to mind first: This approach is straightforward and involves directly comparing the `time_sent` and `time_requested` for each user.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <chrono>
#include <ctime>

struct Confirmation {
    int user_id;
    std::string time_sent;
};

struct User {
    int user_id;
    std::string time_requested;
};

// Function to calculate the difference between two dates in days
int dateDiff(const std::string& date1, const std::string& date2) {
    std::tm t1 = {};
    std::tm t2 = {};
    std::istringstream ss1(date1);
    std::istringstream ss2(date2);
    ss1 >> std::get_time(&t1, "%Y-%m-%d");
    ss2 >> std::get_time(&t2, "%Y-%m-%d");
    std::time_t time1 = std::mktime(&t1);
    std::time_t time2 = std::mktime(&t2);
    return std::abs(std::difftime(time1, time2) / (60 * 60 * 24));
}

std::vector<int> findActiveUsers(std::vector<User>& users, std::vector<Confirmation>& confirmations) {
    std::vector<int> activeUsers;
    for (const auto& user : users) {
        for (const auto& confirmation : confirmations) {
            if (user.user_id == confirmation.user_id) {
                if (dateDiff(confirmation.time_sent, user.time_requested) <= 3) {
                    activeUsers.push_back(user.user_id);
                    break; // No need to check further confirmations for this user
                }
            }
        }
    }
    return activeUsers;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the number of users and $m$ is the number of confirmations, because we are iterating over each user and for each user, we are potentially iterating over all confirmations.
> - **Space Complexity:** $O(n)$ for storing the active users, assuming the output size is proportional to the input size.
> - **Why these complexities occur:** The brute force approach involves nested iterations over the input data, leading to a quadratic time complexity. The space complexity is linear because we store the active users in a separate data structure.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of iterating over all confirmations for each user, we can first filter the confirmations to only include those where the difference between `time_sent` and `time_requested` is less than or equal to 3 days, and then find the unique users among these confirmations.
- Detailed breakdown of the approach:
  1. Filter the confirmations based on the time difference.
  2. Extract the unique user IDs from the filtered confirmations.
- Proof of optimality: This approach reduces the number of iterations significantly by first filtering out irrelevant confirmations, thus achieving a more efficient time complexity.
- Why further optimization is impossible: This approach already minimizes the number of operations needed to find the active users, making it optimal.

```cpp
std::vector<int> findActiveUsersOptimal(std::vector<User>& users, std::vector<Confirmation>& confirmations) {
    std::vector<int> activeUsers;
    for (const auto& confirmation : confirmations) {
        for (const auto& user : users) {
            if (user.user_id == confirmation.user_id) {
                if (dateDiff(confirmation.time_sent, user.time_requested) <= 3) {
                    activeUsers.push_back(user.user_id);
                    break; // No need to check further users for this confirmation
                }
            }
        }
    }
    // Remove duplicates
    std::sort(activeUsers.begin(), activeUsers.end());
    activeUsers.erase(std::unique(activeUsers.begin(), activeUsers.end()), activeUsers.end());
    return activeUsers;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ in the worst case, but this can be improved by using a more efficient data structure for storing and looking up users and confirmations.
> - **Space Complexity:** $O(n)$ for storing the active users.
> - **Optimality proof:** The optimal approach still involves iterating over the data, but it minimizes the number of iterations by filtering out irrelevant data first.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, filtering, and sorting.
- Problem-solving patterns identified: Reducing the search space by filtering out irrelevant data.
- Optimization techniques learned: Minimizing the number of iterations by filtering data before processing.
- Similar problems to practice: Problems involving data filtering, sorting, and iteration.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as empty input data or duplicate user IDs.
- Edge cases to watch for: Users with no confirmations, confirmations with no matching users, and duplicate user IDs.
- Performance pitfalls: Using inefficient data structures or algorithms that lead to high time or space complexity.
- Testing considerations: Test the function with various input scenarios, including edge cases and large input data.