## The K-th Lexicographical String of All Happy Strings of Length N

**Problem Link:** https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/description

**Problem Statement:**
- Input: An integer `n` representing the length of the strings, and an integer `k` representing the k-th lexicographical string to find.
- Constraints: `1 <= n <= 10`, `1 <= k <= 10^5`.
- Expected Output: The k-th lexicographical string of all happy strings of length `n`.
- Key Requirements: 
    - A happy string is a string that consists only of letters 'a', 'b', and 'c', where no two adjacent characters are the same.
    - The output string should be the k-th lexicographical string among all happy strings of length `n`.
- Example Test Cases:
    - Input: `n = 3`, `k = 3`
    - Output: `"abc"`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible happy strings of length `n` and sort them lexicographically to find the k-th string.
- Step-by-step breakdown of the solution:
    1. Generate all possible strings of length `n` using characters 'a', 'b', and 'c'.
    2. Check each string to see if it is a happy string by verifying that no two adjacent characters are the same.
    3. Store all happy strings in a list.
    4. Sort the list of happy strings lexicographically.
    5. Return the k-th string in the sorted list.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

void generateHappyStrings(string& current, int n, vector<string>& happyStrings) {
    if (current.size() == n) {
        happyStrings.push_back(current);
        return;
    }

    for (char c = 'a'; c <= 'c'; c++) {
        if (current.empty() || c != current.back()) {
            current.push_back(c);
            generateHappyStrings(current, n, happyStrings);
            current.pop_back();
        }
    }
}

string getHappyString(int n, int k) {
    vector<string> happyStrings;
    string current;
    generateHappyStrings(current, n, happyStrings);
    sort(happyStrings.begin(), happyStrings.end());
    return happyStrings[k - 1];
}

int main() {
    int n = 3;
    int k = 3;
    cout << getHappyString(n, k) << endl;  // Output: "abc"
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(3^n \cdot n \cdot log(3^n))$ due to generating all possible strings, sorting them, and checking for happy strings.
> - **Space Complexity:** $O(3^n)$ for storing all happy strings.
> - **Why these complexities occur:** The brute force approach generates all possible strings, checks each for the happy string condition, and sorts them, leading to high time and space complexities.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of generating all possible strings and then filtering happy strings, we can generate happy strings directly by ensuring that no two adjacent characters are the same.
- Detailed breakdown of the approach:
    1. Start with an empty string.
    2. For each position in the string, try appending 'a', 'b', and 'c' if the last character is not the same as the one being appended.
    3. Use a recursive function to generate all happy strings.
    4. Use a counter to keep track of the k-th happy string.

```cpp
#include <iostream>
#include <string>

using namespace std;

int count = 0;

void generateHappyStrings(string& current, int n, int k) {
    if (count == k) {
        cout << current << endl;
        return;
    }

    if (current.size() == n) {
        count++;
        if (count == k) {
            cout << current << endl;
        }
        return;
    }

    for (char c = 'a'; c <= 'c'; c++) {
        if (current.empty() || c != current.back()) {
            current.push_back(c);
            generateHappyStrings(current, n, k);
            current.pop_back();
        }
    }
}

string getHappyString(int n, int k) {
    string current;
    generateHappyStrings(current, n, k);
    // Note: The function will print the k-th happy string instead of returning it
    return "";
}

int main() {
    int n = 3;
    int k = 3;
    getHappyString(n, k);  // Output: "abc"
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(3^n)$ because in the worst case, we might generate all possible happy strings.
> - **Space Complexity:** $O(n)$ for the recursive call stack.
> - **Optimality proof:** This is the best possible complexity because we must at least generate the k-th happy string, which requires trying all combinations up to that point.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Recursive generation of strings, filtering based on conditions.
- Problem-solving patterns identified: Generating all possibilities and then filtering, versus generating only valid possibilities.
- Optimization techniques learned: Avoiding unnecessary work by generating only valid strings.
- Similar problems to practice: Generating permutations, combinations, and other constrained sequences.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to check for the base case in recursion, not handling the empty string case correctly.
- Edge cases to watch for: Handling the case when `n` is 1, or when `k` is larger than the total number of happy strings.
- Performance pitfalls: Generating all possible strings and then filtering, which leads to high time complexity.
- Testing considerations: Testing with small values of `n` and `k`, and verifying the output against manually generated happy strings.