## Design Search Autocomplete System
**Problem Link:** https://leetcode.com/problems/design-search-autocomplete-system/description

**Problem Statement:**
- Input format and constraints: The system will receive a list of sentences and their corresponding frequencies. The input will also include a search query to find the top 3 sentences that match the query.
- Expected output format: The system should return the top 3 sentences that match the search query, sorted by frequency and then lexicographically.
- Key requirements and edge cases to consider: The system should handle a large number of sentences and search queries efficiently. It should also handle cases where the search query is empty or does not match any sentences.
- Example test cases with explanations: 
    - Input: `["The quick brown fox jumps over the lazy dog", "The sun is shining"]`, Query: `"The"`
    - Output: `["The sun is shining", "The quick brown fox jumps over the lazy dog"]`
    - Explanation: The system returns the top 2 sentences that match the query `"The"`, sorted by frequency and then lexicographically.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: One possible approach is to iterate through all the sentences for each search query and check if the query is a prefix of the sentence.
- Step-by-step breakdown of the solution:
    1. Iterate through all the sentences.
    2. For each sentence, check if the search query is a prefix of the sentence.
    3. If the query is a prefix, add the sentence to a list of matching sentences.
    4. Sort the list of matching sentences by frequency and then lexicographically.
    5. Return the top 3 sentences from the sorted list.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it has a high time complexity due to the iteration through all the sentences for each search query.

```cpp
class AutocompleteSystem {
public:
    vector<string> sentences;
    vector<int> frequencies;
    unordered_map<string, vector<pair<int, string>>> prefixMap;

    AutocompleteSystem(vector<string>& sentences, vector<int>& times) {
        this->sentences = sentences;
        this->frequencies = times;
    }

    vector<string> input(char c) {
        if (c == '#') {
            // Add the sentence to the prefix map
            for (int i = 0; i < sentences.size(); i++) {
                string sentence = sentences[i];
                for (int j = 0; j < sentence.size(); j++) {
                    string prefix = sentence.substr(0, j + 1);
                    prefixMap[prefix].push_back({frequencies[i], sentence});
                }
            }
            return {};
        } else {
            // Search for sentences that match the query
            string query;
            for (auto& pair : prefixMap) {
                if (pair.first.size() == 1 && pair.first[0] == c) {
                    query = pair.first;
                    break;
                }
            }
            if (query.empty()) {
                return {};
            }
            vector<pair<int, string>> matchingSentences = prefixMap[query];
            sort(matchingSentences.begin(), matchingSentences.end(), [](const pair<int, string>& a, const pair<int, string>& b) {
                if (a.first == b.first) {
                    return a.second < b.second;
                }
                return a.first > b.first;
            });
            vector<string> result;
            for (int i = 0; i < min(3, (int)matchingSentences.size()); i++) {
                result.push_back(matchingSentences[i].second);
            }
            return result;
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the number of sentences and $m$ is the maximum length of a sentence.
> - **Space Complexity:** $O(n \cdot m)$ where $n$ is the number of sentences and $m$ is the maximum length of a sentence.
> - **Why these complexities occur:** The brute force approach has a high time complexity due to the iteration through all the sentences for each search query. The space complexity is also high due to the storage of all the sentences and their prefixes.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a `Trie` data structure to store the sentences and their frequencies. This allows us to efficiently search for sentences that match the query.
- Detailed breakdown of the approach:
    1. Create a `Trie` data structure to store the sentences and their frequencies.
    2. For each sentence, add it to the `Trie` and update the frequency of the sentence.
    3. For each search query, start at the root of the `Trie` and traverse the `Trie` based on the query.
    4. At each node, retrieve the top 3 sentences that match the query and return them.
- Proof of optimality: The `Trie` data structure allows us to efficiently search for sentences that match the query in $O(m)$ time where $m$ is the length of the query.

```cpp
class AutocompleteSystem {
public:
    struct TrieNode {
        unordered_map<char, TrieNode*> children;
        vector<pair<int, string>> sentences;
    };

    TrieNode* root;
    string query;

    AutocompleteSystem(vector<string>& sentences, vector<int>& times) {
        root = new TrieNode();
        for (int i = 0; i < sentences.size(); i++) {
            string sentence = sentences[i];
            int time = times[i];
            TrieNode* node = root;
            for (char c : sentence) {
                if (!node->children.count(c)) {
                    node->children[c] = new TrieNode();
                }
                node = node->children[c];
            }
            node->sentences.push_back({time, sentence});
        }
    }

    vector<string> input(char c) {
        if (c == '#') {
            TrieNode* node = root;
            for (char cc : query) {
                node = node->children[cc];
            }
            sort(node->sentences.begin(), node->sentences.end(), [](const pair<int, string>& a, const pair<int, string>& b) {
                if (a.first == b.first) {
                    return a.second < b.second;
                }
                return a.first > b.first;
            });
            vector<string> result;
            for (int i = 0; i < min(3, (int)node->sentences.size()); i++) {
                result.push_back(node->sentences[i].second);
            }
            query.clear();
            return result;
        } else {
            query += c;
            TrieNode* node = root;
            for (char cc : query) {
                if (!node->children.count(cc)) {
                    return {};
                }
                node = node->children[cc];
            }
            sort(node->sentences.begin(), node->sentences.end(), [](const pair<int, string>& a, const pair<int, string>& b) {
                if (a.first == b.first) {
                    return a.second < b.second;
                }
                return a.first > b.first;
            });
            vector<string> result;
            for (int i = 0; i < min(3, (int)node->sentences.size()); i++) {
                result.push_back(node->sentences[i].second);
            }
            return result;
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m)$ where $m$ is the length of the query.
> - **Space Complexity:** $O(n \cdot m)$ where $n$ is the number of sentences and $m$ is the maximum length of a sentence.
> - **Optimality proof:** The `Trie` data structure allows us to efficiently search for sentences that match the query in $O(m)$ time where $m$ is the length of the query.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: `Trie` data structure, efficient search and retrieval of sentences that match a query.
- Problem-solving patterns identified: Using a `Trie` data structure to efficiently store and retrieve sentences based on prefixes.
- Optimization techniques learned: Using a `Trie` data structure to reduce the time complexity of searching for sentences that match a query.
- Similar problems to practice: Implementing a `Trie` data structure to solve other problems related to efficient search and retrieval of strings.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases such as empty queries or sentences.
- Edge cases to watch for: Handling cases where the query is empty or does not match any sentences.
- Performance pitfalls: Not using a `Trie` data structure to efficiently store and retrieve sentences based on prefixes.
- Testing considerations: Testing the implementation with different inputs and edge cases to ensure correctness and efficiency.