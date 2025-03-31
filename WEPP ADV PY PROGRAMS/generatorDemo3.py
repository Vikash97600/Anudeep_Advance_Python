words=["FIRST","topic","IN","the","PYTHON","generator"]
upperCase=(w.upper() for w in words)
for w in upperCase:
    print(w)

lowerCase=(w.lower() for w in words)
for w in lowerCase:
    print(w)