## Relative Sort Array

**Problem Link:** https://leetcode.com/problems/relative-sort-array/description

**Problem Statement:**
- Input format and constraints: Given two arrays `arr1` and `arr2`, the task is to sort `arr1` in ascending order, but with a twist. If `arr1` contains elements that are also present in `arr2`, those elements should appear in the same order as they do in `arr2`. The elements in `arr1` that are not present in `arr2` should be placed after the elements that are present in `arr2`, in ascending order.
- Expected output format: The function should return the modified `arr1` array.
- Key requirements and edge cases to consider: Handling duplicate elements, ensuring the order of elements from `arr2` is preserved, and placing elements not in `arr2` in ascending order.
- Example test cases with explanations: For instance, given `arr1 = [2,3,1,3,2,4,6,7,9,2,19]` and `arr2 = [2,1,6,9,11,5]`, the output should be `[2,2,2,1,6,9,3,3,4,7,19]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: A straightforward approach is to iterate through `arr2` and append its elements to the result array if they are present in `arr1`. After that, append the remaining elements from `arr1` (not present in `arr2`) in ascending order.
- Step-by-step breakdown of the solution:
  1. Create a copy of `arr1` to avoid modifying the original array.
  2. Iterate through `arr2` and for each element, find and remove it from the copy of `arr1` as many times as it appears.
  3. Sort the remaining elements in the copy of `arr1`.
  4. Combine the elements from `arr2` (in the order they appeared) with the sorted remaining elements.
- Why this approach comes to mind first: It directly addresses the requirement of preserving the order of elements from `arr2` and then sorting the rest.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
    vector<int> result;
    // Iterate through arr2
    for (int num : arr2) {
        // Remove num from arr1 as many times as it appears
        while (find(arr1.begin(), arr1.end(), num) != arr1.end()) {
            result.push_back(num);
            arr1.erase(find(arr1.begin(), arr1.end(), num));
        }
    }
    // Sort the remaining elements in arr1
    sort(arr1.begin(), arr1.end());
    // Append the sorted remaining elements to the result
    result.insert(result.end(), arr1.begin(), arr1.end());
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m + n \log n)$ where $n$ is the size of `arr1` and $m$ is the size of `arr2`, because for each element in `arr2`, we potentially search through `arr1`, and then we sort `arr1`.
> - **Space Complexity:** $O(n)$ for storing the result and the modified `arr1`.
> - **Why these complexities occur:** The time complexity is dominated by the search and removal of elements from `arr1` for each element in `arr2`, followed by the sorting of `arr1`. The space complexity is due to the storage of the result and the temporary modification of `arr1`.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of searching and removing elements one by one, we can use a frequency count approach to efficiently count the occurrences of each number in `arr1` and then reconstruct the array based on the order of elements in `arr2` and the remaining elements in ascending order.
- Detailed breakdown of the approach:
  1. Count the frequency of each number in `arr1`.
  2. Iterate through `arr2` and append its elements to the result as many times as they appear in `arr1`, decrementing their counts.
  3. Iterate through the remaining numbers (not in `arr2`) in ascending order and append them to the result as many times as they appear.
- Proof of optimality: This approach ensures that we only iterate through `arr1` and `arr2` a constant number of times, avoiding the inefficiency of the brute force approach.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>

vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
    unordered_map<int, int> count;
    for (int num : arr1) {
        count[num]++;
    }
    
    vector<int> result;
    // Append elements from arr2
    for (int num : arr2) {
        if (count.find(num) != count.end()) {
            for (int i = 0; i < count[num]; i++) {
                result.push_back(num);
            }
            count.erase(num);
        }
    }
    // Append remaining elements in ascending order
    for (auto& pair : count) {
        for (int i = 0; i < pair.second; i++) {
            result.push_back(pair.first);
        }
    }
    sort(result.begin(), result.end());
    return result;
}
```

However, the above code can be optimized by avoiding the final sort, as we can directly append the remaining elements in ascending order:

```cpp
vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
    unordered_map<int, int> count;
    for (int num : arr1) {
        count[num]++;
    }
    
    vector<int> result;
    // Append elements from arr2
    for (int num : arr2) {
        if (count.find(num) != count.end()) {
            for (int i = 0; i < count[num]; i++) {
                result.push_back(num);
            }
            count.erase(num);
        }
    }
    // Append remaining elements in ascending order
    for (int i = 0; i <= 1000; i++) {
        if (count.find(i) != count.end()) {
            for (int j = 0; j < count[i]; j++) {
                result.push_back(i);
            }
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$ where $n$ is the size of `arr1` and $m` is the size of `arr2`, because we make a constant number of passes through the input arrays.
> - **Space Complexity:** $O(n)$ for storing the frequency count of elements in `arr1`.
> - **Optimality proof:** This approach is optimal because it minimizes the number of operations required to solve the problem, avoiding unnecessary searches and sorts.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Frequency counting, iteration through arrays, and appending elements based on conditions.
- Problem-solving patterns identified: Using `unordered_map` for efficient frequency counting, iterating through arrays to reconstruct the result.
- Optimization techniques learned: Avoiding unnecessary searches and sorts by using a frequency count approach.
- Similar problems to practice: Other array manipulation and sorting problems, such as custom sorting based on specific conditions.

**Mistakes to Avoid:**
- Common implementation errors: Failing to handle edge cases, such as empty input arrays or arrays with duplicate elements.
- Edge cases to watch for: Arrays with negative numbers, arrays with numbers outside the range of 0 to 1000, and arrays with a large number of duplicate elements.
- Performance pitfalls: Using inefficient algorithms, such as the brute force approach, for large input arrays.
- Testing considerations: Thoroughly testing the function with various input cases, including edge cases, to ensure correctness and efficiency.