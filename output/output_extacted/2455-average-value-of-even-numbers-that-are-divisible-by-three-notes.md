## Average Value of Even Numbers That Are Divisible by Three
**Problem Link:** https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/description

**Problem Statement:**
- Input: An array of integers `nums`.
- Output: The average value of even numbers in the array that are divisible by 3.
- Key requirements: 
  - Only consider even numbers that are also divisible by 3.
  - If no such numbers exist, return 0.
- Example test cases: 
  - Input: `nums = [1,2,3,4,5,6]`
    - Output: `4.0`
    - Explanation: The even numbers in the array that are divisible by 3 are 6, so the average is 6 / 1 = 6.0.
  - Input: `nums = [1,2,3,4,5,6,7,8,9,10]`
    - Output: `8.0`
    - Explanation: The even numbers in the array that are divisible by 3 are 6 and 12 is not in the array, but 6 is, and also 12 is not in the array but 6 is, so the average is (6) / 1 = 6.0.

---

### Brute Force Approach

**Explanation:**
- Iterate through the array and check each number to see if it's even and divisible by 3.
- If a number meets these conditions, add it to a sum and increment a counter for the total count of such numbers.
- After iterating through the entire array, calculate the average by dividing the sum by the count.
- If the count is 0 (meaning no numbers met the conditions), return 0.

```cpp
double averageOfEvenNumbers(vector<int>& nums) {
    double sum = 0.0;
    int count = 0;
    for (int num : nums) {
        if (num % 2 == 0 && num % 3 == 0) {
            sum += num;
            count++;
        }
    }
    if (count == 0) return 0;
    return sum / count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the input array. This is because we potentially check each element once.
> - **Space Complexity:** $O(1)$, since we only use a constant amount of space to store the sum and count, regardless of the input size.
> - **Why these complexities occur:** The time complexity is linear because we iterate through the array once, and the space complexity is constant because we use a fixed amount of space that does not grow with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- The brute force approach is already optimal for this problem since we must check each number in the array at least once to determine if it meets the conditions.
- Therefore, the same approach as the brute force is used for the optimal solution.

```cpp
double averageOfEvenNumbers(vector<int>& nums) {
    double sum = 0.0;
    int count = 0;
    for (int num : nums) {
        if (num % 2 == 0 && num % 3 == 0) {
            sum += num;
            count++;
        }
    }
    if (count == 0) return 0;
    return sum / count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the input array.
> - **Space Complexity:** $O(1)$, since we only use a constant amount of space.
> - **Optimality proof:** This solution is optimal because it checks each element exactly once, which is necessary to solve the problem, and uses a constant amount of extra space.

---

### Final Notes

**Learning Points:**
- The importance of checking each element in the array when the problem requires considering each element's properties.
- How to calculate averages by summing relevant values and dividing by the count of those values.
- Understanding that sometimes, the brute force approach is already optimal, especially for problems requiring a linear scan of the input.

**Mistakes to Avoid:**
- Forgetting to check for the case where no numbers meet the conditions, which would result in a division by zero error.
- Not using clear variable names, which can make the code harder to understand.
- Failing to validate inputs, though in this case, the input is assumed to be a valid array of integers.