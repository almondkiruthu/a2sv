# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        res = []
        domain_freq = {}
        for i in range(len(cpdomains)):
            # obtain domain and full domain
            count, domain = cpdomains[i].split()
            domain = domain.split(".")
            domain_length = len(domain)
            # create a build up string that we'll use to build our string backwards
            build_up = ""
            for j in range(domain_length - 1, -1, -1):
                subdomain = domain[j]
                # only separate the subdomains that are not in our first order
                if j < domain_length - 1:
                    build_up  = subdomain + "." + build_up
                else:
                    build_up += subdomain
                if build_up in domain_freq:
                    domain_freq[build_up] += int(count)
                else:
                    domain_freq[build_up] = int(count)

        for subdomain, count in domain_freq.items():
            res.append(f"{count} {subdomain}")
        return res

        