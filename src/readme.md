# languages
## python
### `product` function
`itertools.product` is a function in the `itertools` module in Python. It computes the Cartesian product of input iterables. The Cartesian product represents all possible combinations of elements from the input iterables.

Here's a basic example:

```python
from itertools import product

# Example usage
iterable1 = [1, 2]
iterable2 = ['a', 'b']

result = list(product(iterable1, iterable2))
print(result)
```

Output:
```text
[(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]
```
In this example, `product` generates all possible pairs of elements, one from `iterable1` and one from `iterable2`.

The function takes multiple input iterables, and each element in the result is a tuple containing one element from each input iterable. The number of elements in the result is the product of the lengths of the input iterables.

### unpack
In Python, the `*` (asterisk) is often used for unpacking iterable objects. For example:

```python
from typing import List
from itertools import product

# following lines
set_list: List[set] = [{1, 2, 3}, {4, 5, 6}, {7, 8}]
product(*set_list)
```

The `*set_list` syntax unpacks the sets in `set_list`, passing them as separate arguments to the product function. It is equivalent to `product({1, 2, 3}, {4, 5, 6}, {7, 8})`, generating the Cartesian product of the sets.

