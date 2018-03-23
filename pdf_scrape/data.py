
jsonDict = '''
{ 
    "Meeting":
    {
        "filename":null,
        "title": null,
        "date": null,
        "committee":null,
        "time":null,
        "location":null,
        "attendees":[],
        "subsection": [
              { "Title": null,
                "Items": [
                   {
                          "index_in_pdf": null,
                          "separate_index":null,
                          "title":null,
                          "pages_start":null,
                          "pages_end":null,
                          "text":null,
                          "presenters": [ { "name":null } ],
                          "motions": [
                            {
                                "motion":null,
                                "carried":null,
                                "content":null
                            }],
                          "keywords": [ null, null ],
                          "discussion":null,
                          "purpose":null

                    }]

              }]
    }
} '''

nonAttendance = ["Voting Members:", "(delegate)",
                 "Statutory Members:", "Ex-Officio:", "Appointed",
                 "Members:", "STAFF:", "Approval of the Agenda", "Secretary",
                 "Lisa Stein", "", "Students:", "REGRETS:",
                 "Approval of the Agenda"]

#nonAttendance = "Chris Andersen \n"

testVariable = "Success"