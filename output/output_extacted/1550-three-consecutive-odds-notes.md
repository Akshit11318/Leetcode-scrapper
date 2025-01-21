## Three Consecutive Odds

**Problem Link:** https://leetcode.com/problems/three-consecutive-odds/description

**Problem Statement:**
- Input format and constraints: Given an array of integers `arr`, determine if any sequence of three consecutive elements in the array is comprised entirely of odd integers.
- Expected output format: Return `true` if such a sequence exists, `false` otherwise.
- Key requirements and edge cases to consider: The sequence must be of exactly three consecutive elements, and all must be odd integers.
- Example test cases with explanations:
  - For `arr = [2,6,4,1]`, the output is `false` because there is no sequence of three consecutive odd integers.
  - For `arr = [1,2,34,3,4,5,7,23,12]`, the output is `true` because there is a sequence `3, 5, 7` which are all odd integers.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The simplest way to solve this problem is to iterate through the array and check every sequence of three consecutive elements to see if they are all odd.
- Step-by-step breakdown of the solution:
  1. Iterate through the array, considering each element as the start of a potential sequence of three consecutive elements.
  2. For each starting element, check if it and the next two elements are all odd integers.
  3. If a sequence of three consecutive odd integers is found, immediately return `true`.
  4. If the iteration completes without finding such a sequence, return `false`.
- Why this approach comes to mind first: It is straightforward and directly addresses the problem statement without requiring any complex algorithms or data structures.

```cpp
bool threeConsecutiveOdds(vector<int>& arr) {
    // Check if the array has at least three elements
    if (arr.size() < 3) {
        return false;
    }
    
    // Iterate through the array
    for (int i = 0; i < arr.size() - 2; i++) {
        // Check if the current element and the next two are all odd
        if (arr[i] % 2 != 0 && arr[i + 1] % 2 != 0 && arr[i + 2] % 2 != 0) {
            return true;
        }
    }
    
    // If no sequence of three consecutive odds is found, return false
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array, because we potentially iterate through the entire array once.
> - **Space Complexity:** $O(1)$, because we use a constant amount of space to store the loop counter and do not allocate any additional space that scales with input size.
> - **Why these complexities occur:** The time complexity is linear because we check every sequence of three consecutive elements in the worst case. The space complexity is constant because we do not use any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The brute force approach is already optimal for this problem because it must check every sequence of three consecutive elements to determine if any are all odd. This is a linear scan through the array, which is the most efficient way to solve this problem given its constraints.
- Detailed breakdown of the approach: The same as the brute force approach, as it is already optimal.
- Proof of optimality: Any algorithm must at least read the input, which for this problem means iterating through the array. Since the brute force approach does exactly this and does so in a way that directly solves the problem, it is optimal.
- Why further optimization is impossible: Further optimization is not possible because the brute force approach already has the minimum time complexity required to solve the problem, which is $O(n)$.

```cpp
bool threeConsecutiveOdds(vector<int>& arr) {
    // Check if the array has at least three elements
    if (arr.size() < 3) {
        return false;
    }
    
    // Iterate through the array
    for (int i = 0; i < arr.size() - 2; i++) {
        // Check if the current element and the next two are all odd
        if (arr[i] % 2 != 0 && arr[i + 1] % 2 != 0 && arr[i + 2] % 2 != 0) {
            return true;
        }
    }
    
    // If no sequence of three consecutive odds is found, return false
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array.
> - **Space Complexity:** $O(1)$, because we use a constant amount of space.
> - **Optimality proof:** The algorithm is optimal because it must check every sequence of three consecutive elements, and it does so in a single pass through the array, resulting in a linear time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Linear scanning, checking for properties in sequences of elements.
- Problem-solving patterns identified: Sometimes, the most straightforward approach is also the most efficient.
- Optimization techniques learned: Recognizing when an algorithm is already optimal based on the problem's constraints.
- Similar problems to practice: Other problems involving scanning arrays or sequences for specific properties.

**Mistakes to Avoid:**
- Common implementation errors: Off-by-one errors when iterating through arrays, especially when checking sequences of elements.
- Edge cases to watch for: Arrays with fewer than three elements, which should immediately return `false`.
- Performance pitfalls: Unnecessary iterations or checks that do not contribute to solving the problem.
- Testing considerations: Ensure to test with arrays of varying sizes, including edge cases like empty arrays or arrays with only one or two elements.