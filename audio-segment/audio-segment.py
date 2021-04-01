# import modules
from pydub import AudioSegment
from pydub.utils import make_chunks
import os
try:
    os.makedirs('./ihc_udelaire_DATE')
except FileExistsError:
    # directory already exists
    pass


# set constants
source_path = input('\n'"Enter absolute path to source file: ").strip(" ")
myaudio = AudioSegment.from_file(source_path)
chunk_length_ms = 10000 # set desired clip duration in milliseconds (ms)
chunks = make_chunks(myaudio, chunk_length_ms)


# set export paramaters
for i, chunk in enumerate(chunks, start = 1):
    chunk_name = './output/ihc_udelaire_DATE_{:03d}.mp3'.format(i)
    print('exporting', os.path.basename(chunk_name))
    chunk.export(chunk_name, format='mp3')

print('\n'
'''
     ;
     ;;
     ;';.
     ;  ;;
     ;   ;;
     ;    ;;
     ;    ;;
     ;   ;'
     ;  '
,;;;,;
;;;;;;
`;;;;'    Finished!

''''\n')
