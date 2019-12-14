# import modules
from pydub import AudioSegment
from pydub.utils import make_chunks
import os
try:
    os.makedirs('./output')
except FileExistsError:
    # directory already exists
    pass


# set constants
source_path = input('\n'"Enter path to source file: ")
myaudio = AudioSegment.from_file(source_path)
chunk_length_ms = 10000 # set desired clip duration in milliseconds (ms)
chunks = make_chunks(myaudio, chunk_length_ms)


# set export paramaters
for i, chunk in enumerate(chunks):
    chunk_name = './output/segment_{:02d}.wav'.format(i)
    print('exporting', chunk_name)
    chunk.export(chunk_name, format='wav')
print('\n'"done.")
