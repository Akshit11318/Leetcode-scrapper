## Find Followers Count
**Problem Link:** https://leetcode.com/problems/find-followers-count/description

**Problem Statement:**
- Input format and constraints: The problem involves finding the number of followers for each user in a given list of followers. The input is a list of tuples, where each tuple represents a follow relationship between two users.
- Expected output format: The output should be a list of tuples, where each tuple contains a user and their corresponding follower count.
- Key requirements and edge cases to consider: The solution should handle cases where a user has no followers, and it should also handle cases where a user is not present in the input list but is mentioned as a follower.
- Example test cases with explanations:
  - Example 1: Input: `followers = [["0","1"],["1","0"],["1","2"],["2","0"],["2","1"],["2","2"]]`, Output: `[["0",2],["1",2],["2",3]]`
  - Example 2: Input: `followers = [["0","1"],["1","0"],["1","2"],["2","0"],["2","1"],["2","2"],["3","2"]]`, Output: `[["0",2],["1",2],["2",4],["3",0]]`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves iterating over the list of followers and counting the occurrences of each user.
- Step-by-step breakdown of the solution:
  1. Create a dictionary to store the follower count for each user.
  2. Iterate over the list of followers.
  3. For each follower, increment the count for the corresponding user in the dictionary.
  4. Return a list of tuples, where each tuple contains a user and their corresponding follower count.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it may not be the most efficient solution.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>

vector<vector<string>> findFollowersCount(vector<vector<string>>& followers) {
    unordered_map<string, int> followerCount;
    for (auto& follow : followers) {
        if (followerCount.find(follow[0]) == followerCount.end()) {
            followerCount[follow[0]] = 0;
        }
        followerCount[follow[0]]++;
    }
    vector<vector<string>> result;
    for (auto& pair : followerCount) {
        result.push_back({pair.first, to_string(pair.second)});
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of followers. This is because we iterate over the list of followers once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of unique users. This is because we store the follower count for each user in a dictionary.
> - **Why these complexities occur:** The time complexity occurs because we iterate over the list of followers, and the space complexity occurs because we store the follower count for each user in a dictionary.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution involves using a `unordered_map` to store the follower count for each user, and then iterating over the input list to update the counts.
- Detailed breakdown of the approach:
  1. Create a `unordered_map` to store the follower count for each user.
  2. Iterate over the input list and update the counts in the `unordered_map`.
  3. Return a list of tuples, where each tuple contains a user and their corresponding follower count.
- Proof of optimality: This solution is optimal because it has a time complexity of $O(n)$ and a space complexity of $O(n)$, where $n$ is the number of unique users.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>

vector<vector<string>> findFollowersCount(vector<vector<string>>& followers) {
    unordered_map<string, int> followerCount;
    for (auto& follow : followers) {
        followerCount[follow[1]]++;
    }
    vector<vector<string>> result;
    for (auto& pair : followerCount) {
        result.push_back({pair.first, to_string(pair.second)});
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of followers. This is because we iterate over the list of followers once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of unique users. This is because we store the follower count for each user in a dictionary.
> - **Optimality proof:** This solution is optimal because it has a time complexity of $O(n)$ and a space complexity of $O(n)$, where $n$ is the number of unique users.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the use of `unordered_map` to store and update counts efficiently.
- Problem-solving patterns identified: The problem requires iterating over a list and updating counts in a dictionary.
- Optimization techniques learned: The problem requires optimizing the time and space complexity of the solution.
- Similar problems to practice: Similar problems include finding the frequency of elements in an array or finding the count of each word in a text.

**Mistakes to Avoid:**
- Common implementation errors: One common error is to forget to initialize the counts in the dictionary.
- Edge cases to watch for: One edge case is when a user has no followers.
- Performance pitfalls: One performance pitfall is to use a data structure with high time complexity, such as a linked list.
- Testing considerations: The solution should be tested with different input cases, including edge cases.