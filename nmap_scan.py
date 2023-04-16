import nmap
import argparse
import json

class NmapScanner:
    def __init__(self):
        self.nm = nmap.PortScanner()

    def scan(self, target):
        self.nm.scan(hosts=target, arguments='-sS -T4')
        return self.nm.all_hosts()

    def get_scan_results(self):
        return json.dumps(self.nm.all_hosts(), indent=4)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Nmap scanner')
    parser.add_argument('target', metavar='TARGET', type=str, help='Target to scan')
    parser.add_argument('--output', '-o', metavar='FILE', type=str, help='Output file')
    args = parser.parse_args()

    scanner = NmapScanner()
    scanner.scan(args.target)

    if args.output:
        with open(args.output, 'w') as f:
            f.write(scanner.get_scan_results())
    else:
        print(scanner.get_scan_results())
