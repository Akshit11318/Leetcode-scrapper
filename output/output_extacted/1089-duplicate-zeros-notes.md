## Duplicate Zeros

**Problem Link:** https://leetcode.com/problems/duplicate-zeros/description

**Problem Statement:**
- Input: An array of integers `arr` with length `n`.
- Constraints: `1 <= n <= 10^4`, `0 <= arr[i] <= 9`.
- Expected output: Modify the input array `arr` in-place to duplicate zeros.
- Key requirements: If the element is zero, duplicate it by shifting the elements to the right.
- Example test cases:
  - Input: `arr = [1,0,2,3,0,4,5,0]`, Output: `[1,0,0,2,3,0,0,4]`.
  - Input: `arr = [1,2,3]`, Output: `[1,2,3]`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to iterate through the array and whenever we encounter a zero, we shift all the elements to the right to make space for the duplicated zero.
- Step-by-step breakdown:
  1. Create a temporary array to store the result.
  2. Iterate through the input array.
  3. If the current element is zero, add it to the temporary array twice.
  4. If the current element is not zero, add it to the temporary array once.
  5. Copy the elements from the temporary array back to the input array, truncating any extra elements that don't fit.
- Why this approach comes to mind first: It's a straightforward approach that directly addresses the problem statement.

```cpp
void duplicateZeros(vector<int>& arr) {
    vector<int> temp;
    for (int num : arr) {
        if (num == 0) {
            temp.push_back(0);
            temp.push_back(0);
        } else {
            temp.push_back(num);
        }
        if (temp.size() == arr.size()) break;
    }
    for (int i = 0; i < arr.size(); i++) {
        arr[i] = temp[i];
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input array. This is because we make one pass through the array.
> - **Space Complexity:** $O(n)$, because in the worst case, we need a temporary array of the same size as the input array.
> - **Why these complexities occur:** The time complexity is linear because we only iterate through the array once. The space complexity is also linear because we use a temporary array to store the result.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of using a temporary array, we can iterate through the input array from left to right and use two pointers to track the position where we should write the next element.
- Detailed breakdown:
  1. Initialize two pointers, `i` and `j`, to the start of the array.
  2. Iterate through the array. When `arr[i]` is zero, we copy it to `arr[j]` and then increment `j` and copy the zero again to `arr[j]`.
  3. If `arr[i]` is not zero, we simply copy it to `arr[j]`.
  4. Increment `i` and `j` accordingly.
- Proof of optimality: This approach is optimal because it only requires a single pass through the array and uses a constant amount of extra space.

```cpp
void duplicateZeros(vector<int>& arr) {
    int i = 0, j = 0;
    while (j < arr.size()) {
        if (arr[i] == 0) {
            if (j + 1 < arr.size()) {
                arr[j + 1] = 0;
            }
            j += 2;
        } else {
            j++;
        }
        i++;
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input array.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of extra space to store the pointers.
> - **Optimality proof:** This solution is optimal because it achieves the best possible time complexity ($O(n)$) and uses minimal extra space ($O(1)$).

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Two-pointer technique, in-place modification.
- Problem-solving patterns identified: Handling zeros and non-zeros differently, using temporary storage or in-place modification.
- Optimization techniques learned: Reducing space complexity by using pointers instead of temporary arrays.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling the case where the array is full after duplicating a zero.
- Edge cases to watch for: Empty array, array with only zeros, array with no zeros.
- Performance pitfalls: Using unnecessary extra space or making multiple passes through the array.
- Testing considerations: Ensure that the solution works correctly for arrays of different sizes and compositions.