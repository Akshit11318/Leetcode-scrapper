## Invalid Tweets

**Problem Link:** https://leetcode.com/problems/invalid-tweets/description

**Problem Statement:**
- Input format and constraints: Given a list of tweets and a limit for the number of characters allowed in a tweet.
- Expected output format: Identify and return the indices of the tweets that exceed the character limit.
- Key requirements and edge cases to consider: Handling empty tweets, tweets with exactly the allowed number of characters, and tweets exceeding the limit.
- Example test cases with explanations: 
  - For example, given `tweets = ["hello", "world", "this is a long tweet that exceeds the limit"]` and `limit = 10`, the function should return the indices of tweets that are longer than the limit.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through each tweet and check its length against the given limit.
- Step-by-step breakdown of the solution:
  1. Initialize an empty list to store the indices of invalid tweets.
  2. Loop through each tweet in the list of tweets.
  3. For each tweet, check if its length exceeds the given limit.
  4. If a tweet exceeds the limit, add its index to the list of invalid tweets.
- Why this approach comes to mind first: It directly addresses the problem statement by checking each tweet against the limit.

```cpp
vector<int> invalidTweets(vector<string>& tweets, int limit) {
    vector<int> invalidIndices;
    for (int i = 0; i < tweets.size(); i++) {
        if (tweets[i].length() > limit) {
            invalidIndices.push_back(i);
        }
    }
    return invalidIndices;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of tweets and $m$ is the average length of a tweet. This is because for each tweet, we potentially iterate over its characters to check the length.
> - **Space Complexity:** $O(n)$, as in the worst case, all tweets could exceed the limit, requiring us to store all their indices.
> - **Why these complexities occur:** The time complexity is due to the iteration over each character in each tweet to check its length, and the space complexity is due to storing the indices of all invalid tweets.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The brute force approach is already quite straightforward and optimal for this problem since we must check each tweet's length against the limit. However, we can slightly optimize the code by using `const` references to avoid unnecessary copies of the strings.
- Detailed breakdown of the approach: The optimal approach remains the same as the brute force in terms of logic but with minor optimizations for better performance and readability.
- Proof of optimality: This approach is optimal because it has a linear time complexity with respect to the number of tweets and their average length, which is the minimum required to check each tweet's length.

```cpp
vector<int> invalidTweets(vector<string>& tweets, int limit) {
    vector<int> invalidIndices;
    for (int i = 0; i < tweets.size(); i++) {
        const string& tweet = tweets[i]; // Using const reference for optimization
        if (tweet.length() > limit) {
            invalidIndices.push_back(i);
        }
    }
    return invalidIndices;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of tweets and $m$ is the average length of a tweet. This is because for each tweet, we potentially iterate over its characters to check the length.
> - **Space Complexity:** $O(n)$, as in the worst case, all tweets could exceed the limit, requiring us to store all their indices.
> - **Optimality proof:** This is the optimal complexity because we must at least check the length of each tweet, which requires iterating over its characters in the worst case.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, conditional checks, and storage of results.
- Problem-solving patterns identified: Checking each element in a collection against a condition.
- Optimization techniques learned: Using `const` references to avoid unnecessary copies.
- Similar problems to practice: Other problems involving iteration and conditional checks, such as finding elements in an array that meet certain criteria.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases like empty strings or strings exactly at the limit.
- Edge cases to watch for: Tweets with lengths exactly equal to the limit should not be considered invalid.
- Performance pitfalls: Unnecessary copies of strings can lead to performance issues for large inputs.
- Testing considerations: Ensure to test with a variety of inputs, including empty tweets, tweets at the limit, and tweets exceeding the limit.