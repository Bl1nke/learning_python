def is_palindrome(text:str) -> bool:
    text = text.replace(" ", "")
    text = text.lower()
    if text == text[::-1]:
        return True
    else:
        return False
    


is_palindrome("Я ем змея")