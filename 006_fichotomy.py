def f(x):
    return pow(x,2) - 3*x + 2
def fichotomy(a,b,f,r):
    """a,b 为区间，r为误差"""
    num1 = f(a)
    num2 = f(b)
    if num1*num2 > 0:
        print('该区间不存在值')
        return None
    n_num ,p_num = (a, b) if num1 < num2 else (b, a)
    reslut = None

    def sub_fichotomy(n_num, p_num):
        if abs(n_num-p_num) < r:
            print('result:', (p_num+n_num)/2)
            global result
            result = (p_num+n_num)/2
            return result
        n_num, p_num = ((n_num+p_num)/2, p_num) if f((n_num+p_num)/2) < 0 else (n_num, (n_num+p_num)/2)
        sub_fichotomy(n_num, p_num)
    sub_fichotomy(n_num, p_num)
    return result
if __name__ == '__main__':
    print(fichotomy(0, 1.8, f, 0.0000001))