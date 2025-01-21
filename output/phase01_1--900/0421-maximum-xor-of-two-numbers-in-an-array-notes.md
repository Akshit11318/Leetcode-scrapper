## Maximum XOR of Two Numbers in an Array

**Problem Link:** https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/description

**Problem Statement:**
- Input format: An array of integers `nums`.
- Constraints: `2 <= nums.length <= 10^5`, `0 <= nums[i] <= 2^31 - 1`.
- Expected output format: The maximum XOR of two numbers in the array.
- Key requirements: Find the maximum XOR of two numbers in the array.
- Edge cases: Handle cases where the array has less than two elements.

Example test cases:
- `nums = [3, 10, 5, 25, 2, 8]`, the maximum XOR is `28`.
- `nums = [0]`, the maximum XOR is `0`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to iterate through each pair of numbers in the array and calculate their XOR.
- Then, keep track of the maximum XOR found.

```cpp
class Solution {
public:
    int findMaximumXOR(vector<int>& nums) {
        int max_xor = 0;
        for (int i = 0; i < nums.size(); i++) {
            for (int j = i + 1; j < nums.size(); j++) {
                max_xor = max(max_xor, nums[i] ^ nums[j]);
            }
        }
        return max_xor;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of elements in the array, because we are iterating through each pair of numbers.
> - **Space Complexity:** $O(1)$, because we are only using a constant amount of space to store the maximum XOR.
> - **Why these complexities occur:** The time complexity is quadratic because we are using nested loops to iterate through each pair of numbers. The space complexity is constant because we are not using any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a Trie data structure to store the binary representation of each number in the array.
- We can then iterate through the Trie to find the maximum XOR of two numbers.
- The Trie will allow us to quickly find the maximum XOR by traversing the tree and choosing the opposite bit at each node.

```cpp
class TrieNode {
public:
    TrieNode* children[2];
    TrieNode() {
        children[0] = nullptr;
        children[1] = nullptr;
    }
};

class Solution {
public:
    int findMaximumXOR(vector<int>& nums) {
        TrieNode* root = new TrieNode();
        for (int num : nums) {
            TrieNode* node = root;
            for (int i = 31; i >= 0; i--) {
                int bit = (num >> i) & 1;
                if (!node->children[bit]) {
                    node->children[bit] = new TrieNode();
                }
                node = node->children[bit];
            }
        }
        
        int max_xor = 0;
        for (int num : nums) {
            TrieNode* node = root;
            int curr_xor = 0;
            for (int i = 31; i >= 0; i--) {
                int bit = (num >> i) & 1;
                if (node->children[1 - bit]) {
                    curr_xor |= (1 << i);
                    node = node->children[1 - bit];
                } else {
                    node = node->children[bit];
                }
            }
            max_xor = max(max_xor, curr_xor);
        }
        
        return max_xor;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot b)$, where $n$ is the number of elements in the array and $b$ is the number of bits in each number, because we are iterating through each number and each bit in the number.
> - **Space Complexity:** $O(n \cdot b)$, because we are storing the binary representation of each number in the Trie.
> - **Optimality proof:** This is the optimal solution because we are using a Trie to quickly find the maximum XOR of two numbers. The Trie allows us to traverse the tree and choose the opposite bit at each node, resulting in the maximum XOR.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Trie data structure, binary representation of numbers, and XOR operation.
- Problem-solving patterns identified: Using a Trie to quickly find the maximum XOR of two numbers.
- Optimization techniques learned: Using a Trie to reduce the time complexity from quadratic to linear.
- Similar problems to practice: Other problems involving Trie data structures and XOR operations.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as an empty array or an array with less than two elements.
- Edge cases to watch for: Handling cases where the array has less than two elements.
- Performance pitfalls: Not using a Trie data structure, resulting in a quadratic time complexity.
- Testing considerations: Testing the solution with different input sizes and edge cases to ensure correctness and efficiency.