## Sort the Jumbled Numbers

**Problem Link:** https://leetcode.com/problems/sort-the-jumbled-numbers/description

**Problem Statement:**
- Input format and constraints: Given a list of integers `mapping` and a list of integers `nums`, where `mapping[i]` is a one-to-one mapping from digit `i` to another digit, and `nums` is a list of integers. 
- Expected output format: Return a list of integers `ans`, where `ans[i]` is the integer `nums[i]` after applying the mapping `mapping`.
- Key requirements and edge cases to consider: The input lists will contain at least one element, and all integers in `nums` will be non-negative and less than 10^4.
- Example test cases with explanations: For example, given `mapping = [8,9,4,0,2,1,3,5,7,6]` and `nums = [991]`, the output will be `[123]`, because `9` maps to `8`, `9` maps to `9`, and `1` maps to `1`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The most straightforward way to solve this problem is to iterate over each number in `nums`, and for each digit in the number, apply the mapping to get the new digit.
- Step-by-step breakdown of the solution:
  1. Convert each number to a string to easily access each digit.
  2. For each digit in the string, find its corresponding mapped value in `mapping`.
  3. Append the mapped digit to a new string.
  4. Convert the new string back to an integer and add it to the result list.
- Why this approach comes to mind first: This approach is intuitive because it directly applies the given mapping to each digit in each number.

```cpp
vector<int> sortJumbledNumbers(vector<int>& mapping, vector<int>& nums) {
    vector<int> result;
    for (int num : nums) {
        string str = to_string(num);
        string newStr = "";
        for (char c : str) {
            int digit = c - '0';
            newStr += to_string(mapping[digit]);
        }
        result.push_back(stoi(newStr));
    }
    sort(result.begin(), result.end());
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot log(m) + n \cdot log(n))$, where $n$ is the number of numbers in `nums` and $m$ is the maximum number of digits in a number. This is because for each number, we iterate over its digits and then sort the result list.
> - **Space Complexity:** $O(n \cdot m)$, because we create a new string for each number.
> - **Why these complexities occur:** The time complexity is dominated by the sorting operation and the string manipulation for each number, while the space complexity is due to the storage of the result list and the temporary strings.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of applying the mapping to each number and then sorting, we can apply the mapping to each number and store the original and mapped numbers in a pair, then sort these pairs based on the mapped numbers.
- Detailed breakdown of the approach:
  1. Create a vector of pairs, where each pair contains a number from `nums` and its mapped version.
  2. Sort this vector of pairs based on the mapped numbers.
  3. Extract the original numbers from the sorted pairs and return them.
- Proof of optimality: This approach is optimal because it minimizes the number of operations required to sort the numbers after applying the mapping, by leveraging the built-in sorting functionality.

```cpp
vector<int> sortJumbledNumbers(vector<int>& mapping, vector<int>& nums) {
    vector<pair<int, int>> pairs;
    for (int num : nums) {
        string str = to_string(num);
        string newStr = "";
        for (char c : str) {
            int digit = c - '0';
            newStr += to_string(mapping[digit]);
        }
        pairs.emplace_back(num, stoi(newStr));
    }
    sort(pairs.begin(), pairs.end(), [](const pair<int, int>& a, const pair<int, int>& b) {
        return a.second < b.second;
    });
    vector<int> result;
    for (auto& pair : pairs) {
        result.push_back(pair.first);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m + n \cdot log(n))$, where $n$ is the number of numbers in `nums` and $m$ is the maximum number of digits in a number. This is because we iterate over each digit in each number and then sort the pairs.
> - **Space Complexity:** $O(n)$, because we store the pairs of original and mapped numbers.
> - **Optimality proof:** This approach is optimal because it applies the mapping to each number exactly once and sorts the resulting numbers in a single operation, minimizing both time and space complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting, string manipulation, and the use of pairs to store related data.
- Problem-solving patterns identified: Applying transformations to data before sorting, and using pairs to associate original and transformed data.
- Optimization techniques learned: Minimizing the number of operations by leveraging built-in sorting functionality.
- Similar problems to practice: Other problems involving data transformation and sorting, such as sorting based on custom criteria or applying multiple transformations.

**Mistakes to Avoid:**
- Common implementation errors: Failing to handle edge cases, such as empty input lists or numbers with varying numbers of digits.
- Edge cases to watch for: Handling numbers with leading zeros after applying the mapping.
- Performance pitfalls: Using inefficient sorting algorithms or failing to minimize the number of operations required to apply the mapping and sort the numbers.
- Testing considerations: Thoroughly testing the function with a variety of input cases, including edge cases and large inputs.