## Find Active Users

**Problem Link:** https://leetcode.com/problems/find-active-users/description

**Problem Statement:**
- Input format and constraints: The problem involves a table named `ActiveUsers` with two columns, `username` and `activity`. The goal is to find all active users, where an active user is defined as a user with at least 5 rows in the table.
- Expected output format: The output should be a list of usernames of active users.
- Key requirements and edge cases to consider: Ensure the count of rows per user is accurate and handle cases where a user has exactly 5 rows.
- Example test cases with explanations: For instance, if the table contains 4 rows for a user, that user should not be included in the result.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through each row in the table and count the occurrences of each username.
- Step-by-step breakdown of the solution:
  1. Initialize an empty dictionary to store the count of rows for each user.
  2. Iterate through each row in the table.
  3. For each row, increment the count for the corresponding username in the dictionary.
  4. After iterating through all rows, filter the dictionary to include only usernames with a count of at least 5.
- Why this approach comes to mind first: It directly addresses the requirement by counting the rows for each user and then filtering based on the count.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>

using namespace std;

struct UserActivity {
    string username;
    int activity;
};

vector<string> findActiveUsers(vector<UserActivity>& activities) {
    unordered_map<string, int> userCounts;
    
    // Count rows for each user
    for (const auto& activity : activities) {
        if (userCounts.find(activity.username) != userCounts.end()) {
            userCounts[activity.username]++;
        } else {
            userCounts[activity.username] = 1;
        }
    }
    
    // Filter users with at least 5 rows
    vector<string> activeUsers;
    for (const auto& pair : userCounts) {
        if (pair.second >= 5) {
            activeUsers.push_back(pair.first);
        }
    }
    
    return activeUsers;
}

int main() {
    vector<UserActivity> activities = {
        {"Alice", 1},
        {"Bob", 2},
        {"Alice", 3},
        {"Bob", 4},
        {"Alice", 5},
        {"Bob", 6},
        {"Alice", 7}
    };
    
    vector<string> activeUsers = findActiveUsers(activities);
    
    cout << "Active Users: ";
    for (const auto& user : activeUsers) {
        cout << user << " ";
    }
    cout << endl;
    
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of rows in the table, because we iterate through the table twice: once to count the rows for each user and once to filter the users.
> - **Space Complexity:** $O(n)$, because in the worst-case scenario (all users are unique), the size of the dictionary will be equal to the number of rows.
> - **Why these complexities occur:** The iteration through the table to count rows for each user and the subsequent filtering cause these complexities.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The problem can be solved using SQL, which is more efficient than manually iterating through rows in a programming language. The SQL query can directly count the rows for each user and filter the results.
- Detailed breakdown of the approach:
  1. Use a `GROUP BY` clause to group rows by the `username`.
  2. Apply a `HAVING` clause to filter groups with at least 5 rows.
- Proof of optimality: This approach is optimal because it leverages the database's capability to perform aggregation and filtering operations efficiently, reducing the need for manual iteration and thus improving performance.
- Why further optimization is impossible: The database operations are already optimized for performance, making further optimization unnecessary.

```sql
SELECT username
FROM ActiveUsers
GROUP BY username
HAVING COUNT(username) >= 5;
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of rows in the table, because the database still needs to scan the table to perform the aggregation and filtering.
> - **Space Complexity:** $O(n)$, because the database needs to store the intermediate results of the aggregation.
> - **Optimality proof:** The use of optimized database operations makes this approach the most efficient way to solve the problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Grouping and aggregation.
- Problem-solving patterns identified: Using database queries for efficient data processing.
- Optimization techniques learned: Leveraging database operations for performance improvement.
- Similar problems to practice: Problems involving data aggregation and filtering.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect use of `GROUP BY` and `HAVING` clauses.
- Edge cases to watch for: Handling users with exactly 5 rows.
- Performance pitfalls: Using inefficient algorithms or not leveraging database capabilities.
- Testing considerations: Ensure the query correctly filters users based on the row count.