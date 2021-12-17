import subprocess


class CommandUtilities:
    """
    Utils to run command by Python-daemon
    """

    def __init__(self, cmd=str, encoding="UTF-8", timeout=None) -> None:
        """
        :param cmd: Command lines to run
            ex) wget __file_loc__
        :param encoding: set encoding on output
            default_val = "UTF-8"
        :param timeout: timeout until command finish

        :return: None
        """
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
