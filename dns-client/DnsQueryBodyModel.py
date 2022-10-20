class DnsQueryBodyModel:
    def __init__(self, pa_domain_name, pa_type = 1, pa_query_class = 1) -> None:
        self.domain_name = pa_domain_name
        self.type = pa_type
        self.query_class = pa_query_class
        pass
    