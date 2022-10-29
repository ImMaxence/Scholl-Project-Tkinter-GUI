import subprocess

def mail_sent():
    subprocess.call(["gcc", "F_ATTACHE.c"])
    send_exe = subprocess.call("./13.out")
    print(send_exe)
    print("runFILE & F_ATTACHE.c work")