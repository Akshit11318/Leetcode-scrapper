## Maximum Strong Pair XOR I

**Problem Link:** https://leetcode.com/problems/maximum-strong-pair-xor-i/description

**Problem Statement:**
- Input format and constraints: Given an array of integers `nums`, find the maximum XOR of two numbers in the array.
- Expected output format: The maximum XOR value.
- Key requirements and edge cases to consider: 
    - All elements in `nums` are unique.
    - The length of `nums` is between 1 and 1000.
    - All elements in `nums` are between 0 and $10^5$.
- Example test cases with explanations:
    - For `nums = [2, 3, 6, 5, 4, 1]`, the maximum XOR is 7 (2 XOR 5).
    - For `nums = [0, 1]`, the maximum XOR is 1 (0 XOR 1).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Compare each pair of numbers in the array and calculate the XOR.
- Step-by-step breakdown of the solution:
    1. Iterate over the array using two nested loops to generate all pairs of numbers.
    2. For each pair, calculate the XOR.
    3. Keep track of the maximum XOR found so far.
- Why this approach comes to mind first: It's a straightforward way to consider all possible pairs of numbers.

```cpp
int findMaximumXOR(vector<int>& nums) {
    int max_XOR = 0;
    for (int i = 0; i < nums.size(); i++) {
        for (int j = i + 1; j < nums.size(); j++) {
            int XOR = nums[i] ^ nums[j];
            max_XOR = max(max_XOR, XOR);
        }
    }
    return max_XOR;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of elements in `nums`. This is because we use two nested loops to generate all pairs of numbers.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum XOR.
> - **Why these complexities occur:** The time complexity is quadratic because we consider all pairs of numbers, and the space complexity is constant because we only keep track of the maximum XOR.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a Trie data structure to efficiently store and query the binary representation of numbers in `nums`.
- Detailed breakdown of the approach:
    1. Create a Trie with a root node.
    2. Insert each number from `nums` into the Trie by iterating over its binary representation from most significant bit to least significant bit.
    3. For each number in `nums`, query the Trie to find the maximum XOR by traversing the Trie in a way that maximizes the XOR at each step.
- Proof of optimality: This approach is optimal because it allows us to efficiently consider all possible pairs of numbers and calculate their XOR in $O(n \cdot b)$ time, where $b$ is the number of bits in the binary representation of the numbers.
- Why further optimization is impossible: This approach has a time complexity of $O(n \cdot b)$, which is the best possible time complexity for this problem because we must at least read the input.

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
                if (node->children[bit] == nullptr) {
                    node->children[bit] = new TrieNode();
                }
                node = node->children[bit];
            }
        }
        
        int max_XOR = 0;
        for (int num : nums) {
            TrieNode* node = root;
            int curr_XOR = 0;
            for (int i = 31; i >= 0; i--) {
                int bit = (num >> i) & 1;
                if (node->children[1 - bit] != nullptr) {
                    curr_XOR |= (1 << i);
                    node = node->children[1 - bit];
                } else {
                    node = node->children[bit];
                }
            }
            max_XOR = max(max_XOR, curr_XOR);
        }
        
        return max_XOR;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot b)$, where $n$ is the number of elements in `nums` and $b$ is the number of bits in the binary representation of the numbers.
> - **Space Complexity:** $O(n \cdot b)$, as we store all numbers in the Trie.
> - **Optimality proof:** This approach is optimal because it allows us to efficiently consider all possible pairs of numbers and calculate their XOR in $O(n \cdot b)$ time.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Trie data structure, bit manipulation.
- Problem-solving patterns identified: Using a Trie to efficiently store and query binary representations of numbers.
- Optimization techniques learned: Using a Trie to reduce the time complexity of the algorithm.
- Similar problems to practice: Other problems that involve finding the maximum XOR of two numbers in an array.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as an empty input array.
- Edge cases to watch for: An empty input array, an array with only one element.
- Performance pitfalls: Using a brute force approach with a time complexity of $O(n^2)$.
- Testing considerations: Testing the algorithm with different input arrays, including edge cases.