## Finding the Topic of Each Post

**Problem Link:** https://leetcode.com/problems/finding-the-topic-of-each-post/description

**Problem Statement:**
- Given a list of posts, where each post is represented as a string, and a list of topics, where each topic is a string.
- The task is to find the topic of each post based on the presence of words in the post.
- Each word in a post can be a topic, and the topic of a post is the word that appears most frequently in the post.
- If there are multiple words with the same highest frequency, the topic is the one that comes first alphabetically.

**Input Format and Constraints:**
- The input consists of a list of posts and a list of topics.
- Each post is a string, and each topic is a string.
- The number of posts is between 1 and 100.
- The number of topics is between 1 and 100.
- Each post contains at most 100 words.
- Each topic contains at most 100 characters.

**Expected Output Format:**
- The output should be a list of topics, where each topic corresponds to the topic of a post.

**Key Requirements and Edge Cases to Consider:**
- If a post contains multiple words with the same highest frequency, the topic is the one that comes first alphabetically.
- If a post does not contain any words that are topics, the topic is an empty string.
- The input lists are not empty.

**Example Test Cases with Explanations:**
- Example 1:
  - Input: posts = ["post1", "post2"], topics = ["topic1", "topic2"]
  - Output: ["topic1", "topic2"]
  - Explanation: The topic of each post is the word that appears most frequently in the post.
- Example 2:
  - Input: posts = ["post1 post1", "post2 post2 post2"], topics = ["post1", "post2"]
  - Output: ["post1", "post2"]
  - Explanation: The topic of each post is the word that appears most frequently in the post.

---

### Brute Force Approach

**Explanation:**
- The brute force approach involves iterating over each post and each word in the post to find the frequency of each word.
- Then, iterate over the topics to find the topic that appears most frequently in the post.
- If there are multiple topics with the same highest frequency, the topic is the one that comes first alphabetically.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>

vector<string> findTopics(vector<string>& posts, vector<string>& topics) {
    vector<string> result;
    for (string post : posts) {
        map<string, int> wordCount;
        string word;
        for (char c : post) {
            if (c == ' ') {
                if (!word.empty()) {
                    wordCount[word]++;
                    word.clear();
                }
            } else {
                word += c;
            }
        }
        if (!word.empty()) {
            wordCount[word]++;
        }
        
        string topic;
        int maxCount = 0;
        for (auto& pair : wordCount) {
            if (pair.second > maxCount) {
                maxCount = pair.second;
                topic = pair.first;
            } else if (pair.second == maxCount && pair.first < topic) {
                topic = pair.first;
            }
        }
        
        bool isTopic = false;
        for (string t : topics) {
            if (t == topic) {
                isTopic = true;
                break;
            }
        }
        
        if (isTopic) {
            result.push_back(topic);
        } else {
            result.push_back("");
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot k)$, where $n$ is the number of posts, $m$ is the maximum number of words in a post, and $k$ is the number of topics.
> - **Space Complexity:** $O(n \cdot m)$, where $n$ is the number of posts and $m$ is the maximum number of words in a post.
> - **Why these complexities occur:** The brute force approach involves iterating over each post and each word in the post, which results in a time complexity of $O(n \cdot m \cdot k)$. The space complexity is $O(n \cdot m)$ because we need to store the frequency of each word in each post.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal approach involves using a hashmap to store the frequency of each word in each post.
- Then, iterate over the topics to find the topic that appears most frequently in the post.
- If there are multiple topics with the same highest frequency, the topic is the one that comes first alphabetically.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>

vector<string> findTopics(vector<string>& posts, vector<string>& topics) {
    vector<string> result;
    for (string post : posts) {
        map<string, int> wordCount;
        string word;
        for (char c : post) {
            if (c == ' ') {
                if (!word.empty()) {
                    wordCount[word]++;
                    word.clear();
                }
            } else {
                word += c;
            }
        }
        if (!word.empty()) {
            wordCount[word]++;
        }
        
        string topic;
        int maxCount = 0;
        for (auto& pair : wordCount) {
            if (pair.second > maxCount && find(topics.begin(), topics.end(), pair.first) != topics.end()) {
                maxCount = pair.second;
                topic = pair.first;
            } else if (pair.second == maxCount && pair.first < topic && find(topics.begin(), topics.end(), pair.first) != topics.end()) {
                topic = pair.first;
            }
        }
        
        if (maxCount > 0) {
            result.push_back(topic);
        } else {
            result.push_back("");
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot k)$, where $n$ is the number of posts, $m$ is the maximum number of words in a post, and $k$ is the number of topics.
> - **Space Complexity:** $O(n \cdot m)$, where $n$ is the number of posts and $m$ is the maximum number of words in a post.
> - **Optimality proof:** This approach is optimal because we need to iterate over each post and each word in the post to find the topic of each post.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: hashmap, iteration.
- Problem-solving patterns identified: finding the maximum frequency of a word in a post.
- Optimization techniques learned: using a hashmap to store the frequency of each word in each post.
- Similar problems to practice: finding the maximum frequency of a word in a text.

**Mistakes to Avoid:**
- Common implementation errors: not checking if a word is a topic before updating the topic.
- Edge cases to watch for: a post does not contain any words that are topics.
- Performance pitfalls: using a brute force approach that results in a high time complexity.
- Testing considerations: testing the function with different inputs, including edge cases.