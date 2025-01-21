## Maximum Number of Operations with the Same Score I

**Problem Link:** https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-i/description

**Problem Statement:**
- Input format: Two arrays `nums` and `k`, where `nums` is an array of integers and `k` is an integer.
- Constraints: $1 \leq nums.length \leq 10^5$ and $1 \leq k \leq 10^9$.
- Expected output format: The maximum number of operations that can be performed with the same score.
- Key requirements and edge cases to consider: The score is calculated by taking the absolute difference between each pair of elements and adding them to the score.
- Example test cases with explanations:
  - Example 1: Input: `nums = [2,3,2,4], k = 3`, Output: `2`. Explanation: We can perform two operations: (2, 3) and (2, 4).
  - Example 2: Input: `nums = [1,1,1,1], k = 3`, Output: `0`. Explanation: No operations can be performed.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible pairs of elements and calculate the score for each pair.
- Step-by-step breakdown of the solution:
  1. Generate all possible pairs of elements from the `nums` array.
  2. For each pair, calculate the score by taking the absolute difference between the two elements.
  3. Check if the score is less than or equal to `k`.
  4. If the score is less than or equal to `k`, increment the count of operations.
- Why this approach comes to mind first: It is a straightforward and intuitive approach that tries all possible combinations.

```cpp
int maxOperations(vector<int>& nums, int k) {
    int count = 0;
    for (int i = 0; i < nums.size(); i++) {
        for (int j = i + 1; j < nums.size(); j++) {
            if (abs(nums[i] - nums[j]) <= k) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the `nums` array. This is because we have two nested loops that iterate over the array.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the count of operations.
> - **Why these complexities occur:** The time complexity is quadratic because we generate all possible pairs of elements, and the space complexity is constant because we only use a fixed amount of space.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a `unordered_map` to store the frequency of each element in the `nums` array, and then iterate over the map to find the pairs of elements that have a score less than or equal to `k`.
- Detailed breakdown of the approach:
  1. Create an `unordered_map` to store the frequency of each element in the `nums` array.
  2. Iterate over the `nums` array and update the frequency of each element in the map.
  3. Initialize a count of operations to 0.
  4. Iterate over the map and for each element, find the pairs of elements that have a score less than or equal to `k`.
  5. For each pair, increment the count of operations.
- Proof of optimality: This approach is optimal because it has a time complexity of $O(n)$, which is the best possible time complexity for this problem.

```cpp
int maxOperations(vector<int>& nums, int k) {
    unordered_map<int, int> freq;
    for (int num : nums) {
        freq[num]++;
    }
    int count = 0;
    for (auto& pair : freq) {
        int num = pair.first;
        int freqNum = pair.second;
        if (freq.find(num + k) != freq.end()) {
            int freqNumPlusK = freq[num + k];
            count += min(freqNum, freqNumPlusK);
        }
    }
    return count / 2;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the `nums` array. This is because we iterate over the array once to update the frequency of each element, and then iterate over the map to find the pairs of elements.
> - **Space Complexity:** $O(n)$, as we use an `unordered_map` to store the frequency of each element.
> - **Optimality proof:** This approach is optimal because it has a time complexity of $O(n)$, which is the best possible time complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using an `unordered_map` to store the frequency of each element, and iterating over the map to find the pairs of elements that have a score less than or equal to `k`.
- Problem-solving patterns identified: Using a frequency map to solve problems that involve finding pairs of elements with a certain property.
- Optimization techniques learned: Using an `unordered_map` to reduce the time complexity of the solution.
- Similar problems to practice: Problems that involve finding pairs of elements with a certain property, such as finding pairs of elements that have a sum equal to a target value.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to update the frequency of each element in the map, or forgetting to increment the count of operations for each pair of elements that have a score less than or equal to `k`.
- Edge cases to watch for: The case where the `nums` array is empty, or the case where `k` is 0.
- Performance pitfalls: Using a nested loop to iterate over the `nums` array, which can result in a time complexity of $O(n^2)$.
- Testing considerations: Testing the solution with different inputs, such as an empty array or an array with a single element, to ensure that it handles all edge cases correctly.