"""Fortune Cookie for the Liquidated Trader.

Writes a single fortune-cookie line (at most 20 words) for a crypto
trader who has just been liquidated, to /output/entry.txt.
"""
import os

FORTUNE = (
    "Your fortune has changed, trader: the market kept your coins, "
    "but returned your humility gift-wrapped."
)


def main() -> None:
    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
