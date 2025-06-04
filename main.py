from stats import *
import sys

def main():
    if(len(sys.argv) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        bookpath = sys.argv[1]
        words = get_num_words(bookpath)
        chars = get_num_chars(bookpath)
        report = report_num_chars(chars)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {bookpath}...")
        print("----------- Word Count ----------")
        print(f"Found {words} total words")
        print("--------- Character Count -------")
        for rep in report:
            if(rep["char"].isalpha()):
                print(f"{rep['char']}: {rep['num']}")
        print("============= END ===============")

main()