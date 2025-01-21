## Find the Score of All Prefixes of an Array
**Problem Link:** https://leetcode.com/problems/find-the-score-of-all-prefixes-of-an-array/description

**Problem Statement:**
- Input: A non-empty array of integers `nums`.
- Output: An array of integers where the `i-th` element is the score of the prefix from index `0` to `i`.
- Key Requirements:
  - The score of a prefix is the sum of all elements in the prefix.
- Edge Cases:
  - The input array `nums` is guaranteed to be non-empty.
- Example Test Cases:
  - Input: `nums = [2,3,7,5,10]`
    - Output: `[2,5,12,17,27]`
  - Input: `nums = [1,2,3,4,5]`
    - Output: `[1,3,6,10,15]`

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to calculate the sum of all elements up to each index `i` in the array `nums`.
- This involves iterating through the array and for each index, summing all elements from the start of the array to that index.
- This approach comes to mind first because it directly implements the definition of the prefix sum.

```cpp
vector<int> findPrefixScore(vector<int>& nums) {
    int n = nums.size();
    vector<int> scores(n);
    for (int i = 0; i < n; i++) {
        int sum = 0;
        for (int j = 0; j <= i; j++) {
            sum += nums[j];
        }
        scores[i] = sum;
    }
    return scores;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of elements in the array. This is because for each of the $n$ elements, we potentially sum all previous elements, leading to a quadratic time complexity.
> - **Space Complexity:** $O(n)$, as we need to store the scores of all prefixes in an array of size $n$.
> - **Why these complexities occur:** The quadratic time complexity arises from the nested loops, where the inner loop sums elements up to the current index in the outer loop. The linear space complexity is due to storing the scores for each prefix.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to recognize that the score of each prefix can be calculated by adding the current element to the score of the previous prefix.
- This approach avoids the need for nested loops and thus significantly reduces the computational complexity.
- We initialize the score of the first prefix as the first element of the array and then iteratively calculate the scores of subsequent prefixes.

```cpp
vector<int> findPrefixScore(vector<int>& nums) {
    int n = nums.size();
    vector<int> scores(n);
    scores[0] = nums[0];
    for (int i = 1; i < n; i++) {
        scores[i] = scores[i-1] + nums[i];
    }
    return scores;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array. This linear time complexity arises from a single pass through the array.
> - **Space Complexity:** $O(n)$, as we still need to store the scores of all prefixes in an array of size $n$.
> - **Optimality proof:** This approach is optimal because it achieves a linear time complexity, which is the best possible for this problem since we must at least read the input array once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concept demonstrated: **Prefix Sum** or **Cumulative Sum**, which is a common technique used in array and string processing problems.
- Problem-solving pattern identified: Recognizing that a problem can be solved more efficiently by avoiding redundant calculations and using the results of previous computations.
- Optimization technique learned: **Dynamic Programming** or more specifically, a simple form of it where we build up a solution by iteratively adding to the solution of a smaller subproblem.

**Mistakes to Avoid:**
- Common implementation error: Not initializing the first element of the `scores` array correctly.
- Edge case to watch for: While the problem guarantees a non-empty array, it's always good practice to validate inputs and handle potential edge cases explicitly.
- Performance pitfall: Failing to recognize the opportunity to use a cumulative sum approach and instead using a brute force method with unnecessary nested loops.