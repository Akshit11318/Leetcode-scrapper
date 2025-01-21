## Element Appearing More Than 25% in Sorted Array

**Problem Link:** https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/description

**Problem Statement:**
- Input: A sorted array of integers `arr`.
- Output: The integer that appears more than `25%` of the length of the array. If no such integer exists, return `-1`.
- Key Requirements:
  - The input array is sorted.
  - The integer must appear more than `25%` of the length of the array, not `25%` or more.
- Edge Cases:
  - An empty array.
  - An array with no element appearing more than `25%` of its length.
- Example Test Cases:
  - Input: `[1,2,2,6,6,6,6,7,10]`, Output: `6`
  - Input: `[1,1]`, Output: `1`

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking each unique element in the array to see if it appears more than `25%` of the array's length.
- This approach involves iterating through the array, counting the occurrences of each unique element, and checking if any of these counts exceed `25%` of the array's length.
- This approach comes to mind first because it directly addresses the problem statement without requiring any optimization.

```cpp
int findSpecialInteger(vector<int>& arr) {
    int n = arr.size();
    unordered_map<int, int> count;
    for (int num : arr) {
        count[num]++;
    }
    for (auto& pair : count) {
        if (pair.second > n / 4) {
            return pair.first;
        }
    }
    return -1; // No such integer exists
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array. This is because we are iterating through the array once to count the occurrences of each element.
> - **Space Complexity:** $O(n)$, because in the worst case, every element in the array could be unique, requiring a separate entry in the `unordered_map`.
> - **Why these complexities occur:** The time complexity is linear because we are scanning the array once. The space complexity is also linear because we are storing counts for each unique element.

---

### Optimal Approach (Required)

**Explanation:**
- Given that the array is sorted, we can take advantage of this property to find the element appearing more than `25%` of the array's length more efficiently.
- The key insight is that if an element appears more than `25%` of the array's length, it must appear in at least one of the four segments of equal size within the array.
- We can use a modified binary search approach to find such an element, taking advantage of the fact that the array is sorted.
- This approach involves selecting a random index and checking if the element at this index appears more than `25%` of the time. If it does, we have found our answer. If not, we know which segment of the array to focus on next based on the count of the element at the selected index.

```cpp
int findSpecialInteger(vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n; i++) {
        if (arr[i] == arr[min(i + n / 4, n - 1)]) {
            return arr[i];
        }
    }
    return -1; // No such integer exists
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, because in the worst case, we might need to check every element in the array once.
> - **Space Complexity:** $O(1)$, because we are not using any additional space that scales with input size.
> - **Optimality proof:** This is optimal because we must at least look at each element once to determine if it meets the condition, and our approach does this in a single pass through the array, leveraging the sorted property to minimize unnecessary comparisons.

---

### Final Notes

**Learning Points:**
- The importance of leveraging the properties of the input data (in this case, the array being sorted).
- How to apply a modified binary search approach to solve problems involving sorted arrays and frequency thresholds.
- The trade-off between time and space complexity in different approaches.

**Mistakes to Avoid:**
- Not considering the properties of the input data.
- Overcomplicating the solution with unnecessary data structures or algorithms.
- Not testing edge cases thoroughly.

---