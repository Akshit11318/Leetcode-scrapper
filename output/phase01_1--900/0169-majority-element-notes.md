## Majority Element

**Problem Link:** https://leetcode.com/problems/majority-element/description

**Problem Statement:**
- Input format: An array of integers `nums`.
- Constraints: `1 <= nums.length <= 5 * 10^4`, `10^9 <= nums[i] <= 10^9`.
- Expected output format: The majority element in the array.
- Key requirements and edge cases to consider: The majority element is the element that appears more than `n/2` times where `n` is the size of the array. The input array is guaranteed to have a majority element.
- Example test cases with explanations:
  - Example 1: Input: `nums = [3,2,3]`, Output: `3`. Explanation: `3` appears twice which is more than `n/2`.
  - Example 2: Input: `nums = [2,2,1,1,1,2,2]`, Output: `2`. Explanation: `2` appears four times which is more than `n/2`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: One way to solve this problem is to use a hash map to store the frequency of each element in the array. Then, iterate through the hash map to find the element with a frequency greater than `n/2`.
- Step-by-step breakdown of the solution:
  1. Create a hash map `freq` to store the frequency of each element.
  2. Iterate through the array `nums` and update the frequency of each element in `freq`.
  3. Iterate through `freq` and return the key (element) with a value (frequency) greater than `n/2`.
- Why this approach comes to mind first: This approach is straightforward and easy to understand. It directly addresses the problem statement by counting the occurrences of each element.

```cpp
#include <iostream>
#include <unordered_map>
using namespace std;

int majorityElement(vector<int>& nums) {
    unordered_map<int, int> freq;
    int n = nums.size();
    
    // Count frequency of each element
    for (int num : nums) {
        freq[num]++;
    }
    
    // Find the element with frequency greater than n/2
    for (auto& pair : freq) {
        if (pair.second > n / 2) {
            return pair.first;
        }
    }
    
    // This should not happen as per the problem statement
    return -1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array. This is because we make two passes through the array: one to count frequencies and another to find the majority element.
> - **Space Complexity:** $O(n)$, as in the worst case, we might have to store every element in the hash map.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each element in the array. The space complexity is also linear because in the worst case, every element could be unique, requiring storage for each one.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The Boyer-Moore Voting Algorithm can be used to find the majority element in linear time and constant space. This algorithm works by essentially maintaining a counter for the majority element. It increments the counter when it sees the majority element and decrements it when it sees a different element. If the counter ever reaches zero, it sets the current element as the new majority element.
- Detailed breakdown of the approach:
  1. Initialize `count` to 0 and `candidate` to any value.
  2. Iterate through the array. For each element, if `count` is 0, set `candidate` to the current element and set `count` to 1. If the current element is equal to `candidate`, increment `count`. Otherwise, decrement `count`.
  3. After the iteration, `candidate` is the majority element. However, to ensure this is correct, we can perform a second pass through the array to confirm that `candidate` occurs more than `n/2` times.
- Proof of optimality: This approach is optimal because it achieves a time complexity of $O(n)$ and a space complexity of $O(1)$, which are the best possible complexities for this problem.

```cpp
int majorityElement(vector<int>& nums) {
    int count = 0;
    int candidate;
    
    // First pass: Find the candidate for majority element
    for (int num : nums) {
        if (count == 0) {
            candidate = num;
            count = 1;
        } else if (candidate == num) {
            count++;
        } else {
            count--;
        }
    }
    
    // Second pass: Confirm the majority element
    int confirmCount = 0;
    for (int num : nums) {
        if (num == candidate) {
            confirmCount++;
        }
    }
    
    // If confirmed, return the candidate
    if (confirmCount > nums.size() / 2) {
        return candidate;
    }
    
    // This should not happen as per the problem statement
    return -1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array. This is because we make two passes through the array.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the `count` and `candidate`.
> - **Optimality proof:** This is the optimal solution because we achieve the best possible time and space complexities for solving the problem. The Boyer-Moore Voting Algorithm is specifically designed for finding the majority element in an array, making it the most efficient approach for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The Boyer-Moore Voting Algorithm for finding the majority element.
- Problem-solving patterns identified: Using a counter to track the majority element and confirming the result with a second pass.
- Optimization techniques learned: Reducing space complexity from $O(n)$ to $O(1)$ by using a constant amount of space.
- Similar problems to practice: Finding the majority element in a stream of data, or finding the top-k elements in an array.

**Mistakes to Avoid:**
- Common implementation errors: Not confirming the majority element with a second pass, which could lead to incorrect results if the input array does not actually have a majority element.
- Edge cases to watch for: Empty input array, or an array with all unique elements (though the problem statement guarantees a majority element).
- Performance pitfalls: Using a hash map without considering the space complexity, or not optimizing the algorithm for the specific requirements of the problem.
- Testing considerations: Thoroughly testing the solution with various input arrays, including edge cases and large datasets.