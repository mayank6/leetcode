class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        dicti={}
        for domain in cpdomains:
                    count,domain=domain.split()
                    count=int(count)
                    frags=domain.split(".")
                    for i in range(len(frags)):
                        if ".".join(frags[i:]) in dicti:
                            dicti[".".join(frags[i:])]+=count
                        else:
                            dicti[".".join(frags[i:])]=count 
        a=[]
        for i in dicti:
            a.append("{} {}".format(dicti[i],i))
        return a
        
        
  #--------------------------------------------------------------------#
  class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        ans=collections.Counter()
        for domain in cpdomains:
            count,domain=domain.split()
            count=int(count)
            frags=domain.split(".")
            for i in range(len(frags)):
                ans[".".join(frags[i:])]+=count
        return ["{} {}".format(ct,dom) for dom,ct in ans.items()]
