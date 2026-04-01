"""

name, email1, email2 ...

1 union 2

dict
john@mail.com -> 1
john@mail.com -> 2
bob@mail.com -> 3

"""
from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_ids = defaultdict(list)
        for i, account in enumerate(accounts):
            for email in account[1:]:
                email_to_ids[email].append(i)

        visited = [False] * len(accounts)

        def dfs(i, emails):
            if visited[i]:
                return

            visited[i] = True

            for email in accounts[i][1:]:
                emails.add(email)
                for neighbor in email_to_ids[email]:
                    dfs(neighbor, emails)


        output = []
        for i, account in enumerate(accounts):
            if not visited[i]:
                emails = set()
                dfs(i, emails)
                output.append([account[0]] + sorted(emails))
        return output
        