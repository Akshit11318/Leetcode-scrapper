## Sort Array by Parity

**Problem Link:** https://leetcode.com/problems/sort-array-by-parity/description

**Problem Statement:**
- Input format: An array of integers `A` with a length of `n`.
- Constraints: `0 <= n <= 2 * 10^4`, and `0 <= A[i] <= 2 * 10^4` for all `i`.
- Expected output format: The input array `A` sorted in-place such that all even numbers come before all odd numbers.
- Key requirements: The problem requires sorting the array in-place without using extra space that scales with input size, except for a constant amount of space.
- Example test cases:
  - `A = [3, 1, 2, 4]`, the output should be `[2, 4, 3, 1]`.
  - `A = [0]`, the output should be `[0]`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves separating the even and odd numbers and then combining them.
- Step-by-step breakdown:
  1. Create two separate arrays, one for even numbers and one for odd numbers.
  2. Iterate through the input array, placing each number in the appropriate array based on its parity.
  3. Combine the even and odd arrays to form the final sorted array.
- Why this approach comes to mind first: It's straightforward and easy to understand, but it requires extra space that scales with the input size.

```cpp
#include <vector>

void sortArrayByParity(std::vector<int>& A) {
    std::vector<int> even, odd;
    for (int num : A) {
        if (num % 2 == 0) {
            even.push_back(num);
        } else {
            odd.push_back(num);
        }
    }
    A.clear();
    A.insert(A.end(), even.begin(), even.end());
    A.insert(A.end(), odd.begin(), odd.end());
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array, because we make a single pass through the array.
> - **Space Complexity:** $O(n)$, because in the worst case, we might end up storing all elements in the `even` or `odd` array.
> - **Why these complexities occur:** The time complexity is linear because we process each element once, and the space complexity is linear because we use extra arrays that can potentially store all elements.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: We can solve this problem in-place without using extra space that scales with the input size by using two pointers, one starting from the beginning of the array and one from the end.
- Detailed breakdown:
  1. Initialize two pointers, `left` at the start and `right` at the end of the array.
  2. Move the `left` pointer to the right until we find an odd number.
  3. Move the `right` pointer to the left until we find an even number.
  4. Swap the numbers at the `left` and `right` pointers.
  5. Repeat steps 2-4 until `left` meets or crosses `right`.
- Proof of optimality: This approach is optimal because it only requires a single pass through the array and uses a constant amount of extra space.

```cpp
void sortArrayByParity(std::vector<int>& A) {
    int left = 0, right = A.size() - 1;
    while (left < right) {
        if (A[left] % 2 == 0) {
            left++;
        } else if (A[right] % 2 == 1) {
            right--;
        } else {
            std::swap(A[left], A[right]);
            left++;
            right--;
        }
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array, because we potentially visit each element once.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the pointers and do not allocate any additional arrays that scale with input size.
> - **Optimality proof:** This is the best possible time complexity for this problem because we must at least look at each element once to determine its parity. The space complexity is optimal because we do not use any extra space that scales with the input size.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Two-pointer technique, in-place sorting.
- Problem-solving patterns identified: Separating elements based on a condition and then recombining them, optimizing space usage by avoiding unnecessary allocations.
- Optimization techniques learned: Using two pointers to reduce space complexity, avoiding extra allocations.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling edge cases (e.g., an empty array or an array with a single element), not checking for the meeting or crossing of pointers.
- Edge cases to watch for: Empty array, array with a single element, array with all elements of the same parity.
- Performance pitfalls: Using extra space that scales with the input size unnecessarily.
- Testing considerations: Ensure to test with arrays of varying sizes and compositions to cover all edge cases.