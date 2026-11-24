"""The One-Line Exit — entry for make.fun.

Writes one line to /output/entry.txt.
The line is a funny one-line resignation letter.
"""
import os

LINE = "Dear boss, I quit. My last day is today, because the printer broke again and it was the final straw."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
