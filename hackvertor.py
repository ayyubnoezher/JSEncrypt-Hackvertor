import subprocess

cmd = 'python3 "<path_JSEncrypt_Lib.py>" ' + input

try:
    output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)

except subprocess.CalledProcessError as e:
        raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
