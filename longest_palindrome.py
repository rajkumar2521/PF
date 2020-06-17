def palindromes(text):
    text = text.lower()

    for i in range(len(text)):
        for j in range(0, i):
            chunk = text[j:i + 1]

            if chunk == chunk[::-1]:
                results=''.join(chunk)

    return  results

print(palindromes('babad'))    
    