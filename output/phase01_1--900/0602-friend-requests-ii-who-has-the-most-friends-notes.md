## Friend Requests II: Who Has the Most Friends
**Problem Link:** https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/description

**Problem Statement:**
- Input format: The input will be a list of friend requests where each request is a tuple of two integers representing the IDs of the two people who want to be friends.
- Constraints: Each person has a unique ID.
- Expected output format: The IDs of the people who have the most friends.
- Key requirements and edge cases to consider: 
  - If there are multiple people with the most friends, return all of them.
  - If there are no friend requests, return an empty list.
- Example test cases with explanations:
  - For example, given the friend requests `[(1, 2), (1, 3), (2, 3)]`, the output should be `[1, 2, 3]` because each person has 2 friends.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Create an adjacency list representation of the graph where each person is a node and their friends are their neighbors.
- Step-by-step breakdown of the solution:
  1. Initialize an empty graph.
  2. Iterate over each friend request and add an edge between the two people in the graph.
  3. Iterate over each person in the graph and count the number of their friends.
  4. Keep track of the maximum number of friends and the people who have that many friends.
- Why this approach comes to mind first: It is a straightforward way to represent the relationships between people and count the number of friends each person has.

```cpp
vector<int> mostFriends(vector<vector<int>>& requests) {
    unordered_map<int, unordered_set<int>> graph;
    for (auto& request : requests) {
        int person1 = request[0];
        int person2 = request[1];
        graph[person1].insert(person2);
        graph[person2].insert(person1);
    }
    int maxFriends = 0;
    vector<int> mostFriends;
    for (auto& person : graph) {
        if (person.second.size() > maxFriends) {
            maxFriends = person.second.size();
            mostFriends = {person.first};
        } else if (person.second.size() == maxFriends) {
            mostFriends.push_back(person.first);
        }
    }
    return mostFriends;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of people and $m$ is the number of friend requests. This is because we iterate over each friend request once to build the graph, and then over each person once to count their friends.
> - **Space Complexity:** $O(n + m)$, where $n$ is the number of people and $m$ is the number of friend requests. This is because we store each person and their friends in the graph.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each friend request and each person. The space complexity is also linear because we store each person and their friends in the graph.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a hash map to store the count of friends for each person. This allows us to update the count in constant time when we add a new friend request.
- Detailed breakdown of the approach:
  1. Initialize a hash map to store the count of friends for each person.
  2. Iterate over each friend request and increment the count of friends for both people.
  3. Keep track of the maximum count of friends and the people who have that many friends.
- Proof of optimality: This solution has the same time complexity as the brute force approach, but it uses less space because we only store the count of friends for each person, rather than their actual friends.

```cpp
vector<int> mostFriends(vector<vector<int>>& requests) {
    unordered_map<int, int> friendCount;
    for (auto& request : requests) {
        int person1 = request[0];
        int person2 = request[1];
        friendCount[person1]++;
        friendCount[person2]++;
    }
    int maxFriends = 0;
    vector<int> mostFriends;
    for (auto& person : friendCount) {
        if (person.second > maxFriends) {
            maxFriends = person.second;
            mostFriends = {person.first};
        } else if (person.second == maxFriends) {
            mostFriends.push_back(person.first);
        }
    }
    return mostFriends;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of people and $m$ is the number of friend requests. This is because we iterate over each friend request once to update the friend count, and then over each person once to find the maximum friend count.
> - **Space Complexity:** $O(n)$, where $n$ is the number of people. This is because we store the friend count for each person in the hash map.
> - **Optimality proof:** This solution is optimal because it has the same time complexity as the brute force approach, but it uses less space. We cannot do better than linear time complexity because we must at least read the input, and we cannot do better than linear space complexity because we must store the friend count for each person.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Hash maps, graph traversal, and counting.
- Problem-solving patterns identified: Using a hash map to store counts and updating them in constant time.
- Optimization techniques learned: Reducing space complexity by only storing the necessary information.
- Similar problems to practice: Other graph problems, such as finding the shortest path or the minimum spanning tree.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to initialize the hash map or not updating the friend count correctly.
- Edge cases to watch for: Handling the case where there are no friend requests or where there are multiple people with the most friends.
- Performance pitfalls: Using a data structure that has poor time or space complexity, such as a linked list or a tree.
- Testing considerations: Testing the solution with different inputs, such as an empty list of friend requests or a list with duplicate requests.