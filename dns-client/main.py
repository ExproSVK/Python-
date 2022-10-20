from DnsHeaderModel import DnsHeaderModel
from DnsQueryBodyModel import DnsQueryBodyModel


question_text = input("Enter DNS name: ")
dns_header = DnsHeaderModel()
dns_body = DnsQueryBodyModel(question_text)
