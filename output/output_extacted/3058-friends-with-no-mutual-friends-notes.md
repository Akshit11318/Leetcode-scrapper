## Friends with No Mutual Friends
**Problem Link:** https://leetcode.com/problems/friends-with-no-mutual-friends/description

**Problem Statement:**
- Input: An integer `n` representing the number of people, and a 2D array `friends` where each subarray contains two integers representing a friendship between two people.
- Expected Output: A list of pairs of people who are friends but do not have any mutual friends.
- Key Requirements: 
  - Each person is represented by an integer from 0 to n-1.
  - There are no duplicate friendships (i.e., if [a, b] is a friendship, then [b, a] is not).
  - No person is friends with themselves.
- Edge Cases: 
  - If there are no friendships, return an empty list.
  - If two people are not friends but have no mutual friends, they should not be included in the output.
- Example Test Cases:
  - Input: `n = 2`, `friends = [[0,1]]`, Output: `[[0,1]]`
  - Input: `n =4`, `friends = [[0,1],[0,2],[1,2]]`, Output: `[]`

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to iterate over all possible pairs of people and check if they are friends and do not have any mutual friends.
- This involves checking for each pair if they are directly friends and then verifying if they share any common friends.
- This approach comes to mind first because it directly addresses the problem statement without requiring additional insights.

```cpp
vector<vector<int>> friendsWithNoMutualFriends(int n, vector<vector<int>>& friends) {
    vector<vector<int>> result;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            bool areFriends = false;
            bool haveMutualFriend = false;
            for (auto& friendship : friends) {
                if ((friendship[0] == i && friendship[1] == j) || (friendship[0] == j && friendship[1] == i)) {
                    areFriends = true;
                }
                for (auto& otherFriendship : friends) {
                    if ((otherFriendship[0] == i && otherFriendship[1] == friendship[0]) && 
                        (friendship[1] == j || friendship[1] == otherFriendship[1])) {
                        haveMutualFriend = true;
                    }
                }
            }
            if (areFriends && !haveMutualFriend) {
                result.push_back({i, j});
            }
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot m^2)$, where $n$ is the number of people and $m$ is the number of friendships. This is because for each pair of people, we are potentially checking all friendships twice (once for direct friendship and once for mutual friends).
> - **Space Complexity:** $O(1)$, excluding the space needed for the output. This is because we are using a constant amount of space to store our variables, regardless of the input size.
> - **Why these complexities occur:** These complexities occur because of the nested loops over people and friendships, leading to a quadratic time complexity in both the number of people and friendships.

---

### Optimal Approach (Required)

**Explanation:**
- A more efficient approach involves using a graph data structure to represent friendships. We can then iterate over all pairs of people and check if they are directly connected (friends) and if they have any common neighbors (mutual friends).
- This approach is optimal because it reduces the time complexity of checking for mutual friends from $O(m^2)$ to $O(m)$ by leveraging the graph structure.
- We can further optimize this by using an adjacency list representation of the graph, which allows for efficient lookup of neighbors.

```cpp
vector<vector<int>> friendsWithNoMutualFriends(int n, vector<vector<int>>& friends) {
    vector<unordered_set<int>> graph(n);
    for (auto& friendship : friends) {
        graph[friendship[0]].insert(friendship[1]);
        graph[friendship[1]].insert(friendship[0]);
    }
    
    vector<vector<int>> result;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (graph[i].find(j) != graph[i].end()) {
                bool haveMutualFriend = false;
                for (int neighbor : graph[i]) {
                    if (neighbor != j && graph[j].find(neighbor) != graph[j].end()) {
                        haveMutualFriend = true;
                        break;
                    }
                }
                if (!haveMutualFriend) {
                    result.push_back({i, j});
                }
            }
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot k)$, where $n$ is the number of people and $k$ is the average number of friends per person. This is because for each pair of people, we are checking their neighbors.
> - **Space Complexity:** $O(n \cdot k)$, for storing the graph. This is because in the worst case, every person could be friends with every other person.
> - **Optimality proof:** This is the best possible time complexity because we must at least check each pair of people once to determine if they are friends without mutual friends. The use of a graph reduces the time complexity of checking for mutual friends, making this approach optimal.

---

### Final Notes

**Learning Points:**
- Using a graph data structure can significantly improve the efficiency of problems involving relationships between entities.
- Adjacency list representation of graphs is particularly useful for problems requiring efficient neighbor lookup.
- Optimizing the data structure used can lead to substantial improvements in time complexity.

**Mistakes to Avoid:**
- Not considering the use of more efficient data structures.
- Failing to optimize the algorithm based on the problem's specific constraints (e.g., no duplicate friendships).
- Not testing the solution thoroughly with edge cases (e.g., no friendships, all people are friends with each other).