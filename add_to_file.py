def add_task_to_file(file_path):

    new_task = "Celebrate small wins with a cookie"

    with open(file_path, "a", encoding="utf-8") as f: # "a" - flag. fail avatakse millegi lisamiseks
        f.write("\n" + new_task) # lisame uue rea/andmed faili lõppu

add_task_to_file(r"data\\todo.txt")