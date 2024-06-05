import os
import sys
import shlex
import subprocess
import pexpect

def run_command(command):
    try:
        result = subprocess.run(shlex.split(command), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, cwd='/')
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Hata: {e.stderr}")

def main():
    while True:
        prompt = "┌──(kali㉿localhost)-[~]\n└─$ "
        command = input(prompt)
        
        if not command.strip():
            continue
        
        if command.strip().lower() in ['exit', 'quit']:
            break
        
        try:
            if command.strip().split()[0] == 'apt':
                run_command(command)
            else:
                child = pexpect.spawn(command, cwd='/')
                child.logfile = sys.stdout
                child.expect(pexpect.EOF)
        except pexpect.ExceptionPexpect as e:
            print(f"Hata: {e}")
        except Exception as e:
            print(f"Hata: {e}")

if __name__ == "__main__":
    main()
