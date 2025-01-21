## Tournament Winners

**Problem Link:** https://leetcode.com/problems/tournament-winners/description

**Problem Statement:**
- The input consists of a list of integers representing the number of matches played and won by each player.
- The task is to find the top three players with the most wins.
- The output should be a list of the names of the top three players.
- Key requirements include handling cases where there are fewer than three players and where players have the same number of wins.
- Example test cases include scenarios with a varying number of players and wins.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves sorting the players based on their wins and then selecting the top three.
- This approach comes to mind first because it directly addresses the requirement of finding the top three players with the most wins.
- However, it might not be the most efficient solution due to the overhead of sorting.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

struct Player {
    string name;
    int wins;
};

bool comparePlayers(const Player& a, const Player& b) {
    return a.wins > b.wins;
}

vector<string> findTopThree(vector<Player>& players) {
    // Sort players based on their wins in descending order
    sort(players.begin(), players.end(), comparePlayers);
    
    vector<string> topThree;
    for (int i = 0; i < min(3, (int)players.size()); i++) {
        topThree.push_back(players[i].name);
    }
    
    return topThree;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting operation, where $n$ is the number of players.
> - **Space Complexity:** $O(n)$ for storing the players and $O(1)$ for the sorting algorithm (in-place), making it $O(n)$ overall.
> - **Why these complexities occur:** The time complexity is dominated by the sorting operation, and the space complexity is due to the storage of players and the output.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a `priority_queue` to keep track of the top three players with the most wins.
- This approach is optimal because it avoids the need for sorting the entire list of players, reducing the time complexity.
- By maintaining a `priority_queue` of size 3, we can efficiently find the top three players.

```cpp
#include <iostream>
#include <vector>
#include <queue>

struct Player {
    string name;
    int wins;
};

struct ComparePlayers {
    bool operator()(const Player& a, const Player& b) {
        return a.wins < b.wins;
    }
};

vector<string> findTopThree(vector<Player>& players) {
    priority_queue<Player, vector<Player>, ComparePlayers> pq;
    
    for (const auto& player : players) {
        if (pq.size() < 3) {
            pq.push(player);
        } else if (player.wins > pq.top().wins) {
            pq.pop();
            pq.push(player);
        }
    }
    
    vector<string> topThree;
    while (!pq.empty()) {
        topThree.push_back(pq.top().name);
        pq.pop();
    }
    
    reverse(topThree.begin(), topThree.end());
    
    return topThree;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log k)$, where $n$ is the number of players and $k=3$ is the size of the `priority_queue`.
> - **Space Complexity:** $O(k)$ for the `priority_queue`, making it $O(1)$ since $k$ is constant.
> - **Optimality proof:** This is the best possible complexity because we only need to consider the top three players, and using a `priority_queue` allows us to do so efficiently.

---

### Final Notes

**Learning Points:**
- The importance of using the right data structure (e.g., `priority_queue`) for efficient problem-solving.
- Understanding the trade-offs between time and space complexity.
- Identifying the key insight that leads to an optimal solution.

**Mistakes to Avoid:**
- Not considering the use of a `priority_queue` for similar problems.
- Overlooking the possibility of using a more efficient data structure.
- Failing to analyze the time and space complexity of the solution.