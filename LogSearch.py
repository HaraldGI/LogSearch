import os
import re

print("""
 ___      _______  _______  _______  _______  _______  ______    _______  __   __   
|   |    |       ||       ||       ||       ||   _   ||    _ |  |       ||  | |  |  
|   |    |   _   ||    ___||  _____||    ___||  |_|  ||   | ||  |       ||  |_|  |  
|   |    |  | |  ||   | __ | |_____ |   |___ |       ||   |_||_ |       ||       |  
|   |___ |  |_|  ||   ||  ||_____  ||    ___||       ||    __  ||      _||       |  
|       ||       ||   |_| | _____| ||   |___ |   _   ||   |  | ||     |_ |   _   |  
|_______||_______||_______||_______||_______||__| |__||___|  |_||_______||__| |__|  
|  | |  ||    |       |  _    |                                                     
|  |_|  | |   |       | | |   |                                                     
|       | |   |       | | |   |                                                     
|       | |   |  ___  | |_|   |                                                     
 |     |  |   | |   | |       |                                                     
 _|___|_  |___|_|___| |_______|

Search .log files from the Autromaster systems. Place the program inside
the same folder as the console1.log, console2.log files.

For errors please contact:
harald@gimse.digital

What kind of log item do you want to search for?
Self Verify finds every item logged with a Self Verify fault
Forurenset find every item logged which are contaminated.

""")

pattern = input("Please state the input: ")
# Chosen search pattern
detectorPattern = re.compile(r'\d\d\.\d\d\d')
# Fire alarm detector pattern, etc. 03.040
directory = os.listdir()
foundDetector = []
for x in range(len(directory)):
    try:
        with open(directory[x], 'r') as reader:
            # Read and print the entire file line by line
            for line in reader:
                findLine = re.search(pattern, line)
                if findLine is not None:
                    mo = detectorPattern.search(findLine.string)
                    mog = mo.group()
                    if mog not in foundDetector:
                        foundDetector.append(mog)
    except:
        continue
        print(f"Could not open {directory[x]}, invalid filetype.")
        # For skipping documents who cant be opened.

for x in foundDetector:
    print(x)

input()
