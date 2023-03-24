def countEmail():
    # This first line is provided for you
    name = input("Enter file:")
    if len(name) < 1 : name = "mbox-short.txt"
    handle = open(name)
    filelist = [i.split() for i in handle if i.startswith('From ')]
    emails = [i[1] for i in filelist]
    mydic = {i:emails.count(i) for i in emails}
    max_key = max(mydic, key=mydic.get)
    print(max_key, mydic[max_key])
        

## if you want to test locally run > python counter.py
if __name__ == "__main__":
    countEmail()
