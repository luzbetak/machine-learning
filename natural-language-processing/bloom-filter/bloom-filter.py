from pybloom_live import BloomFilter

# Create a Bloom filter with a false positive probability of 0.1
filter = BloomFilter(capacity=1000000, error_rate=0.1)

# Add some elements to the filter
filter.add("element1")
filter.add("element2")
filter.add("element3")

# Check if an element is in the filter
if "element1" in filter:
    print("element1 is probably in the filter")
else:
    print("element1 is definitely not in the filter")

if "element4" in filter:
    print("element4 is probably in the filter")
else:
    print("element4 is definitely not in the filter")

