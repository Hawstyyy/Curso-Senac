from Especie import Especie

def print_master(animal):
    print(f"""
- Tipo celular: {animal.tipo_celular}
- Nutrição: {animal.nutricao}
- Nome do filo: {animal.nome_filo}
- Reprodução: {animal.reproducao}
- Hábito de sono: {animal.sono_hab}
- Locomoção: {animal.locomocao}
- Nome da ordem: {animal.nome_ordem}
- Características da ordem: {animal.caracterisca_ordem}
- Nome da Família: {animal.nome_familia}
- Características da família: {animal.caracteristica_familia}
- Nome do gênero: {animal.nome_genero}
- Característica do gênero: {animal.caracterisca_genero}
- Tamanho Corporal: {animal.tamanho_corporal}""")
    if animal.tipo_camuflagem == 'Ausente':
        pass
    else:
        print(f"- Tipo de Camuflagem: {animal.tipo_camuflagem}")

banco_de_dados = {

'Leão':Especie(
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
),

'Elefante':Especie(
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
),

'Golfinho':Especie(
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
),

'Aguia':Especie(
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
),

'Cobra':Especie(
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
),

'Onça Pintada':Especie(
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
),

'Tigre':Especie(
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
),

'Baleia Azul':Especie(
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
),

'Chimpanze':Especie(
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
),

'Aguia Calva':Especie(
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
),

'Tucano':Especie(
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
),

'Tubarão Branco':Especie(
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
),

'Orangotango':Especie(
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
),

'Lobo':Especie(
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
),

'Girafa':Especie(
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
),

'Gorila':Especie(
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
),

'Tartaruga Verde':Especie(
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
),

'Lince':Especie(
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
),

'Pinguim Imperador':Especie(
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
),

'Rinoceronte':Especie(
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
),

'Hipopotamo':Especie(
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
),

'Puma':Especie(
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
),

'Suricato':Especie(
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
),

'Quati':Especie(
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
),

'Ornitorrinco':Especie(
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
}
while True:
  print("\n---------------------- Nosso banco de dados! ----------------------\n")
  i = 1

  for key,value in banco_de_dados.items():
    print(f"({i}) - {key}")
    i += 1
  
  escolha = int(input("\n\n- Escolha o animal que deseja, pelo número associado! "))

  if escolha > len(banco_de_dados) or escolha <= 0:
    print("\n\n-!!!!!!!!!!!!!!!! Esse animal não está presente no nosso banco de dados e/ou é um número inválido !!!!!!!!!!!!!!!!-\n")

  else:
    i = 1
    for key,value in banco_de_dados.items():
        if i == escolha:
            print(f"\n\n---------------------- Apresentando informações do(a) {key} ----------------------\n")
            print_master(value)
            print()
            break
        else:
            i += 1
