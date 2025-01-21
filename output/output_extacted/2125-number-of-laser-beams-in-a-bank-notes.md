## Number of Laser Beams in a Bank
**Problem Link:** https://leetcode.com/problems/number-of-laser-beams-in-a-bank/description

**Problem Statement:**
- Input format: A list of strings `bank` representing the bank's layout, where each string is a row and each character is either '0' (empty space) or '1' (security device).
- Constraints: `1 <= bank.length <= 500`, `1 <= bank[i].length <= 500`, `bank[i][j]` is either '0' or '1'.
- Expected output format: The number of laser beams in the bank.
- Key requirements and edge cases to consider:
  - Each security device can be part of at most one laser beam.
  - A laser beam is defined as a sequence of security devices in the same row or column, with no other security devices in between.
- Example test cases with explanations:
  - `["00000000","11111111","00000000","11111111","00000000","11111111","00000000","11111111"]` returns `8`, because there are 8 laser beams in the bank, each consisting of 8 security devices in the same row or column.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Iterate over each character in the bank's layout, and for each security device, check all possible directions (up, down, left, right) to see if there are any other security devices that can form a laser beam.
- Step-by-step breakdown of the solution:
  1. Iterate over each character in the bank's layout.
  2. For each security device, check all possible directions to see if there are any other security devices.
  3. If a security device is found in a direction, increment the count of laser beams and continue checking in that direction until no more security devices are found.
- Why this approach comes to mind first: It's a straightforward approach that checks all possible directions for each security device, but it's inefficient because it has a high time complexity.

```cpp
int numberOfBeams(vector<string>& bank) {
    int count = 0;
    for (int i = 0; i < bank.size(); i++) {
        for (int j = 0; j < bank[i].size(); j++) {
            if (bank[i][j] == '1') {
                // Check up direction
                for (int k = i - 1; k >= 0; k--) {
                    if (bank[k][j] == '1') {
                        count++;
                        break;
                    }
                }
                // Check down direction
                for (int k = i + 1; k < bank.size(); k++) {
                    if (bank[k][j] == '1') {
                        count++;
                        break;
                    }
                }
                // Check left direction
                for (int k = j - 1; k >= 0; k--) {
                    if (bank[i][k] == '1') {
                        count++;
                        break;
                    }
                }
                // Check right direction
                for (int k = j + 1; k < bank[i].size(); k++) {
                    if (bank[i][k] == '1') {
                        count++;
                        break;
                    }
                }
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot (n + m))$, where $n$ is the number of rows and $m$ is the number of columns, because for each security device, we're checking all possible directions.
> - **Space Complexity:** $O(1)$, because we're only using a constant amount of space to store the count of laser beams.
> - **Why these complexities occur:** The time complexity is high because we're checking all possible directions for each security device, and the space complexity is low because we're only using a constant amount of space.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: Instead of checking all possible directions for each security device, we can iterate over each row and column and count the number of security devices in each row and column. Then, we can calculate the number of laser beams by multiplying the counts of security devices in each row and column.
- Detailed breakdown of the approach:
  1. Iterate over each row and count the number of security devices in each row.
  2. Iterate over each column and count the number of security devices in each column.
  3. Calculate the number of laser beams by multiplying the counts of security devices in each row and column.
- Proof of optimality: This approach is optimal because it has a lower time complexity than the brute force approach and it's guaranteed to find all laser beams.

```cpp
int numberOfBeams(vector<string>& bank) {
    int count = 0;
    vector<int> rowCounts(bank.size(), 0);
    vector<int> colCounts(bank[0].size(), 0);
    
    // Count security devices in each row
    for (int i = 0; i < bank.size(); i++) {
        for (int j = 0; j < bank[i].size(); j++) {
            if (bank[i][j] == '1') {
                rowCounts[i]++;
            }
        }
    }
    
    // Count security devices in each column
    for (int j = 0; j < bank[0].size(); j++) {
        for (int i = 0; i < bank.size(); i++) {
            if (bank[i][j] == '1') {
                colCounts[j]++;
            }
        }
    }
    
    // Calculate number of laser beams
    for (int i = 0; i < bank.size(); i++) {
        for (int j = 0; j < bank[i].size(); j++) {
            if (bank[i][j] == '1') {
                count += (rowCounts[i] - 1) + (colCounts[j] - 1);
            }
        }
    }
    
    return count / 2;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of rows and $m$ is the number of columns, because we're iterating over each row and column once.
> - **Space Complexity:** $O(n + m)$, because we're using space to store the counts of security devices in each row and column.
> - **Optimality proof:** This approach is optimal because it has a lower time complexity than the brute force approach and it's guaranteed to find all laser beams.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, counting, and multiplication.
- Problem-solving patterns identified: Counting security devices in each row and column, and calculating the number of laser beams by multiplying the counts.
- Optimization techniques learned: Reducing time complexity by iterating over each row and column once, and using space to store counts of security devices.
- Similar problems to practice: Problems that involve counting and multiplication, such as counting the number of islands in a grid or calculating the number of ways to reach a target sum.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing variables, not checking for edge cases, and not using space efficiently.
- Edge cases to watch for: Empty input, input with no security devices, and input with only one security device.
- Performance pitfalls: Using a brute force approach with high time complexity, and not using space efficiently.
- Testing considerations: Testing with different input sizes, testing with different numbers of security devices, and testing with edge cases.