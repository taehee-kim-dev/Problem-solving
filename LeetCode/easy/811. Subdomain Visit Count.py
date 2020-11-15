from typing import List
import collections


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:

        subdomains_count = collections.defaultdict(int)

        for subdomain in cpdomains:
            visit_times, main_domain = subdomain.split()
            subdomains = main_domain.split('.')
            tmp_domains = ''
            for i, part_of_domain in enumerate(subdomains[::-1]):
                if i == 0:
                    subdomains_count[part_of_domain] += int(visit_times)
                    tmp_domains = part_of_domain
                else:
                    tmp_domains = part_of_domain + '.' + tmp_domains
                    subdomains_count[tmp_domains] += int(visit_times)

        answer = []
        for subdomain_result, times in subdomains_count.items():
            answer.append(str(times) + ' ' + subdomain_result)

        return answer


print(Solution().subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))
