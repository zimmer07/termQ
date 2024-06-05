import os
import sys
import shlex
import subprocess

def run_command(command):
    try:
        result = subprocess.run(shlex.split(command), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(result.stdout.strip())  # Bytes to str conversion
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
            run_command(command)
        except Exception as e:
            print(f"Hata: {e}")

if __name__ == "__main__":
    main()
