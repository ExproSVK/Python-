import imp

from DnsSocketService import DnsSocketService
from DnsHeaderModel import DnsHeaderModel
from DnsQueryBodyModel import DnsQueryBodyModel
from DnsService import DnsService

dns_service = DnsService()
socket_service = DnsSocketService()

question_text = input("Enter DNS name: ")
dns_header = DnsHeaderModel()
dns_body = DnsQueryBodyModel(question_text)

socket_service.init_socket()
socket_service.send_data(dns_service.generate_header(dns_header) + dns_service.generate_query_body(dns_body))

reply_bytes, reply_addr = socket_service.get_response()
