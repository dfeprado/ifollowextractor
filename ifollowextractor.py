from bs4 import BeautifulSoup
import sys

if (len(sys.argv) != 3):
    exit()

with open(sys.argv[1], 'rb') as html:
    soup = BeautifulSoup(html, 'html.parser')
    html.close()

followersElements = soup.findAll("a", {"class":"_0imsa"})
followersNames = []
for follower in followersElements:
    followersNames.append(follower.text)

print("Found %d followers" % len(followersNames))
followersNames.sort()

with open(sys.argv[2], 'w') as output:
    for follower in followersNames:
        output.write("%s\n" % follower)
    output.close()