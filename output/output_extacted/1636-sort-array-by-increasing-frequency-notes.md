## Sort Array by Increasing Frequency
**Problem Link:** https://leetcode.com/problems/sort-array-by-increasing-frequency/description

**Problem Statement:**
- Input format: An array of integers `nums`.
- Constraints: $1 \leq nums.length \leq 100$ and $1 \leq nums[i] \leq 100$.
- Expected output format: The array sorted by the frequency of its elements. Elements with the same frequency should be sorted by their value in ascending order.
- Key requirements and edge cases to consider: Handling duplicate elements, sorting by frequency and then by value.
- Example test cases with explanations:
  - Input: `nums = [1,1,2,2,3]`
    - Output: `[3,1,1,2,2]`
    - Explanation: The frequency of `3` is 1, `1` is 2, and `2` is 2. Sorting by frequency and then by value gives the output.
  - Input: `nums = [1,1,2,2,3,3,4,4,4]`
    - Output: `[1,1,2,2,3,3,4,4,4]`
    - Explanation: The frequency of `1` and `2` is 2, `3` is 2, and `4` is 3. Sorting by frequency and then by value gives the output.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Count the frequency of each element, then sort the array based on these frequencies and values.
- Step-by-step breakdown of the solution:
  1. Create a frequency map of the elements in the array.
  2. Create a new array of pairs where each pair contains an element and its frequency.
  3. Sort the array of pairs based on the frequency and value.
  4. Create the final sorted array by iterating through the sorted pairs.
- Why this approach comes to mind first: It directly addresses the requirements of sorting by frequency and then by value.

```cpp
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

std::vector<int> frequencySort(std::vector<int>& nums) {
    std::map<int, int> frequencyMap;
    for (int num : nums) {
        frequencyMap[num]++;
    }

    std::vector<std::pair<int, int>> frequencyVector;
    for (auto& pair : frequencyMap) {
        frequencyVector.push_back(pair);
    }

    std::sort(frequencyVector.begin(), frequencyVector.end(), [](const auto& a, const auto& b) {
        if (a.second == b.second) {
            return a.first < b.first;
        }
        return a.second < b.second;
    });

    std::vector<int> result;
    for (auto& pair : frequencyVector) {
        for (int i = 0; i < pair.second; i++) {
            result.push_back(pair.first);
        }
    }

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of unique elements in the array. This is because we're sorting the vector of pairs.
> - **Space Complexity:** $O(n)$, for storing the frequency map and the vector of pairs.
> - **Why these complexities occur:** The sorting operation dominates the time complexity, and the storage of frequencies and pairs dominates the space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Utilize a more efficient data structure, such as `std::unordered_map` for frequency counting, and leverage the `std::sort` function with a custom comparator for sorting.
- Detailed breakdown of the approach:
  1. Use `std::unordered_map` to count the frequency of each element.
  2. Use `std::sort` with a custom comparator that first compares the frequencies and then the values.
- Proof of optimality: This approach minimizes the number of operations needed to sort the array by frequency and then by value.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

std::vector<int> frequencySort(std::vector<int>& nums) {
    std::unordered_map<int, int> frequencyMap;
    for (int num : nums) {
        frequencyMap[num]++;
    }

    std::sort(nums.begin(), nums.end(), [&frequencyMap](int a, int b) {
        if (frequencyMap[a] == frequencyMap[b]) {
            return a < b;
        }
        return frequencyMap[a] < frequencyMap[b];
    });

    return nums;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the length of the input array. This is due to the sorting operation.
> - **Space Complexity:** $O(n)$, for storing the frequency map.
> - **Optimality proof:** This solution is optimal because it uses the most efficient data structures and algorithms available for the task, minimizing both time and space complexities.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting, frequency counting, and custom comparators.
- Problem-solving patterns identified: Using efficient data structures and algorithms to minimize complexity.
- Optimization techniques learned: Leveraging `std::unordered_map` for frequency counting and `std::sort` with a custom comparator for efficient sorting.
- Similar problems to practice: Other sorting and frequency-based problems.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly implementing the custom comparator or using inefficient data structures.
- Edge cases to watch for: Handling arrays with duplicate elements or elements with the same frequency.
- Performance pitfalls: Using overly complex or inefficient algorithms that lead to high time or space complexity.
- Testing considerations: Ensuring the solution works correctly for various input scenarios, including edge cases.