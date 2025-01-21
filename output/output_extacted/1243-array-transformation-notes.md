## Array Transformation

**Problem Link:** https://leetcode.com/problems/array-transformation/description

**Problem Statement:**
- Input: An array of integers `arr` and an integer `k`.
- Constraints: `1 <= arr.length <= 10^5`, `1 <= k <= 10^9`, `1 <= arr[i] <= 10^5`.
- Expected Output: The transformed array after `k` operations.
- Key Requirements: 
  - In each operation, if the current element is greater than the next element, replace the current element with its next element. 
  - If the current element is less than or equal to the next element, replace the current element with the element before it.
- Edge Cases: 
  - If the array has less than two elements, no operations can be performed, so return the original array.
  - If `k` is 0, return the original array.
- Example Test Cases: 
  - Input: `arr = [6, 2, 3, 4]`, `k = 2`.
    - After the first operation: `arr = [2, 2, 3, 4]`.
    - After the second operation: `arr = [2, 2, 2, 4]`.
    - Output: `[2, 2, 2, 4]`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to simulate each operation `k` times.
- In each operation, we iterate through the array from the first element to the second last element.
- For each element, we compare it with the next element and replace it based on the comparison.
- This approach is straightforward but inefficient for large `k` because it repeats the same comparison and replacement process `k` times.

```cpp
class Solution {
public:
    vector<int> transformArray(vector<int>& arr, int k) {
        if (k == 0 || arr.size() < 2) return arr;
        
        for (int i = 0; i < k; i++) {
            vector<int> temp(arr.size());
            temp[0] = arr[0];
            for (int j = 1; j < arr.size() - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    temp[j] = arr[j - 1];
                } else {
                    temp[j] = arr[j + 1];
                }
            }
            temp[arr.size() - 1] = arr[arr.size() - 1];
            arr = temp;
        }
        return arr;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k)$, where $n$ is the size of the array `arr` and $k$ is the number of operations.
> - **Space Complexity:** $O(n)$, where $n$ is the size of the array `arr`, for storing the temporary array `temp`.
> - **Why these complexities occur:** The time complexity is $O(n \cdot k)$ because in each of the $k$ operations, we iterate through the array of size $n$. The space complexity is $O(n)$ because we need a temporary array of the same size as the input array to store the transformed elements.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to observe the pattern of transformation and notice that after a certain number of operations, the array will stabilize and no further changes will occur.
- We can take advantage of this property to reduce the number of operations.
- The optimal solution involves simulating the operations until the array stabilizes, which is when no element is changed in an operation.

```cpp
class Solution {
public:
    vector<int> transformArray(vector<int>& arr, int k) {
        if (k == 0 || arr.size() < 2) return arr;
        
        bool changed;
        do {
            changed = false;
            vector<int> temp(arr.size());
            temp[0] = arr[0];
            for (int j = 1; j < arr.size() - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    temp[j] = arr[j - 1];
                    if (temp[j] != arr[j]) changed = true;
                } else {
                    temp[j] = arr[j + 1];
                    if (temp[j] != arr[j]) changed = true;
                }
            }
            temp[arr.size() - 1] = arr[arr.size() - 1];
            arr = temp;
        } while (changed);
        
        return arr;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the size of the array `arr` and $m$ is the number of operations until the array stabilizes.
> - **Space Complexity:** $O(n)$, where $n$ is the size of the array `arr`, for storing the temporary array `temp`.
> - **Optimality proof:** This solution is optimal because it takes advantage of the fact that after a certain number of operations, the array will stabilize. This reduces the number of operations from $k$ to the minimum number of operations required to stabilize the array.

---

### Final Notes

**Learning Points:**
- The importance of observing patterns in the problem and leveraging them for optimization.
- How to take advantage of stabilization in iterative processes to reduce computational complexity.
- The trade-off between time and space complexity in different approaches.

**Mistakes to Avoid:**
- Not considering the stabilization of the array, leading to unnecessary operations.
- Not using a temporary array to store the transformed elements, which could lead to incorrect results due to concurrent modification of the original array.
- Not checking for the base cases (e.g., `k == 0` or `arr.size() < 2`) to handle edge cases correctly.