## Reverse Pairs
**Problem Link:** https://leetcode.com/problems/reverse-pairs/description

**Problem Statement:**
- Input format: An integer array `nums`.
- Constraints: `1 <= nums.length <= 5 * 10^4`, `0 <= nums[i] <= 10^9`.
- Expected output format: The number of reverse pairs in the array.
- Key requirements: A reverse pair is a pair `(i, j)` where `0 <= i < j < nums.length` and `nums[i] > 2 * nums[j]`.
- Example test cases:
  - Input: `nums = [1,3,2,3,1]`
    Output: `2`
    Explanation: The reverse pairs are `(1, 0)` and `(3, 0)` because `nums[1] > 2 * nums[0]` and `nums[3] > 2 * nums[0]`.
  - Input: `nums = [2,4,3,5,1]`
    Output: `3`
    Explanation: The reverse pairs are `(1, 0)`, `(2, 0)`, and `(3, 1)` because `nums[1] > 2 * nums[0]`, `nums[2] > 2 * nums[0]`, and `nums[3] > 2 * nums[1]`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Iterate over all pairs of elements in the array and check if each pair is a reverse pair.
- Step-by-step breakdown of the solution:
  1. Initialize a variable `count` to store the number of reverse pairs.
  2. Iterate over the array using two nested loops to generate all pairs of elements.
  3. For each pair `(i, j)`, check if `i < j` and `nums[i] > 2 * nums[j]`.
  4. If the condition is met, increment the `count` variable.
- Why this approach comes to mind first: It is the most straightforward way to solve the problem by checking all possible pairs.

```cpp
int reversePairs(vector<int>& nums) {
    int count = 0;
    for (int i = 0; i < nums.size(); i++) {
        for (int j = i + 1; j < nums.size(); j++) {
            if (nums[i] > 2 * nums[j]) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the array, because we use two nested loops to iterate over all pairs of elements.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input array, because we only use a constant amount of space to store the count variable.
> - **Why these complexities occur:** The time complexity is quadratic because we generate all pairs of elements, and the space complexity is constant because we only use a fixed amount of space to store the count.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: We can use a modified merge sort algorithm to count the reverse pairs in linear time.
- Detailed breakdown of the approach:
  1. Split the array into two halves recursively until each half has one element.
  2. When merging two halves, count the number of reverse pairs by iterating over the elements in the right half and checking how many elements in the left half are greater than twice the current element in the right half.
  3. Combine the counts from the recursive calls and the merge step to get the total count of reverse pairs.
- Proof of optimality: The modified merge sort algorithm has a time complexity of $O(n \log n)$, which is optimal for this problem because we need to at least read the input array.

```cpp
int reversePairs(vector<int>& nums) {
    return mergeSort(nums, 0, nums.size() - 1);
}

int mergeSort(vector<int>& nums, int start, int end) {
    if (start >= end) {
        return 0;
    }
    int mid = start + (end - start) / 2;
    int count = mergeSort(nums, start, mid) + mergeSort(nums, mid + 1, end);
    int j = mid + 1;
    for (int i = start; i <= mid; i++) {
        while (j <= end && nums[i] > 2 * nums[j]) {
            j++;
        }
        count += j - mid - 1;
    }
    merge(nums, start, mid, end);
    return count;
}

void merge(vector<int>& nums, int start, int mid, int end) {
    vector<int> temp(end - start + 1);
    int i = start, j = mid + 1, k = 0;
    while (i <= mid && j <= end) {
        if (nums[i] <= nums[j]) {
            temp[k++] = nums[i++];
        } else {
            temp[k++] = nums[j++];
        }
    }
    while (i <= mid) {
        temp[k++] = nums[i++];
    }
    while (j <= end) {
        temp[k++] = nums[j++];
    }
    for (int i = start; i <= end; i++) {
        nums[i] = temp[i - start];
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the length of the array, because we use a modified merge sort algorithm.
> - **Space Complexity:** $O(n)$, excluding the space needed for the input array, because we use a temporary array to store the merged elements.
> - **Optimality proof:** The time complexity is optimal because we need to at least read the input array, and the space complexity is reasonable because we only use a linear amount of extra space.

---

### Final Notes
**Learning Points:**
- Key algorithmic concepts: Modified merge sort, counting reverse pairs.
- Problem-solving patterns: Divide and conquer, recursive algorithms.
- Optimization techniques: Using a modified merge sort algorithm to count reverse pairs in linear time.
- Similar problems to practice: Other problems that involve counting pairs or triplets in an array.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases correctly, not initializing variables properly.
- Edge cases to watch for: Empty arrays, arrays with one element, arrays with duplicate elements.
- Performance pitfalls: Using a brute force approach with a time complexity of $O(n^2)$.
- Testing considerations: Testing the algorithm with large inputs to ensure it scales well.