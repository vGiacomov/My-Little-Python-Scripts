import os


def generate_lorem_ipsum(length):
    lorem_ipsum = (
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
        "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
        "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris "
        "nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in "
        "reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla "
        "pariatur. Excepteur sint occaecat cupidatat non proident, sunt in "
        "culpa qui officia deserunt mollit anim id est laborum."
    )
    result = []
    current_length = 0
    while current_length < length:
        remaining_length = length - current_length
        if remaining_length >= len(lorem_ipsum):
            result.append(lorem_ipsum)
            current_length += len(lorem_ipsum)
        else:
            result.append(lorem_ipsum[:remaining_length])
            current_length += remaining_length

    return ''.join(result)


def main():
    print("Lorem ipsum Generator \n ")
    try:
        length = int(input("Please enter the number of characters: "))
        if length <= 0:
            print("The length must be greater than 0")
            return

        filename = input("Enter the file name (e.g. 'notepad.txt'): ").strip()
        if not filename:
            filename = "lorem_ipsum.txt"


        with open(filename, "w", encoding="utf-8") as file:
            file.write(generate_lorem_ipsum(length))

        print(f" \nSuccessfully generated a notepad with a length of {length} characters in the file '{filename}'")
        print(f"File size: {os.path.getsize(filename)} bytes")

    except ValueError:
        print("Error: Please enter a valid integer.")
    except IOError as e:
        print(f"File write error: {e} \n \n")

    input("\n\n Press Enter to exit...")


if __name__ == "__main__":
    main()


#pyinstaller --onefile --icon=lorem.ico --name "lorem ipsum generator" LoremIpsumGenerator.py

