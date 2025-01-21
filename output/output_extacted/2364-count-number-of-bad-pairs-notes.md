## Count Number of Bad Pairs
**Problem Link:** https://leetcode.com/problems/count-number-of-bad-pairs/description

**Problem Statement:**
- Input format: `n` integers in an array `nums`.
- Constraints: `1 <= n <= 10^5`, `1 <= nums[i] <= 10^9`.
- Expected output: The number of bad pairs, where a bad pair is a pair `(i, j)` such that `i < j` and `nums[i] - i != nums[j] - j`.
- Key requirements and edge cases to consider: Handling large inputs and avoiding unnecessary comparisons.
- Example test cases:
  - `nums = [1,2,3,4,5]`, output: `0`.
  - `nums = [1,1,1,1,1]`, output: `10`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Compare each pair of elements to check if they form a bad pair.
- Step-by-step breakdown:
  1. Iterate over the array with two nested loops to consider all pairs of elements.
  2. For each pair `(i, j)`, check if `nums[i] - i != nums[j] - j`.
  3. If the condition is true, increment the count of bad pairs.

```cpp
int countBadPairs(vector<int>& nums) {
    int n = nums.size();
    int bad = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (nums[i] - i != nums[j] - j) {
                bad++;
            }
        }
    }
    return bad;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of elements in the array. This is because we are using two nested loops to compare all pairs of elements.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the count of bad pairs.
> - **Why these complexities occur:** The brute force approach has a high time complexity due to the nested loops, making it inefficient for large inputs.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: Instead of comparing each pair directly, we can use a hashmap to count the frequency of each difference `nums[i] - i`.
- Detailed breakdown:
  1. Initialize a hashmap `freq` to store the frequency of each difference.
  2. Iterate over the array, and for each element `nums[i]`, calculate the difference `diff = nums[i] - i`.
  3. Increment the frequency of `diff` in the hashmap.
  4. Calculate the total number of pairs that are not bad by summing the squares of the frequencies (since for each frequency `f`, there are `f*(f-1)/2` pairs that have the same difference).
  5. The total number of bad pairs is the total number of pairs minus the number of pairs that are not bad.

```cpp
int countBadPairs(vector<int>& nums) {
    int n = nums.size();
    unordered_map<int, int> freq;
    long long good = 0;
    for (int i = 0; i < n; i++) {
        int diff = nums[i] - i;
        good += freq[diff];
        freq[diff]++;
    }
    long long total = (long long)n * (n - 1) / 2;
    return total - good;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array. This is because we are iterating over the array once and performing constant-time operations for each element.
> - **Space Complexity:** $O(n)$, as in the worst case, we might need to store all elements in the hashmap.
> - **Optimality proof:** This approach is optimal because it avoids unnecessary comparisons and only requires a single pass over the input array.

---

### Final Notes
**Learning Points:**
- Key algorithmic concepts demonstrated: Using a hashmap to count frequencies and avoid unnecessary comparisons.
- Problem-solving patterns identified: Looking for ways to reduce the number of comparisons and using data structures to store and retrieve information efficiently.
- Optimization techniques learned: Avoiding nested loops and using single-pass algorithms when possible.

**Mistakes to Avoid:**
- Common implementation errors: Failing to handle edge cases or using incorrect data structures.
- Edge cases to watch for: Handling large inputs and avoiding overflows.
- Performance pitfalls: Using inefficient algorithms or data structures that lead to high time or space complexities.
- Testing considerations: Testing the algorithm with various inputs, including edge cases and large inputs, to ensure correctness and efficiency.