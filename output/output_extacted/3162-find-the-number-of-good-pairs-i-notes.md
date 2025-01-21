## Find the Number of Good Pairs I

**Problem Link:** https://leetcode.com/problems/find-the-number-of-good-pairs-i/description

**Problem Statement:**
- Input: An array of integers `nums`.
- Constraints: `1 <= nums.length <= 100`, `1 <= nums[i] <= 100`.
- Expected output: The number of good pairs.
- Key requirements: A good pair is a pair `(i, j)` where `i < j` and `nums[i] == nums[j]`.
- Example test cases:
  - Input: `nums = [1,2,3,1,1,3]`
  - Output: `4`
  - Explanation: The good pairs are `(0,3)`, `(0,4)`, `(3,4)`, `(2,5)`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through all pairs of numbers in the array and count the pairs where the numbers are equal.
- Step-by-step breakdown of the solution:
  1. Initialize a variable `count` to store the number of good pairs.
  2. Iterate through the array using two nested loops to generate all pairs of indices `(i, j)` where `i < j`.
  3. For each pair `(i, j)`, check if `nums[i] == nums[j]`. If true, increment the `count`.
  4. Return the `count` as the result.

```cpp
int numIdenticalPairs(vector<int>& nums) {
    int count = 0;
    int n = nums.size();
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (nums[i] == nums[j]) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ where $n$ is the length of the input array. This is because we are using two nested loops to iterate through all pairs of indices.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input and output. We are only using a constant amount of space to store the count and indices.
> - **Why these complexities occur:** The time complexity is quadratic because we are generating all pairs of indices, resulting in $n*(n-1)/2$ comparisons. The space complexity is constant because we are not using any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of comparing each pair of numbers, we can use a frequency count to calculate the number of good pairs directly.
- Detailed breakdown of the approach:
  1. Initialize a map `freq` to store the frequency of each number in the array.
  2. Iterate through the array and update the frequency count for each number.
  3. For each frequency count `f`, calculate the number of good pairs as `f*(f-1)/2` and add it to the total count.
  4. Return the total count as the result.

```cpp
int numIdenticalPairs(vector<int>& nums) {
    map<int, int> freq;
    for (int num : nums) {
        freq[num]++;
    }
    int count = 0;
    for (auto& pair : freq) {
        int f = pair.second;
        count += f * (f - 1) / 2;
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the length of the input array. This is because we are iterating through the array twice: once to count the frequencies and once to calculate the good pairs.
> - **Space Complexity:** $O(n)$, because in the worst case, every number in the array could be unique, resulting in a frequency map with $n$ entries.
> - **Optimality proof:** This approach is optimal because it reduces the number of comparisons from $O(n^2)$ to $O(n)$, which is the minimum required to process each element in the input array.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Frequency counting and the formula for combinations (`n*(n-1)/2`).
- Problem-solving patterns identified: Using a frequency count to avoid redundant comparisons.
- Optimization techniques learned: Reducing the number of comparisons by using a frequency count.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle edge cases (e.g., an empty input array).
- Edge cases to watch for: Input arrays with duplicate numbers, input arrays with a single element.
- Performance pitfalls: Using a brute force approach for large input arrays.
- Testing considerations: Testing the function with various input arrays, including edge cases.