import sys
from cherv.cherv import cherv_say

def main():
    if (len(sys.argv) >= 2):
        if (sys.argv[1] == "--help"):
            print("Использование: python -m cherv [сообщение]")
            return
        cherv_say(" ".join(sys.argv[1:]))

    if len(sys.argv) < 2:
        cherv_say()

if __name__ == "__main__":
    main()