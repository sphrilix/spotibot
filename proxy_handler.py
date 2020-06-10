from http_request_randomizer.requests.proxy.requestProxy import RequestProxy


class ProxyHandler:
    req_proxy = RequestProxy()
    proxies = req_proxy.get_proxy_list()

    def get_proxies(self, count: int):
        assert count < len(self.proxies), "Can't return more proxies then avaliable"
        return self.proxies[:count]

    def to_string(self):
        proxy_string = ""
        for i in range(len(self.proxies)):
            proxy_string = proxy_string + str(i + 1) + ". " + self.proxies[i].get_address() \
                           + " " + self.proxies[i].country + "\n"
        return proxy_string


p = ProxyHandler()
print(len(p.get_proxies(10000)))