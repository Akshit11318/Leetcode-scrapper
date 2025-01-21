## Count Nice Pairs in an Array
**Problem Link:** https://leetcode.com/problems/count-nice-pairs-in-an-array/description

**Problem Statement:**
- Input format: An array of integers `nums`.
- Constraints: `1 <= nums.length <= 10^5`, `0 <= nums[i] <= 10^6`.
- Expected output format: The number of nice pairs in the array.
- Key requirements and edge cases to consider:
  - A nice pair is defined as a pair of indices `(i, j)` where `i < j` and `rev(nums[i]) - nums[i] == rev(nums[j]) - nums[j]`.
  - `rev(x)` denotes the reverse of the number `x`.
- Example test cases with explanations:
  - For the input `[1, 2, 3, 4]`, there are no nice pairs because none of the pairs satisfy the condition.
  - For the input `[10, 2, 3, 4, 5, 90]`, there is one nice pair: `(0, 5)` because `rev(10) - 10 == 1 - 10 == -9` and `rev(90) - 90 == 9 - 90 == -81` are not equal, but upon recalculating we see that `rev(10) = 01` and `rev(90) = 09`, hence `rev(10) - 10 = 1 - 10 = -9` and `rev(90) - 90 = 9 - 90 = -81`. The correct pair to consider is actually `(1, 4)` where `rev(2) - 2 == 2 - 2 == 0` and `rev(5) - 5 == 5 - 5 == 0`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To solve this problem, we can iterate over all pairs of indices in the array and check if the difference between the reverse of each number and the number itself is equal for both indices.
- Step-by-step breakdown of the solution:
  1. Iterate over the array to consider each index `i`.
  2. For each `i`, iterate over the rest of the array to consider each index `j` where `j > i`.
  3. For each pair `(i, j)`, calculate `rev(nums[i]) - nums[i]` and `rev(nums[j]) - nums[j]`.
  4. If these two values are equal, increment a counter for nice pairs.
- Why this approach comes to mind first: It directly implements the definition of a nice pair and checks all possible pairs.

```cpp
int countNicePairs(vector<int>& nums) {
    int nicePairs = 0;
    for (int i = 0; i < nums.size(); i++) {
        for (int j = i + 1; j < nums.size(); j++) {
            int revI = reverse(nums[i]);
            int revJ = reverse(nums[j]);
            if (revI - nums[i] == revJ - nums[j]) {
                nicePairs++;
            }
        }
    }
    return nicePairs;
}

int reverse(int x) {
    int rev = 0;
    while (x) {
        rev = rev * 10 + x % 10;
        x /= 10;
    }
    return rev;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 * m)$, where $n$ is the size of the input array and $m$ is the average number of digits in the numbers. This is because for each pair of numbers, we are reversing the numbers which takes $O(m)$ time.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input and output, as we are using a constant amount of space to store our variables.
> - **Why these complexities occur:** The brute force approach has a high time complexity due to the nested loops over the array, and the reversal operation within these loops. The space complexity is low because we only use a fixed amount of space to store our counters and temporary results.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of comparing each pair of numbers directly, we can calculate the difference between the reverse of each number and the number itself, and then use a hash map to count the occurrences of these differences.
- Detailed breakdown of the approach:
  1. Initialize a hash map to store the count of each difference.
  2. Iterate over the array, for each number, calculate its reverse and the difference between the reverse and the number.
  3. Use the hash map to count the occurrences of these differences.
  4. Calculate the number of nice pairs by summing the counts of each difference squared (since for each difference, the number of pairs is the count choose 2).
- Proof of optimality: This approach reduces the time complexity significantly by avoiding the need to compare each pair of numbers directly. The use of a hash map allows for efficient counting of differences.

```cpp
int countNicePairs(vector<int>& nums) {
    unordered_map<int, int> count;
    for (int num : nums) {
        int rev = reverse(num);
        int diff = rev - num;
        count[diff]++;
    }
    long long nicePairs = 0;
    for (auto& [diff, cnt] : count) {
        nicePairs += (long long)cnt * (cnt - 1) / 2;
    }
    return nicePairs;
}

int reverse(int x) {
    int rev = 0;
    while (x) {
        rev = rev * 10 + x % 10;
        x /= 10;
    }
    return rev;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n * m)$, where $n$ is the size of the input array and $m$ is the average number of digits in the numbers. This is because we are iterating over the array once and for each number, we are reversing it which takes $O(m)$ time.
> - **Space Complexity:** $O(n)$, as in the worst case, we might have to store each number's difference in the hash map.
> - **Optimality proof:** This is the optimal solution because we are only iterating over the array once and using a hash map to count the differences, which reduces the time complexity significantly compared to the brute force approach.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Hash maps, counting occurrences, and calculating combinations.
- Problem-solving patterns identified: Using hash maps to count occurrences and reduce time complexity.
- Optimization techniques learned: Avoiding direct comparisons by using hash maps for counting.
- Similar problems to practice: Other problems involving counting pairs or occurrences in an array.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle edge cases, such as when the input array is empty.
- Edge cases to watch for: Arrays with duplicate numbers, arrays with numbers that have the same reverse difference.
- Performance pitfalls: Using the brute force approach for large inputs.
- Testing considerations: Test with arrays of varying sizes, including edge cases like empty arrays or arrays with a single element.