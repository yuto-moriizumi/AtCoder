print(*[i[::-1] for i in sorted([input()[::-1]
                                 for _ in range(int(input()))])], sep='\n')
