## Maximum XOR with an Element from Array

**Problem Link:** https://leetcode.com/problems/maximum-xor-with-an-element-from-array/description

**Problem Statement:**
- Input format and constraints: Given an array `nums` and an integer `queries`, return an array `ans` where `ans[i]` is the maximum XOR of `queries[i]` with any element in `nums`.
- Expected output format: An array of integers representing the maximum XOR values for each query.
- Key requirements and edge cases to consider: The input array `nums` can be empty, and the `queries` array can contain duplicate elements.
- Example test cases with explanations: 
  - For `nums = [0, 1, 2, 3, 4]` and `queries = [3, 10, 21, 42, 84]`, the output should be `[3, 7, 7, 7, 7]`.
  - For `nums = []` and `queries = [1, 2, 3]`, the output should be `[-1, -1, -1]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The simplest approach to solve this problem is to iterate over each query and calculate the XOR with every element in the `nums` array.
- Step-by-step breakdown of the solution:
  1. Initialize an empty array `ans` to store the maximum XOR values for each query.
  2. Iterate over each query in the `queries` array.
  3. For each query, iterate over every element in the `nums` array.
  4. Calculate the XOR of the current query and the current element in `nums`.
  5. Update the maximum XOR value for the current query if the calculated XOR is greater.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it has a high time complexity due to the nested loops.

```cpp
vector<int> maximizeXor(vector<int>& nums, vector<int>& queries) {
    vector<int> ans;
    for (int query : queries) {
        int maxXor = -1;
        for (int num : nums) {
            int xorVal = query ^ num;
            maxXor = max(maxXor, xorVal);
        }
        ans.push_back(maxXor);
    }
    return ans;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the number of queries and $m$ is the number of elements in `nums`. This is because we have nested loops iterating over `queries` and `nums`.
> - **Space Complexity:** $O(n)$ for storing the maximum XOR values for each query in the `ans` array.
> - **Why these complexities occur:** The brute force approach has high time complexity due to the nested loops, and the space complexity is linear because we need to store the maximum XOR values for each query.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a Trie data structure to store the binary representation of the elements in `nums`. This allows us to efficiently find the maximum XOR for each query by traversing the Trie.
- Detailed breakdown of the approach:
  1. Create a Trie data structure and insert the binary representation of each element in `nums`.
  2. Iterate over each query in the `queries` array.
  3. For each query, traverse the Trie to find the maximum XOR value.
  4. Update the maximum XOR value for the current query if a greater XOR value is found.
- Proof of optimality: The Trie data structure allows us to reduce the time complexity from $O(n \cdot m)$ to $O(n \cdot b)$ where $b$ is the number of bits in the binary representation of the elements in `nums`. This is because we can efficiently traverse the Trie to find the maximum XOR value for each query.

```cpp
struct TrieNode {
    TrieNode* children[2];
    TrieNode() {
        children[0] = children[1] = nullptr;
    }
};

void insert(TrieNode* root, int num) {
    TrieNode* node = root;
    for (int i = 31; i >= 0; i--) {
        int bit = (num >> i) & 1;
        if (!node->children[bit]) {
            node->children[bit] = new TrieNode();
        }
        node = node->children[bit];
    }
}

int query(TrieNode* root, int num) {
    TrieNode* node = root;
    int result = 0;
    for (int i = 31; i >= 0; i--) {
        int bit = (num >> i) & 1;
        if (node->children[1 - bit]) {
            result |= (1 << i);
            node = node->children[1 - bit];
        } else {
            node = node->children[bit];
        }
    }
    return result;
}

vector<int> maximizeXor(vector<int>& nums, vector<int>& queries) {
    TrieNode* root = new TrieNode();
    for (int num : nums) {
        insert(root, num);
    }
    vector<int> ans;
    for (int query : queries) {
        ans.push_back(query(root, query));
    }
    return ans;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot b)$ where $n$ is the number of queries and $b$ is the number of bits in the binary representation of the elements in `nums`. This is because we traverse the Trie for each query.
> - **Space Complexity:** $O(m \cdot b)$ for storing the Trie data structure where $m$ is the number of elements in `nums`.
> - **Optimality proof:** The Trie data structure allows us to efficiently find the maximum XOR value for each query, reducing the time complexity from $O(n \cdot m)$ to $O(n \cdot b)$. This is the optimal solution because we cannot do better than traversing the Trie for each query.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Trie data structure, XOR operation, and bit manipulation.
- Problem-solving patterns identified: Using a Trie data structure to efficiently find the maximum XOR value for each query.
- Optimization techniques learned: Reducing the time complexity by using a Trie data structure.
- Similar problems to practice: Other problems that involve finding the maximum XOR value or using a Trie data structure.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as an empty `nums` array or duplicate elements in `queries`.
- Edge cases to watch for: Handling queries that are not present in `nums`.
- Performance pitfalls: Not using a Trie data structure, leading to a high time complexity.
- Testing considerations: Testing the solution with different input sizes and edge cases to ensure correctness and performance.