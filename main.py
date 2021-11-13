from numpy import loadtxt
import webbrowser

i=0

with open("doc.txt", "r") as tf:
    lines = tf.read().split(',')

for line in lines:
    print(str(i)+": "+line)
    new=2
    url=line
    webbrowser.open(url,new=new)
    i+=1