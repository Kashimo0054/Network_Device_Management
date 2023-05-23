import paramiko
import time
import getpass
from datetime import datetime

time_file = datetime.now().strftime("%y-%m-%d")

username = "Yourusername"
password = "YourPassword"
port = 22
device_list = {
"0.0.0.0":"core_Sw",
"0.0.0.0":"Cache_Sw",

}

for device in device_list:
    print("connnecting to  " + str(device))
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(device, port, username, password)
    connection = ssh_client.invoke_shell()

    connection.send('system-view\n')
    time.sleep(1)
    connection.send('ospf mib-binding 1\n')
    time.sleep(1)
    connection.send('q\n')
    time.sleep(1)
    connection.send('save\n')
    time.sleep(1)
    connection.send('y\n')
    time.sleep(10)

    connection.send('screen-length 0 temporary\n')
    time.sleep(2)
    connection.send('display current-configuration | include ospf ' + '\n' + '\n')
    time.sleep(6)


    resp = connection.recv(10000000000000000000000000000000000000000)
    output = resp.decode("ascii").split(',')

    readoutput = (''.join(output))
    time.sleep(5)
    saveoutput = open (" device "+ device +"txt",'w')

    saveoutput.write(str(readoutput))
    saveoutput.close()
    print("file saved successfully")
