from windows_toasts import Toast, WindowsToaster
import os, subprocess

toaster = WindowsToaster('Chrome Remote Switch')
newToast = Toast()

result = subprocess.run(['net', 'start', 'chromoting'], shell=True)
# print(result.returncode)

if result.returncode==2:
    # os.system("net stop chromoting >/dev/null 2>&1")
    subprocess.Popen('net stop chromoting', shell=True)
    newToast.text_fields = ['Stop Chrome Remote']
else:
    # os.system("net start chromoting >/dev/null 2>&1")
    subprocess.Popen('net start chromoting', shell=True)
    newToast.text_fields = ['Start Chrome Remote']

toaster.show_toast(newToast)
