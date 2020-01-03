# Segment audio files

## Description

This script uses [pydub](https://github.com/jiaaro/pydub/ "jiaaro - pydub | Github") to splice an audio file into multiple segments based on the number of milliseconds specified.
* e.g., `chunk_length_ms = 10000` will segment an audio file into 10 second intervals.

Note that duration of the last audio segment will be typically less than the specified length.

Specify the file format you want for your segments by modifying the export parameters in the script.
  * e.g., Replace `wav` with another audio file extension such as `mp3`, `flac`, `ogg`, etc .



## Installation
* Python 3.x

* Open Terminal

* Install [Homebrew](https://brew.sh/ "Homebrew"): `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

* Install **pydub**: `pip install pydub`

* Install [ffmpeg](https://ffmpeg.org/ffmpeg.html "ffmpeg"): `brew install ffmpeg`


## Run
* Run script: `python audio-segment.py`

* An output subdirectory (`/output`) will be created automatically.

* You will then be prompted to enter the source path to the audio file.

* The segments will then populate the output subdirectory.
