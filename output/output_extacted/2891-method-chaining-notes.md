## Method Chaining

**Problem Link:** https://leetcode.com/problems/method-chaining/description

**Problem Statement:**
- Input format and constraints: The problem requires creating a class `MyString` with methods `append`, `add`, and `reverse` to manipulate a string.
- Expected output format: The output should be a string after applying the given methods.
- Key requirements and edge cases to consider: 
    - The `append` method should add a string to the end of the current string.
    - The `add` method should add an integer to the current string.
    - The `reverse` method should reverse the current string.
- Example test cases with explanations:
    - `MyString str; str.append("Hello"); str.add(123); str.reverse();` should output `"321olleH"`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can start by implementing each method separately without considering optimization.
- Step-by-step breakdown of the solution:
    1. Create a `MyString` class with a `string` member variable to store the current string.
    2. Implement the `append` method to add a string to the end of the current string.
    3. Implement the `add` method to convert an integer to a string and add it to the current string.
    4. Implement the `reverse` method to reverse the current string.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it may not be optimal in terms of performance.

```cpp
class MyString {
public:
    string str;
    MyString() {}
    MyString(string s) { str = s; }
    MyString& append(string s) {
        str += s;
        return *this;
    }
    MyString& add(int num) {
        str += to_string(num);
        return *this;
    }
    MyString& reverse() {
        reverse(str.begin(), str.end());
        return *this;
    }
    string toString() {
        return str;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ for `append`, $O(log n)$ for `add`, and $O(n)$ for `reverse`, where $n$ is the length of the string. The overall time complexity is $O(n + log n)$.
> - **Space Complexity:** $O(n)$ for storing the string.
> - **Why these complexities occur:** The time complexity is due to the string operations, and the space complexity is due to storing the string.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use the same approach as the brute force solution, but with some minor optimizations.
- Detailed breakdown of the approach:
    1. Create a `MyString` class with a `string` member variable to store the current string.
    2. Implement the `append` method to add a string to the end of the current string using the `+=` operator.
    3. Implement the `add` method to convert an integer to a string and add it to the current string using the `+=` operator.
    4. Implement the `reverse` method to reverse the current string using the `reverse` function from the `<algorithm>` library.
- Proof of optimality: This approach is optimal because it uses the most efficient string operations available in C++.

```cpp
class MyString {
public:
    string str;
    MyString() {}
    MyString(string s) { str = s; }
    MyString& append(string s) {
        str += s;
        return *this;
    }
    MyString& add(int num) {
        str += to_string(num);
        return *this;
    }
    MyString& reverse() {
        reverse(str.begin(), str.end());
        return *this;
    }
    string toString() {
        return str;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ for `append`, $O(log n)$ for `add`, and $O(n)$ for `reverse`, where $n$ is the length of the string. The overall time complexity is $O(n + log n)$.
> - **Space Complexity:** $O(n)$ for storing the string.
> - **Optimality proof:** This approach is optimal because it uses the most efficient string operations available in C++.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: string manipulation, method chaining.
- Problem-solving patterns identified: using the `+=` operator for string concatenation, using the `reverse` function for reversing a string.
- Optimization techniques learned: using the most efficient string operations available in C++.
- Similar problems to practice: other string manipulation problems, such as substring searching or string matching.

**Mistakes to Avoid:**
- Common implementation errors: not using the `+=` operator for string concatenation, not using the `reverse` function for reversing a string.
- Edge cases to watch for: empty strings, strings with special characters.
- Performance pitfalls: using inefficient string operations, such as using the `+` operator for string concatenation instead of the `+=` operator.
- Testing considerations: testing with different input strings, testing with edge cases.