## Count Beautiful Splits in an Array

**Problem Link:** https://leetcode.com/problems/count-beautiful-splits-in-an-array/description

**Problem Statement:**
- Input: An array of integers `nums`.
- Output: The number of beautiful splits in the array.
- Key requirements: A beautiful split is a pair of indices `(i, j)` where `0 <= i < j < nums.length`, `nums[i]` is a factor of `nums[j]`, and `nums[j]` is a factor of `nums[i]`.
- Edge cases: The array can be empty, or `nums.length` can be 1.

**Example Test Cases:**

* Input: `nums = [10, 2, 5, 20]`
Output: `3`
Explanation: There are three beautiful splits: `(0, 1)`, `(2, 3)`, and `(0, 3)`.
* Input: `nums = [1, 2, 3, 4]`
Output: `0`
Explanation: There are no beautiful splits.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to check every pair of elements in the array to see if they form a beautiful split.
- We need to iterate over the array and for each element, check all the elements that come after it.

```cpp
int countBeautifulSplits(vector<int>& nums) {
    int count = 0;
    for (int i = 0; i < nums.size(); i++) {
        for (int j = i + 1; j < nums.size(); j++) {
            if (nums[i] != 0 && nums[j] % nums[i] == 0 && nums[i] % nums[j] == 0) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the array. This is because we are using two nested loops to check every pair of elements.
> - **Space Complexity:** $O(1)$, as we are not using any extra space that scales with the input size.
> - **Why these complexities occur:** The time complexity is quadratic because we are checking every pair of elements in the array, and the space complexity is constant because we are only using a fixed amount of space to store the count of beautiful splits.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is that a beautiful split can only occur between two numbers that are equal.
- This is because if `nums[i]` is a factor of `nums[j]` and `nums[j]` is a factor of `nums[i]`, then `nums[i]` and `nums[j]` must be equal.
- Therefore, we can simply count the number of pairs of equal elements in the array.

```cpp
int countBeautifulSplits(vector<int>& nums) {
    int count = 0;
    for (int i = 0; i < nums.size(); i++) {
        for (int j = i + 1; j < nums.size(); j++) {
            if (nums[i] == nums[j]) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the array. This is because we are still using two nested loops to check every pair of elements.
> - **Space Complexity:** $O(1)$, as we are not using any extra space that scales with the input size.
> - **Optimality proof:** This is the optimal solution because we are only checking pairs of elements that could potentially be beautiful splits, and we are doing so in a way that minimizes the number of comparisons.

---

### Final Notes

**Learning Points:**
- The key algorithmic concept demonstrated in this problem is the importance of understanding the properties of the problem and using them to simplify the solution.
- The problem-solving pattern identified is to look for ways to reduce the number of comparisons needed to solve the problem.
- The optimization technique learned is to use the properties of the problem to eliminate unnecessary comparisons.

**Mistakes to Avoid:**
- A common implementation error is to forget to check for the case where the array is empty or has only one element.
- An edge case to watch for is when the array contains duplicate elements.
- A performance pitfall is to use a solution that has a time complexity greater than $O(n^2)$, as this can lead to slow performance for large inputs.
- A testing consideration is to make sure to test the solution with a variety of inputs, including edge cases and large inputs.