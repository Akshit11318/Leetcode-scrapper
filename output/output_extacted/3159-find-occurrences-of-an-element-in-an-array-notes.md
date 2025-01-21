## Find Occurrences of an Element in an Array

**Problem Link:** https://leetcode.com/problems/find-occurrences-of-an-element-in-an-array/description

**Problem Statement:**
- Input format: An array of integers and a target element.
- Constraints: The array can be empty, and the target element can be any integer.
- Expected output format: The indices of all occurrences of the target element in the array.
- Key requirements and edge cases to consider:
  - Handling an empty array.
  - Handling an array with a single element.
  - Handling an array with duplicate elements.
  - Handling an array with no occurrences of the target element.

**Example Test Cases:**
- Input: `arr = [1, 2, 3, 4, 5]`, `target = 3`. Output: `[2]`.
- Input: `arr = [1, 2, 2, 3, 3, 3]`, `target = 2`. Output: `[1, 2]`.
- Input: `arr = []`, `target = 5`. Output: `[]`.

### Brute Force Approach

**Explanation:**
- The initial thought process is to iterate through the array and check each element to see if it matches the target.
- This approach is straightforward but not efficient for large arrays.

```cpp
vector<int> findOccurrences(vector<int>& arr, int target) {
    vector<int> occurrences;
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] == target) {
            occurrences.push_back(i);
        }
    }
    return occurrences;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of the array, because we are scanning the array once.
> - **Space Complexity:** $O(n)$, because in the worst-case scenario (all elements are the target), the size of the `occurrences` vector will be equal to the size of the array.
> - **Why these complexities occur:** The time complexity is linear because we are checking each element in the array once. The space complexity is also linear because we are storing the indices of all occurrences of the target element.

### Optimal Approach (Required)

**Explanation:**
- The key insight is that the brute force approach is already optimal for this problem because we must check each element in the array at least once to find all occurrences of the target.
- The optimal approach is the same as the brute force approach, but we can make minor optimizations such as using `const` references and checking for an empty array at the beginning.

```cpp
vector<int> findOccurrences(const vector<int>& arr, int target) {
    if (arr.empty()) {
        return {};
    }
    vector<int> occurrences;
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] == target) {
            occurrences.push_back(i);
        }
    }
    return occurrences;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of the array, because we are scanning the array once.
> - **Space Complexity:** $O(n)$, because in the worst-case scenario (all elements are the target), the size of the `occurrences` vector will be equal to the size of the array.
> - **Optimality proof:** This is the optimal solution because we must check each element in the array at least once to find all occurrences of the target. Any algorithm that claims to do better than linear time would have to skip checking some elements, which would lead to incorrect results.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: linear search, array iteration.
- Problem-solving patterns identified: checking each element in a collection to find matches.
- Optimization techniques learned: using `const` references, checking for edge cases.
- Similar problems to practice: finding the maximum or minimum element in an array, finding the first occurrence of an element in an array.

**Mistakes to Avoid:**
- Common implementation errors: not checking for an empty array, not using `const` references when possible.
- Edge cases to watch for: an empty array, an array with a single element, an array with duplicate elements.
- Performance pitfalls: using algorithms with higher time complexity than necessary, such as sorting the array before searching.
- Testing considerations: test with arrays of different sizes, test with arrays containing duplicate elements, test with an empty array.