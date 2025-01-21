## Reported Posts
**Problem Link:** https://leetcode.com/problems/reported-posts/description

**Problem Statement:**
- Input format: A table `actions` with columns `id`, `post_id`, `action_date`, `action`, `extra`.
- Constraints: Each row represents a user's action on a post.
- Expected output format: A table with two columns, `id` and `report_reason`, where `id` is the post id and `report_reason` is the reason for reporting the post.
- Key requirements and edge cases to consider:
  - A post is considered reported if it has a 'report' action.
  - If a post is reported, the report reason is the 'extra' value from the report action.
- Example test cases with explanations:
  - If a post has multiple 'report' actions, the report reason is the 'extra' value from the first 'report' action.
  - If a post has no 'report' actions, it should not be included in the output.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over each action in the `actions` table and check if the action is 'report'. If it is, add the post id and report reason to the result table.
- Step-by-step breakdown of the solution:
  1. Initialize an empty result table.
  2. Iterate over each action in the `actions` table.
  3. Check if the action is 'report'.
  4. If it is, add the post id and report reason to the result table.
- Why this approach comes to mind first: It is a straightforward and intuitive approach that directly implements the problem requirements.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>

struct Action {
    int id;
    int post_id;
    std::string action;
    std::string extra;
};

std::vector<std::pair<int, std::string>> reportedPosts(std::vector<Action>& actions) {
    std::unordered_map<int, bool> reported;
    std::unordered_map<int, std::string> reportReasons;
    std::vector<std::pair<int, std::string>> result;

    for (const auto& action : actions) {
        if (action.action == "report") {
            if (!reported[action.post_id]) {
                reportReasons[action.post_id] = action.extra;
                reported[action.post_id] = true;
            }
        }
    }

    for (const auto& pair : reportReasons) {
        result.push_back({pair.first, pair.second});
    }

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of actions. This is because we are iterating over each action once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of actions. This is because we are storing the reported posts and their report reasons in hash maps.
> - **Why these complexities occur:** The time complexity is linear because we are iterating over each action once. The space complexity is linear because we are storing the reported posts and their report reasons in hash maps.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The same as the brute force approach, but we can use a more efficient data structure to store the reported posts and their report reasons.
- Detailed breakdown of the approach:
  1. Initialize an empty hash map to store the reported posts and their report reasons.
  2. Iterate over each action in the `actions` table.
  3. Check if the action is 'report'.
  4. If it is, add the post id and report reason to the hash map if the post id is not already in the hash map.
- Proof of optimality: This approach is optimal because we are only iterating over each action once and using a hash map to store the reported posts and their report reasons, which allows for constant time lookups and insertions.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>

struct Action {
    int id;
    int post_id;
    std::string action;
    std::string extra;
};

std::vector<std::pair<int, std::string>> reportedPosts(std::vector<Action>& actions) {
    std::unordered_map<int, std::string> reportReasons;
    std::vector<std::pair<int, std::string>> result;

    for (const auto& action : actions) {
        if (action.action == "report" && reportReasons.find(action.post_id) == reportReasons.end()) {
            reportReasons[action.post_id] = action.extra;
        }
    }

    for (const auto& pair : reportReasons) {
        result.push_back({pair.first, pair.second});
    }

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of actions. This is because we are iterating over each action once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of actions. This is because we are storing the reported posts and their report reasons in a hash map.
> - **Optimality proof:** This approach is optimal because we are only iterating over each action once and using a hash map to store the reported posts and their report reasons, which allows for constant time lookups and insertions.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Hash maps, iteration over a list of actions.
- Problem-solving patterns identified: Using a hash map to store reported posts and their report reasons.
- Optimization techniques learned: Using a more efficient data structure to store the reported posts and their report reasons.
- Similar problems to practice: Problems involving iteration over a list of actions and using a hash map to store data.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if a post id is already in the hash map before adding it.
- Edge cases to watch for: Posts with no 'report' actions, posts with multiple 'report' actions.
- Performance pitfalls: Using a data structure with slower lookups and insertions, such as a vector or list.
- Testing considerations: Testing the function with different inputs, including posts with no 'report' actions, posts with multiple 'report' actions, and posts with different report reasons.