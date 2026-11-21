"""Write one original one-line joke about working beside an AI coding agent
to /output/entry.txt. Deterministic: same joke on every run."""
import os

JOKE = "My agent deleted 200 lines, added three tests, and the only line it couldn't explain in review was mine."

out_dir = "/output"
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(JOKE + "\n")
