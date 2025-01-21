## Sort Array By Parity II
**Problem Link:** https://leetcode.com/problems/sort-array-by-parity-ii/description

**Problem Statement:**
- Input format and constraints: Given an array `nums` of size `n`, where each element is an integer, and `n` is even. 
- Expected output format: Return an array where all even integers are at even indices and all odd integers are at odd indices.
- Key requirements and edge cases to consider: The input array will always have an even length. All elements in the array will be integers.
- Example test cases with explanations:
    - Input: `nums = [4,2,5,7]`
      Output: `[4,5,2,7]`
    - Input: `nums = [2,3]`
      Output: `[2,3]`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The most straightforward approach is to separate the even and odd numbers into two different arrays and then merge them, placing even numbers at even indices and odd numbers at odd indices.
- Step-by-step breakdown of the solution:
    1. Initialize two empty arrays, `even` and `odd`, to store even and odd numbers respectively.
    2. Iterate through the input array `nums`. For each number, check if it's even or odd and append it to the corresponding array.
    3. Initialize an empty array `result` to store the final sorted array.
    4. Iterate through the `even` and `odd` arrays simultaneously, placing even numbers at even indices and odd numbers at odd indices in the `result` array.
- Why this approach comes to mind first: It's a straightforward and intuitive approach that directly addresses the problem statement.

```cpp
vector<int> sortArrayByParityII(vector<int>& nums) {
    vector<int> even, odd, result;
    for (int num : nums) {
        if (num % 2 == 0) even.push_back(num);
        else odd.push_back(num);
    }
    for (int i = 0; i < nums.size() / 2; i++) {
        result.push_back(even[i]);
        result.push_back(odd[i]);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the input array. This is because we're iterating through the array three times: once to separate even and odd numbers, and twice to construct the final result.
> - **Space Complexity:** $O(n)$, as we're using additional space to store the `even`, `odd`, and `result` arrays.
> - **Why these complexities occur:** These complexities occur because of the additional space used to store the intermediate arrays and the linear time complexity of iterating through the arrays.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of using extra space to store even and odd numbers separately, we can achieve the same result by swapping elements in the original array when they are not in the correct position.
- Detailed breakdown of the approach:
    1. Initialize two pointers, `evenIndex` and `oddIndex`, starting at 0 and 1 respectively.
    2. Iterate through the array. If the current element at `evenIndex` is odd, swap it with the element at `oddIndex`.
    3. After swapping, move both pointers two steps forward.
- Proof of optimality: This approach is optimal because it only requires a single pass through the array and uses constant extra space, making it more efficient than the brute force approach.
- Why further optimization is impossible: This approach is already optimal in terms of time and space complexity, as it only requires a single pass through the array and uses constant extra space.

```cpp
vector<int> sortArrayByParityII(vector<int>& nums) {
    for (int evenIndex = 0, oddIndex = 1; evenIndex < nums.size(); evenIndex += 2, oddIndex += 2) {
        if (nums[evenIndex] % 2 != 0) {
            while (oddIndex < nums.size() && nums[oddIndex] % 2 != 0) {
                oddIndex += 2;
            }
            if (oddIndex < nums.size()) {
                swap(nums[evenIndex], nums[oddIndex]);
            }
        }
    }
    return nums;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the input array. This is because we're iterating through the array once.
> - **Space Complexity:** $O(1)$, as we're only using a constant amount of extra space to store the pointers.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the array and uses constant extra space.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Array manipulation, swapping elements, and using pointers to iterate through an array.
- Problem-solving patterns identified: Separating even and odd numbers, using extra space to store intermediate results, and optimizing the solution by reducing extra space usage.
- Optimization techniques learned: Reducing extra space usage by swapping elements in the original array instead of using separate arrays.
- Similar problems to practice: Other array manipulation problems, such as sorting arrays by parity or finding the first duplicate in an array.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as an empty input array or an array with an odd length.
- Edge cases to watch for: Handling arrays with an odd length, which is not applicable in this problem since the input array is guaranteed to have an even length.
- Performance pitfalls: Using extra space unnecessarily, which can increase the space complexity of the solution.
- Testing considerations: Testing the solution with different input arrays, including arrays with an even length and arrays with a mix of even and odd numbers.