import wikipedia

search = input("Enter phrase to search: ")

while search != "":
    print("Search results: ")
    print(wikipedia.search(search))

    suggested = wikipedia.search(search,1)

    try:
        print("Summary: ")
        print(wikipedia.summary(suggested))
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
        new_search = input("Enter: ")
        print("Summary: ")
        print(wikipedia.summary(new_search))

    search = input("Enter phrase to search: ")

print("Stopping")

