# Split Audio Files on Silence

## Description

This script uses [pydub](https://github.com/jiaaro/pydub/ "jiaaro - pydub | Github") to splice an audio file into multiple segments where there are silent breaks in the audio.

Credits: [jiaaro](https://github.com/jiaaro/pydub/ "jiaaro | Github") & [Anil_M](https://stackoverflow.com/users/5936628/anil-m "Anil_M | StackOverflow")
#### Audio file formats
Specify the file format you want for your segments by modifying the export parameters in the script.
* e.g., Replace `wav` with another audio file extension such as `mp3`, `flac`, `ogg`, etc .



## Installation
* Python 3.x

* Open Terminal

* Install [Homebrew](https://brew.sh/ "Homebrew"): `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

* Install **pydub**: `pip install pydub`

* Install [ffmpeg](https://ffmpeg.org/ffmpeg.html "ffmpeg"): `brew install ffmpeg`



## Run
* Run script: `python split-silence.py`

* An output subdirectory (`/output`) will be created automatically.

* You will then be prompted to enter the source path to the audio file.

* The segments will then populate the output subdirectory.


## Troubleshooting


#### No output
If you are getting and output with little or no audio, it may be that the source file is quieter than your specified silence threshold.

Increase the `silence_thresh` value so that the script can adequately recognize the audio.
