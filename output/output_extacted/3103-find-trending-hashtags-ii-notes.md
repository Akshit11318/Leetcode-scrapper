## Find Trending Hashtags II
**Problem Link:** https://leetcode.com/problems/find-trending-hashtags-ii/description

**Problem Statement:**
- Input format: You are given a list of `tweets`, where each tweet is a string containing one or more `hashtags`.
- Constraints: 
  - Each hashtag starts with a `#` symbol.
  - Each hashtag is unique within a tweet.
  - The list of tweets can be empty.
- Expected output format: Return a list of all unique `hashtags` that appear in at least two tweets.
- Key requirements and edge cases to consider:
  - Handling empty tweets or tweets with no hashtags.
  - Case sensitivity of hashtags.
  - Efficiency in processing large lists of tweets.
- Example test cases with explanations:
  - Input: `["#apple #banana", "#apple #orange", "#banana #grape"]`
    Output: `["#apple", "#banana"]`
  - Input: `["#apple", "#banana", "#orange"]`
    Output: `[]`
  - Input: `[]`
    Output: `[]`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through each tweet, extract the hashtags, and then count the occurrences of each hashtag across all tweets.
- Step-by-step breakdown of the solution:
  1. Initialize an empty map to store hashtags and their counts.
  2. Iterate through each tweet, split it into words, and identify words that start with `#` as hashtags.
  3. For each hashtag, increment its count in the map.
  4. After processing all tweets, iterate through the map and collect hashtags with counts greater than 1.
- Why this approach comes to mind first: It directly addresses the problem by counting the occurrences of each hashtag.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

std::vector<std::string> findTrendingHashtags(std::vector<std::string>& tweets) {
    std::unordered_map<std::string, int> hashtagCounts;
    for (const auto& tweet : tweets) {
        std::string word;
        for (char c : tweet) {
            if (c == ' ') {
                if (!word.empty() && word[0] == '#') {
                    hashtagCounts[word]++;
                }
                word.clear();
            } else {
                word += c;
            }
        }
        if (!word.empty() && word[0] == '#') {
            hashtagCounts[word]++;
        }
    }
    
    std::vector<std::string> trendingHashtags;
    for (const auto& pair : hashtagCounts) {
        if (pair.second > 1) {
            trendingHashtags.push_back(pair.first);
        }
    }
    return trendingHashtags;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(N \cdot M)$, where $N$ is the number of tweets and $M$ is the average number of words in a tweet. This is because we potentially iterate through each word in each tweet once.
> - **Space Complexity:** $O(N \cdot M)$, as in the worst case, every word in every tweet could be a unique hashtag.
> - **Why these complexities occur:** The brute force approach requires iterating through all tweets and all words within those tweets, leading to the time complexity. The space complexity arises from storing all unique hashtags in the map.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The brute force approach is already quite efficient for this problem. However, we can slightly optimize it by using a more efficient way to split the tweets into words and by directly checking if a word is a hashtag without needing to iterate through all characters of the word.
- Detailed breakdown of the approach:
  1. Use a `std::istringstream` to split each tweet into words, which can be more efficient than manual character iteration.
  2. For each word, check if it starts with `#` and then update its count in the map.
  3. The rest of the approach remains the same as the brute force.
- Proof of optimality: This approach still has a time complexity of $O(N \cdot M)$ but with potentially better constants due to the use of `std::istringstream`.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <sstream>

std::vector<std::string> findTrendingHashtagsOptimal(std::vector<std::string>& tweets) {
    std::unordered_map<std::string, int> hashtagCounts;
    for (const auto& tweet : tweets) {
        std::istringstream iss(tweet);
        std::string word;
        while (iss >> word) {
            if (word[0] == '#') {
                hashtagCounts[word]++;
            }
        }
    }
    
    std::vector<std::string> trendingHashtags;
    for (const auto& pair : hashtagCounts) {
        if (pair.second > 1) {
            trendingHashtags.push_back(pair.first);
        }
    }
    return trendingHashtags;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(N \cdot M)$, similar to the brute force approach but potentially with better performance due to the use of `std::istringstream`.
> - **Space Complexity:** $O(N \cdot M)$, as the space usage does not change from the brute force approach.
> - **Optimality proof:** This approach is optimal because it must iterate through all tweets and all words within those tweets to find the trending hashtags. The use of `std::istringstream` might provide a slight improvement in practice.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, hashmap usage for counting, and string processing.
- Problem-solving patterns identified: The importance of iterating through all data points (in this case, tweets and words within tweets) to solve a problem that requires counting or aggregating information.
- Optimization techniques learned: Using built-in functions or classes (like `std::istringstream`) for tasks they are optimized for can lead to better performance.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases like empty tweets or tweets with no hashtags.
- Edge cases to watch for: Handling case sensitivity of hashtags, and ensuring that the solution works correctly for large inputs.
- Performance pitfalls: Using inefficient methods for string processing or not utilizing hashmap for efficient counting.
- Testing considerations: Ensure to test the solution with various inputs, including edge cases, to verify its correctness and performance.