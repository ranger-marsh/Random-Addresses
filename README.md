This script takes in a text file. The file has one address per line. The script writes a text file that contains a random sampling of the original file. This script is used to help administer surveys for a local police station. The surveys are administered in specific neighborhoods concerning police relations. 

It can also accept a text file with used addresses. These addresses will not be sampled. The sample size will be based off of number of original addresses including the used addresses. 

USAGE: 
This script takes in a text file (in-file) of addresses and writes a text file (out-file) containing a random sample of the in-file. sample-rate is inputed as a floating point number (e.g. 0.5 == %50). The rate should be less than 1.0.

**Basic usage:**

$random_addresses.py [in-file] [out-file] [sample-rate]

On a second or subsequent runs a text file containing used
addresses can be passed. These addresses will not be sampled.

**Subsequent usage:**

$random_addresses.py [in-file ] [out-file ] [sample-rate] [used-file]

This script uses pytest for running test. http://doc.pytest.org/en/latest/
