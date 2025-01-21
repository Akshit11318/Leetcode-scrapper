## Length of Longest Fibonacci Subsequence

**Problem Link:** [https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/description](https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/description)

**Problem Statement:**
- Input format: An array of integers `A` representing a set of numbers.
- Constraints: `2 <= A.length <= 1000`, and each element in `A` is distinct.
- Expected output format: The length of the longest Fibonacci-like subsequence.
- Key requirements and edge cases to consider: A Fibonacci-like sequence is a sequence where every number is the sum of the two preceding ones, and the sequence must start with two distinct numbers from the input array.
- Example test cases with explanations:
  - Input: `A = [1,2,3,5,8,13]`, Output: `6` (the sequence itself is a Fibonacci-like sequence).
  - Input: `A = [1,3,7,11,12,14,18]`, Output: `3` (a possible subsequence is `3, 11, 14`).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible pairs of numbers from the input array and then try to extend each pair into a Fibonacci-like sequence by checking if the sum of the last two numbers in the sequence exists in the array.
- Step-by-step breakdown of the solution:
  1. Initialize the maximum length of the Fibonacci-like subsequence to `0`.
  2. Iterate over all pairs of distinct numbers in the array.
  3. For each pair, try to extend it into a Fibonacci-like sequence by checking if the sum of the last two numbers is in the array.
  4. Update the maximum length if a longer sequence is found.
- Why this approach comes to mind first: It directly addresses the problem by considering all possible starting points for a Fibonacci-like sequence.

```cpp
#include <vector>
#include <unordered_set>

int lenLongestFibSubseq(vector<int>& A) {
    unordered_set<int> nums(A.begin(), A.end());
    int maxLen = 0;
    for (int i = 0; i < A.size(); ++i) {
        for (int j = i + 1; j < A.size(); ++j) {
            int a = A[i], b = A[j];
            int len = 2;
            while (nums.find(a + b) != nums.end()) {
                int temp = a + b;
                a = b;
                b = temp;
                len++;
            }
            maxLen = max(maxLen, len);
        }
    }
    return maxLen > 2 ? maxLen : 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \times m)$ where $n$ is the number of elements in the array and $m$ is the average length of the Fibonacci-like subsequences. The nested loops iterate over all pairs of numbers, and for each pair, we potentially extend the sequence until we cannot find the next number in the array.
> - **Space Complexity:** $O(n)$ for storing the input array in an `unordered_set` for efficient lookup.
> - **Why these complexities occur:** The brute force approach checks all possible pairs and tries to extend each into a Fibonacci-like sequence, leading to quadratic time complexity in the number of elements in the array. The space complexity is linear due to the use of an `unordered_set` for efficient lookup of numbers in the array.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Utilizing a hash set for efficient lookup and only iterating over pairs of numbers once.
- Detailed breakdown of the approach:
  1. Store the input array in a hash set for $O(1)$ lookup.
  2. Iterate over all pairs of distinct numbers in the array.
  3. For each pair, attempt to extend it into a Fibonacci-like sequence by checking if the sum of the last two numbers is in the hash set.
  4. Keep track of the maximum length of the Fibonacci-like subsequence found.
- Proof of optimality: This approach is optimal because it only requires a single pass over all pairs of numbers and uses efficient lookup to extend sequences, minimizing both time and space complexity.

```cpp
#include <vector>
#include <unordered_set>

int lenLongestFibSubseq(vector<int>& A) {
    unordered_set<int> nums(A.begin(), A.end());
    int maxLen = 0;
    for (int i = 0; i < A.size(); ++i) {
        for (int j = i + 1; j < A.size(); ++j) {
            int a = A[i], b = A[j];
            int len = 2;
            while (nums.find(a + b) != nums.end()) {
                int temp = a + b;
                a = b;
                b = temp;
                len++;
            }
            if (len > 2) maxLen = max(maxLen, len);
        }
    }
    return maxLen;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \times m)$ where $n$ is the number of elements in the array and $m$ is the average length of the Fibonacci-like subsequences. The nested loops iterate over all pairs of numbers, and for each pair, we potentially extend the sequence.
> - **Space Complexity:** $O(n)$ for storing the input array in an `unordered_set`.
> - **Optimality proof:** The approach is optimal because it minimizes both time and space complexity by using efficient lookup and only considering each pair of numbers once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using hash sets for efficient lookup and iterating over pairs of numbers to find Fibonacci-like subsequences.
- Problem-solving patterns identified: Breaking down the problem into smaller sub-problems (finding all pairs and then extending them) and using data structures for efficient computation.
- Optimization techniques learned: Minimizing time complexity by using $O(1)$ lookup and minimizing space complexity by only storing necessary data.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for the existence of the next number in the sequence before attempting to extend it.
- Edge cases to watch for: Handling cases where the input array is empty or contains only one element.
- Performance pitfalls: Using inefficient data structures or algorithms that lead to higher time or space complexity.
- Testing considerations: Thoroughly testing the solution with various inputs, including edge cases, to ensure correctness and efficiency.