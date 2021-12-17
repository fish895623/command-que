import subprocess


class CommandUtilities:
    def __init__(self, cmd=str, encoding="UTF-8", timeout=None) -> None:
        self.command = cmd.split()
        self.timeout = timeout
        self.encoding = encoding

    def run(self):
        proc = subprocess.Popen(
            self.command, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        res, err = proc.communicate(timeout=self.timeout)
        if err is None:
            return err.decode(self.encoding)
        elif res:
            return res.decode(self.encoding)
