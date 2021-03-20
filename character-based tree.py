#input: species and character tables
species = 'Abantias_multifasciata Acanthogonatus_heterolepidotus Acanthogonatus_pardalis Actitis_paradisi Actitis_rufinus Aix_doriae Alloporus_exquisita Alopex_carinata Aphonopelma_exquisita Argynnis_caesius Avicularia_ochropus Boiga_piscator Brachyramphus_proteus Bradypterus_coloratovillosum Branta_cinclus Branta_citrsola Caiman_tarandus Capeila_ferina Casarca_querquedula Castor_yeltoniensis Chamaeleo_rosmarus Charadrius_uncia Crocodylus_sibirica Ctenotus_miliaris Cuora_ammon Cyclagras_boyciana Dasypeltis_calvus Dendrelaphis_acutus Dendrobates_mitratus Erpeton_boa Eublepharis_salei Fregilegus_solitaria Gazella_sibiricus Gerrhosaurus_tenuirostris Grammostola_boyciana Haliaetus_canagica Haliaetus_serricollis Holodactylus_dentata Kaloula_quinquestriatus Lagenorhynchus_sieboldii Leptopelis_clypeatus Mustela_aureostriata Mylopharyngodon_hirundo Ophisops_cambridgei Pandion_ibis Paramesotriton_dolosus Pelodiscus_Bernicla Phelsuma_armata Phormictopus_karelini Physignathus_avinivi Platalea_climacophora Psalmopoeus_bimaculata Pseudorca_rutilans Pterinochilus_peregusna Recurvirostra_japonica Regulus_chuatsi Rosalia_cyanea Sceloporus_caudolineatus Scorpio_milii Selenocosmia_crassidens Sphenops_limosa Spizaetus_jubata Spizaetus_pendulinus Sterna_leucogaster Sus_flavescens Sus_pugnax Sus_rubida Teratoscincus_rostratus Vulpes_hispida'.split()
character = '''100001000000010000010010001000100100010000000100010010011000000000001
100011111110011010110011011101100111111010010110010111011101110111001
111111111110111011111111111111111111111111111111011111111111111111111
111101101111111101111111111111111111011111111111111111111111011011111
111111111110111010111111111111111111111111111111011111111111111111111
011110010111101111001101100010011011101111111001101000100010101101110
000000000000010000010000001000000000000000000000010000000000000000001
110011111111011111110111111111101111111111111110110111111101111111111
001000000000000000001000000000000000000000000000000000000000000000000
000000000001000101000100100010001000000101001000100000100000001000000
000000000000010000010010001000000000000000000000010010000000000000001
000000000010000000000001000000000010000010010000000000000000000000000
111111111111111111111011011111111111111111111111111111111111111111111
000000100000000000000000010000000000000000000010000001000000010010000
111111111111111111111111111111111111111111111111111111111111111111001
000000000000010000000000001000000000000000000000000000000000000000000
111111010111111111111111101011111111111111111101111110111110101101111
111111111111111111111011011101111111111010110111111111011111111111111
111111010111111111111111101010111111111111111101111110111110101101111
100001000000000000000000000000100100010000000100000000011000000000000
110111111111011111110111111111101111111111111111111111111101111111111
100001000000000000000000000000000100000000000000000000000000000000000
000000000000000000000100100010001000000101001000000000100000000000000
000001000000000000000000000000000100000000000000000000000000000000000
111111111111111111111110111111111101111101101111111111111111111111111
100011111110010010110011011101100111111010010110010111011101110111001
111111101111111111111111111111111111011111111111111111111111111111111
000000000000000000000000000000100000010000000000000000001000000000000
111101101111111101111111111111111111010111111111111111111111011011111
000000000000000000000000000010000000000100000000000000000000000000000
111111111111111111111111111111111101111101101111111111111111111111111
000000000000000000000100100000000000000001001000000000100000000000000
000000000001000101000100100010001000000101101000100000100000001000110
111111111111111111111111111111111101111111101111111111111111111111111
111111111111111111111011011111111111111111110111111111011111111111111
111111111111111111111111111111011111101111111011111111100111111111111
000000000000000000000000010000000000000000000010000000000000010000000
111011111111111111111111111111111111111111111110110111111111111111111
000000000000000100000000000000000000000000000000100000000000000000000
000000000000000000010000000000000000000000000000010000000000000000000
111111111111111111111111111111111111111111111110110111111111111111111
111111010111111111111111101010111111111111111101111010111110101101111
111111111111101111101111110111111111111111111111101101111111111111110
111111111111111111111111101111111111111111111101111110111111101101111
111111111111111111111011011111111111111111111111111111011111111111111
000000000000000000000000000000000000000000000100000000010000000000000
000000000000000000000000000000100000000000000000000000001000000000000
011110010111101111101101100010011011101111111001101000100010101101110
110111111111111111110111111111111111111111111111111111111101111111111
000000100000000000000000010000000000000000000010000001000001010010000
000010010000000000000000000000000000100000000000000000000000100100000
000000000000000000000000010000000000000000000000000000000000010000000
111111111110111010111111111111111111111111111111011111111111110111111
111111111111111111111111111111111111111111111111111111111111011011111
111111111011111111111111111111111111111111111111111111111111111110111
000000000000000000000000000000000000000000100000000000000000000000110
011100000111101101001101100010011011000111111001101000100010001001110
111111111111101111111111110111111111111111111111111111111111111111110
011110010111101111101101100010011011101111111001101000100110101101110
111101101111111111111111111111111111011111111111111111111111111111111
111111010111111111111111101111111111111111111101111110111110101101111
000000000000000000000000000000000000000000000000000001000000000010000
011100000001101101001100100010011001000101101001101000100010001000110
000000000110000000000001000000000010000010010000000000000000000001000
101111111110111010111011011101110111111010010111011111011111110111001
110111111111011111110111111111111111111111111111111111111101111111111'''.split()

#manage character tables
char=[]
num1=[]
for c in character:
    n = c.count('1')
    if n > len(c)//2:
        c = c.replace('1','a').replace('0','1').replace('a','0')
    n = c.count('1')
    if n > 1 and c not in char:
        char.append(c)
        num1.append(n)
cha = [x for _,x in sorted(zip(num1,char))][::-1]

#manage taxa based on characters (from large to small)
taxa=[]
for c in cha:
    taxon=[]
    for n in range(len(c)):
        if c[n] == '1':
            taxon.append(species[n])
    g=0
    for t in range(len(taxa)):
        for i in taxon:
            if i in taxa[t]:
                g=1
                break
        if g == 1:
            t2 = []
            for l in taxon:
                if l in taxa[t]:
                    index = taxa[t].index(l)
                    taxa[t][index] = ''
                    t2.append(l)
            taxa[t].insert(index, ")")
            for e in t2:
                taxa[t].insert(index, e)
            taxa[t].insert(index, "(")
            taxa[t] = list(filter(None, taxa[t]))
            break
    if g == 0:
        taxa.append(taxon)

#add remaining species
for i in range(len(cha[0])):
    f=0
    for c in cha:
        if c[i] == '1':
            f=1
            break
    if f == 0:
        taxa.append(species[i])

#output the newick tree
print(str(taxa).replace("'",'').replace("(, ","(").replace(", )",")").replace('[','(').replace(']',')').replace(', ',',')+";")