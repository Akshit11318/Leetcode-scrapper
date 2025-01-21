## Intersection of Two Arrays II
**Problem Link:** https://leetcode.com/problems/intersection-of-two-arrays-ii/description

**Problem Statement:**
- Input format and constraints: Given two integer arrays `nums1` and `nums2`, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and the result can be in any order.
- Expected output format: An array of integers representing the intersection of `nums1` and `nums2`.
- Key requirements and edge cases to consider: 
    - The input arrays can contain duplicate elements.
    - The output array should contain each element as many times as it appears in both input arrays.
    - The arrays can be empty or have different lengths.
- Example test cases with explanations:
    - `nums1 = [1,2,2,1], nums2 = [2,2]`: The output should be `[2,2]` because `2` appears twice in both arrays.
    - `nums1 = [4,9,5], nums2 = [9,4,9,8,4]`: The output should be `[4,9]` because each element appears once in both arrays.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The simplest way to solve this problem is to iterate through each element in `nums1` and check if it exists in `nums2`. If it does, add it to the result and remove it from `nums2` to handle duplicates.
- Step-by-step breakdown of the solution:
    1. Initialize an empty result array.
    2. Iterate through each element in `nums1`.
    3. For each element in `nums1`, check if it exists in `nums2`.
    4. If the element exists in `nums2`, add it to the result and remove the first occurrence of this element from `nums2`.
- Why this approach comes to mind first: It directly addresses the requirement of finding intersections while considering duplicates.

```cpp
#include <vector>
using namespace std;

vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
    vector<int> result;
    for (int i = 0; i < nums1.size(); i++) {
        for (int j = 0; j < nums2.size(); j++) {
            if (nums1[i] == nums2[j]) {
                result.push_back(nums1[i]);
                nums2.erase(nums2.begin() + j);
                break;
            }
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ and $m$ are the sizes of `nums1` and `nums2`, respectively, because in the worst case, we are iterating through each element of `nums1` and for each element, we are iterating through `nums2`.
> - **Space Complexity:** $O(n + m)$ for the result array in the worst case when all elements are common.
> - **Why these complexities occur:** The nested loops cause the high time complexity, and the potential size of the result array contributes to the space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a hash map (or an unordered map in C++) to store the frequency of each element in `nums1`. Then, we iterate through `nums2` and for each element, we check if it exists in the hash map. If it does, we add it to the result and decrement its count in the hash map.
- Detailed breakdown of the approach:
    1. Create a hash map to store the frequency of each element in `nums1`.
    2. Iterate through `nums2` and for each element, check if it exists in the hash map.
    3. If an element exists in the hash map, add it to the result and decrement its count in the hash map.
- Proof of optimality: This approach ensures we find all intersections while considering duplicates and does so in a more efficient manner than the brute force approach by avoiding nested loops.

```cpp
#include <vector>
#include <unordered_map>
using namespace std;

vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
    unordered_map<int, int> countMap;
    vector<int> result;
    
    // Count frequency of elements in nums1
    for (int num : nums1) {
        countMap[num]++;
    }
    
    // Find intersections
    for (int num : nums2) {
        if (countMap.find(num) != countMap.end() && countMap[num] > 0) {
            result.push_back(num);
            countMap[num]--;
        }
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$ where $n$ and $m$ are the sizes of `nums1` and `nums2`, respectively, because we are doing a constant amount of work for each element in both arrays.
> - **Space Complexity:** $O(n)$ for the hash map in the worst case when all elements in `nums1` are unique.
> - **Optimality proof:** This is the best possible time complexity because we must at least look at each element once to determine if it is part of the intersection.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Hash map usage for frequency counting and efficient lookup.
- Problem-solving patterns identified: Using data structures to reduce time complexity by avoiding unnecessary comparisons.
- Optimization techniques learned: Replacing nested loops with a single pass through data structures like hash maps.
- Similar problems to practice: Other intersection or set operation problems that can be solved using hash maps or similar data structures.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases like empty input arrays or not checking for the existence of an element in the hash map before decrementing its count.
- Edge cases to watch for: Handling arrays of different sizes or with duplicate elements.
- Performance pitfalls: Using nested loops when a more efficient data structure like a hash map can be used.
- Testing considerations: Ensure to test with arrays of varying sizes, with and without duplicates, and with different intersection sets.