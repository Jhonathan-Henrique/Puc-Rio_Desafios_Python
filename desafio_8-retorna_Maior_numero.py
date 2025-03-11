# def retornaMaior(x, y):
#     if x > y:
#         print(f'{x} é o maior numero')
#     else:
#         print(f'{y} é o maior numero')

# retornaMaior(10,20)

def retornaMaior(x, y):
    if x > y:
        maior = x
    else:
        maior = y
    return maior

print(retornaMaior(10,20))