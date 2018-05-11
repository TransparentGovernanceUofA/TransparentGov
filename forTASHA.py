import tika, copy
tika.initVM()
from tika import parser
#from dateutil import parser as date_parser
import os, glob
import json
import pathlib
import requests
# import config as cfg


def adding_TASHA_fields():

    # usr = cfg.tasha['user']
    # psw = cfg.tasha['passwd']

    usr = input("enter user name: ")
    psw = input("enter psw: ")

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


                payload = {usr:psw}
                r = requests.post("http://162.246.157.115/tasha/opengovtest", data = json_data, params=payload)
                print(r)


            # json_filename = "DATA/" + file_name+'.txt'
            # os.makedirs(os.path.dirname(json_filename), exist_ok=True)
            # with open(json_filename, "w") as outfile:
            #     json.dump(json_data, outfile, indent=4, ensure_ascii=False)


adding_TASHA_fields()
