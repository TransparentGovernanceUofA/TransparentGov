import tika, copy
tika.initVM()
from tika import parser
#from dateutil import parser as date_parser
import os, glob
import json
import pathlib


def adding_TASHA_fields():
    path_to_data = 'paird_material_minutes/bulk_input'


    for meeting in glob.glob(os.path.join(path_to_data, '*')):
        if '_TIKA' in meeting:
            new_value = ''
            dash_pos = meeting.find('-')
            suffix_pos = meeting.find('_TIKA')
            bulk_pos = meeting.find('bulk_input/')
            file_name = meeting[:suffix_pos]
            committee = meeting[bulk_pos+11:dash_pos]

            with open(meeting) as tika_file:
                for line in tika_file.readlines():
                    new_value += line

                tika_dict = {'content': new_value, "collection title":committee}


            with open(file_name+'.txt') as json_file:
                json_file.seek(0)
                json_data = json.load(json_file)
                json_data.update(tika_dict)



            json_filename = "DATA/" + file_name+'.txt'
            os.makedirs(os.path.dirname(json_filename), exist_ok=True)
            with open(json_filename, "w") as outfile:
                json.dump(json_data, outfile, indent=4, ensure_ascii=False)


adding_TASHA_fields()
