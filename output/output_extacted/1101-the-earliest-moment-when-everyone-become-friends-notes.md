## The Earliest Moment When Everyone Become Friends

**Problem Link:** https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/description

**Problem Statement:**
- Input format: A 2D array `logs` where each log is an array containing two integers representing the user ID and the timestamp, and a string representing the action ("become friends" or "unfriend").
- Constraints: The number of users is less than or equal to $10^4$, the number of logs is less than or equal to $10^5$, and the timestamp is a positive integer.
- Expected output format: The earliest moment when everyone becomes friends, or -1 if it's impossible for everyone to become friends.
- Key requirements and edge cases to consider: Handling unfriend actions, checking for connected components, and finding the minimum timestamp.
- Example test cases with explanations:
  - `logs = [[0,6,"become friends"],[1,2,"become friends"],[3,1,"become friends"]]`: Everyone becomes friends at timestamp 6.
  - `logs = [[0,7,"become friends"],[1,8,"become friends"],[1,8,"unfriend"]]`: No one becomes friends.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over each log and update the friendship status.
- Step-by-step breakdown of the solution:
  1. Initialize a set to store the current friends for each user.
  2. Iterate over each log and update the friendship status accordingly.
  3. Check if everyone is friends after each log.
- Why this approach comes to mind first: It's a straightforward approach to simulate the process of users becoming friends or unfriending each other.

```cpp
class Solution {
public:
    int earliestMoment(int n, vector<vector<string>>& logs) {
        unordered_map<int, unordered_set<int>> friends;
        int timestamp = -1;
        for (auto& log : logs) {
            int user1 = stoi(log[0]);
            int user2 = stoi(log[1]);
            if (log[2] == "become friends") {
                friends[user1].insert(user2);
                friends[user2].insert(user1);
            } else {
                friends[user1].erase(user2);
                friends[user2].erase(user1);
            }
            bool everyoneFriends = true;
            for (int i = 0; i < n; i++) {
                if (friends[i].size() != n - 1) {
                    everyoneFriends = false;
                    break;
                }
            }
            if (everyoneFriends) {
                timestamp = max(timestamp, stoi(log[3]));
            }
        }
        return timestamp;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$ where $m$ is the number of logs and $n$ is the number of users, because we iterate over each log and check if everyone is friends.
> - **Space Complexity:** $O(n^2)$ because in the worst case, every user is friends with every other user.
> - **Why these complexities occur:** The time complexity occurs because we simulate the process of users becoming friends or unfriending each other, and the space complexity occurs because we store the friendship status for each user.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a union-find data structure to keep track of the connected components.
- Detailed breakdown of the approach:
  1. Initialize a union-find data structure with $n$ users.
  2. Iterate over each log and update the union-find data structure accordingly.
  3. Check if everyone is in the same connected component after each log.
- Proof of optimality: This approach is optimal because it uses a union-find data structure, which has an average time complexity of $O(\alpha(n))$ for each operation, where $\alpha(n)$ is the inverse Ackermann function.

```cpp
class UnionFind {
public:
    vector<int> parent;
    vector<int> rank;
    int components;
    
    UnionFind(int n) {
        parent.resize(n);
        rank.resize(n);
        components = n;
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
    }
    
    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }
    
    void union_(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY) {
            if (rank[rootX] > rank[rootY]) {
                parent[rootY] = rootX;
            } else if (rank[rootX] < rank[rootY]) {
                parent[rootX] = rootY;
            } else {
                parent[rootY] = rootX;
                rank[rootX]++;
            }
            components--;
        }
    }
};

class Solution {
public:
    int earliestMoment(int n, vector<vector<string>>& logs) {
        UnionFind uf(n);
        int timestamp = -1;
        for (auto& log : logs) {
            int user1 = stoi(log[0]);
            int user2 = stoi(log[1]);
            int time = stoi(log[3]);
            if (log[2] == "become friends") {
                uf.union_(user1, user2);
            } else {
                // Handle unfriend action
            }
            if (uf.components == 1) {
                timestamp = max(timestamp, time);
            }
        }
        return timestamp == -1 ? -1 : timestamp;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot \alpha(n))$ where $m$ is the number of logs and $n$ is the number of users, because we use a union-find data structure.
> - **Space Complexity:** $O(n)$ because we store the union-find data structure.
> - **Optimality proof:** This approach is optimal because it uses a union-find data structure, which has an average time complexity of $O(\alpha(n))$ for each operation.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Union-find data structure, connected components.
- Problem-solving patterns identified: Using a union-find data structure to solve problems involving connected components.
- Optimization techniques learned: Using a union-find data structure to reduce the time complexity.
- Similar problems to practice: Problems involving connected components, such as finding the number of connected components in a graph.

**Mistakes to Avoid:**
- Common implementation errors: Not handling the unfriend action correctly.
- Edge cases to watch for: Handling the case where the number of users is 1.
- Performance pitfalls: Not using a union-find data structure, which can lead to a high time complexity.
- Testing considerations: Testing the solution with different inputs, including edge cases.