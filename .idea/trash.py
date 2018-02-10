str = '"bob" - 0 Matches in this meeting , 7 Matches in other meetings '
print([int(s) for s in str.split() if s.isdigit()])

search_results = {"current_meeting": ([int(s) for s in str.split() if s.isdigit()])[0],
                  "other_meetings": ([int(s) for s in str.split() if s.isdigit()])[1]}

# assert 5 == 3, "Fuck!"

page_results = 12

assert (search_results["current_meeting"] + search_results
["other_meetings"]) == page_results, "invalid number of results!"
