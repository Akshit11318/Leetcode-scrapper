## Search Suggestions System

**Problem Link:** https://leetcode.com/problems/search-suggestions-system/description

**Problem Statement:**
- Given a list of strings `products` and a string `searchWord`, return a list of lists, where each sublist contains the top 3 most relevant product suggestions based on the given search word.
- Input format: `products` is a list of strings, and `searchWord` is a string.
- Expected output format: A list of lists, where each sublist contains at most 3 product suggestions.
- Key requirements and edge cases to consider:
  - Handle cases where the search word is empty or contains only spaces.
  - If there are less than 3 matching products, return all matching products.
- Example test cases with explanations:
  - Input: `products = ["mobile","mouse","moneypot","monitor","mousepad"]`, `searchWord = "mouse"`
  - Output: `[["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]`
  - Explanation: The output is a list of lists, where each sublist contains the top 3 most relevant product suggestions based on the given search word.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible prefixes of the `searchWord` and for each prefix, iterate through the `products` list to find matching products.
- Step-by-step breakdown of the solution:
  1. Initialize an empty list to store the result.
  2. For each character in the `searchWord`, generate a prefix.
  3. For each prefix, iterate through the `products` list to find matching products.
  4. For each matching product, add it to the result list.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it may not be efficient for large inputs.

```cpp
vector<vector<string>> suggestedProducts(vector<string>& products, string searchWord) {
    vector<vector<string>> result;
    for (int i = 0; i < searchWord.size(); i++) {
        string prefix = searchWord.substr(0, i + 1);
        vector<string> suggestions;
        for (string product : products) {
            if (product.find(prefix) == 0) {
                suggestions.push_back(product);
            }
        }
        sort(suggestions.begin(), suggestions.end());
        vector<string> top3;
        for (int j = 0; j < min(3, (int)suggestions.size()); j++) {
            top3.push_back(suggestions[j]);
        }
        result.push_back(top3);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot log(m))$, where $n$ is the length of the `searchWord` and $m$ is the number of products.
> - **Space Complexity:** $O(n \cdot m)$, where $n$ is the length of the `searchWord` and $m$ is the number of products.
> - **Why these complexities occur:** The time complexity occurs because we are iterating through the `products` list for each prefix of the `searchWord`, and sorting the matching products. The space complexity occurs because we are storing the result in a list of lists.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a Trie data structure to store the products, and then traverse the Trie to find matching products for each prefix of the `searchWord`.
- Detailed breakdown of the approach:
  1. Create a Trie and insert all products into the Trie.
  2. For each character in the `searchWord`, traverse the Trie to find matching products.
  3. For each matching product, add it to the result list.
- Proof of optimality: This approach is optimal because it reduces the time complexity to $O(n \cdot m)$, where $n$ is the length of the `searchWord` and $m$ is the number of products.

```cpp
class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    vector<string> products;
};

vector<vector<string>> suggestedProducts(vector<string>& products, string searchWord) {
    TrieNode* root = new TrieNode();
    for (string product : products) {
        TrieNode* node = root;
        for (char c : product) {
            if (node->children.find(c) == node->children.end()) {
                node->children[c] = new TrieNode();
            }
            node = node->children[c];
            node->products.push_back(product);
        }
    }
    vector<vector<string>> result;
    TrieNode* node = root;
    for (char c : searchWord) {
        if (node->children.find(c) == node->children.end()) {
            break;
        }
        node = node->children[c];
        vector<string> suggestions;
        for (string product : node->products) {
            suggestions.push_back(product);
        }
        sort(suggestions.begin(), suggestions.end());
        vector<string> top3;
        for (int j = 0; j < min(3, (int)suggestions.size()); j++) {
            top3.push_back(suggestions[j]);
        }
        result.push_back(top3);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the length of the `searchWord` and $m$ is the number of products.
> - **Space Complexity:** $O(m)$, where $m$ is the number of products.
> - **Optimality proof:** This approach is optimal because it reduces the time complexity to $O(n \cdot m)$, and it uses a Trie data structure to efficiently store and retrieve matching products.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Trie data structure, string matching, and sorting.
- Problem-solving patterns identified: Using a Trie to efficiently store and retrieve matching products.
- Optimization techniques learned: Reducing the time complexity by using a Trie data structure.
- Similar problems to practice: Other problems involving string matching and Trie data structures.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as an empty `searchWord` or an empty `products` list.
- Edge cases to watch for: Handling cases where the `searchWord` is longer than the length of the `products` list.
- Performance pitfalls: Using a brute force approach that has a high time complexity.
- Testing considerations: Testing the solution with different inputs, such as an empty `searchWord` or an empty `products` list.