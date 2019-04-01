to run this you will need:

pip install mmh3
pip install bitarray

you might need sudo for the above, as we learned in class don't run in sudo all the time though.

to execute type: python bloom_filter.py -d dictionary.txt -i sample_input.txt -o output3.txt output5.txt
according to my classmate the makefile is not needed since one does not compile python.
Questions:


1) I choose to use the mmh3 or murmur3 because in my experience when I am doing webpages they have trival data usually. So I am more concerned with speed than overall security. It is a non cryptographic function, but from my searching of how to implement hashes in python which would best fit this assignment for file i/o, and timing. In general non-crypto functions are used when speed is the concern, not the best in terms stability and guarantee according to geeksforgeeks on their page for the mmh3 libray. 

2) Time3 is usually about 0.00745 seconds long, Time5 is about 1.55 seconds long. The one with 3 hashes seems to perform almost twice as fast as the one 5 hashes. 


3) The probability of a false positive is (1-e^(-(kn)/m))^k. For 3 hashes: it is about 45.77E-6
							     For 5 hashes: it is about 76.291E-6

For false negatives it is impossible for bloom filters to have them which is one attractive property of the for security.

4) The way to reduce false positives is to increase the number of hashes or the or the hash space. 
