"""sanchit-gandhi Whisper-JAX transcription to SRT."""

from __future__ import annotations

import re
import sys


def convert_to_srt(input_file: str, output_file: str) -> None:
    with open(input_file, "r", encoding="utf-8") as infile:
        lines = infile.readlines()

    srt_lines = []
    subtitle_index = 1

    for line in lines:
        # Use regular expression to parse the timestamps and text
        match = re.match(
            r"\[(\d{2}:\d{2}\.\d{3}) -> (\d{2}:\d{2}\.\d{3})\]  (.+)", line.strip()
        )
        if match:
            start_time = match.group(1).replace(".", ",")
            end_time = match.group(2).replace(".", ",")
            text = match.group(3)

            # Append the subtitle index
            srt_lines.append(f"{subtitle_index}")
            subtitle_index += 1

            # Append the timestamp
            srt_lines.append(f"00:{start_time} --> 00:{end_time}")

            # Append the text
            srt_lines.append(text)

            # Append an empty line to separate subtitles
            srt_lines.append("")

    # Write the SRT content to the output file
    with open(output_file, "w", encoding="utf-8") as outfile:
        outfile.write("\n".join(srt_lines))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = f"{input_file}.formatted.srt"

    convert_to_srt(input_file, output_file)
