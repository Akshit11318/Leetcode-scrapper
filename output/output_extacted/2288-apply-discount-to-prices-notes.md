## Apply Discount to Prices
**Problem Link:** https://leetcode.com/problems/apply-discount-to-prices/description

**Problem Statement:**
- Input format and constraints: The input is a string `sentence` and a decimal number `discount`. The `sentence` contains prices in the format `$X.XX` where `X` is a digit, and the `discount` is a decimal number representing the percentage discount to be applied.
- Expected output format: The output should be the `sentence` with all prices discounted by the given percentage.
- Key requirements and edge cases to consider: 
  - Prices in the sentence should be updated to reflect the discount.
  - Non-price parts of the sentence should remain unchanged.
  - The discount should be applied correctly, considering rounding if necessary.
- Example test cases with explanations:
  - Input: `sentence = "there are $1.00 dollars and 100% discount"`, `discount = 100`
    - Output: `"there are $0.00 dollars and 100% discount"`
  - Input: `sentence = "1 2 $3.00 4 $5.00 6 7 8$9.00$3$"`, `discount = 100`
    - Output: `"1 2 $0.00 4 $0.00 6 7 8$0.00$0$"`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first step is to identify all prices in the sentence and then apply the discount to each price.
- Step-by-step breakdown of the solution:
  1. Iterate through the sentence to find all substrings that match the price format `$X.XX`.
  2. For each price found, apply the discount by multiplying the price by `(100 - discount) / 100`.
  3. Replace the original price in the sentence with the discounted price.
- Why this approach comes to mind first: It's a straightforward method that directly addresses the problem by finding and modifying all prices in the sentence.

```cpp
#include <iostream>
#include <string>
#include <regex>

std::string applyDiscount(const std::string& sentence, double discount) {
    std::string result = sentence;
    std::regex priceRegex("\\$\\d+\\.\\d+");
    auto words_begin = std::sregex_iterator(result.begin(), result.end(), priceRegex);
    auto words_end = std::sregex_iterator();

    for (std::sregex_iterator i = words_begin; i != words_end; ++i) {
        std::smatch match = *i;
        std::string price = match.str();
        // Remove the dollar sign
        double priceValue = std::stod(price.substr(1));
        double discountedPrice = priceValue * ((100 - discount) / 100);
        // Format the discounted price to two decimal places
        char buffer[10];
        sprintf(buffer, "$%.2f", discountedPrice);
        std::string discountedPriceStr(buffer);
        // Replace the original price with the discounted price
        size_t pos = result.find(price);
        while (pos != std::string::npos) {
            result.replace(pos, price.length(), discountedPriceStr);
            pos = result.find(price, pos + discountedPriceStr.length());
        }
    }

    return result;
}

int main() {
    std::string sentence = "there are $1.00 dollars and 100% discount";
    double discount = 100.0;
    std::cout << applyDiscount(sentence, discount) << std::endl;
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the length of the sentence and $m$ is the number of prices in the sentence. The reason is that for each price found, we potentially iterate through the sentence again to replace it.
> - **Space Complexity:** $O(n)$ for storing the result and temporary strings. 
> - **Why these complexities occur:** The brute force approach involves finding all prices in the sentence and then replacing them, which leads to these complexities due to the nested operations of finding and replacing.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of replacing each price individually, which could lead to inefficiencies if there are many prices, we can iterate through the sentence once, applying the discount to each price as we find it.
- Detailed breakdown of the approach:
  1. Initialize an empty string `result` to build the output sentence.
  2. Iterate through the input `sentence` character by character.
  3. When a price is encountered (indicated by the `$` symbol), extract the price value, apply the discount, and append the discounted price to `result`.
  4. If the character is not part of a price, simply append it to `result`.
- Proof of optimality: This approach is optimal because it only requires a single pass through the sentence, minimizing both time and space complexity.

```cpp
#include <iostream>
#include <string>

std::string applyDiscount(const std::string& sentence, double discount) {
    std::string result;
    bool inPrice = false;
    std::string price;
    for (char c : sentence) {
        if (c == '$') {
            inPrice = true;
            price += c;
        } else if (inPrice && (c >= '0' && c <= '9' || c == '.')) {
            price += c;
        } else if (inPrice) {
            // Apply discount to the price
            double priceValue = std::stod(price.substr(1));
            double discountedPrice = priceValue * ((100 - discount) / 100);
            char buffer[10];
            sprintf(buffer, "$%.2f", discountedPrice);
            result += buffer;
            inPrice = false;
            result += c;
        } else {
            result += c;
        }
    }
    // Handle the case where the sentence ends with a price
    if (inPrice) {
        double priceValue = std::stod(price.substr(1));
        double discountedPrice = priceValue * ((100 - discount) / 100);
        char buffer[10];
        sprintf(buffer, "$%.2f", discountedPrice);
        result += buffer;
    }
    return result;
}

int main() {
    std::string sentence = "there are $1.00 dollars and 100% discount";
    double discount = 100.0;
    std::cout << applyDiscount(sentence, discount) << std::endl;
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the length of the sentence. This is because we make a single pass through the sentence.
> - **Space Complexity:** $O(n)$ for storing the result string.
> - **Optimality proof:** This approach is optimal because it minimizes the number of operations required to apply the discount to all prices in the sentence, achieving linear time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, string manipulation, and basic arithmetic operations.
- Problem-solving patterns identified: The importance of a single pass through the data to achieve optimal time complexity.
- Optimization techniques learned: Minimizing the number of passes through the data and avoiding unnecessary operations.
- Similar problems to practice: Other string manipulation and optimization problems.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling edge cases, such as prices at the end of the sentence or non-price dollar signs.
- Edge cases to watch for: Prices with varying numbers of decimal places, negative prices, and non-numeric characters within prices.
- Performance pitfalls: Using inefficient algorithms or data structures that lead to high time or space complexity.
- Testing considerations: Thoroughly testing the function with a variety of inputs, including edge cases, to ensure correctness and robustness.