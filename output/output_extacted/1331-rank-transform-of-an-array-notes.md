## Rank Transform of an Array
**Problem Link:** https://leetcode.com/problems/rank-transform-of-an-array/description

**Problem Statement:**
- Input: An array of integers `arr`.
- Constraints: $1 \leq arr.length \leq 10^5$, $1 \leq arr[i] \leq 10^9$.
- Expected Output: Return the array `arr` with each element modified to be its rank in the array.
- Key Requirements: Ranks are assigned in ascending order, starting from 1. If two elements are equal, their rank will be the same, but the rank will be assigned in the order they first appear in the array.
- Example Test Cases:
  - Input: `arr = [40,10,20,30]`
    - Output: `[4,1,2,3]`
    - Explanation: `40` is the largest element, `10` is the smallest, `20` is the second smallest, and `30` is the third smallest.
  - Input: `arr = [100,100,100]`
    - Output: `[1,1,1]`
    - Explanation: All elements are equal, so they all have the same rank.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Sort the array and then iterate through it to assign ranks.
- Step-by-step breakdown:
  1. Create a copy of the array.
  2. Sort the copied array in ascending order.
  3. Initialize a rank counter to 1.
  4. Iterate through the sorted array, assigning the current rank to each element.
  5. If an element is equal to the previous one, assign the same rank; otherwise, increment the rank.
  6. Use a hash map to store the ranks of elements.
  7. Iterate through the original array and replace each element with its rank from the hash map.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>

vector<int> arrayRankTransform(vector<int>& arr) {
    vector<int> sortedArr = arr;
    sort(sortedArr.begin(), sortedArr.end());
    
    unordered_map<int, int> ranks;
    int rank = 1;
    
    for (int i = 0; i < sortedArr.size(); i++) {
        if (ranks.find(sortedArr[i]) == ranks.end()) {
            ranks[sortedArr[i]] = rank;
            rank++;
        }
    }
    
    for (int i = 0; i < arr.size(); i++) {
        arr[i] = ranks[arr[i]];
    }
    
    return arr;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to sorting.
> - **Space Complexity:** $O(n)$ for storing the sorted array and the hash map.
> - **Why these complexities occur:** Sorting requires $O(n \log n)$ time, and storing the ranks in a hash map requires $O(n)$ space.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: Use a hash map to store the ranks directly without sorting the entire array, leveraging the fact that we can iterate through the array to assign ranks based on the sorted order of unique elements.
- Detailed breakdown:
  1. Create a set of unique elements from the array and sort this set.
  2. Initialize a rank counter to 1.
  3. Iterate through the sorted set, assigning the current rank to each unique element in a hash map.
  4. Iterate through the original array, replacing each element with its rank from the hash map.

```cpp
#include <iostream>
#include <vector>
#include <set>
#include <unordered_map>

vector<int> arrayRankTransform(vector<int>& arr) {
    set<int> uniqueElements(arr.begin(), arr.end());
    vector<int> sortedUniqueElements(uniqueElements.begin(), uniqueElements.end());
    
    unordered_map<int, int> ranks;
    int rank = 1;
    
    for (int element : sortedUniqueElements) {
        ranks[element] = rank;
        rank++;
    }
    
    for (int i = 0; i < arr.size(); i++) {
        arr[i] = ranks[arr[i]];
    }
    
    return arr;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to sorting the unique elements.
> - **Space Complexity:** $O(n)$ for storing the set of unique elements and the hash map.
> - **Optimality proof:** This approach is optimal because it minimizes the number of operations required to assign ranks, leveraging the fact that we only need to consider unique elements for ranking.

---

### Final Notes
**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting, using hash maps for efficient lookups, and leveraging sets for unique elements.
- Problem-solving patterns identified: Breaking down the problem into smaller, manageable parts (e.g., sorting unique elements, assigning ranks).
- Optimization techniques learned: Minimizing the number of operations by focusing on unique elements for ranking.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle edge cases (e.g., an empty array), incorrectly assuming the input array is already sorted.
- Performance pitfalls: Using inefficient data structures or algorithms (e.g., not using a hash map for rank lookups).
- Testing considerations: Ensuring test cases cover various scenarios, including arrays with duplicate elements, negative numbers, and arrays of different sizes.