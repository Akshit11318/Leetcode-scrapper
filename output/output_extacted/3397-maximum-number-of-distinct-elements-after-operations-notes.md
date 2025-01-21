## Maximum Number of Distinct Elements After Operations
**Problem Link:** https://leetcode.com/problems/maximum-number-of-distinct-elements-after-operations/description

**Problem Statement:**
- Given an array `nums` and an integer `k`, return the maximum number of distinct elements in an array after `k` operations. An operation is defined as removing an element from the array and adding a new element to the array that is not already present.
- Input format and constraints: The input array `nums` will have a length between 1 and $10^5$. The integer `k` will be between 0 and $10^5$.
- Expected output format: The maximum number of distinct elements after `k` operations.
- Key requirements and edge cases to consider:
  - If `k` is greater than or equal to the number of elements in the array, the maximum number of distinct elements will be the minimum of `k` and the array length.
  - If `k` is 0, the maximum number of distinct elements will be the number of distinct elements in the original array.
- Example test cases with explanations:
  - For the input `nums = [5, 5, 4]` and `k = 1`, the maximum number of distinct elements is 2, because we can remove one of the duplicate 5's and add a new distinct element.
  - For the input `nums = [4, 3, 1, 1, 3, 3, 2]` and `k = 3`, the maximum number of distinct elements is 7, because we can remove all the duplicate elements and add new distinct elements.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves iterating over all possible combinations of elements in the array and checking the number of distinct elements after each operation.
- Step-by-step breakdown of the solution:
  1. Initialize a set to store the distinct elements in the array.
  2. Iterate over the array and add each element to the set.
  3. Calculate the number of duplicate elements by subtracting the size of the set from the array length.
  4. If `k` is greater than or equal to the number of duplicate elements, return the minimum of `k` and the array length.
  5. Otherwise, return the size of the set.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it has high time complexity due to the iteration over all possible combinations.

```cpp
int maxDistinctElements(vector<int>& nums, int k) {
    unordered_set<int> distinctElements;
    for (int num : nums) {
        distinctElements.insert(num);
    }
    int duplicateElements = nums.size() - distinctElements.size();
    if (k >= duplicateElements) {
        return min(k, (int)nums.size());
    } else {
        return distinctElements.size();
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the array, because we iterate over the array once.
> - **Space Complexity:** $O(n)$, because we use a set to store the distinct elements.
> - **Why these complexities occur:** The time complexity is linear because we only iterate over the array once, and the space complexity is linear because we store all distinct elements in the set.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a hash map to count the frequency of each element in the array, and then calculate the number of duplicate elements.
- Detailed breakdown of the approach:
  1. Initialize a hash map to count the frequency of each element.
  2. Iterate over the array and update the frequency count for each element.
  3. Calculate the number of duplicate elements by summing up the frequencies minus one for each element.
  4. If `k` is greater than or equal to the number of duplicate elements, return the minimum of `k` and the array length.
  5. Otherwise, return the number of distinct elements.
- Proof of optimality: This approach is optimal because it only requires a single pass over the array and uses a hash map to count the frequency of each element, resulting in a time complexity of $O(n)$.

```cpp
int maxDistinctElements(vector<int>& nums, int k) {
    unordered_map<int, int> frequencyCount;
    for (int num : nums) {
        frequencyCount[num]++;
    }
    int duplicateElements = 0;
    for (auto& pair : frequencyCount) {
        duplicateElements += pair.second - 1;
    }
    if (k >= duplicateElements) {
        return min(k, (int)nums.size());
    } else {
        return frequencyCount.size();
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the array, because we iterate over the array once and update the frequency count for each element.
> - **Space Complexity:** $O(n)$, because we use a hash map to store the frequency count for each element.
> - **Optimality proof:** This approach is optimal because it only requires a single pass over the array and uses a hash map to count the frequency of each element, resulting in a time complexity of $O(n)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Hash maps, frequency counting, and duplicate element removal.
- Problem-solving patterns identified: Using hash maps to count frequency and calculating duplicate elements.
- Optimization techniques learned: Reducing time complexity by using a single pass over the array and a hash map.
- Similar problems to practice: Problems involving frequency counting, duplicate element removal, and hash map usage.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the hash map or frequency count correctly, or not handling edge cases properly.
- Edge cases to watch for: Handling cases where `k` is greater than or equal to the array length, or where the array is empty.
- Performance pitfalls: Using nested loops or recursive approaches that result in high time complexity.
- Testing considerations: Testing the function with different input arrays and values of `k` to ensure correct output.