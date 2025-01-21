## Map Sum Pairs
**Problem Link:** https://leetcode.com/problems/map-sum-pairs/description

**Problem Statement:**
- Input format and constraints: The problem involves implementing a `MapSum` class that supports two operations: `insert` and `sum`. The `insert` operation takes a `string` key and an `int` value as input, and the `sum` operation takes a `string` prefix as input and returns the sum of all values associated with keys that start with the given prefix. The constraints are that the `insert` operation should be performed in O(1) time complexity, and the `sum` operation should be performed in O(1) time complexity as well.
- Expected output format: The `sum` operation should return the sum of all values associated with keys that start with the given prefix.
- Key requirements and edge cases to consider: The `insert` operation should update the sum of all values associated with keys that start with the prefix of the inserted key, and the `sum` operation should return 0 if no keys start with the given prefix.
- Example test cases with explanations:
  - `MapSum mapSum = new MapSum();`
  - `mapSum.insert("apple", 3);`
  - `mapSum.sum("ap"); // Output: 3`
  - `mapSum.insert("app", 2);`
  - `mapSum.sum("ap"); // Output: 5`

---

### Brute Force Approach
**Explanation:**
- Initial thought process: The brute force approach involves storing all the key-value pairs in a `map` and then iterating over the map to find the sum of all values associated with keys that start with the given prefix.
- Step-by-step breakdown of the solution:
  1. Create a `map` to store the key-value pairs.
  2. Implement the `insert` operation by inserting the key-value pair into the map.
  3. Implement the `sum` operation by iterating over the map and summing up the values associated with keys that start with the given prefix.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it has a high time complexity for the `sum` operation.

```cpp
class MapSum {
public:
    unordered_map<string, int> map;
    void insert(string key, int val) {
        map[key] = val;
    }
    int sum(string prefix) {
        int sum = 0;
        for (auto& pair : map) {
            if (pair.first.find(prefix) == 0) {
                sum += pair.second;
            }
        }
        return sum;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** O(n) for the `sum` operation, where n is the number of key-value pairs in the map, because we are iterating over the map to find the sum.
> - **Space Complexity:** O(n) for storing the key-value pairs in the map.
> - **Why these complexities occur:** The time complexity of the `sum` operation is high because we are iterating over the map, and the space complexity is high because we are storing all the key-value pairs in the map.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can use a `Trie` data structure to store the key-value pairs, which allows us to efficiently find the sum of all values associated with keys that start with the given prefix.
- Detailed breakdown of the approach:
  1. Create a `Trie` data structure to store the key-value pairs.
  2. Implement the `insert` operation by inserting the key-value pair into the Trie.
  3. Implement the `sum` operation by traversing the Trie from the root node to the node that corresponds to the last character of the prefix, and then summing up the values associated with all nodes in the subtree rooted at that node.
- Proof of optimality: This approach has a time complexity of O(1) for both the `insert` and `sum` operations, which is optimal.

```cpp
class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    int sum;
    TrieNode() : sum(0) {}
};

class MapSum {
public:
    unordered_map<string, int> map;
    TrieNode* root;
    MapSum() : root(new TrieNode()) {}
    void insert(string key, int val) {
        int delta = val - (map.count(key) ? map[key] : 0);
        map[key] = val;
        TrieNode* node = root;
        for (char c : key) {
            if (!node->children.count(c)) {
                node->children[c] = new TrieNode();
            }
            node = node->children[c];
            node->sum += delta;
        }
    }
    int sum(string prefix) {
        TrieNode* node = root;
        for (char c : prefix) {
            if (!node->children.count(c)) {
                return 0;
            }
            node = node->children[c];
        }
        return node->sum;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** O(1) for both the `insert` and `sum` operations, because we are using a Trie data structure to efficiently find the sum.
> - **Space Complexity:** O(n) for storing the key-value pairs in the Trie.
> - **Optimality proof:** This approach is optimal because it has a time complexity of O(1) for both operations, which is the best possible time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Trie data structure, prefix sum.
- Problem-solving patterns identified: Using a Trie data structure to efficiently find the sum of all values associated with keys that start with the given prefix.
- Optimization techniques learned: Using a Trie data structure to reduce the time complexity of the `sum` operation.
- Similar problems to practice: Implementing a Trie data structure to solve other problems, such as autocomplete or spell-checking.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as an empty prefix or a key that is not in the map.
- Edge cases to watch for: An empty prefix, a key that is not in the map, or a prefix that is longer than any key in the map.
- Performance pitfalls: Using a brute force approach that has a high time complexity for the `sum` operation.
- Testing considerations: Testing the implementation with different inputs, such as an empty prefix, a key that is not in the map, or a prefix that is longer than any key in the map.