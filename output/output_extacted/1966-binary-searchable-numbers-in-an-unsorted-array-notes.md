## Binary Searchable Numbers in an Unsorted Array

**Problem Link:** https://leetcode.com/problems/binary-searchable-numbers-in-an-unsorted-array/description

**Problem Statement:**
- Input format: An array of integers `nums`.
- Constraints: The length of `nums` is in the range $[1, 10^5]$ and each element is in the range $[-10^6, 10^6]$.
- Expected output format: The count of binary searchable numbers in the array.
- Key requirements and edge cases to consider: A number is considered binary searchable if its digits in binary representation form a valid binary search tree, i.e., for each node, all numbers in its left subtree are less than the node, and all numbers in its right subtree are greater.
- Example test cases with explanations:
    - For the input `[1, 3, 5]`, the output is `1` because only `1` (binary `1`) is a binary searchable number.
    - For the input `[4, 3, 2, 1]`, the output is `1` because only `1` (binary `1`) is a binary searchable number.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The problem requires checking each number in the array to see if it forms a valid binary search tree when its binary digits are considered as node values.
- Step-by-step breakdown of the solution:
    1. Convert each number to its binary representation.
    2. For each binary representation, attempt to construct a binary search tree.
    3. Check if the constructed tree is valid by ensuring that for each node, all elements in its left subtree are less than the node, and all elements in its right subtree are greater.
- Why this approach comes to mind first: It directly addresses the problem statement by checking each number individually against the criteria for being a binary searchable number.

```cpp
#include <iostream>
#include <vector>
#include <string>
using namespace std;

// Function to check if a binary tree is a valid binary search tree
bool isValidBST(vector<int>& nums) {
    if (nums.size() <= 1) return true; // Base case: single node or empty tree
    int root = nums[0];
    vector<int> left, right;
    for (int i = 1; i < nums.size(); ++i) {
        if (nums[i] < root) left.push_back(nums[i]);
        else if (nums[i] > root) right.push_back(nums[i]);
        else return false; // Duplicate values not allowed in a BST
    }
    // Recursively check left and right subtrees
    return isValidBST(left) && isValidBST(right);
}

// Function to convert an integer to binary and store in a vector
vector<int> toBinary(int num) {
    vector<int> binary;
    while (num > 0) {
        binary.push_back(num % 2);
        num /= 2;
    }
    return binary;
}

int binarySearchableNumbers(vector<int>& nums) {
    int count = 0;
    for (int num : nums) {
        vector<int> binary = toBinary(num);
        if (isValidBST(binary)) count++;
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot 2^m)$ where $n$ is the number of elements in the array and $m$ is the maximum number of bits in the binary representation of the numbers. The reason is that for each number, we potentially explore all possible binary trees that can be constructed from its binary digits.
> - **Space Complexity:** $O(2^m)$ for storing the recursive call stack and temporary binary representations.
> - **Why these complexities occur:** The exponential time complexity comes from the recursive nature of checking all possible subtrees for each binary representation. The space complexity is due to the recursive call stack and the storage needed for the binary representations.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of constructing a binary search tree for each number's binary representation, we can directly check if the binary digits are in a valid order for a binary search tree. This can be done by iterating through the binary digits and ensuring that each digit is either greater than the previous one (for a right subtree) or less than the previous one but only if we haven't seen a smaller digit before (for a left subtree).
- Detailed breakdown of the approach:
    1. Convert each number to its binary representation.
    2. Iterate through the binary digits, keeping track of the minimum and maximum values seen so far.
    3. If a digit is less than the minimum seen so far, it indicates a left subtree, so update the minimum. If it's greater than the maximum seen so far, it indicates a right subtree, so update the maximum.
    4. If a digit is neither less than the minimum nor greater than the maximum, it means the binary digits do not form a valid binary search tree, so move on to the next number.
- Proof of optimality: This approach is optimal because it directly checks the condition for a binary search tree without the overhead of constructing trees, reducing the time complexity significantly.

```cpp
int binarySearchableNumbers(vector<int>& nums) {
    int count = 0;
    for (int num : nums) {
        vector<int> binary = toBinary(num);
        int minSeen = binary[0], maxSeen = binary[0];
        bool isValid = true;
        for (int i = 1; i < binary.size(); ++i) {
            if (binary[i] < minSeen) {
                if (binary[i] < minSeen) minSeen = binary[i];
                else { isValid = false; break; }
            } else if (binary[i] > maxSeen) {
                maxSeen = binary[i];
            } else { isValid = false; break; }
        }
        if (isValid) count++;
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the number of elements in the array and $m$ is the maximum number of bits in the binary representation of the numbers. This is because we iterate through each binary representation once.
> - **Space Complexity:** $O(m)$ for storing the binary representation of each number.
> - **Optimality proof:** This approach is optimal because it directly checks the validity of the binary search tree condition without unnecessary overhead, achieving a linear time complexity with respect to the size of the input.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iterative approach, binary search tree validation.
- Problem-solving patterns identified: Direct validation of conditions instead of constructing complex data structures.
- Optimization techniques learned: Reducing time complexity by avoiding unnecessary constructions and using iterative methods.
- Similar problems to practice: Other problems involving validation of tree structures or iterative approaches to complex data structures.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect handling of edge cases, such as single-node trees or empty arrays.
- Edge cases to watch for: Numbers with leading zeros in their binary representation, duplicate values in the binary representation.
- Performance pitfalls: Using recursive approaches for large inputs, not optimizing the validation process.
- Testing considerations: Thoroughly testing with arrays of varying sizes and numbers with different binary representations.