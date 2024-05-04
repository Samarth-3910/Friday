url = input("Enter the URL: ")

if not url.startswith("http://") and not url.startswith("https://"):
    print("invalidURL")
    url = input("Enter the URL: ")

display_text = input("Enter the display text: ")

#markdown_link = "[" + display_text + "](" + url + ")"
markdown_link = url

print(markdown_link)
