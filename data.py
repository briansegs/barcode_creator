"App data"
data = {
    "folder_path" : "/home/b-man/Documents/Programming/bar-code_creator/bar_codes",
    "options" : {
        "1" : "Use your own 13 digit number",
        "2" : "Generate a random 13 digit number",
        "3" : "Input a 3 digit prefix followed by a random 10 digit number"
    },
    "prefix" : "202"
}

def errorMsg(error):
    "returns a generic input error"
    errorStr = print(f'Input error: "{error}" is an invalid input.')
    return errorStr
