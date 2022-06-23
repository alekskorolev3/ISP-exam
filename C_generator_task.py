# def C(n, m):
#     res = []
#
#     def rec(i):
#         if len(res) == m:
#             yield res.copy()
#             return
#
#         while i < n:
#             res.append(i)
#             for res_t in rec(i + 1):
#                 yield res_t
#             i += 1
#             res.pop()
#
#     for res in rec(0):
#         yield res
#
#
# ans = list()
# for e in C(5, 3):
#     ans.append(e)
#     print(e)

def soch(n,m):
    arr = []

    for i in range(m):
        arr.append(i)
    arr.append(n)
    arr.append(0)

    while True:
        yield arr[0:m]
        for j in range(len(arr) - 1):
            if arr[j + 1] == arr[j] + 1:
                arr[j] = j
            else:
                break
        if j < m:
            arr[j] += 1
        else:
            break



for e in soch(5, 3):
    print(e)