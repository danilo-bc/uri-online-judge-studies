glossario = {'vertebrado':{'ave':
                                {'carnivoro':'aguia', 'onivoro':'pomba'},
                           'mamifero':
                                {'onivoro':'homem', 'herbivoro':'vaca'}},
            'invertebrado':{'inseto':
                                {'hematofago':'pulga', 'herbivoro':'lagarta'},
                            'anelideo':
                                {'hematofago':'sanguessuga', 'onivoro':'minhoca'}}}




depth1 = input()
depth2 = input()
depth3 = input()
print(glossario[depth1][depth2][depth3])
