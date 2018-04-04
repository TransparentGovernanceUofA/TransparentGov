import tika, copy
tika.initVM()
from tika import parser
from dateutil import parser as date_parser
import os, glob
import json

def tika_handles_scrap():
    path_to_pdfs = 'PDFs'
    #list_of_paired_minutes = list()

    for committee in glob.glob(os.path.join(path_to_pdfs, '*')):
        for minute in glob.glob(os.path.join(committee, '*')):
            paired_minutes_path = glob.glob(os.path.join(minute, '*'))

            parsed_material = parser.from_file(paired_minutes_path[1])
            parsed_minutes = parser.from_file(paired_minutes_path[0])

            f_material = open("Tika_Material.txt", "w")
            f_minutes = open("Tika_Minutes.txt", "w")

            output_material = parsed_material["content"]
            output_minutes = parsed_minutes["content"]

            f_material.write(output_material)
            f_minutes.write(output_minutes)

            f_material.close()
            f_minutes.close()

            with open("Tika_Minutes.txt") as infile, open("new_approved_minutes.txt", 'w') as outfile:
                for line in infile:
                    if not line.strip(): continue
                    outfile.write(line)

            the_list, prepared_list, new_item_list, content =  breaking_items()
            file_no_list = generate_item(the_list, prepared_list, new_item_list, content)
            build_JSON(file_no_list)

def tika_handles_single_file():
    #path_to_pdfs = 'PDFs'
    #list_of_paired_minutes = list()
    #
    # for committee in glob.glob(os.path.join(path_to_pdfs, '*')):
    #     for minute in glob.glob(os.path.join(committee, '*')):
    #         paired_minutes_path = glob.glob(os.path.join(minute, '*'))
    #
    parsed_material = parser.from_file("PDFs/ASC/2017-06-15/Past-Meeting-Material.pdf")
    parsed_minutes = parser.from_file("PDFs/ASC/2017-06-15/Approved-Minutes.pdf")

    f_material = open("Tika_Material.txt", "w")
    f_minutes = open("Tika_Minutes.txt", "w")

    output_material = parsed_material["content"]
    output_minutes = parsed_minutes["content"]

    f_material.write(output_material)
    f_minutes.write(output_minutes)

    f_material.close()
    f_minutes.close()

    with open("Tika_Minutes.txt") as infile, open("new_approved_minutes.txt", 'w') as outfile:
        for line in infile:
            if not line.strip(): continue
            outfile.write(line)

    the_list, prepared_list, new_item_list, content =  breaking_items()
    file_no_list = generate_item(the_list, prepared_list, new_item_list, content)
    build_JSON(file_no_list)

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
                    try:
                        new_item_list.remove(thing)
                    except ValueError:
                        print("OPS!", thing)
                else:
                    skip = thing
                    break

        the_list = list(zip(new_item_list, new_prepared_list))

        return the_list, prepared_list, new_item_list, content


def build_JSON(file_no_list):
    committee_dict = {"General Faculties Council":"GFC", "Academic Planning Committee":"APC", "Academic Standards Committee":"ASC", "Committee on the Learning Environment":"CLE", "Campus Law Review Committee":"CLRC",
    "Executive Committee":"EXEC", "Facilities Development Committee":"FDC", "Undergraduate Awards and Scholarship Committee":"UASC"}
    attendees_skip_words = [x.lower() for x in ['ATTENDEES:', 'Statutory Members:', 'Ex-Officio:','Elected faculty:','Students:','Appointed Members:', 'REGRETS:','STAFF:', 'Voting Members:', 'Non-Voting Members:', 'Presenter(s):', 'Academic staff-at-large', 'Alternate', 'Alumni', 'Appointed',
    'Chair-at-large', 'Dean-at-large', 'Delegate', 'Academic Staff', 'For Information', 'Observer', 'Other', 'Regular', 'Member']]

    check_point = "Open Session Minutes"
    json_dict = dict()
    item_dict = dict()
    list_of_items = list()
    new_item_dict = dict()


    with open("new_approved_minutes.txt") as f_minutes:
        content_minutes = f_minutes.readlines()
        if check_point in content_minutes[1].rstrip():
            committee = committee_dict[content_minutes[0].rstrip()]
            print(committee, content_minutes[2])
            date = content_minutes[2]
            location = content_minutes[3].rstrip()
            time = content_minutes[4].rstrip()
            starting = content_minutes[5].rstrip()
        # elif check_point in content_minutes[2].rstrip():
        else:
            committee = committee_dict[content_minutes[1].rstrip().lstrip()]
            print(committee, content_minutes[3])
            date = content_minutes[3]
            location = content_minutes[4].rstrip()
            time = content_minutes[5].rstrip()
            starting = content_minutes[6].rstrip()

        for line_num, line in enumerate(content_minutes):
            if 'OPENING SESSION' in line:
                end_num = line_num
                ending = content_minutes[end_num-2].rstrip()
                start_items_pg_num = line_num + 1

        attendees_with_title = [content_minutes[i].rstrip() for i in range(5, end_num-2)]
        attendees_list = [attendees for attendees in attendees_with_title if attendees.lower() not in attendees_skip_words]

        date = date_parser.parse(date).strftime('%Y-%m-%d')
        title = committee + ' ' + content_minutes[0].rstrip() + ' - ' + date
        #title_flag = False
        for num in file_no_list:
            item_number = num
            f_item = open(num + ".txt")
            title_flag = False
            motion_flag = False
            proposed_by_flag = False
            description_flag = True
            approval_route_flag = False
            participation_flag = False
            i_line_number = "999"
            motion_line = "999"
            #motion_subsection = ['Motion I:', 'Motion II:', 'Motion III:', 'Motion IV:', 'Motion V:']

            item_content = f_item.readlines()

            for line_num, x in enumerate(item_content):
                if x.startswith('Agenda Title'):

                    title_flag = True
                    start = 'Agenda Title: '

                if x.startswith('Motion'):
                    #motion_pos = x.find(':')
                    #motion_type = x[:motion_pos]
                    #if motion_type in motion_subsection:
                        #motion_type = x[:motion_pos]
                    #else:
                    motion_type = 'Motion'

                    motion_line = line_num



                if x.startswith('MOTION:'):
                    motion_line = line_num
                    motion_type = 'MOTION'


                if x.startswith('Proposed by'):
                    i_line_number = line_num - 1
                    proposed_by_flag = True
                    proposed_by_start = "Proposed by "
                    proposed_by_end = 'Presenter'
                    presenter_end = "Details"
                    proposed_by = block_of_lines(item_content, proposed_by_start, proposed_by_end)
                    presenter = block_of_lines(item_content, proposed_by_end, presenter_end)

                if x.startswith('Responsibility'):
                    description_flag = False

                if x.startswith('The Purpose'):
                    description_flag = False

                if x.startswith("Details"):
                    detail_line_num = line_num

                if x.startswith("Approval Route"):
                    approval_route_flag = True
                    approval_route_start = '(including meeting dates)'
                    approval_route_end = 'Final Approver'
                    router, approver = approval_route(item_content, approval_route_start, approval_route_end)

                if x.startswith('Participation:'):
                    participation_flag = True
                    participation_start = "Participation:"
                    participation_end = "Approval Route"
                    participation = block_of_participation(item_content, participation_start, participation_end)


            if int(motion_line) < int(i_line_number):
                motion_flag = True
                motion_start = motion_type + ": "
                motion_end = "Item"
                motion_field = block_of_lines(item_content, motion_start, motion_end)

            elif int(motion_line) >= int(i_line_number):
                motion_flag = False
                motion_type = 'Item'
                motion_field = "N/A"

            if not title_flag:
                title_start = item_content[0].rstrip()
                title_end = item_content[1].rstrip()
                item_title = title_start + ' ' + title_end

            if not proposed_by_flag:
                proposed_by ="N/A"
                presenter = "N/A"

            description = ''
            if description_flag:
                for i in range(2, len(item_content)):
                    description += item_content[i].replace(' \n', ' ')
            elif not description_flag:
                for i in range(detail_line_num, len(item_content)):
                    description += item_content[i].replace(' \n', ' ')

            if not participation_flag:
                participation = ["N/A"]

            if not approval_route_flag:
                router = ['N/A']
                approver = 'N/A'

            if title_flag:
                item_title = block_of_lines(item_content, start, motion_type)


            item_dict.update({'Item No.':item_number, 'Agenda Title':item_title, 'Motion': motion_field,
            "Action Requested": 'N/A', 'Date':date,'Committee': committee, 'Proposed By':proposed_by, 'Presenter':presenter,
            'Description':description, 'Participation': participation, 'Approval Route':router, 'Final Approver':approver})
            #print(item_dict)
            new_item_dict = copy.deepcopy(item_dict)
            list_of_items.append(new_item_dict)

        path_to_prototype = '/static/' + committee + '/' + date + '/Past-Meeting-Material.pdf'
        pdf_path = os.path.abspath(os.path.join(path_to_prototype, os.pardir))

        json_dict.update({'Committee':committee, 'Date':date, 'Title':title,
        'Location':location, 'Time':time, 'Attendees':attendees_list, "Items":list_of_items, "url": path_to_prototype})

        json_filename = "JSON/" + title + "_JSON.txt"
        os.makedirs(os.path.dirname(json_filename), exist_ok=True)
        with open(json_filename, "w") as o_file:
            json.dump(json_dict, o_file, indent=4, ensure_ascii=False)


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


def block_of_lines(content, start, end):
    block = ""
    found = False

    for line in content:
        line = line.rstrip()
        #print(line)
        if found:

            if line.startswith(end): break
            else:
                block += line + ' '
            # print("DAH", block)
        else:
            if line.startswith(start):
                found = True
                block = line.replace(start, '') + ' '

    return block

def block_of_participation(content, start, end):
    block = []
    found = False

    for line in content:
        line = line.rstrip()
        #print(line)
        if found:

            if line.startswith(end): break
            else:
                block.append(line + ' ')
            # print("DAH", block)
        else:
            if line.startswith(start):
                found = True
                block.append(line.replace(start, '') + ' ')

    return block


def approval_route(content, start, end):
    block = list()
    approver = ''
    found = False

    for line in content:
        line = line.rstrip()
        #print(line)
        if found:
            if 'http://www.governance.ualberta.ca/GovernanceToolkit/Toolkit.aspx' in line:
                continue
            if line.startswith(end):
                approver += line.replace(end, '')
                break
            else:
                block.append(line)
            # print("DAH", block)
        else:
            if line.startswith(start):
                found = True
                continue
                #block = line.replace(start, '')

    return block, approver


#tika_handles_scrap()
tika_handles_single_file()

# the_list, prepared_list, new_item_list, content =  breaking_items()
# file_no_list = generate_item(the_list, prepared_list, new_item_list, content)
# build_JSON(file_no_list)
