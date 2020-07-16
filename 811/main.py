class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        
        all_cpdomains = {}

        for cp in cpdomains:
            count, domain = cp.split(' ')
            count = int(count)
            while domain.find('.') != -1:
                if domain in all_cpdomains:
                    all_cpdomains[domain] += count 
                else:
                    all_cpdomains[domain] = count
                domain = domain[domain.find('.')+1:]
            # do it again for top level domain like com
            if domain in all_cpdomains:
                all_cpdomains[domain] += count 
            else:
                all_cpdomains[domain] = count
            domain = domain[domain.find('.')+1:]
        
        cpdomains = []
        for domain, count in all_cpdomains.items():
            cpdomains.append(str(count) + ' ' + domain)

        return cpdomains
