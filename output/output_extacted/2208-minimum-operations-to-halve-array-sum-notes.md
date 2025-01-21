## Minimum Operations to Halve Array Sum
**Problem Link:** https://leetcode.com/problems/minimum-operations-to-halve-array-sum/description

**Problem Statement:**
- Input: A non-empty array of integers `nums`.
- Constraints: `1 <= nums.length <= 10^5`, `1 <= nums[i] <= 10^5`.
- Expected Output: The minimum number of operations required to halve the sum of the array.
- Key Requirements: Find the minimum number of operations to reduce the array sum to half or less.
- Edge Cases: Consider arrays with negative numbers, zero, or very large numbers.

**Example Test Cases:**
- `nums = [5,6,8]`, the output should be `3` because `5 + 6 + 8 = 19`, and after halving `8` twice and `6` once, the sum becomes `5 + 3 + 4 = 12`, which is less than half of `19`.
- `nums = [1,2,3]`, the output should be `3` because `1 + 2 + 3 = 6`, and after halving each number once, the sum becomes `0.5 + 1 + 1.5 = 3`, which is half of `6`.

---

### Brute Force Approach
**Explanation:**
- Sort the array in descending order to prioritize larger numbers.
- Iterate through the sorted array and halve each number until the sum is halved.
- Count the number of halving operations performed.

```cpp
int minOperations(vector<int>& nums) {
    int sum = 0;
    for (int num : nums) sum += num;
    target = sum / 2;
    sort(nums.rbegin(), nums.rend());
    int operations = 0;
    while (sum > target) {
        for (int i = 0; i < nums.size(); i++) {
            if (sum > target) {
                sum -= nums[i] / 2;
                nums[i] /= 2;
                operations++;
            }
        }
    }
    return operations;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \log n)$ due to sorting and nested loops.
> - **Space Complexity:** $O(1)$ as we are modifying the input array in-place.
> - **Why these complexities occur:** The brute force approach involves sorting the array and then iterating through it, which leads to a high time complexity.

---

### Optimal Approach (Required)
**Explanation:**
- Sort the array in descending order to prioritize larger numbers.
- Use a priority queue to efficiently select the largest number to halve in each iteration.
- Continue halving numbers until the sum is halved.

```cpp
int minOperations(vector<int>& nums) {
    int sum = 0;
    for (int num : nums) sum += num;
    int target = sum / 2;
    priority_queue<int> pq;
    for (int num : nums) pq.push(num);
    int operations = 0;
    while (sum > target) {
        int num = pq.top();
        pq.pop();
        sum -= num / 2;
        pq.push(num / 2);
        operations++;
    }
    return operations;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to sorting and priority queue operations.
> - **Space Complexity:** $O(n)$ for the priority queue.
> - **Optimality proof:** This approach is optimal because it always selects the largest number to halve in each iteration, which minimizes the number of operations required.

---

### Final Notes

**Learning Points:**
- The importance of prioritizing larger numbers when reducing the sum.
- The use of priority queues for efficient selection of the largest number.
- The trade-off between time and space complexity in different approaches.

**Mistakes to Avoid:**
- Not considering the impact of integer division on the halving operation.
- Not checking for edge cases such as empty arrays or arrays with very large numbers.
- Not optimizing the solution for time and space complexity.