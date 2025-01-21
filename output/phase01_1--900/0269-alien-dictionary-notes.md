## Alien Dictionary
**Problem Link:** https://leetcode.com/problems/alien-dictionary/description

**Problem Statement:**
- Input format and constraints: The input is a list of strings `words`, representing a list of words in an alien dictionary.
- Expected output format: The output should be a string representing the lexicographical order of the alien dictionary.
- Key requirements and edge cases to consider: The input list may contain duplicate words, and the list may be empty. If the input list is invalid (i.e., it cannot form a valid lexicographical order), the output should be an empty string.
- Example test cases with explanations:
  - Example 1: `words = ["wrt","wrf","er","ett","rftt"]`, Output: `"wertf"`
  - Example 2: `words = ["z","x"]`, Output: `"zx"`
  - Example 3: `words = ["z","x","z"]`, Output: `""` (invalid input)

---

### Brute Force Approach
**Explanation:**
- Initial thought process: We can compare each pair of words in the input list to determine the lexicographical order.
- Step-by-step breakdown of the solution:
  1. Create a graph with each character as a node.
  2. Iterate over each pair of words in the input list.
  3. For each pair of words, compare the characters at each position.
  4. If a character in the first word is different from the character at the same position in the second word, add an edge to the graph from the character in the first word to the character in the second word.
  5. If a cycle is detected in the graph, the input list is invalid.
  6. Otherwise, perform a topological sort on the graph to determine the lexicographical order.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, as it directly compares each pair of words to determine the lexicographical order.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <unordered_set>

using namespace std;

bool isInvalid(const vector<string>& words) {
    for (int i = 0; i < words.size() - 1; i++) {
        if (words[i].size() > words[i + 1].size() && words[i].substr(0, words[i + 1].size()) == words[i + 1]) {
            return true;
        }
    }
    return false;
}

string alienOrder(vector<string>& words) {
    if (isInvalid(words)) {
        return "";
    }

    unordered_map<char, unordered_set<char>> graph;
    unordered_map<char, int> indegree;

    for (const string& word : words) {
        for (char c : word) {
            indegree[c] = 0;
        }
    }

    for (int i = 0; i < words.size() - 1; i++) {
        for (int j = 0; j < min(words[i].size(), words[i + 1].size()); j++) {
            if (words[i][j] != words[i + 1][j]) {
                if (graph[words[i][j]].find(words[i + 1][j]) == graph[words[i][j]].end()) {
                    graph[words[i][j]].insert(words[i + 1][j]);
                    indegree[words[i + 1][j]]++;
                }
                break;
            }
        }
    }

    string result;
    queue<char> q;
    for (const auto& pair : indegree) {
        if (pair.second == 0) {
            q.push(pair.first);
        }
    }

    while (!q.empty()) {
        char c = q.front();
        q.pop();
        result += c;
        for (const auto& neighbor : graph[c]) {
            indegree[neighbor]--;
            if (indegree[neighbor] == 0) {
                q.push(neighbor);
            }
        }
    }

    if (result.size() != indegree.size()) {
        return "";
    }

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(N \cdot M + C)$, where $N$ is the number of words, $M$ is the maximum length of a word, and $C$ is the number of unique characters. The reason is that we iterate over each pair of words to build the graph, and then perform a topological sort on the graph.
> - **Space Complexity:** $O(C + N \cdot M)$, where $C$ is the number of unique characters and $N \cdot M$ is the total number of characters in all words. The reason is that we need to store the graph and the indegree of each character.
> - **Why these complexities occur:** The time complexity occurs because we need to iterate over each pair of words to build the graph, and then perform a topological sort on the graph. The space complexity occurs because we need to store the graph and the indegree of each character.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: The optimal solution is similar to the brute force approach, but with some optimizations.
- Detailed breakdown of the approach:
  1. Create a graph with each character as a node.
  2. Iterate over each pair of words in the input list.
  3. For each pair of words, compare the characters at each position.
  4. If a character in the first word is different from the character at the same position in the second word, add an edge to the graph from the character in the first word to the character in the second word.
  5. If a cycle is detected in the graph, the input list is invalid.
  6. Otherwise, perform a topological sort on the graph to determine the lexicographical order.
- Why further optimization is impossible: The optimal solution has a time complexity of $O(N \cdot M + C)$, which is the minimum time complexity required to solve the problem.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <unordered_set>

using namespace std;

bool isInvalid(const vector<string>& words) {
    for (int i = 0; i < words.size() - 1; i++) {
        if (words[i].size() > words[i + 1].size() && words[i].substr(0, words[i + 1].size()) == words[i + 1]) {
            return true;
        }
    }
    return false;
}

string alienOrder(vector<string>& words) {
    if (isInvalid(words)) {
        return "";
    }

    unordered_map<char, unordered_set<char>> graph;
    unordered_map<char, int> indegree;

    for (const string& word : words) {
        for (char c : word) {
            indegree[c] = 0;
        }
    }

    for (int i = 0; i < words.size() - 1; i++) {
        for (int j = 0; j < min(words[i].size(), words[i + 1].size()); j++) {
            if (words[i][j] != words[i + 1][j]) {
                if (graph[words[i][j]].find(words[i + 1][j]) == graph[words[i][j]].end()) {
                    graph[words[i][j]].insert(words[i + 1][j]);
                    indegree[words[i + 1][j]]++;
                }
                break;
            }
        }
    }

    string result;
    queue<char> q;
    for (const auto& pair : indegree) {
        if (pair.second == 0) {
            q.push(pair.first);
        }
    }

    while (!q.empty()) {
        char c = q.front();
        q.pop();
        result += c;
        for (const auto& neighbor : graph[c]) {
            indegree[neighbor]--;
            if (indegree[neighbor] == 0) {
                q.push(neighbor);
            }
        }
    }

    if (result.size() != indegree.size()) {
        return "";
    }

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(N \cdot M + C)$, where $N$ is the number of words, $M$ is the maximum length of a word, and $C$ is the number of unique characters. The reason is that we iterate over each pair of words to build the graph, and then perform a topological sort on the graph.
> - **Space Complexity:** $O(C + N \cdot M)$, where $C$ is the number of unique characters and $N \cdot M$ is the total number of characters in all words. The reason is that we need to store the graph and the indegree of each character.
> - **Optimality proof:** The optimal solution has a time complexity of $O(N \cdot M + C)$, which is the minimum time complexity required to solve the problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Topological sort, graph construction, and cycle detection.
- Problem-solving patterns identified: The problem can be solved by constructing a graph and performing a topological sort on the graph.
- Optimization techniques learned: The optimal solution uses a queue to perform the topological sort, which reduces the time complexity.
- Similar problems to practice: Other problems that involve constructing a graph and performing a topological sort, such as course scheduling and package dependencies.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for invalid input, not handling cycle detection correctly, and not implementing the topological sort correctly.
- Edge cases to watch for: Empty input list, duplicate words, and words with different lengths.
- Performance pitfalls: Using an inefficient data structure, such as a linked list, to store the graph and indegree of each character.
- Testing considerations: Testing the solution with different input cases, including invalid input, to ensure that the solution works correctly.