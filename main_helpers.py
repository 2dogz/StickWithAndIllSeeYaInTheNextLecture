import os

def fLoop(directory):
    return os.listdir(directory)

def validatePath(message):
    while True:
        inputPath = input(message)
        try:
            fileBool = os.path.isdir(inputPath)
            if fileBool:
                return inputPath
                break
        except Exception as e:
            print(e)
            continue
