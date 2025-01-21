## Missing Ranges
**Problem Link:** https://leetcode.com/problems/missing-ranges/description

**Problem Statement:**
- Input: `nums` (a sorted list of unique integers) and `lower` and `upper` bounds.
- Expected output: A list of strings representing the missing ranges in the form `"lower->upper"` or just `"lower"` if the range consists of a single number.
- Key requirements and edge cases:
  - Handle empty `nums` array.
  - Consider cases where `lower` and `upper` bounds are included or excluded from `nums`.
  - Ensure the output format matches the problem requirements.
- Example test cases:
  - `nums = [0, 1, 3, 50, 75]`, `lower = 0`, `upper = 99`
  - `nums = []`, `lower = 1`, `upper = 10`
  - `nums = [1, 2, 3, 4, 5]`, `lower = 1`, `upper = 5`

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves iterating through all numbers from `lower` to `upper` and checking if each number is present in `nums`.
- For each missing number, construct the corresponding range string.

```cpp
vector<string> findMissingRanges(vector<int>& nums, int lower, int upper) {
    vector<string> result;
    for (int i = lower; i <= upper; i++) {
        bool found = false;
        for (int num : nums) {
            if (num == i) {
                found = true;
                break;
            }
        }
        if (!found) {
            result.push_back(to_string(i));
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the range from `lower` to `upper` and $m$ is the size of `nums`, because for each number in the range, we potentially scan through all elements of `nums`.
> - **Space Complexity:** $O(n)$, because in the worst case, if all numbers in the range are missing from `nums`, we store each one in the result.
> - **Why these complexities occur:** The brute force approach is inefficient because it involves nested loops, leading to high time complexity. The space complexity is linear due to the potential storage of every number in the range.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal approach involves iterating through `nums` and considering the gaps between numbers, as well as the gaps before the first number and after the last number in `nums`.
- For each gap, construct the corresponding range string and add it to the result.

```cpp
vector<string> findMissingRanges(vector<int>& nums, int lower, int upper) {
    vector<string> result;
    if (nums.empty()) {
        result.push_back(getRange(lower, upper));
        return result;
    }
    
    // Check the gap before the first number
    if (nums[0] > lower) {
        result.push_back(getRange(lower, nums[0] - 1));
    }
    
    // Check gaps between numbers
    for (int i = 0; i < nums.size() - 1; i++) {
        if (nums[i + 1] - nums[i] > 1) {
            result.push_back(getRange(nums[i] + 1, nums[i + 1] - 1));
        }
    }
    
    // Check the gap after the last number
    if (nums.back() < upper) {
        result.push_back(getRange(nums.back() + 1, upper));
    }
    
    return result;
}

string getRange(int lower, int upper) {
    if (lower == upper) {
        return to_string(lower);
    } else {
        return to_string(lower) + "->" + to_string(upper);
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the size of `nums` and $m$ is the number of missing ranges, because we make a single pass through `nums` and potentially add each missing range to the result.
> - **Space Complexity:** $O(m)$, because we store each missing range in the result.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through `nums` and directly constructs the missing ranges without unnecessary comparisons, minimizing both time and space complexity.