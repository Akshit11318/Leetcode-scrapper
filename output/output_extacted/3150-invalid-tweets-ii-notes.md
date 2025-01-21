## Invalid Tweets II
**Problem Link:** https://leetcode.com/problems/invalid-tweets-ii/description

**Problem Statement:**
- Input format and constraints: Given a list of `tweets` where each `tweet` is a string containing the `id` of the user who posted it and the `content` of the tweet.
- Expected output format: Return a list of `id`s of users who have posted at least one invalid tweet.
- Key requirements and edge cases to consider: A tweet is invalid if its length is greater than 15 characters. We need to find users who have posted at least one invalid tweet.
- Example test cases with explanations:
  - `tweets = ["1,hello", "2,world", "1,hello world"]`, the function should return `[1]` because user 1 has posted a tweet "hello world" which is longer than 15 characters.
  - `tweets = ["1,a", "2,b", "3,c"]`, the function should return `[]` because none of the tweets are longer than 15 characters.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can iterate through each tweet, split it into `id` and `content`, and then check if the length of the `content` is greater than 15. If it is, we add the `id` to our result list.
- Step-by-step breakdown of the solution:
  1. Initialize an empty set `invalidUsers` to store the `id`s of users who have posted at least one invalid tweet.
  2. Iterate through each `tweet` in the `tweets` list.
  3. Split the `tweet` into `id` and `content`.
  4. Check if the length of the `content` is greater than 15.
  5. If it is, add the `id` to the `invalidUsers` set.
- Why this approach comes to mind first: This is a straightforward approach that checks each tweet individually.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_set>

vector<int> invalidUsers(vector<string>& tweets) {
    unordered_set<int> invalidUsers;
    for (const string& tweet : tweets) {
        size_t commaIndex = tweet.find(',');
        int id = stoi(tweet.substr(0, commaIndex));
        string content = tweet.substr(commaIndex + 1);
        if (content.length() > 15) {
            invalidUsers.insert(id);
        }
    }
    vector<int> result(invalidUsers.begin(), invalidUsers.end());
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the number of tweets and $m$ is the maximum length of a tweet. This is because we are iterating through each tweet and then through each character in the content of the tweet.
> - **Space Complexity:** $O(n)$ where $n$ is the number of tweets. This is because in the worst-case scenario, all tweets could be invalid and we would need to store all their ids.
> - **Why these complexities occur:** These complexities occur because we are using a straightforward approach that checks each tweet individually.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use the same approach as the brute force solution but with a slight optimization. Instead of using a vector to store the result and then converting it to a set, we can directly use a set to store the ids of invalid users. This will eliminate any duplicate ids.
- Detailed breakdown of the approach:
  1. Initialize an empty set `invalidUsers` to store the `id`s of users who have posted at least one invalid tweet.
  2. Iterate through each `tweet` in the `tweets` list.
  3. Split the `tweet` into `id` and `content`.
  4. Check if the length of the `content` is greater than 15.
  5. If it is, add the `id` to the `invalidUsers` set.
- Proof of optimality: This approach is optimal because it only requires a single pass through the tweets list and uses a set to eliminate any duplicate ids.
- Why further optimization is impossible: Further optimization is impossible because we must check each tweet at least once to determine if it is invalid.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_set>

vector<int> invalidUsers(vector<string>& tweets) {
    unordered_set<int> invalidUsers;
    for (const string& tweet : tweets) {
        size_t commaIndex = tweet.find(',');
        int id = stoi(tweet.substr(0, commaIndex));
        string content = tweet.substr(commaIndex + 1);
        if (content.length() > 15) {
            invalidUsers.insert(id);
        }
    }
    vector<int> result(invalidUsers.begin(), invalidUsers.end());
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the number of tweets and $m$ is the maximum length of a tweet. This is because we are iterating through each tweet and then through each character in the content of the tweet.
> - **Space Complexity:** $O(n)$ where $n$ is the number of tweets. This is because in the worst-case scenario, all tweets could be invalid and we would need to store all their ids.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the tweets list and uses a set to eliminate any duplicate ids.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a set to eliminate duplicate ids.
- Problem-solving patterns identified: Checking each tweet individually to determine if it is invalid.
- Optimization techniques learned: Using a set instead of a vector to store the result.
- Similar problems to practice: Other problems that involve checking each item in a list and eliminating duplicates.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases such as empty tweets or tweets with no content.
- Edge cases to watch for: Tweets with no content or empty tweets.
- Performance pitfalls: Using a vector to store the result and then converting it to a set.
- Testing considerations: Testing the function with different inputs such as empty tweets, tweets with no content, and tweets with duplicate ids.