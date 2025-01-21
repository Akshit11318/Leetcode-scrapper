## Create Target Array in the Given Order
**Problem Link:** https://leetcode.com/problems/create-target-array-in-the-given-order/description

**Problem Statement:**
- Input: Two arrays, `index` and `values`, where `index` contains the positions to insert the corresponding values from `values` into a new array.
- Constraints: `0 <= index.length <= 100` and `index.length == values.length`.
- Expected output: The target array after inserting all values according to the given indices.
- Key requirements: Maintain the relative order of elements based on the insertion indices.

### Brute Force Approach
**Explanation:**
- The initial thought process involves directly inserting values at the specified indices in a new array. However, this approach requires shifting elements to the right for each insertion, which is inefficient.
- Step-by-step breakdown:
  1. Initialize an empty array `target` to store the result.
  2. Iterate over the `index` and `values` arrays simultaneously.
  3. For each pair of `index` and `value`, insert the `value` at the specified `index` in the `target` array by shifting all elements to the right of the `index` one position to the right.

```cpp
#include <vector>

std::vector<int> createTargetArray(std::vector<int>& index, std::vector<int>& values) {
    std::vector<int> target;
    for (int i = 0; i < index.size(); ++i) {
        // Insert value at index i in target, shifting elements if necessary
        target.insert(target.begin() + index[i], values[i]);
    }
    return target;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the `index` array. This is because in the worst case, for each insertion, we might need to shift all previous elements.
> - **Space Complexity:** $O(n)$, for storing the `target` array.
> - **Why these complexities occur:** The time complexity is quadratic due to the insertion operation in the vector, which may require shifting all elements to the right of the insertion point. The space complexity is linear as we need to store all elements from the `values` array in the `target` array.

### Optimal Approach (Required)
**Explanation:**
- Key insight: Utilize the `std::vector` class's `insert` method, which handles shifting elements internally, but recognize that inserting at the end and then rearranging is more efficient than shifting for each insertion.
- Detailed breakdown:
  1. Initialize an empty vector `target`.
  2. Iterate through the `index` and `values` arrays.
  3. For each `value`, append it to the end of the `target` vector.
  4. After all values are appended, rearrange the `target` vector based on the `index` array to get the final order.

However, a more efficient approach involves directly using the indices to place the values in their correct positions without the need for shifting elements during insertion, which can be achieved by maintaining a separate data structure or by utilizing the properties of the given indices.

```cpp
#include <vector>

std::vector<int> createTargetArray(std::vector<int>& index, std::vector<int>& values) {
    std::vector<int> target;
    target.reserve(index.size()); // Reserve space for efficiency
    for (int i = 0; i < index.size(); ++i) {
        target.insert(target.begin() + index[i], values[i]);
    }
    return target;
}
```

> Complexity Analysis:
> - **Time Complexity:** Still $O(n^2)$ in the worst case, due to the insertion operation. However, reserving space can improve performance in practice.
> - **Space Complexity:** $O(n)$, for storing the `target` array.
> - **Optimality proof:** While the time complexity remains quadratic, this approach is straightforward and leverages the `std::vector` class's capabilities, making it a practical solution.

### Alternative Approach
**Explanation:**
- Instead of inserting elements into the `target` vector, which may require shifting, we can create the `target` vector with the correct size initially and then fill it according to the `index` array. This approach avoids the shifting issue but requires a single pass through the data.

```cpp
#include <vector>

std::vector<int> createTargetArray(std::vector<int>& index, std::vector<int>& values) {
    std::vector<int> target(index.size());
    for (int i = 0; i < index.size(); ++i) {
        target[index[i]] = values[i];
    }
    return target;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the `index` array, as we make a single pass through the data.
> - **Space Complexity:** $O(n)$, for storing the `target` array.
> - **Trade-off analysis:** This approach is more efficient than the previous ones, especially for large inputs, as it avoids the shifting operation during insertion.

### Final Notes

**Learning Points:**
- Understanding the implications of using `std::vector` methods like `insert`.
- Recognizing the importance of reserving space in vectors for efficiency.
- Identifying when a direct construction approach can be more efficient than iterative insertion.

**Mistakes to Avoid:**
- Not considering the performance impact of shifting elements in vectors.
- Not reserving space in vectors when the final size is known.
- Overlooking simpler, more efficient algorithms.