## Max Number of K-Sum Pairs
**Problem Link:** https://leetcode.com/problems/max-number-of-k-sum-pairs/description

**Problem Statement:**
- Input format and constraints: Given an array of integers `nums` and an integer `k`, find the maximum number of pairs of elements in the array that sum to `k`.
- Expected output format: The maximum number of pairs.
- Key requirements and edge cases to consider: Handle cases where `nums` is empty, `k` is not found, or when there are multiple pairs with the same sum.
- Example test cases with explanations:
    - `nums = [1, 2, 3, 4], k = 7` returns 1 because the pair `(3, 4)` sums to 7.
    - `nums = [3, 1, 3, 4, 3], k = 6` returns 1 because the pair `(3, 3)` sums to 6.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The most straightforward way to find all pairs that sum to `k` is to check every possible pair of elements in the array.
- Step-by-step breakdown of the solution:
    1. Iterate over each element in the array.
    2. For each element, iterate over the rest of the elements in the array.
    3. Check if the sum of the current pair equals `k`.
    4. If it does, increment a counter.
- Why this approach comes to mind first: It's a direct and intuitive way to solve the problem, ensuring we don't miss any pairs.

```cpp
int maxNumberOfPairs(vector<int>& nums, int k) {
    int count = 0;
    for (int i = 0; i < nums.size(); i++) {
        for (int j = i + 1; j < nums.size(); j++) {
            if (nums[i] + nums[j] == k) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the size of the input array `nums`. This is because for each of the $n$ elements, we potentially iterate over the remaining $n-1$ elements.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input and output, as we only use a constant amount of space to store the count.
> - **Why these complexities occur:** The nested loops cause the quadratic time complexity, while the constant space usage is due to only needing a single variable to keep track of the count.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking every possible pair, we can use a hash map (or unordered map in C++) to store the frequency of each number we've seen so far. This way, when we encounter a new number, we can quickly check if its complement (the value needed to reach `k`) has been seen before.
- Detailed breakdown of the approach:
    1. Initialize an unordered map `freq` to store the frequency of each number.
    2. Initialize a variable `count` to store the maximum number of pairs.
    3. Iterate over the array `nums`. For each number `num`:
        - Check if its complement `k - num` is in `freq`.
        - If it is, increment `count` and decrement the frequency of the complement in `freq` to avoid counting the same pair twice.
        - Increment the frequency of `num` in `freq`.
- Proof of optimality: This approach ensures we find all pairs that sum to `k` without checking every possible pair, reducing the time complexity significantly.
- Why further optimization is impossible: We must at least look at each element once to determine if it can form a pair, making the linear time complexity optimal for this problem.

```cpp
int maxNumberOfPairs(vector<int>& nums, int k) {
    unordered_map<int, int> freq;
    int count = 0;
    for (int num : nums) {
        if (freq.find(k - num) != freq.end() && freq[k - num] > 0) {
            count++;
            freq[k - num]--;
        }
        freq[num]++;
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of the input array `nums`. This is because we make a single pass through the array.
> - **Space Complexity:** $O(n)$, as in the worst case, we might store every element in the hash map.
> - **Optimality proof:** The linear time complexity is optimal because we must examine each element at least once to determine if it can be part of a pair that sums to `k`.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using hash maps for efficient lookups and counting frequencies.
- Problem-solving patterns identified: Reducing the problem space by using complementary values to find pairs.
- Optimization techniques learned: Avoiding unnecessary iterations and using data structures to reduce time complexity.
- Similar problems to practice: Other problems involving finding pairs or combinations in arrays, such as two-sum or three-sum problems.

**Mistakes to Avoid:**
- Common implementation errors: Failing to handle edge cases like an empty input array or not initializing variables correctly.
- Edge cases to watch for: Handling duplicates and ensuring that each pair is only counted once.
- Performance pitfalls: Using brute force approaches for large inputs, leading to high time complexities.
- Testing considerations: Thoroughly testing with various inputs, including edge cases and large datasets, to ensure the solution is robust and efficient.