## Guess the Majority in a Hidden Array
**Problem Link:** https://leetcode.com/problems/guess-the-majority-in-a-hidden-array/description

**Problem Statement:**
- Input format: You are given a function `predicate` that takes an integer array `nums` and returns a boolean indicating whether a given number is in the majority.
- Constraints: The array is non-empty, and the majority element is guaranteed to exist.
- Expected output format: The index of the majority element.
- Key requirements and edge cases to consider: The majority element is the element that appears more than n/2 times where n is the size of the array.
- Example test cases with explanations:
  - `predicate([1, 2, 3, 4, 1, 1, 1], [1])` returns `true`, indicating that `1` is in the majority.
  - `predicate([1, 1, 1, 2, 2], [2])` returns `false`, indicating that `2` is not in the majority.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Use the given `predicate` function to check each element in the array to see if it's the majority element.
- Step-by-step breakdown of the solution:
  1. Iterate through each element in the array.
  2. For each element, use the `predicate` function to check if it's the majority element.
  3. If an element is found to be the majority, return its index.
- Why this approach comes to mind first: It's the most straightforward way to solve the problem, as it checks every possible element.

```cpp
int findMajorityIndex(const std::vector<int>& nums, std::function<bool(const std::vector<int>&, const std::vector<int>&)> predicate) {
    for (int i = 0; i < nums.size(); ++i) {
        std::vector<int> num = {nums[i]};
        if (predicate(nums, num)) {
            return i;
        }
    }
    return -1; // This should never happen according to the problem statement
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the size of the input array, because we are potentially checking every element in the array.
> - **Space Complexity:** $O(1)$, because we are only using a constant amount of space to store the current index and the current number.
> - **Why these complexities occur:** The time complexity is linear because we are checking each element in the array once, and the space complexity is constant because we are not using any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use the `predicate` function to perform a binary search on the array to find the majority element.
- Detailed breakdown of the approach:
  1. Initialize the search range to the entire array.
  2. While the search range is not empty:
     - Calculate the midpoint of the search range.
     - Use the `predicate` function to check if the midpoint element is the majority element.
     - If it is, return its index.
     - Otherwise, use the `predicate` function to check if the majority element is in the left or right half of the search range.
     - Update the search range accordingly.
- Proof of optimality: This approach is optimal because it reduces the search range by half at each step, resulting in a logarithmic time complexity.

```cpp
int findMajorityIndex(const std::vector<int>& nums, std::function<bool(const std::vector<int>&, const std::vector<int>&)> predicate) {
    int left = 0;
    int right = nums.size() - 1;
    while (left < right) {
        int mid = left + (right - left) / 2;
        std::vector<int> num = {nums[mid]};
        if (predicate(nums, num)) {
            return mid;
        }
        std::vector<int> leftHalf;
        for (int i = left; i <= mid; ++i) {
            leftHalf.push_back(nums[i]);
        }
        std::vector<int> rightHalf;
        for (int i = mid + 1; i <= right; ++i) {
            rightHalf.push_back(nums[i]);
        }
        if (predicate(leftHalf, num)) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }
    return left;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, because we are performing a binary search on the array, and at each step, we are potentially checking half of the remaining elements.
> - **Space Complexity:** $O(n)$, because we are creating temporary arrays to represent the left and right halves of the search range.
> - **Optimality proof:** This approach is optimal because it reduces the search range by half at each step, resulting in a logarithmic time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Binary search, use of a predicate function to guide the search.
- Problem-solving patterns identified: Using a predicate function to search for an element in an array.
- Optimization techniques learned: Reducing the search range by half at each step to achieve a logarithmic time complexity.
- Similar problems to practice: Searching for an element in a sorted array, finding the first occurrence of an element in a sorted array.

**Mistakes to Avoid:**
- Common implementation errors: Failing to update the search range correctly, not handling the base case correctly.
- Edge cases to watch for: The case where the majority element is at the beginning or end of the array.
- Performance pitfalls: Using a linear search instead of a binary search, not using the predicate function to guide the search.
- Testing considerations: Testing the function with different input arrays, including edge cases and corner cases.