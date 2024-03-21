STOP_WORDS = set(
    """
men haýran
düýpli
diýen ýaly
degişlidir
emma
zordan
seýle-de bolsa, muňa garamazdan
arada
indi
aslynda
takyk
mundan başga-da
az
düşnükli
dogrymy aýtsam
maňa
iň
iň bolmanda
käwagt
käbirleri
käbirlerine
käbirlerinde
käbirlerinden
başga biri
başga birinde
başga birinden
başga biriniň
belki
Men
Menem
menden
Men
Mina
şondan bäri
indiki ýyldan bäri
beýlekisi
indiki
Mundan başga-da
umuman
hatda
esaslanýar
degişlilikde
biraz
tizara
birek-birege
biri-birinden
birden
birden
birine
kimdir biri
birinde
nden
nämüçindir
kimdir birinde
kimdir birinden
birnäçe
birnäçe adama
olaryň birnäçesi
birnäçesinden
bir gezek
bilelikde
köp
köplere
köpüsinde
köplerden
köpüsi
bir zat
tükeniksiz
üznüksiz
elbetde
biz
Özi
biziň pikirimizçe
bize mähirli bol
ABŞ
bize
biz
biziňki
biziňki
şahsy
biderek
Bu
bular
edil şu ýerde
ine
şu ýerden
şu ýerde
bu ýer
ýaly
şeýlelik bilen
ýaly
umuman
hemmesi
dik
sözlem
sözleme
sözlem
sözlem
sözlemden
sözlemimize
sözlemimiz
sözlemimizden
çalt
çalt
dürli
Köp
köp
köpler tarapyndan
märeke
esasan
köp
köpüsi
köpüsi
köplenç
köpüsinde
köpüsinden
esasan
olaryň köpüsi
olaryň köpüsi
Sebäbi
içinde
has köp
üstesine-de
zehin
goşmak bilen
içerde
elmydama
hakda
esaslanýar
Şeýle hem
gezek
çenli
edil şu wagt
demincek
edil şu wagt
köp
derakap
derrew
diýýärkä
däl
çenli
diýýär
beýlekisi
beýlekisi
başga birine
beýlekisi
beýlekisinden
sebäbi
şonuň üçin
HAKYKAT
eder
kim edýär
tarapyndan
bolar
bolýar
bolmak
edýär
elbetde
elbetde
emdirmek
- iň ýokary
düýpli
gaty gowy
gaty az
birneme
düýpli
wagtynda
etmek
hemmetaraplaýyn
düýpli
etdi
etdi
etdi
ilki bilen
öň
ilki bilen
ozal
öňünden
geçmişde
öň
eger
emma
we şuňa meňzeşler
şeýle-de
gah
gaty gowy
gowy
däl
däl
ýöne geliň

zerur
garamazdan
geçmişde
ýakynda
ýaly
ýaly
ýaly
Gwineýa
boýunça
gykylyk
edil şonuň ýaly
bolsa
häzirki wagtda

bolşy ýaly
iň bolmanda
Haýsy
Haýsy
haýsy
haýsy
Haýsy
haýsyndan
nirede
öz içine almaýar
düwme
Netije
hatda
esasanam
ikisem
entek
elmydama
hemmesi
hemmesi
Hemmesi
Umuman
Ählisinden
hersi
Islendik
hemmeler
hemmeler
Hemmeler
hemmelerden
hiç

hiç
hiç kime
bularyň hiç biri-de ýok
Hiç birinde
Hiç kimden
ýakymly
gysgaça
wagtynda
to
bilen
bilen
bilen baglanyşykly
ilki bilen
hökmany suratda
islendik ýagdaýda
Indi
pursatda
aşak düşýär
goýmak
bolsa
bolsun ... ýa-da
dan
bolşy ýaly
bolşy ýaly
Gowy
düýpli
düýpli
üçin
işlemek
işde
köp
kafes
kah
galmak
meniň pikirimçe
garamazdan
Çeşme
näçe
nädip saklanmalydygyny
haýsy wagtda
näçe
näçe
gaça dur
kelli
eýeçilik edýär
özlerinde
özlerinden
özleri
özleri
özleriniňki
Özi
Özi
öz-özünden
Özünden
özüne
Özi
özüne degişli
gezek
gezek
Şeýle hem
edil şonuň ýaly
Diňe bolsa
Bu
kim
kimden
kime?
kim
kim
käbirleri
käbirlerinde
käbirlerinden
käbirlerine
käbirleri
Hiç kim
hiç kim
Hiç kim
dolulygyna
gysgaça
gysgaça
ol däl
ýalpyldawuk
Haýyş edýärin
Mundan başga-da
şondan bäri
şondan bäri
Şeýle-de bolsa
mebni
Görnüşi ýaly
çykýar
çykýar
Megerem
Bolýarmy?
Bolýarmy?
Bolýarmy?
Bolýarmy?
Nädip
nämüçindir
bilen deňeşdirilende
nashi
Näme
Nireden
sebapli
şu sebäpli
sebäpleri
sebäplere görä
käbir sebäpler üçin
Nirede
Nireden
diýen ýaly
nirede
nirede
nireden
diýen ýaly
nirede
Nirä
Hakykatdanam
nirede
Näme
Her niçigem bolsa
gowy
ahyrynda
ahyrynda
şeýlelik bilen
Näme üçin
Näme üçin
Ol
biri ...
tarapy
bolup geçdi
olar
gitdigiçe köpelýär
bolup durýar
bolup durýar
bolmak
bolmak
garamazdan
bolsun
bolup durýar
Mümkin
bolup geçýän bolsa
bolup geçýär
Ol
örän köp
pioner
onunjy
Ondan
olar
olara
olardan
Olara
Olar
özi-de
Ol
ol ýerde
edil şol ýerde
ýerinde
ol ýerde
ol ýerden
gatnaşygy
degişlilikde
ol ýerde
bolsa
emma
açgöz
beýlekisi
beýlekisi
beýlekisinde
beýlekisinden
beýlekisine
beýlekisi
öň
ozal
öň
ilki bilen
beýlekisi
beýlekisi
ýaly
edil şeýle
şeýlelik bilen
edil şeýle
Özi
köp
bolýar
Bolýar
köp
ädim-ädim
garamazdan
Diňe
aslynda
hakykatdanam
saňa
ýaly
sen
senden
Sen
seniň
sen
senden
sen
seniňki
soňrak
soňrak
soňrak
ahyrynda
eger
zat
bir zatdan
zat
zatlar
Bu
üçin
azajyk
Bu
Ondan
Bular
Bular
şolardan
Bu
Bu
geňeş
edil şu ýerde
edil şu ýerde
ol ýerde
Bu ýaly
Indi
elbetde
doly
Bolýar
dolulygyna
doly
tarapyndan
diňe
hemmesi
hakda
bar
bardy
tarapyndan
We
hatda
gysgaça
Gysgaça aýdylanda
ýa
ýada
ýa-da
Elbetde
basym
ýakyndan
ýakynda
ýeke
Diňe
gowy
eder
etmek
ýasaldy
näme etdiler
näme etdi
näme etdiň
ýasaldy
edilmeli
etmek
ýakynda
ýerine
ýene
ýok
ýa-da?
tarapyndan
sebäbi
içinde

eýýäm
üçin
""".split()
)
