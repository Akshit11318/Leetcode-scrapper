## Count Symmetric Integers

**Problem Link:** https://leetcode.com/problems/count-symmetric-integers/description

**Problem Statement:**
- Given an array of integers `nums` and an integer `k`, return the number of symmetric integers in the array.
- A symmetric integer is an integer `x` such that `x` and `k - x` both exist in the array.
- The input array `nums` contains distinct integers, and the integer `k` is within the range of the array.
- The expected output is the count of symmetric integers.
- Key requirements include handling edge cases where the array is empty or `k` is out of range.
- Example test cases include arrays with and without symmetric integers, as well as edge cases.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking every pair of integers in the array to see if they are symmetric.
- The step-by-step breakdown involves iterating over the array for each integer, and for each integer, checking if its symmetric counterpart exists in the array.
- This approach comes to mind first because it directly addresses the problem statement without requiring any additional insights.

```cpp
int countSymmetricIntegers(vector<int>& nums, int k) {
    int count = 0;
    for (int num : nums) {
        if (find(nums.begin(), nums.end(), k - num) != nums.end()) {
            count++;
        }
    }
    // Since we're counting each pair twice, we need to divide by 2
    return count / 2;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of integers in the array. This is because for each integer, we are potentially searching through the entire array.
> - **Space Complexity:** $O(1)$, since we are not using any additional space that scales with input size.
> - **Why these complexities occur:** The time complexity is quadratic because of the nested search operation, and the space complexity is constant because we only use a fixed amount of space to store the count.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to use a `set` data structure to store the integers in the array. This allows for constant time lookup of integers.
- The detailed breakdown involves creating a set from the array, then iterating over the array to check if the symmetric counterpart of each integer exists in the set.
- This approach is optimal because it reduces the time complexity of the lookup operation from linear to constant.

```cpp
int countSymmetricIntegers(vector<int>& nums, int k) {
    unordered_set<int> numSet(nums.begin(), nums.end());
    int count = 0;
    for (int num : nums) {
        if (numSet.find(k - num) != numSet.end() && num <= k - num) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of integers in the array. This is because creating the set and then iterating over the array both take linear time.
> - **Space Complexity:** $O(n)$, since we are storing all integers in the set.
> - **Optimality proof:** This is the best possible time complexity because we must at least read the input, and our approach does this in a single pass while also performing the necessary lookup operations in constant time.

---

### Final Notes

**Learning Points:**
- The key algorithmic concept demonstrated is the use of a `set` for efficient lookup operations.
- The problem-solving pattern identified is the reduction of time complexity by using appropriate data structures.
- The optimization technique learned is the importance of choosing the right data structure for the problem at hand.
- Similar problems to practice include those involving efficient lookup, insertion, and deletion operations.

**Mistakes to Avoid:**
- A common implementation error is not handling edge cases properly, such as an empty array or `k` being out of range.
- An edge case to watch for is when `k` is equal to twice an integer in the array, which would result in counting the same integer twice.
- A performance pitfall is using a linear search instead of a constant time lookup, leading to a quadratic time complexity.
- A testing consideration is to ensure that the solution works correctly for both positive and negative integers, as well as for integers of different magnitudes.