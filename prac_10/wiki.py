import wikipedia

search = input("Enter phrase to search: ")

while search != "":
    # print("Search results: ")
    # print(wikipedia.search(search))

    suggested = wikipedia.search(search, 1)

    try:
        # print("Summary: ")
        wikipedia.summary(suggested)
        # print(wikipedia.summary(suggested))
    except wikipedia.exceptions.DisambiguationError as e:
        print("Options: ")
        print(e.options)
        suggested = input("Enter option choice: ")
        # print("Summary: ")
        # print(wikipedia.summary(suggested))
        wikipedia.summary(suggested)

    page_result = wikipedia.page(suggested,auto_suggest=False)  # Removed the printed outputs of the previous parts
    print(page_result.title)
    print(page_result.summary)
    print(page_result.url)

    search = input("Enter phrase to search: ")

print("Ended :D")
