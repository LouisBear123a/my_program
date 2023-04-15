from typing import List

class Vulnerability:
    def __init__(self, name: str, severity: str, description: str):
        self.name = name
        self.severity = severity
        self.description = description

class VulnerabilityDatabase:
    def __init__(self):
        self.vulnerabilities = []

    def add_vulnerability(self, vulnerability: Vulnerability):
        self.vulnerabilities.append(vulnerability)

    def get_vulnerabilities(self) -> List[Vulnerability]:
        return self.vulnerabilities

    def search_vulnerabilities(self, keyword: str) -> List[Vulnerability]:
        return [vuln for vuln in self.vulnerabilities if keyword in vuln.name.lower() or keyword in vuln.description.lower()]

    def filter_vulnerabilities(self, severity: str) -> List[Vulnerability]:
        return [vuln for vuln in self.vulnerabilities if vuln.severity == severity]
