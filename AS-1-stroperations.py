#1.STRING SLICING OPERATIONS

s="PythonProgramming"
print(s[0:6])

# # o/p:
# # python

print(s[6:18])

#o/p:
#programming

print(s[12:]) 

    #(OR)

print(s[-5:]) 

#o/p:
#mming

print(s[0:17:2])

#o/p:
#ptopormig

print(s[-1:-18:-1])

#o/p:
#gnimmargorpnohtyp

a="DataScience"
print(a[4:])

#o/p:
#Science

b="ArtificialIntelligence"
print(b[10:])

#o/p:
#Intelligence

h="MachineLearning"
print(h[4:11])

#o/p:
#ineLear

i="OpenAIChatGPT"
print(i[0:13:3])

#o/p:
#OnCtT

s="ComputerVision"
print(s[1:-1])

#o/p:
#omputerVisio


#2.List Slicing Operations

list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list[0:5])

#o/p:
#[1, 2, 3, 4, 5]

print(list[-3:])

#o/p:
#[8, 9, 10]

print(list[2:8])

#o/p:
# [3, 4, 5, 6, 7, 8]

print(list[::2])

#o/p:
# [1, 3, 5, 7, 9]

print(list[::-1])

#o/p:
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

l=['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(l[2:5])

#o/p:
# ['c', 'd', 'e']

print(l[2:])

#o/p:
# ['c', 'd', 'e', 'f', 'g']

print(l[0:4])

#o/p:
# ['a', 'b', 'c', 'd']

i=[10, 20, 30, 40, 50, 60, 70, 80]
print(i[0:7:3])

#o/p:
# [10, 40, 70]

a=i[::-1]
print(a[::2])

#o/p:
# [80, 60, 40, 20]


# 3.Complex String Operations:
s="PythonProgramming"
a=(s[0:6])
b=(s[-5:])
print(a+b)

#o/p:
# Pythonmming

s="DataScience2026"
print(s[2:9]+s[::-1])

#o/p:
# taScien6202ecneicSataD

d="HelloWorld"
print(d[0:5]+d[-5:])

#o/p:
# HelloWorld

s="ComputerNetwork"
print(s[0:14:2]+s[:4])

#o/p:
# CmueNtoComp

a="ArtificialIntelligence"
print(a[10:12])
print(a[-6:])

#o/p:
# In
# igence

b="ProgrammingLanguage"
print(b[3:13]+b[0:3])

#o/p:
# grammingLaPro

v="OpenAIChatGPT"
a=v[:6]
b=v[6:]
print(a)
print(b)
print(a+b)

#o/p:
# OpenAI
# ChatGPT
# OpenAIChatGPT

c="MachineLearning"
a=c[1::2]
b=c[-1::-1]
print(a)
print(b)
print(a+b)

#o/p:
# ahnLann
# gninraeLenihcaM
# ahnLanngninraeLenihcaM

r="WebDevelopment"
print(r[-1:-5:-1])
print(r[0:5])

#o/p:
# tnem
# WebDe

t="DatabaseManagement"
a=t[4:11]
b=t[-5::-1]
print(a+b)

#o/p:
# baseManeganaMesabataD

k="CyberSecurity"
a=k[1::2]
b=k[::2]
print(a)
print(b)
print(a+b)

#o/p:
# yeScrt
# Cbreuiy
# yeScrtCbreuiy

s="MobileApplication"
a=s[:8]
b=s[11::1]
print(a)
print(b)

#o/p:
# MobileAp
# cation

s="CloudComputing"
a=s[-1::-1]
b=s[:3]
print(a+b)

#o/p:
# gnitupmoCduolCClo

e="SoftwareEngineering"
a=e[-1:-12:-1]
b=e[:8]
print(a+b)

#o/p:
# gnireenignESoftware

q="ArtificialNeuralNetwork"
a=q[5:16]
b=q[18:]
print(a+b)

#o/p:
# icialNeuraltwork

s="DataAnalysisTools"
a=s[2::3]
b=s[-1::-1]
print(a+b)

#o/p:
# tnysoslooTsisylanAataD

h="Programming12345"
print(h[:11])

#o/p:
# Programming

s="StringOperations"
a=s[:6]
b=s[10:]
print(a+b)

#o/p:
# Stringations

w="LearningPython"
a=w[2:10]
b=w[-6:-1]
print(a+b)

#o/p:
# arningPyPytho

s="ArtificialIntelligence2026"
a=s[-4:]
b=s[:10]
print(a+b)

#o/p:
# 2026Artificial








