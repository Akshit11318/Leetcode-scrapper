## Find All Lonely Numbers in the Array
**Problem Link:** https://leetcode.com/problems/find-all-lonely-numbers-in-the-array/description

**Problem Statement:**
- Input: An integer array `nums`.
- Output: A list of integers representing all lonely numbers in `nums`. A lonely number is a number that appears only once in the array and its adjacent numbers (i.e., `x-1` and `x+1`) do not exist in the array.
- Key requirements: Identify all lonely numbers in the given array.
- Edge cases: Empty array, array with a single element, array with all elements being the same.

### Brute Force Approach
**Explanation:**
- The initial thought process is to iterate through each number in the array and check if it's a lonely number.
- Step-by-step breakdown:
  1. Iterate through each number `x` in the array.
  2. For each `x`, count the occurrences of `x-1`, `x`, and `x+1` in the array.
  3. If `x` appears only once and both `x-1` and `x+1` do not exist in the array, add `x` to the result list.

```cpp
vector<int> findLonelyNumbers(vector<int>& nums) {
    vector<int> result;
    for (int x : nums) {
        int count_x = 0, count_x_minus_1 = 0, count_x_plus_1 = 0;
        for (int num : nums) {
            if (num == x) count_x++;
            if (num == x - 1) count_x_minus_1++;
            if (num == x + 1) count_x_plus_1++;
        }
        if (count_x == 1 && count_x_minus_1 == 0 && count_x_plus_1 == 0) {
            result.push_back(x);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of elements in the array. This is because for each number in the array, we're potentially iterating through the entire array again to count occurrences.
> - **Space Complexity:** $O(n)$, for storing the result list.
> - **Why these complexities occur:** The brute force approach involves nested iterations over the array, leading to quadratic time complexity. The space complexity is linear because in the worst case, we might store every number in the result list.

### Optimal Approach (Required)
**Explanation:**
- Key insight: We can improve the brute force approach by using a hash map to store the count of each number in the array. This allows us to check the counts of `x`, `x-1`, and `x+1` in constant time.
- Detailed breakdown:
  1. Create a hash map `count_map` to store the count of each number in the array.
  2. Iterate through the array to populate `count_map`.
  3. Iterate through the array again. For each number `x`, check if it's a lonely number by looking up the counts of `x`, `x-1`, and `x+1` in `count_map`.
  4. If `x` is a lonely number, add it to the result list.

```cpp
vector<int> findLonelyNumbers(vector<int>& nums) {
    unordered_map<int, int> count_map;
    for (int num : nums) {
        count_map[num]++;
    }
    vector<int> result;
    for (int x : nums) {
        if (count_map[x] == 1 && count_map.find(x - 1) == count_map.end() && count_map.find(x + 1) == count_map.end()) {
            result.push_back(x);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array. This is because we're iterating through the array twice: once to populate the count map and once to find lonely numbers.
> - **Space Complexity:** $O(n)$, for storing the count map and the result list.
> - **Optimality proof:** This approach is optimal because it reduces the time complexity to linear by using a hash map to store and look up counts in constant time, and it minimizes the number of iterations over the array.

### Final Notes
**Learning Points:**
- Using hash maps to store and look up data in constant time can significantly improve the efficiency of algorithms.
- The optimal approach often involves a trade-off between time and space complexity.
- Identifying lonely numbers in an array can be solved efficiently by leveraging data structures like hash maps.

**Mistakes to Avoid:**
- Not considering the use of hash maps or other data structures to improve algorithm efficiency.
- Failing to check for edge cases, such as an empty array or an array with a single element.
- Not optimizing the algorithm for both time and space complexity.