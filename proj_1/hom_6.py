# Pro6(피보나치)

n = int(input())

fi = [0] * 91

fi[1] = 1

for i in range(2, n+1):

    fi[i] = fi[i-1] + fi[i-2]

print(fi[n])