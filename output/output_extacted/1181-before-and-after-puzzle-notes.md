## Before and After Puzzle

**Problem Link:** https://leetcode.com/problems/before-and-after-puzzle/description

**Problem Statement:**
- Input: `phrases` array of strings, where each string represents a phrase.
- Constraints: `1 <= phrases.length <= 4` and `1 <= phrases[i].length <= 6`.
- Expected Output: A list of strings representing the before-and-after puzzles.
- Key requirements:
  - Each phrase must be used exactly once.
  - The last word of one phrase must be the first word of another phrase.
- Edge cases:
  - Empty input array.
  - Single phrase in the input array.

**Example Test Cases:**
- `phrases = ["writing code","code rocks"]`
  - Output: `["writing code rocks"]`
- `phrases = ["mission go","go jump","jump say","say hi","hi if"]`
  - Output: `["mission go jump say hi if"]`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all permutations of phrases and check if the last word of one phrase matches the first word of another phrase.
- Step-by-step breakdown:
  1. Generate all permutations of phrases using a recursive function or `next_permutation` algorithm.
  2. For each permutation, iterate through the phrases and check if the last word of one phrase matches the first word of the next phrase.
  3. If a match is found, add the concatenated phrase to the result list.
- Why this approach comes to mind first: It's a straightforward way to generate all possible combinations of phrases and check for the required condition.

```cpp
#include <vector>
#include <string>
#include <algorithm>

std::vector<std::string> beforeAndAfterPuzzles(std::vector<std::string>& phrases) {
    std::vector<std::string> result;
    std::sort(phrases.begin(), phrases.end());
    do {
        std::string puzzle;
        for (int i = 0; i < phrases.size(); i++) {
            if (i > 0 && phrases[i - 1].substr(phrases[i - 1].find_last_of(' ') + 1) != phrases[i].substr(0, phrases[i].find_first_of(' '))) {
                break;
            }
            puzzle += phrases[i] + " ";
        }
        if (puzzle.size() > 0 && puzzle.size() == phrases.size() * phrases[0].size() + phrases.size() - 1) {
            puzzle.pop_back();
            result.push_back(puzzle);
        }
    } while (std::next_permutation(phrases.begin(), phrases.end()));
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n! \cdot m)$, where $n$ is the number of phrases and $m$ is the maximum length of a phrase. This is because we generate all permutations of phrases and iterate through each permutation to check for the required condition.
> - **Space Complexity:** $O(n \cdot m)$, where $n$ is the number of phrases and $m$ is the maximum length of a phrase. This is because we store the result list and the permutation of phrases.
> - **Why these complexities occur:** The time complexity occurs because we generate all permutations of phrases, and for each permutation, we iterate through the phrases to check for the required condition. The space complexity occurs because we store the result list and the permutation of phrases.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Use a graph to represent the phrases and their connections.
- Detailed breakdown:
  1. Create a graph where each phrase is a node, and two nodes are connected if the last word of one phrase matches the first word of another phrase.
  2. Use a depth-first search (DFS) algorithm to traverse the graph and find all possible paths that represent the before-and-after puzzles.
- Proof of optimality: This approach is optimal because it avoids generating all permutations of phrases and only explores the relevant connections between phrases.

```cpp
#include <vector>
#include <string>
#include <unordered_map>
#include <unordered_set>

std::vector<std::string> beforeAndAfterPuzzles(std::vector<std::string>& phrases) {
    std::unordered_map<std::string, std::vector<std::string>> graph;
    for (const auto& phrase : phrases) {
        std::string firstWord = phrase.substr(0, phrase.find_first_of(' '));
        std::string lastWord = phrase.substr(phrase.find_last_of(' ') + 1);
        graph[lastWord].push_back(phrase);
    }
    std::unordered_set<std::string> visited;
    std::vector<std::string> result;
    for (const auto& phrase : phrases) {
        std::string firstWord = phrase.substr(0, phrase.find_first_of(' '));
        std::string puzzle = phrase;
        visited.insert(phrase);
        dfs(graph, visited, result, puzzle, firstWord);
        visited.clear();
    }
    return result;
}

void dfs(std::unordered_map<std::string, std::vector<std::string>>& graph, std::unordered_set<std::string>& visited, std::vector<std::string>& result, std::string& puzzle, std::string& lastWord) {
    if (graph.find(lastWord) == graph.end()) {
        return;
    }
    for (const auto& nextPhrase : graph[lastWord]) {
        if (visited.find(nextPhrase) != visited.end()) {
            continue;
        }
        visited.insert(nextPhrase);
        puzzle += " " + nextPhrase.substr(nextPhrase.find_first_of(' ') + 1);
        if (visited.size() == graph.size()) {
            result.push_back(puzzle);
        }
        dfs(graph, visited, result, puzzle, nextPhrase.substr(nextPhrase.find_last_of(' ') + 1));
        visited.erase(nextPhrase);
        puzzle = puzzle.substr(0, puzzle.size() - (nextPhrase.size() - nextPhrase.find_first_of(' ')));
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of phrases and $m$ is the maximum length of a phrase. This is because we create a graph and use DFS to traverse the graph.
> - **Space Complexity:** $O(n \cdot m)$, where $n$ is the number of phrases and $m$ is the maximum length of a phrase. This is because we store the graph and the result list.
> - **Optimality proof:** This approach is optimal because it avoids generating all permutations of phrases and only explores the relevant connections between phrases.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: Graphs, depth-first search, and permutations.
- Problem-solving patterns: Using graphs to represent connections between objects and using DFS to traverse the graph.
- Optimization techniques: Avoiding unnecessary computations by using a graph and DFS.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as an empty input array or a single phrase in the input array.
- Edge cases to watch for: Empty input array, single phrase in the input array, and phrases with no connections.
- Performance pitfalls: Generating all permutations of phrases and iterating through each permutation to check for the required condition.
- Testing considerations: Test the solution with different input sizes, including edge cases, and verify the correctness of the output.