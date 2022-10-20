import struct

from DnsQueryBodyModel import DnsQueryBodyModel
from DnsHeaderModel import DnsHeaderModel

class DnsService:

    def generate_header(self, pa_dns_header_model:DnsHeaderModel):
        return struct.pack("!6H",pa_dns_header_model.transaction,
                                 pa_dns_header_model.flags, 
                                 pa_dns_header_model.question_count,
                                  pa_dns_header_model.answer_count,
                                   pa_dns_header_model.authority_count,
                                    pa_dns_header_model.additional_count)

    def _format_domain_to_query_name(self, pa_domain):
        domain_splitted = pa_domain.split(".")
        qnameb_resultb = bytes()
        for label in domain_splitted:
            print(label)
            qnameb_resultb += struct.pack("!B", len(label))
            qnameb_resultb += label.encode()
        qnameb_resultb += struct.pack("!B", 0)
        return qnameb_resultb
        

    def generate_query_body(self, pa_dns_query_body_model:DnsQueryBodyModel):
        qnameb = self._format_domain_to_query_name(pa_dns_query_body_model.domain_name)
        qtypeb= struct.pack("!H", pa_dns_query_body_model.type)
        qclassb = struct.pack("!H", pa_dns_query_body_model.query_class)
        return qnameb + qtypeb + qclassb


