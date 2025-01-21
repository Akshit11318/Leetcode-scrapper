## Add to Array-Form of Integer
**Problem Link:** https://leetcode.com/problems/add-to-array-form-of-integer/description

**Problem Statement:**
- Input: A non-negative integer `k` and a non-negative integer array `num` representing the array-form of an integer.
- Constraints: `1 <= num.length <= 10^4`, `0 <= num[i] <= 9`, `num.length >= 1`, `0 <= k <= 10^4`, and the array-form of the integer `num` does not have leading zeros (except for the number 0 itself).
- Expected Output: The array-form of the integer resulting from adding `k` to `num`.
- Key Requirements: Handle edge cases such as overflow, leading zeros, and ensure the output is in array-form.

**Example Test Cases:**
- For `num = [1,2,0,0]` and `k = 34`, the output should be `[1,2,3,4]`.
- For `num = [0]` and `k = 0`, the output should be `[0]`.
- For `num = [9,9,9,9,9,9,9,9,9,9]` and `k = 1`, the output should be `[1,0,0,0,0,0,0,0,0,0,0]`.

---

### Brute Force Approach
**Explanation:**
- Convert the array `num` to a single integer by iterating through the array and multiplying each digit by the appropriate power of 10, then summing these values.
- Add the integer `k` to the sum.
- Convert the resulting sum back into an array-form integer by repeatedly taking the last digit (using modulo 10) and then removing it (using integer division by 10), until the sum is 0.
- Store each digit in an array and return it.

```cpp
vector<int> addToArrayForm(vector<int>& num, int k) {
    int sum = 0;
    // Convert array to integer
    for (int i = 0; i < num.size(); i++) {
        sum += num[i] * pow(10, num.size() - i - 1);
    }
    // Add k to the sum
    sum += k;
    vector<int> result;
    // Convert sum back to array
    while (sum > 0) {
        result.push_back(sum % 10);
        sum /= 10;
    }
    // Handle case where sum is 0
    if (result.empty()) {
        result.push_back(0);
    }
    // Reverse the result since we appended in reverse order
    reverse(result.begin(), result.end());
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + log(k + sum))$ where $n$ is the size of `num` and $log(k + sum)$ accounts for converting the sum back into an array, assuming $sum$ is the sum of `num` and `k`.
> - **Space Complexity:** $O(n + log(k + sum))$ for storing the result.
> - **Why these complexities occur:** The initial conversion from array to integer and the addition are linear and constant time, respectively. The conversion of the sum back to an array depends on the number of digits in the sum, which is logarithmic in the value of the sum.

---

### Optimal Approach (Required)
**Explanation:**
- Instead of converting the entire array to an integer and then back, iterate through the array from right to left (least significant digit to most), adding `k` to each digit and handling carry-over.
- This approach avoids the need for explicit conversion to and from integers, reducing the computational complexity.
- Start with an initial carry of `k`, and for each digit in `num` from right to left, calculate the new carry and the digit to be placed in the result array.

```cpp
vector<int> addToArrayForm(vector<int>& num, int k) {
    vector<int> result;
    int carry = k;
    for (int i = num.size() - 1; i >= 0; i--) {
        int sum = num[i] + carry;
        result.push_back(sum % 10);
        carry = sum / 10;
    }
    while (carry > 0) {
        result.push_back(carry % 10);
        carry /= 10;
    }
    // Reverse the result since we appended in reverse order
    reverse(result.begin(), result.end());
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + log(k))$ where $n$ is the size of `num`, because we process each digit in `num` once and potentially add up to $log(k)$ additional digits from `k`.
> - **Space Complexity:** $O(n + log(k))$ for storing the result.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through `num` and handles the addition of `k` without needing to convert the entire array to an integer, thus minimizing both time and space complexity.

---

### Final Notes

**Learning Points:**
- Handling carry-over in arithmetic operations.
- Avoiding unnecessary conversions between data types.
- Iterating through arrays from right to left for certain operations.

**Mistakes to Avoid:**
- Not considering edge cases like when the sum of `num` and `k` results in an array longer than `num`.
- Failing to handle carry-over correctly.
- Using inefficient data type conversions.