#Expects file of integers separated by breakline
def read_file(filepath):
    with open(filepath, "r") as file:
        arrayOfInput = file.read().splitlines()
        file.close()
        if len(arrayOfInput) > 0:
            return list(map(int, arrayOfInput))
        else:
            print("No values found in file")
            return []