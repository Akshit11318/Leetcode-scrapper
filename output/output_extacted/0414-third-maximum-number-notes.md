## Third Maximum Number
**Problem Link:** https://leetcode.com/problems/third-maximum-number/description

**Problem Statement:**
- Input format and constraints: The function takes a list of integers `nums` as input, with a constraint that `1 <= nums.length <= 10^4` and `-2^31 <= nums[i] <= 2^31 - 1`.
- Expected output format: The function should return the third maximum number in the list. If the third maximum number does not exist, return the maximum number.
- Key requirements and edge cases to consider: The input list may contain duplicate numbers, and the list may contain less than three unique numbers.
- Example test cases with explanations: 
    - `nums = [3, 2, 1]`, the output should be `1` because `1` is the third maximum number.
    - `nums = [1, 2]`, the output should be `1` because there is no third maximum number.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find the third maximum number, we can first remove duplicates from the list by converting it to a set, then sort the set in descending order.
- Step-by-step breakdown of the solution: 
    1. Convert the list to a set to remove duplicates.
    2. Sort the set in descending order.
    3. If the set has at least three elements, return the third element; otherwise, return the first element (which is the maximum number).
- Why this approach comes to mind first: This approach is straightforward and easy to implement, making it a natural first thought.

```cpp
#include <vector>
#include <set>
#include <algorithm>

int thirdMax(std::vector<int>& nums) {
    std::set<int> unique_nums(nums.begin(), nums.end());
    std::vector<int> sorted_nums(unique_nums.begin(), unique_nums.end());
    std::sort(sorted_nums.rbegin(), sorted_nums.rend());
    if (sorted_nums.size() >= 3) {
        return sorted_nums[2];
    } else {
        return sorted_nums[0];
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of unique elements in the list. This is because we are sorting the list of unique numbers.
> - **Space Complexity:** $O(n)$, where $n$ is the number of unique elements in the list. This is because we are storing the unique numbers in a set and a vector.
> - **Why these complexities occur:** The sorting operation dominates the time complexity, while the space complexity is due to storing the unique numbers.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of sorting the entire list of unique numbers, we can keep track of the three largest numbers seen so far as we iterate through the list.
- Detailed breakdown of the approach: 
    1. Initialize three variables to store the maximum, second maximum, and third maximum numbers.
    2. Iterate through the list, updating the three variables as we find larger numbers.
    3. If we find a number that is larger than the current maximum, update the maximum, second maximum, and third maximum accordingly.
    4. If we find a number that is larger than the current second maximum but not larger than the maximum, update the second maximum and third maximum.
    5. If we find a number that is larger than the current third maximum but not larger than the second maximum, update the third maximum.
- Proof of optimality: This approach has a time complexity of $O(n)$ because we only need to iterate through the list once, making it more efficient than the brute force approach for large lists.

```cpp
int thirdMax(std::vector<int>& nums) {
    long long max1 = LLONG_MIN, max2 = LLONG_MIN, max3 = LLONG_MIN;
    for (int num : nums) {
        if (num > max1) {
            max3 = max2;
            max2 = max1;
            max1 = num;
        } else if (num > max2 && num != max1) {
            max3 = max2;
            max2 = num;
        } else if (num > max3 && num != max1 && num != max2) {
            max3 = num;
        }
    }
    if (max3 == LLONG_MIN) {
        return max1;
    } else {
        return max3;
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the list. This is because we are iterating through the list once.
> - **Space Complexity:** $O(1)$, because we are using a constant amount of space to store the three maximum numbers.
> - **Optimality proof:** This is the optimal solution because we are only iterating through the list once, making it the most efficient approach in terms of time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The importance of iterating through a list only once to achieve optimal time complexity.
- Problem-solving patterns identified: Keeping track of the maximum, second maximum, and third maximum numbers as we iterate through the list.
- Optimization techniques learned: Avoiding unnecessary sorting operations by using a single pass through the list.
- Similar problems to practice: Finding the kth largest element in an array, finding the minimum window that contains all elements of a given array.

**Mistakes to Avoid:**
- Common implementation errors: Not handling the case where the third maximum number does not exist.
- Edge cases to watch for: Lists with less than three unique elements, lists with duplicate elements.
- Performance pitfalls: Using sorting operations unnecessarily, which can increase the time complexity.
- Testing considerations: Test the function with lists of varying sizes and with lists that have less than three unique elements.