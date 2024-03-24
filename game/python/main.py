import subprocess

process = subprocess.Popen(["python", r"D:\renpy-8.1.3-sdk\kodigo\game\python\sub.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

output = process.communicate()#[0].decode('utf-8')
print(output)
