## Game Play Analysis III

**Problem Link:** https://leetcode.com/problems/game-play-analysis-iii/description

**Problem Statement:**
- Input format and constraints: We are given three tables: `Activity` (with columns `player_id`, `device_id`, `event_date`, `games_played`), `Friend` (with columns `player_id`, `friend_id`), and `Game` (not used in this problem). We need to find the number of friends for each player who logged in on a specific day, along with the number of friends who played on that day.
- Expected output format: A table with columns `player_id`, `event_date`, `num_friends`, `num_friends_played`.
- Key requirements and edge cases to consider: We need to handle cases where a player has no friends or no friends played on a specific day.
- Example test cases with explanations: For example, if we have two players, 1 and 2, who are friends, and both played on '2016-03-01', then the output for player 1 on '2016-03-01' should be (1, '2016-03-01', 1, 1).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can start by iterating over each row in the `Activity` table, finding all friends for each player, and then checking which of these friends played on the same day.
- Step-by-step breakdown of the solution:
  1. Iterate over each row in the `Activity` table.
  2. For each player, find all their friends by querying the `Friend` table.
  3. For each friend, check if they played on the same day by querying the `Activity` table again.
  4. Count the total number of friends and the number of friends who played.
- Why this approach comes to mind first: It's a straightforward, intuitive approach that directly addresses the problem statement.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>

struct Activity {
    int player_id;
    int device_id;
    std::string event_date;
    int games_played;
};

struct Friend {
    int player_id;
    int friend_id;
};

std::vector<std::tuple<int, std::string, int, int>> gamePlayAnalysisIII(std::vector<Activity>& activity, std::vector<Friend>& friend) {
    std::vector<std::tuple<int, std::string, int, int>> result;
    std::unordered_map<int, std::unordered_set<int>> friends;

    // Build friends map
    for (const auto& f : friend) {
        friends[f.player_id].insert(f.friend_id);
    }

    for (const auto& a : activity) {
        int numFriends = 0;
        int numFriendsPlayed = 0;
        for (const auto& f : friends[a.player_id]) {
            numFriends++;
            for (const auto& act : activity) {
                if (act.player_id == f && act.event_date == a.event_date) {
                    numFriendsPlayed++;
                    break;
                }
            }
        }
        result.emplace_back(a.player_id, a.event_date, numFriends, numFriendsPlayed);
    }

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot m)$, where $n$ is the number of rows in the `Activity` table and $m$ is the number of rows in the `Friend` table. This is because for each row in `Activity`, we potentially iterate over all rows in `Activity` again to find friends who played on the same day.
> - **Space Complexity:** $O(n + m)$, for storing the friends map and the result.
> - **Why these complexities occur:** The nested iteration over the `Activity` table for each friend of each player leads to the high time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use SQL to efficiently join the tables and count the friends and friends who played on the same day.
- Detailed breakdown of the approach:
  1. Use a SQL query to join the `Activity` and `Friend` tables based on the player ID.
  2. Use a subquery or join to count the number of friends who played on the same day.
- Proof of optimality: This approach is optimal because it leverages the efficiency of database queries to perform the necessary joins and counts, reducing the time complexity significantly compared to the brute force approach.
- Why further optimization is impossible: This approach directly addresses the problem statement in the most efficient way possible using SQL, making further optimization unlikely.

```sql
SELECT 
    a.player_id, 
    a.event_date, 
    COUNT(DISTINCT f.friend_id) AS num_friends,
    COUNT(DISTINCT CASE WHEN fa.event_date = a.event_date THEN f.friend_id END) AS num_friends_played
FROM 
    Activity a
LEFT JOIN 
    Friend f ON a.player_id = f.player_id
LEFT JOIN 
    Activity fa ON f.friend_id = fa.player_id
GROUP BY 
    a.player_id, 
    a.event_date
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the total number of rows in the `Activity` and `Friend` tables, due to the database operations (joins and sorting for grouping).
> - **Space Complexity:** $O(n)$, for storing the intermediate results of the join and the final grouped results.
> - **Optimality proof:** This is the most efficient approach because it utilizes database query optimizations and indexing, making it much faster than the brute force approach for large datasets.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Efficient use of database queries for joining and counting.
- Problem-solving patterns identified: Leveraging database capabilities for complex data analysis tasks.
- Optimization techniques learned: Using SQL queries to reduce computational complexity.
- Similar problems to practice: Other problems involving complex data analysis and database queries.

**Mistakes to Avoid:**
- Common implementation errors: Not optimizing database queries, leading to high time complexities.
- Edge cases to watch for: Handling cases where players have no friends or no friends played on a specific day.
- Performance pitfalls: Not utilizing database indexing and query optimizations.
- Testing considerations: Ensuring the query works correctly for various input scenarios and edge cases.