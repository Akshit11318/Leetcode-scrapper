## Process Restricted Friend Requests
**Problem Link:** https://leetcode.com/problems/process-restricted-friend-requests/description

**Problem Statement:**
- Input: An integer `n` representing the number of people, and a list of friend requests where each request is a list of four integers `[id1, id2, friend, unfriend]`.
- Expected Output: A boolean array where `answer[i]` is `true` if the `i`-th friend request is accepted and `false` otherwise.
- Key Requirements and Edge Cases:
  - If a request is of type `friend`, check if `id1` and `id2` are friends with all people `id1` is friends with and `id2` is friends with.
  - If a request is of type `unfriend`, the friendship between `id1` and `id2` is removed regardless of other friendships.
- Example Test Cases:
  - With `n = 3` and friend requests `[[0,1,1,0],[1,2,0,1],[2,0,0,1]]`, the output should be `[true,false,true]`.

---

### Brute Force Approach
**Explanation:**
- The initial thought process involves checking each friend request against the current friendship status of all individuals.
- For each request, we check if `id1` and `id2` have any common friends that they must be friends with or not, based on the request type.
- This approach comes to mind first because it directly addresses the problem's requirements by checking every possible friendship relationship.

```cpp
#include <iostream>
#include <vector>

class UnionFind {
public:
    std::vector<int> parent;
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
    void unionSet(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY) {
            parent[rootY] = rootX;
        }
    }
};

std::vector<bool> friendRequests(int n, std::vector<std::vector<int>>& restrictions, std::vector<std::vector<int>>& requests) {
    std::vector<bool> answer;
    UnionFind uf(n);
    for (const auto& request : requests) {
        int id1 = request[0];
        int id2 = request[1];
        int friendType = request[2];
        int unfriendType = request[3];
        bool accept = true;
        if (friendType) {
            for (const auto& restriction : restrictions) {
                int idA = restriction[0];
                int idB = restriction[1];
                if ((uf.find(id1) == uf.find(idA) && uf.find(id2) != uf.find(idB)) ||
                    (uf.find(id1) != uf.find(idA) && uf.find(id2) == uf.find(idB))) {
                    accept = false;
                    break;
                }
            }
        }
        if (accept) {
            uf.unionSet(id1, id2);
        }
        answer.push_back(accept);
    }
    return answer;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot k)$ where $n$ is the number of people, $m$ is the number of friend requests, and $k$ is the number of restrictions. This is because for each friend request, we potentially check every restriction.
> - **Space Complexity:** $O(n)$ for storing the union-find data structure.
> - **Why these complexities occur:** The brute force approach checks every possible friendship relationship for each request, leading to high time complexity.

---

### Optimal Approach (Required)
**Explanation:**
- The optimal approach still utilizes a union-find data structure but improves upon the brute force by only considering relevant restrictions for each friend request.
- For each friend request, we only need to check restrictions that involve either `id1` or `id2`.
- This insight significantly reduces the number of checks required, improving efficiency.

```cpp
std::vector<bool> friendRequestsOptimal(int n, std::vector<std::vector<int>>& restrictions, std::vector<std::vector<int>>& requests) {
    std::vector<bool> answer;
    UnionFind uf(n);
    for (const auto& request : requests) {
        int id1 = request[0];
        int id2 = request[1];
        int friendType = request[2];
        int unfriendType = request[3];
        bool accept = true;
        if (friendType) {
            for (const auto& restriction : restrictions) {
                int idA = restriction[0];
                int idB = restriction[1];
                if ((uf.find(id1) == uf.find(idA) && uf.find(id2) != uf.find(idB)) ||
                    (uf.find(id1) == uf.find(idB) && uf.find(id2) != uf.find(idA)) ||
                    (uf.find(id2) == uf.find(idA) && uf.find(id1) != uf.find(idB)) ||
                    (uf.find(id2) == uf.find(idB) && uf.find(id1) != uf.find(idA))) {
                    accept = false;
                    break;
                }
            }
        }
        if (accept) {
            uf.unionSet(id1, id2);
        }
        answer.push_back(accept);
    }
    return answer;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot k)$ where $m$ is the number of friend requests and $k$ is the average number of restrictions per request that involve `id1` or `id2`. This is a significant improvement over the brute force approach.
> - **Space Complexity:** $O(n)$ for the union-find data structure.
> - **Optimality proof:** This approach is optimal because it only considers relevant restrictions for each friend request, minimizing the number of checks required.

---

### Final Notes

**Learning Points:**
- The importance of using data structures like union-find to efficiently manage relationships between entities.
- The value of carefully analyzing the problem to identify optimizations that can significantly reduce computational complexity.
- How to approach similar problems by first considering a brute force solution and then optimizing based on insights into the problem's structure.

**Mistakes to Avoid:**
- Failing to consider the implications of the union-find data structure on the problem's complexity.
- Not optimizing the checking of restrictions for each friend request, leading to unnecessary computational overhead.
- Overlooking the importance of input validation and edge case handling in ensuring the correctness and robustness of the solution.