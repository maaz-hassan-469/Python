def palindrome(a):
    temp=""
    for i in range(len(a)-1,-1,-1):
        temp=temp+a[i]
    if temp==a:
        return "it is a palindrome"
    return "it is not palindrome"
var=input("enter a word:")
print(palindrome(var))
        