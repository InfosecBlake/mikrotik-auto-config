
# Notes:
    #yn = input('Would you like to reset the configuration? (y/n): ') /// These two lines will be used later
    #reset = 'system reset-configuration no-defaults={}'.format(yn) /// These two line will be used later


from pprint import pprint
import paramiko
from tkinter import *

#yn = input('Would you like to reset the configuration? (y/n): ') /// These two lines will be used later
#reset = 'system reset-configuration no-defaults={}'.format(yn) /// These two line will be used later

root = Tk()
root.geometry("750x315")
root.title("Lets get configuring!")
root.eval('tk::PlaceWindow . center')

mgmt_ip_label = Label(root, text = 'Management IP Address:', font=('calibre', 10, 'bold'))
mgmt_ip_entry = Entry(root, justify = 'center', font=('calibre', 10))
mgmt_ip_label.grid(row = 0, column = 0, sticky = W, pady = 2, padx = 5)
mgmt_ip_entry.grid(row = 0, column = 1, pady = 2)
print(mgmt_ip_entry.get())
def hostname(): 
    str(mgmt_ip_entry.get())

port_label = Label(root, text = 'Management Port:', font=('calibre', 10, 'bold'))
port_entry = Entry(root, justify = 'center', font=('calibre', 10))
port_label.grid(row = 0, column = 2, sticky = W, pady = 2, padx = 5)
port_entry.grid(row = 0, column = 3, pady = 2)

def port():
    port_1 = port_entry.get()
    print(f"port: '{port_1}'")
    port_2 = int(port_1)   
    return port_2 

port = port()
hostname = hostname()

nbytes = 4096

print(port)
print(hostname)

def send_commands():
    client = paramiko.Transport((hostname, port))
    client.connect(username=username, password=password)

    stdout_data = []
    stderr_data = []
    session = client.open_channel(kind='session')
    session.exec_command(formated_commands)

    while True:
        if session.recv_ready():
            stdout_data.append(session.recv(nbytes))
        if session.recv_stderr_ready():
            stderr_data.append(session.recv_stderr(nbytes))
        if session.exit_status_ready():
            break

    print('exit status: ', session.recv_exit_status())
    #print(''.join(stdout_data))
    print(''.join(stderr_data))

    session.close()
    client.close()


def clear_commands():
    mgmt_ip_entry.delete(0, 'end')
    port_entry.delete(0, 'end')
    user_entry.delete(0, 'end')
    pass_entry.delete(0, 'end')
    ip_entry.delete(0, 'end')
    gateway_entry.delete(0, 'end')
    identity_entry.delete(0, 'end')
    wpa_entry.delete(0, 'end')
    ssid1_entry.delete(0, 'end')
    ssid2_entry.delete(0, 'end')



interface_list = ['ether1', 'ether2', 'ether3', 'ether4', 'ether5', 'ether6', 'ether7', 'ether8', 'ether9', 'ether10', 'wlan1', 'wlan2', 'sfp1', 'sfp+plus1']
interface_select = StringVar(root)
interface_select.set(interface_list[0])


user_label = Label(root, text = 'Username:', font=('calibre', 10, 'bold'))
user_entry = Entry(root, justify = 'center', font=('calibre', 10))
user_label.grid(row = 1, column = 0, sticky = W, pady = 2, padx = 5)
user_entry.grid(row = 1, column = 1, pady = 2)

username = str(user_entry.get())
if username == '.!entry4':
    username = ''
else:
    username = str(user_entry.get())


pass_label = Label(root, text = 'Password:', font=('calibre', 10, 'bold'))
pass_entry = Entry(root, justify = 'center', show='*', font=('calibre', 10))
pass_label.grid(row = 1, column = 2, sticky = W, pady = 2, padx = 5)
pass_entry.grid(row = 1, column = 3, pady = 2)
password = str(pass_entry.get())

ip_label = Label(root, text = 'WAN IP Address:', font=('calibre', 10, 'bold'))
ip_entry = Entry(root, justify = 'center', font=('calibre', 10))
ip_label.grid(row = 2, column = 0, sticky = W, pady = 2, padx = 5)
ip_entry.grid(row = 2, column = 1, pady = 2)


interface_label = Label(root, text = 'WAN Interface:', font=('calibre', 10, 'bold')) #this should be a drop down
interface_drop = OptionMenu(root, interface_select, *interface_list)
interface_label.grid(row = 3, column = 0, sticky = W, pady = 2, padx = 5)
interface_drop.grid(row = 3, column = 1, pady = 2)


gateway_label = Label(root, text = 'Default Gateway:', font=('calibre', 10, 'bold'))
gateway_entry = Entry(root, justify = 'center', font=('calibre', 10))
gateway_label.grid(row = 4, column = 0, sticky = W, pady = 2, padx = 5)
gateway_entry.grid(row = 4, column = 1, pady = 2)


identity_label = Label(root, text = 'Identity:', font=('calibre', 10, 'bold'))
identity_entry = Entry(root, justify = 'center', font=('calibre', 10))
identity_label.grid(row = 5, column = 0, sticky = W, pady = 2, padx = 5)
identity_entry.grid(row = 5, column = 1, pady = 2)


wpa_label = Label(root, text = 'WiFi Password:', font=('calibre', 10, 'bold'))
wpa_entry = Entry(root, justify = 'center', show='*', font=('calibre', 10))
wpa_label.grid(row = 6, column = 0, sticky = W, pady = 2, padx = 5)
wpa_entry.grid(row = 6, column = 1, pady = 2)


ssid1_label = Label(root, text = '2.4Ghz SSID:', font=('calibre', 10, 'bold')) #ssid for 2.4Ghz
ssid1_entry = Entry(root, justify = 'center', font=('calibre', 10))
ssid1_label.grid(row = 7, column = 0, sticky = W, pady = 2, padx = 5)
ssid1_entry.grid(row = 7, column = 1, pady = 2)


ssid2_label = Label(root, text = '5Ghz SSID:', font=('calibre', 10, 'bold')) #ssid for 5Ghz
ssid2_entry = Entry(root, justify = 'center', font=('calibre', 10))
ssid2_label.grid(row = 8, column = 0, sticky = W, pady = 2, padx = 5)
ssid2_entry.grid(row = 8, column = 1, pady = 2)

#firmware_label = Label(root, text = 'Upgrade Firmware?', font=('calibre', 10, 'bold')) #this should be a yes or no
#firmware_yn
#reboot_label = Label(root, text = 'WARNING: Reboot required to update firmware, continue?', fg = 'red')
#script_label = Label(root, text = 'Baseline Configuration File', font=('calibre', 10, 'bold')) #this needs to be able to pick a file directory
#script_entry


submit_button = Button(root, text = 'Submit', command = send_commands)
submit_button.grid(row = 9, column = 2, sticky = W, pady = 10, padx = 5)
clear_button = Button(root, text = 'Clear', command = clear_commands)
clear_button.grid(row = 9, column = 1, sticky = E, pady = 10, padx = 5)


ip = str(ip_entry.get()) # will need to add a check to see if this will cause an ip conflict and valid ip
interface = str(interface_select.get())
gateway = str(gateway_entry.get()) # will need to add a check to make sure that gateway is within ip scope
identity = str(identity_entry.get()) 
wpa = str(wpa_entry.get())
ssid1 = str(ssid1_entry.get())
ssid2 = str(ssid2_entry.get())
#firmware = input('Would you like to update the firmware? (yes/no): ')

ip_command = 'ip address add address={} interface={}'.format(ip, interface)
gateway_command = 'ip route add dst-address=0.0.0.0/0 gateway={}'.format(gateway)
id_command = 'system identity set name={}'.format(identity)
wpa_command = 'interface wireless security-profiles add name=WPA mode=dynamic-keys authentication-types=wpa2-psk wpa2-pre-shared-key={}'.format(wpa)
#ssid1_command = 'interface wireless set ssid={} wlan1'.format(ssid1)
ssid2_command = 'interface wireless set ssid={} wlan2'.format(ssid2)

all_commands = [ip_command, gateway_command, id_command, wpa_command, ssid2_command]
formated_commands = "\n".join(all_commands)

root.mainloop()