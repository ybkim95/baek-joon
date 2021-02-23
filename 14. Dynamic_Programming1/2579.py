import sys

num_stair = int(sys.stdin.readline().rstrip())

stair = [0]*(num_stair)
score = [int(sys.stdin.readline().rstrip()) for _ in range(num_stair)]

if num_stair == 1:
    stair[0] = score[0]
    print(stair[0])
elif num_stair == 2:
    stair[0] = score[0]
    stair[1] = max( stair[0]+score[1], score[1])
    print(stair[1])
elif num_stair == 3:
    stair[0] = score[0]
    stair[1] = max( stair[0]+score[1], score[1])
    stair[2] = max( score[1]+score[2], score[0]+score[2] )
    print(stair[2])
else:
    stair[0] = score[0]
    stair[1] = max( stair[0]+score[1], score[1])
    stair[2] = max( score[1]+score[2], score[0]+score[2] )

    for i in range(3,num_stair):
        stair[i] = max( stair[i-2]+score[i], stair[i-3]+score[i-1]+score[i] )

    print(stair[num_stair-1])    