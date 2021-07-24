import paramiko

from tkinter import *
from tkinter import filedialog


def run_command(cmd_str, hostname, port, username, password, nbytes=4096):
    client = paramiko.Transport((hostname, port))
    client.connect(username=username, password=password)

    stdout_data = []
    stderr_data = []
    session = client.open_channel(kind='session')
    session.exec_command(cmd_str)

    while True:
        if session.recv_ready():
            stdout_data.append(session.recv(nbytes))
        if session.recv_stderr_ready():
            stderr_data.append(session.recv_stderr(nbytes))
        if session.exit_status_ready():
            break

    print('exit status: ', session.recv_exit_status())


    session.close()
    client.close()


def sftp_upload_config(config_file, hostname, port, username, password):
    client = paramiko.Transport((hostname, port))
    client.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(client)
    sftp.put(config_file, "flash/config.rsc")
    sftp.close()
    print('SFTP Upload Complete.')


def sftp_upload_firmware(fw_file, hostname, port, username, password):
    client = paramiko.Transport((hostname, port))
    client.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(client)
    sftp.put(fw_file, "firmware.npk")
    sftp.close()
    print('SFTP Upload Complete.')


def gen_cmd_str_ip(ip, interface):
    return f"ip address add address={ip} interface={interface}"


def gen_cmd_str_gw(gateway):
    return f"ip route add dst-address=0.0.0.0/0 gateway={gateway}"


def gen_cmd_str_id(identity):
    return f"system identity set name={identity}"


def gen_cmd_str_wpa(wpa):
    return f"interface wireless security-profiles add name=WPA mode=dynamic-keys authentication-types=wpa2-psk wpa2-pre-shared-key={wpa}"


def gen_cmd_str_ssid1(ssid1):
    return f"interface wireless set ssid={ssid1} wlan1"


def gen_cmd_str_ssid2(ssid2):
    return f"interface wireless set ssid={ssid2} wlan2"


def init_tk(root):
    def select_config():
        filename = filedialog.askopenfilename()
        config_entries.insert('0.0', filename)
    def upload_config():
        print('Config Uploaded')
        config_name = config_entries.get('0.0', 'end')
        formatted_config_name = config_name.strip()
        sftp_upload_config((formatted_config_name), entries['mgmt_ip'].get(), int(entries['port'].get()), entries['user'].get(), entries['pass'].get())
    def select_firmware():
        firmware = filedialog.askopenfilename()
        firmware_entries.insert('0.0', firmware)
    def upload_firmware():
        fw_name = firmware_entries.get('0.0', 'end')
        formatted_fw_name = fw_name.strip()
        sftp_upload_firmware((formatted_fw_name), entries['mgmt_ip'].get(), int(entries['port'].get()), entries['user'].get(), entries['pass'].get())
        print('Firmware Uploaded')  
    def reboot_device():
        reboot_command = []
        reboot_cmd = 'system reboot'
        reboot_command.append(reboot_cmd)
        reboot_cmd = 'y'
        reboot_command.append(reboot_cmd)
        format_reboot = "\n".join(reboot_command)
        run_command(format_reboot, entries['mgmt_ip'].get(), int(entries['port'].get()), entries['user'].get(), entries['pass'].get())
        print('Device is rebooting')
    def reset_config():
        reset_command = []
        reset_cmd = 'system reset-configuration run-after-reset=flash/config.rsc no-defaults=yes'
        reset_command.append(reset_cmd)
        reset_cmd = 'y'
        reset_command.append(reset_cmd)
        format_reset = "\n".join(reset_command)
        run_command(format_reset, entries['mgmt_ip'].get(), int(entries['port'].get()), entries['user'].get(), entries['pass'].get())
    def clear_entries():
        for key, entry, in entries.items():
            entry.delete(0, 'end')
        config_entries.delete('0.0', 'end')
        firmware_entries.delete('0.0', 'end')
    def send_commands():
        all_commands = []
        cmd_str = gen_cmd_str_ip(entries['ip'].get(), interface_select.get())
        all_commands.append(cmd_str)
        cmd_str = gen_cmd_str_gw(entries['gateway'].get())
        all_commands.append(cmd_str)
        cmd_str = gen_cmd_str_id(entries['identity'].get())
        all_commands.append(cmd_str)
        cmd_str = gen_cmd_str_wpa(entries['wpa'].get())
        all_commands.append(cmd_str)
        cmd_str = gen_cmd_str_ssid1(entries['ssid1'].get())
        all_commands.append(cmd_str)
        cmd_str = gen_cmd_str_ssid2(entries['ssid2'].get())
        all_commands.append(cmd_str)
        formatted_commands = "\n".join(all_commands)
        run_command(formatted_commands, entries['mgmt_ip'].get(), int(entries['port'].get()), entries['user'].get(), entries['pass'].get())
    
    root.geometry("825x315")
    root.title("Lets get configuring!")
    root.eval('tk::PlaceWindow . center')
    entries = {}
    mgmt_ip_label = Label(root, text='Management IP Address:', font=('calibre', 10, 'bold'))
    entries['mgmt_ip'] = Entry(root, justify='center', font=('calibre', 10))
    mgmt_ip_label.grid(row=0, column=0, sticky = W, pady=2, padx=5)
    entries['mgmt_ip'].grid(row=0, column=1, pady=2)
    port_label = Label(root, text='Management Port:', font=('calibre', 10, 'bold'))
    entries['port'] = Entry(root, justify='center', font=('calibre', 10))
    port_label.grid(row=0, column=2, sticky=W, pady=2, padx=5)
    entries['port'].grid(row=0, column=3, pady=2)
    user_label = Label(root, text='Username:', font=('calibre', 10, 'bold'))
    entries['user'] = Entry(root, justify='center', font=('calibre', 10))
    user_label.grid(row=1, column=0, sticky=W, pady=2, padx=5)
    entries['user'].grid(row=1, column=1, pady=2)
    pass_label = Label(root, text='Password:', font=('calibre', 10, 'bold'))
    entries['pass'] = Entry(root, justify='center', show='*', font=('calibre', 10))
    pass_label.grid(row = 1, column=2, sticky=W, pady=2, padx=5)
    entries['pass'].grid(row=1, column=3, pady=2)
    ip_label = Label(root, text='WAN IP Address:', font=('calibre', 10, 'bold'))
    entries['ip'] = Entry(root, justify='center', font=('calibre', 10))
    ip_label.grid(row=2, column=0, sticky=W, pady=2, padx=5)
    entries['ip'].grid(row= 2, column=1, pady=2)
    interface_list = ['ether1', 'ether2', 'ether3', 'ether4', 'ether5', 'ether6', 'ether7', 'ether8', 'ether9', 'ether10', 'wlan1', 'wlan2', 'sfp1', 'sfp+plus1']
    interface_select = StringVar(root)
    interface_select.set(interface_list[0])
    interface_label = Label(root, text = 'WAN Interface:', font=('calibre', 10, 'bold'))
    interface_drop = OptionMenu(root, interface_select, *interface_list)
    interface_label.grid(row=3, column=0, sticky=W, pady=2, padx=5)
    interface_drop.grid(row=3, column=1, pady=2)
    gateway_label = Label(root, text='Default Gateway:', font=('calibre', 10, 'bold'))
    entries['gateway']=Entry(root, justify='center', font=('calibre', 10))
    gateway_label.grid(row=4, column=0, sticky=W, pady=2, padx=5)
    entries['gateway'].grid(row=4, column=1, pady=2)
    identity_label = Label(root, text='Identity:', font=('calibre', 10, 'bold'))
    entries['identity'] = Entry(root, justify='center', font=('calibre', 10))
    identity_label.grid(row=5, column=0, sticky=W, pady=2, padx=5)
    entries['identity'].grid(row=5, column=1, pady=2)
    wpa_label = Label(root, text='WiFi Password:', font=('calibre', 10, 'bold'))
    entries['wpa'] = Entry(root, justify='center', show='*', font=('calibre', 10))
    wpa_label.grid(row = 6, column=0, sticky=W, pady=2, padx=5)
    entries['wpa'].grid(row=6, column=1, pady=2)
    ssid1_label = Label(root, text='2.4Ghz SSID:', font=('calibre', 10, 'bold'))
    entries['ssid1'] = Entry(root, justify='center', font=('calibre', 10))
    ssid1_label.grid(row=7, column=0, sticky=W, pady=2, padx=5)
    entries['ssid1'].grid(row=7, column=1, pady=2)
    ssid2_label = Label(root, text='5Ghz SSID:', font=('calibre', 10, 'bold'))
    entries['ssid2'] = Entry(root, justify='center', font=('calibre', 10))
    ssid2_label.grid(row=8, column=0, sticky=W, pady=2, padx=5)
    entries['ssid2'].grid(row=8, column=1, pady=2)
    submit_button = Button(root, text='Submit', command=send_commands)
    submit_button.grid(row=9, column=2, sticky=W, pady=10, padx=5)
    clear_button = Button(root, text='Clear', command=clear_entries)
    clear_button.grid(row=9, column=1, sticky=E, pady=10, padx=5)
    config_entries = Text(root, height=1, width=20, font=('calibre', 10))
    config_entries.grid(row=3, column=3, sticky=N, columnspan=2, pady=2, padx=5)
    config_label = Label(root, text='Upload Configuration File:', font=('calibre', 10, 'bold'))
    config_label.grid(row=2, column=2, sticky=N, pady=2, padx=5)
    config_button = Button(root, text='Select', command=select_config)
    config_button.grid(row=3, column=2, sticky=W, pady=2, padx=5)
    upload_button = Button(root, text='Upload', command=upload_config)
    upload_button.grid(row=3, column=2, sticky=E, pady=2, padx=5)
    firmware_entries = Text(root, height=1, width=20, font=('calibre', 10))
    firmware_entries.grid(row=5, column=3, sticky=N, columnspan=2, pady=2, padx=5)
    firmware_label = Label(root, text='Upload Firmware File:', font=('calibre', 10, 'bold'))
    firmware_label.grid(row=4, column=2, sticky=W, pady=2, padx=5)
    firmware_select_button = Button(root, text='Select', command=select_firmware)
    firmware_select_button.grid(row=5, column=2, sticky=W, pady=2, padx=5)
    firmware_upload_button = Button(root, text='Upload', command=upload_firmware)
    firmware_upload_button.grid(row=5, column=2, sticky=E, pady=2, padx=5)
    reboot_button = Button(root, text='Reboot', command=reboot_device)
    reboot_button.grid(row=6, column=3, sticky=N, pady=2, padx=5)
    reset_button = Button(root, text='Run', command=reset_config)
    reset_button.grid(row=4, column=3, sticky=N, pady=2, padx=5)

def main():
    root = Tk()
    init_tk(root)
    root.mainloop()
    paramiko.util.log_to_file('paramiko.log', level='INFO')

if __name__ == '__main__':
    main()

