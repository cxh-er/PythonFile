def is_palindrome(n):
    return str(n)==str(n)[::-1]

output = filter(is_palindrome, range(1, 1000))
L=list(output)
print(L)
print(L[1])
