## Top K Frequent Words

**Problem Link:** https://leetcode.com/problems/top-k-frequent-words/description

**Problem Statement:**
- Input: A list of words `words` and an integer `k`.
- Constraints: `1 <= k <= words.length <= 10^5` and `1 <= words[i].length <= 10^5`.
- Expected output: The `k` most frequent words in descending order of frequency and then lexicographically.
- Key requirements: The solution should handle cases where multiple words have the same frequency, and the output should be sorted first by frequency and then by lexicographical order.
- Example test cases:
  - Input: `words = ["i", "love", "leetcode", "i", "love", "coding"]`, `k = 2`
  - Output: `["i", "love"]`
  - Explanation: The words "i" and "love" appear twice, which is more than any other word. They are also in lexicographical order.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find the `k` most frequent words, we can start by counting the frequency of each word in the list.
- Step-by-step breakdown:
  1. Create a `map` to store the frequency of each word.
  2. Iterate through the list of words and update the frequency count for each word in the map.
  3. Create a list of pairs, where each pair contains a word and its frequency.
  4. Sort the list of pairs based on the frequency (in descending order) and then the word itself (in ascending order).
  5. Return the top `k` words from the sorted list.

```cpp
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

vector<string> topKFrequent(vector<string>& words, int k) {
    map<string, int> frequency;
    for (const auto& word : words) {
        frequency[word]++;
    }

    vector<pair<string, int>> wordFrequency;
    for (const auto& pair : frequency) {
        wordFrequency.push_back(pair);
    }

    sort(wordFrequency.begin(), wordFrequency.end(),
        [](const pair<string, int>& a, const pair<string, int>& b) {
            if (a.second == b.second) {
                return a.first < b.first;
            }
            return a.second > b.second;
        });

    vector<string> result;
    for (int i = 0; i < k; i++) {
        result.push_back(wordFrequency[i].first);
    }

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of unique words. This is due to the sorting operation.
> - **Space Complexity:** $O(n)$, for storing the frequency of each word and the sorted list of words.
> - **Why these complexities occur:** The time complexity is dominated by the sorting operation, which has a time complexity of $O(n \log n)$. The space complexity is due to the storage required for the frequency map and the sorted list of words.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: We can use a `priority_queue` to efficiently find the top `k` frequent words.
- Detailed breakdown:
  1. Create a `map` to store the frequency of each word.
  2. Iterate through the list of words and update the frequency count for each word in the map.
  3. Create a `priority_queue` of pairs, where each pair contains a word and its frequency. The priority queue is ordered based on the frequency (in descending order) and then the word itself (in ascending order).
  4. Push all word-frequency pairs into the priority queue.
  5. Pop the top `k` elements from the priority queue and return them as the result.

```cpp
#include <iostream>
#include <vector>
#include <map>
#include <queue>

using namespace std;

struct Compare {
    bool operator()(const pair<int, string>& a, const pair<int, string>& b) {
        if (a.first == b.first) {
            return a.second > b.second;
        }
        return a.first < b.first;
    }
};

vector<string> topKFrequent(vector<string>& words, int k) {
    map<string, int> frequency;
    for (const auto& word : words) {
        frequency[word]++;
    }

    priority_queue<pair<int, string>, vector<pair<int, string>>, Compare> pq;
    for (const auto& pair : frequency) {
        pq.push({pair.second, pair.first});
    }

    vector<string> result;
    for (int i = 0; i < k; i++) {
        result.push_back(pq.top().second);
        pq.pop();
    }

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log k)$, where $n$ is the total number of words. This is because we push $n$ elements into the priority queue, and each push operation takes $O(\log k)$ time.
> - **Space Complexity:** $O(n)$, for storing the frequency of each word and the priority queue.
> - **Optimality proof:** This solution is optimal because it uses a priority queue to efficiently find the top `k` frequent words, which reduces the time complexity from $O(n \log n)$ to $O(n \log k)$.