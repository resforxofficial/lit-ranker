import os

def joiner(value):
    return "\n".join(str(i) for i in value)

def startswith(lis: str, value: str) -> bool:
    if value == "":
        return False
    
    if len(value) > len(lis):
        return False
    
    return lis[:len(value)] == value

def lenerfolder(directory):
    if os.path.exists(directory) and os.path.isdir(directory):
        files_and_folders = os.listdir(directory)
        files = [f for f in files_and_folders if os.path.isfile(os.path.join(directory, f))]
        return len(files)
    else:
        print("error: dir not found")
        return 0