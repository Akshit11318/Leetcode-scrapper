## Odd Even Jump

**Problem Link:** https://leetcode.com/problems/odd-even-jump/description

**Problem Statement:**
- Input format and constraints: Given an array `A` of integers, where each element is in the range `[1, 10000]`, and the length of `A` is in the range `[1, 20000]`.
- Expected output format: Return the count of numbers in `A` that are **good indices**. A good index is an index `i` where we can reach the end of the array by only doing odd or even jumps.
- Key requirements and edge cases to consider: 
    - A jump from index `i` is allowed if the target index `j` satisfies `A[j] % 2 == A[i] % 2` and `j` is either the smallest or largest possible index that satisfies the condition and is greater than `i`.
    - We can only move forward in the array.
- Example test cases with explanations: 
    - For `A = [10, 13, 12, 14, 15]`, the good indices are `0`, `2`, and `4`, because we can jump to the end of the array starting from these indices by only doing odd or even jumps.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible jumps from each index and check if we can reach the end of the array.
- Step-by-step breakdown of the solution: 
    1. Iterate over each index in the array.
    2. For each index, try all possible odd and even jumps.
    3. Check if we can reach the end of the array from the current index.
- Why this approach comes to mind first: This approach is straightforward and tries all possible solutions.

```cpp
class Solution {
public:
    int oddEvenJumps(vector<int>& A) {
        int n = A.size();
        int count = 0;
        for (int i = 0; i < n; i++) {
            bool canReachEnd = canReachEndFromIndex(A, i);
            if (canReachEnd) {
                count++;
            }
        }
        return count;
    }
    
    bool canReachEndFromIndex(vector<int>& A, int index) {
        int n = A.size();
        bool canReachEnd = false;
        while (index < n - 1) {
            bool foundNextIndex = false;
            int nextIndex = -1;
            for (int i = index + 1; i < n; i++) {
                if (A[i] % 2 == A[index] % 2) {
                    if (!foundNextIndex) {
                        nextIndex = i;
                        foundNextIndex = true;
                    } else {
                        if (A[i] > A[nextIndex]) {
                            nextIndex = i;
                        }
                    }
                }
            }
            if (nextIndex != -1) {
                index = nextIndex;
            } else {
                break;
            }
        }
        if (index == n - 1) {
            canReachEnd = true;
        }
        return canReachEnd;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the array. This is because in the worst case, we are trying all possible jumps from each index.
> - **Space Complexity:** $O(1)$, because we are not using any additional space that scales with the input size.
> - **Why these complexities occur:** These complexities occur because of the nested loops in the brute force approach.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a dynamic programming approach to store the results of subproblems and avoid redundant computation.
- Detailed breakdown of the approach: 
    1. Initialize two arrays `odd` and `even` of size `n`, where `odd[i]` and `even[i]` represent whether we can reach the end of the array from index `i` by only doing odd or even jumps, respectively.
    2. Initialize a sorted array `sortedA` based on the values in `A`.
    3. Iterate over the sorted array and update the `odd` and `even` arrays accordingly.
- Proof of optimality: This approach is optimal because we are only iterating over the array once and using a dynamic programming approach to store the results of subproblems.

```cpp
class Solution {
public:
    int oddEvenJumps(vector<int>& A) {
        int n = A.size();
        vector<bool> odd(n), even(n);
        odd[n - 1] = even[n - 1] = true;
        
        vector<pair<int, int>> sortedA;
        for (int i = 0; i < n; i++) {
            sortedA.push_back({A[i], i});
        }
        sort(sortedA.begin(), sortedA.end());
        
        vector<int> small(n, -1), large(n, -1);
        int smallIdx = -1, largeIdx = -1;
        for (int i = 0; i < n; i++) {
            if (smallIdx < i) {
                smallIdx = i;
            }
            while (smallIdx < n && sortedA[smallIdx].first == sortedA[i].first) {
                small[sortedA[smallIdx].second] = i;
                smallIdx++;
            }
        }
        for (int i = n - 1; i >= 0; i--) {
            if (largeIdx > i) {
                largeIdx = i;
            }
            while (largeIdx >= 0 && sortedA[largeIdx].first == sortedA[i].first) {
                large[sortedA[largeIdx].second] = i;
                largeIdx--;
            }
        }
        
        for (int i = 0; i < n; i++) {
            if (small[i] != -1) {
                if (A[i] % 2 == 0) {
                    even[i] |= odd[sortedA[small[i]].second];
                } else {
                    odd[i] |= even[sortedA[small[i]].second];
                }
            }
            if (large[i] != -1) {
                if (A[i] % 2 == 0) {
                    even[i] |= odd[sortedA[large[i]].second];
                } else {
                    odd[i] |= even[sortedA[large[i]].second];
                }
            }
        }
        
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (odd[i] || even[i]) {
                count++;
            }
        }
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the length of the array. This is because we are sorting the array and then iterating over it once.
> - **Space Complexity:** $O(n)$, because we are using additional space to store the `odd`, `even`, `small`, and `large` arrays.
> - **Optimality proof:** This approach is optimal because we are only iterating over the array once and using a dynamic programming approach to store the results of subproblems.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, sorting, and iteration.
- Problem-solving patterns identified: Using a dynamic programming approach to store the results of subproblems and avoid redundant computation.
- Optimization techniques learned: Sorting the array and using a dynamic programming approach to store the results of subproblems.
- Similar problems to practice: Problems that involve dynamic programming and sorting, such as the "Jump Game" and "Jump Game II" problems.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the `odd` and `even` arrays correctly, not updating the `small` and `large` arrays correctly.
- Edge cases to watch for: The case where the input array is empty, the case where the input array contains duplicate elements.
- Performance pitfalls: Using a brute force approach that tries all possible jumps from each index, not using a dynamic programming approach to store the results of subproblems.
- Testing considerations: Testing the function with different input arrays, including arrays with duplicate elements and arrays with a large number of elements.