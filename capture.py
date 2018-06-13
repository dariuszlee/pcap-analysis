from subprocess import run, Popen, PIPE
import shlex
from time import sleep

__CAP_FILE = "capture.pcap"
__JSON_FILE = "capture.json"

# def start_capture():
#     cmd = '/usr/bin/tshark -f "port 443 || port 80" -Y "http || http2" -T json'
#     cmdArgs = shlex.split(cmd)
#     with open(__JSON_FILE, mode="w") as outFile:
#         proc = Popen(args=cmdArgs, stdout=outFile, stderr=PIPE)
#         input("Enter anything to stop capture:\n")
#         proc.kill()
#         proc.wait()
#         sleep(2)


def start_capture():
    cmd = '/usr/bin/tshark -w ' + __CAP_FILE + ' -f "port 443 || port 80"'
    cmdArgs = shlex.split(cmd)
    print(cmdArgs)
    proc = Popen(args=cmdArgs, stderr=PIPE)
    input("Enter anything to stop capture:\n")
    proc.kill()
    proc.wait()

def convert_capture():
    cmd = '/usr/bin/tshark -r ' + __CAP_FILE + ' -Y "http || http2" -T json'
    cmdArgs = shlex.split(cmd)
    with open(__JSON_FILE, mode="w") as outFile:
        run(args=cmdArgs, stdout=outFile)

if __name__ == "__main__":
    # Capture in pcap format
    start_capture()
    # Convert to json
    convert_capture()
    # Structure requests
