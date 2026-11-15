# #função
# def adicionar_print(a, b):
#     print(a + b)
# #adicionando valores
# adicionar_print(a = 5, b = 10)
# #retornando valores
# def add_return(a, b):
#     return a + b

# resultado = add_return(a = 5, b = 10)


# def calculate_area(width, height):
#     area = width * height
#     area = area * 1.5
#     return area

# # Store the returned value
# room_area = calculate_area(10, 12)
# print(f"Room size: {room_area} sq ft")  # Room size: 120 sq ft

# def double(number):
#     return number * 2

# # Store in variable
# result = double(5)

# # Use in expressions
# total = double(2) + double(8)  # 10 + 6 = 16

# # Pass to other functions
# print(double(2))  # 20

# # Use in conditions
# if double(7) > 10:
#     print("Big number!")
# else:
#     print('shit number')

#retorno de várias funções
def simples():
    numeros = [1,2,3,4,5]
    primeiro_numero = numeros[0]
    ultimo_numero = numeros[-1]
    return primeiro_numero, ultimo_numero
primeiro_numero, ultimo_numero = simples()
print(f'primeiro número: {primeiro_numero} ')
print(f"último número: {ultimo_numero}")