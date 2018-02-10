import logging

str = '"bob" - 0 Matches in this meeting , 7 Matches in other meetings '
print([int(s) for s in str.split() if s.isdigit()])

search_results = {"current_meeting": ([int(s) for s in str.split() if s.isdigit()])[0],
                  "other_meetings": ([int(s) for s in str.split() if s.isdigit()])[1]}

# assert 5 == 3, "Fuck!"

page_results = 12

# assert (search_results["current_meeting"] + search_results
# ["other_meetings"]) == page_results, "invalid number of results!"


sr = [
    '"bob" - 0 Matches in this meeting , 7 Matches in other meetings',
    '1 Matches found in "1 - Call"',
    '1 Matches found in "7 - Automation Standup"',
    '1 Matches found in "35 - Automation Standup"',
    '3 Matches found in "46 - Automation Standup"']

top_summary = ([int(s) for s in sr[0].split() if s.isdigit()])[0] + ([int(s) for s in sr[0].split() if s.isdigit()])[1]
print(top_summary)
bottom_summary = 0
for i in range(1, len(sr)):
    bottom_summary += ([int(s) for s in sr[i].split() if s.isdigit()])[0]

print(bottom_summary)

import logging

try:
    assert top_summary == bottom_summary, "invalid number of search results"
    passed = True
except AssertionError as e:
    print (e)
    passed= False

print("go on ")
print(passed)