n = int(input("n: "))
for i in range(1,11,1):
    for j in range(1,n+1,1):
        print(f"{j} * {i} = {i*j}", end='\t')
    print()