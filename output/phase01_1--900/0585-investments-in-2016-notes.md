## Investments in 2016
**Problem Link:** https://leetcode.com/problems/investments-in-2016/description

**Problem Statement:**
- The problem requires finding the maximum number of investments that can be made in 2016, given the `investments` array where each element is a subarray containing the `id`, `amount`, and `currency` of an investment.
- Input format: `investments` array.
- Constraints: Each `id` is unique, and the `amount` is always positive.
- Expected output format: The maximum number of investments that can be made.
- Key requirements and edge cases to consider: Handling cases where there are no investments, or when the `amount` is zero.

**Example Test Cases:**
- `investments = [[1, 1000, 'USD'], [2, 2000, 'EUR'], [3, 3000, 'GBP']]`
- `investments = []`
- `investments = [[1, 0, 'USD']]`

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to iterate over each investment and count the number of unique `id`s.
- This approach comes to mind first because it directly addresses the problem statement by counting each investment.

```cpp
int maxInvestments(vector<vector<int>>& investments) {
    int count = 0;
    for (auto& investment : investments) {
        count++;
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of investments, because we iterate over each investment once.
> - **Space Complexity:** $O(1)$, because we use a constant amount of space to store the count.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each investment, and the space complexity is constant because we only use a fixed amount of space to store the count.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is recognizing that the problem is simply asking for the number of investments, which can be found by getting the size of the `investments` array.
- This approach is optimal because it directly accesses the size of the array without needing to iterate over each element.

```cpp
int maxInvestments(vector<vector<int>>& investments) {
    return investments.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, because accessing the size of the array is a constant-time operation.
> - **Space Complexity:** $O(1)$, because we use a constant amount of space to store the result.
> - **Optimality proof:** This is the optimal solution because it achieves the minimum possible time complexity by directly accessing the size of the array without iterating over each element.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Direct array access, iteration.
- Problem-solving patterns identified: Recognizing when a problem can be solved by directly accessing the size of an array.
- Optimization techniques learned: Avoiding unnecessary iteration.
- Similar problems to practice: Problems that involve counting or accessing the size of a data structure.

**Mistakes to Avoid:**
- Common implementation errors: Unnecessary iteration, using a brute force approach when a more efficient solution exists.
- Edge cases to watch for: Empty arrays, arrays with zero elements.
- Performance pitfalls: Using a brute force approach for large inputs.
- Testing considerations: Test with empty arrays, arrays with one element, and large arrays to ensure the solution works correctly in all cases.