## Find Original Array from Doubled Array
**Problem Link:** https://leetcode.com/problems/find-original-array-from-doubled-array/description

**Problem Statement:**
- Input: An integer array `changed` of length `n`.
- Constraints: `1 <= n <= 10^4`, `1 <= changed[i] <= 10^6`.
- Expected output: The original array if it exists, otherwise an empty array.
- Key requirements: Determine if it's possible to construct the original array where each element was doubled to get the `changed` array.
- Edge cases: Empty input, arrays with odd length, arrays with elements that cannot be halved.

**Example Test Cases:**
- `changed = [1,2,3,4]`: No solution because `1` and `3` are not doubled in the array.
- `changed = [1,2,4,8,16]`: The original array could be `[1,2,4,8]`, but this doesn't cover `16`, which is also a doubled element, so there's no solution.
- `changed = [4,2,1,3]`: Sorting and then trying to construct the original array by halving elements shows that there's no valid sequence.

---

### Brute Force Approach
**Explanation:**
- The initial thought is to try every possible combination of elements from the `changed` array to see if halving them could form a sequence that, when doubled, gives back the `changed` array.
- This involves generating all permutations of the `changed` array and checking each permutation.

```cpp
#include <vector>
#include <algorithm>

std::vector<int> findOriginalArray(std::vector<int>& changed) {
    std::sort(changed.begin(), changed.end());
    std::vector<int> original;
    
    // Attempt to construct the original array by halving elements
    while (!changed.empty()) {
        int first = changed[0];
        changed.erase(changed.begin());
        
        // Try to find the doubled element in the remaining array
        auto it = std::find(changed.begin(), changed.end(), first * 2);
        if (it != changed.end()) {
            original.push_back(first);
            changed.erase(it);
        } else {
            // If the doubled element is not found, return empty array
            return {};
        }
    }
    
    return original;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ due to the use of `std::find` within a loop over the array.
> - **Space Complexity:** $O(n)$ for storing the original array.
> - **Why these complexities occur:** The brute force approach involves searching for each element's double in the array, leading to quadratic time complexity.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to use a frequency map to store the count of each number in the `changed` array, then iteratively try to remove elements and their doubles from the map.
- This approach ensures that we are efficiently checking for the presence of doubled elements without unnecessary searches.

```cpp
#include <vector>
#include <unordered_map>
#include <algorithm>

std::vector<int> findOriginalArray(std::vector<int>& changed) {
    std::sort(changed.begin(), changed.end());
    std::unordered_map<int, int> freq;
    std::vector<int> original;
    
    // Count frequency of each number
    for (int num : changed) {
        freq[num]++;
    }
    
    // Try to construct the original array
    for (int num : changed) {
        if (freq[num] == 0) continue;
        freq[num]--;
        
        // Check if the double exists
        if (freq.find(2 * num) != freq.end() && freq[2 * num] > 0) {
            freq[2 * num]--;
            original.push_back(num);
        } else {
            // If the double does not exist, return empty array
            return {};
        }
    }
    
    return original;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to sorting, and $O(n)$ for constructing the frequency map and the original array, resulting in overall $O(n \log n)$ complexity.
> - **Space Complexity:** $O(n)$ for storing the frequency map and the original array.
> - **Optimality proof:** This approach is optimal because it efficiently utilizes a frequency map to avoid unnecessary searches, reducing the time complexity to linear after the initial sort.

---

### Final Notes
**Learning Points:**
- Using frequency maps to efficiently count and manage elements.
- The importance of sorting in simplifying the problem and reducing complexity.
- Constructing the original array by iteratively removing elements and their doubles.

**Mistakes to Avoid:**
- Not checking for the existence of doubled elements before adding them to the original array.
- Not handling edge cases where the input array is empty or contains elements that cannot be halved.
- Failing to sort the array before attempting to construct the original array, which can lead to incorrect results.