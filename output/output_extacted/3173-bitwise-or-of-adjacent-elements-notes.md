## Bitwise OR of Adjacent Elements

**Problem Link:** https://leetcode.com/problems/bitwise-or-of-adjacent-elements/description

**Problem Statement:**
- Input: A list of integers `arr` representing the elements of an array.
- Constraints: `1 <= arr.length <= 100`, `0 <= arr[i] <= 1000`.
- Expected Output: An integer representing the bitwise OR of all adjacent elements in the array.
- Key Requirements: Calculate the bitwise OR of each element with its adjacent elements.
- Edge Cases: Handle arrays with a single element or no elements.

### Brute Force Approach

**Explanation:**
- The initial thought process involves iterating over each element in the array and calculating the bitwise OR with its adjacent elements.
- This approach comes to mind first because it directly addresses the problem statement without requiring any additional insights.
- Step-by-step breakdown:
  1. Initialize an empty list to store the results of bitwise OR operations.
  2. Iterate over each element in the input array.
  3. For each element, calculate the bitwise OR with its adjacent elements (if they exist).
  4. Append the result to the list.
  5. Return the list of results.

```cpp
vector<int> getAdjacentElements(vector<int>& arr) {
    vector<int> result;
    for (int i = 0; i < arr.size(); i++) {
        int bitwise_or = arr[i];
        if (i > 0) {
            bitwise_or |= arr[i - 1];
        }
        if (i < arr.size() - 1) {
            bitwise_or |= arr[i + 1];
        }
        result.push_back(bitwise_or);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array, since we iterate over each element once.
> - **Space Complexity:** $O(n)$, as we store the results in a list of the same size as the input array.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each element in the array. The space complexity is also linear because we store a result for each element.

### Optimal Approach (Required)

**Explanation:**
- The optimal approach is essentially the same as the brute force approach, as the problem requires calculating the bitwise OR of each element with its adjacent elements.
- Detailed breakdown:
  1. Initialize an empty list to store the results.
  2. Iterate over each element in the input array.
  3. For each element, calculate the bitwise OR with its adjacent elements (if they exist).
  4. Append the result to the list.
  5. Return the list of results.
- Proof of optimality: This approach is optimal because it only requires a single pass over the input array and performs a constant amount of work for each element.

```cpp
vector<int> getAdjacentElementsOptimal(vector<int>& arr) {
    vector<int> result(arr.size());
    for (int i = 0; i < arr.size(); i++) {
        int bitwise_or = arr[i];
        if (i > 0) {
            bitwise_or |= arr[i - 1];
        }
        if (i < arr.size() - 1) {
            bitwise_or |= arr[i + 1];
        }
        result[i] = bitwise_or;
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array.
> - **Space Complexity:** $O(n)$, as we store the results in a list of the same size as the input array.
> - **Optimality proof:** This approach is optimal because it has the same time and space complexity as the brute force approach, but is slightly more efficient in practice due to the use of a pre-allocated list.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: iteration, bitwise operations, and list manipulation.
- Problem-solving patterns identified: breaking down the problem into smaller sub-problems (calculating the bitwise OR for each element) and combining the results.
- Optimization techniques learned: using a pre-allocated list to store results instead of appending to a list.
- Similar problems to practice: other problems involving bitwise operations, iteration, and list manipulation.

**Mistakes to Avoid:**
- Common implementation errors: forgetting to handle edge cases (e.g., arrays with a single element or no elements).
- Edge cases to watch for: arrays with a single element or no elements.
- Performance pitfalls: using unnecessary loops or recursive function calls.
- Testing considerations: testing the function with different input arrays, including edge cases.