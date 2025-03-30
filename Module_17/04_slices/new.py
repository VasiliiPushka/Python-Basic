alphabet = 'abcdefg'

def cut(string:str):
    new_string = string[:]
    print(f"1. {new_string} - copy")
    print(f"2. {string[::-1]} - back")
    print(f"3. {string[::2]} - every second element")
    print(f"4. {string[1::2]} - Every second element of the line after the first")
    print(f"5. {string[:1:]} - All elements up to the second")
    print(f"6. {string[-1::]} - All elements starting from the end up to the second-to-last")
    print(f"7. {string[3:4]} - All elements in the index range from 3 to 4 (not including 4)")
    print(f"8. {string[-1-2:]} - The last three elements of the string")
    print(f"9. {string[3:5]} - All elements in the index range from 3 to 4")
    print(f"10. {string[-3:2:-1]} - The same as in the previous point, but in reverse order")

if __name__ == "__main__":
    cut(alphabet)

