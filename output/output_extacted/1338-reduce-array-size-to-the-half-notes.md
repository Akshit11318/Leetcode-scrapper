## Reduce Array Size to The Half
**Problem Link:** https://leetcode.com/problems/reduce-array-size-to-the-half/description

**Problem Statement:**
- Input format: An array of integers `arr`.
- Constraints: `2 <= arr.length <= 100`.
- Expected output format: The length of the resulting array after removing the least frequent elements.
- Key requirements: Remove the least frequent elements until the array size is reduced to half.
- Edge cases: If there are multiple elements with the same least frequency, remove any of them.

### Example Test Cases:
- Input: `arr = [3,3,3,3,5,5,5,2,2,7]`
  Output: `5`
- Input: `arr = [1,9]`
  Output: `1`

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Count the frequency of each element in the array and sort these frequencies.
- Step-by-step breakdown:
  1. Count the frequency of each element.
  2. Sort the frequencies in ascending order.
  3. Remove the least frequent elements until the array size is reduced to half.

```cpp
#include <iostream>
#include <map>
#include <vector>
#include <algorithm>

int minSize(std::vector<int>& arr) {
    std::map<int, int> freq;
    for (auto& num : arr) {
        freq[num]++;
    }

    std::vector<int> frequencies;
    for (auto& pair : freq) {
        frequencies.push_back(pair.second);
    }

    std::sort(frequencies.begin(), frequencies.end());

    int halfSize = arr.size() / 2;
    int removed = 0;
    for (int freq : frequencies) {
        removed += freq;
        if (removed >= halfSize) break;
    }

    return arr.size() - removed;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to sorting the frequencies, where $n$ is the number of unique elements in the array.
> - **Space Complexity:** $O(n)$ for storing the frequencies of elements.
> - **Why these complexities occur:** Sorting the frequencies to find the least frequent elements causes the time complexity, and storing the frequencies in a map and vector causes the space complexity.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: Use a `multiset` to store the frequencies of elements, which allows for efficient removal of the least frequent elements.
- Detailed breakdown:
  1. Count the frequency of each element.
  2. Store the frequencies in a `multiset`.
  3. Remove the least frequent elements from the `multiset` until the array size is reduced to half.

```cpp
#include <iostream>
#include <map>
#include <set>
#include <vector>

int minSize(std::vector<int>& arr) {
    std::map<int, int> freq;
    for (auto& num : arr) {
        freq[num]++;
    }

    std::multiset<int> frequencies;
    for (auto& pair : freq) {
        frequencies.insert(pair.second);
    }

    int halfSize = arr.size() / 2;
    int removed = 0;
    while (removed < halfSize) {
        int minFreq = *frequencies.begin();
        frequencies.erase(frequencies.begin());
        removed += minFreq;
    }

    return arr.size() - removed;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to inserting and removing elements from the `multiset`, where $n$ is the number of unique elements in the array.
> - **Space Complexity:** $O(n)$ for storing the frequencies of elements.
> - **Optimality proof:** This approach is optimal because it uses the most efficient data structure (a `multiset`) to remove the least frequent elements, and it only requires a single pass through the array to count the frequencies.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: frequency counting, sorting, and using a `multiset` for efficient removal of least frequent elements.
- Problem-solving patterns: breaking down the problem into smaller steps (counting frequencies, sorting, and removing elements).
- Optimization techniques: using the most efficient data structure (a `multiset`) to reduce the time complexity.

**Mistakes to Avoid:**
- Common implementation errors: not handling edge cases (e.g., an empty array or an array with a single element).
- Performance pitfalls: using an inefficient data structure (e.g., a vector) to store and remove the least frequent elements.
- Testing considerations: testing the function with different input sizes and edge cases to ensure correctness and efficiency.