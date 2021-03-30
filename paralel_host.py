import subprocess
import multiprocessing
import time

T1 = time.perf_counter()
i = 0
hosts = ['192.168.1.10', '202.134.4.201', '192.168.1.3', '8.8.8.8', '8.8.4.4']

def check_host():
    status, result = subprocess.getstatusoutput("ping -c1 " + hosts[i])
    if (status == 0):
        print(f'Host {hosts[i]} is UP')
    else:
        print(f'Host {hosts[i]} is DOWN')
Processes = []

for x in range(len(hosts)):
    P = multiprocessing.Process(target=check_host)
    P.start()
    Processes.append(P)
    i += 1

for process in Processes:
    process.join()

T2 = time.perf_counter()
print(f"selesai dalam : {round(T2 - T1, 1)} detik")