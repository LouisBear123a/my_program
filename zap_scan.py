import logging
from zapv2 import ZAPv2

# Set up logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

class ZAPScanner:
    def __init__(self, zap_url='http://localhost:8080'):
        self.zap_url = zap_url
        self.zap = ZAPv2(proxies={'http': self.zap_url, 'https': self.zap_url})
        self.zap.urlopen(self.zap_url)
        self.api_key = None

    def set_api_key(self, api_key):
        self.api_key = api_key
        self.zap.core.access_token(self.api_key)

    def spider(self, target_url):
        logger.info(f'Starting ZAP spider on {target_url}')
        spider_id = self.zap.spider.scan(target_url)
        while int(self.zap.spider.status(spider_id)) < 100:
            logger.info(f'Spider progress: {self.zap.spider.status(spider_id)}%')
        logger.info('ZAP spider scan complete')

    def active_scan(self, target_url):
        logger.info(f'Starting ZAP active scan on {target_url}')
        scan_id = self.zap.ascan.scan(target_url)
        while int(self.zap.ascan.status(scan_id)) < 100:
            logger.info(f'Active scan progress: {self.zap.ascan.status(scan_id)}%')
        logger.info('ZAP active scan complete')

    def report(self):
        logger.info('Generating ZAP HTML report')
        report_html = self.zap.core.htmlreport()
        with open('zap_report.html', 'w') as f:
            f.write(report_html)
        logger.info('ZAP HTML report saved to zap_report.html')

    def shutdown(self):
        logger.info('Shutting down ZAP')
        self.zap.core.shutdown()
