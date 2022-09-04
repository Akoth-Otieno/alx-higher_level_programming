#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    module_names = dir(hidden_4)
    for module_name in module_names:
        if module_name[:2] != "__":
            print("{:s}".format(module_name))
