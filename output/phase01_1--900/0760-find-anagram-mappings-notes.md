## Find Anagram Mappings
**Problem Link:** https://leetcode.com/problems/find-anagram-mappings/description

**Problem Statement:**
- Input: Two integer arrays `A` and `B` where `A` has a length of `n` and `B` has a length of `n`. `B` is an anagram of `A`.
- Constraints: `1 <= A.length == B.length == n <= 10^5`, `1 <= A[i], B[i] <= 10^5`
- Expected Output: An integer array `P` of length `n` where `P[i]` is the index of the element in `B` which is the anagram of `A[i]`.
- Key Requirements: For each element in `A`, find its corresponding anagram in `B`.
- Edge Cases: All elements in `A` will have a corresponding anagram in `B`.

### Example Test Cases:
- **Test Case 1:** `A = [12, 28, 46], B = [46, 12, 28]`, Expected Output: `[1, 0, 2]`
- **Test Case 2:** `A = [1, 2, 3], B = [3, 1, 2]`, Expected Output: `[1, 0, 2]`

---

### Brute Force Approach
**Explanation:**
- For each element `A[i]` in array `A`, iterate through array `B` to find the anagram.
- Once found, store the index of the anagram in the result array `P`.
- This approach is straightforward but inefficient for large inputs.

```cpp
vector<int> anagramMappings(vector<int>& A, vector<int>& B) {
    vector<int> P;
    for (int i = 0; i < A.size(); i++) {
        for (int j = 0; j < B.size(); j++) {
            if (A[i] == B[j]) {
                P.push_back(j);
                break; // Assuming there's only one anagram for simplicity
            }
        }
    }
    return P;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of arrays `A` and `B`. This is because for each element in `A`, we potentially iterate through all elements in `B`.
> - **Space Complexity:** $O(n)$, for storing the result array `P`.
> - **Why these complexities occur:** The nested loops cause the quadratic time complexity, and the need to store the result for each element in `A` leads to the linear space complexity.

---

### Optimal Approach (Required)
**Explanation:**
- Create a hash map (unordered_map in C++) where the keys are the elements of `B` and the values are their indices.
- Then, for each element in `A`, look up its index in `B` using the hash map.
- This approach reduces the time complexity significantly because looking up an element in a hash map is an average $O(1)$ operation.

```cpp
vector<int> anagramMappings(vector<int>& A, vector<int>& B) {
    unordered_map<int, int> indexMap;
    for (int i = 0; i < B.size(); i++) {
        indexMap[B[i]] = i; // Store index of each element in B
    }
    vector<int> P;
    for (int i = 0; i < A.size(); i++) {
        P.push_back(indexMap[A[i]]); // Find index of A[i] in B
    }
    return P;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of arrays `A` and `B`. This is because we perform a constant amount of work for each element in both arrays.
> - **Space Complexity:** $O(n)$, for storing the hash map and the result array `P`.
> - **Optimality proof:** This solution is optimal because we only iterate through each array once, achieving the best possible time complexity for this problem.

---

### Final Notes
**Learning Points:**
- The importance of using hash maps for efficient lookups.
- How to approach problems involving anagrams and mappings.
- Optimization techniques to reduce time complexity from $O(n^2)$ to $O(n)$.

**Mistakes to Avoid:**
- Not considering the use of hash maps for lookup operations.
- Not checking for edge cases, such as an empty input array.
- Failing to validate the input arrays `A` and `B` to ensure they are of the same length.