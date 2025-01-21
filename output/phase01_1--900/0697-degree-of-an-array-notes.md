## Degree of an Array
**Problem Link:** https://leetcode.com/problems/degree-of-an-array/description

**Problem Statement:**
- Input: An integer array `nums`.
- Output: The shortest subarray length that contains all `nums` elements with their highest frequency.
- Key Requirements:
  - The subarray must contain all unique elements of `nums`.
  - The frequency of each element within the subarray should match its highest frequency in `nums`.
- Edge Cases:
  - If `nums` is empty, return 0.
  - If `nums` contains only one unique element, return 1.

**Example Test Cases:**
- `nums = [1, 2, 2, 3, 1]`: The answer is 2 because `[1, 2, 2, 3, 1]` contains all elements with their highest frequency. However, we can get a shorter subarray `[2, 2]` for the element 2, but we cannot get a subarray of length less than 2 that contains all unique elements (1, 2, 3) with their highest frequency.
- `nums = [1, 2, 2, 3, 1, 4, 2]`: The answer is 6 because the subarray `[1, 2, 2, 3, 1, 4, 2]` contains all unique elements with their highest frequency, but any subarray of length less than 6 will not satisfy this condition.

---

### Brute Force Approach
**Explanation:**
- The initial thought process involves checking every possible subarray of `nums` to see if it contains all unique elements with their highest frequency.
- We iterate over all possible start and end indices of subarrays.
- For each subarray, we calculate the frequency of each unique element and compare it with its highest frequency in `nums`.
- If a subarray satisfies the condition, we update our answer with the minimum length found so far.

```cpp
#include <vector>
#include <unordered_map>
using namespace std;

int findShortestSubArray(vector<int>& nums) {
    unordered_map<int, int> count, first, last;
    for (int i = 0; i < nums.size(); ++i) {
        if (count.find(nums[i]) == count.end()) {
            first[nums[i]] = i;
        }
        last[nums[i]] = i;
        count[nums[i]]++;
    }

    int degree = 0;
    for (auto& pair : count) {
        degree = max(degree, pair.second);
    }

    int min_length = nums.size();
    for (auto& pair : count) {
        if (pair.second == degree) {
            min_length = min(min_length, last[pair.first] - first[pair.first] + 1);
        }
    }

    return min_length;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the length of `nums`. This is because we iterate over `nums` once to calculate the frequency, first occurrence, and last occurrence of each element.
> - **Space Complexity:** $O(n)$ because in the worst case, every element in `nums` could be unique, requiring space to store all of them in our maps.
> - **Why these complexities occur:** These complexities occur because we need to process each element in `nums` at least once to calculate frequencies and find the first and last occurrence of each element.

---

### Optimal Approach (Required)
**Explanation:**
- The optimal solution involves a single pass through `nums` to calculate the frequency, first occurrence, and last occurrence of each element.
- We maintain a `count` map to store the frequency of each element, a `first` map to store the index of the first occurrence of each element, and a `last` map to store the index of the last occurrence of each element.
- After calculating these, we find the degree of the array by finding the maximum frequency.
- Then, for each element with the maximum frequency, we calculate the length of the subarray that contains it with the highest frequency and update our answer with the minimum length found.

```cpp
#include <vector>
#include <unordered_map>
using namespace std;

int findShortestSubArray(vector<int>& nums) {
    unordered_map<int, int> count, first, last;
    for (int i = 0; i < nums.size(); ++i) {
        if (count.find(nums[i]) == count.end()) {
            first[nums[i]] = i;
        }
        last[nums[i]] = i;
        count[nums[i]]++;
    }

    int degree = 0;
    for (auto& pair : count) {
        degree = max(degree, pair.second);
    }

    int min_length = nums.size();
    for (auto& pair : count) {
        if (pair.second == degree) {
            min_length = min(min_length, last[pair.first] - first[pair.first] + 1);
        }
    }

    return min_length;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the length of `nums`.
> - **Space Complexity:** $O(n)$ because in the worst case, every element in `nums` could be unique.
> - **Optimality proof:** This solution is optimal because we only need to process each element in `nums` once to find the degree and the shortest subarray that contains all elements with their highest frequency.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: frequency counting, first and last occurrence of elements.
- Problem-solving patterns: finding the degree of an array and the shortest subarray that satisfies a condition.
- Optimization techniques: single pass through the input array.

**Mistakes to Avoid:**
- Not considering edge cases, such as an empty input array.
- Not optimizing the solution to find the shortest subarray, leading to inefficient solutions.
- Not using data structures like maps to efficiently store and retrieve element frequencies and occurrences.