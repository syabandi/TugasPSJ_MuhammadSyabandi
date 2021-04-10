import subprocess
import concurrent.futures
import time
from datetime import datetime
import csv

with open('hosts.cfg') as file:
    readFile = file.read().splitlines()


tanggal = datetime.now() 
tgl_jam = tanggal.strftime("%Y-%m-%d %H:%M:%S")

def check(ip):
    status, result = subprocess.getstatusoutput("ping -c1 " + ip)
    csvFile = open('output.csv', 'a')
    csvWriter = csv.writer(csvFile, delimiter=";")
    if (status == 0):
        csvWriter.writerow([tanggal, ip, 'UP'])
        return f"{tanggal} {ip} is UP"
    else:
        csvWriter.writerow([datetime.now(), ip, 'DOWN'])
        return f'{tanggal} {ip} is DOWN'



while(True):
    T1 = time.perf_counter()

    # proses multithreading
    with concurrent.futures.ThreadPoolExecutor() as executor:
        print("Mulai monitor......")
        results = executor.map(check, readFile)
        for result in results:
            print(result)

    T2 = time.perf_counter()

    print(f"selesai dalam : {round(T2 - T1, 2)} detik \n")

    time.sleep(3)