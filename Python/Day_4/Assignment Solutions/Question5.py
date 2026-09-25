# Question 5
def traverse_nested_config(config_dict, path, default = None): 
    if(type(config_dict) != dict or not path):
        return default
    try:
        value = config_dict[path[0]]

        if(len(path) == 1):
            return value

        return traverse_nested_config(value, path[1:])
        
    except (KeyError, TypeError, AttributeError):
            print("Key was not found, incorrect path given.")
            return default
def main():
    config_dict = {
        "server": {
            "host": "127.0.0.1",
            "port": 8080,
            "ssl": {
                "enabled": True,
                "cert_path": "/etc/ssl/certs"
            }
        },
        "database": "postgresql://localhost:5432"
    }

    path_str = input("Type the path: ")
    path = path_str.split(".")
    print(traverse_nested_config(config_dict, path))
    
main()