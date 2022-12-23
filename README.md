# audacity-labels-to-subtitles
Python scripts to convert [Audacity](https://www.audacityteam.org/) labels to subtitles. Currently supported formats are:

* SubRip (*.srt) — The most well-known and easily understood subtitle file format on the Internet.
* SAMI (*.smi, *.sami) — It is one of the formats that allows colored subtitle text on YouTube.

This tool can be used to create accurately-timed subtitles quickly, for people used to using Audacity for audio editing.

## How to use

1. If you are adding subtitles to a video, extract the audio file (I recommend using [Avidemux](https://avidemux.org/)).
2. Import the audio file into Audacity, converting it to WAV if necessary.
3. Add labels to the audio file. You can use Ctrl+B as a keyboard shortcut to add a label.
    * **Note:** This tool assumes that all the labels are area labels. Do not add a point label.
4. Export the labels as a .txt file (which is also valid as a .tsv file).
5. Use the appropriate Python script in the command line. For example, to convert Audacity labels to SubRip subtitles:
    * `python labels_to_srt.py audacity_labels.txt subtitles.srt` (assuming `python` is in your `PATH`)
6. For further editing, I recommend [SubtitleEdit](https://www.nikse.dk/SubtitleEdit).

## How to contribute

You are welcome to fork this repository and add extra subtitle file formats to convert into.

If you cannot write code in Python, I may write the script if you explain to me how the particular file format works.