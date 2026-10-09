def number_the_tasks(file_path):

    data_from_file = []

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            data_from_file.append(line.strip()) #strip kustutab reavahetused ja tühikud

    numbered_todo_list = []
    number = 1

    for element in data_from_file:
        numbered_line = f"{number}. {element}" # 1. tekst
        numbered_todo_list.append(numbered_line)
        number += 1 #numbri ühe võrra suurendamine. sama mis number = number + 1

    with open(file_path, "w", encoding="utf-8") as f:
        for element in numbered_todo_list:
            f.write(element + "\n") #kirjutab andmed faili üle

    

number_the_tasks(r"data\\todo.txt") #funktsiooni välja kutsumine