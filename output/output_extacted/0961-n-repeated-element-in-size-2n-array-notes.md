## N-Repeated Element in Size 2N Array

**Problem Link:** https://leetcode.com/problems/n-repeated-element-in-size-2n-array/description

**Problem Statement:**
- Input: An array `nums` of size `2n`, where `n` is an integer.
- Constraints: `1 <= n <= 10^5`, `nums.length == 2 * n`, and `1 <= nums[i] <= 10^5`.
- Expected Output: The element that appears `n` times in the array.
- Key Requirements: Identify the element that repeats `n` times in an array of size `2n`.
- Edge Cases: The input array may contain duplicate elements, and there is exactly one element that repeats `n` times.

Example Test Cases:
- Input: `nums = [1,2,3,3]`, Output: `3`
- Input: `nums = [2,1,2,5,3,2]`, Output: `2`
- Input: `nums = [5,1,5,2,5,3,5,4]`, Output: `5`

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking each element in the array to see if it appears `n` times.
- This can be achieved by iterating through the array for each element and counting its occurrences.
- This approach comes to mind first because it directly addresses the problem statement.

```cpp
vector<int> countElements(vector<int>& nums) {
    vector<int> count(100001, 0); // Assuming max value is 10^5
    for (int num : nums) {
        count[num]++;
    }
    int n = nums.size() / 2;
    for (int i = 1; i <= 100000; i++) {
        if (count[i] == n) {
            return {i};
        }
    }
    return {}; // Return empty vector if no such element is found
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2n + m)$, where $n$ is the size of the input array divided by 2, and $m$ is the maximum possible value in the array (10^5 in this case). This is because we perform a constant amount of work for each element in the array and then iterate up to the maximum possible value.
> - **Space Complexity:** $O(m)$, where $m$ is the maximum possible value in the array. This is because we use an array of size $m$ to store the counts of each element.
> - **Why these complexities occur:** These complexities occur because we are using a simple iterative approach to count the occurrences of each element and then searching for the element that appears `n` times.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is recognizing that we can use a `unordered_map` to store the counts of each element as we iterate through the array.
- This approach allows us to find the element that appears `n` times in a single pass through the array.
- We can prove that this is optimal because we must at least read the input array once, which takes $O(n)$ time.

```cpp
int repeatedNTimes(vector<int>& nums) {
    unordered_map<int, int> count;
    int n = nums.size() / 2;
    for (int num : nums) {
        count[num]++;
        if (count[num] == n) {
            return num;
        }
    }
    return -1; // Return -1 if no such element is found
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of the input array. This is because we perform a constant amount of work for each element in the array.
> - **Space Complexity:** $O(n)$, where $n$ is the size of the input array. This is because in the worst case, we might have to store every element in the `unordered_map`.
> - **Optimality proof:** This is optimal because we must at least read the input array once, which takes $O(n)$ time. Using a `unordered_map` to store the counts allows us to find the element that appears `n` times in a single pass.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a `unordered_map` to store counts of elements, recognizing the need for a single pass through the array.
- Problem-solving patterns identified: Looking for opportunities to use a `unordered_map` to store counts or frequencies of elements.
- Optimization techniques learned: Reducing the number of passes through the array, using a `unordered_map` to store counts.
- Similar problems to practice: Other problems that involve finding elements based on their frequencies or counts.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to initialize the `unordered_map`, not checking for the case where the element is not found.
- Edge cases to watch for: The input array may contain duplicate elements, and there is exactly one element that repeats `n` times.
- Performance pitfalls: Using a slow data structure, such as a `vector` or `list`, to store the counts of elements.
- Testing considerations: Testing the function with different input arrays, including edge cases and large inputs.