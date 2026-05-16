import bisect

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        n = len(searchWord)
        products.sort()

        outputs = []
        for i in range(1, n + 1):
            prefix = searchWord[:i]
            good = bisect.bisect_left(products, prefix)
            output = []
            for j in range(good, min(good + 3, len(products))):
                if products[j].startswith(prefix):
                    output.append(products[j])
                else:
                    break

            outputs.append(output)      
        return outputs
