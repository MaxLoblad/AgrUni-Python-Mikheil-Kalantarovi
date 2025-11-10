
keyboard_rows = ["qwertyuiop","asdfghjkl","zxcvbnm"]

while True:
    action = input("Enter action (e/d): ")
    if action == 'e':
        text = input("Enter text: ")
        result = ""
        for ch in text:
            if 'a' <= ch <= 'z':
                for row in keyboard_rows:
                    if ch in row:
                        i = row.index(ch)
                        result += row[(i + 1) % len(row)]
                        break
            else:
                result += ch
        print (result)
        break
    elif action == 'd':
        text = input("Enter text: ")
        result = ""
        for ch in text:
            if 'a' <= ch <= 'z':
                for row in keyboard_rows:
                    if ch in row:
                        i = row.index(ch)
                        result += row[(i - 1) % len(row)]
                        break
            else:
                result += ch
        print (result)
        break
    else:
        print("Invalid input!")
