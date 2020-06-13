
import platform
from subprocess import Popen, PIPE
isAudio = False
if platform.system() == "Windows":
	p = Popen(["C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe", ". \"./get_media.ps1\";"], stdout=PIPE, stderr=PIPE)
	output, err = p.communicate()
	err = err.decode('utf-8')
	if(not err):
		isAudio = output.decode("utf-8").replace("\r\n","") == "True"
		print(isAudio)
elif platform.system() == "Linux":
	bashCommand = "if pacmd list-sink-inputs | grep -w state | grep RUNNING >/dev/null ; then echo True; else echo False; fi"
	p = Popen(bashCommand, shell=True, executable='/bin/bash', stdout=PIPE, stderr=PIPE)
	output, err = p.communicate()
	err = err.decode('utf-8')
	if(not err):
		isAudio = output.decode("utf-8").replace("\n","") == "True"
		print(isAudio)
	else:
		print(f"error is {err}")
elif platform.system() == "Darwin":
	bashCommand = " if [[ $(pmset -g | grep ' sleep') == *coreaudiod* ]]; then echo True; else echo False; fi"
	p = Popen(bashCommand, shell=True, executable='/bin/bash', stdout=PIPE, stderr=PIPE)
	output, err = p.communicate()
	err = err.decode('utf-8')
	if(not err):
		isAudio = output.decode("utf-8").replace("\n","") == "True"
		print(isAudio)
	else:
		print(f"error is {err}")
else:
	print("another platform")
