def most_frequent(s):
    d = dict()
    for key in s:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    sorted_dict=dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
    print (sorted_dict)
s=input("Please enter a string ")
s=s.lower()
most_frequent(s)
