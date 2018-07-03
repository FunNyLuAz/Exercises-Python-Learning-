a = input('Digite algo:')

print('Tipo primitivo:',type(a))

print('Apenas possui letras?', a.isalpha())
print('Apenas possui números?', a.isnumeric())
print('Apenas está em maiúscula?', a.isupper())
print('Apenas está em minúscula?', a.islower())
print('Apenas possui digitos?', a.isdigit())
print('Está capitalizado?', a.istitle())
print('Apenas está em espaços?', a.isspace())
print('É Alfanúmerico?', a.isalnum())
