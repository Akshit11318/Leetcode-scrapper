## Count the Number of Inversions
**Problem Link:** https://leetcode.com/problems/count-the-number-of-inversions/description

**Problem Statement:**
- Input format: An array of integers
- Constraints: The array can contain duplicate elements and can be empty
- Expected output format: The number of inversions in the array
- Key requirements and edge cases to consider: Handling duplicate elements, empty arrays, and arrays with a single element
- Example test cases with explanations: 
  - Input: `[2, 4, 1, 3, 5]`
  - Output: `3`
  - Explanation: The inversions are `(2, 1)`, `(4, 1)`, and `(4, 3)`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Compare each pair of elements in the array to check for inversions
- Step-by-step breakdown of the solution:
  1. Initialize a variable to store the count of inversions
  2. Iterate over the array using two nested loops
  3. In the inner loop, check if the current element is greater than the element at the next index
  4. If it is, increment the inversion count
- Why this approach comes to mind first: It is the most straightforward way to solve the problem, but it is not efficient for large arrays

```cpp
int countInversions(vector<int>& nums) {
    int count = 0;
    for (int i = 0; i < nums.size(); i++) {
        for (int j = i + 1; j < nums.size(); j++) {
            if (nums[i] > nums[j]) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the size of the array, because we are using two nested loops to compare each pair of elements
> - **Space Complexity:** $O(1)$, because we are only using a constant amount of space to store the inversion count
> - **Why these complexities occur:** The nested loops cause the time complexity to be quadratic, while the space complexity is constant because we are not using any additional data structures that scale with the input size

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a modified merge sort algorithm to count the inversions
- Detailed breakdown of the approach:
  1. Split the array into two halves recursively until we have subarrays of size 1
  2. Merge the subarrays while counting the inversions
- Proof of optimality: This approach has a time complexity of $O(n \log n)$, which is optimal for comparison-based sorting algorithms
- Why further optimization is impossible: The lower bound for comparison-based sorting algorithms is $O(n \log n)$, so we cannot do better than this

```cpp
int countInversions(vector<int>& nums) {
    return mergeSort(nums, 0, nums.size() - 1);
}

int mergeSort(vector<int>& nums, int start, int end) {
    if (start >= end) {
        return 0;
    }
    int mid = start + (end - start) / 2;
    int leftInversions = mergeSort(nums, start, mid);
    int rightInversions = mergeSort(nums, mid + 1, end);
    int mergedInversions = merge(nums, start, mid, end);
    return leftInversions + rightInversions + mergedInversions;
}

int merge(vector<int>& nums, int start, int mid, int end) {
    int count = 0;
    vector<int> left(nums.begin() + start, nums.begin() + mid + 1);
    vector<int> right(nums.begin() + mid + 1, nums.begin() + end + 1);
    int i = 0, j = 0, k = start;
    while (i < left.size() && j < right.size()) {
        if (left[i] <= right[j]) {
            nums[k++] = left[i++];
        } else {
            nums[k++] = right[j++];
            count += left.size() - i;
        }
    }
    while (i < left.size()) {
        nums[k++] = left[i++];
    }
    while (j < right.size()) {
        nums[k++] = right[j++];
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the size of the array, because we are using a divide-and-conquer approach with a logarithmic number of levels
> - **Space Complexity:** $O(n)$, because we are using additional space to store the temporary arrays during the merge process
> - **Optimality proof:** The time complexity of $O(n \log n)$ is optimal for comparison-based sorting algorithms, and we are counting the inversions as a byproduct of the sorting process

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Modified merge sort, divide-and-conquer approach
- Problem-solving patterns identified: Using a sorting algorithm to solve a related problem
- Optimization techniques learned: Using a modified sorting algorithm to count inversions
- Similar problems to practice: Other problems that involve counting or sorting, such as counting the number of pairs with a certain property

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases correctly, such as empty arrays or arrays with a single element
- Edge cases to watch for: Duplicate elements, empty arrays, arrays with a single element
- Performance pitfalls: Using a naive approach with a time complexity of $O(n^2)$
- Testing considerations: Test the function with a variety of inputs, including edge cases and large arrays.