## Shortest Word Distance
**Problem Link:** https://leetcode.com/problems/shortest-word-distance/description

**Problem Statement:**
- Input format and constraints: Given a list of words and two words `word1` and `word2` that exist in the list, find the shortest distance between these two words.
- Expected output format: The minimum distance between `word1` and `word2` in the list.
- Key requirements and edge cases to consider: 
    - The list of words is not empty.
    - `word1` and `word2` are distinct.
    - `word1` and `word2` exist in the list.
- Example test cases with explanations:
    - Input: `words = ["practice", "makes", "perfect", "coding", "makes"]`, `word1 = "coding"`, `word2 = "practice"`. Output: `3`.
    - Input: `words = ["practice", "makes", "perfect", "coding", "makes"]`, `word1 = "makes"`, `word2 = "coding"`. Output: `1`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Iterate through the list to find all occurrences of `word1` and `word2`, then calculate the distance between each pair of occurrences.
- Step-by-step breakdown of the solution:
    1. Create lists to store indices of `word1` and `word2`.
    2. Iterate through the list of words to find indices of `word1` and `word2`.
    3. For each index of `word1`, calculate the distance to the nearest index of `word2`.
    4. Keep track of the minimum distance found.
- Why this approach comes to mind first: It directly addresses the problem by considering all possible pairs of occurrences of `word1` and `word2`.

```cpp
vector<int> findWord1(const vector<string>& words, const string& word1) {
    vector<int> indices;
    for (int i = 0; i < words.size(); ++i) {
        if (words[i] == word1) {
            indices.push_back(i);
        }
    }
    return indices;
}

vector<int> findWord2(const vector<string>& words, const string& word2) {
    vector<int> indices;
    for (int i = 0; i < words.size(); ++i) {
        if (words[i] == word2) {
            indices.push_back(i);
        }
    }
    return indices;
}

int shortestDistance(vector<string>& words, string word1, string word2) {
    vector<int> indices1 = findWord1(words, word1);
    vector<int> indices2 = findWord2(words, word2);
    int minDistance = INT_MAX;
    for (int i : indices1) {
        for (int j : indices2) {
            if (i != j) { // Ensure we're not comparing the same index
                minDistance = min(minDistance, abs(i - j));
            }
        }
    }
    return minDistance;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ where $n$ is the length of the `words` list, because in the worst case, we're iterating through all pairs of indices.
> - **Space Complexity:** $O(n)$ for storing the indices of `word1` and `word2`.
> - **Why these complexities occur:** The brute force approach involves nested iterations over the list of indices for both words, leading to quadratic time complexity. The space complexity is linear because we store all indices of both words.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Instead of storing all indices and then comparing, we can iterate through the list once and keep track of the most recent indices of `word1` and `word2`.
- Detailed breakdown of the approach:
    1. Initialize variables to store the last seen indices of `word1` and `word2`.
    2. Initialize a variable to store the minimum distance.
    3. Iterate through the list of words. If the current word is `word1`, update its last seen index and calculate the distance to the last seen index of `word2`. If the current word is `word2`, update its last seen index and calculate the distance to the last seen index of `word1`.
    4. Update the minimum distance if a smaller distance is found.
- Proof of optimality: This approach ensures we consider all relevant pairs of occurrences of `word1` and `word2` in a single pass through the list, minimizing both time and space complexity.

```cpp
int shortestDistance(vector<string>& words, string word1, string word2) {
    int last1 = -1, last2 = -1;
    int minDistance = INT_MAX;
    for (int i = 0; i < words.size(); ++i) {
        if (words[i] == word1) {
            if (last2 != -1) {
                minDistance = min(minDistance, i - last2);
            }
            last1 = i;
        } else if (words[i] == word2) {
            if (last1 != -1) {
                minDistance = min(minDistance, i - last1);
            }
            last2 = i;
        }
    }
    return minDistance;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the length of the `words` list, because we make a single pass through the list.
> - **Space Complexity:** $O(1)$, as we use a constant amount of space to store the last seen indices and the minimum distance.
> - **Optimality proof:** This approach is optimal because it minimizes the number of operations required to find the shortest distance between `word1` and `word2` by only considering the most recent occurrences of each word, thus achieving linear time complexity and constant space complexity.