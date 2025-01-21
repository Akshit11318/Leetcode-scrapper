## Intervals Between Identical Elements
**Problem Link:** https://leetcode.com/problems/intervals-between-identical-elements/description

**Problem Statement:**
- Input format: A 0-indexed array of `n` integers `arr`.
- Constraints: `1 <= n <= 10^5`, `1 <= arr[i] <= 10^5`.
- Expected output format: An array of integers where the `i-th` integer is the length of the smallest interval that contains at least one occurrence of the integer `i`.
- Key requirements and edge cases to consider: The array may contain duplicate integers, and the output should be in the same order as the integers appear in the array.
- Example test cases with explanations:
  - Example 1: `arr = [2,1,3,1,2,1,3,1]`, Output: `[2,1,3,1]`.
  - Example 2: `arr = [10,10,10]`, Output: `[1,1,1]`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Iterate over the array for each unique integer to find the first and last occurrence, then calculate the interval length.
- Step-by-step breakdown of the solution:
  1. Create a set of unique integers from the array.
  2. For each unique integer, iterate over the array to find the first and last occurrence.
  3. Calculate the interval length as the difference between the last and first occurrence plus one.
  4. Store the interval lengths in an array in the order of the integers' first appearance.
- Why this approach comes to mind first: It directly addresses the problem statement by iterating over the array to find the required intervals.

```cpp
vector<int> getInterval(vector<int>& arr) {
    unordered_set<int> unique;
    for (int num : arr) unique.insert(num);
    
    vector<int> result;
    for (int num : unique) {
        int first = -1, last = -1;
        for (int i = 0; i < arr.size(); i++) {
            if (arr[i] == num) {
                if (first == -1) first = i;
                last = i;
            }
        }
        result.push_back(last - first + 1);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the size of the array and $m$ is the number of unique integers. This is because for each unique integer, we potentially iterate over the entire array.
> - **Space Complexity:** $O(m)$, where $m$ is the number of unique integers. This is because we store the unique integers in a set and the result in a vector.
> - **Why these complexities occur:** The brute force approach involves nested iterations over the array, leading to a higher time complexity. The space complexity is linear due to the storage of unique integers and the result.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can use a single pass over the array to store the first and last occurrence of each integer in a hash map.
- Detailed breakdown of the approach:
  1. Create a hash map to store the first and last occurrence of each integer.
  2. Iterate over the array, updating the first and last occurrence of each integer in the hash map.
  3. Calculate the interval length for each integer as the difference between the last and first occurrence plus one.
  4. Store the interval lengths in an array in the order of the integers' first appearance.
- Proof of optimality: This approach reduces the time complexity to linear, as we only need a single pass over the array.

```cpp
vector<int> getInterval(vector<int>& arr) {
    unordered_map<int, pair<int, int>> map;
    for (int i = 0; i < arr.size(); i++) {
        if (map.find(arr[i]) == map.end()) {
            map[arr[i]] = {i, i};
        } else {
            map[arr[i]].second = i;
        }
    }
    
    vector<int> result;
    for (int num : arr) {
        if (map.find(num) != map.end()) {
            result.push_back(map[num].second - map[num].first + 1);
            map.erase(num);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of the array. This is because we make a single pass over the array.
> - **Space Complexity:** $O(m)$, where $m$ is the number of unique integers. This is because we store the first and last occurrence of each integer in a hash map.
> - **Optimality proof:** This approach is optimal because it achieves the lowest possible time complexity by only iterating over the array once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Hash maps, single pass iteration, and interval calculation.
- Problem-solving patterns identified: Using hash maps to store and retrieve data efficiently.
- Optimization techniques learned: Reducing time complexity by minimizing iterations.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly updating the first and last occurrence of integers in the hash map.
- Edge cases to watch for: Handling duplicate integers and ensuring the output is in the correct order.
- Performance pitfalls: Using nested iterations or inefficient data structures.
- Testing considerations: Verifying the correctness of the output for different input scenarios.