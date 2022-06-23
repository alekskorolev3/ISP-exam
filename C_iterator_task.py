def soch(n, m, c):
    arr = []

    soch_counter = 0

    for i in range(m):
        arr.append(i)
    arr.append(n)
    arr.append(0)

    while True:
        if soch_counter == c:
            return arr[0:m]
        else:
            soch_counter += 1

        for j in range(len(arr) - 1):
            if arr[j + 1] == arr[j] + 1:
                arr[j] = j
            else:
                break
        if j < m:
            arr[j] += 1
        else:
            break

def C(n,m):
    n_mul = 1
    m_mul = 1
    n_s_m_mul = 1;
    for i in range(n):
        n_mul *= i
        while i <= m:
            m_mul *= i
        while i <= n - m:
            n_s_m_mul *= i
    return n_mul / n_s_m_mul * m_mul

class Iterator:
    def __iter__(self):
        return self

    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.count = 0
        self.maxn = C(n, m)

    def __next__(self):
        if self.count < self.maxn:
            self.count += 1
            return soch(self.n, self.m, self.count - 1)
        else:
            raise StopIteration


for e in Iterator(5, 3):
    print(e)
