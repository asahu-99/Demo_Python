{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 def binary_search(arr, target):\
    low, high = 0, len(arr) - 1\
    while low <= high:\
        mid = (low + high) // 2\
        if arr[mid] == target:\
            return mid\
        elif arr[mid] < target:\
            low = mid + 1\
        else:\
            high = mid - 1\
    return -1\
\
arr = sorted(list(map(int, input("Enter sorted numbers: ").split())))\
target = int(input("Enter element to search: "))\
print("Found at index:", binary_search(arr, target))\
}