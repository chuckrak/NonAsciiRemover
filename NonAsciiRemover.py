"""
Author: Chuck Rak
Date: May 3 2021
"""
#opens files
import time
import string
def remove_ascii(infile, outfile):
    start = time.time()
    file_in = open(infile, 'r')
    file_out = open(outfile, 'w')
    count = 0
    file_lines = file_in.readlines()
    for line in file_lines:
        for char in line:
            if ord(char) > 128:
                line = line.replace(char, "")
                count +=1 
                if(count % 1000 == 0):
                    print(str(count) + " replacements made")
        file_out.write(line)
    print("file read")
    file_in.close()
    file_out.close()
    end = time.time()
    time_elapsed = end - start
    time_elapsed = time_elapsed * 1000 // 1 / 1000
    print("Removed " + str(count) + " non-Ascii characters in " + str(time_elapsed) + " seconds")


def main():
    infile = input("enter the name of the csv file you want to work with (no extension)")
    outfile = infile +'ascii.csv'
    infile = infile + '.csv'
    remove_ascii(infile, outfile)

if __name__ == "__main__":
    main()









## TESTING
# for line in new_lines:
#     for char in line:
#         if ord(char) > 128:
#             line = line.replace(char, "")
#             count +=1 
#             print(str(count) + " replacements made")

# print("total replacements made " + str(count))
# print("new file has " + str(count) + "ascii characters")



    


    





