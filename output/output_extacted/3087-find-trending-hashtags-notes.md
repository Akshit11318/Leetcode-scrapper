## Find Trending Hashtags
**Problem Link:** https://leetcode.com/problems/find-trending-hashtags/description

**Problem Statement:**
- Input format and constraints: The input will be a list of tweets where each tweet is a string. The task is to find the top `k` trending hashtags from these tweets. 
- Expected output format: The output should be a list of the top `k` trending hashtags in the order of their frequency.
- Key requirements and edge cases to consider: 
    - The input list of tweets can be empty.
    - The tweets can be empty strings.
    - The same hashtag can appear multiple times in the same tweet.
    - The hashtags are case-sensitive.
    - The input list can be very large.
- Example test cases with explanations:
    - Example 1:
        - Input: `tweets = ["#apple is a great company", "#apple is very innovative", "#banana is a delicious fruit"]`, `k = 2`
        - Output: `["#apple", "#banana"]`
        - Explanation: The hashtag `#apple` appears twice and `#banana` appears once.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find the top `k` trending hashtags, we can first extract all the hashtags from the tweets, then count their frequencies, and finally sort them based on their frequencies.
- Step-by-step breakdown of the solution:
    1. Extract all the hashtags from the tweets.
    2. Count the frequency of each hashtag.
    3. Sort the hashtags based on their frequencies in descending order.
    4. Return the top `k` hashtags.
- Why this approach comes to mind first: It is a straightforward approach that directly addresses the problem statement.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>

vector<string> findTrendingHashtags(vector<string>& tweets, int k) {
    unordered_map<string, int> hashtagCount;
    for (const string& tweet : tweets) {
        size_t start = 0;
        while (start < tweet.size()) {
            size_t hashtagStart = tweet.find('#', start);
            if (hashtagStart == string::npos) break;
            size_t hashtagEnd = tweet.find(' ', hashtagStart);
            if (hashtagEnd == string::npos) hashtagEnd = tweet.size();
            string hashtag = tweet.substr(hashtagStart, hashtagEnd - hashtagStart);
            hashtagCount[hashtag]++;
            start = hashtagEnd;
        }
    }

    vector<pair<string, int>> sortedHashtags;
    for (const auto& pair : hashtagCount) {
        sortedHashtags.push_back(pair);
    }
    sort(sortedHashtags.begin(), sortedHashtags.end(), [](const pair<string, int>& a, const pair<string, int>& b) {
        return a.second > b.second;
    });

    vector<string> result;
    for (int i = 0; i < k && i < sortedHashtags.size(); i++) {
        result.push_back(sortedHashtags[i].first);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot log(m))$ where $n$ is the number of tweets and $m$ is the average number of hashtags per tweet. The reason is that we first extract all the hashtags which takes $O(n \cdot m)$ time, then we sort the hashtags which takes $O(m \cdot log(m))$ time.
> - **Space Complexity:** $O(n \cdot m)$ where $n$ is the number of tweets and $m$ is the average number of hashtags per tweet. The reason is that we store all the hashtags in the `hashtagCount` map.
> - **Why these complexities occur:** The time complexity occurs because we use a sorting algorithm to sort the hashtags. The space complexity occurs because we store all the hashtags in the `hashtagCount` map.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a priority queue to store the top `k` hashtags. This way, we don't need to sort all the hashtags.
- Detailed breakdown of the approach:
    1. Extract all the hashtags from the tweets.
    2. Count the frequency of each hashtag.
    3. Use a priority queue to store the top `k` hashtags.
    4. Return the top `k` hashtags.
- Proof of optimality: This approach is optimal because we only need to store the top `k` hashtags, which reduces the space complexity.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <queue>

vector<string> findTrendingHashtags(vector<string>& tweets, int k) {
    unordered_map<string, int> hashtagCount;
    for (const string& tweet : tweets) {
        size_t start = 0;
        while (start < tweet.size()) {
            size_t hashtagStart = tweet.find('#', start);
            if (hashtagStart == string::npos) break;
            size_t hashtagEnd = tweet.find(' ', hashtagStart);
            if (hashtagEnd == string::npos) hashtagEnd = tweet.size();
            string hashtag = tweet.substr(hashtagStart, hashtagEnd - hashtagStart);
            hashtagCount[hashtag]++;
            start = hashtagEnd;
        }
    }

    priority_queue<pair<int, string>> maxHeap;
    for (const auto& pair : hashtagCount) {
        if (maxHeap.size() < k) {
            maxHeap.push({pair.second, pair.first});
        } else if (pair.second > maxHeap.top().first) {
            maxHeap.pop();
            maxHeap.push({pair.second, pair.first});
        }
    }

    vector<string> result;
    while (!maxHeap.empty()) {
        result.push_back(maxHeap.top().second);
        maxHeap.pop();
    }
    reverse(result.begin(), result.end());
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot log(k))$ where $n$ is the number of tweets and $m$ is the average number of hashtags per tweet. The reason is that we use a priority queue to store the top `k` hashtags.
> - **Space Complexity:** $O(n \cdot m)$ where $n$ is the number of tweets and $m$ is the average number of hashtags per tweet. The reason is that we store all the hashtags in the `hashtagCount` map.
> - **Optimality proof:** This approach is optimal because we only need to store the top `k` hashtags, which reduces the time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: 
    - Using a priority queue to store the top `k` elements.
    - Using an unordered map to count the frequency of each hashtag.
- Problem-solving patterns identified: 
    - Extracting information from a string.
    - Counting the frequency of each element.
- Optimization techniques learned: 
    - Using a priority queue to reduce the time complexity.
- Similar problems to practice: 
    - Finding the top `k` frequent elements in an array.
    - Finding the top `k` frequent words in a document.

**Mistakes to Avoid:**
- Common implementation errors: 
    - Not handling edge cases such as an empty input list.
    - Not checking for invalid inputs such as a negative value of `k`.
- Edge cases to watch for: 
    - An empty input list.
    - A negative value of `k`.
- Performance pitfalls: 
    - Using a sorting algorithm to sort all the hashtags.
- Testing considerations: 
    - Testing with an empty input list.
    - Testing with a negative value of `k`.