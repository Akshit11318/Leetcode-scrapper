## Maximum XOR for Each Query
**Problem Link:** https://leetcode.com/problems/maximum-xor-for-each-query/description

**Problem Statement:**
- Input format and constraints: Given a list of non-negative integers `nums`, find the maximum XOR for each query where the query is defined as finding the maximum XOR value between any two elements in `nums` that is less than or equal to `x`, where `x` is the query value.
- Expected output format: Return a list of integers representing the maximum XOR value for each query.
- Key requirements and edge cases to consider: 
    - The list `nums` contains non-negative integers.
    - Each query value `x` is a non-negative integer.
    - The XOR operation is commutative and associative.
- Example test cases with explanations:
    - `nums = [0, 1, 2, 3, 4], queries = [3, 1, 2]`
    - The maximum XOR for each query is `[3, 1, 3]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: For each query, iterate through all pairs of numbers in `nums` and find the maximum XOR value that is less than or equal to the query value.
- Step-by-step breakdown of the solution:
    1. Iterate through each query value.
    2. For each query value, iterate through all pairs of numbers in `nums`.
    3. For each pair, calculate the XOR value.
    4. If the XOR value is less than or equal to the query value, update the maximum XOR value for the current query.
- Why this approach comes to mind first: This approach is straightforward and directly addresses the problem statement.

```cpp
vector<int> maximizeXor(vector<int>& nums, vector<int>& queries) {
    vector<int> result;
    for (int query : queries) {
        int max_xor = 0;
        for (int num1 : nums) {
            for (int num2 : nums) {
                if (num1 != num2) {
                    int xor_val = num1 ^ num2;
                    if (xor_val <= query && xor_val > max_xor) {
                        max_xor = xor_val;
                    }
                }
            }
        }
        result.push_back(max_xor);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot q)$, where $n$ is the number of elements in `nums` and $q$ is the number of queries. This is because for each query, we iterate through all pairs of numbers in `nums`.
> - **Space Complexity:** $O(q)$, where $q$ is the number of queries. This is because we store the result for each query in a separate vector.
> - **Why these complexities occur:** The brute force approach has high time complexity due to the nested loops iterating through all pairs of numbers for each query.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a `Trie` data structure to store the binary representation of numbers in `nums`. This allows us to efficiently find the maximum XOR value for each query.
- Detailed breakdown of the approach:
    1. Create a `Trie` node with `children` and `val` attributes.
    2. Insert all numbers in `nums` into the `Trie`.
    3. For each query, traverse the `Trie` to find the maximum XOR value.
- Proof of optimality: The `Trie` data structure allows us to reduce the time complexity of finding the maximum XOR value for each query from $O(n^2)$ to $O(n \cdot q \cdot b)$, where $b$ is the number of bits in the binary representation of the numbers.

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

int findMaxXor(TrieNode* root, int num) {
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
    vector<int> result;
    for (int query : queries) {
        int max_xor = 0;
        for (int num : nums) {
            int xor_val = findMaxXor(root, num);
            if (xor_val <= query && xor_val > max_xor) {
                max_xor = xor_val;
            }
        }
        result.push_back(max_xor);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot q \cdot b)$, where $n$ is the number of elements in `nums`, $q$ is the number of queries, and $b$ is the number of bits in the binary representation of the numbers.
> - **Space Complexity:** $O(n \cdot b)$, where $n$ is the number of elements in `nums` and $b$ is the number of bits in the binary representation of the numbers.
> - **Optimality proof:** The `Trie` data structure allows us to efficiently find the maximum XOR value for each query, reducing the time complexity from $O(n^2 \cdot q)$ to $O(n \cdot q \cdot b)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: `Trie` data structure, XOR operation, and binary representation of numbers.
- Problem-solving patterns identified: Using a data structure to reduce time complexity and improving the efficiency of finding the maximum XOR value.
- Optimization techniques learned: Using a `Trie` data structure to efficiently find the maximum XOR value for each query.
- Similar problems to practice: Other problems involving XOR operations and binary representation of numbers.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as an empty `nums` array or an empty `queries` array.
- Edge cases to watch for: Handling queries with values greater than the maximum value in `nums`.
- Performance pitfalls: Not using an efficient data structure, such as a `Trie`, to find the maximum XOR value for each query.
- Testing considerations: Testing with different input sizes and edge cases to ensure the correctness and efficiency of the solution.