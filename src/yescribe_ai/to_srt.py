"""Transform https://yescribe.ai transcripts into SRT."""

from __future__ import annotations

import argparse
from pathlib import Path
import re


def parse_and_convert(input_file: Path, output_file: Path) -> None:
    """
    Read a text file containing timestamped dialogue and convert it to SRT format.

    Args:
        input_file (Path): Path to the input text file.
        output_file (Path): Path to the output SRT file.
    """
    srt_output = []

    with input_file.open("r", encoding="utf-8") as file:
        content = file.read()

    # Split by speaker blocks
    blocks = content.split("SPEAKER_00:")
    srt_index = 1

    for block in blocks:
        if match := re.search(
            r"\((\d{2}:\d{2}:\d{2}-\d{2}:\d{2}:\d{2})\)\s+(.*)", block, re.DOTALL
        ):
            time_range, text = match.groups()
            start_time, end_time = time_range.split("-")

            # Clean up text by stripping excess whitespace
            cleaned_text = " ".join(text.strip().split())

            # Format SRT block
            srt_output.append(
                f"{srt_index}\n{start_time},000 --> {end_time},000\n{cleaned_text}\n\n"
            )
            srt_index += 1

    # Write to output file
    with output_file.open("w", encoding="utf-8") as file:
        file.writelines(srt_output)


def main():
    parser = argparse.ArgumentParser(
        description="Convert timestamped text from Yescribe to SRT format."
    )
    parser.add_argument(
        "input_file",
        type=Path,
        help="Path to the input text file.",
    )
    parser.add_argument(
        "output_file",
        type=Path,
        nargs="?",
        help="Path to the output SRT file. Defaults to input file with .srt extension.",
    )

    args = parser.parse_args()

    input_file: Path = args.input_file  # type: ignore[annotation-unchecked]
    output_file: Path = args.output_file or input_file.with_suffix(".srt")  # type: ignore[annotation-unchecked]

    if not input_file.exists():
        print(f"Error: The file {input_file} does not exist.")
        return

    parse_and_convert(input_file, output_file)
    print(f"Converted {input_file} to {output_file}")


if __name__ == "__main__":
    main()
