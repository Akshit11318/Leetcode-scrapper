## Find All Numbers Disappeared in an Array

**Problem Link:** https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description

**Problem Statement:**
- Input format: An array of integers `nums` containing `n` elements, where each element is in the range `[1, n]`.
- Constraints: `1 <= n <= 10^5`.
- Expected output format: A vector of integers representing the numbers in the range `[1, n]` that do not appear in `nums`.
- Key requirements and edge cases to consider:
  - The input array may contain duplicates.
  - The output should not contain duplicates.
  - The numbers in the output should be in ascending order.
- Example test cases with explanations:
  - Input: `nums = [4,3,2,7,8,2,3,1]`, Output: `[5,6]`
  - Input: `nums = [1,1]`, Output: `[2]`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check each number in the range `[1, n]` to see if it exists in the input array `nums`.
- Step-by-step breakdown of the solution:
  1. Create an empty vector `result` to store the disappeared numbers.
  2. Iterate through each number `i` in the range `[1, n]`.
  3. For each number `i`, check if it exists in the input array `nums`.
  4. If `i` does not exist in `nums`, add it to the `result` vector.
- Why this approach comes to mind first: It is a straightforward and intuitive solution that directly addresses the problem statement.

```cpp
vector<int> findDisappearedNumbers(vector<int>& nums) {
    int n = nums.size();
    vector<int> result;
    for (int i = 1; i <= n; i++) {
        bool found = false;
        for (int j = 0; j < n; j++) {
            if (nums[j] == i) {
                found = true;
                break;
            }
        }
        if (!found) {
            result.push_back(i);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the size of the input array `nums`. This is because we have a nested loop structure, where the outer loop runs $n$ times and the inner loop also runs $n$ times.
> - **Space Complexity:** $O(n)$, where $n$ is the size of the input array `nums`. This is because in the worst case, all numbers in the range `[1, n]` might be missing from `nums`, resulting in a `result` vector of size $n$.
> - **Why these complexities occur:** The brute force approach has high time complexity due to the nested loop structure, which leads to a quadratic increase in computation time as the input size increases. The space complexity is linear because we are storing the disappeared numbers in a separate vector.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can utilize the input array `nums` itself as extra space to mark the presence of each number in the range `[1, n]`.
- Detailed breakdown of the approach:
  1. Iterate through each number `i` in the input array `nums`.
  2. For each number `i`, use it as an index to mark the presence of `i` in the array. We can do this by taking the absolute value of the number at index `i-1` and negating it. This effectively marks the presence of `i` without modifying the original value.
  3. After marking the presence of all numbers, iterate through the array again to find the indices where the numbers are still positive. These indices correspond to the numbers that are missing from the array.
- Proof of optimality: This approach has a time complexity of $O(n)$ and a space complexity of $O(1)$, making it optimal for this problem.

```cpp
vector<int> findDisappearedNumbers(vector<int>& nums) {
    int n = nums.size();
    vector<int> result;
    for (int i = 0; i < n; i++) {
        int index = abs(nums[i]) - 1;
        if (nums[index] > 0) {
            nums[index] = -nums[index];
        }
    }
    for (int i = 0; i < n; i++) {
        if (nums[i] > 0) {
            result.push_back(i + 1);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of the input array `nums`. This is because we have two separate loops, each running $n$ times.
> - **Space Complexity:** $O(1)$, excluding the space needed for the output vector `result`. This is because we are using the input array `nums` itself as extra space to mark the presence of each number.
> - **Optimality proof:** The optimal approach has a linear time complexity and constant space complexity, making it the most efficient solution for this problem.