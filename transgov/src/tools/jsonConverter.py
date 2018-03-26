import tika, copy
tika.initVM()
from tika import parser
from dateutil import parser as date_parser
import os.path

def tika_handles_scrap():
    parsed_material = parser.from_file('Past-Meeting-Material.pdf')
    parsed_minutes = parser.from_file('Approved-Minutes.pdf')

    f_material = open("Tika_Material.txt", "w")
    f_minutes = open("Tika_Minutes.txt", "w")

    output_material = parsed_material["content"]
    output_minutes = parsed_minutes["content"]

    f_material.write(output_material)
    f_minutes.write(output_minutes)

    with open("Tika_Minutes.txt") as infile, open("new_approved_minutes.txt", 'w') as outfile:
        for line in infile:
            if not line.strip(): continue
            outfile.write(line)


def breaking_items():
    stopwords = ['Prepared by', 'Submitted by', 'Item No.']
    #f = open('material_wo_attachments.txt', 'w')
    li = list()
    prepared_list = list()
    item_list = list()
    headers = list()


    with open("Tika_Material.txt") as infile, open("new_material.txt", 'w') as outfile:
        for line in infile:
            if not line.strip(): continue
            outfile.write(line)

    with open("new_material.txt") as f_material:
        content = f_material.readlines()

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
            if skip > tracker:
                new_prepared_list.remove(tracker)
                continue
            for num, thing in enumerate(item_list):
                if thing <= skip:
                    continue
                elif int(thing) < int(tracker):
                    new_item_list.remove(thing)
                else:
                    skip = thing
                    break

        the_list = list(zip(new_item_list, new_prepared_list))

        return the_list, prepared_list, new_item_list, content


def build_JSON(file_no_list):
    committee_dict = {"General Faculties Council":"GFC", "Academic Planning Committee":"APC", "Academic Standards Committee":"ASC", "Committee on the Learning Environment":"CLE", "Campus Law Review Committee":"CLRC",
    "Executive Committee":"EXEC", "Facilities Development Committee":"FDC", "Undergraduate Awards and Scholarship Committee":"UASC"}
    attendees_skip_words = ['ATTENDEES:', 'Statutory Members:', 'Ex-Officio:','Elected faculty:','Students:','Appointed Members:', 'REGRETS:','STAFF:']
    json_dict = dict()
    item_dict = dict()

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
                start_items_pg_num = line_num + 1

        attendees_with_title = [content_minutes[i].rstrip() for i in range(5, end_num-2)]
        attendees_list = [attendees for attendees in attendees_with_title if attendees not in attendees_skip_words]

        date = date_parser.parse(date).strftime('%Y-%m-%d')
        title = committee + ' ' + content_minutes[0].rstrip() + ' - ' + date
        #title_flag = False
        for num in file_no_list:
            item_number = num
            item_dict['Item No.'] = item_number
            f_item = open(num + ".txt")
            title_flag = False
            item_content = f_item.readlines()
            for x in item_content:
                if 'Agenda Title: ' in x:
                    title_flag = True
                    p = x.find(':')
                    agenda_title = x[p+2:].rstrip()

            if not title_flag:
                print(item_number)
                agenda_title = "N/A"
                #TODO: get the title from approved Minutes
            item_dict['Agenda Title'] = agenda_title
            print("LALALALALAL", item_dict)






        json_dict.update({'Committee':committee, 'Date':date, 'Title':title,
        'Location':location, 'Time':time, 'Attendees':attendees_list})

        print(json_dict)


def generate_item(the_list, prepared_list, new_item_list, content):
    item_no_list = list()
    item_line_number = list()
    file_no_list = list()

    f_agenda = open("agenda.txt", "w")
    for n in range(0, prepared_list[0]+1):
        f_agenda.write(content[n])

    f_agenda.close()

    for i in new_item_list:
        item_no_line = content[i].rstrip()
        dot_pos = item_no_line.find(".")
        item_no_list.append(item_no_line[dot_pos+2:])

    matching = list(zip(item_no_list, the_list))
    #print(matching)
    for counter, item in enumerate(matching):
        file_no = matching[counter][0]
        file_no_list.append(file_no)

        f_item = open(file_no + ".txt", 'w')
        for j in range(int(matching[counter][1][0]), int(matching[counter][1][1])):
            f_item.write(content[j])

        f_item.close()


    for num in file_no_list:
        headers = list()
        read_file = open(num + ".txt", 'r+')
        read_content = read_file.readlines()
        read_file.seek(0)
        for co, l in enumerate(list(read_content)):
            if "Item No. " in l:
                headers.append(co)
                headers.append(co+1)
                headers.append(co+2)

            if co not in headers:
                read_file.write(read_content[co])

        read_file.truncate()
        read_file.close()
    return file_no_list



tika_handles_scrap()
the_list, prepared_list, new_item_list, content =  breaking_items()
file_no_list = generate_item(the_list, prepared_list, new_item_list, content)
build_JSON(file_no_list)
