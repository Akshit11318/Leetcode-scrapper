## Leetcodify Friends Recommendations

**Problem Link:** https://leetcode.com/problems/leetcodify-friends-recommendations/description

**Problem Statement:**
- Input format: `int n`, `vector<vector<int>>& friendships`, `int k`
- Constraints: `2 <= n <= 10^5`, `0 <= friendships.length <= 10^5`, `1 <= k <= n`
- Expected output format: `vector<int>` representing the IDs of the top `k` recommended friends for the user with ID `1`
- Key requirements: Recommend friends based on the number of common friends with the user with ID `1`
- Example test cases:
  - `n = 4`, `friendships = [[1, 2], [1, 3], [2, 3]]`, `k = 2`
  - `n = 6`, `friendships = [[1, 2], [1, 3], [3, 4], [2, 4], [4, 5]]`, `k = 1`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Calculate the number of common friends between the user with ID `1` and each other user.
- Step-by-step breakdown:
  1. Create an adjacency list to represent the friendships.
  2. For each user, calculate the number of common friends with the user with ID `1`.
  3. Sort the users based on the number of common friends and return the top `k` users.

```cpp
vector<int> recommendFriends(int n, vector<vector<int>>& friendships, int k) {
    vector<vector<int>> graph(n + 1);
    for (auto& friendship : friendships) {
        graph[friendship[0]].push_back(friendship[1]);
        graph[friendship[1]].push_back(friendship[0]);
    }

    vector<int> commonFriends(n + 1, 0);
    for (int i = 2; i <= n; i++) {
        for (int friend1 : graph[1]) {
            for (int friend2 : graph[i]) {
                if (friend1 == friend2) {
                    commonFriends[i]++;
                }
            }
        }
    }

    vector<pair<int, int>> sortedUsers;
    for (int i = 2; i <= n; i++) {
        sortedUsers.push_back({commonFriends[i], i});
    }
    sort(sortedUsers.begin(), sortedUsers.end(), greater<pair<int, int>>());

    vector<int> result;
    for (int i = 0; i < k; i++) {
        result.push_back(sortedUsers[i].second);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot m)$, where $n$ is the number of users and $m$ is the number of friendships, because we are iterating over all friendships for each user.
> - **Space Complexity:** $O(n + m)$, because we are storing the adjacency list and the common friends for each user.
> - **Why these complexities occur:** The brute force approach has high time complexity due to the nested loops over all friendships for each user.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Use a `set` to efficiently calculate the common friends between the user with ID `1` and each other user.
- Detailed breakdown:
  1. Create an adjacency list to represent the friendships.
  2. Use a `set` to store the friends of the user with ID `1`.
  3. For each user, calculate the number of common friends with the user with ID `1` using the `set`.
  4. Sort the users based on the number of common friends and return the top `k` users.

```cpp
vector<int> recommendFriends(int n, vector<vector<int>>& friendships, int k) {
    vector<set<int>> graph(n + 1);
    for (auto& friendship : friendships) {
        graph[friendship[0]].insert(friendship[1]);
        graph[friendship[1]].insert(friendship[0]);
    }

    vector<pair<int, int>> commonFriends(n + 1, {0, 0});
    set<int> user1Friends = graph[1];
    for (int i = 2; i <= n; i++) {
        set<int> intersection;
        for (int friend1 : graph[i]) {
            if (user1Friends.find(friend1) != user1Friends.end()) {
                intersection.insert(friend1);
            }
        }
        commonFriends[i] = {intersection.size(), i};
    }

    sort(commonFriends.begin() + 1, commonFriends.end(), greater<pair<int, int>>());

    vector<int> result;
    for (int i = 1; i <= n && result.size() < k; i++) {
        if (commonFriends[i].first > 0) {
            result.push_back(commonFriends[i].second);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of users and $m$ is the average number of friendships per user, because we are iterating over all friendships for each user.
> - **Space Complexity:** $O(n \cdot m)$, because we are storing the adjacency list and the common friends for each user.
> - **Optimality proof:** This approach is optimal because we are using a `set` to efficiently calculate the common friends between the user with ID `1` and each other user.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: Using `set` to efficiently calculate common friends.
- Problem-solving patterns: Iterating over all friendships for each user to calculate common friends.
- Optimization techniques: Using a `set` to reduce the time complexity of calculating common friends.
- Similar problems to practice: Problems involving graph traversal and set operations.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as an empty input.
- Edge cases to watch for: Users with no friends, users with no common friends with the user with ID `1`.
- Performance pitfalls: Using a brute force approach with high time complexity.
- Testing considerations: Testing with different inputs, including edge cases, to ensure correctness and performance.