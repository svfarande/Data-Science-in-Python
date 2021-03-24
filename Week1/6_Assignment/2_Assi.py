# Assignment 1
# Part A

def names():
    simple_string = """Amy is 5 years old, and her sister Mary is 2 years old. 
    Ruth and Peter, their parents, have 3 kids."""

    # YOUR CODE HERE
    return re.findall(r'[A-Z][a-z]*', simple_string)
    # raise NotImplementedError()


print(names())


# Part B


def grades():
    with open("grades.txt", "r") as file:
        names = file.read()
        return re.findall(r'[A-Za-z ]+(?=: B)', names)

    # YOUR CODE HERE
    # raise NotImplementedError()


print(grades())

# Part C

import re


def logs():
    with open("logdata.txt", "r") as file:
        log_list = []
        log_data = file.read().splitlines()
        for log in log_data:
            log_dict = dict()
            host = re.search(r'\d+.\d+.\d+.\d+', log)
            log_dict["host"] = host.group()
            username = re.search(r'(?<= - )[a-z0-9-]*', log)
            log_dict["user_name"] = username.group()
            time = re.search(r'(?<=\[)\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2} -\d{4}', log)
            log_dict["time"] = time.group()
            request = re.search(r'(?<=")[A-Z]* /[\S]* [A-Z]*/\d.\d', log)
            log_dict["request"] = request.group()
            log_list.append(log_dict)
            # print(log.split("\"")[1])
        return log_list

    # YOUR CODE HERE
    # raise NotImplementedError()
    
'''
def logs():
    mylist = []
    with open("assets/logdata.txt", "r") as file:
        logdata = file.read()
    for item in re.finditer("(?P<host>[0-9\.]+)([\- ]{3,3})(?P<user_name>[a-z0-9\-]*)([ \[]+)(?P<time>[0-9\w\/\:\- ]+)([\] \"]+)(?P<request>[A-Z ]+[\/\w\.\-\:\(\)\%\&\^\$\#\@\!0-9 ]+)([0-9 ]*)", logdata):
        mylist.append(item.groupdict())
    return mylist
'''


print(len(logs()))
one_item = {'host': '146.204.224.152',
            'user_name': 'feest6811',
            'time': '21/Jun/2019:15:45:24 -0700',
            'request': 'POST /incentivize HTTP/1.1'}
print(one_item in logs())
