## Two Sum II - Input Array Is Sorted
**Problem Link:** https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description

**Problem Statement:**
- Input format: A sorted array of integers `numbers` and a target integer `target`.
- Constraints: The array `numbers` will have a length in the range $[2, 10^3]$ and the integers in the array will be in the range $[-10^9, 10^9]$. The `target` will be in the range $[-10^9, 10^9]$.
- Expected output format: Return the indices of the two numbers such that they add up to the `target`. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.
- Key requirements and edge cases to consider: The array is sorted, and we should take advantage of this property to optimize our solution. We should also consider the case where the two numbers are at the beginning and end of the array.
- Example test cases with explanations:
  - Input: `numbers = [2,7,11,15], target = 9`
  - Output: `[1,2]` (because `numbers[1] + numbers[2] == 9`)
  - Input: `numbers = [2,3,4], target = 6`
  - Output: `[1,3]` (because `numbers[1] + numbers[3] == 6`)

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can use a nested loop to check every pair of numbers in the array.
- Step-by-step breakdown of the solution:
  1. Iterate through each number in the array.
  2. For each number, iterate through the rest of the numbers in the array.
  3. Check if the sum of the current pair of numbers equals the target.
  4. If it does, return the indices of the two numbers.
- Why this approach comes to mind first: It's a straightforward and intuitive solution, but it's not efficient for large inputs.

```cpp
vector<int> twoSum(vector<int>& numbers, int target) {
    for (int i = 0; i < numbers.size(); i++) {
        for (int j = i + 1; j < numbers.size(); j++) {
            if (numbers[i] + numbers[j] == target) {
                return {i + 1, j + 1};
            }
        }
    }
    return {}; // Return an empty vector if no solution is found
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the input array. This is because we have a nested loop structure.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the indices of the two numbers.
> - **Why these complexities occur:** The time complexity is high because we're checking every pair of numbers in the array, and the space complexity is low because we're not using any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Since the array is sorted, we can use a two-pointer technique to find the pair of numbers that add up to the target.
- Detailed breakdown of the approach:
  1. Initialize two pointers, one at the beginning of the array and one at the end.
  2. Calculate the sum of the numbers at the current positions of the two pointers.
  3. If the sum is equal to the target, return the indices of the two numbers.
  4. If the sum is less than the target, move the left pointer to the right to increase the sum.
  5. If the sum is greater than the target, move the right pointer to the left to decrease the sum.
- Proof of optimality: This approach has a time complexity of $O(n)$, which is the best we can achieve because we have to at least read the input array once.
- Why further optimization is impossible: We can't do better than $O(n)$ because we have to check every number in the array at least once.

```cpp
vector<int> twoSum(vector<int>& numbers, int target) {
    int left = 0;
    int right = numbers.size() - 1;
    while (left < right) {
        int sum = numbers[left] + numbers[right];
        if (sum == target) {
            return {left + 1, right + 1};
        } else if (sum < target) {
            left++;
        } else {
            right--;
        }
    }
    return {}; // Return an empty vector if no solution is found
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input array. This is because we're only iterating through the array once.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the indices of the two numbers.
> - **Optimality proof:** The time complexity is optimal because we're only checking each number in the array once, and the space complexity is optimal because we're not using any data structures that scale with the input size.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Two-pointer technique, taking advantage of sorted arrays.
- Problem-solving patterns identified: Using the properties of the input to optimize the solution.
- Optimization techniques learned: Reducing the number of iterations, using constant space.
- Similar problems to practice: Other problems that involve finding pairs or triples of numbers in sorted arrays.

**Mistakes to Avoid:**
- Common implementation errors: Off-by-one errors when indexing the array, not checking for edge cases.
- Edge cases to watch for: Empty input arrays, arrays with only one element.
- Performance pitfalls: Using nested loops, not taking advantage of the sorted property of the array.
- Testing considerations: Test the function with different input sizes, test edge cases, test with different types of input (e.g., positive and negative numbers).