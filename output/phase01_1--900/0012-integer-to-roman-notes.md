## Integer to Roman
**Problem Link:** [https://leetcode.com/problems/integer-to-roman/description](https://leetcode.com/problems/integer-to-roman/description)

**Problem Statement:**
- Input: An integer `num` between 1 and 3999.
- Output: The Roman numeral representation of `num` as a string.
- Key requirements: The solution should handle all integers within the specified range and produce the correct Roman numeral representation.
- Example test cases:
  - Input: `num = 3`, Output: `"III"`
  - Input: `num = 4`, Output: `"IV"`
  - Input: `num = 9`, Output: `"IX"`
  - Input: `num = 58`, Output: `"LVIII"`
  - Input: `num = 1994`, Output: `"MCMXCIV"`

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to create a mapping of all possible integers to their Roman numeral representations and then look up the input number in this mapping.
- This approach involves creating a large lookup table or a complex series of if-else statements to cover all cases.
- However, this method is impractical due to the large number of possible integers and the complexity of handling all edge cases.

```cpp
#include <iostream>
#include <string>

std::string intToRoman(int num) {
    std::string result = "";
    while (num > 0) {
        if (num >= 1000) {
            result += "M";
            num -= 1000;
        } else if (num >= 900) {
            result += "CM";
            num -= 900;
        } else if (num >= 500) {
            result += "D";
            num -= 500;
        } else if (num >= 400) {
            result += "CD";
            num -= 400;
        } else if (num >= 100) {
            result += "C";
            num -= 100;
        } else if (num >= 90) {
            result += "XC";
            num -= 90;
        } else if (num >= 50) {
            result += "L";
            num -= 50;
        } else if (num >= 40) {
            result += "XL";
            num -= 40;
        } else if (num >= 10) {
            result += "X";
            num -= 10;
        } else if (num >= 9) {
            result += "IX";
            num -= 9;
        } else if (num >= 5) {
            result += "V";
            num -= 5;
        } else if (num >= 4) {
            result += "IV";
            num -= 4;
        } else {
            result += "I";
            num -= 1;
        }
    }
    return result;
}

int main() {
    std::cout << intToRoman(3) << std::endl;  // III
    std::cout << intToRoman(4) << std::endl;  // IV
    std::cout << intToRoman(9) << std::endl;  // IX
    std::cout << intToRoman(58) << std::endl;  // LVIII
    std::cout << intToRoman(1994) << std::endl;  // MCMXCIV
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the input number, because in the worst case, we might need to subtract 1 from the number $n$ times.
> - **Space Complexity:** $O(n)$, as the length of the output string can be up to $n$ in the worst case (though practically, it's much less due to the nature of Roman numerals).
> - **Why these complexities occur:** The brute force approach involves a simple iterative process that builds the Roman numeral string by subtracting the largest possible Roman numeral values from the input number until it reaches 0.

---

### Optimal Approach (Required)
**Explanation:**
- The optimal approach involves using a more systematic method to map integers to Roman numerals.
- We can define a list of Roman numeral values and their corresponding integer values in descending order.
- Then, we iterate through this list, subtracting the largest possible Roman numeral value from the input number and appending the corresponding Roman numeral to the result string, until the number becomes 0.
- This method is more efficient and easier to implement than the brute force approach.

```cpp
#include <iostream>
#include <string>

std::string intToRoman(int num) {
    int values[] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    std::string romanLiterals[] = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
    std::string result = "";
    for (int i = 0; i < 13; i++) {
        while (num >= values[i]) {
            result += romanLiterals[i];
            num -= values[i];
        }
    }
    return result;
}

int main() {
    std::cout << intToRoman(3) << std::endl;  // III
    std::cout << intToRoman(4) << std::endl;  // IV
    std::cout << intToRoman(9) << std::endl;  // IX
    std::cout << intToRoman(58) << std::endl;  // LVIII
    std::cout << intToRoman(1994) << std::endl;  // MCMXCIV
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, because we are iterating through a fixed list of Roman numeral values (13 values), regardless of the input size.
> - **Space Complexity:** $O(1)$, as the space used does not grow with the size of the input, but is determined by the size of the output string, which has a maximum length but does not grow indefinitely with the input size.
> - **Optimality proof:** This approach is optimal because it uses a fixed number of operations to convert any integer to a Roman numeral, making it more efficient than the brute force approach for large inputs.

---

### Final Notes

**Learning Points:**
- The importance of understanding the problem domain (in this case, Roman numerals) to devise an efficient solution.
- Using a systematic approach to solve problems can lead to more efficient and scalable solutions.
- The difference between brute force and optimal solutions in terms of time and space complexity.

**Mistakes to Avoid:**
- Overcomplicating the solution by not understanding the problem domain well.
- Not considering the constraints of the problem (e.g., the range of input integers).
- Failing to optimize the solution for better performance.