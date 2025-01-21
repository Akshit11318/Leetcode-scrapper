## Find Lucky Integer in an Array

**Problem Link:** https://leetcode.com/problems/find-lucky-integer-in-an-array/description

**Problem Statement:**
- Given an array of integers `arr`, a lucky integer is an integer which is equal to its index in the array (1-indexed).
- The task is to find a lucky integer in the array. If there are multiple lucky integers, return the largest one. If there is no lucky integer, return -1.

**Input Format and Constraints:**
- The input array `arr` will have a length between 1 and 10^5.
- The elements of the array will be integers between 1 and 10^5.

**Expected Output Format:**
- The function should return a single integer, which is the largest lucky integer in the array, or -1 if no lucky integer exists.

**Key Requirements and Edge Cases to Consider:**
- The array may contain duplicate elements.
- The array may not contain any lucky integers.
- The function should handle edge cases where the array is empty or contains only one element.

**Example Test Cases with Explanations:**
- For the input `arr = [2,2,3,4]`, the output should be `2`, because `2` is the largest lucky integer in the array.
- For the input `arr = [1,2,2,3,3,3]`, the output should be `3`, because `3` is the largest lucky integer in the array.
- For the input `arr = [2,3,4,5,6]`, the output should be `-1`, because there are no lucky integers in the array.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to iterate through the array and check each element to see if it is equal to its index (1-indexed).
- If an element is equal to its index, it is a lucky integer and should be stored as the current largest lucky integer.
- After iterating through the entire array, the function should return the largest lucky integer found, or -1 if no lucky integers were found.

```cpp
int findLucky(vector<int>& arr) {
    int maxLucky = -1;
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] == i + 1) {
            maxLucky = max(maxLucky, arr[i]);
        }
    }
    return maxLucky;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array, because the function iterates through the array once.
> - **Space Complexity:** $O(1)$, because the function uses a constant amount of space to store the maximum lucky integer.
> - **Why these complexities occur:** The time complexity is linear because the function checks each element in the array once. The space complexity is constant because the function only uses a fixed amount of space to store the maximum lucky integer.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal approach is the same as the brute force approach, because the problem requires checking each element in the array to find the largest lucky integer.
- The key insight is that the array only needs to be iterated through once, and the maximum lucky integer can be updated as the function iterates through the array.

```cpp
int findLucky(vector<int>& arr) {
    int maxLucky = -1;
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] == i + 1) {
            maxLucky = max(maxLucky, arr[i]);
        }
    }
    return maxLucky;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array, because the function iterates through the array once.
> - **Space Complexity:** $O(1)$, because the function uses a constant amount of space to store the maximum lucky integer.
> - **Optimality proof:** This is the optimal solution because the problem requires checking each element in the array to find the largest lucky integer. Any solution that does not check each element will not be able to find the largest lucky integer.

---

### Final Notes

**Learning Points:**
- The key algorithmic concept demonstrated is iterating through an array to find a specific condition.
- The problem-solving pattern identified is checking each element in the array to find the maximum value that meets a certain condition.
- The optimization technique learned is that sometimes the brute force approach is the optimal solution, especially when the problem requires checking each element in the array.

**Mistakes to Avoid:**
- A common implementation error is to forget to initialize the maximum lucky integer to -1.
- An edge case to watch for is when the array is empty, in which case the function should return -1.
- A performance pitfall is to use a nested loop to check each element in the array, which would result in a time complexity of $O(n^2)$.