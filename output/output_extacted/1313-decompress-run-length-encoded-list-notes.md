## Decompress Run-Length Encoded List
**Problem Link:** https://leetcode.com/problems/decompress-run-length-encoded-list/description

**Problem Statement:**
- Input format: A list of integers `nums` where each pair of integers represents the frequency and value of a number in the decompressed list.
- Constraints: The input list is in the format of pairs (i.e., its length is even), and the length of the input list is in the range `[1, 100]`.
- Expected output format: A list of integers where each number appears as many times as specified by its corresponding frequency.
- Key requirements and edge cases to consider: The input list must be processed in pairs, and each pair must be used to generate the decompressed list.

**Example Test Cases:**
- For input `nums = [1,2,3,4]`, the output should be `[2,4,4,4]` because the first pair `[1,2]` means the number `2` appears once, and the second pair `[3,4]` means the number `4` appears three times.
- For input `nums = [1,1,2,3]`, the output should be `[1,3,3]` because the first pair `[1,1]` means the number `1` appears once, and the second pair `[2,3]` means the number `3` appears twice.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To decompress the list, we need to iterate through the input list in pairs, using each pair to generate the decompressed list.
- Step-by-step breakdown of the solution:
  1. Initialize an empty list `result` to store the decompressed numbers.
  2. Iterate through the input list `nums` in steps of 2 (since each pair of numbers represents a frequency and a value).
  3. For each pair of numbers, append the value to the `result` list as many times as specified by the frequency.
- Why this approach comes to mind first: It directly follows from the problem statement, which asks us to decompress the list based on the given frequencies and values.

```cpp
vector<int> decompressRLElist(vector<int>& nums) {
    vector<int> result;
    for (int i = 0; i < nums.size(); i += 2) {
        int freq = nums[i];
        int val = nums[i + 1];
        for (int j = 0; j < freq; j++) {
            result.push_back(val);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of pairs in the input list and $m$ is the maximum frequency. This is because in the worst case, we are iterating through the input list and for each pair, we are potentially appending a value to the result list up to `m` times.
> - **Space Complexity:** $O(n \cdot m)$, as the size of the output list can grow up to $n \cdot m$ in the worst case.
> - **Why these complexities occur:** The time complexity is due to the nested loop structure (iterating over pairs and then potentially appending up to `m` times for each pair), and the space complexity is due to storing the decompressed list.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The problem doesn't require any complex data structures or algorithms beyond simple iteration and appending to a list. Thus, the brute force approach is already quite straightforward and efficient for this problem.
- Detailed breakdown of the approach: Same as the brute force approach, as it is already optimal for this problem.
- Proof of optimality: Since we must process each pair of numbers in the input list and potentially append up to `m` values for each pair, the time complexity of $O(n \cdot m)$ is optimal. Similarly, the space complexity of $O(n \cdot m)$ is necessary to store the output.

```cpp
vector<int> decompressRLElist(vector<int>& nums) {
    vector<int> result;
    for (int i = 0; i < nums.size(); i += 2) {
        int freq = nums[i];
        int val = nums[i + 1];
        result.insert(result.end(), freq, val);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of pairs and $m$ is the maximum frequency. This is because we are iterating through the input list and for each pair, we are inserting up to `m` values into the result list.
> - **Space Complexity:** $O(n \cdot m)$, as the size of the output list can grow up to $n \cdot m$ in the worst case.
> - **Optimality proof:** The time and space complexities are optimal because we must process each input pair and store the output, and the given approach does so with the minimum necessary operations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, conditional statements, and list manipulation.
- Problem-solving patterns identified: Directly applying the problem statement to the solution, using iteration to process pairs of numbers.
- Optimization techniques learned: Recognizing when the initial approach is already optimal, understanding the importance of considering the size and complexity of the input and output.
- Similar problems to practice: Other problems involving list manipulation, iteration, and basic algorithmic concepts.

**Mistakes to Avoid:**
- Common implementation errors: Off-by-one errors in iteration, incorrect handling of edge cases (e.g., empty input list).
- Edge cases to watch for: Input lists with odd lengths (which should not occur according to the problem statement but could be a consideration in similar problems), handling of zero frequencies.
- Performance pitfalls: Unnecessary complexity in the solution, failing to consider the size and structure of the input and output.
- Testing considerations: Ensuring that the solution works correctly for various input sizes, frequencies, and values, including edge cases.