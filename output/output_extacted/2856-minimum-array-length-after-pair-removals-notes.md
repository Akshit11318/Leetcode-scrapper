## Minimum Array Length After Pair Removals

**Problem Link:** https://leetcode.com/problems/minimum-array-length-after-pair-removals/description

**Problem Statement:**
- Input: An integer array `nums` and an integer `k`.
- Constraints: `2 <= nums.length <= 10^5`, `1 <= nums[i] <= 10^9`, `1 <= k <= nums.length / 2`.
- Expected Output: The minimum length of `nums` after removing `k` pairs of elements that have the same value.
- Key Requirements and Edge Cases:
  - The order of elements in the array does not matter.
  - A pair consists of two elements with the same value.
  - The task is to minimize the length of the array after removing `k` pairs.

**Example Test Cases:**
- Input: `nums = [3,1,3,4,3,4,4,5,2], k = 2`
  - Output: `4`
  - Explanation: Remove two pairs of elements that have the same value: `[3,3]` and `[4,4]`. The remaining array is `[1,3,4,5,2]`.
- Input: `nums = [1,1,1,1,1], k = 1`
  - Output: `3`
  - Explanation: Remove one pair of elements that have the same value: `[1,1]`. The remaining array is `[1,1,1]`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to try all possible combinations of removing pairs from the array.
- The step-by-step breakdown involves:
  1. Generating all possible pairs of elements with the same value.
  2. For each possible pair, remove it from the array.
  3. Repeat the process until `k` pairs have been removed or no more pairs can be found.
- This approach comes to mind first because it directly addresses the problem statement without considering optimizations.

```cpp
#include <vector>
#include <unordered_map>

int minArrayLength(std::vector<int>& nums, int k) {
    std::unordered_map<int, int> count;
    for (int num : nums) {
        count[num]++;
    }
    
    int removed = 0;
    for (auto& pair : count) {
        while (pair.second >= 2 && k > 0) {
            pair.second -= 2;
            k--;
            removed += 2;
        }
    }
    
    return nums.size() - removed;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the size of `nums` and $m$ is the number of unique elements in `nums`. The reason is that we iterate over `nums` to count occurrences and then iterate over the unique elements to remove pairs.
> - **Space Complexity:** $O(m)$, where $m$ is the number of unique elements in `nums`, because we use a map to store the count of each element.
> - **Why these complexities occur:** The time complexity is due to the iteration over `nums` and the unique elements. The space complexity is due to the storage of unique elements in the map.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to realize that we can directly calculate the maximum number of pairs that can be removed from the array without explicitly trying all combinations.
- The detailed breakdown involves:
  1. Counting the occurrences of each element in the array.
  2. For each element, calculating how many pairs can be removed based on its count.
  3. Summing up the pairs that can be removed for all elements and taking the minimum between this sum and `k`.
- The proof of optimality is that this approach considers all possible pairs that can be removed in a single pass, ensuring no potential removal is missed.

```cpp
#include <vector>
#include <unordered_map>

int minArrayLength(std::vector<int>& nums, int k) {
    std::unordered_map<int, int> count;
    for (int num : nums) {
        count[num]++;
    }
    
    int totalPairs = 0;
    for (auto& pair : count) {
        totalPairs += pair.second / 2;
    }
    
    int removed = std::min(totalPairs, k) * 2;
    
    return nums.size() - removed;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the size of `nums` and $m$ is the number of unique elements in `nums`. The reason is that we iterate over `nums` to count occurrences and then iterate over the unique elements to calculate the total pairs.
> - **Space Complexity:** $O(m)$, where $m$ is the number of unique elements in `nums`, because we use a map to store the count of each element.
> - **Optimality proof:** This approach is optimal because it directly calculates the maximum number of pairs that can be removed in a single pass, without the need for explicit combination generation or removal.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Hashing (using maps to count occurrences), greedy approach (removing as many pairs as possible directly).
- Problem-solving patterns identified: Counting occurrences, calculating pairs based on counts, and optimizing removals.
- Optimization techniques learned: Direct calculation of removable pairs instead of trying all combinations.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect counting of pairs, not considering the minimum between total pairs and `k`.
- Edge cases to watch for: When `k` is greater than the total number of pairs that can be removed, when `nums` has an odd length and `k` is half of it.
- Performance pitfalls: Using inefficient data structures or algorithms for counting and calculating pairs.
- Testing considerations: Test with arrays of varying lengths, with different distributions of elements, and with `k` values ranging from 0 to half the length of the array.