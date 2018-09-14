import sys

script, input_encode, error = sys.argv


def print_line(line , encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string=raw_bytes.decode(encoding, errors=errors)
    print(raw_bytes, "~~~", cooked_string)
    pass


def main(lang_file, encoding, errors):
    line = lang_file.readline()
    if line:
        print_line(line, encoding, errors)
        return main(lang_file, encoding, errors)

lang_file = open("../../resources/languages.txt", encoding="UTF-8")
main(lang_file, input_encode, error)

