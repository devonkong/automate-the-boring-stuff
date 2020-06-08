## Chapter 7

1. `re.compile()` is a function that creates `Regex` objects.

2. Raw strings are used when creating `Regex` objects because the `\` character is used often.

3. The `search()` method returns a `Match` object equal to the *first* match of the `Regex` object in a given string.

4. To get the actual strings that match the pattern from a `Match` object, call the `.group()` method.

5. For `r"(\d\d\d)-(\d\d\d-\d\d\d\d)"`:  
`.group(0)` covers the entire matched string  
`.group(1)` covers the first three digit group or area code `(\d\d\d)`
`.group(2)` covers `(\d\d\d-\d\d\d\d)`

6. To specify that you want a regex to match actual parentheses and period characters, use the escape character `\` (eg. `\(\)\.`).

7. The `.findall()` method returns a list of strings if no groups are specified in the `Regex` object, and returns a list of tuples of strings if there are groups specified in the `Regex` object.

8. The `|` character signifies the *bitwise or* operator in regular expressions, meaning *either*.

9. In regular expressions, the `?` character signifies that the group preceeding it is present 0 or 1 times. It is also used to signify *non-greedy* matching.

10. In regular expressions, `+` means that the preceeding group appears 1 or more times, while `*` means 0 or more times.

11. In regular expressions, adding `{3}` after a group means that the group appears exactly 3 times. Adding `{3,5}` means that the group appears between 3 and 5 times, and can also be entered as `(3|4|5)`.

12. In regular expressions, the `\d` character class signifies any digit character, `\w` signifies any digit, letter or underscore character, and `\s` signifies a blank space, tab or newline character.

13. The `\D`, `\W`, and `\S` chracter classes signify any non-digit character, any character that is not a digit, letter or underscore character, and any character that is not a blank space, tab or newline character, respectively.

14. `.*` and `.*?` both match all characters except the newline character, but the former uses greedy matching while the latter uses non-greedy matching.

15. The character class syntax to match all numbers and lowerase letters is `[0-9a-z]`.

16. To make a regular expression case-insensitive, add `re.IGNORECASE` or `re.I` as a second argument when calling the `re.compile()` function.

17. The `.` character normally matches all characters except the newline character. When `re.DOTALL` is passed as the second argument to `re.compile()`, the `.` character matches all characters, including the newline character.

18. `num_regex = re.compile(r"\d+")`  
`num_regex.sub('X', '12 drummers, 11 pipers, five rings, 3 hens')` will return `'X drummers, X pipers, five rings, X hens'`.

19. Passing `re.VERBOSE` as the second argument to `re.compile()` allows the use of multi-line strings, whitespace and commenting.

20. A regex that will match `'42', '1,234', '6,368,745'` but not `'12,34,567', '1234'` is `re.compile(r"^\d{1,3}(,\d{3})*$")`.

21. A regex that will match `'Haruto Watanabe', 'Alice Watanabe', 'Robocop Watanabe'` but not `'haruto Watanabe', 'Mr. Watanabe', 'Watanabe', 'Haruto watanabe'` is `re.compile(r"[A-Z][a-z]+\sWatanabe")`.

22. A regex that will match `“Alice eats apples.', 'Bob pets cats.', 'Carol throws baseballs.', 'Alice throws Apples.', 'BOB EATS CATS.'` but not `'RoboCop eats apples.', 'ALICE THROWS FOOTBALLS.', 'Carol eats 7 cats.”` is `re.compile(r"(^(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.$, re.IGNORECASE")`.