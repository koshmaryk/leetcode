"""

name, email1, email2 ...

1 union 2

dict
john@mail.com -> 1
john@mail.com -> 2
bob@mail.com -> 3

"""
from collections import defaultdict

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        while self.parent[x] != x:
            x = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return

        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
            self.rank[root_x] += self.rank[root_y]
        else:
            self.parent[root_x] = root_y
            self.rank[root_y] += self.rank[root_x]


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        uf = UnionFind(n)

        email_to_id = {}
        for i in range(n):
            for email in accounts[i][1:]:
                if email in email_to_id:
                    uf.union(i, email_to_id[email])
                else:
                    email_to_id[email] = i

        id_to_emails = defaultdict(list)
        for email, id in email_to_id.items():
            root_id = uf.find(id)
            id_to_emails[root_id].append(email)

        output = []
        for root_id, emails in id_to_emails.items():
            output.append([accounts[root_id][0]] + sorted(emails))
        return output