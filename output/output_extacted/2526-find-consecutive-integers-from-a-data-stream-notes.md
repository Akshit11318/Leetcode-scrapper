## Find Consecutive Integers From a Data Stream
**Problem Link:** https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/description

**Problem Statement:**
- Input format and constraints: The problem involves a data stream where integers are added one by one. We need to find the first sequence of `k` consecutive integers from this stream.
- Expected output format: The solution should return a list of these consecutive integers once found.
- Key requirements and edge cases to consider: The stream may not contain `k` consecutive integers, and the integers can be negative.
- Example test cases with explanations:
  - For `k = 3` and a stream of integers `[4, 1, 2, 3]`, the output should be `[1, 2, 3]`.
  - For `k = 5` and a stream of integers `[1, 2, 3, 4, 5]`, the output should be `[1, 2, 3, 4, 5]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The simplest way to solve this problem is to store all the integers from the stream in a set or list and then check for every possible sequence of `k` consecutive integers.
- Step-by-step breakdown of the solution:
  1. Store each integer from the stream in a set for efficient lookup.
  2. For each integer in the set, check if it is the start of a sequence of `k` consecutive integers.
  3. If such a sequence is found, return it immediately.
- Why this approach comes to mind first: It directly addresses the problem statement without considering optimizations, making it a straightforward but potentially inefficient solution.

```cpp
class DataStream {
public:
    unordered_set<int> nums;
    int k;

    DataStream(int k) : k(k) {}

    void add(int num) {
        nums.insert(num);
        if (nums.size() >= k) {
            for (int n : nums) {
                bool isConsecutive = true;
                for (int i = 1; i < k; i++) {
                    if (nums.find(n + i) == nums.end()) {
                        isConsecutive = false;
                        break;
                    }
                }
                if (isConsecutive) {
                    vector<int> result;
                    for (int i = 0; i < k; i++) {
                        result.push_back(n + i);
                    }
                    // Found the first sequence of k consecutive integers
                    // You can store this result or print it
                    cout << "Consecutive integers found: ";
                    for (int val : result) {
                        cout << val << " ";
                    }
                    cout << endl;
                    return;
                }
            }
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k)$ where $n$ is the number of unique integers in the stream, because for each integer, we potentially check for a sequence of length $k$.
> - **Space Complexity:** $O(n)$ for storing all unique integers in the stream.
> - **Why these complexities occur:** The brute force approach involves checking every possible sequence start point, leading to a time complexity that scales with both the number of unique integers and the sequence length $k$. The space complexity is directly related to storing all unique integers.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking all possible start points for a sequence of $k$ consecutive integers, we can maintain a sliding window of integers we've seen so far and track the longest sequence of consecutive integers seen.
- Detailed breakdown of the approach:
  1. Use a `set` to store unique integers from the stream for efficient lookup.
  2. For each new integer, check if it extends any existing sequence of consecutive integers.
  3. If it does, update the longest sequence length and its start point.
- Proof of optimality: This approach ensures we find the first sequence of $k$ consecutive integers as soon as it becomes possible, because we're always checking the latest integer against the existing sequences.
- Why further optimization is impossible: We must examine each integer at least once, and checking for sequence extensions with each new integer is necessary to ensure we find the first sequence of length $k$.

```cpp
class DataStream {
public:
    unordered_set<int> nums;
    int k;
    int longestSeqStart = INT_MAX;
    int longestSeqLen = 0;

    DataStream(int k) : k(k) {}

    void add(int num) {
        nums.insert(num);
        if (nums.find(num - 1) == nums.end() && nums.find(num + 1) != nums.end()) {
            // num could be the start of a new sequence
            int currentNum = num;
            int currentSeqLen = 1;
            while (nums.find(currentNum + 1) != nums.end()) {
                currentNum += 1;
                currentSeqLen += 1;
            }
            if (currentSeqLen > longestSeqLen) {
                longestSeqStart = num;
                longestSeqLen = currentSeqLen;
            }
            if (longestSeqLen >= k) {
                vector<int> result;
                for (int i = 0; i < k; i++) {
                    result.push_back(longestSeqStart + i);
                }
                // Found the first sequence of k consecutive integers
                // You can store this result or print it
                cout << "Consecutive integers found: ";
                for (int val : result) {
                    cout << val << " ";
                }
                cout << endl;
            }
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of integers in the stream, because each integer is processed once and we only extend sequences when a new integer is added.
> - **Space Complexity:** $O(n)$ for storing all unique integers in the stream.
> - **Optimality proof:** This approach is optimal because it checks each new integer against the possibility of extending an existing sequence, ensuring that the first sequence of length $k$ is found as soon as possible.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Efficient sequence detection, use of a set for fast lookup.
- Problem-solving patterns identified: Maintaining a sliding window or tracking longest sequences seen so far.
- Optimization techniques learned: Reducing the number of checks by only considering new integers against existing sequences.
- Similar problems to practice: Other sequence detection problems, such as finding the longest increasing subsequence.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases like an empty stream or sequences of length 1.
- Edge cases to watch for: Handling negative integers and sequences that start with a negative number.
- Performance pitfalls: Using inefficient data structures or algorithms that scale poorly with the size of the input.
- Testing considerations: Thoroughly testing with different sequence lengths, start points, and edge cases.