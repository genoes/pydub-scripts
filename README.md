# Installation
* Python 3.x

* Open Terminal

* Install [Homebrew](https://brew.sh/ "Homebrew"): `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

* Install [pydub](https://github.com/jiaaro/pydub/ "jiaaro - pydub | Github"): `pip install pydub`

* Install [ffmpeg](https://ffmpeg.org/ffmpeg.html "ffmpeg"): `brew install ffmpeg`


# audio-segment

### Description

This script uses pydub to splice an audio file into multiple segments based on the number of milliseconds specified.
* e.g., `chunk_length_ms = 10000` will segment an audio file into 10 second intervals.


# split-silence

### Description

This script uses pydub to splice an audio file into multiple segments where there are silent breaks in the audio.
