def palindrome(word):
    result=''
    for i in reversed(word):
        result+=i
    return 'palindrome' if word==result else 'non-palindrome'

print(palindrome('baab'))