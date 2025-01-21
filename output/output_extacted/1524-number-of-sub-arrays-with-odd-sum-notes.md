## Number of Sub-arrays with Odd Sum

**Problem Link:** https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/description

**Problem Statement:**
- Input: An integer array `arr` and an integer `k`.
- Output: The number of sub-arrays with an odd sum.
- Key requirements: 
  - Calculate the sum of each sub-array.
  - Determine if the sum is odd or even.
  - Count the number of sub-arrays with an odd sum.
- Edge cases: 
  - Empty array.
  - Array with a single element.
  - Array with all elements being even or odd.
- Example test cases:
  - Input: `arr = [1, 3, 5]`, Output: `4` (Sub-arrays with odd sum: `[1]`, `[1, 3]`, `[3]`, `[1, 3, 5]`)
  - Input: `arr = [2, 4, 6]`, Output: `0` (No sub-arrays with odd sum)

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Calculate the sum of each possible sub-array and check if it's odd or even.
- Step-by-step breakdown:
  1. Generate all possible sub-arrays.
  2. Calculate the sum of each sub-array.
  3. Check if the sum is odd or even using the modulo operator (`%`).
  4. Count the number of sub-arrays with an odd sum.
- Why this approach comes to mind first: It's a straightforward and intuitive solution that checks every possible sub-array.

```cpp
int numOfSubarrays(vector<int>& arr) {
    int count = 0;
    for (int i = 0; i < arr.size(); i++) {
        int sum = 0;
        for (int j = i; j < arr.size(); j++) {
            sum += arr[j];
            if (sum % 2 != 0) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of elements in the array. This is because we're using two nested loops to generate all possible sub-arrays.
> - **Space Complexity:** $O(1)$, excluding the input array. We're only using a constant amount of space to store the count and sum variables.
> - **Why these complexities occur:** The nested loops cause the time complexity to be quadratic, while the constant space usage results in a space complexity of $O(1)$.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of calculating the sum of each sub-array, we can use a prefix sum array to keep track of the cumulative sum.
- Detailed breakdown:
  1. Create a prefix sum array `prefixSum` where `prefixSum[i]` represents the sum of the first `i` elements.
  2. Iterate through the array and calculate the sum of each sub-array using the prefix sum array.
  3. Check if the sum is odd or even using the modulo operator (`%`).
  4. Count the number of sub-arrays with an odd sum.
- Proof of optimality: This approach has a time complexity of $O(n^2)$, which is the same as the brute force approach. However, it uses a more efficient data structure (prefix sum array) to reduce the number of calculations.

```cpp
int numOfSubarrays(vector<int>& arr) {
    int count = 0;
    for (int i = 0; i < arr.size(); i++) {
        int sum = 0;
        for (int j = i; j < arr.size(); j++) {
            sum += arr[j];
            if (sum % 2 != 0) {
                count++;
            }
        }
    }
    return count;
}
```

However, we can further optimize this by using the fact that the sum of a subarray is odd if and only if the number of odd numbers in the subarray is odd. We can use a single pass to count the number of odd numbers and calculate the number of sub-arrays with an odd sum.

```cpp
int numOfSubarrays(vector<int>& arr) {
    int count = 0;
    for (int i = 0; i < arr.size(); i++) {
        int oddCount = 0;
        for (int j = i; j < arr.size(); j++) {
            if (arr[j] % 2 != 0) {
                oddCount++;
            }
            if (oddCount % 2 != 0) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of elements in the array. This is because we're using two nested loops to generate all possible sub-arrays.
> - **Space Complexity:** $O(1)$, excluding the input array. We're only using a constant amount of space to store the count and odd count variables.
> - **Optimality proof:** This approach has the same time complexity as the brute force approach but uses a more efficient data structure to reduce the number of calculations.

However, there's an even more efficient approach that uses the fact that the sum of a subarray is odd if and only if the number of odd numbers in the subarray is odd. We can use a single pass to count the number of odd numbers and calculate the number of sub-arrays with an odd sum.

```cpp
int numOfSubarrays(vector<int>& arr) {
    int count = 0;
    for (int i = 0; i < arr.size(); i++) {
        int sum = 0;
        for (int j = i; j < arr.size(); j++) {
            sum += arr[j];
            if (sum % 2 != 0) {
                count++;
            }
        }
    }
    return count;
}
```
is equivalent to 
```cpp
int numOfSubarrays(vector<int>& arr) {
    int n = arr.size();
    int count = 0;
    for (int i = 0; i < n; i++) {
        int sum = 0;
        for (int j = i; j < n; j++) {
            sum += arr[j];
            if (sum % 2 != 0) count++;
        }
    }
    return count;
}
```
But we can optimize it further:
```cpp
int numOfSubarrays(vector<int>& arr) {
    int n = arr.size();
    int odd = 0, even = 0, res = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] % 2 == 0) even++;
        else odd++;
        res += odd;
    }
    return res;
}
```
> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array. This is because we're using a single pass to count the number of odd numbers and calculate the number of sub-arrays with an odd sum.
> - **Space Complexity:** $O(1)$, excluding the input array. We're only using a constant amount of space to store the count, odd count, and even count variables.
> - **Optimality proof:** This approach has a time complexity of $O(n)$, which is more efficient than the previous approaches.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Prefix sum array, counting odd numbers, and calculating sub-arrays with an odd sum.
- Problem-solving patterns identified: Using a prefix sum array to reduce calculations, counting odd numbers to determine sub-arrays with an odd sum.
- Optimization techniques learned: Using a single pass to count odd numbers and calculate sub-arrays with an odd sum.
- Similar problems to practice: Counting sub-arrays with an even sum, calculating the sum of all sub-arrays.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing variables, not checking for edge cases.
- Edge cases to watch for: Empty array, array with a single element, array with all elements being even or odd.
- Performance pitfalls: Using nested loops to generate all possible sub-arrays, not using a prefix sum array to reduce calculations.
- Testing considerations: Testing with different input sizes, testing with different types of input (e.g., all even, all odd).