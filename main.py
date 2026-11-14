"""Copy the committed letter image to the output directory, byte for byte.

The image is the entry; this program only places its exact bytes at
/output/entry.png (or $MAKEFUN_OUTPUT_DIR when set). Standard library only,
no network, no randomness: repeated runs produce identical output.
"""

import os
import shutil
from pathlib import Path

IMAGE_NAME = "entry.png"


def main():
    here = Path(__file__).resolve().parent
    source = here / IMAGE_NAME
    if not source.is_file():
        raise SystemExit(f"missing committed image: {source}")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, out_dir / IMAGE_NAME)


if __name__ == "__main__":
    main()
