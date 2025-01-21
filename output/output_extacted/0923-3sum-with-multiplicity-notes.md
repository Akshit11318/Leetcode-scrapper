## 3Sum with Multiplicity
**Problem Link:** https://leetcode.com/problems/3sum-with-multiplicity/description

**Problem Statement:**
- Input format and constraints: The problem involves an array of integers `arr` and a target sum `target`. The array contains both positive and negative integers, and the target sum is an integer. The constraints are that the array length is between 1 and 10^5, and each element in the array is between -10^9 and 10^9. The target sum is also between -10^9 and 10^9.
- Expected output format: The task is to find the number of triplets in the array that sum up to the target sum, considering multiplicity. For example, if the array is [1, 1, 2, 2, 3, 3, 4, 4, 5, 5] and the target sum is 6, the triplets could be (1, 2, 3) with different permutations, and also considering (1, 1, 4), (2, 2, 2), etc.
- Key requirements and edge cases to consider: The key requirement is to count the number of unique triplets that sum up to the target sum. Edge cases include arrays with duplicate elements, arrays with negative numbers, and arrays with large numbers that could potentially cause overflow.
- Example test cases with explanations:
  - Example 1: `arr = [1,1,2,2,3,3,4,4,5,5], target = 8`. The expected output is the count of unique triplets that sum up to 8.
  - Example 2: `arr = [1,1,2,2], target = 4`. The expected output is the count of unique triplets that sum up to 4.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: The brute force approach involves checking every possible combination of three numbers in the array to see if their sum equals the target sum.
- Step-by-step breakdown of the solution:
  1. Initialize a counter variable to store the count of triplets that sum up to the target sum.
  2. Iterate over the array using three nested loops to generate all possible triplets.
  3. For each triplet, check if the sum of the three numbers equals the target sum.
  4. If the sum equals the target sum, increment the counter variable.
- Why this approach comes to mind first: This approach is straightforward and easy to implement. However, it is inefficient for large arrays because it has a high time complexity.

```cpp
int threeSumMulti(vector<int>& arr, int target) {
    int count = 0;
    int n = arr.size();
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            for (int k = j + 1; k < n; k++) {
                if (arr[i] + arr[j] + arr[k] == target) {
                    count++;
                }
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the size of the input array. This is because we are using three nested loops to generate all possible triplets.
> - **Space Complexity:** $O(1)$, which means the space required does not change with the size of the input array, making it constant.
> - **Why these complexities occur:** The high time complexity occurs because we are checking every possible combination of three numbers in the array. The constant space complexity occurs because we are only using a fixed amount of space to store the counter variable and the loop indices.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can sort the array first and then use two pointers, one starting from the beginning and one from the end, to find the triplets that sum up to the target sum.
- Detailed breakdown of the approach:
  1. Sort the array in ascending order.
  2. Iterate over the array using one loop.
  3. For each element, use two pointers, one starting from the next element and one from the end of the array, to find a pair of elements that sum up to the remaining target sum.
  4. Move the pointers based on the sum of the three elements.
- Proof of optimality: This approach is optimal because it reduces the time complexity from $O(n^3)$ to $O(n^2)$.

```cpp
int threeSumMulti(vector<int>& arr, int target) {
    sort(arr.begin(), arr.end());
    int count = 0;
    int n = arr.size();
    for (int i = 0; i < n - 2; i++) {
        int left = i + 1;
        int right = n - 1;
        while (left < right) {
            int sum = arr[i] + arr[left] + arr[right];
            if (sum == target) {
                int leftCount = 1;
                int rightCount = 1;
                while (left + 1 < right && arr[left] == arr[left + 1]) {
                    left++;
                    leftCount++;
                }
                while (right - 1 > left && arr[right] == arr[right - 1]) {
                    right--;
                    rightCount++;
                }
                count += leftCount * rightCount;
                left++;
                right--;
            } else if (sum < target) {
                left++;
            } else {
                right--;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the size of the input array. This is because we are using one loop to iterate over the array and two pointers to find the pair of elements that sum up to the remaining target sum.
> - **Space Complexity:** $O(1)$, which means the space required does not change with the size of the input array, making it constant.
> - **Optimality proof:** This approach is optimal because it reduces the time complexity from $O(n^3)$ to $O(n^2)$, making it more efficient for large arrays.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting, two pointers technique.
- Problem-solving patterns identified: Reducing time complexity by using efficient algorithms and data structures.
- Optimization techniques learned: Using two pointers to find a pair of elements that sum up to a target sum.
- Similar problems to practice: 3Sum, 4Sum, etc.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, not checking for duplicate elements.
- Edge cases to watch for: Arrays with duplicate elements, arrays with negative numbers, arrays with large numbers that could potentially cause overflow.
- Performance pitfalls: Using inefficient algorithms with high time complexity.
- Testing considerations: Test the solution with different input arrays and target sums to ensure it works correctly.