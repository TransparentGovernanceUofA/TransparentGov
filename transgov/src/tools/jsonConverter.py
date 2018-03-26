import tika, copy
tika.initVM()
from tika import parser
from dateutil import parser as date_parser

parsed_material = parser.from_file('Past-Meeting-Material.pdf')
parsed_minutes = parser.from_file('Approved-Minutes.pdf')
#print(parsed["metadata"])
#print(parsed["content"])

f_material = open("Tika_Material.txt", "w")
f_minutes = open("Tika_Minutes.txt", "w")

output_material = parsed_material["content"]
output_minutes = parsed_minutes["content"]

f_material.write(output_material)
f_minutes.write(output_minutes)

stopwords = ['Prepared by', 'Submitted by', 'Item No.']

f = open('material_wo_attachments.txt', 'w')
li = list()
prepared_list = list()
item_list = list()
committee_dict = {"General Faculties Council":"GFC", "Academic Planning Committee":"APC", "Academic Standards Committee":"ASC", "Committee on the Learning Environment":"CLE", "Campus Law Review Committee":"CLRC",
"Executive Committee":"EXEC", "Facilities Development Committee":"FDC", "Undergraduate Awards and Scholarship Committee":"UASC"}
attendees_skip_words = ['ATTENDEES:', 'Statutory Members:', 'Ex-Officio:','Elected faculty:','Students:','Appointed Members:', 'REGRETS:','STAFF:']
json_dict = dict()

with open("Tika_Material.txt") as f_material:
    content = f_material.readlines()
    #content = f_material.read().splitlines()
    #content = [x.strip() for x in content]
    #print(content)
    for line in content:
        li.append(line)

    for counter, item in enumerate(li):
        if stopwords[0] in item:
            prepared_list.append(counter)
        elif stopwords[1] in item:
            prepared_list.append(counter)
        elif stopwords[2] in item:
            item_list.append(counter)

    new_prepared_list = prepared_list[:]
    new_item_list = item_list[:]

    skip = item_list[0]

    for index, tracker in enumerate(prepared_list):
        #print("tracker: ", tracker)
        if skip > tracker:
            new_prepared_list.remove(tracker)
            continue
        for num, thing in enumerate(item_list):
            #print("thing: ", thing)
            #print("skip: ", skip)
            if thing <= skip:
                continue
            elif int(thing) < int(tracker):
                #print("removing: ", thing)
                new_item_list.remove(thing)
            else:
                skip = thing
                break


    print(new_prepared_list, new_item_list)

    the_list = list(zip(new_item_list, new_prepared_list))

    for n in range(0, prepared_list[0]+1):
        f.write(content[n])
    for c, i in enumerate(the_list):
        for j in range(int(the_list[c][0]), int(the_list[c][1])):
            f.write(content[j])

with open("Tika_Minutes.txt") as infile, open("new_approved_minutes.txt", 'w') as outfile:
    for line in infile:
        if not line.strip(): continue
        outfile.write(line)
    #content_minutes = f_minutes.read().splitlines()

with open("new_approved_minutes.txt") as f_minutes:
    content_minutes = f_minutes.readlines()
    committee = committee_dict[content_minutes[0].rstrip()]
    date = content_minutes[2]
    location = content_minutes[3].rstrip()
    time = content_minutes[4].rstrip()
    starting = content_minutes[5].rstrip()
    for line_num, line in enumerate(content_minutes):
        if 'OPENING SESSION' in line:
            end_num = line_num
            ending = content_minutes[end_num-2].rstrip()

    attendees_with_title = [content_minutes[i].rstrip() for i in range(5, end_num-2)]
    #print(attendees_with_title)
    attendees_list = [attendees for attendees in attendees_with_title if attendees not in attendees_skip_words]

    #json_dict['Committee'] = committee
    date = date_parser.parse(date).strftime('%Y-%m-%d')
    #json_dict['Date'] = date
    title = committee + ' ' + content_minutes[0].rstrip() + ' - ' + date
    #json_dict['Title'] = title
    #json_dict['Location'] = location
    #json_dict['Time'] = time
    #json_dict['Attendees'] = attendees_list
    json_dict.update({'Committee':committee, 'Date':date, 'Title':title,
    'Location':location, 'Time':time, 'Attendees':attendees_list})

    print(json_dict)

    #print(content_minutes[0:5])
