def is_balanced_html(html):
    """Check if HTML tags are properly balanced."""
    stack = []
    i = 0
    while i < len(html):
        if html[i] == '<':
            j = html.find('>', i)
            if j == -1:
                return False  # Malformed tag

            tag = html[i+1:j]

            if tag.startswith('/'):
                if not stack or stack[-1] != tag[1:]:
                    return False  # Mismatched closing tag
                stack.pop()
            else:
                stack.append(tag)
            i = j + 1
        else:
            i += 1
    return len(stack) == 0


if __name__ == "__main__":
    print("Test Case 1:")
    html1 = "<div><p>Hello</p></div>"
    print("HTML:", html1)
    print("Is balanced:", is_balanced_html(html1))
    print()

    print("Test Case 2:")
    html2 = "<div><p>Hello</div></p>"
    print("HTML:", html2)
    print("Is balanced:", is_balanced_html(html2))
    print()

    print("Test Case 3:")
    html3 = "<html><body><h1>Title</h1></body></html>"
    print("HTML:", html3)
    print("Is balanced:", is_balanced_html(html3))
