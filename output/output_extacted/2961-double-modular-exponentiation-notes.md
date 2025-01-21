## Double Modular Exponentiation

**Problem Link:** https://leetcode.com/problems/double-modular-exponentiation/description

**Problem Statement:**
- The problem requires calculating the value of `(x^a) % n` and `(x^b) % n` for given values of `x`, `a`, `b`, and `n`.
- The goal is to find the values of these two modular exponentiations.
- Key requirements and edge cases to consider include handling large values of `x`, `a`, `b`, and `n`, as well as cases where `x` is 0 or 1.
- Example test cases include calculating `(2^3) % 5` and `(2^4) % 5`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves using the naive approach of calculating `x^a` and `x^b` directly and then taking the modulus `n`.
- However, this approach is inefficient due to the large values of `x`, `a`, and `b`.
- We can implement this approach using a simple loop to calculate the exponentiation.

```cpp
int doubleModularExponentiation(int x, int a, int b, int n) {
    int resultA = 1;
    for (int i = 0; i < a; i++) {
        resultA = (resultA * x) % n;
    }
    int resultB = 1;
    for (int i = 0; i < b; i++) {
        resultB = (resultB * x) % n;
    }
    return resultA * resultB;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(a + b)$, where $a$ and $b$ are the exponents. This is because we use two loops to calculate the exponentiations.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the results.
> - **Why these complexities occur:** The time complexity is high because we use a naive approach to calculate the exponentiations, resulting in a large number of multiplications. The space complexity is low because we only need to store a few variables.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to use the property of modular exponentiation that $(x^a) % n = ((x^{a/2}) % n)^2 % n$.
- This property allows us to reduce the number of multiplications required to calculate the exponentiation.
- We can implement this approach using a recursive function or a loop.
- Additionally, we can use the `pow` function in C++ to calculate the modular exponentiation.

```cpp
int doubleModularExponentiation(int x, int a, int b, int n) {
    long long resultA = 1;
    long long resultB = 1;
    for (int i = 0; i < a; i++) {
        resultA = (resultA * x) % n;
    }
    for (int i = 0; i < b; i++) {
        resultB = (resultB * x) % n;
    }
    return (resultA * resultB) % n;
}
```
Alternatively, we can also use the following approach which uses the property of modular exponentiation:
```cpp
int power(int x, int y, int p)  
{  
    int res = 1;   
    x = x % p; 
    while (y > 0)  
    {  
        if (y & 1)  
            res = (res * x) % p;  
        y = y >> 1; 
        x = (x * x) % p;  
    }  
    return res;  
}  
int doubleModularExponentiation(int x, int a, int b, int n) {
    return (power(x, a, n) * power(x, b, n)) % n;
}
```
> Complexity Analysis:
> - **Time Complexity:** $O(log(a) + log(b))$, where $a$ and $b$ are the exponents. This is because we use a loop to calculate the exponentiations, and the number of iterations is proportional to the logarithm of the exponents.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the results.
> - **Optimality proof:** The time complexity is optimal because we use the property of modular exponentiation to reduce the number of multiplications required. The space complexity is optimal because we only need to store a few variables.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated include modular exponentiation and the use of properties to reduce the number of multiplications required.
- Problem-solving patterns identified include the use of recursive functions or loops to calculate the exponentiations.
- Optimization techniques learned include the use of properties to reduce the number of multiplications required.
- Similar problems to practice include calculating the modular inverse of a number and finding the largest power of a prime that divides a number.

**Mistakes to Avoid:**
- Common implementation errors include using the naive approach to calculate the exponentiations, resulting in a large number of multiplications.
- Edge cases to watch for include handling large values of `x`, `a`, `b`, and `n`, as well as cases where `x` is 0 or 1.
- Performance pitfalls include using a large number of multiplications to calculate the exponentiations, resulting in a high time complexity.
- Testing considerations include testing the function with large values of `x`, `a`, `b`, and `n`, as well as testing the function with edge cases.