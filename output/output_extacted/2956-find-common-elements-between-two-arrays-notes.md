## Find Common Elements Between Two Arrays

**Problem Link:** https://leetcode.com/problems/find-common-elements-between-two-arrays/description

**Problem Statement:**
- Input format and constraints: The problem takes two arrays of integers as input, `nums1` and `nums2`, and returns an array of integers containing the common elements between the two arrays. The input arrays are not guaranteed to be sorted, and the common elements should be returned in the order they appear in `nums1`.
- Expected output format: An array of integers containing the common elements between the two arrays.
- Key requirements and edge cases to consider: The problem requires finding the common elements between two arrays, which can be solved using various approaches. Key considerations include handling duplicate elements, maintaining the order of elements, and optimizing the solution for performance.
- Example test cases with explanations: 
    - Example 1: Input: `nums1 = [1, 2, 2, 1]`, `nums2 = [2, 2]`. Output: `[2, 2]`. Explanation: The common elements between the two arrays are `[2, 2]`, which appear in the order they appear in `nums1`.
    - Example 2: Input: `nums1 = [1, 2, 3, 4, 5]`, `nums2 = [4, 5, 6, 7, 8]`. Output: `[4, 5]`. Explanation: The common elements between the two arrays are `[4, 5]`, which appear in the order they appear in `nums1`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves iterating through each element in `nums1` and checking if it exists in `nums2`. This can be achieved using nested loops, where the outer loop iterates through `nums1` and the inner loop iterates through `nums2`.
- Step-by-step breakdown of the solution:
    1. Initialize an empty array `result` to store the common elements.
    2. Iterate through each element `num` in `nums1`.
    3. For each `num`, iterate through each element `num2` in `nums2`.
    4. If `num` is equal to `num2`, add `num` to the `result` array.
- Why this approach comes to mind first: The brute force approach is often the most straightforward solution, as it involves a simple iteration through the input arrays.

```cpp
vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
    vector<int> result;
    for (int num : nums1) {
        for (int num2 : nums2) {
            if (num == num2) {
                result.push_back(num);
                // Remove the matched element from nums2 to handle duplicates
                nums2.erase(find(nums2.begin(), nums2.end(), num2));
                break;
            }
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the length of `nums1` and $m$ is the length of `nums2`. This is because we have nested loops that iterate through each element in the input arrays.
> - **Space Complexity:** $O(n)$, as we need to store the common elements in the `result` array. In the worst case, all elements in `nums1` could be common with `nums2`.
> - **Why these complexities occur:** The time complexity is high due to the nested loops, while the space complexity is relatively low since we only need to store the common elements.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use an unordered map to store the frequency of each element in `nums2`. Then, we iterate through `nums1` and check if each element exists in the map. If it does, we add it to the `result` array and decrement its frequency in the map.
- Detailed breakdown of the approach:
    1. Initialize an unordered map `countMap` to store the frequency of each element in `nums2`.
    2. Iterate through each element `num` in `nums2` and update its frequency in `countMap`.
    3. Initialize an empty array `result` to store the common elements.
    4. Iterate through each element `num` in `nums1`.
    5. If `num` exists in `countMap` and its frequency is greater than 0, add `num` to the `result` array and decrement its frequency in `countMap`.
- Proof of optimality: This approach has a time complexity of $O(n + m)$, which is optimal since we need to iterate through each element in the input arrays at least once.

```cpp
vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
    unordered_map<int, int> countMap;
    for (int num : nums2) {
        countMap[num]++;
    }
    vector<int> result;
    for (int num : nums1) {
        if (countMap.find(num) != countMap.end() && countMap[num] > 0) {
            result.push_back(num);
            countMap[num]--;
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the length of `nums1` and $m` is the length of `nums2`. This is because we have two separate loops that iterate through each element in the input arrays.
> - **Space Complexity:** $O(m)$, as we need to store the frequency of each element in `nums2` in the `countMap`. In the worst case, all elements in `nums2` could be unique.
> - **Optimality proof:** This approach is optimal since we only need to iterate through each element in the input arrays once, resulting in a linear time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the use of nested loops, unordered maps, and frequency counting to solve a common elements problem.
- Problem-solving patterns identified: The problem requires identifying the common elements between two arrays, which can be solved using various approaches such as brute force, frequency counting, and map-based solutions.
- Optimization techniques learned: The problem demonstrates the importance of optimizing solutions for performance, such as using unordered maps to reduce the time complexity from $O(n \cdot m)$ to $O(n + m)$.
- Similar problems to practice: Similar problems include finding the intersection of two sets, finding the union of two sets, and finding the difference between two sets.

**Mistakes to Avoid:**
- Common implementation errors: Common errors include not handling duplicate elements, not maintaining the order of elements, and not optimizing the solution for performance.
- Edge cases to watch for: Edge cases include handling empty input arrays, handling arrays with duplicate elements, and handling arrays with a large number of elements.
- Performance pitfalls: Performance pitfalls include using nested loops, not using data structures like unordered maps, and not optimizing the solution for performance.
- Testing considerations: Testing considerations include testing the solution with various input arrays, testing the solution with edge cases, and testing the solution for performance.