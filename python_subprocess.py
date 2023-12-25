from re import sub
import subprocess #สำหรับรัน terminal command

if __name__ == "__main__":
    # basic terminal command
    #subprocess.run(["ls","-ltr"])
    #subprocess.run(["rm","-r","/home/tohn/testfolder1"])

    #python commands
    print(f"first run num=100 XX=90")
    subprocess.run(["python","firstpy.py", "--num", "100", "--XX", "90"])
    print(f"second run num=-10 XX=-90")
    subprocess.run(["python","firstpy.py", "--num", "-10", "--XX", "-90"])
    print(f"first run num=0")
    subprocess.run(["python","firstpy.py", "--num", "0"])