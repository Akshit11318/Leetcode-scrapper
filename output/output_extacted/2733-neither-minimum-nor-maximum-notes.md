## Neither Minimum Nor Maximum
**Problem Link:** https://leetcode.com/problems/neither-minimum-nor-maximum/description

**Problem Statement:**
- Input format and constraints: Given a list of integers `arr`, return the count of elements that are neither the minimum nor the maximum in the list.
- Expected output format: An integer representing the count of elements that are neither the minimum nor the maximum.
- Key requirements and edge cases to consider:
  - The input list may contain duplicate elements.
  - The list may contain negative numbers.
  - The list may contain a single element or no elements at all.
- Example test cases with explanations:
  - Example 1: Input: `arr = [1,2,3]`, Output: `1`. Explanation: Only the middle element `2` is neither the minimum nor the maximum.
  - Example 2: Input: `arr = [1,1,1]`, Output: `0`. Explanation: All elements are the same, so none are neither the minimum nor the maximum.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Compare each element in the list to the minimum and maximum values in the list to determine if it's neither.
- Step-by-step breakdown of the solution:
  1. Find the minimum and maximum values in the list.
  2. Iterate through the list, comparing each element to the minimum and maximum.
  3. Count the elements that are neither the minimum nor the maximum.
- Why this approach comes to mind first: It's straightforward and directly addresses the problem statement.

```cpp
int countNeitherMinNorMax(vector<int>& arr) {
    if (arr.size() < 3) return 0; // If less than 3 elements, no element can be neither min nor max.
    
    int minVal = *min_element(arr.begin(), arr.end());
    int maxVal = *max_element(arr.begin(), arr.end());
    
    int count = 0;
    for (int num : arr) {
        if (num != minVal && num != maxVal) {
            count++;
        }
    }
    
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the list, because we are iterating through the list twice: once to find the min and max, and once to count the elements that are neither min nor max.
> - **Space Complexity:** $O(1)$, because we are using a constant amount of space to store the minimum, maximum, and count variables.
> - **Why these complexities occur:** The time complexity is linear due to the iteration through the list, and the space complexity is constant because we are not using any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The same as the brute force approach, as the problem inherently requires checking each element against the minimum and maximum.
- Detailed breakdown of the approach: The optimal solution is essentially the same as the brute force approach because it's already quite efficient.
- Proof of optimality: This approach is optimal because it checks each element exactly once, which is necessary to count the elements that are neither the minimum nor the maximum.
- Why further optimization is impossible: Further optimization is not possible because the problem requires at least one pass through the data to identify the minimum and maximum, and then another pass to count the elements that are neither.

```cpp
int countNeitherMinNorMax(vector<int>& arr) {
    if (arr.size() < 3) return 0;
    
    int minVal = *min_element(arr.begin(), arr.end());
    int maxVal = *max_element(arr.begin(), arr.end());
    
    int count = count_if(arr.begin(), arr.end(), [minVal, maxVal](int x){ return x != minVal && x != maxVal; });
    
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, because we are still iterating through the list twice: once to find the min and max, and once to count the elements that are neither min nor max.
> - **Space Complexity:** $O(1)$, because we are still using a constant amount of space to store the minimum, maximum, and count variables.
> - **Optimality proof:** This solution is optimal because it performs the minimum number of operations required to solve the problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Linear scanning, use of standard library functions for finding minimum and maximum.
- Problem-solving patterns identified: Checking each element against certain conditions (in this case, minimum and maximum).
- Optimization techniques learned: Recognizing when further optimization is not possible due to the inherent requirements of the problem.
- Similar problems to practice: Other problems involving linear scanning and conditional checks.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling edge cases (like empty lists or lists with a single element).
- Edge cases to watch for: Lists with duplicate minimum or maximum values.
- Performance pitfalls: Unnecessary iterations or using inefficient algorithms for finding minimum and maximum.
- Testing considerations: Thoroughly testing with various input sizes, including edge cases like empty lists or lists with a single element.