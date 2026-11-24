# Break Production, Own It entry: deterministic, stdlib only, no network.
# Writes one line, 1-200 chars, no leading/trailing whitespace or newline.
import os

LINE = "I deleted the production database. The backup was in the same database."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(LINE)
    except OSError:
        os.makedirs("output", exist_ok=True)
        with open(os.path.join("output", "entry.txt"), "w", encoding="utf-8", newline="") as f:
            f.write(LINE)

if __name__ == "__main__":
    main()
