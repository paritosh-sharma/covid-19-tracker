def location_lists_maker():
    location_lists=[]
    with open ("countries_data.txt",'r') as l:
        data = l.read()
        for line in data.splitlines():
            location_lists.append(line)
    return location_lists
location_lists_maker()
