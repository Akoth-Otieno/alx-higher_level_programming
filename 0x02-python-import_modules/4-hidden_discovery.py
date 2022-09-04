#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4
    file_names = dir(hidden_4)
    for file_name in file_names:
        if file_name[:2] != "__":
            print(file_name)
