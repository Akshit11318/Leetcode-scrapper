## Maximum XOR Score Subarray Queries
**Problem Link:** https://leetcode.com/problems/maximum-xor-score-subarray-queries/description

**Problem Statement:**
- Input format and constraints: The problem takes a binary array `arr` and a list of queries `queries` as input, where each query is a subarray range `[i, j]`.
- Expected output format: The function should return an array where the `i-th` element is the maximum XOR score of the subarray specified by the `i-th` query.
- Key requirements and edge cases to consider: The XOR score of a subarray is the maximum XOR of any two elements in the subarray. The input array and queries are non-empty, and each query is valid.
- Example test cases with explanations: For example, given `arr = [1, 2, 3]` and `queries = [[0, 2]]`, the output should be `[3]` because the maximum XOR score of the subarray `[1, 2, 3]` is `3` (i.e., `1 XOR 2 = 3`).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find the maximum XOR score for each query, we can iterate over all pairs of elements in the specified subarray and calculate their XOR.
- Step-by-step breakdown of the solution:
  1. Iterate over each query.
  2. For each query, iterate over all pairs of elements in the specified subarray.
  3. Calculate the XOR of each pair of elements.
  4. Keep track of the maximum XOR score found.
- Why this approach comes to mind first: It directly addresses the problem statement by considering all possible pairs of elements in each subarray.

```cpp
vector<int> maximizeXor(vector<int>& arr, vector<vector<int>>& queries) {
    int n = arr.size();
    int q = queries.size();
    vector<int> result(q);
    
    for (int i = 0; i < q; i++) {
        int max_xor = 0;
        int start = queries[i][0];
        int end = queries[i][1];
        
        for (int j = start; j <= end; j++) {
            for (int k = j; k <= end; k++) {
                max_xor = max(max_xor, arr[j] ^ arr[k]);
            }
        }
        
        result[i] = max_xor;
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(q \cdot n^2)$, where $q$ is the number of queries and $n$ is the size of the input array. This is because for each query, we potentially iterate over all pairs of elements in the subarray.
> - **Space Complexity:** $O(q)$, for storing the result of each query.
> - **Why these complexities occur:** The brute force approach has a high time complexity due to the nested loops over the array elements for each query.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a Trie data structure to store the binary representation of the numbers in the array. This allows us to efficiently find the maximum XOR score for each query by traversing the Trie.
- Detailed breakdown of the approach:
  1. Create a Trie and insert all numbers from the array into it.
  2. For each query, find the maximum XOR score by traversing the Trie and selecting the path that maximizes the XOR with the current number.
- Proof of optimality: This approach is optimal because it reduces the time complexity of finding the maximum XOR score for each query from $O(n)$ to $O(log m)$, where $m$ is the maximum value in the array.

```cpp
struct TrieNode {
    TrieNode* children[2];
};

TrieNode* newNode() {
    TrieNode* node = new TrieNode();
    node->children[0] = node->children[1] = nullptr;
    return node;
}

void insert(TrieNode* root, int num) {
    TrieNode* node = root;
    for (int i = 31; i >= 0; i--) {
        int bit = (num >> i) & 1;
        if (!node->children[bit]) {
            node->children[bit] = newNode();
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

vector<int> maximizeXor(vector<int>& arr, vector<vector<int>>& queries) {
    int n = arr.size();
    int q = queries.size();
    vector<int> result(q);
    TrieNode* root = newNode();
    
    for (int i = 0; i < n; i++) {
        insert(root, arr[i]);
    }
    
    for (int i = 0; i < q; i++) {
        int start = queries[i][0];
        int end = queries[i][1];
        int max_xor = 0;
        
        for (int j = start; j <= end; j++) {
            max_xor = max(max_xor, query(root, arr[j]));
        }
        
        result[i] = max_xor;
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot log m + q \cdot log m)$, where $n$ is the size of the input array, $q$ is the number of queries, and $m$ is the maximum value in the array. This is because we insert all numbers into the Trie and then query the Trie for each number in each query.
> - **Space Complexity:** $O(n \cdot log m)$, for storing the Trie.
> - **Optimality proof:** This approach is optimal because it reduces the time complexity of finding the maximum XOR score for each query from $O(n)$ to $O(log m)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a Trie to efficiently find the maximum XOR score.
- Problem-solving patterns identified: Reducing the time complexity by using a data structure that allows for efficient querying.
- Optimization techniques learned: Using a Trie to store binary representations of numbers.
- Similar problems to practice: Other problems involving finding the maximum XOR score or using a Trie to solve a problem.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as an empty input array or queries.
- Edge cases to watch for: Queries that span the entire array, or queries that have a start index greater than the end index.
- Performance pitfalls: Using a brute force approach that has a high time complexity.
- Testing considerations: Testing the solution with different input sizes and edge cases to ensure it works correctly and efficiently.