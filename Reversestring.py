{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww30040\viewh18900\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 def is_prime(n):\
    if n <= 1:\
        return False\
    for i in range(2, int(n ** 0.5) + 1):\
        if n % i == 0:\
            return False\
    return True\
\
n = int(input("Enter a number: "))\
print("Prime" if is_prime(n) else "Not Prime")\
}