## Check If a Number Is Majority Element in a Sorted Array

**Problem Link:** https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/description

**Problem Statement:**
- Input format and constraints: Given a sorted array `nums` and a number `target`, return `true` if `target` is a majority element in `nums`, and `false` otherwise. A majority element is an element that appears more than `n/2` times where `n` is the length of the array.
- Expected output format: A boolean value indicating whether the target is a majority element.
- Key requirements and edge cases to consider: The input array is sorted, and we need to find if the target appears more than `n/2` times.
- Example test cases with explanations:
  - Input: `nums = [2,4,5,5,5,5,5,6,6]`, `target = 5`
    Output: `true`
    Explanation: 5 appears 5 times which is more than `n/2` times.
  - Input: `nums = [10,9,9]`, `target = 9`
    Output: `true`
    Explanation: 9 appears 2 times which is more than `n/2` times.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The simplest way to check if a target is a majority element in an array is to count its occurrences and compare it with `n/2`.
- Step-by-step breakdown of the solution:
  1. Initialize a counter for the target element.
  2. Iterate through the array and increment the counter whenever the target element is found.
  3. After iterating through the entire array, check if the counter is greater than `n/2`.
- Why this approach comes to mind first: It directly addresses the problem statement by counting the occurrences of the target element.

```cpp
bool isMajorityElement(vector<int>& nums, int target) {
    int count = 0;
    for (int num : nums) {
        if (num == target) {
            count++;
        }
    }
    return count > nums.size() / 2;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array. This is because we are iterating through the array once.
> - **Space Complexity:** $O(1)$, as we are using a constant amount of space to store the count of the target element.
> - **Why these complexities occur:** The time complexity is linear because we are scanning the array once, and the space complexity is constant because we only use a fixed amount of space regardless of the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Since the array is sorted, we can use binary search to find the first and last occurrence of the target element. This allows us to calculate the count of the target element more efficiently.
- Detailed breakdown of the approach:
  1. Use binary search to find the first occurrence of the target element.
  2. Use binary search to find the last occurrence of the target element.
  3. Calculate the count of the target element by subtracting the index of the first occurrence from the index of the last occurrence and adding 1.
  4. Check if the count is greater than `n/2`.
- Proof of optimality: This approach is optimal because binary search has a time complexity of $O(\log n)$, which is more efficient than the linear scan in the brute force approach.

```cpp
bool isMajorityElement(vector<int>& nums, int target) {
    int first = binarySearchFirst(nums, target);
    if (first == -1) return false; // Target not found
    int last = binarySearchLast(nums, target);
    return (last - first + 1) > nums.size() / 2;
}

int binarySearchFirst(vector<int>& nums, int target) {
    int left = 0, right = nums.size() - 1;
    int first = -1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] == target) {
            first = mid;
            right = mid - 1; // Continue searching in the left half
        } else if (nums[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return first;
}

int binarySearchLast(vector<int>& nums, int target) {
    int left = 0, right = nums.size() - 1;
    int last = -1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] == target) {
            last = mid;
            left = mid + 1; // Continue searching in the right half
        } else if (nums[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return last;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log n)$, where $n$ is the number of elements in the array. This is because we are using binary search to find the first and last occurrence of the target element.
> - **Space Complexity:** $O(1)$, as we are using a constant amount of space to store the indices and the count of the target element.
> - **Optimality proof:** This approach is optimal because binary search has a time complexity of $O(\log n)$, which is the best possible time complexity for searching in a sorted array.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Binary search, counting occurrences of an element.
- Problem-solving patterns identified: Using binary search to find the first and last occurrence of an element in a sorted array.
- Optimization techniques learned: Using binary search to reduce the time complexity from $O(n)$ to $O(\log n)$.
- Similar problems to practice: Finding the first and last occurrence of an element in a sorted array, counting occurrences of an element in an array.

**Mistakes to Avoid:**
- Common implementation errors: Not handling the case where the target element is not found in the array.
- Edge cases to watch for: The target element appears exactly `n/2` times, the target element is the first or last element in the array.
- Performance pitfalls: Using a linear scan instead of binary search to find the first and last occurrence of the target element.
- Testing considerations: Test the function with different input arrays and target elements, including edge cases.