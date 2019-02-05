import metrics

def top3():
    query = raw_input("Write the name of the person you want to know for the top 3 matches: ")
    print metrics.overallCompatibility(query)
    

