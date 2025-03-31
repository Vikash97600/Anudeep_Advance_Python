# 1)You have a list of strings, and you want to extract all digits from these strings and
# combine them into a single list.
# strings = [
# "abc123",
# "hello456world",
# "789",
# "test"
# ]
'''
strings = [
"abc123",
"hello456world",
"789",
"test"
]

digits = []
for string in strings:
    for char in string:
        if char.isdigit():
            digits.append(int(char))
print(digits)

'''

# 3. You have a list of URLs, and you need to filter out only those that start with 'https'.
# urls = [
# "http://example.com",
# "https://secure-site.com",
# "ftp://files.example.org",
# "https://another-secure-site.com"
# ]

urls = [
"http://example.com",
"https://secure-site.com",
"ftp://files.example.org",
"https://another-secure-site.com"
]

httpsUrls = [url for url in urls if url.startswith("https")]
print(httpsUrls)