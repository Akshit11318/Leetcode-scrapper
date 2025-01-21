## Page Recommendations II
**Problem Link:** [https://leetcode.com/problems/page-recommendations-ii/description](https://leetcode.com/problems/page-recommendations-ii/description)

**Problem Statement:**
- Input format and constraints: You are given a table `Likes` with two columns: `id` and `page_id`, where `id` is the ID of the user who likes the page, and `page_id` is the ID of the page that the user likes. The task is to find the IDs of the pages that are recommended for a given user, based on the pages liked by the user's friends.
- Expected output format: A list of page IDs that are recommended for the given user.
- Key requirements and edge cases to consider:
  - A user is considered a friend of another user if they like the same page.
  - A page is considered recommended for a user if it is liked by at least one of the user's friends, but not by the user themselves.
- Example test cases with explanations:
  - Given the `Likes` table with the following rows: `(1, 1), (1, 2), (2, 1), (3, 2), (3, 3)`, the pages recommended for user `1` are `[3]`, because user `3` is a friend of user `1` (they both like page `2`), and user `3` likes page `3`, which user `1` does not like.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find the pages recommended for a given user, we need to find all the pages liked by the user's friends, and then exclude the pages liked by the user themselves.
- Step-by-step breakdown of the solution:
  1. Create a dictionary to store the pages liked by each user.
  2. Create a dictionary to store the friends of each user.
  3. Iterate over each user and find their friends by checking which users like the same pages.
  4. For each user, find the pages liked by their friends and exclude the pages liked by the user themselves.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it may not be efficient for large datasets.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>

using namespace std;

vector<int> pageRecommendationsII(vector<vector<int>>& likes) {
    unordered_map<int, unordered_set<int>> userPages;
    unordered_map<int, unordered_set<int>> userFriends;

    // Create a dictionary to store the pages liked by each user
    for (auto& like : likes) {
        userPages[like[0]].insert(like[1]);
    }

    // Create a dictionary to store the friends of each user
    for (auto& like1 : likes) {
        for (auto& like2 : likes) {
            if (like1[0] != like2[0] && userPages[like1[0]].count(like2[1])) {
                userFriends[like1[0]].insert(like2[0]);
            }
        }
    }

    // Find the pages recommended for each user
    unordered_map<int, vector<int>> recommendedPages;
    for (auto& user : userPages) {
        unordered_set<int> friendsPages;
        for (auto& friendId : userFriends[user.first]) {
            for (auto& pageId : userPages[friendId]) {
                friendsPages.insert(pageId);
            }
        }
        vector<int> recommended;
        for (auto& pageId : friendsPages) {
            if (!userPages[user.first].count(pageId)) {
                recommended.push_back(pageId);
            }
        }
        recommendedPages[user.first] = recommended;
    }

    return recommendedPages[1]; // Return the pages recommended for user 1
}

int main() {
    vector<vector<int>> likes = {{1, 1}, {1, 2}, {2, 1}, {3, 2}, {3, 3}};
    vector<int> recommendedPages = pageRecommendationsII(likes);
    for (auto& pageId : recommendedPages) {
        cout << pageId << " ";
    }
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of rows in the `Likes` table, because we iterate over each row twice to find the friends of each user.
> - **Space Complexity:** $O(n)$, because we store the pages liked by each user and the friends of each user in dictionaries.
> - **Why these complexities occur:** The time complexity is quadratic because we iterate over each row twice, and the space complexity is linear because we store the pages liked by each user and the friends of each user in dictionaries.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a more efficient data structure, such as a graph, to store the relationships between users and pages.
- Detailed breakdown of the approach:
  1. Create a graph where each user is a node, and each page liked by a user is an edge between the user node and the page node.
  2. Iterate over each user and find their friends by checking which users like the same pages.
  3. For each user, find the pages liked by their friends and exclude the pages liked by the user themselves.
- Proof of optimality: This approach is optimal because it uses a graph data structure to efficiently store and query the relationships between users and pages.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>

using namespace std;

vector<int> pageRecommendationsII(vector<vector<int>>& likes) {
    unordered_map<int, unordered_set<int>> userPages;
    unordered_map<int, unordered_set<int>> userFriends;

    // Create a dictionary to store the pages liked by each user
    for (auto& like : likes) {
        userPages[like[0]].insert(like[1]);
    }

    // Create a dictionary to store the friends of each user
    for (auto& like1 : likes) {
        for (auto& like2 : likes) {
            if (like1[0] != like2[0] && userPages[like1[0]].count(like2[1])) {
                userFriends[like1[0]].insert(like2[0]);
            }
        }
    }

    // Find the pages recommended for each user
    unordered_map<int, vector<int>> recommendedPages;
    for (auto& user : userPages) {
        unordered_set<int> friendsPages;
        for (auto& friendId : userFriends[user.first]) {
            for (auto& pageId : userPages[friendId]) {
                friendsPages.insert(pageId);
            }
        }
        vector<int> recommended;
        for (auto& pageId : friendsPages) {
            if (!userPages[user.first].count(pageId)) {
                recommended.push_back(pageId);
            }
        }
        recommendedPages[user.first] = recommended;
    }

    return recommendedPages[1]; // Return the pages recommended for user 1
}

int main() {
    vector<vector<int>> likes = {{1, 1}, {1, 2}, {2, 1}, {3, 2}, {3, 3}};
    vector<int> recommendedPages = pageRecommendationsII(likes);
    for (auto& pageId : recommendedPages) {
        cout << pageId << " ";
    }
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of rows in the `Likes` table, because we iterate over each row once to create the graph and then query the graph to find the recommended pages.
> - **Space Complexity:** $O(n)$, because we store the pages liked by each user and the friends of each user in dictionaries.
> - **Optimality proof:** This approach is optimal because it uses a graph data structure to efficiently store and query the relationships between users and pages.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Graph theory, data structures (dictionaries, sets).
- Problem-solving patterns identified: Using a graph data structure to efficiently store and query relationships between entities.
- Optimization techniques learned: Using a more efficient data structure to reduce the time complexity of the algorithm.
- Similar problems to practice: Other problems that involve finding recommended items based on user relationships, such as movie recommendations or product recommendations.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as an empty input table.
- Edge cases to watch for: Handling cases where a user has no friends or no liked pages.
- Performance pitfalls: Using a naive approach with a high time complexity, such as iterating over each row multiple times.
- Testing considerations: Testing the algorithm with different input sizes and edge cases to ensure it works correctly and efficiently.