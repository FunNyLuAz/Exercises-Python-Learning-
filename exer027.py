n = input('Digite seu nome completo: ').strip()
ns = n.split()
nc = len(ns)

print('O seu primeiro nome é:{}\nO seu último nome é:{}'.format(ns[0], ns[nc-1]))
