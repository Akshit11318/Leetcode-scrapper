## Valid Mountain Array
**Problem Link:** https://leetcode.com/problems/valid-mountain-array/description

**Problem Statement:**
- Input: An array of integers `arr`.
- Constraints: The length of `arr` is in the range `[2, 10^4]`. Each element `arr[i]` is an integer in the range `[0, 10^4]`.
- Expected Output: A boolean indicating whether the input array is a valid mountain array.
- Key Requirements: A valid mountain array should have the following properties:
  - It should have at least one element.
  - It should strictly increase until it reaches a peak, then strictly decrease.
- Edge Cases:
  - An array with only one element is not a valid mountain array.
  - An array that only increases or only decreases is not a valid mountain array.
- Example Test Cases:
  - `arr = [2,1]`: Not a valid mountain array because it only decreases.
  - `arr = [3,5,5]`: Not a valid mountain array because it does not strictly increase.
  - `arr = [0,3,2,1]`: A valid mountain array because it strictly increases until the peak (3) and then strictly decreases.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to iterate through the array and check for the conditions of a mountain array.
- We start by checking if the array has less than 3 elements. If so, it cannot be a mountain array.
- Then, we iterate through the array to find the peak. The array must strictly increase until the peak and then strictly decrease.
- If at any point the array does not meet these conditions, we return false.

```cpp
bool validMountainArray(vector<int>& arr) {
    if (arr.size() < 3) return false;
    int n = arr.size();
    int i = 0;
    // Check for strictly increasing
    while (i < n - 1 && arr[i] < arr[i + 1]) i++;
    // If we are at the start or the end, it's not a mountain array
    if (i == 0 || i == n - 1) return false;
    // Check for strictly decreasing
    while (i < n - 1 && arr[i] > arr[i + 1]) i++;
    // If we've reached the end, it's a mountain array
    return i == n - 1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array, because we make a single pass through the array.
> - **Space Complexity:** $O(1)$, because we use a constant amount of space to store our variables.
> - **Why these complexities occur:** The time complexity is linear because we potentially check every element in the array once. The space complexity is constant because we do not use any data structures that scale with the input size.

---

### Optimal Approach (Required)

The provided brute force approach is already optimal for this problem because it only requires a single pass through the array to determine if it is a valid mountain array. There are no significant improvements to be made without changing the fundamental approach of checking each element's relation to its neighbors.

```cpp
bool validMountainArray(vector<int>& arr) {
    if (arr.size() < 3) return false;
    int n = arr.size();
    int i = 0;
    // Check for strictly increasing
    while (i < n - 1 && arr[i] < arr[i + 1]) i++;
    // If we are at the start or the end, it's not a mountain array
    if (i == 0 || i == n - 1) return false;
    // Check for strictly decreasing
    while (i < n - 1 && arr[i] > arr[i + 1]) i++;
    // If we've reached the end, it's a mountain array
    return i == n - 1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array, because we make a single pass through the array.
> - **Space Complexity:** $O(1)$, because we use a constant amount of space to store our variables.
> - **Optimality proof:** This approach is optimal because it only requires checking each element once, which is the minimum number of checks required to determine if an array is a valid mountain array.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated include iterating through an array and checking conditions.
- Problem-solving patterns identified include checking for edge cases first and then applying the main logic.
- Optimization techniques learned include minimizing the number of passes through the data.
- Similar problems to practice include other array-based problems that require checking conditions or patterns.

**Mistakes to Avoid:**
- Common implementation errors include not checking for edge cases or not properly handling the end conditions of the array.
- Edge cases to watch for include arrays with less than 3 elements or arrays that are strictly increasing or decreasing without a peak.
- Performance pitfalls include making unnecessary passes through the data or using data structures that have higher than necessary space complexity.
- Testing considerations include testing with arrays of varying lengths and compositions to ensure the function handles all possible cases correctly.