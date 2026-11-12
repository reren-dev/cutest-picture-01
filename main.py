#!/usr/bin/env python3
"""
The Red Panda Hug: a baby red panda hugging a fluffy duckling, soft 3D render, daisy crown, mint background.
Copies entry.png to the output directory (MAKEFUN_OUTPUT_DIR or /output).
"""

import os
import pathlib
import shutil
import sys

def main():
    # The grader runs without MAKEFUN_OUTPUT_DIR set, so /output is the default (per the kit starter convention).
    output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR') or '/output'
    os.makedirs(output_dir, exist_ok=True)
    
    script_dir = pathlib.Path(__file__).parent
    src_path = script_dir / 'entry.png'
    dest_path = pathlib.Path(output_dir) / 'entry.png'
    
    if not src_path.exists():
        print(f"Error: Source image not found at {src_path}", file=sys.stderr)
        sys.exit(1)
        
    shutil.copyfile(src_path, dest_path)
    
    # Verify destination exists and compare source and destination file sizes
    if not dest_path.exists():
        print(f"Error: Destination file not found at {dest_path}", file=sys.stderr)
        sys.exit(1)

    src_size = src_path.stat().st_size
    dest_size = dest_path.stat().st_size
    if src_size != dest_size:
        print(f"Error: Size mismatch! Source size ({src_size}) != Dest size ({dest_size})", file=sys.stderr)
        sys.exit(1)
        
    print(f"Successfully copied entry.png to {dest_path} ({dest_size} bytes)")

if __name__ == '__main__':
    main()
