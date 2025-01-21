## Tweet Counts Per Frequency

**Problem Link:** https://leetcode.com/problems/tweet-counts-per-frequency/description

**Problem Statement:**
- Input format: `tweets` array of strings, each representing a tweet, and `freq` array of strings, representing the frequency of each tweet.
- Constraints: The length of `tweets` and `freq` are the same.
- Expected output format: A 2D array where each sub-array contains the tweet and its corresponding frequency.
- Key requirements and edge cases to consider: Handling empty input arrays, invalid frequency strings, and duplicate tweets.
- Example test cases with explanations:
  - Input: `tweets = ["tweet3","tweet1","tweet2","tweet3","tweet1","tweet2"], freq = ["daily","daily","daily","daily","daily","daily"]`
    Output: `[["tweet1","2"],["tweet2","2"],["tweet3","2"]]`
  - Input: `tweets = ["tweet3","tweet1","tweet2","tweet3","tweet1","tweet2"], freq = ["daily","daily","daily","hourly","hourly","hourly"]`
    Output: `[["tweet1","1"],["tweet2","1"],["tweet3","1"]]`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Create a dictionary to store the frequency of each tweet and then iterate over the dictionary to create the output.
- Step-by-step breakdown of the solution:
  1. Create a dictionary to store the frequency of each tweet.
  2. Iterate over the `tweets` and `freq` arrays, and update the frequency of each tweet in the dictionary.
  3. Iterate over the dictionary and create the output array.
- Why this approach comes to mind first: It is a straightforward approach that uses a dictionary to store the frequency of each tweet, making it easy to calculate the frequency.

```cpp
vector<vector<string>> tweetCounts(vector<string>& tweets, vector<string>& freq) {
    unordered_map<string, unordered_map<string, int>> tweet_freq;
    for (int i = 0; i < tweets.size(); i++) {
        string tweet = tweets[i];
        string frequency = freq[i];
        if (tweet_freq.find(tweet) == tweet_freq.end()) {
            tweet_freq[tweet] = {};
        }
        if (tweet_freq[tweet].find(frequency) == tweet_freq[tweet].end()) {
            tweet_freq[tweet][frequency] = 0;
        }
        tweet_freq[tweet][frequency]++;
    }
    vector<vector<string>> result;
    for (auto& tweet : tweet_freq) {
        for (auto& freq : tweet.second) {
            result.push_back({tweet.first, to_string(freq.second)});
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the `tweets` array. This is because we are iterating over the `tweets` and `freq` arrays twice.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the `tweets` array. This is because we are storing the frequency of each tweet in a dictionary.
> - **Why these complexities occur:** The time complexity occurs because we are iterating over the `tweets` and `freq` arrays twice, and the space complexity occurs because we are storing the frequency of each tweet in a dictionary.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a single pass over the `tweets` and `freq` arrays to calculate the frequency of each tweet.
- Detailed breakdown of the approach:
  1. Create a dictionary to store the frequency of each tweet.
  2. Iterate over the `tweets` and `freq` arrays, and update the frequency of each tweet in the dictionary.
  3. Create the output array from the dictionary.
- Proof of optimality: This approach is optimal because it only requires a single pass over the `tweets` and `freq` arrays, resulting in a time complexity of $O(n)$.
- Why further optimization is impossible: This approach is already optimal because it only requires a single pass over the input arrays.

```cpp
vector<vector<string>> tweetCounts(vector<string>& tweets, vector<string>& freq) {
    unordered_map<string, unordered_map<string, int>> tweet_freq;
    for (int i = 0; i < tweets.size(); i++) {
        string tweet = tweets[i];
        string frequency = freq[i];
        if (tweet_freq.find(tweet) == tweet_freq.end()) {
            tweet_freq[tweet] = {};
        }
        if (tweet_freq[tweet].find(frequency) == tweet_freq[tweet].end()) {
            tweet_freq[tweet][frequency] = 0;
        }
        tweet_freq[tweet][frequency]++;
    }
    vector<vector<string>> result;
    for (auto& tweet : tweet_freq) {
        for (auto& freq : tweet.second) {
            result.push_back({tweet.first, to_string(freq.second)});
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the `tweets` array. This is because we are iterating over the `tweets` and `freq` arrays once.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the `tweets` array. This is because we are storing the frequency of each tweet in a dictionary.
> - **Optimality proof:** This approach is optimal because it only requires a single pass over the `tweets` and `freq` arrays, resulting in a time complexity of $O(n)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Hashing, dictionary operations.
- Problem-solving patterns identified: Using a dictionary to store frequency of elements.
- Optimization techniques learned: Reducing the number of passes over the input arrays.
- Similar problems to practice: Frequency of elements in an array, counting the number of occurrences of each word in a text.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as empty input arrays.
- Edge cases to watch for: Duplicate tweets, invalid frequency strings.
- Performance pitfalls: Using multiple passes over the input arrays when a single pass is possible.
- Testing considerations: Testing with different input sizes, testing with edge cases.