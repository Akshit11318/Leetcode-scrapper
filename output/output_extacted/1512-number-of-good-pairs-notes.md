## Number of Good Pairs

**Problem Link:** https://leetcode.com/problems/number-of-good-pairs/description

**Problem Statement:**
- Input: An array of integers `nums`.
- Constraints: `1 <= nums.length <= 100`, `1 <= nums[i] <= 100`.
- Expected Output: The number of good pairs, where a good pair is defined as two indices `i` and `j` such that `i < j` and `nums[i] == nums[j]`.
- Key Requirements: Count all unique pairs of indices that satisfy the condition.
- Edge Cases: Empty array, array with a single element, array with all unique elements.

**Example Test Cases:**
- Input: `nums = [1,2,3,1,1,3]`
  Output: `4`
  Explanation: The good pairs are `(0,3)`, `(0,4)`, `(3,4)`, `(2,5)`.
- Input: `nums = [1,1,1,1]`
  Output: `6`
  Explanation: The good pairs are `(0,1)`, `(0,2)`, `(0,3)`, `(1,2)`, `(1,3)`, `(2,3)`.
- Input: `nums = [1,2,3]`
  Output: `0`
  Explanation: There are no good pairs.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through the array for each element and check every other element to its right.
- Step-by-step breakdown:
  1. Initialize a counter for good pairs.
  2. Iterate through the array with two nested loops, where the inner loop starts from the next index of the outer loop.
  3. Inside the inner loop, check if the current elements of both loops are equal. If they are, increment the counter.
- Why this approach comes to mind first: It's straightforward and directly implements the problem's definition.

```cpp
int numIdenticalPairs(vector<int>& nums) {
    int goodPairs = 0;
    for (int i = 0; i < nums.size(); i++) {
        for (int j = i + 1; j < nums.size(); j++) {
            if (nums[i] == nums[j]) {
                goodPairs++;
            }
        }
    }
    return goodPairs;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the size of the input array `nums`. This is because we are using two nested loops to compare each pair of elements.
> - **Space Complexity:** $O(1)$, as we are using a constant amount of space to store the count of good pairs.
> - **Why these complexities occur:** The nested loops cause the quadratic time complexity, while the constant space usage is due to only using a single variable to store the count.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of comparing each pair of elements directly, we can count the occurrences of each number and then calculate the number of good pairs for each count.
- Detailed breakdown:
  1. Create a frequency map to count the occurrences of each number.
  2. For each count in the frequency map, calculate the number of good pairs using the formula $\frac{n(n-1)}{2}$, where $n$ is the count.
  3. Sum up the good pairs for all counts to get the total.
- Proof of optimality: This approach reduces the time complexity to linear by avoiding the need for nested loops.

```cpp
int numIdenticalPairs(vector<int>& nums) {
    unordered_map<int, int> freqMap;
    for (int num : nums) {
        freqMap[num]++;
    }
    int goodPairs = 0;
    for (auto& pair : freqMap) {
        int count = pair.second;
        if (count > 1) {
            goodPairs += (count * (count - 1)) / 2;
        }
    }
    return goodPairs;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of the input array `nums`. This is because we make two passes through the data: one to count the frequencies and another to calculate the good pairs.
> - **Space Complexity:** $O(n)$, as in the worst case, every element in `nums` could be unique, requiring space proportional to $n$ for the frequency map.
> - **Optimality proof:** This is the most efficient approach because we only need to make two linear passes through the data, and we avoid the $O(n^2)$ complexity of comparing each pair directly.

---

### Final Notes

**Learning Points:**
- The importance of frequency maps or hash tables in solving problems involving counts or frequencies.
- How to calculate combinations using the formula $\frac{n(n-1)}{2}$.
- The trade-off between time and space complexity, as seen in the optimal approach where we use more space to achieve linear time complexity.

**Mistakes to Avoid:**
- Directly comparing each pair of elements without considering more efficient data structures or algorithms.
- Not considering edge cases, such as an empty array or an array with a single element.
- Failing to optimize the solution by not recognizing the pattern that allows for the use of a frequency map.