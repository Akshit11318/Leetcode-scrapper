## Intersection of Multiple Arrays

**Problem Link:** https://leetcode.com/problems/intersection-of-multiple-arrays/description

**Problem Statement:**
- Input: A list of lists (`nums`) where each sublist contains integers.
- Constraints: Each sublist is non-empty, and all integers are within the range $[1, 10^6]$.
- Expected Output: A list of integers representing the intersection of all sublists.
- Key Requirements:
  - Find common elements across all sublists.
  - Handle edge cases like empty sublists or sublists with no common elements.
- Example Test Cases:
  - `nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]`: Expected output is `[3,4]`.
  - `nums = [[1,2,3],[4,5,6]]`: Expected output is `[]`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking each element of the first sublist against all elements of the subsequent sublists to find common elements.
- This approach is straightforward but inefficient due to its high time complexity.

```cpp
#include <iostream>
#include <vector>
#include <unordered_set>

std::vector<int> intersection(std::vector<std::vector<int>>& nums) {
    if (nums.empty()) return {};
    
    std::unordered_set<int> common;
    for (int num : nums[0]) common.insert(num);
    
    for (int i = 1; i < nums.size(); ++i) {
        std::unordered_set<int> current;
        for (int num : nums[i]) {
            if (common.find(num) != common.end()) {
                current.insert(num);
            }
        }
        common = current;
    }
    
    std::vector<int> result(common.begin(), common.end());
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the number of sublists and $m$ is the maximum size of a sublist. This is because for each sublist, we potentially iterate over all its elements.
> - **Space Complexity:** $O(m)$ for storing the common elements in the set.
> - **Why these complexities occur:** The time complexity is high because we're using nested loops to compare elements across sublists. The space complexity is relatively low because we're storing at most $m$ unique elements in the set.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a hash map (unordered_map in C++) to store the count of each number across all sublists. This way, we can efficiently find numbers that appear in every sublist by checking their count in the map.
- This approach is optimal because it allows us to process each sublist once, reducing the time complexity significantly.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>

std::vector<int> intersection(std::vector<std::vector<int>>& nums) {
    if (nums.empty()) return {};
    
    std::unordered_map<int, int> countMap;
    for (int num : nums[0]) countMap[num]++;
    
    for (int i = 1; i < nums.size(); ++i) {
        std::unordered_map<int, int> currentMap;
        for (int num : nums[i]) {
            if (countMap.find(num) != countMap.end()) {
                currentMap[num]++;
            }
        }
        countMap = currentMap;
    }
    
    std::vector<int> result;
    for (auto& pair : countMap) {
        if (pair.second == nums.size()) {
            result.push_back(pair.first);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the number of sublists and $m$ is the maximum size of a sublist. However, this approach is more efficient in practice because we only iterate over each sublist once and use constant time operations for map lookups.
> - **Space Complexity:** $O(m)$ for storing the count of each number in the map.
> - **Optimality proof:** This is the best possible time complexity because we must at least read the input once. The space complexity is optimal because we need to store information about each unique number.

---

### Final Notes

**Learning Points:**
- Using hash maps to efficiently count occurrences of elements.
- Reducing time complexity by minimizing the number of iterations over input data.
- Understanding the trade-offs between time and space complexity.

**Mistakes to Avoid:**
- Not handling edge cases like empty input lists.
- Incorrectly assuming all sublists have the same size.
- Not validating the input to ensure it meets the problem's constraints.

**Similar Problems to Practice:**
- Intersection of Two Arrays
- Find Common Characters
- Minimum Window Substring