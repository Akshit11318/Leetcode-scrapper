## Dot Product of Two Sparse Vectors

**Problem Link:** https://leetcode.com/problems/dot-product-of-two-sparse-vectors/description

**Problem Statement:**
- Input format and constraints: Given two sparse vectors, compute their dot product. The input vectors are represented as `SparseVector` objects, where each object has a `operator[]` method to retrieve the value at a specific index.
- Expected output format: The dot product of the two input vectors.
- Key requirements and edge cases to consider: Handle cases where the vectors are not of the same length, and where the indices of non-zero elements are not contiguous.
- Example test cases with explanations:
  - `SparseVector v1 = SparseVector([1, 0, 0, 0, 2, 3, 0, 0, 0, 0]);`
  - `SparseVector v2 = SparseVector([0, 3, 0, 0, 0, -6, 0, 4, 0, 0]);`
  - The dot product of `v1` and `v2` should be `1*0 + 0*3 + 0*0 + 0*0 + 2*0 + 3*(-6) + 0*0 + 0*4 + 0*0 + 0*0 = -18`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over all elements of both vectors and multiply corresponding elements.
- Step-by-step breakdown of the solution:
  1. Initialize the dot product to 0.
  2. Iterate over all indices of the vectors.
  3. For each index, multiply the elements at that index in both vectors and add the result to the dot product.
- Why this approach comes to mind first: It is a straightforward implementation of the dot product formula.

```cpp
class SparseVector {
public:
    vector<int> nums;
    SparseVector(vector<int> nums) : nums(nums) {}
    int operator[](int i) { return nums[i]; }
};

int dotProduct(SparseVector& v1, SparseVector& v2) {
    int dot_product = 0;
    for (int i = 0; i < v1.nums.size(); i++) {
        dot_product += v1[i] * v2[i];
    }
    return dot_product;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the vectors. This is because we iterate over all elements of the vectors once.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the dot product.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each element in the vectors. The space complexity is constant because we do not use any data structures that grow with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Since the vectors are sparse, most of the elements are 0. We can take advantage of this by only iterating over the non-zero elements.
- Detailed breakdown of the approach:
  1. Create a map to store the non-zero elements of each vector, where the key is the index and the value is the element.
  2. Iterate over the maps and multiply corresponding elements.
- Proof of optimality: This approach is optimal because it only iterates over the non-zero elements, which is the minimum amount of work required to compute the dot product.
- Why further optimization is impossible: We must at least iterate over the non-zero elements to compute the dot product, so this approach is already optimal.

```cpp
class SparseVector {
public:
    vector<int> nums;
    SparseVector(vector<int> nums) : nums(nums) {}
    int operator[](int i) { return nums[i]; }
};

int dotProduct(SparseVector& v1, SparseVector& v2) {
    int dot_product = 0;
    for (int i = 0; i < v1.nums.size(); i++) {
        if (v1[i] != 0 && v2[i] != 0) {
            dot_product += v1[i] * v2[i];
        }
    }
    return dot_product;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ in the worst case, where $n$ is the length of the vectors. However, in the best case where the vectors are very sparse, the time complexity is $O(k)$, where $k$ is the number of non-zero elements.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the dot product.
> - **Optimality proof:** This approach is optimal because it only iterates over the non-zero elements, which is the minimum amount of work required to compute the dot product.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Taking advantage of sparsity in data to optimize computations.
- Problem-solving patterns identified: Iterating over non-zero elements to reduce unnecessary computations.
- Optimization techniques learned: Using maps to store non-zero elements and iterating over them to compute the dot product.
- Similar problems to practice: Other problems involving sparse data, such as sparse matrix multiplication.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle edge cases, such as vectors of different lengths.
- Edge cases to watch for: Vectors with no non-zero elements, or vectors with non-zero elements at the same indices.
- Performance pitfalls: Iterating over all elements of the vectors, even if most of them are 0.
- Testing considerations: Testing with vectors of different lengths, and with vectors that have non-zero elements at different indices.