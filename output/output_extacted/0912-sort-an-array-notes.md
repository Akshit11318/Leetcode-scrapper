## Sort an Array
**Problem Link:** https://leetcode.com/problems/sort-an-array/description

**Problem Statement:**
- Input format: The input is an array of integers `nums`.
- Constraints: $1 \leq nums.length \leq 100$ and $0 \leq nums[i] \leq 100$.
- Expected output format: The output should be the sorted array in ascending order.
- Key requirements and edge cases to consider: The input array can contain duplicate elements, and the array should be sorted in-place.
- Example test cases with explanations: 
    - Example 1: Input: `nums = [5,2,3,1]`, Output: `[1,2,3,5]`.
    - Example 2: Input: `nums = [1,1,1,1]`, Output: `[1,1,1,1]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The most straightforward way to sort an array is to use a brute force approach, where we compare each pair of elements and swap them if they are in the wrong order.
- Step-by-step breakdown of the solution:
    1. Start from the first element and compare it with every other element in the array.
    2. If the current element is greater than any other element, swap them.
    3. Repeat this process for each element in the array.
- Why this approach comes to mind first: This approach is simple and easy to understand, but it is not efficient for large arrays.

```cpp
class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        int n = nums.size();
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                if (nums[i] > nums[j]) {
                    swap(nums[i], nums[j]);
                }
            }
        }
        return nums;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of elements in the array. This is because we are using two nested loops to compare each pair of elements.
> - **Space Complexity:** $O(1)$, as we are not using any extra space that scales with the input size.
> - **Why these complexities occur:** The time complexity is quadratic because we are comparing each element with every other element, resulting in $n(n-1)/2$ comparisons. The space complexity is constant because we are not using any extra space that scales with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a divide-and-conquer approach to sort the array, which is more efficient than the brute force approach.
- Detailed breakdown of the approach:
    1. Divide the array into two halves.
    2. Recursively sort each half.
    3. Merge the two sorted halves into a single sorted array.
- Proof of optimality: This approach is optimal because it has a time complexity of $O(n \log n)$, which is the best possible time complexity for comparison-based sorting algorithms.
- Why further optimization is impossible: The time complexity of $O(n \log n)$ is optimal because it is the best possible time complexity for comparison-based sorting algorithms.

```cpp
class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        mergeSort(nums, 0, nums.size() - 1);
        return nums;
    }
    
    void mergeSort(vector<int>& nums, int left, int right) {
        if (left < right) {
            int mid = left + (right - left) / 2;
            mergeSort(nums, left, mid);
            mergeSort(nums, mid + 1, right);
            merge(nums, left, mid, right);
        }
    }
    
    void merge(vector<int>& nums, int left, int mid, int right) {
        vector<int> temp(right - left + 1);
        int i = left, j = mid + 1, k = 0;
        while (i <= mid && j <= right) {
            if (nums[i] <= nums[j]) {
                temp[k++] = nums[i++];
            } else {
                temp[k++] = nums[j++];
            }
        }
        while (i <= mid) {
            temp[k++] = nums[i++];
        }
        while (j <= right) {
            temp[k++] = nums[j++];
        }
        for (int i = left; i <= right; i++) {
            nums[i] = temp[i - left];
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of elements in the array. This is because we are using a divide-and-conquer approach to sort the array.
> - **Space Complexity:** $O(n)$, as we are using extra space to store the temporary array.
> - **Optimality proof:** The time complexity of $O(n \log n)$ is optimal because it is the best possible time complexity for comparison-based sorting algorithms.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Divide-and-conquer approach, merge sort.
- Problem-solving patterns identified: Using a divide-and-conquer approach to solve a problem.
- Optimization techniques learned: Using a more efficient algorithm to solve a problem.
- Similar problems to practice: Other sorting algorithms, such as quicksort and heapsort.

**Mistakes to Avoid:**
- Common implementation errors: Not handling the base case correctly, not merging the sorted halves correctly.
- Edge cases to watch for: Empty array, array with one element, array with duplicate elements.
- Performance pitfalls: Using a brute force approach to solve a problem, not optimizing the algorithm.
- Testing considerations: Testing the algorithm with different input sizes, testing the algorithm with edge cases.