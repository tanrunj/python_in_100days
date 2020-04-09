a = float(input('edge a: '))
b = float(input('edge b: '))
c = float(input('edge c: '))

if a +b > c and a+c > b and b+c >a:
    print('Circumference is %f' %(a+b+c))
    p = (a+b+c)/2
    # Helen Formulation
    area = (p*(p-a)*(p-b)*(p-c)) ** 0.5
    print('area is %f' %(area))
else:
    print('cant construct a triangles')