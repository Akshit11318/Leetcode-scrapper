## Kth Missing Positive Number

**Problem Link:** https://leetcode.com/problems/kth-missing-positive-number/description

**Problem Statement:**
- Input format: `arr` - a sorted array of unique positive integers, and `k` - the number of missing positive integers to find.
- Constraints: $1 \leq arr.length \leq 1000$, $1 \leq arr[i] \leq 1000$, and $1 \leq k \leq 1000$.
- Expected output format: The `kth` missing positive number.
- Key requirements and edge cases to consider: 
  - Handle arrays with no missing positive integers.
  - Handle arrays with all positive integers present (e.g., `[1, 2, 3]`).
  - Handle cases where `k` is larger than the number of missing positive integers.
- Example test cases with explanations:
  - `arr = [2, 3, 4], k = 1`, expected output: `1`.
  - `arr = [1, 2, 3, 4], k = 2`, expected output: `5`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Create a list of all positive integers up to the maximum value in the array, then remove the integers present in the array.
- Step-by-step breakdown of the solution:
  1. Find the maximum value in the array.
  2. Generate a list of all positive integers up to the maximum value.
  3. Remove the integers present in the array from the list.
  4. Return the `kth` integer in the resulting list.

```cpp
class Solution {
public:
    int findKthPositive(vector<int>& arr, int k) {
        unordered_set<int> s(arr.begin(), arr.end());
        int count = 0;
        int num = 1;
        while (true) {
            if (s.find(num) == s.end()) {
                count++;
                if (count == k) return num;
            }
            num++;
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the length of the array and $m$ is the maximum value in the array. This is because we iterate over the array to create a set and then iterate up to the maximum value in the array.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the array. This is because we store the array elements in a set.
> - **Why these complexities occur:** The time complexity occurs because we perform a linear scan of the array and then a linear scan up to the maximum value in the array. The space complexity occurs because we store all elements of the array in a set.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a two-pointer technique to iterate over the array and the list of positive integers simultaneously.
- Detailed breakdown of the approach:
  1. Initialize two pointers, one at the beginning of the array and one at the first positive integer.
  2. Compare the values at the two pointers. If the value in the array is greater than the current positive integer, increment the count of missing integers and move the positive integer pointer.
  3. If the count of missing integers reaches `k`, return the current positive integer.
  4. If the value in the array is equal to the current positive integer, move the array pointer.
- Proof of optimality: This approach has a time complexity of $O(n + k)$, which is optimal because we must at least read the input array and find the `kth` missing positive integer.

```cpp
class Solution {
public:
    int findKthPositive(vector<int>& arr, int k) {
        int i = 0;
        int num = 1;
        while (true) {
            if (i < arr.size() && arr[i] == num) {
                i++;
            } else {
                k--;
                if (k == 0) return num;
            }
            num++;
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + k)$, where $n$ is the length of the array and $k$ is the number of missing positive integers to find. This is because we iterate over the array and up to the `kth` missing positive integer.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the pointers and the count of missing integers.
> - **Optimality proof:** This approach is optimal because we must at least read the input array and find the `kth` missing positive integer, and we do so in a single pass.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Two-pointer technique, iteration over arrays and lists.
- Problem-solving patterns identified: Using sets to keep track of unique elements, using pointers to iterate over arrays and lists.
- Optimization techniques learned: Reducing the number of iterations, using constant space.
- Similar problems to practice: Finding the `kth` largest element in an array, finding the `kth` smallest element in a sorted array.

**Mistakes to Avoid:**
- Common implementation errors: Off-by-one errors, incorrect handling of edge cases.
- Edge cases to watch for: Empty arrays, arrays with no missing positive integers, cases where `k` is larger than the number of missing positive integers.
- Performance pitfalls: Using unnecessary iterations or space, failing to optimize the solution.
- Testing considerations: Testing with different input sizes, testing with different values of `k`, testing with edge cases.