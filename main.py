import subprocess

powershell_command = 'Set-DNSClientServerAddress –interfaceIndex $(Get-NetAdapter | % { Process { If ( $_.Status -eq "up" ) { $_.ifIndex } }}) –ServerAddresses ("78.157.42.100","78.157.42.101");'
cmd_command = """for /f "tokens=1,2,3,* delims= " %a in ('netsh interface show interface ^| findstr "Connected"') do @netsh interface ip set dns name="%d" static 78.157.42.100 & @netsh interface ip add dns name="%d" address=78.157.42.101 index=2"""

subprocess.run(cmd_command, shell=True)
