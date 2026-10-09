def use_write_mode(file_path):

    with open(file_path, "w", encoding="utf-8") as f: # "w" - flag. fail avatakse millegi kirjutamiseks
        pass #ei tehta mitte midagi

use_write_mode(r"data\\todo.txt")

#kirjutab faili todo.txt sisu üle, kustutades kõik olemasolevad andmed