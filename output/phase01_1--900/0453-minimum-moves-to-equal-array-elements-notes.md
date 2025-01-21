## Minimum Moves to Equal Array Elements
**Problem Link:** https://leetcode.com/problems/minimum-moves-to-equal-array-elements/description

**Problem Statement:**
- Input format and constraints: Given a non-empty integer array `nums`, find the minimum number of moves required to make all array elements equal. Each move involves incrementing `n-1` elements by `1`.
- Expected output format: The minimum number of moves.
- Key requirements and edge cases to consider: The array may contain duplicate elements, and the minimum number of moves should be calculated based on the median of the array.
- Example test cases with explanations:
  - Example 1: Input: `nums = [1,2,3]`, Output: `3`, Explanation: We can make all elements equal by incrementing `1` to `3` (two moves), `2` to `3` (one move), and `3` remains the same (zero moves). So, the total number of moves is `2 + 1 = 3`.
  - Example 2: Input: `nums = [1,10,2,9]`, Output: `16`, Explanation: The median of the array is `4.5`, which is between `2` and `3`. To make all elements equal to the median, we would need to increment `1` to `4.5` (three moves) and `2` to `4.5` (two moves), and decrement `10` to `4.5` (five moves) and `9` to `4.5` (four moves). However, we can't increment or decrement to a non-integer value, so we round the median to the nearest integer, which is `3` or `4`. If we choose `3`, we would need to increment `1` to `3` (two moves) and `2` to `3` (one move), and decrement `10` to `3` (seven moves) and `9` to `3` (six moves). The total number of moves would be `2 + 1 + 7 + 6 = 16`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Calculate the median of the array and then calculate the total number of moves required to make all elements equal to the median.
- Step-by-step breakdown of the solution:
  1. Sort the array in ascending order.
  2. Calculate the median of the array. If the length of the array is odd, the median is the middle element. If the length is even, the median is the average of the two middle elements.
  3. Calculate the total number of moves required to make all elements equal to the median.
- Why this approach comes to mind first: It's a straightforward approach that involves calculating the median and then calculating the total number of moves.

```cpp
int minMoves2(vector<int>& nums) {
    // Sort the array in ascending order
    sort(nums.begin(), nums.end());
    
    // Calculate the median of the array
    int median;
    if (nums.size() % 2 == 0) {
        // If the length of the array is even, the median is the average of the two middle elements
        median = (nums[nums.size() / 2 - 1] + nums[nums.size() / 2]) / 2;
    } else {
        // If the length of the array is odd, the median is the middle element
        median = nums[nums.size() / 2];
    }
    
    // Calculate the total number of moves required to make all elements equal to the median
    int totalMoves = 0;
    for (int num : nums) {
        totalMoves += abs(num - median);
    }
    
    return totalMoves;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of elements in the array. This is because we're sorting the array using the `sort` function, which has a time complexity of $O(n \log n)$.
> - **Space Complexity:** $O(1)$, as we're not using any additional space that scales with the input size.
> - **Why these complexities occur:** The time complexity occurs because we're sorting the array, and the space complexity occurs because we're not using any additional space that scales with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of sorting the array, we can find the median using a single pass through the array.
- Detailed breakdown of the approach:
  1. Find the median of the array using a single pass.
  2. Calculate the total number of moves required to make all elements equal to the median.
- Proof of optimality: This approach is optimal because it has a time complexity of $O(n)$, which is the best possible time complexity for this problem.
- Why further optimization is impossible: We can't optimize the solution further because we need to examine each element in the array at least once to find the median and calculate the total number of moves.

```cpp
int minMoves2(vector<int>& nums) {
    // Find the median of the array using a single pass
    int median = findMedian(nums);
    
    // Calculate the total number of moves required to make all elements equal to the median
    int totalMoves = 0;
    for (int num : nums) {
        totalMoves += abs(num - median);
    }
    
    return totalMoves;
}

int findMedian(vector<int>& nums) {
    int n = nums.size();
    if (n % 2 == 0) {
        // If the length of the array is even, the median is the average of the two middle elements
        int mid1 = quickSelect(nums, n / 2 - 1);
        int mid2 = quickSelect(nums, n / 2);
        return (mid1 + mid2) / 2;
    } else {
        // If the length of the array is odd, the median is the middle element
        return quickSelect(nums, n / 2);
    }
}

int quickSelect(vector<int>& nums, int k) {
    // Implement the quickSelect algorithm to find the k-th smallest element in the array
    if (nums.size() == 1) {
        return nums[0];
    }
    
    int pivot = nums[nums.size() / 2];
    vector<int> left, middle, right;
    for (int num : nums) {
        if (num < pivot) {
            left.push_back(num);
        } else if (num == pivot) {
            middle.push_back(num);
        } else {
            right.push_back(num);
        }
    }
    
    if (k < left.size()) {
        return quickSelect(left, k);
    } else if (k < left.size() + middle.size()) {
        return middle[0];
    } else {
        return quickSelect(right, k - left.size() - middle.size());
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array. This is because we're finding the median using a single pass through the array.
> - **Space Complexity:** $O(n)$, as we're using additional space to store the left, middle, and right arrays in the quickSelect algorithm.
> - **Optimality proof:** This approach is optimal because it has a time complexity of $O(n)$, which is the best possible time complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The quickSelect algorithm, which is used to find the k-th smallest element in an array.
- Problem-solving patterns identified: The problem can be solved by finding the median of the array and then calculating the total number of moves required to make all elements equal to the median.
- Optimization techniques learned: The solution can be optimized by using a single pass through the array to find the median, instead of sorting the array.

**Mistakes to Avoid:**
- Common implementation errors: Not handling the case where the length of the array is even or odd.
- Edge cases to watch for: The array may contain duplicate elements, and the minimum number of moves should be calculated based on the median of the array.
- Performance pitfalls: The solution may have a high time complexity if the array is not sorted or if the median is not found efficiently.
- Testing considerations: The solution should be tested with different input arrays to ensure that it works correctly and efficiently.