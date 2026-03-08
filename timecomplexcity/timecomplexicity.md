# Time Complexity Patterns for Beginners

## 1. Single Loop

```
for i in range(n):
```

Time Complexity: **O(n)**
Reason: The loop runs **n times**.

---

## 2. Two Nested Loops

```
for i in range(n):
    for j in range(n):
```

Time Complexity: **O(n²)**
Reason: Outer loop runs **n times**, inner loop runs **n times**.
Total operations = **n × n = n²**

---

## 3. Triangular Nested Loop

```
for i in range(n):
    for j in range(i):
```

Time Complexity: **O(n²)**
Reason: Total operations ≈ **n(n+1)/2**

---

## 4. Doubling Loop

```
i = 1
while i < n:
    i *= 2
```

Time Complexity: **O(log n)**
Because the value doubles each step.

---

## 5. Halving Loop

```
i = n
while i > 0:
    i //= 2
```

Time Complexity: **O(log n)**
Because the value is divided by 2 each step.

---

## 6. Half Loop

```
for i in range(n//2):
```

Time Complexity: **O(n)**
Constants are ignored in Big-O notation.

---

## 7. Two Separate Loops

```
for i in range(n):
for i in range(n):
```

Time Complexity: **O(n + n) = O(n)**

---

## 8. Recursion

```
T(n) = T(n-1) + O(1)
```

Time Complexity: **O(n)**

---

## 9. Divide and Conquer

```
T(n) = 2T(n/2) + O(n)
```

Example: **Merge Sort**

Time Complexity: **O(n log n)**

---

## 10. Fibonacci Recursion

```
T(n) = T(n-1) + T(n-2)
```

Time Complexity: **O(2ⁿ)**

---

## Summary

| Pattern             | Time Complexity |
| ------------------- | --------------- |
| Single Loop         | O(n)            |
| Nested Loops        | O(n²)           |
| Doubling / Halving  | O(log n)        |
| Two Loops           | O(n)            |
| Divide & Conquer    | O(n log n)      |
| Fibonacci Recursion | O(2ⁿ)           |

Understanding these patterns helps you quickly estimate the efficiency of algorithms.
