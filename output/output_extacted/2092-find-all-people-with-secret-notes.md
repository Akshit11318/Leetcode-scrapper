## Find All People With Secret
**Problem Link:** https://leetcode.com/problems/find-all-people-with-secret/description

**Problem Statement:**
- Input format and constraints: The problem takes in a `2D` array `meetings` where each subarray contains three integers representing a meeting between two people and the time of the meeting, and a string `secret` which is the secret being shared. The goal is to find all people who know the secret after all meetings have taken place.
- Expected output format: A list of integers representing the IDs of people who know the secret.
- Key requirements and edge cases to consider: Handling cases where a person meets multiple people who know the secret, ensuring that the secret is only shared among people who meet after the secret is shared.
- Example test cases with explanations: For example, given `meetings = [[1,2,5],[2,3,8],[1,5,10]]` and `secret = "hello"`, the function should return `[1,2,5]` because person 1 shares the secret with person 2 at time 5, and then person 2 shares the secret with person 3 at time 8, but person 1 also shares the secret with person 5 at time 10.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Create a graph where each person is a node, and two nodes are connected if the corresponding people meet. Then, perform a depth-first search (DFS) from the person who knows the secret to find all people who can know the secret.
- Step-by-step breakdown of the solution:
  1. Create a graph from the meetings.
  2. Identify the person who knows the secret initially.
  3. Perform DFS from the initial person to find all people who can know the secret.
- Why this approach comes to mind first: It's a straightforward way to model the problem as a graph and use a standard graph traversal algorithm to find the solution.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>

using namespace std;

vector<int> findAllPeople(vector<vector<int>>& meetings, string secret) {
    unordered_map<int, vector<int>> graph;
    for (auto& meeting : meetings) {
        graph[meeting[0]].push_back(meeting[1]);
        graph[meeting[1]].push_back(meeting[0]);
    }

    unordered_set<int> knowSecret;
    knowSecret.insert(0); // Person 0 knows the secret initially

    for (auto& meeting : meetings) {
        if (knowSecret.find(meeting[0]) != knowSecret.end()) {
            knowSecret.insert(meeting[1]);
        } else if (knowSecret.find(meeting[1]) != knowSecret.end()) {
            knowSecret.insert(meeting[0]);
        }
    }

    vector<int> result;
    for (int person : knowSecret) {
        result.push_back(person);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$ where $n$ is the number of people and $m$ is the number of meetings, because we iterate over all meetings and people once.
> - **Space Complexity:** $O(n + m)$ because we store all people and meetings in the graph and the set of people who know the secret.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each meeting and person. The space complexity is also linear because we store all meetings and people in the graph and the set.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a union-find data structure to keep track of the people who know the secret. When two people meet, we union their groups. If one of them knows the secret, we can then find all people in their group.
- Detailed breakdown of the approach:
  1. Create a union-find data structure with a `find` function to find the root of a group and a `union` function to merge two groups.
  2. Initialize the union-find data structure with each person in their own group.
  3. Iterate over the meetings and union the groups of the two people meeting.
  4. If one of the people knows the secret, find all people in their group and add them to the result.
- Proof of optimality: This approach is optimal because it uses a union-find data structure which has an amortized time complexity of $O(\alpha(n))$ for the `find` and `union` operations, where $\alpha(n)$ is the inverse Ackermann function which grows very slowly.

```cpp
class UnionFind {
public:
    vector<int> parent;
    UnionFind(int n) : parent(n) {
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
            parent[rootX] = rootY;
        }
    }
};

vector<int> findAllPeople(vector<vector<int>>& meetings, string secret) {
    int n = 0;
    for (auto& meeting : meetings) {
        n = max(n, max(meeting[0], meeting[1]));
    }
    n++;
    UnionFind uf(n);
    vector<int> knowSecret;
    knowSecret.push_back(0); // Person 0 knows the secret initially
    for (auto& meeting : meetings) {
        uf.union_(meeting[0], meeting[1]);
    }
    unordered_set<int> result;
    for (int person : knowSecret) {
        result.insert(uf.find(person));
    }
    vector<int> finalResult;
    for (int i = 0; i < n; i++) {
        if (result.find(uf.find(i)) != result.end()) {
            finalResult.push_back(i);
        }
    }
    return finalResult;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m \alpha(n))$ where $n$ is the number of people and $m$ is the number of meetings, because we iterate over all meetings and people once and perform union-find operations.
> - **Space Complexity:** $O(n)$ because we store all people in the union-find data structure.
> - **Optimality proof:** The time complexity is optimal because we use a union-find data structure which has an amortized time complexity of $O(\alpha(n))$ for the `find` and `union` operations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Union-find data structure, graph traversal.
- Problem-solving patterns identified: Using a union-find data structure to keep track of groups of people.
- Optimization techniques learned: Using a union-find data structure to reduce the time complexity of the solution.
- Similar problems to practice: Other problems involving graph traversal and union-find data structures.

**Mistakes to Avoid:**
- Common implementation errors: Not handling the case where two people meet multiple times.
- Edge cases to watch for: Handling cases where a person meets multiple people who know the secret.
- Performance pitfalls: Not using a union-find data structure which can lead to a higher time complexity.
- Testing considerations: Testing the solution with different inputs and edge cases to ensure it works correctly.