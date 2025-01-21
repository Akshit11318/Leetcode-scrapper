## Count Pairs with XOR in a Range
**Problem Link:** https://leetcode.com/problems/count-pairs-with-xor-in-a-range/description

**Problem Statement:**
- Input format and constraints: Given an array of integers `nums` and an integer `low`, and an integer `high`, return the number of pairs `(i, j)` such that `i < j`, `nums[i] XOR nums[j]` is in the range `[low, high]`.
- Expected output format: An integer representing the count of such pairs.
- Key requirements and edge cases to consider: `1 <= nums.length <= 10^5`, `0 <= nums[i] <= 10^6`, `0 <= low <= high <= 10^6`.
- Example test cases with explanations:
  - For `nums = [1, 4, 2, 7]`, `low = 2`, `high = 3`, the pairs `(0, 1)`, `(1, 2)`, `(2, 3)` have XOR values `5`, `6`, `5` respectively, which are not within the range `[2, 3]`. So, the output is `0`.
  - For `nums = [9, 8, 4, 2, 3, 5, 7, 6, 1]`, `low = 6`, `high = 8`, the pairs that satisfy the condition are `(0, 1)`, `(0, 2)`, `(0, 3)`, `(1, 3)`, `(1, 4)`, `(2, 4)`, `(3, 4)`, `(4, 5)`, `(4, 6)`, `(5, 6)`, `(5, 7)`, `(6, 7)`, `(7, 8)`, giving a total count of `13`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The straightforward way to solve this problem is to iterate through each pair of numbers in the array, calculate the XOR of the pair, and check if it falls within the given range.
- Step-by-step breakdown of the solution:
  1. Initialize a counter variable to store the number of pairs that satisfy the condition.
  2. Iterate through the array using two nested loops to consider each pair `(i, j)` where `i < j`.
  3. For each pair, calculate the XOR of `nums[i]` and `nums[j]`.
  4. Check if the XOR value is within the range `[low, high]`. If it is, increment the counter.
- Why this approach comes to mind first: It directly addresses the problem statement by checking every possible pair, which makes it easy to understand and implement.

```cpp
int countPairs(vector<int>& nums, int low, int high) {
    int count = 0;
    for (int i = 0; i < nums.size(); ++i) {
        for (int j = i + 1; j < nums.size(); ++j) {
            if (low <= (nums[i] ^ nums[j]) && (nums[i] ^ nums[j]) <= high) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the size of the input array `nums`. This is because for each element, we potentially check every other element.
> - **Space Complexity:** $O(1)$, not including the space needed for the input and output, as we only use a constant amount of space to store the count.
> - **Why these complexities occur:** The time complexity is quadratic due to the nested loops, and the space complexity is constant because we only use a fixed amount of space regardless of the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Utilizing a Trie data structure to store the binary representations of the numbers in `nums`. This allows for efficient calculation of XOR values and checking if they fall within the given range.
- Detailed breakdown of the approach:
  1. Create a Trie and insert all numbers from `nums` into it.
  2. For each number in `nums`, calculate its XOR with every other number by traversing the Trie and counting the number of nodes that represent values within the range `[low, high]`.
- Proof of optimality: This approach is optimal because it reduces the time complexity significantly by avoiding the need to explicitly calculate the XOR for every pair of numbers, instead leveraging the properties of the Trie to efficiently explore possible XOR values.

```cpp
class TrieNode {
public:
    TrieNode* children[2];
    TrieNode() {
        children[0] = children[1] = nullptr;
    }
};

void insert(TrieNode* root, int num) {
    TrieNode* node = root;
    for (int i = 20; i >= 0; --i) {
        int bit = (num >> i) & 1;
        if (!node->children[bit]) {
            node->children[bit] = new TrieNode();
        }
        node = node->children[bit];
    }
}

int countPairsUtil(TrieNode* root, int num, int low, int high, int bit) {
    if (low > high) return 0;
    if (bit < 0) return 1;
    TrieNode* node = root;
    int lowBit = (low >> bit) & 1;
    int highBit = (high >> bit) & 1;
    int count = 0;
    if (lowBit == highBit) {
        if (node->children[lowBit ^ ((num >> bit) & 1)]) {
            count += countPairsUtil(node->children[lowBit ^ ((num >> bit) & 1)], num, low, high, bit - 1);
        }
    } else {
        if (node->children[0 ^ ((num >> bit) & 1)]) {
            count += countPairsUtil(node->children[0 ^ ((num >> bit) & 1)], num, low, (1 << bit) - 1 + lowBit, bit - 1);
        }
        if (node->children[1 ^ ((num >> bit) & 1)]) {
            count += countPairsUtil(node->children[1 ^ ((num >> bit) & 1)], num, highBit << bit, high, bit - 1);
        }
    }
    return count;
}

int countPairs(vector<int>& nums, int low, int high) {
    TrieNode* root = new TrieNode();
    int count = 0;
    for (int num : nums) {
        count += countPairsUtil(root, num, low, high, 20);
        insert(root, num);
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot b)$, where $n$ is the number of elements in `nums` and $b$ is the number of bits in the binary representation of the numbers (in this case, $b = 21$ for numbers up to $10^6$).
> - **Space Complexity:** $O(n \cdot b)$, for storing the Trie.
> - **Optimality proof:** This approach is optimal because it efficiently explores the XOR space using the Trie, reducing the time complexity from $O(n^2)$ to $O(n \cdot b)$, which is significantly better for large inputs.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a Trie to efficiently explore the space of XOR values.
- Problem-solving patterns identified: Leveraging data structures to reduce computational complexity.
- Optimization techniques learned: Applying Trie to problems involving bitwise operations.
- Similar problems to practice: Other problems involving XOR operations and range queries.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling edge cases, such as when `low > high`.
- Edge cases to watch for: Ensuring that the Trie is properly initialized and updated.
- Performance pitfalls: Failing to consider the bit length of the numbers, leading to incorrect results.
- Testing considerations: Thoroughly testing the implementation with various inputs, including edge cases.