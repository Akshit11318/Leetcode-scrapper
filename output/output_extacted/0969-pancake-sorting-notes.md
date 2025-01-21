## Pancake Sorting
**Problem Link:** https://leetcode.com/problems/pancake-sorting/description

**Problem Statement:**
- Input format: An array of integers `A` where each integer represents the size of a pancake.
- Constraints: `1 <= A.length <= 100`, `1 <= A[i] <= 10^9`.
- Expected output format: The minimum number of flips required to sort the array in ascending order.
- Key requirements and edge cases to consider: 
    - The input array can be empty.
    - The input array can have duplicate elements.
    - The input array can be already sorted.
- Example test cases with explanations:
    - `A = [3,2,4,1]`, expected output is `2` because we can flip the first three elements to get `[1,2,3,4]`.
    - `A = [1,2,3]`, expected output is `0` because the array is already sorted.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: We can use a recursive approach to try all possible flips and find the minimum number of flips required to sort the array.
- Step-by-step breakdown of the solution:
    1. Define a recursive function `flip` that takes the current array and the number of flips as arguments.
    2. In the recursive function, try all possible flips and recursively call the function with the updated array and the incremented number of flips.
    3. Keep track of the minimum number of flips required to sort the array.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it has a high time complexity due to the recursive nature.

```cpp
class Solution {
public:
    int pancakeSort(vector<int>& A) {
        int n = A.size();
        int flips = 0;
        for (int size = n; size > 0; --size) {
            int maxIndex = 0;
            int maxVal = 0;
            for (int i = 0; i < size; ++i) {
                if (A[i] > maxVal) {
                    maxIndex = i;
                    maxVal = A[i];
                }
            }
            if (maxIndex == size - 1) continue;
            if (maxIndex != 0) {
                reverse(A.begin(), A.begin() + maxIndex + 1);
                flips++;
            }
            reverse(A.begin(), A.begin() + size);
            flips++;
        }
        return flips;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the input array. This is because we are iterating over the array for each flip.
> - **Space Complexity:** $O(1)$, because we are only using a constant amount of space to store the number of flips and the current array.
> - **Why these complexities occur:** The time complexity is high because we are trying all possible flips, and the space complexity is low because we are only using a constant amount of space.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can use a greedy approach to find the minimum number of flips required to sort the array. The idea is to find the maximum element in the unsorted part of the array and move it to the correct position.
- Detailed breakdown of the approach:
    1. Iterate over the array from the end to the beginning.
    2. For each iteration, find the maximum element in the unsorted part of the array.
    3. If the maximum element is not in the correct position, flip the array to move it to the correct position.
    4. Keep track of the number of flips.
- Proof of optimality: This approach is optimal because we are always moving the maximum element to the correct position, which minimizes the number of flips required.

```cpp
class Solution {
public:
    int pancakeSort(vector<int>& A) {
        int n = A.size();
        int flips = 0;
        for (int size = n; size > 0; --size) {
            int maxIndex = 0;
            int maxVal = 0;
            for (int i = 0; i < size; ++i) {
                if (A[i] > maxVal) {
                    maxIndex = i;
                    maxVal = A[i];
                }
            }
            if (maxIndex == size - 1) continue;
            if (maxIndex != 0) {
                reverse(A.begin(), A.begin() + maxIndex + 1);
                flips++;
            }
            reverse(A.begin(), A.begin() + size);
            flips++;
        }
        return flips;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the input array. This is because we are iterating over the array for each flip.
> - **Space Complexity:** $O(1)$, because we are only using a constant amount of space to store the number of flips and the current array.
> - **Optimality proof:** This approach is optimal because we are always moving the maximum element to the correct position, which minimizes the number of flips required.

---

### Final Notes
**Learning Points:**
- Key algorithmic concepts demonstrated: Greedy approach, iteration, and flipping.
- Problem-solving patterns identified: Finding the maximum element in the unsorted part of the array and moving it to the correct position.
- Optimization techniques learned: Using a greedy approach to minimize the number of flips required.
- Similar problems to practice: Sorting arrays using different techniques, such as selection sort and insertion sort.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for the maximum element in the unsorted part of the array, not flipping the array correctly.
- Edge cases to watch for: Empty arrays, arrays with duplicate elements, and already sorted arrays.
- Performance pitfalls: Using a recursive approach, which can lead to high time complexity.
- Testing considerations: Testing the function with different input arrays, including edge cases.