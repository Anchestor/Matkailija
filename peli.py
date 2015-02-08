# (c) Arna Hyvarinen 2015
# Yhteistyo ja lahteet: Ohjelmointiopas

# MATKALAINEN

import random
import sys

class PelaajaTiedot():
    rahat = 0
    inventory = []
    asusteet = []
    arvoitusluku = 0
    questnro = 0
    questvalmius = 'valmis'
    lammella = []

def loppu(pelaaja):
        print('1) Aloita seikkaileminen alusta\n2) Haahuile vapaasti\n3) Aloita peli alusta\n4) Lopeta peli.')
        valinta = input('Valintasi: ')
        if valinta == '1':
            pelaaja.questnro = -1
            pelaaja.questvalmius = 'valmis'
            tori(pelaaja)
        elif valinta == '2':
            metsa(pelaaja)
        elif valinta == '3':
            del pelaaja
            pelaaja = PelaajaTiedot()
            metsa(pelaaja)
        elif valinta == '4':
            print('Kiitos pelaamisesta, toivottavasti sinulla oli kivaa!\n Credits: Arna Hyvarinen 2015')
            sys.exit(0)
        else:
            print('Åläs yritä.')
            metsa(pelaaja)

def onkoSinulla(pelaaja, etsitty):
    monesko = 'ei ole'
    for i in range(0, len(pelaaja.inventory)):
        if pelaaja.inventory[i] == etsitty:
            monesko = i
            return monesko

def tori(pelaaja):
    if pelaaja.questvalmius == 'ei valmis':
        print('Torilla ei ole ketään.')
        kyla(pelaaja)
    quest = ['Kauppamatkustajan ongelma', 'Luuta ja nahkaa', 'Hyväksi hampaille', 'Dam di dam rakkaalleni', 'Prinsessa pulassa', 'Linnansa vanki', 'Omnomnom', 'Baarikärpänen', 'Päänuotti, sydännuotti, perusnuotti', 'Prinsessa pulassa (taas..)', 'Tyylinsä kullakin', 'Päätön juttu', 'Isistä parhain']
    questteksti1 = ['"Oi-joi. Lupasin koota tohtorille luurangon. Enää tarvitsisin pääkallon.\nHei sinä! Saat aimo palkkion, jos löydät minulle pääkallon ja tuot sen kaivolle!"',\
                    'Se katsoo sinua nälkeisenä ja löntystelee kaivolle.', \
                    '"Terrrvehdys, ihminen... Sssaat olla ilonen, että hampaani ovat kipuisssat, muuten sssöisin sssinut... Tai lähtisssin kotiin itään...\nEhkä kaivon kylmä vesssi turrrrrruttaaa..."', \
                   '"Voih, rakkaaani on vihainen. Hänet lepyttääkseni tarvitsisin kauniin kukkakinmpun,\nenkä minä tiedä, mistä löytäisin edes rumia kukkia.\nVoitko auttaa? Tule kaivolle, jos löydät jotain, saat kyllä vastineeksi jotain hienoa!"', \
                    '"Niisk. Miksi KAIKILLA on aina jotain hienoja vaatteita, mutta minulla ei ole mitään.\nNo, ehkä joku on jättänyt kaivolle jotain nättiä..."', \
                    '"Hei! Tiesitkö, että metsässä on linna? Sieltä on kuulemma kuulunut outoa melua viime aikoina. Mitähän on tekeillä?"', \
                    '"Hassuja nämä ihmiset. niin paljon ruokaa, muttei mitään hyvää! Ja kaivoistakin saa vain vettä. Hmm.. Vettä..."', \
                    '"Gnääh. Sarsaparilla on hyvää, mutta pitemmän päälle se on tylsää. No, ainakin kaivolla on vettä."', \
                    '"Argh! Koko päivä pitää lapata lantaa ja hyysätä hevosia, voisi kuvitella, että kun hommat on hoidettu, voisi rentoutua, vaan EI!\nHaju roikkuu ihossa, haju roikkuu vaatteissa, haju roikkuu mielessä!\nKuinka mun pitäisi tehdä mitään, kun tallin lemu roikkuu mukana!\nJa mä pesen ja pesen, mutta se ei auta! Ei vain auta!\nNo, ei kai muutakaan voi. Ja eikun kaivolle..."', \
                    '"Voi ei! Kadotin tiarani! Sinä! Matkalainen! Etsi minulle tiara! Jos epäonnistut, heitän sinut vankilaan!"', \
                    '"Ugh. Nättiä? Vaimolle.. Hääpäivä... Hörkh. Jano..."', \
                    '"Ugh. Käytännöllistä? Miehelle.. Hääpäivä... Hörkh. Jano..."', \
                    '"Anteeksi, muukalainen, mutta onko teillä jotakin lääkettä? Tai parantavia yrttejä?\nLapseni on sairas... Jospa kaivolla on joku, jolla on rohtoa.."']
    questhenkilo = ['kauppamatkustaja',  'koira', 'mantikori', 'nuorukainen', 'pikkutyttö', 'kyläläinen', 'keijukainen', 'huru-ukko', 'pahanhajuinen tallipoika', 'prinsessa', 'peikko', 'toinen peikko', 'isä']
    pelaaja.questvalmius = 'ei valmis'
    try:
        print('Seuraava seikkailusi on:', quest[pelaaja.questnro])
        print('Vastaan tulee ' + questhenkilo[pelaaja.questnro] + '.')
        print(questteksti1[pelaaja.questnro])
        print('Palaat keskustaan.')
        kyla(pelaaja)
    except IndexError:
        print('Olet suorittanut kaikki seikkailut.')
        pelaaja.questvalmius == 'valmis'
        loppu(pelaaja)
    
def kaivo(pelaaja):
    if pelaaja.questvalmius == 'valmis':
        print('Kaivolla ei ole ketään.')
    else:
        questhenkilo = ['kauppamatkustaja',  'koira', 'mantikori', 'nuorukainen', 'pikkutyttö', 'kyläläinen', 'keijukainen', 'huru-ukko', 'pahanhajuinen tallipoika', 'prinsessa', 'peikko', 'toinen peikko', 'isä']
        questitem = ['pääkallo', 'luu', 'maito', 'kukkakimppu', 'voikukkaseppele', 'LINNA', 'karkkia', 'seljajuoma', 'parfyymi', 'tiara', 'luukoru', 'barbaariastiasto', 'kuuliljauute']
        questteksti2 = ['"Löysitkö sen kallon?"', \
                        '"Vuh?"', \
                        '"Terrrvehdys, ihminen... Onkosss sssinulla jotain minulle?"', \
                        '"Voi, mitä minä teen! Ai sinä! Ei sinulla olisi kukkia?"', \
                        '"Hei. Onko sinulla mitään nättiä?"', \
                        '"Hei taas! Kuulitko mitään?"', \
                        '"Hie! Onkos sinulla mitää hyvää, hassu ihminen?"', \
                        '"Onko sinulla mitään juotavaa?"', \
                        'Hajun pahin terä on taittunut. Hän kaataa ämpäristä vettä niskaana.\n"Mitä nyt? Onko sulla asiaa?"', \
                        '"Löysitkö sen tiaran?"', \
                        '"Orhrk. Nättiä?"', \
                        '"Orhrk. Käytännöllistä?"', \
                        '"Anteeksi, onko teillä jotakin lääkettä?"']
        questtekstikylla = ['"Mahtavaa! Tässä se huima palkkiosi: 6 rahaa! Älä käytä kaikkea kerralla!"', \
                            'Koira ottaa luun ja alkaa järsiä sitä innoissaan. Se lönkittelee pois, mutta sen kaulasta tippuu nahkapussukka.', \
                            '"Kiitosss, ihminen... Tässstä hyvässstä en sssyö sssinua... Tässssssä, sssaat tämän helmen..."', \
                            '"Oi ihanuus! Tässä, saat kiitokseksi tämän kauniin meripihkan palan!\nNyt rakkaani kyllä antaa minulle anteeksi, että unohdin hänen lempivärinsä!"', \
                            '"Voi jee! Kiitoskiitoskiios! Saat tämän kaarnaveneen, minä tein sen ihan itse!"', \
                            'LINNA', \
                            '"Hmm. ihan makoisia nämä \'karkit\'. Tässä - saat 18 rahaa? Vaikka mitä ihmettä te tuolla teettekään."', \
                            '"Jes! Tässä, saat.. öö... Suolaa! Palkkioksi!"', \
                            '"OOH, tää tuoksuu niin hyvälle! Tulee se keltasia luumuja myyvä typy mieleen. Tiiäks, se nätti? Hei kiitti! Täs, 25 rahaa!"', \
                            '"Hienoa! Juuri ajoissa ennen seremoniaa! Tässä ruhtinaallinen palkkiosi: kuulilja! Sillä on parantavia vaikutuksia..."', \
                            '"Uörkh! Rubiini!"', \
                            '"Uörkh! Kukkakimppu!"', \
                            '"Oi, kiitos! Minulla ei ole paljon, mutta tämä helmi on arvokkainta mitä minulla on. Ota se maksuksi!"']
        questtekstiei = ['"Älä sitten tuhlaa aikaani!"', \
                         '"Vuh..."', \
                         '"No, menesss sssitten sssiitä..."', \
                         '"Voi ei, voi ei, voi ei! Mitä minä teen!"', \
                         '"No, ei sitten..."', \
                         '"Ai, no ei sitten."', \
                         '"Ai."', \
                         '"Höh."', \
                         '"No suksi kuuseen sitten!"\nTallipoika kaataa', \
                         '"Älä sitten tuhlaa aikaani!"', \
                         '"Öörkh!"', \
                         '"Öörkh!"', \
                         '"Ai, no ei sitten.."']
        questpalkkio = [6, 'nahkapussukka', 'helmi', 'meripihkanpala', 'kaarnavene', 'LINNA', 18, 'merisuolaa', 25, 'kuulilja', 'rubiini', 'kukkakimppu', 'helmi']
        print(questhenkilo[pelaaja.questnro].capitalize(), 'on kaivolla.')
        print(questteksti2[pelaaja.questnro])
        print('1) Kyllä\n2) Ei')
        valinta = input('Valintasi: ')
        if valinta == '2':
            print(questtekstiei[pelaaja.questnro])
        elif valinta == '1':
            monesko = onkoSinulla(pelaaja, questitem[pelaaja.questnro])
            try:
                del pelaaja.inventory[monesko]
                print(questtekstikylla[pelaaja.questnro])
                if isinstance(questpalkkio[pelaaja.questnro], str) == True:
                    pelaaja.inventory.append(questpalkkio[pelaaja.questnro])
                    pelaaja.inventory.sort()
                    pelaaja.questvalmius = 'valmis'
                    pelaaja.questnro = pelaaja.questnro + 1
                else:
                    pelaaja.rahat = pelaaja.rahat + pelaaja.questpalkkio[pelaaja.questnro]
                    pelaaja.questvalmius = 'valmis'
                    pelaaja.questnro = pelaaja.questnro + 1
            except TypeError:
                print('Sinulla ei ole, mitä tarvitaan. Palaat kylään.')
                kyla(pelaaja)
        else:
            print('Annas olla.')
            kaivo(pelaaja)

def kaupanteko(pelaaja, kauppiaalla):
    hinta = kauppiaalla[-1]
    del kauppiaalla[-1]
    print('"Tervehdys, matkalainen! Kaipaaisitteko jotain? Minulta löytyisi:')
    print(kauppiaalla)
    print('... ja kaikki maksaa', hinta, ' rahaa"')
    print('Sinulla on nyt', pelaaja.inventory, 'ja', pelaaja.rahat, 'rahaa.')
    while True:
        print('1) En osta mitään!\n2) Ostan!')
        valinta = input('Valintasi: ')
        if valinta == '1':
            break
        elif valinta == '2':
            ostos = input('"Mitä saisi olla?" ')
            if ostos in kauppiaalla:
                if pelaaja.rahat - hinta >= 0:
                    pelaaja.inventory.append(ostos)
                    pelaaja.inventory.sort()
                    pelaaja.rahat = pelaaja.rahat - hinta
                    print('Sinulla on nyt', pelaaja.inventory, 'ja', pelaaja.rahat, 'rahaa.')
                else:
                    print('"Sori, kaveri. Meillä ei tingitä. Mutta saisiko olla jotain muuta?"')
            else:
                print('"Eipä taida löytyä... Saisiko olla jotain muuta?"')
        else:
            print('"Häh?"')
    return pelaaja
           
def kaupanVarastot(pelaaja):
    varasto1 = ['kehäkukka', 'luu', 3]
    varasto2 = ['vesililja', 'sarvi', 7]
    varastot = [varasto1, varasto2]
    kauppiaalla = random.choice(varastot)
    kaupanteko(pelaaja, kauppiaalla)

def kauppamatkustajanVarastot(pelaaja):
    varasto1 = ['karkkia', 'hammas', 4]
    varasto2 = ['ruusu', 'sarvi', 5]
    varastot = [varasto1, varasto2]
    kauppiaalla = random.choice(varastot)
    kaupanteko(pelaaja, kauppiaalla) 

def myynti(pelaaja):
    halpa = ['voikukka', 'pääkallo', 'maito']
    keski = ['ruusu', 'vesililja', 'hammas', 'selja', 'kehäkukka', 'karkkia', 'merisuolaa', 'pähkinöitä']
    kallis = ['kukkakimppu', 'nahkapussukka', 'meripihkanpala', 'kaarnavene','voikukkaseppele', 'seljajuoma', 'luukoru', 'barbaariastiasto', 'pähkinäöljy']
    tosikallis = ['timantti', 'kuulilja', 'helmi', 'rubiini', 'parfyymi']
    hyvinkallis = ['tiara', 'kuuliljauute']
    print('Sinulla on:', pelaaja.inventory, 'ja', pelaaja.rahat, 'rahaa.')
    myydaan = input('Mikä on se, jonka haluat myydä? ')
    if myydaan in halpa:
        hinta = 2
    elif myydaan in keski:
        hinta = 5
    elif myydaan in kallis:
        hinta = 30
    elif myydaan in tosikallis:
        hinta = 50
    elif myydaan in hyvinkallis:
        hinta = 250
    else:
        hinta = 7
    print('"Hmm.. saat', hinta, 'rahaa."')
    print('Jatketaanko?')
    print('1) Kyllä\n2) Ei')
    valinta = input('Valintasi: ')
    if valinta == '2':
        print('"Myytkö sitten jotain muuta?"')
        print('1) Kyllä\n2) Ei')
        valinta = input('Valintasi: ')
        if valinta == '1':
            myynti(pelaaja)
        elif valinta == '2':
            print('"Kiitos käynnistä, tervetuloa uudelleen!"')
            kyla(pelaaja)
    monesko = onkoSinulla(pelaaja, myydaan)
    try:
        del pelaaja.inventory[monesko]
        pelaaja.rahat = pelaaja.rahat + hinta
    except TypeError:
        print('"Et voi myydä jotain, mitä sinulla ei ole!"')
    print('"Myytkö vielä jotain?"')
    print('1) Kyllä\n2) Ei\n0) Mitäs minulla on taskuissani?')
    valinta = input('Valintasi: ')
    if valinta == '2':
        print('"Kiitos käynnistä, tervetuloa uudelleen!"')
        kyla(pelaaja)
    elif valinta == '1':
        myynti(pelaaja)
    elif valinta == '0':
        print('Sinulla on:', pelaaja.inventory)
        myynti(pelaaja)
    else:
        print('Älä yritä.')
        kauppa(pelaaja)

def kauppa(pelaaja):
    print('Astut kauppaan.')
    print('Haluatko ostaa vai myydä?')
    print('1) Ostaa\n2) Myydä\n3) Antaa olla\n0) Mitäs minulla on taskuissani?')
    valinta = input('Valintasi: ')
    if valinta == '1':
        kaupanVarastot(pelaaja)
    elif valinta == '2':
        print('"Tervehdys, matkalainen! Myyntipuuhissa vai?"')
        myynti(pelaaja)
    elif valinta == '3':
        print('"Yrittäisit päättää.."')
        kyla(pelaaja)
    elif valinta == '0':
        print('Sinulla on', pelaaja.inventory, 'ja', pelaaja.rahat, 'rahaa.')
    else:
        print('Älä yritä.')
        kauppa(pelaaja)

def itemencounter(pelaaja):
    useat = ['pääkallo', 'voikukka']
    harvat1 = ['selja', 'hammas']
    harvat2 = ['pähkinöitä']
    items = [useat, useat, harvat1, harvat2]
    loytyy = random.choice(random.choice(items))
    print('Puskasta löytyy ' + loytyy + '.')
    pelaaja.inventory.append(loytyy)
    pelaaja.inventory.sort()

def luola(pelaaja):
    if 'lyhty' not in pelaaja.asusteet:
        print('Luolassa on niin pimeää, ettet näe mitään. Menet ulos.')
        metsa(pelaaja)
    kamat1 = ['sarvi', 'kukkakimppu']
    kamat2 = ['nahkapussukka']
    kamat3 = ['kaarnavene']
    kamat4 = ['merisuolaa']
    kamat = [kamat1, kamat2, kamat3, kamat4]
    loytyy = random.choice(kamat)
    print('Luolasta löytyy:', loytyy)
    for esine in loytyy:
        pelaaja.inventory.append(esine)
        pelaaja.inventory.sort()
    return pelaaja

def vaihtokauppa(pelaaja, annetaan, saadaan, teksti):
    monesko = onkoSinulla(pelaaja, annetaan)
    try:
        del pelaaja.inventory[monesko]
        pelaaja.inventory.append(saadaan)
        pelaaja.inventory.sort()
        print(teksti)
        metsa(pelaaja)
    except TypeError:
        print('Et voi antaa jotain, mitä sinulla ei ole!')

def menninkainen(pelaaja, hinta):
    print('1) Ei\n2) Kyllä\n0) Mitäs minulla on taskuissani?')
    valinta = input('Valintasi: ')
    if valinta == '2':
        pelaaja.rahat = pelaaja.rahat - hinta
        lista = ['helmi', 'meripihkanpala', 'nahkapussukka', 'kaarnavene']
        for esine in lista:
            pelaaja.inventory.append(esine)
        print('"Jipii! Jipii! Nyt minä saan rahaa!"')
        metsa(pelaaja)
    elif valinta == '1':
        print('"No möh. Älä sitten osta!"')
        metsa(pelaaja)
    elif valinta == '0':
        print('Sinulla on', pelaaja.inventory, 'ja', pelaaja.rahat, 'rahaa.')
        print('"NO, ostatko!?"')
        menninkainen(pelaaja, hinta)
    else:
        print('Älä yritä.')

def peikko(pelaaja):
    print('1) Ei\n2) Kyllä\n0) Mitäs minulla on taskuissani?')
    valinta = input('Valintasi: ')
    if valinta == '2':
        print('"Kumpi?"')
        print('1) Nahkapussukka\n2) Kaarnavene\n3) Antaa olla..')
        valinta = input('Valintasi: ')
        if valinta == '3':
            print('"Hyvä on..."')
            metsa(pelaaja)
        elif valinta == '1':
            annetaan = 'nahkapussukka'
        elif valinta == '2':
            annetaan = 'kaarnavene'
        else:
            print('Annas olla.')
            haltia(pelaaja)
        saadaan = 'timantti'
        teksti = '"Uörgh!"'
        vaihtokauppa(pelaaja, annetaan, saadaan, teksti)
        metsa(pelaaja)
    elif valinta == '1':
        print('"Urk."')
        metsa(pelaaja)
    elif valinta == '0':
        print('Sinulla on', pelaaja.inventory, 'ja', pelaaja.rahat, 'rahaa.')
        peikko(pelaaja)
    else:
        print('Annas olla.')
        metsa(pelaaja)

def haltia(pelaaja):
    print('1) Ei\n2) Kyllä\n0) Mitäs minulla on taskuissani?')
    valinta = input('Valintasi: ')
    if valinta == '2':
        print('"No, mitä sinulla on?"')
        print('1) Meripihkanpala\n2) Helmi\n3) Antaa olla..')
        valinta = input('Valintasi: ')
        if valinta == '3':
            print('"Hyvä on..."')
            metsa(pelaaja)
        elif valinta == '1':
            annetaan = 'meripihkanpala'
        elif valinta == '2':
            annetaan = 'helmi'
        else:
            print('Annas olla.')
            haltia(pelaaja)
        saadaan = 'kuulilja'
        teksti = '"Kiitos, kuolevainen..."'
        vaihtokauppa(pelaaja, annetaan, saadaan, teksti)
        metsa(pelaaja)
    elif valinta == '1':
        print('"Hyvä on..."')
        metsa(pelaaja)
    elif valinta == '0':
        print('Sinulla on', pelaaja.inventory, 'ja', pelaaja.rahat, 'rahaa.')
        haltia(pelaaja)
    else:
        print('Annas olla.')
        metsa(pelaaja)

def sfinksi(pelaaja):
    vastaukset = ['avain', 'noppa', 'onni', 'sumu', 'varjo', 'kynttilä', 'muna', 'tuli']
    arvoitukset = ['Ei voimalla pysty saavuttamaan\nsitä minkä kevyesti aikaan saan\nmoni jäisi kadulle seisomaan\nellei löytyisi minua auttamaan.\nMikä minä olen?"', \
                   'Minulla on 21 silmää, mutta en näe.\nMikä minä olen?"', \
                   'Minua etsii jokainen\nvaan jos minut löytää\nharva huomaa sen.\nMikä minä olen?"', \
                   'Täyttyy siitä onkalo,\nlaakso, mäki, maa\nkulhon täyttä sitä et\nsilti koskaan saa.\nMikä minä olen?"', \
                   'Värejä vain yksi, koko vaihtelee maassa on kiinni, silti lentelee\nluonasi on paistesäällä sateella ei näy\ntuskaa se ei tunne eikä haitaksikaan käy.\nMikä se on?"', \
                   'Anna tyttö pienoinen\nalushame valkoinen\nja nenä punainen\nmitä pidempään hän seisoskelee\nsitä enemmän hän lyhenee. Mikä se on?"', \
                   'Sisällä seinien maidonvalkoisten\njoita sisält\' verhoo silkki pehmoinen\nkeskellä lähdettä kristallinkirkasta syntyy kultainen, kaunis omena.\nVaikka tähän holviin ovia ei lie\nvarkaat sisään murtautuu ja sieltä kullan vie.\nMikä minä olen?"', \
                   'Anna minulle ruokaa, niin elän\nanna minulle vettä, niin kuolen.\nMikä minä olen?"']
    palkinnot = ['avain', 'noppa', 'jäniksenkäpälä', 'usvahelmi', 'obsidiaanikorvakorut', 'lyhty', 'lohikäärmeenmuna', 'liekinheitin']
    print('"Tervehdys, kuolevainen. Jos osaat vastata arvoitukseeni, saat palkinnon.')
    try:
        print(arvoitukset[pelaaja.arvoitusluku])
    except IndexError:
        print('Vaan kas! Sinä tunnetkin jo kaikki arvoitukseni No, menehän sitten tiehesi..."')
        metsa(pelaaja)
    vastaus = input('Mitä vastaat? ')
    if vastaus == vastaukset[pelaaja.arvoitusluku]:
        pelaaja.asusteet.append(palkinnot[pelaaja.arvoitusluku])
        print('"Hämmästyttävää! Vastasit oikein! Palkintosi on ' + palkinnot[pelaaja.arvoitusluku] + '."')
        pelaaja.arvoitusluku = pelaaja.arvoitusluku + 1
        metsa(pelaaja)
    else:
        print('"Vastasit väärin, kuten saattoi odotaa.\nMutta en taida syödä sinua, vatsani on vielä täysi edellisestä seikkailiasta..."')
        metsa(pelaaja)

def linna(pelaaja):
    if 'avain' in pelaaja.asusteet:
        print('Linnan ovet avautuvat naristen.\nAstut suureen halliin.')
        print('Edessäsi seisöö velho.')
        print('"KUKA USKALTAA HÄIRITÄ MAJANI RAUHAA?\nÄh, anteeksi. Olen ollut viime aikona nuhainen, ja se saa minut kärttyisäksi.\n'\
              'Tuo typerä tuulimylly vain aiheuttaa niin paljon melua! Tekisi mieli räjäyttää koko höttelö."')
        print('Velhon huitoessa sanojensa painoksi hänen sauvastaan lennähtää tulipallo, joka lentää ikkunasta ulos ja sytyttää tuulimyllyn tuleen.')
        print('1) Huomauta asiasta\n2) Pysy vaiti')
        valinta = input('Valintasi: ')
        if valinta == '1':
            print('"Ai mitä? OHO!"\nVelho lähettää sauvastaan vesipallon, joka sammuttaa tulen, vaikka vahingoilta ei enää voikaan välttyä.\n"Kiitos, kun sanoit, muuten joku olisi saattanut suuttua.')
        elif valinta == '2':
            print('Tuulimylly palaa loimottaen.\n"Oho. Öö. Tuota, voisitko olla kertomatta kenellekkään? Ainakaan heti?')
        print('Kuule, saat tämän sormuksen! Löysin sen yhdestä luolasta."')
        print('Velho lähtee mumisten.\n"Pitää varmaan muuttaa.."\nKun lähdet linnasta ja käännyt katsomaan taaksesi, näet, kun linna ja se mitä tuulimyllystä on jäljellä häviävät.')
        monesko = onkoAsustetta(pelaaja, 'avain')
        del pelaaja.asusteet[monesko]
        pelaaja.asusteet.append('sormus')
        pelaaja.questvalmius = 'valmis'
        pelaaja.questnro = pelaaja.questnro + 1
        metsa(pelaaja)
    else:
        print('Linnan ovet ovat lukossa.')
        metsa(pelaaja)

def tuulimylly(pelaaja):
    print('Löydät myllystä 3 rahaa.')
    pelaaja.rahat = pelaaja.rahat + 3
    metsa(pelaaja)


def huipulla(pelaaja):
    print('1) Pudota jotain laavaan\n2) Lähde pois\n0) Mitäs minulla on taskuissani?')
    valinta = input('Valintasi: ')
    if valinta == '1':
        esine = input('Mitä haluat pudottaa? ')
        if esine in pelaaja.inventory:
            monesko = onkoSinulla(pelaaja, esine)
            del pelaaja.inventory[monesko]
            print('Katsot, kun', esine, 'putoaa laavaan.')
            huipulla(pelaaja)
        elif esine in pelaaja.asusteet:
            monesko = onkoAsustetta(pelaaja, esine)
            del pelaaja.asusteet[monesko]
            if esine == 'obsidiaanikorvakorut':
                print('Heti kun riisut korvakorut, laavan hohkaava kuumuus käy sietämättömäksi. Puet ne heti takaisin')
                pelaaja.asusteet.append('obsidiaanikorvakorut')
                huipulla(pelaaja)
            print('Katsot, kun', esine, 'putoaa laavaan.')
            if esine == 'sormus':
                print('Kaukaisuudessa siintää pahaenteinen torni. Sormuksen sulaessa laavaan se sortuu.')
                huipulla(pelaaja)
            elif esine == 'lohikäärmeenmuna':
                print('Hetken kuluttua laavasta syöksyy pieni lohikäärme. Se lentää pois.')
                huipulla(pelaaja)
        else:
            print('Et voi luopua jostain, mitä sinulla ei ole!')
            huipulla(pelaaja)
    elif valinta == '2':
        metsa(pelaaja)
    elif valinta == '0':
        print('Sinulla on', pelaaja.inventory, 'ja', pelaaja.rahat, 'rahaa.')
        print('Sinulla on ylläsi ' + pelaaja.asusteet + '.')
        huipulla(pelaaja)

def tulivuori(pelaaja):
    print('Kiipeatkö vuorelle?')
    print('1) Ei\n2) Kyllä\n0) Mitäs minulla on taskuissani?')
    valinta = input('Valintasi: ')
    if valinta == '2':
        if 'obsidiaanikorvakorut' in pelaaja.asusteet:
            print('Obsidiaanikorvakorusi välähtävät punaisina. Laava tunnistaa laavan.\nVoit jatkaa.')
            if 'sormus' in pelaaja.asusteet:
                for i in range (1,4):
                    jatkaa = random.randint(1,4)
                    if jatkaa == 1:
                        print('Sormus ylläsi käy liian raskaaksi. Joudut palaamaan takaisin.')
                        metsa(pelaaja)
                    else:
                        print('Kiipeät vuorelle, yhä ylemmäs')
            else:
                for i in range (1,4):
                    print('Kiipeät vuorelle, yhä ylemmäs')
            print('Saavut suurelle oviaukolle. Alhaalla hohkaa laava.')
            huipulla(pelaaja)
        else:
            print('Laava hohkaa liian kuumana. Joudut kääntypään takaisin.')
            metsa(pelaaja)
    elif valinta == '1':
        metsa(pelaaja)
    elif valinta == '0':
        print('Sinulla on', pelaaja.inventory, 'ja', pelaaja.rahat, 'rahaa.')
        tulivuori(pelaaja)
    else:
        print('Annas olla.')
        tulivuori(pelaaja)

def notko(pelaaja):
    print('1) Mene pois\n2) Mene pesään\n0) Mitäs minulla on taskuissani?')
    valinta = input('Valintasi: ')
    if valinta == '2':
        print('Pesässä makaa nukkuva lohikäärme rahakasan päällä.')
        heraako = random.randint(1, 10)
        if heraako == 1:
            print('Lohikäärme herää ja ajaa sinut metsään.')
            metsa(pelaaja)
        else:
            print('Otatko rahaa?')
            print('1) Kyllä\n2) Ei')
            valinta = input('Valintasi: ')
            if valinta == '1':
                while True:
                    try:
                        paljonko = int(input('Paljonko? '))
                        if paljonko < 0:
                            print('Anna positiivinen luku!')
                            paljonko = int(input('Paljonko? '))
                        else:
                            break
                    except ValueError:
                        print('Anna luku!')
                if paljonko > 128:
                    print('Kahmaiset niin paljon rahaa, että kolikoiden kilinä herättää lohikäärmen.\nSe ajaa sinut pois.')
                    metsa(pelaaja)
                else:
                    pelaaja.rahat = pelaaja.rahat + paljonko
                    print('Lähdet, ennen kuin lohikäärme herää.')
                    metsa(pelaaja)
            elif valinta == '2':
                loytyy = random.choice(['kuulilja', 'timantti'])
                print('Hiivit ulos. Lähtiessäsi notkosta palaneiden ohdakkeiden juuresta löytyy ' + loytyy + '.')
                pelaaja.inventory.append(loytyy)
                pelaaja.inventory.sort()
                metsa(pelaaja)
            else:
                print('Älä yritä.')
                notko(pelaaja)
    elif valinta == '1':
        print('Lähdet notkosta.')
        if ('kukkakimppu' and 'seljajuoma' and 'voikukkaseppele') in pelaaja.inventory:
            print('Lähtiessäsi kuulet oudon äänen.\nKun käännyt katsomaan, notkoon on ilmestynyt suuri, sininen laatikko, josta astuu ulos '\
                  'rusettikaulainen mies\npunatukkaisen nuoren naisen ja nuoren, huolestuneen näköisen miehen kanssa.\nHe katselevat hieman ympärilleen. '\
                  'Nuori mies sanoo kahdelle muulle jotain,\njosta et saa selvää ja vetää heidät takaisin laatikkoon heidän vastustellessaan. '\
                  '\nPian laatikko haipuu ilmaan oudon äänen saattelemana.')
        metsa(pelaaja)
    elif valinta == '0':
        print('Sinulla on', pelaaja.inventory, 'ja', pelaaja.rahat, 'rahaa.')
        notko(pelaaja)
    else:
        print('Älä yritä.')
        notko(pelaaja)

def mordor(pelaaja):
    kamat = []
    arvoituspalkinnot = ['noppa', 'jäniksenkäpälä', 'lyhty']
    for esine in arvoituspalkinnot:
        if esine not in pelaaja.asusteet:
            kamat.append(esine)
    if len(kamat) == 0:
        print('Löydät timantin ja kuuliljan.')
        pelaaja.inventory.append('timantti')
        pelaaja.inventory.append('kuulilja')
        pelaaja.inventory.sort()
        metsa(pelaaja)
    else:
        print('Löydät vajan, jossa on tarvikkeita:', kamat)
        for esine in kamat:
            pelaaja.asusteet.append(esine)
        metsa(pelaaja)

def lampi(pelaaja):
    halpa = ['voikukka', 'pääkallo', 'ruusu', 'vesililja', 'hammas', 'selja', 'kehäkukka']
    if len(pelaaja.lammella) != 0:
        if pelaaja.lammella[0] == 'rubiini':
            del pelaaja.lammella[0]
            print('Vesinymfi istuu rantakivellä pyöritellen rubiinia käsissään. Hän hymyilee sinulle arvoituksellisesti.')
            print('"Me olemme antaneet toisillemme niin hienoja lahjoja, mutta mitään näin hienoa minulla ei ole antaa.\nPaitsi tämä salaisuus: Se lohikäärmeenmuna. Ne syntyvät tulesta. Vie se kotiin. Vie se laavaan."')
            print('Vesinymfi sukeltaa veteen.')
            metsa(pelaaja)
        elif pelaaja.lammella[0] in halpa:
            loytyy = 'meripihkanpala'
        else:
            loytyy = 'helmi'
        print('Rannasta löytyy ' + loytyy + '.')
        del pelaaja.lammella[0]
        metsa(pelaaja)
    print('1) Heitä jotain lampeen\n2) Lähde\n0) Mitäs minulla on taskuissani?')
    valinta = input('Valintasi: ')
    if valinta == '1':
        mika = input('Mitä haluat heittää? ')
        if mika in pelaaja.inventory:
            monesko = onkoSinulla(pelaaja, mika)
            del pelaaja.inventory[monesko]
            print('Järvestä nousee käsi, joka ottaa kopin.')
            pelaaja.lammella.append(mika)
        else:
            print('Et voi heittää jotain, mitä sinulla ei ole!')
            lampi(pelaaja)
    elif valinta == '2':
        metsa(pelaaja)
    elif valinta == '0':
        print('Sinulla on, ', pelaaja.inventory, 'ja', pelaaja.rahat, 'rahaa.')
    else:
        print('Annahan olla.')
        lampi(pelaaja)

def mokki(pelaaja):
    print('1) Lähde\n2) Juttele mummolle\n3) Anna mummolle kukkakimppu\n0) Mitäs minulla on taskuissani?')
    valinta = input('Valintasi: ')
    if valinta == '1':
        print('"Näkemiin, kullanmuru! Tulethan pian uudestaan!"')
        metsa(pelaaja)
    elif valinta == '2':
        pelaaja.rahat = pelaaja.rahat + 5
        print('Juttelet mummon kanssa. Lähtiessäsi mummon nipistää poskeasi ja antaa sinulle 5 rahaa.')
        print('"Tässä, nuppulainen. Osta itsellesi vähän karkkia. Ja tule pian uudestaan!"')
        metsa(pelaaja)
    elif valinta == '3':
        if 'kukkakimppu' in pelaaja.inventory:
            monesko = onkoSinulla(pelaaja, 'kukkakimppu')
            del pelaaja.inventory[monesko]
            print('"Voi kiitos, pikkuinen! Ovatpa ne kauniita."')
            print('"Oioi. Onkos sinulla huolia? Jokin pulma? Kerro mummolle, kyllä mummo tietää!"')
            print('1) Itse asiassa, on tämä yksi arvoitus, josta en saa selvää...\n2) Pärjään kyllä')
            valinta = input('Valintasi: ')
            if valinta == '1':
                try:
                    vastaukset = ['avain', 'noppa', 'onni', 'sumu', 'varjo', 'kynttilä', 'muna', 'tuli']
                    print('"Annahan kun mummo miettii. Aa, sehän on ' + vastaukset[pelaaja.arvoitusluku] + '!"')
                except IndexError:
                    print('"Ai, tuo onkin paha. Enpä taida tietää tuota."')
                print('"Kuulehan, oli ihanaa, että kävit, mussukka, mutta jousiammuntatuntini alkaa kohta. Mutta tulehan pian uudestaan!"')
            elif valinta == '2':
                print('"Aivan, tiedänhän minä, että vaavini osaa jo itse hoitaa asiansa."')
                pelaaja.rahat = pelaaja.rahat + 20
                print('Juttelet mummon kanssa. Lähtiessäsi mummon nipistää poskeasi ja antaa sinulle 20 rahaa.')
                print('"Tässä, kullannuppu. Osta itsellesi vähän karkkia. Ja tule pian uudestaan!"')
                metsa(pelaaja)
            else:
                print('Anna olla.')
                mokki(pelaaja)
        else:
            print('Et voi antaa jotain, mitä sinulla ei ole!')
            mokki(pelaaja)
    elif valinta == '0':
        print('Sinulla on', pelaaja.inventory, 'ja', pelaaja.rahat, 'rahaa.')
    else:
        print('Anna olla.')
        mokki(pelaaja)

def tapaaminen(pelaaja):
    if pelaaja.questnro < 5:
        encounter = ['', 'kauppamatkustaja', 'puska', 'puska']
    elif pelaaja.questnro > 5:
        encounter = ['', 'kauppamatkustaja', 'puska', 'puska', 'puska', 'puska', 'luola', 'haltia', 'peikko', 'menninkäinen', 'sfinksi', 'tulivuori', 'notko', 'Varjojen saartama maa', 'lampi', 'mökki']
    elif pelaaja.questnro == 5:
        encounter = ['peikko', 'linna', 'sfinksi', 'tuulimylly']
    vastaanTulee = random.choice(encounter)
    if vastaanTulee == '':
        metsa(pelaaja)
    else:
        print('Vastaan tulee ' + vastaanTulee + '.')
        if vastaanTulee == 'kauppamatkustaja':
            kauppamatkustajanVarastot(pelaaja)
        elif vastaanTulee == 'puska':
            itemencounter(pelaaja)
        elif vastaanTulee == 'luola':
            luola(pelaaja)
        elif vastaanTulee == 'haltia':
            print('"Kas vain, kuolevainen. Tahtoisitko tehdä kauppaa?\n'\
                  'Jos sinulla meripihkaa tai helmiä, otan ne mielelläni käsistäsi...\n'\
                  'Vastineeksi saat kuuliljan."')
            haltia(pelaaja)
        elif vastaanTulee == 'peikko':
            print('"Orkh. Nahka-pussi? Kaarna-vene? Ögr... Annan timantin."')
            peikko(pelaaja)
        elif vastaanTulee == 'menninkäinen':
            hinta = random.randint(20, 64)
            print('"Hei hei hei! Onkos sitä rahaa? Minä PIDÄN rahasta. Osta jotain! Osta jotain!\n'\
                  'Minulla on... Helmi! Ja meripihkaa! Ja nahkapussi ja kaarnavene!', hinta, 'rahaa! Osta!"')
            print('Sinulla on', pelaaja.rahat, 'rahaa.')
            menninkainen(pelaaja, hinta)
        elif vastaanTulee == 'linna':
            linna(pelaaja)
        elif vastaanTulee == 'tuulimylly':
            tuulimylly(pelaaja)
        elif vastaanTulee == 'sfinksi':
            sfinksi(pelaaja)
        elif vastaanTulee == 'tulivuori':
            tulivuori(pelaaja)
        elif vastaanTulee == 'notko':
            if (pelaaja.arvoitusluku <= 6) or ('lohikäärmeenmuna' in pelaaja.asusteet):
                print('Notkon suu on täynnä ohdakkeita. Et pääse eteenpäin.')
                metsa(pelaaja)
            else:
                print('Notkon suun reunoila on hiiltyneitä ohdakkeita. Edessä näkyy lohikäärmeen pesä.')
                notko(pelaaja)
        elif vastaanTulee == 'Varjojen saartama maa':
            if (pelaaja.questnro <= 5) or ('sormus' in pelaaja.asusteet):
                print('Maan yllä on pimeys. Rumat örkit vartioivat portteja. Hiivit pois ennen kuin sinut nähdään.')
                metsa(pelaaja)
            else:
                print('Varjot ovat väistyneet. Kukaan ei vartioi portteja. Astut sisään')
                mordor(pelaaja)
        elif vastaanTulee == 'lampi':
            print('Lampea ja sen rantaa peittää usva, etkä näe mitään.')
            if 'usvahelmi' in pelaaja.asusteet:
                print('Usvahelmi taskussasi alkaa hehkua. Kun otat sen esille, maaginen puhuri ajaa usvan helmeen, ja näet rannan kirkkaasti.')
                lampi(pelaaja)
            else:
                print('Käännyt pois ennen kuin eksyt.')
                metsa(pelaaja)
        elif vastaanTulee == 'mökki':
            print('Astutko sisään?')
            print('1) Ei\n2) Kyllä')
            valinta = input('Valintasi: ')
            if valinta == '2':
                print('Astuessasi mökkiin, näet mummon keinutuolissa.')
                print('"Hei, kultaseni! Kuinka ihanaa, että tulit käymään!"')
                mokki(pelaaja)
            elif valinta == '1':
                metsa(pelaaja)

def taotaan(pelaaja, esineet, saadaan, teksti):
    poistetut = []
    for i in range (0, len(esineet)):
        if esineet[i] not in pelaaja.inventory:
            for esine in poistetut:
                pelaaja.inventory.append(esine)
            pelaaja.inventory.sort()
            print('"Ai-jai, jotain taitaa puuttua! Sinulla on:\n', pelaaja.inventory, \
                  '\n' + teksti + '\n'\
                  'Tule takaisin, kun sinulla on kaikki tarvittava. Vai tarttisitko jotain muuta?"')
            seppa(pelaaja)
        monesko = onkoSinulla(pelaaja, esineet[i])
        del pelaaja.inventory[monesko]
        poistetut.append(esineet[i])
    pelaaja.inventory.append(saadaan)
    pelaaja.inventory.sort()
    pelaaja.rahat = pelaaja.rahat - 2
    print('"Siinä!"')
    print('Sinulla on nyt:', pelaaja. inventory, 'ja', pelaaja.rahat, 'rahaa.')
    print('"Kootaanko vielä jotain?"')

def seppa(pelaaja):
    while True:
        print('1) Kootaan!\n2) Minulla on kaikki mitä tarvitsen')
        valinta = input('Valintasi: ')
        if valinta == '2':
            print('"Ei sitten, mutta piipahda, jos mieli muuttuu!"')
            kyla(pelaaja)
        elif valinta == '1':
            if pelaaja.rahat - 2 < 0:
                print('"Ai-jai, sinulla ei taida rahat riittää, toveri. Pahoittelut, mutta pitää minunkin perheeni elättää.\n'\
                      'Tule takaisin, kun varasi ovat riittoisammat!"')
                kyla(pelaaja)
            print('"No mitäs kootaan?"')
            if pelaaja.questnro <= 4:
                print('1) Kukkakimppu\n2) Seljajuoma\n3) Voikukkaseppele\n4) Luukoru\n5) Barbaariastiasto')
            else:
                print('1) Kukkakimppu\n2) Seljajuoma\n3) Voikukkaseppele\n4) Luukoru\n5) Barbaariastiasto\n6) Kuuliljauute\n7) Tiara\n8) Parfyymi\n9) Pähkinäöljy')
            kootaan = input('Valintasi: ')
            if kootaan == '1':
                esineet = ['ruusu', 'selja', 'kehäkukka', 'vesililja']
                saadaan = 'kukkakimppu'
                teksti = 'mutta kukkakimpun tekemiseen tarvitaan ruusu, selja, kehäkukka ja vesililja.'
            elif kootaan == '2':
                esineet = ['selja', 'selja', 'selja', 'selja', 'selja']
                saadaan = 'seljajuoma'
                teksti = 'mutta seljajuoman tekemiseen tarvitaan viisi seljankukkaa.'
            elif kootaan == '3':
                esineet = ['voikukka', 'voikukka', 'voikukka', 'voikukka', 'voikukka', 'voikukka', 'voikukka', 'voikukka', 'voikukka', 'voikukka']
                saadaan = 'voikukkaseppele'
                teksti = 'mutta voikukkaseppeleen tekemiseen tarvitaan kymmenen voikukkaa.'
            elif kootaan == '4':
                esineet = ['sarvi', 'pääkallo', 'luu', 'hammas', 'hammas', 'hammas', 'hammas']
                saadaan = 'luukoru'
                teksti = 'mutta luukorun tekemiseen tarvitaan sarvi, pääkallo, luu ja neljä hammasta.'                
            elif kootaan == '5':
                esineet = ['pääkallo', 'pääkallo', 'pääkallo', 'pääkallo', 'pääkallo', 'pääkallo', 'pääkallo', 'pääkallo', 'pääkallo', 'pääkallo', 'pääkallo', 'pääkallo', ]
                saadaan = 'barbaariastiasto'
                teksti = 'mutta barbaariastostoon tarvitaan 12 pääkalloa.'
            elif kootaan == '6':
                esineet = ['kuulilja', 'kuulilja', 'kuulilja', 'kuulilja', 'kuulilja', 'kuulilja', 'kuulilja']
                saadaan = 'kuuliljauute'
                teksti = 'mutta kuuliljauutteen uuttamiseen tarvitaan seitsemän kuuliljaa.'
            elif kootaan == '7':
                esineet = ['timantti', 'timantti', 'timantti']
                saadaan = 'tiara'
                teksti = 'mutta tiaran tekemiseen tarvitaan kolme timanttia.'
            elif kootaan == '8':
                esineet = ['merisuolaa', 'pähkinäöljy', 'vesililja', 'vesililja', 'vesililja', 'vesililja', 'vesililja']
                saadaan = 'parfyymi'
                teksti = 'mutta parfymin uuttamiseen tarvitaan suolaa, pähkinäöljyä ja viisi vesilijaa.'
            elif kootaan == '9':
                esineet = ['pähkinöitä', 'pähkinöitä', 'pähkinöitä']
                saadaan = ['pähkinäöljy']
                teksti = 'mutta pähkinäöljyn uuttamiseen tarvitaan kolme satsia pähkinöitä.'
            else:
                print('Ännahan olla.')
            taotaan(pelaaja, esineet, saadaan, teksti)
        else:
            print('Annas olla')

def juomanOsto(pelaaja, hinta, juoma):
    if (pelaaja.rahat - hinta) < 0:
        print('"Hei! Täällä ei myydä velaksi! Mutta ehkä sinulla olisi varaa johonkin halvempaan?"')
        tiski(pelaaja)
    else:
        pelaaja.rahat = pelaaja.rahat - hinta
        pelaaja.inventory.append(juoma)
        pelaaja.inventory.sort()
        print('"Saisiko olla vielä jotain muuta?"')
        tiski(pelaaja)

def tiski(pelaaja):
    print('1) Sarsaparilla, 10 rahaa\n2) Maito, 2 rahaa\n3) Ei mitään, kiitos.\n0) Mitäs minulla on taskuissani?')
    valinta = input('Valintasi: ')
    if valinta == '1':
        hinta = 10
        juoma = 'sarsaparilla'
    elif valinta == '2':
        hinta = 2
        juoma = 'maito'
    elif valinta == '3':
        print('"No, tule takaisin kun taas janottaa!"')
        taverna(pelaaja)
    elif valinta == '0':
        print('Sinulla on', pelaaja.inventory, 'ja', pelaaja.rahat, 'rahaa.')
        tiski(pelaaja)
    else:
        print('Annas olla.')
        taverna(pelaaja)
    juomanOsto(pelaaja, hinta, juoma)

def pelaaNoppaa(pelaaja):
    if 'noppa' in pelaaja.asusteet:
        try:
            panokset = int(input('"Mitkä ovat panokset?" '))
        except ValueError:
            print('"Annahan olla! Täällä pelataan rahasta!"')
            pelaaNoppaa(pelaaja)
        while True:
            if panokset < 0:
                panokset = int(input('"Ai voittaja häviää vai? Anna kunnon numero!" '))
            elif panokset >= 0:
                break
        if 'jäniksenkäpälä' in pelaaja.asusteet:
            sina = random.randint(4, 12)
            vastapeluri =random.randint(2, 9)
        else:
            sina = random.randint(2, 12)
            vastapeluri =random.randint(2, 12)
        print('Sinä heität ' + str(sina) + ' ja hän heittää ' + str(vastapeluri) + '.')
        if sina > vastapeluri:
            pelaaja.rahat = pelaaja.rahat + panokset
            print('Voitit. Sinulla on nyt', pelaaja.rahat, 'rahaa.')
        elif vastapeluri > sina:
            pelaaja.rahat = pelaaja.rahat - panokset
            print('Hävisit. Sinulla on nyt', pelaaja.rahat, 'rahaa.')
        else:
            print('Tasapeli. Kukaan ei voita.')
        print('"Aijai. Pelataanko uudestaan?"')
        print('1) Kyllä\n2) Ei\n3) Paljonko rahaa minulla on?')
        valinta = input('Valintasi: ')
        if valinta == '1':
            pelaaNoppaa(pelaaja)
        elif valinta == '2':
            print('"Voi, kyllä sinä vielä pelata haluat. Minä odotan.."')
            taverna(pelaaja)
        elif valinta == '3':
            print('Sinulla on', pelaaja.rahat, 'rahaa.')
            pelaaNoppaa(pelaaja)
        else:
            print('Annas olla.')
            taverna(pelaaja)
    else:
        print('"Hei, et sinä voi pelata noppaa ilman noppia! Tule takaisin, kun sinulla on omat pelivälineet."')
        taverna(pelaaja)
    return pelaaja

def huruUkko(pelaaja):
    if pelaaja.questvalmius == 'valmis':
        print('Huru-ukko nukkuu.')
        taverna(pelaaja)
    else:
        print('"Heips. Ei sulla olisi tarjota lasillista sarsaparillaa?"')
        print('1) Kyllä\n2) Ei')
        vastaus = input('Vastauksesi: ')
        if vastaus == '1':
            if 'sarsaparilla' in pelaaja.inventory:
                try:
                    vihje = ['"Kalloa vailla vai? Eikös niitä ole metsä puolillaan?\nKuinka niitä edes on niin paljon, mutta muita luita ei koskaan näy missään?"', \
                             '"Ai että nälkäinen koira? Luitahan tuommoiset kaluavat, eikö? Tai ehkä kaupassa on koiranruokaa?"', \
                             '"Hammaskipu? Ainakin maito on hyväksi hampaille. Toisin kuin virnuilu.\nJa jos annat sille, mitä se tahtoo, se lähtee ehkä pois..."', \
                             '"Nuoret. Ei niistä nykyään mihinkään ole. Eikös seppä näpertele tuommoisia?"', \
                             '"Voi, tuo on kyllä surullista. Hmm. Kukat ovat sieviä, mutte ei niitä voi pukea. Vai voiko?"', \
                             '"Juu, tuon jutun olen minäkin kuullut. Mutta se linna on varmaan lukossa. Avain ei kyllä varmaan ole linnasta kaukana.."', \
                             '"Jotain hyvää? Eikö se kauppamatkustaja raahaa jotain naposteltavaa?\nIhme ammatti tuo kauppamatkustelu. Juoksentelee vaan ympäriisä ja kantaa kamaa..."', \
                             '"Ei, kyllä sarsaparilla vaan maistuu puulta. Menen takaisin kaivolle. Ihan kohta."', \
                             '"Ai se tyyppi. Joo, se tulee tänne perjantaisin, ja koko paikka haisee.\nBaarimikko sitten sen mentyä saa sen peitettyä jallain ihme hajusteella.\nJa se on hyvä, sillä ei täällä muuten pystyisi kukaan istumaan varttia kauempaa."', \
                             '"Aikamoinen tapaus! Ehkä seppä osaa auttaa, metalliahan nuo tiarat ovat."', \
                             '"Mietitääs. Naiset tykkäävät.. koruista? Ehkä peikkonaiset tykkäävät karusta koruista?"', \
                             '"Toinen? Justiinsa. No. Mitä voi käyttää? Laseista voi ainakin juoda.."', \
                             '"Rohtoa vailla? Eikos kuuliljoilla voi lääkitä joitain tauteja?\nHaltiat nääs kasvattavat niitä, joten kuun parantava voima imeytyy niihin. Tai jotain."']
                    print(vihje[pelaaja.questnro])
                except IndexError:
                    print('Mitä sinä enää haluat? Menes jo siitä.')
                monesko = onkoSinulla(pelaaja, 'sarsaparilla')
                del pelaaja.inventory[monesko]
                taverna(pelaaja)
            else:
                print('"Höh, eihän ole..."')
                taverna(pelaaja)
        elif vastaus == '2':
            print('"No ei sitten..."')
            taverna(pelaaja)

def taverna(pelaaja):
    print('1) Mene tiskille\n2) Pelaa noppaa\n3) Juttele huru-ukolle\n4) Lähde pois\n0) Mitäs minulla on taskuissani?')
    valinta = input('Valintasi: ')
    if valinta == '1':
        print('"Elikkä, mitäs saisi olla?"')
        tiski(pelaaja)
    elif valinta == '2':
        pelaaNoppaa(pelaaja)
        print('"Tervehdys, ystäväiseni. Pelureita siis?"')
    elif valinta == '3':
        huruUkko(pelaaja)
    elif valinta == '4':
        kyla(pelaaja)
    elif valinta == '0':
        print('Sinulla on', pelaaja.inventory, 'ja', pelaaja.rahat, 'rahaa.')
        taverna(pelaaja)
    else:
        print('Annas olla.')
        kyla(pelaaja)

def onkoAsustetta(pelaaja, puetaan):
    monesko = 'ei ole'
    for i in range(0, len(pelaaja.asusteet)):
        if pelaaja.asusteet[i] == puetaan:
            monesko = i
            return monesko

def lue(pelaaja):
    print('1) "Maailma ympärillämme"\n2) "Olentojen kirja"\n3) "Par\'aikaisen hallitsijamme saavutukset"\n4) "Vastakkainen sukupuoli: Kuinka se ajattelee, mitä se haluaa ja kuinka sitä viehätetään"\n5) Lähde')
    valinta = input('Valintasi: ')
    if valinta == '1':
        print('"On olemassa tahoja, jotka uskovat maailmamme olevan vain mielipuolien kuvitelmaa,\ntai jonkinlainen kirjoitettu teos järkevämmästä maailmasta, niin kummallinen se on.'\
              '\nTämä ei kuitenkaan pidä paikkaansa. Kaikki kummalliset asiat on selitettävissä, niitä vain ei ehkä ole vielä selitetty.\nEsimerkiksi kyläämme ympäröivä metsä on lumouksen alainen: '\
              'se muuttaa alati muotoaan.\nSiksi paikat siirtyvät, ja samaa reittiä on mahdotonta seurata kahdesti.\nKylän pystyttämisen mahdollistastemiseksi tämä paikka on myös lumottu niin,'\
              ' että jokainen sitä etsivä sen myös löytää. Melko välittömästi, jopa."\n')
    elif valinta == '2':
        print('"SFINKSIT\n\nSfinksi on olento, joka on pakkomielteisen innostunut arvoituksista.\nSe arvuuttaa kaikkia, jotka sitä vastaan tulevat, olivat he sitten ihmisiä, haltioita tai eläimiä.\n'\
              'Ne palkitsevat ne, jotka tietävät vastauksen, ja syövät ne, jotka vastaavat väärin (puhekyvyttmät olennot mukaan lukien).\nTämä aiheuttaa suuria määriä luita niitten elinympäristössä. Luukauppiaat eivät usein siksi ole kaukana sfinkseistä.\n'\
              'Sfinksit ovat myös hyvin ylpeitä ja itsetietoisia; ne usein väheksyvät kaikkia muita.\n\nHALTIAT\n\nHaltiat ovat sfinksien tavoin ylpeitä ja muita väheksyviä olentoja, ne ovat vain vähän kohteliaampia.\n'\
              'Ne asuvat metsässä, sillä ne arvostavat luontoa ja kasveja yli kaiken, viettäen aikansa viljellen, kukkia kasvattaen ja metsää hoitaen.\nHaltiat elävät hyvin pitkään, miltei ikuisesti niiden luonnonmukaisen elintavan takia(tosin laaja valikoima parantavia yrttejä varmaankin auttaa myös).'\
              '\nNe arvostavat elämää ja kasvamista. Ne myös  väheksyvät peikkoja suurissa määrin niitten epäorgaanisuuden takia.\nSilti haltiat tekevät mielellään kauppaa saadakseen orgaanisia mineraaleja.\n\nPEIKOT\n\n'\
              'Peikot ovat suureksi osaksi kiveä, ja tämä tekee niille vaikeaksi puhua kieltämme:\nniitten kurkku on yksinkertaisesti liian kova.\nTämä antaa peikoista tyhmän kuvan, mutta todellisuudessa peikot ovat yhtä älykkäitä kuin ihmisetkin, ja niitten yhteisö muistuttaa suuresti omaamme.\n'\
              'Ne ovat silti hyvin kömpelöitä, ja niitten on vaikea tehdä tarvekaluja. Siksi ne hankkivat mieluiten käyttöesineensä ihmisiltä.\nNe ovat myös hyvin mieltyneitä luihin: tämä pehmeässä lihassa kasvava kova materiaali kiehtoo niitä.'\
              '\nVahvasti mineraalipitoisen kurkun ja suun takia peikkojen oma kieli kuulostaa ihmisen korvaan karhealta korinalta.\nKivinen ruumis myös auttaa niitä sulautumaan niitten luonnolliseen elinympäristöön eli vuorille ja kivikkoon.\nVuorilla asumisen takia niillä on helppo pääsy erilaiseen jalokiviin.\n\n'\
              'MENNINKÄISET JA KEIJUT\n\nMenninkäiset ovat kiinnostuneita vain yhdestä asiasta: rahasta.\nNe keräävät rahaa pakkomielteisesti ja kantavat sitä ympäriinsä.\nMenninkäiset eivät kuitenkaan tahdo tehdä rahallaan mitään muuta kuin omistaa sitä mahdollisimman paljon.\n'\
              'Jos niiltä kysyy, miksi ne haluavat rahaa vain rahan itsensä takia, vaikka ne eivät sitä käytä,\nsaa vastaukseksi vain hyvin hämmentyneen katseen.\nMenninkäiset pysyvät usein tiiviisti tietyllä alueella.\n\nKeijut taas ovat kuin lähisukulaistensa menninkäisten vastakohta: ne haluavat tehdä, kokea ja seikkailla.\n'\
              'Tämän takia ne myös pysyvät samassa paikassa vain vähän aikaa. Näitä kahta lajia yhdistää perimän lisäksi vain tietty maanisuus:\nmenninkäisten suunnatessa tarmonsa yhteen asiaan (rahaan), keijut suuntaavat energiansa AIVAN KAIKKEEN.\n\nLOHIKÄÄRMEET\n\nNäitä tulta syökseviä petoja kannattaa vältellä.'\
              'Ne pesivät tulivuorien lähettyvillä, sillä niiten munat vaativat kehittyäkseen kuumia läpötiloja.\nMunien kuoriutuessa emot ja isot syöksevät yhdessä tulta niitten päälle. Vain tämä haurastuttaa munien kuorta tarpeeksi, että poikaset pääsevät kuoriutumaan.\nLohikäärmeet keräävät menninkäisten lailla rahaa pesiinsä, '\
              'tosin tämä johtunee enemmän harakkamaisesta viehätyksestä kiiltäviin esineisiin kuin tietoisesta arvotavaroiden arvostuksesta. "\n')
    elif valinta == '3':
        print('"Perunasato on suurempi\n        - ja se olisi siinä"\n')
    elif valinta == '4':
        print('Historioitsija tempaisee kirjan käsistäsi.\n"Miten tuo tänne joutui?! Et sinä tuota saa lukea, se on keräilykappale! Tänne se ennen kuin naarmutat sitä hengitykselläsi!\nEiköhän tuo ole tarpeeksi lukemista tälle päivälle. Nyt ulos!"\nHistorioitsija heittää sinut ulos.')
        kyla(pelaaja)
    elif valinta == '5':
        print('"Näkemisiin, matkalainen.."')
        kyla(pelaaja)
    else:
        print('Anna olla.')
    print('Luetko vielä jotain?')
    lue(pelaaja)

def tallenna(pelaaja):
    print('1) Tallenna peli\n2) Lue kirjoja\n3) Lähde')
    valinta = input('Valintasi: ')
    if valinta == '1':
        nimi = input('"Kerrohan sitten nimesi, matkalainen." ')
        nimi = nimi + '.txt'
        try:
            tiedosto = open(nimi, 'w', encoding='utf-8')
            teksti = str(pelaaja.inventory).strip('[]') + '\n' + str(pelaaja.asusteet).strip('[]') + '\n' + str(pelaaja.lammella).strip('[]') + '\n' + str(pelaaja.rahat) + ';' + str(pelaaja.arvoitusluku) + ';' + str(pelaaja.questnro) + ';' + str(pelaaja.questvalmius) + '\n'
            tiedosto.write(teksti)
            tiedosto.close()
            print('"Noin, matkalainen. Tietosi on kirjoitettu kronikoihin. Nimellä, jonka annot, ne voidaan jälleen löytää.\nVaan nyt jätä minut kammioni rauhaan..."')
            print('Lopetetaanko peli?\n1) Ei\n2) Kyllä')
            valinta = input('Valintasi: ')
            if valinta == '1':
                kyla(pelaaja)
            elif valinta == '2':
                print('Kiitos pelaamisesta, toivottavasti sinulla oli kivaa!\nCredits: Arna Hyvärinen 2015')
                sys.exit(0)
        except IOError:
            print('"Outoa, matkalainen. Tietojasi ei voida kirjoittaa. Yritämmekö uudestaan?"')
            tallenna(pelaaja)
    elif valinta == '2':
        print('"Aah. Hyvä että nuoriso kiinnostuu kirjoista. Tässä, voit lukea näitä:"')
        lue(pelaaja)
    elif valinta == '3':
        print('"Hyvä on, matkalainen. Mutta palaa, jos haluat, että tarinasi muistetaan."')
        kyla(pelaaja)
    else:
        print('Annahan olla.')
        tallenna(pelaaja)

def kyla(pelaaja):
    while True:
        print('Olet pienessä kylässä.')
        print('1) Mene torille\n2) Mene sepän luo\n3) Mene kauppaan'\
              '\n4) Mene metsään\n5) Mene kaivolle\n6) Mene tavernaan\n7) Mene tapaamaan historioitsijaa\n0) Mitäs minulla on taskuissani?')
        valinta = input('Valintasi: ')
        if valinta == '1':
            tori(pelaaja)
        elif valinta == '2':
            print('Saavut sepän pajaan.')
            print('"Terve, toveri! Tarvitsetkos apuja jonkin kasaamiseen? Jelpin kyllä, jos heltiää 2 rahaa!"')
            seppa(pelaaja)
        elif valinta == '3':
            kauppa(pelaaja)
        elif valinta == '4':
            metsa(pelaaja)
        elif valinta == '5':
            kaivo(pelaaja)
        elif valinta == '6':
            print('Astut tavernaan.')
            taverna(pelaaja)
        elif valinta == '7':
            print('Astut pieneen taloon. Kirjahyllyt ja arkut kiertävät seiniä.\nKeskellä huonetta, suuren kirjoituspöydän takana istuu vanhus sulkakynä kädessään.')
            print('"Tervehdys, matkalainen. Olet varmasti nähnyt paljon. Haluatko, että kirjoitan seikkailusi ylös?\nVai tulitko etsimään tiedon aarretta?"')
            tallenna(pelaaja)
        elif valinta == '0':
            print('Sinulla on', pelaaja.inventory, 'ja', pelaaja.rahat, 'rahaa.')
            kyla(pelaaja)
        else:
            print('Åläs yritä.')
            kyla(pelaaja)

def metsa(pelaaja):
    while True:
        print('Olet synkässä metsässä.')
        print('1) Jatka\n2) Mene kylään\n0) Mitäs minulla on taskuissani?')
        valinta = input('Valintasi: ')
        if valinta == '1':
            tapaaminen(pelaaja)
        elif valinta == '2':
            kyla(pelaaja)
        elif valinta == '0':
            print('Sinulla on', pelaaja.inventory, 'ja', pelaaja.rahat, 'rahaa.')
        elif valinta == 'esi-isä':
            pelaaja.rahat = 1256
            pelaaja.asusteet = ['avain', 'noppa', 'jäniksenkäpälä', 'usvahelmi', 'obsidiaanikorvakorut']
            pelaaja.arvoitusluku = 2
            pelaaja.questnro = 11
            pelaaja.lammella = ['rubiini']
            pelaaja.inventory = ['barbaariastiasto', 'kukkakimppu', 'voikukkaseppele']
        elif valinta == 'se on loppu nyt!':
            print('Kiitos pelaamisesta, toivottavasti sinulla oli kivaa!\nCredits: Arna Hyvarinen 2015')
            sys.exit(0)
        else:
            print('Åläs yritä.')
            metsa(pelaaja)

def main():
    print('1) Aloita uusi peli\n2) Jatka vanhaa peliä')
    valinta = input('Valintasi: ')
    if valinta == '1':
        print('\nMATKALAINEN\n\n\nArna Hyvarinen 2015\n')
        print('Valitse haluamaasi toimintoa vastaava numero. Vain nämä toimivat.\nJos numerovalikkoa ei ole, kirjoita sana perusmuodossaan ja pienillä kirjaimilla.\n'\
              'Lue kaikki huolellisesti, muuten sinulta saattaa mennä jotain ohi.\n'\
              'Tallentaaksesi pelisi mene historioitsijan luo.\n'\
              'Jos tunnet olevasi jumissa, kokeile mennä eri paikkoihin. Myös viisaat vanhukset tietävät ratkaisuja.\n'\
              'Kauppojen valikoimat vaihtelevat, joten jos jotain ei ole saatavilla yhdellä käynnillä, se on ehkä seuraavalla.\n'\
              'Ja muista, että metsä on syvä, siellä saattaa joutua vaeltamaan jonkun aikaa, ennen kuin löytää tiensä!\n')
        pelaaja = PelaajaTiedot()
        metsa(pelaaja)
    elif valinta == '2':
        nimi = input('Anna nimi: ')
        nimi = nimi + '.txt'
        try:
            tiedosto = open(nimi, 'r', encoding='utf-8')
            pelaaja = PelaajaTiedot()
            for i in range(1,5):
                rivi = tiedosto.readline()
                if i == 1:
                    rivi = rivi[:-1]
                    kamat = rivi.split(', ')
                    for tavara in kamat:
                        tavara = tavara[1:-1]
                        pelaaja.inventory.append(tavara)
                elif i == 2:
                    rivi = rivi[:-1]
                    kamat = rivi.split(', ')
                    for tavara in kamat:
                        tavara = tavara[1:-1]
                        pelaaja.asusteet.append(tavara)
                elif i == 3:
                    rivi = rivi[1:-2]
                    pelaaja.lammella.append(rivi)
                else:
                    komponentit = rivi.split(';')
                    pelaaja.rahat = int(komponentit[0])
                    pelaaja.arvoitusluku = int(komponentit[1])
                    pelaaja.questnro = int(komponentit[2])
                    pelaaja.questvalmius = str(komponentit[3])
            tiedosto.close()
            try:
                quest = ['Kauppamatkustajan ongelma', 'Luuta ja nahkaa', 'Hyväksi hampaille', 'Dam di dam rakkaalleni', 'Prinsessa pulassa', 'Linnansa vanki', 'Omnomnom', 'Baarikärpänen', 'Päänuotti, sydännuotti, perusnuotti', 'Prinsessa pulassa (taas..)', 'Tyylinsä kullakin', 'Päätön juttu', 'Isistä parhain']
                print('Jäit seikkailuun:', quest[pelaaja.questnro])
            except IndexError:
                print('Olet suorittanut jo kaikki sekkailut.')
            metsa(pelaaja)
        except IOError:
            print('Tiedostoa ei voitu avata.')
            main()
    else:
        print('Tuntematon valinta.')
        main()

main()

#eof
