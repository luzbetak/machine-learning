Bloom Filter
============

## Input Element --> Hash Functions --> Bit Array Positions

A Bloom filter is a space-efficient probabilistic data structure that is used to test whether an element is a member of a set. This means it can check if an element is in the set, and it may return a false positive, but it will never return a false negative. In other words, if the Bloom filter says the element is not in the set, it is definitely not in the set. But if it says it is in the set, it might be mistaken.

The Bloom filter uses multiple hash functions to map the input element to multiple positions in a bit array. When checking if an element is in the set, it hashes the element again and checks all the positions. If all positions are set to 1, it assumes the element is in the set.

Bloom filters are widely used in various applications where we need to check the existence of an element in a large set without actually storing the elements, such as web crawlers, network routers, and databases.

However, the main downside of Bloom filters is that they can give false positives.

Here is a simple representation of a Bloom filter:



