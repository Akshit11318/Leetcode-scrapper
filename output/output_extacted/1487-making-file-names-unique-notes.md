## Making File Names Unique

**Problem Link:** https://leetcode.com/problems/making-file-names-unique/description

**Problem Statement:**
- Input format: A list of file names as strings.
- Constraints: The length of the list is between 1 and 10^5.
- Expected output format: A list of unique file names.
- Key requirements: Each file name must be unique.
- Edge cases to consider: File names that are the same but for case, file names that are the same but for a number at the end.

**Example Test Cases:**
- Input: `["kitty","kitty","kitty"]`
- Output: `["kitty","kitty(1)","kitty(2)"]`
- Explanation: The first "kitty" remains unchanged, the second "kitty" becomes "kitty(1)", and the third "kitty" becomes "kitty(2)".

### Brute Force Approach

**Explanation:**
- Initial thought process: Use a dictionary to keep track of the count of each file name.
- Step-by-step breakdown of the solution:
  1. Initialize an empty dictionary to store the count of each file name.
  2. Iterate through the list of file names.
  3. For each file name, check if it is already in the dictionary.
  4. If it is, append the count to the file name and increment the count.
  5. If it is not, add it to the dictionary with a count of 0.

```cpp
vector<string> getFolderNames(vector<string>& names) {
    unordered_map<string, int> count;
    vector<string> result;
    for (string name : names) {
        if (count.find(name) == count.end()) {
            count[name] = 0;
            result.push_back(name);
        } else {
            int num = count[name];
            string newName = name + "(" + to_string(num) + ")";
            while (count.find(newName) != count.end()) {
                num++;
                newName = name + "(" + to_string(num) + ")";
            }
            count[name] = num + 1;
            count[newName] = 0;
            result.push_back(newName);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the number of file names and $m$ is the maximum length of a file name.
> - **Space Complexity:** $O(n \cdot m)$ for storing the count of each file name and the result.
> - **Why these complexities occur:** The time complexity occurs because we are iterating through the list of file names and for each file name, we are checking if it is already in the dictionary and updating the count if necessary. The space complexity occurs because we are storing the count of each file name and the result.

### Optimal Approach (Required)

**Explanation:**
- Key insight: Use a dictionary to keep track of the count of each file name and update the count only when a duplicate is found.
- Detailed breakdown of the approach:
  1. Initialize an empty dictionary to store the count of each file name.
  2. Iterate through the list of file names.
  3. For each file name, check if it is already in the dictionary.
  4. If it is, append the count to the file name and increment the count.
  5. If it is not, add it to the dictionary with a count of 0.
- Proof of optimality: This approach is optimal because it only updates the count when a duplicate is found, reducing the number of iterations.

```cpp
vector<string> getFolderNames(vector<string>& names) {
    unordered_map<string, int> count;
    vector<string> result;
    for (string name : names) {
        if (count.find(name) == count.end()) {
            count[name] = 0;
            result.push_back(name);
        } else {
            int num = count[name];
            string newName = name + "(" + to_string(num) + ")";
            while (count.find(newName) != count.end()) {
                num++;
                newName = name + "(" + to_string(num) + ")";
            }
            count[newName] = 0;
            count[name] = num + 1;
            result.push_back(newName);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the number of file names and $m$ is the maximum length of a file name.
> - **Space Complexity:** $O(n \cdot m)$ for storing the count of each file name and the result.
> - **Optimality proof:** This approach is optimal because it only updates the count when a duplicate is found, reducing the number of iterations.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a dictionary to keep track of the count of each file name, updating the count only when a duplicate is found.
- Problem-solving patterns identified: Checking for duplicates and updating the count accordingly.
- Optimization techniques learned: Reducing the number of iterations by only updating the count when a duplicate is found.
- Similar problems to practice: Problems that involve keeping track of counts and updating them accordingly.

**Mistakes to Avoid:**
- Common implementation errors: Not updating the count correctly, not checking for duplicates correctly.
- Edge cases to watch for: File names that are the same but for case, file names that are the same but for a number at the end.
- Performance pitfalls: Not using a dictionary to keep track of the count of each file name, not updating the count only when a duplicate is found.
- Testing considerations: Testing for duplicates, testing for edge cases.