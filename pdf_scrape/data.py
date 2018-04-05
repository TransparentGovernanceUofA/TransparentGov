
jsonDictOld = '''
{ 
    "Meeting":
    {
        "filename":null,
        "materialFilename":null,
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


jsonDict3 = '''
{
  "Committee": "N/A",
  "Date": "N/A",
  "Title": "N/A",
  "Location": "N/A",
  "Time": "N/A",
  "Attendees": ["N/A"],
  "Items": [ {
      "Item No.": "N/A",
      "Agenda Title": "N/A",
      "Motion": "N/A",
      "Action Requested": "N/A",
      "Date": "N/A",
      "Committee": "N/A",
      "Proposed By": "N/A",
      "Presenter": "N/A",
      "Description": "N/A",
      "Participation": [ "N/A" ],
      "Approval Route": [ ""],
      "Final Approver": "N/A"
            } ],
  "url": "N/A"
}'''

nonAttendance = ["Voting Members:", "(delegate)",
                 "Statutory Members:", "Ex-Officio:", "Appointed",
                 "Members:", "STAFF:", "Approval of the Agenda", "Secretary",
                 "Lisa Stein", "", "Students:", "REGRETS:",
                 "Approval of the Agenda"]

#nonAttendance = "Chris Andersen \n"

testVariable = "Success"
