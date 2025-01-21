## How Many Numbers Are Smaller Than the Current Number
**Problem Link:** https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/description

**Problem Statement:**
- Input: An array of integers `nums`.
- Constraints: The length of `nums` is between 2 and 500.
- Expected Output: An array where each element at index `i` represents the number of elements in `nums` that are smaller than `nums[i]`.
- Key Requirements: The solution should efficiently count the number of smaller elements for each element in the array.
- Example Test Cases:
  - Input: `nums = [8,1,2,2,3]`
    - Output: `[4,0,1,1,3]`
    - Explanation: For `nums[0] = 8`, there are 4 numbers smaller than 8. For `nums[1] = 1`, there are 0 numbers smaller than 1, and so on.

---

### Brute Force Approach
**Explanation:**
- The initial thought process involves comparing each element in the array with every other element to count the number of smaller elements.
- Step-by-step breakdown:
  1. Iterate through each element in the array.
  2. For each element, compare it with all other elements in the array.
  3. Count the number of elements that are smaller.
  4. Store the count for each element in a new array.

```cpp
vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
    vector<int> result;
    for (int i = 0; i < nums.size(); i++) {
        int count = 0;
        for (int j = 0; j < nums.size(); j++) {
            if (nums[j] < nums[i]) {
                count++;
            }
        }
        result.push_back(count);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of elements in the array. This is because for each element, we are potentially comparing it with every other element.
> - **Space Complexity:** $O(n)$, as we need to store the count of smaller numbers for each element in a new array.
> - **Why these complexities occur:** The nested loop structure leads to quadratic time complexity, and the need to store the results for each element leads to linear space complexity.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to use a frequency array to count the occurrences of each number and then calculate the cumulative sum of these counts to efficiently determine the number of smaller elements for each number.
- Step-by-step breakdown:
  1. Create a frequency array `freq` where `freq[i]` represents the number of occurrences of the number `i` in the input array.
  2. Calculate the cumulative sum of `freq` to get the count of numbers smaller than each number.
  3. For each number in the input array, use its value as an index into the cumulative sum array to find the count of smaller numbers.

```cpp
vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
    vector<int> result;
    vector<int> freq(101, 0); // Assuming numbers are in the range [0, 100]
    for (int num : nums) {
        freq[num]++;
    }
    for (int i = 1; i <= 100; i++) {
        freq[i] += freq[i-1];
    }
    for (int num : nums) {
        if (num == 0) {
            result.push_back(0);
        } else {
            result.push_back(freq[num-1]);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of elements in the input array and $m$ is the range of numbers (in this case, 101). This is because we make two passes: one to count frequencies and another to calculate the cumulative sum.
> - **Space Complexity:** $O(m)$, for storing the frequency and cumulative sum arrays.
> - **Optimality proof:** This approach is optimal because it reduces the comparison-based approach to a simple array lookup after preprocessing, leveraging the fact that the input range is bounded.

---

### Final Notes
**Learning Points:**
- Using frequency arrays and cumulative sums can significantly improve efficiency in problems involving counting and comparisons.
- Understanding the input constraints (e.g., bounded range of numbers) is crucial for optimizing solutions.

**Mistakes to Avoid:**
- Not considering the input constraints and thus failing to optimize the solution.
- Overlooking the possibility of using auxiliary arrays for frequency counting and cumulative sums.

**Similar Problems to Practice:**
- Counting elements in an array that satisfy certain conditions.
- Finding the rank of an element in a sorted array.
- Efficiently calculating statistics (e.g., mean, median) in arrays with specific properties.