import json
import os
from pathlib import Path


JSON_CONFIG = "config.json"
banner="""
     _            _                       _       _ _   
  __| | ___   ___| | _____ _ __ ___ _ __ | | ___ (_) |_ 
 / _` |/ _ \ / __| |/ / _ \ '__/ __| '_ \| |/ _ \| | __|
| (_| | (_) | (__|   <  __/ |  \__ \ |_) | | (_) | | |_ 
 \__,_|\___/ \___|_|\_\___|_|  |___/ .__/|_|\___/|_|\__|
 """
def usage():
    print(banner)
    print("{}".format(sys.argv[0]))
    
def allowed_language(l):
    return not (l == "binary" or l == "txt")
def get_language(ext):
    languages = {
        ".py" : "python",
        ".rb" : "ruby",
        ".c" : "c",
        ".php" : "php",
        ".pl" : "pl",
        ".txt" : "textual"
    }
    if ext in languages:
        return languages[ext]
    return "binary"

def read_config():
    with open(JSON_CONFIG, 'r') as f:
        config = json.load(f)
    return config

def get_exploits(exploit_db_path):
    p = Path(exploit_db_path)
    exploits = [str(x) for x in p.glob("**/*") if x.is_file()]
    return exploits

def categorize(exploits):
    ret = []
    for e in exploits:
        filename , file_extension = os.path.splitext(e)
        language = get_language(file_extension)
        exploit_path = e
        ret.append({
            "exploit_path" : exploit_path,
            "language" : language
        })
    return ret
    
            




    

def main():
    json_config_file = read_config()
    exploit_db_path = json_config_file['exploit-path']
    exploits = get_exploits(exploit_db_path)
    exploits = categorize(exploits)
    print(exploits)


if __name__ == "__main__":
    main()

