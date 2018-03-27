import requests
import sys
sys.stdout = open('output.ppm', 'w')

print("P3")
print("128 128")
print("255")
for i in range(0,128): 
    read = requests.get("https://www.random.org/integers/?num=384&min=0&max=255&col=1&base=10&format=plain&rnd=new").content.decode("utf-8")
    nums = read.split("\n")
    nums = [n for n in nums if n]
    for i in range (0,384,3):
        print( nums[i], nums[i+1], nums[i+2])
