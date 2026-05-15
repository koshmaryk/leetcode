class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        n = len(searchWord)
        products.sort()

        outputs = []
        for i in range(1, n + 1):
            prefix = searchWord[:i]
            output = []
            for product in products:
                if product.startswith(prefix):
                    output.append(product)

                if len(output) == 3:
                    break

            outputs.append(output)      
        return outputs
