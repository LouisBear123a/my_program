import os
import time
from threading import Thread
from openvas_lib import VulnscanManager, ScannerError

class OpenVASScanner:
    def __init__(self, username, password, host, port=9390):
        self.username = username
        self.password = password
        self.host = host
        self.port = port

    def _launch_scan(self, target):
        try:
            scanner = VulnscanManager(self.host, self.port, self.username, self.password)
            scan_id, _ = scanner.launch_scan(target, profile="Full and fast")
            while True:
                status = scanner.get_scan_status(scan_id)
                if status == "Done":
                    break
                time.sleep(5)
            return scan_id
        except ScannerError as e:
            print("OpenVAS Scanner Error: ", e)

    def scan(self, target):
        scan_thread = Thread(target=self._launch_scan, args=[target])
        scan_thread.start()
        return "Scan launched. Use `show report` to see the results."
