MORSE_CODE = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': "'", '-.-.--': '!', '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&', '---...': ':', '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_', '.-..-.': '"', '...-..-': '$', '.--.-.': '@', '...---...': 'SOS'}

def normalization_morse_code(morse_code: str) -> list[list[str]]:
    morse_code = morse_code.strip()
    words = morse_code.split("   ")
    words = [word.split(" ") for word in words]

    return words

def decode_morse(morse_code: str) -> str:
    result = ""
    words = normalization_morse_code(morse_code)
    for word in words:
        result += " "
        for char in word:
            result += MORSE_CODE.get(char)
    result = result.strip()

    return result

def main():
    print(decode_morse('.... . -.--   .--- ..- -.. .'))

if __name__ == "__main__":
    main()