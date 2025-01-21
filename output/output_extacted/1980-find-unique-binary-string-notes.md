## Find Unique Binary String

**Problem Link:** https://leetcode.com/problems/find-unique-binary-string/description

**Problem Statement:**
- Input format and constraints: Given an array of integers `nums` where every integer is between 1 and `n` (inclusive), and `n` is the length of the array. The task is to find the lexicographically smallest unique binary string of length `n`.
- Expected output format: The lexicographically smallest unique binary string of length `n`.
- Key requirements and edge cases to consider: The binary string should be unique, and the lexicographically smallest.
- Example test cases with explanations:
  - `nums = [1, 2, 3]`, `n = 3`, the output should be `"001"`.
  - `nums = [1, 1, 2]`, `n = 2`, the output should be `"00"`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible binary strings of length `n`, and check if each string is unique.
- Step-by-step breakdown of the solution:
  1. Generate all possible binary strings of length `n`.
  2. For each binary string, check if it is unique by comparing it with all other strings.
  3. Return the lexicographically smallest unique binary string.
- Why this approach comes to mind first: It is a straightforward approach that involves generating all possible solutions and then selecting the best one.

```cpp
class Solution {
public:
    string findDifferentBinaryString(vector<int>& nums) {
        int n = nums.size();
        vector<string> binaryStrings;
        for (int i = 0; i < (1 << n); i++) {
            string binaryString;
            for (int j = 0; j < n; j++) {
                binaryString += (i >> j) & 1 ? '1' : '0';
            }
            binaryStrings.push_back(binaryString);
        }
        sort(binaryStrings.begin(), binaryStrings.end());
        for (string& binaryString : binaryStrings) {
            bool isUnique = true;
            for (int i = 0; i < n; i++) {
                string substr = binaryString.substr(i, 1);
                if (nums[i] == 1 && substr == "1") {
                    isUnique = false;
                    break;
                }
                if (nums[i] == 2 && substr == "0") {
                    isUnique = false;
                    break;
                }
            }
            if (isUnique) {
                return binaryString;
            }
        }
        return "";
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n \cdot log(2^n)) = O(2^n \cdot n^2)$, where $n$ is the length of the input array. This is because we generate $2^n$ binary strings, each of length $n$, and then sort them.
> - **Space Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the input array. This is because we store $2^n$ binary strings, each of length $n$.
> - **Why these complexities occur:** The brute force approach involves generating all possible binary strings, which results in exponential time and space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can construct the lexicographically smallest unique binary string by iterating over the input array and appending the smallest possible digit that makes the current prefix unique.
- Detailed breakdown of the approach:
  1. Initialize an empty binary string.
  2. Iterate over the input array.
  3. For each element, append the smallest possible digit that makes the current prefix unique.
  4. Return the constructed binary string.
- Proof of optimality: This approach is optimal because it constructs the lexicographically smallest unique binary string by making the smallest possible choices at each step.

```cpp
class Solution {
public:
    string findDifferentBinaryString(vector<int>& nums) {
        int n = nums.size();
        string binaryString;
        for (int i = 0; i < n; i++) {
            if (i == nums[i] - 1) {
                binaryString += '0';
            } else {
                binaryString += '1';
            }
        }
        return binaryString;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input array. This is because we iterate over the input array once.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input array. This is because we construct a binary string of length $n$.
> - **Optimality proof:** This approach is optimal because it constructs the lexicographically smallest unique binary string by making the smallest possible choices at each step.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iterative construction of the lexicographically smallest unique binary string.
- Problem-solving patterns identified: Making the smallest possible choices at each step to construct the optimal solution.
- Optimization techniques learned: Avoiding unnecessary computations by making the smallest possible choices.
- Similar problems to practice: Constructing the lexicographically smallest unique string over a larger alphabet.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling edge cases, such as when the input array is empty.
- Edge cases to watch for: When the input array is empty, or when the input array contains duplicate elements.
- Performance pitfalls: Using inefficient algorithms, such as generating all possible binary strings.
- Testing considerations: Testing the solution with different input arrays, including edge cases.