def sort_data_alph(file_path):

    data_from_file = []
    with open(file_path, "r", encoding="utf-8") as f:
        
        for line in f:
            data_from_file.append(line.strip()) #strip kustutab reavahetused ja tühikud

    data_from_file.sort() #sort meetod sorteerib andmed tähestikulises järjekorras

    with open(file_path, "w", encoding="utf-8") as f:

        for element in data_from_file:
            f.write(element + "\n") #kirjutab andmed faili üle, kustutades kõik olemasolevad andmed


sort_data_alph(r"data\\todo.txt")
