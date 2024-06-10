from Especie import Especie

banco_de_dados = {}

banco_de_dados['Leão'] = Especie(
    tipo_celular='Eucariontes',
    nutricao='Carnívoro',
    nome_filo='Chordata',
    reproducao='Sexuada',
    sono_hab='Diurno',
    locomocao='Quadrúpede',
    nome_ordem='Carnivora',
    caracterisca_ordem='Carnívoros terrestres',
    nome_familia='Felidae',
    caracteristica_familia='Carnívoros de topo de cadeia alimentar',
    nome_genero='Panthera',
    caracterisca_genero='Grandes felinos sociais',
    tamanho_corporal='Grande',
    tipo_camuflagem='Coloração amarela'
)

banco_de_dados['Elefante'] = Especie(
    tipo_celular='Eucariontes',
    nutricao='Herbívoro',
    nome_filo='Chordata',
    reproducao='Sexuada',
    sono_hab='Diurno',
    locomocao='Quadrúpede',
    nome_ordem='Proboscidea',
    caracterisca_ordem='Mamíferos com tromba',
    nome_familia='Elephantidae',
    caracteristica_familia='Mamíferos de grande porte',
    nome_genero='Loxodonta',
    caracterisca_genero='Mamíferos terrestres de grande porte',
    tamanho_corporal='Grande',
    tipo_camuflagem='Ausente'
)

banco_de_dados['Golfinho'] = Especie(
    tipo_celular='Eucariontes',
    nutricao='Carnívoro',
    nome_filo='Chordata',
    reproducao='Sexuada',
    sono_hab='Diurno',
    locomocao='Nadador',
    nome_ordem='Cetacea',
    caracterisca_ordem='Mamíferos marinhos',
    nome_familia='Delphinidae',
    caracteristica_familia='Odontocetos',
    nome_genero='Delphinus',
    caracterisca_genero='Mamíferos marinhos inteligentes',
    tamanho_corporal='Grande',
    tipo_camuflagem='Ausente'
)

banco_de_dados['Aguia'] = Especie(
    tipo_celular='Eucariontes',
    nutricao='Carnívoro',
    nome_filo='Chordata',
    reproducao='Sexuada',
    sono_hab='Diurno',
    locomocao='Voador',
    nome_ordem='Accipitriformes',
    caracterisca_ordem='Aves de rapina',
    nome_familia='Accipitridae',
    caracteristica_familia='Raptores diurnos',
    nome_genero='Aquila',
    caracterisca_genero='Aves de rapina com visão aguçada',
    tamanho_corporal='Médio',
    tipo_camuflagem='Plumagem camuflada'
)

banco_de_dados['Cobra'] = Especie(
    tipo_celular='Eucariontes',
    nutricao='Carnívoro',
    nome_filo='Chordata',
    reproducao='Sexuada',
    sono_hab='Diurno',
    locomocao='Rastejante',
    nome_ordem='Squamata',
    caracterisca_ordem='Répteis escamados',
    nome_familia='Colubridae',
    caracteristica_familia='Répteis não venenosos',
    nome_genero='Naja',
    caracterisca_genero='Geralmente venenosa',
    tamanho_corporal='Pequeno',
    tipo_camuflagem='Padrão de cores crípticas'
)

banco_de_dados['Onça Pintada'] = Especie(
    tipo_celular='Eucariontes',
    nutricao='Carnívoro',
    nome_filo='Chordata',
    reproducao='Sexuada',
    sono_hab='Noturno',
    locomocao='Quadrúpede',
    nome_ordem='Carnivora',
    caracterisca_ordem='Carnívoros terrestres',
    nome_familia='Felidae',
    caracteristica_familia='Carnívoros de topo de cadeia alimentar',
    nome_genero='Panthera',
    caracterisca_genero='Grandes felinos manchados',
    tamanho_corporal='Grande',
    tipo_camuflagem='Manchas em roseta'
)

banco_de_dados['Tigre'] = Especie(
    tipo_celular='Eucariontes',
    nutricao='Carnívoro',
    nome_filo='Chordata',
    reproducao='Sexuada',
    sono_hab='Diurno',
    locomocao='Quadrúpede',
    nome_ordem='Carnivora',
    caracterisca_ordem='Carnívoros terrestres',
    nome_familia='Felidae',
    caracteristica_familia='Carnívoros de topo de cadeia alimentar',
    nome_genero='Panthera',
    caracterisca_genero='Grandes felinos solitários e poderosos',
    tamanho_corporal='Grande',
    tipo_camuflagem='Listras verticais'
)

banco_de_dados['Baleia Azul'] = Especie(
    tipo_celular='Eucariontes',
    nutricao='Carnívoro',
    nome_filo='Chordata',
    reproducao='Sexuada',
    sono_hab='Diurno',
    locomocao='Nadador',
    nome_ordem='Cetacea',
    caracterisca_ordem='Mamíferos marinhos',
    nome_familia='Balaenopteridae',
    caracteristica_familia='Maior animal existente',
    nome_genero='Balaenoptera',
    caracterisca_genero='Maiores mamíferos marinhos',
    tamanho_corporal='Enorme',
    tipo_camuflagem='Ausente'
)

banco_de_dados['Chimpanze'] = Especie(
    tipo_celular='Eucariontes',
    nutricao='Omnívoro',
    nome_filo='Chordata',
    reproducao='Sexuada',
    sono_hab='Diurno',
    locomocao='Quadrúpede',
    nome_ordem='Primates',
    caracterisca_ordem='Mamíferos primatas',
    nome_familia='Hominidae',
    caracteristica_familia='Parentes próximos dos humanos',
    nome_genero='Pan',
    caracterisca_genero='Primatas inteligentes e sociais',
    tamanho_corporal='Médio',
    tipo_camuflagem='Ausente'
)

banco_de_dados['Aguia Calva'] = Especie(
    tipo_celular='Eucariontes',
    nutricao='Carnívoro',
    nome_filo='Chordata',
    reproducao='Sexuada',
    sono_hab='Diurno',
    locomocao='Voador',
    nome_ordem='Accipitriformes',
    caracterisca_ordem='Aves de rapina',
    nome_familia='Accipitridae',
    caracteristica_familia='Raptores diurnos',
    nome_genero='Haliaeetus',
    caracterisca_genero='Aves de rapina com plumagem distintiva',
    tamanho_corporal='Grande',
    tipo_camuflagem='Plumagem branca na cabeça'
)

banco_de_dados['Tucano'] = Especie(
    tipo_celular='Eucariontes',
    nutricao='Omnívoro',
    nome_filo='Chordata',
    reproducao='Sexuada',
    sono_hab='Diurno',
    locomocao='Voador',
    nome_ordem='Piciformes',
    caracterisca_ordem='Aves com bico serrilhado',
    nome_familia='Ramphastidae',
    caracteristica_familia='Aves com bico colorido',
    nome_genero='Ramphastos',
    caracterisca_genero='Aves com bico colorido',
    tamanho_corporal='Pequeno',
    tipo_camuflagem='Cores vibrantes'
)

banco_de_dados['Tubarão Branco'] = Especie(
    tipo_celular='Eucariontes',
    nutricao='Carnívoro',
    nome_filo='Chordata',
    reproducao='Sexuada',
    sono_hab='Diurno',
    locomocao='Nadador',
    nome_ordem='Lamniformes',
    caracterisca_ordem='Peixes cartilaginosos',
    nome_familia='Lamnidae',
    caracteristica_familia='Maior predador marinho',
    nome_genero='Carcharodon',
    caracterisca_genero='Predadores marinhos temidos',
    tamanho_corporal='Grande',
    tipo_camuflagem='Ausente'
)

banco_de_dados['Orangotango'] = Especie(
    tipo_celular='Eucariontes',
    nutricao='Frugívoro',
    nome_filo='Chordata',
    reproducao='Sexuada',
    sono_hab='Diurno',
    locomocao='Quadrúpede',
    nome_ordem='Primates',
    caracterisca_ordem='Mamíferos primatas',
    nome_familia='Hominidae',
    caracteristica_familia='Parentes próximos dos humanos',
    nome_genero='Pongo',
    caracterisca_genero='Primatas arborícolas da Indonésia',
    tamanho_corporal='Grande',
    tipo_camuflagem='Ausente'
)

banco_de_dados['Lobo'] = Especie(
    tipo_celular='Eucariontes',
    nutricao='Carnívoro',
    nome_filo='Chordata',
    reproducao='Sexuada',
    sono_hab='Noturno',
    locomocao='Quadrúpede',
    nome_ordem='Carnivora',
    caracterisca_ordem='Carnívoros terrestres',
    nome_familia='Canidae',
    caracteristica_familia='Predadores de médio a grande porte',
    nome_genero='Canis',
    caracterisca_genero='Canídeos sociais e caçadores habilidosos',
    tamanho_corporal='Médio',
    tipo_camuflagem='Cinza com manchas'
)

banco_de_dados['Girafa'] = Especie(
    tipo_celular='Eucariontes',
    nutricao='Herbívoro',
    nome_filo='Chordata',
    reproducao='Sexuada',
    sono_hab='Diurno',
    locomocao='Quadrúpede',
    nome_ordem='Artiodactyla',
    caracterisca_ordem='Mamíferos ungulados com cascos pares',
    nome_familia='Giraffidae',
    caracteristica_familia='Pescoço longo e pernas compridas',
    nome_genero='Giraffa',
    caracterisca_genero='Mamíferos com pescoço longo',
    tamanho_corporal='Grande',
    tipo_camuflagem='Manchas irregulares'
)

banco_de_dados['Gorila'] = Especie(
    tipo_celular='Eucariontes',
    nutricao='Herbívoro',
    nome_filo='Chordata',
    reproducao='Sexuada',
    sono_hab='Diurno',
    locomocao='Quadrúpede',
    nome_ordem='Primates',
    caracterisca_ordem='Mamíferos primatas',
    nome_familia='Hominidae',
    caracteristica_familia='Parentes próximos dos humanos',
    nome_genero='Gorilla',
    caracterisca_genero='Grandes primatas herbívoros',
    tamanho_corporal='Grande',
    tipo_camuflagem='Ausente'
)

banco_de_dados['Tartaruga Verde'] = Especie(
    tipo_celular='Eucariontes',
    nutricao='Herbívoro',
    nome_filo='Chordata',
    reproducao='Sexuada',
    sono_hab='Diurno',
    locomocao='Nadador',
    nome_ordem='Testudines',
    caracterisca_ordem='Répteis com carapaça',
    nome_familia='Cheloniidae',
    caracteristica_familia='Grande nadadora dos oceanos',
    nome_genero='Chelonia',
    caracterisca_genero='Répteis marinhos ameaçados de extinção',
    tamanho_corporal='Grande',
    tipo_camuflagem='Carapaça esverdeada'
)

banco_de_dados['Lince'] = Especie(
    tipo_celular='Eucariontes',
    nutricao='Carnívoro',
    nome_filo='Chordata',
    reproducao='Sexuada',
    sono_hab='Noturno',
    locomocao='Quadrúpede',
    nome_ordem='Carnivora',
    caracterisca_ordem='Carnívoros terrestres',
    nome_familia='Felidae',
    caracteristica_familia='Carnívoros de médio porte',
    nome_genero='Lynx',
    caracterisca_genero='Felinos ágeis e excelentes caçadores',
    tamanho_corporal='Médio',
    tipo_camuflagem='Manchas pontilhadas'
)

banco_de_dados['Pinguim Imperador'] = Especie(
    tipo_celular='Eucariontes',
    nutricao='Carnívoro',
    nome_filo='Chordata',
    reproducao='Sexuada',
    sono_hab='Diurno',
    locomocao='Nadador',
    nome_ordem='Sphenisciformes',
    caracterisca_ordem='Aves marinhas não voadoras',
    nome_familia='Spheniscidae',
    caracteristica_familia='Pinguins gigantes do polo sul',
    nome_genero='Aptenodytes',
    caracterisca_genero='Grandes pinguins antárticos',
    tamanho_corporal='Grande',
    tipo_camuflagem='Plumagem preta e branca'
)

banco_de_dados['Rinoceronte'] = Especie(
    tipo_celular='Eucariontes',
    nutricao='Herbívoro',
    nome_filo='Chordata',
    reproducao='Sexuada',
    sono_hab='Diurno',
    locomocao='Quadrúpede',
    nome_ordem='Perissodactyla',
    caracterisca_ordem='Mamíferos ungulados com cascos ímpares',
    nome_familia='Rhinocerotidae',
    caracteristica_familia='Grandes mamíferos herbívoros com chifres',
    nome_genero='Rhinoceros',
    caracterisca_genero='Mamíferos herbívoros com chifres distintivos',
    tamanho_corporal='Grande',
    tipo_camuflagem='Cinza com rugas'
)

banco_de_dados['Hipopotamo'] = Especie(
    tipo_celular='Eucariontes',
    nutricao='Herbívoro',
    nome_filo='Chordata',
    reproducao='Sexuada',
    sono_hab='Noturno',
    locomocao='Quadrúpede',
    nome_ordem='Artiodactyla',
    caracterisca_ordem='Mamíferos ungulados com cascos pares',
    nome_familia='Hippopotamidae',
    caracteristica_familia='Mamíferos semelhantes a porcos',
    nome_genero='Hippopotamus',
    caracterisca_genero='Gigantes herbívoros semi-aquáticos',
    tamanho_corporal='Grande',
    tipo_camuflagem='Ausente'
)

banco_de_dados['Puma'] = Especie(
    tipo_celular='Eucariontes',
    nutricao='Carnívoro',
    nome_filo='Chordata',
    reproducao='Sexuada',
    sono_hab='Noturno',
    locomocao='Quadrúpede',
    nome_ordem='Carnivora',
    caracterisca_ordem='Carnívoros terrestres',
    nome_familia='Felidae',
    caracteristica_familia='Carnívoros de médio porte',
    nome_genero='Puma',
    caracterisca_genero='Felinos solitários e ágeis',
    tamanho_corporal='Médio',
    tipo_camuflagem='Cor uniforme'
)

banco_de_dados['Suricato'] = Especie(
    tipo_celular='Eucariontes',
    nutricao='Omnívoro',
    nome_filo='Chordata',
    reproducao='Sexuada',
    sono_hab='Diurno',
    locomocao='Quadrúpede',
    nome_ordem='Carnivora',
    caracterisca_ordem='Carnívoros terrestres',
    nome_familia='Herpestidae',
    caracteristica_familia='Parentes das mangustas',
    nome_genero='Suricata',
    caracterisca_genero='Pequenos mamíferos sociais e vigilantes',
    tamanho_corporal='Pequeno',
    tipo_camuflagem='Ausente'
)

banco_de_dados['Quati'] = Especie(
    tipo_celular='Eucariontes',
    nutricao='Omnívoro',
    nome_filo='Chordata',
    reproducao='Sexuada',
    sono_hab='Diurno',
    locomocao='Quadrúpede',
    nome_ordem='Carnivora',
    caracterisca_ordem='Carnívoros terrestres',
    nome_familia='Procyonidae',
    caracteristica_familia='Parentes dos guaxinins',
    nome_genero='Nasua',
    caracterisca_genero='Parentes dos guaxinins, geralmente encontrados em grupos',
    tamanho_corporal='Médio',
    tipo_camuflagem='Rabo listrado'
)

banco_de_dados['Ornitorrinco'] = Especie(
    tipo_celular='Eucariontes',
    nutricao='Carnívoro e herbívoro',
    nome_filo='Chordata',
    reproducao='Oviparidade',
    sono_hab='Diurno e noturno',
    locomocao='Nadador',
    nome_ordem='Monotremata',
    caracterisca_ordem='Mamíferos ovíparos',
    nome_familia='Ornithorhynchidae',
    caracteristica_familia='Mamífero semi-aquático',
    nome_genero='Ornithorhynchus',
    caracterisca_genero='Mamíferos semi-aquáticos ovíparos com bicos de pato e caudas de castor',
    tamanho_corporal='Pequeno',
    tipo_camuflagem='Pele marrom e densa'
)

print("\n----- Banco de dados -----")
while True:
  i = 0

  for key,value in banco_de_dados.items():
    print(f"-({i+1}) - {key}")
    i += 1
  
  escolha = int(input("\n- Escolha o número associado ao animal que deseja: "))

  if escolha > len(banco_de_dados) or escolha < len(banco_de_dados):
    print("\n- Esse animal não está presente no nosso banco de dados!\n")
  else:
    print