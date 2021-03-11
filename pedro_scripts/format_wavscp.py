import os
import sys
from pathlib import Path

'''
This script formats wav.scp since the full paths to the data files change according to the machine
where the data si stored, sorting the files in process like required by the kaldi framework.
'''

current_path = os.getcwd()
path = Path(os.getcwd())

data_folders = ["train", "test"]
string_dir = str(path.parent) + str("/data")

for folder in data_folders:
    filename_prefix = string_dir + "/" + folder
    filename = filename_prefix + "/wav.scp"

    new_wavscp_content = []
    with open(filename) as f:
        lines = f.readlines()

        # Read file content
        for l in lines:
            utterance_id = l.strip()
            if utterance_id[-4:] == '.wav':
                sys.exit(
                    'wav.scp is already formatted and ready for use. Follow the README.md instructions. Exiting.')

            utterance_id_without_spk = utterance_id.replace("pedro_", "")
            full_path_to_audio_file = filename_prefix + \
                "/pedro/" + utterance_id_without_spk + ".wav"
            line = utterance_id + " " + full_path_to_audio_file
            
            new_wavscp_content.append(line)

        # Write to file
        new_wavscp_content.sort()
        new_file = open(filename, "w")
        for l in new_wavscp_content:
            new_file.writelines([l, '\n'])
        print('{} is now formatted.'.format(filename))
        new_file.close()
