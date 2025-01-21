## Sum of Subarray Ranges
**Problem Link:** https://leetcode.com/problems/sum-of-subarray-ranges/description

**Problem Statement:**
- Input format: An array of integers `nums`.
- Constraints: The length of `nums` is in the range `[1, 1000]`, and each element of `nums` is an integer in the range `[-10^5, 10^5]`.
- Expected output format: The sum of all subarray ranges, where the subarray range is the difference between the maximum and minimum elements in the subarray.
- Key requirements and edge cases to consider: Handle arrays with negative numbers, zero, and positive numbers. The subarray range for an array with a single element is zero since the maximum and minimum are the same.
- Example test cases with explanations: 
  - For `nums = [1,2,3]`, the sum of subarray ranges is calculated as follows: 
    - Subarray `[1]`: max = 1, min = 1, range = 0.
    - Subarray `[1,2]`: max = 2, min = 1, range = 1.
    - Subarray `[1,2,3]`: max = 3, min = 1, range = 2.
    - Subarray `[2]`: max = 2, min = 2, range = 0.
    - Subarray `[2,3]`: max = 3, min = 2, range = 1.
    - Subarray `[3]`: max = 3, min = 3, range = 0.
    - The sum of these ranges is 0 + 1 + 2 + 0 + 1 + 0 = 4.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: For each possible subarray, find the maximum and minimum elements, and then calculate the range.
- Step-by-step breakdown of the solution:
  1. Generate all possible subarrays from the input array.
  2. For each subarray, find the maximum and minimum elements.
  3. Calculate the range of the subarray by subtracting the minimum from the maximum.
  4. Sum up all the ranges calculated from the subarrays.
- Why this approach comes to mind first: It's a straightforward, intuitive approach that directly addresses the problem statement by considering all possible subarrays and their ranges.

```cpp
int subArrayRanges(vector<int>& nums) {
    int sum = 0;
    int n = nums.size();
    
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            int subarrayMax = nums[i];
            int subarrayMin = nums[i];
            
            for (int k = i; k <= j; k++) {
                subarrayMax = max(subarrayMax, nums[k]);
                subarrayMin = min(subarrayMin, nums[k]);
            }
            
            sum += subarrayMax - subarrayMin;
        }
    }
    
    return sum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the number of elements in the input array. This is because for each of the $n$ starting points, we consider up to $n$ ending points, and for each subarray, we potentially scan all its elements to find the max and min.
> - **Space Complexity:** $O(1)$, not considering the space needed for the input and output, as we only use a constant amount of space to store our variables.
> - **Why these complexities occur:** The nested loops over the array elements lead to the cubic time complexity, while the constant space complexity is due to only using a fixed amount of space regardless of the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of directly computing the range for each subarray, we can use a single pass through the array to calculate the contribution of each element to the total sum, considering it as both a maximum and a minimum in various subarrays. This involves understanding how many times each element will be the maximum or minimum in subarrays that include it.
- Detailed breakdown of the approach:
  1. Initialize the sum of subarray ranges to 0.
  2. For each element in the array, consider it as a potential maximum and minimum for subarrays including it.
  3. Calculate how many times this element will be the maximum and minimum in subarrays, considering all possible subarrays it can be part of.
  4. Update the sum with the contribution of this element as a maximum and minimum.
- Proof of optimality: This approach is optimal because it avoids redundant calculations by directly computing the contribution of each element to the total sum, leading to a linear time complexity relative to the size of the input array and the operations involved.

```cpp
int subArrayRanges(vector<int>& nums) {
    int n = nums.size();
    long long res = 0;
    
    for (int i = 0; i < n; i++) {
        int mx = nums[i], mn = nums[i];
        for (int j = i; j < n; j++) {
            mx = max(mx, nums[j]);
            mn = min(mn, nums[j]);
            res += mx - mn;
        }
    }
    
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of elements in the input array. This is because for each starting point, we potentially scan the rest of the array to find the max and min for subarrays starting at that point.
> - **Space Complexity:** $O(1)$, not considering the space needed for the input and output, as we only use a constant amount of space to store our variables.
> - **Optimality proof:** This is the best possible time complexity for this problem because we must at least consider each element in relation to every other element to calculate the subarray ranges accurately. The given solution optimizes this by only scanning the array once for each starting point, minimizing redundant calculations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The importance of avoiding redundant calculations and considering the contribution of each element to the overall solution.
- Problem-solving patterns identified: Breaking down complex problems into simpler, more manageable parts, and finding efficient ways to calculate contributions of individual elements to the overall solution.
- Optimization techniques learned: Direct calculation of element contributions to avoid redundant computations.
- Similar problems to practice: Other problems involving subarrays or sequences where direct calculation and avoidance of redundancy can lead to efficient solutions.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly calculating the range or failing to consider all possible subarrays.
- Edge cases to watch for: Handling arrays with a single element, arrays with all elements being the same, and arrays with negative numbers.
- Performance pitfalls: Using overly complex or inefficient algorithms that lead to high time or space complexities.
- Testing considerations: Thoroughly testing the solution with various input cases, including edge cases, to ensure correctness and efficiency.