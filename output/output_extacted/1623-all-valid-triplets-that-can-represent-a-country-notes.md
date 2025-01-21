## All Valid Triplets That Can Represent a Country

**Problem Link:** https://leetcode.com/problems/all-valid-triplets-that-can-represent-a-country/description

**Problem Statement:**
- Input format and constraints: The input will be a list of codes representing countries, where each code is a three-letter string. The constraints are that the input list will contain at least one code and at most $10^4$ codes. Each code is unique and consists of uppercase English letters only.
- Expected output format: The output should be a list of all valid triplets that can represent a country. A valid triplet is a three-letter string where the first letter is not '0', and the first and second letters are not the same, and the second and third letters are not the same.
- Key requirements and edge cases to consider: The input list can contain duplicate codes, and the codes can be in any order. The output should not contain any duplicate triplets.
- Example test cases with explanations:
  - Input: `["ABC", "DEF", "GHI"]`
  - Output: `["ABC", "DEF", "GHI"]`
  - Explanation: All three codes are valid triplets because they meet the conditions of not having '0' as the first letter and not having consecutive letters that are the same.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to iterate through each code in the input list and check if it meets the conditions of a valid triplet. This involves checking the first letter to ensure it's not '0', and then checking each pair of consecutive letters to ensure they are not the same.
- Step-by-step breakdown of the solution:
  1. Initialize an empty list to store valid triplets.
  2. Iterate through each code in the input list.
  3. For each code, check the first letter to ensure it's not '0'.
  4. Check the first and second letters to ensure they are not the same.
  5. Check the second and third letters to ensure they are not the same.
  6. If all conditions are met, add the code to the list of valid triplets.
- Why this approach comes to mind first: This approach is straightforward and directly addresses the conditions given in the problem statement.

```cpp
#include <iostream>
#include <vector>
#include <string>

std::vector<std::string> validTriplets(std::vector<std::string>& codes) {
    std::vector<std::string> validTriplets;
    for (const auto& code : codes) {
        if (code[0] != '0' && code[0] != code[1] && code[1] != code[2]) {
            validTriplets.push_back(code);
        }
    }
    return validTriplets;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of codes in the input list. This is because we are iterating through each code once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of valid triplets. This is because in the worst-case scenario, all codes could be valid triplets, and we need to store them.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each code in the input list. The space complexity is also linear because we store each valid triplet in the output list.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The problem doesn't require any additional optimization beyond the brute force approach because we must check each code at least once to determine if it's a valid triplet. The conditions for a valid triplet are simple and can be checked in constant time per code.
- Detailed breakdown of the approach: The optimal approach is the same as the brute force approach because it already has a linear time complexity, which is the best we can achieve given the need to examine each code.
- Proof of optimality: This approach is optimal because it checks each code exactly once, which is necessary to determine if it's a valid triplet. Any algorithm must at least read the input, resulting in a time complexity of at least $O(n)$.
- Why further optimization is impossible: Further optimization is impossible because the problem requires examining each code at least once. The current approach does this in linear time, which is the best possible time complexity for this problem.

```cpp
#include <iostream>
#include <vector>
#include <string>

std::vector<std::string> validTriplets(std::vector<std::string>& codes) {
    std::vector<std::string> validTriplets;
    for (const auto& code : codes) {
        if (code[0] != '0' && code[0] != code[1] && code[1] != code[2]) {
            validTriplets.push_back(code);
        }
    }
    return validTriplets;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of codes in the input list.
> - **Space Complexity:** $O(n)$, where $n$ is the number of valid triplets.
> - **Optimality proof:** The time complexity is optimal because we must check each code at least once. The space complexity is also optimal because we only store valid triplets.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, conditional checks, and list manipulation.
- Problem-solving patterns identified: Directly addressing the problem statement's conditions.
- Optimization techniques learned: Recognizing when a brute force approach is already optimal due to the inherent need to examine all input data.
- Similar problems to practice: Problems that involve filtering or validating data based on specific conditions.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as an empty input list.
- Edge cases to watch for: Handling codes with less than three characters, or codes with non-uppercase letters.
- Performance pitfalls: Unnecessary iterations or checks that could increase the time complexity beyond linear.
- Testing considerations: Ensuring to test with a variety of inputs, including edge cases and large datasets.