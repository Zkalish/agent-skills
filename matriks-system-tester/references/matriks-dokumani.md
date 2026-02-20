# matriks-dokumani

**Pages**: 1-107

---

**📄 Source: PDF Page 1**

TEKNİK ANALİZ  
KHN (KAHİN) MENÜLERİ

---

---

**📄 Source: PDF Page 2**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 2 / 107 
 
 
 
 
TEKNİK ANALİZ MODÜLLERİ 
KHN ( KAHİN) MENÜLERİ 
İNDEKS 
 
1. İndikatör Builder ( Gösterge Oluşturma)                
4 
1.1 Genel Görünüm 
                                                         5 
1.2 İndikatörler    
                                                         5 
1.3 Alanlar           
                                                         7 
1.4 Operatörler                                                                       8 
1.5 Fonksiyonlar  
                                                        9 
1.6 Alarm Sekmesi 
                                                      23 
1.7 Parametre Sekmesi                                                      24 
1.8 Tanım Kısmı  
                                                      24 
1.9 Diğer Detaylar  
                                                      24 
1.10 İndikatör Oluşturma                                                  25 
1.10.1 Örnek Yazım (Hareketli Ortalama) 
           25 
1.10.2 Data Olarak İndikatör Kullanmak                          27 
1.10.3 Alarm Tanımlama 
                                        28 
1.10.4 İndikatör Builder Penceresinin Diğer Açıklamaları 
31 
1.10.5 Öteleme İçin Örnek  
                                          34 
2. İndikatör Pozisyonları 
                                        35 
2.1 Genel Görünüm ve İlk Bilgiler  
                          35 
2.2 Sembol Seçimi 
                                                      37 
2.3 İndikatör Seçimi 
                                                      37 
2.4 Excel’e Aktar 
                                                       44 
2.5 Yazdır 
                                                                    44 
2.6 Şablonlar 
                                                                     44 
2.7 Hesapla 
                                                                     47 
2.8. Sağ Klik Menüleri                                                       48 
3. İndikatör Değerleri                                                       49 
3.1. Sembol seçimi 
                                                      50

---

---

**📄 Source: PDF Page 3**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 3 / 107 
 
 
3.2. Excel’e Aktar 
                                                    50 
3.3. Yazdır 
                                                                  50 
3.4. Varsayılan Olarak Kaydet                                        50 
3.5. Periyot 
                                                                  50 
3.6. Birim  
                                                                  50 
3.7. Hesapla 
                                                                   50 
3.8 İndikatör Değerleri Penceresi Sağ Klik Menüleri 
51 
4. System Tester 
                                                       52 
4.1 Üst Banttaki Menüler 
                                          53 
4.2 Tanımlı Sistemler 
                                                       55 
4.3 Uygulanmış Simülasyonlar                                          56 
4.4 Yeni Sistem (Oluşturma) 
                                          57 
4.5 Sistem Çalıştırma 
                                                       63 
4.6 Sistem Ayarları 
                                                      70 
4.7 Sistem Tester Sonuçları 
                                         74 
4.8 Grafik Üzerinde Ek Menüler                                          80 
5. Explorer 
                                                                      82 
5.1. İlk Bakış         
                                                       82 
5.2. Yeni Sistem                                                                      83 
5.3. Çalıştır İşlevi 
                                                       87 
6. Expert Advisor 
                                                       92 
6.1.Genel Bakış  
                                                        92 
6.2. Yeni Sistem                                                                     93 
6.3. Sistemin Kapatılması / Düzenlenmesi 
            99 
7. Formasyonları Bul 
                                                    100 
8. Ek Bilgiler            
                                                    100 
8.1 Bar Sayısı      
                                                    100 
8.2 İndikatör Çizgilerinin Taşınması 
                        101 
8.3 İndikatör Builder’da Değişken Kullanmak 
         101 
8.4 Ters Grafik     
                                                    102 
8.5 Listede Olmayan Fonksiyonlar 
                       103 
8.6 Oto Optimizasyon                                                       104

---

---

**📄 Source: PDF Page 4**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 4 / 107 
 
 
Giriş:  
Matriks Veri Terminali’nde trendler, formasyonlar, indikatörler ve diğer gelişmiş teknik analiz 
uygulamalarının tamamı grafik menüleri içerisinde yer almaktadır. Standart uygulamaların 
dışında kalan ileri düzey analiz modülleri, Grafik ekranının üst bandında bulunan KHN(Kahin) 
butonu altında yer alır. Bu doküman içinde, KHN başlığı altında bulunan ileri düzey 
uygulamaların nasıl kullanılabileceği ile ilgili açıklamalar yer almaktadır. 
 
Bu doküman ile amaçladığımız, yatırım önerisi vermek değildir. Teknik analizi bilen / 
öğrenmek / kullanmak isteyen üyelerimizin, Matriks Veri Terminali programımızı kullanarak 
bu işlemleri nasıl yapabileceklerinin anlatımıdır. Bununla birlikte, bazı kullanım özelliklerinin 
anlaşılması için Analiz uygulama örnekleri gösterilmiştir. Bu örnekler, Teknik Analiz 
uygulamaları için bilinmesi gereken noktaları açıklama amacı ile sunulmuş olup, AL-SAT 
işlemlerinizde kullanılma önerisi olarak algılanmamalıdır. Tabii ki, piyasayı bilen ama teknik 
analizi bilmeyen kullanıcılarımız, bu modüllerimizi kullandıkça, Teknik Analiz hakkında bilgi-
fikir sahibi olacaklardır. 
 
Matriks Teknik Analiz araçları Matriks Grafik menüleri içinde KHN altında yer almaktadır. Bu 
modüller İndikator Builder, İndikatör Pozisyonları, System Tester, Expert Advisor, Explorer 
modülleri olup, ortak bir dille yazılmaktadır.  
1. İndikatör Builder ( Gösterge Oluşturma) 
 
Bu modül, Matriks Veri Terminali programımızda var olan indikatörleri ve / veya data tiplerini 
kullanarak, yeni indikatörler oluşturulması içindir. Var olan indikatörler kullanılarak, 
matematiksel bir takım işlemlerle farklı indikatörler oluşturabileceğiniz gibi, kapanış, işlem 
hacmi gibi muhtelif data alanlarımı kullanarak da yeni indikatörler oluşturabilirsiniz. İndikatör 
oluştururken matematiksel işlevleri kullanarak hesaplamalar yapabilir ve fonksiyonları 
kullanarak ek uygulamalar gerçekleştirebilirsiniz.  
İndikatör Builder menüsünü tıkladığınızda karşınıza aşağıda göreceğiniz pencere açılır.

---

---

**📄 Source: PDF Page 5**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 5 / 107 
 
 
1.1 Genel Görünüm:  
Öncelikle, bu pencere üzerinde var olan kısımları ve kısaca işlevlerini tanıyalım. 
 
 Tanımlı İndikatörler: Pencerenin sol tarafında ‘Tanımlı İndikatörler’ kısmı vardır.  
Bir indikatör oluşturup kaydettiğinizde, o indikatör verdiğiniz isim ile bu pencerede görünür. 
 
 İndikatör Adı: 
İndikatör oluşturmaya başladığınızda ilk olarak bir isim veriniz. Herhangi bir isim 
verebilirsiniz. Doğal olarak size ne hazırladığınızı hatırlatacak bir isim vermeniz daha 
uygundur. İsim vermeden kaydetmeye çalıştığınızda program sizi uyaracaktır.  
 
 İndikatör Kısaltması:  
En fazla 4 karakter olabilir ve harf ile başlamak zorundadır. Size indikatörü hatırlatacak, 
indikatör adına uygun bir kodlama yapmanızda fayda vardır.  
 
 Anlık Güncelleme Yap:  
Bu mini pencerenin yanındaki kutucuğa işaretleyerek seçerseniz, her yeni veri geldiğinde, 
gelen veriler indikatör uygulamasına dahil edilir.  
 
 Genel Sekmesi: 
İndikatör Builder penceresinin orta kısmında, indikatör yazımında kullanılacak seçeneklerin 
sunulduğu bölüm vardır. Görünüm aşağıdaki gibidir.  
 
 
 
1.2 İndikatörler:  
Genel sekmesi altında ‘İndikatörler’ penceresi içinde, yeni bir indikatör oluşturmak için 
kullanabileceğiniz indikatörler listelenir. Matriks içinde yer alan ve formüle edilmeye uygun 
uygun tüm indikatörler burada yer almaktadır.  
İndikatörler hakkında daha detaylı bilgi için Bakınız: İndikatörler (Göstergeler) dokümanı. 
 
Buradan bir indikatör seçip üzerine çift tıkladığınızda, indikatör yazım şablonu tanım kısmına 
gelir.

---

---

**📄 Source: PDF Page 6**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 6 / 107 
 
 
 
 
Örnek olarak yukarıda Asymmetrical RSI indikatörü üzerine çift tıkladığımızda tanım kısmına 
ARSI(Data,Period) ifadesi gelir. 
Bu ifade o indikatörün matriks dilindeki yazım şablonunu ifade eder. 
Dikkat etmeniz gereken detay şudur: 
Şablon sizden hangi veriyi istiyor ise, sadece ve tam olarak o veriyi vermeniz. 
Data yerine hangi datanın ARSI değeri hesaplanacak ise o yazılmalıdır. 
Genel olarak normalde sembolün fiyat verisi üzerinden hesaplama yapılır. 
Bu durumda buraya kapanış değerini ifade etmek üzere C yazılır. 
Period yerine de indikatörün hangi periyod için hesaplama yapmasını istiyorsanız o değeri 
yazmalısınız. 
ARSI indikatörünü orijinal indikatör kısmından seçip grafik üzerine atmak istersek aşağıda 
göreceğimiz parametre penceresi gelir: 
 
 
 
Buradan normalde ARSI indikatörünün kapanış üzerinden hesaplandığını ve ön tanımlı 
periyodunun 14 olduğunu anlıyoruz. 
Tanım kısmındaki şablonda Data ve Period yerine C ve 14 yazalım. 
İfade ARSI(C,14) şeklini alacaktır. 
İsim ve kısaltma verip kaydederseniz tanımlı indikatörler kısmına eklenecektir. Grafik 
üzerinde göster derseniz grafik üzerine atanacaktır. 
Aşağıdaki grafikte orijinal indikatör ve indikatör builder’da yazılmış hali alt alta 
görünmektedir.

---

---

**📄 Source: PDF Page 7**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 7 / 107 
 
 
 
 
Yukarıda görebileceğiniz gibi birebir aynıdır. 
Yani ARSI(C,14) ifadesi matriks program dilinde Asymmetrical RSI indikatörünün tanımıdır.  
 
İpucu: İndikatör şablonlarına dikkat ediniz. Hangi veriyi talep ediyor ise sadece onu yazınız. 
Eksik veya fazla parametre girmeyiniz. Parantez, virgül, nokta, tırnak işaretlerine 
dokunmayınız. Data, period gibi ifadeleri kaldırıp yerine kullanılmasını istediğiniz 
parametreleri yazınız.  
 
Örnekler: 
CCI(Period) 
CCI(14) olarak yazmalısınız. 
 
DI()  Bu demand indeks şablonudur.  
DI()  olarak yazmalısınız. Herhangi bir veri istemiyor. O yüzden parantez içine bir şey 
yazmamalısınız.  
 
MOV(Data,Period,Yöntem S E W TRI VAR ZL WW TSF) 
MOV(C,10,E)  olarak yazarsanız yöntem olarak E: Üssel Hareketli Ortalamayı seçmiş 
olursunuz. 
İpucu: Hareketli ortalama isimlendirmeleri literatürde EMA, SMA olarak geçer. 
EMA 10 ifadesi matriks dilinde MOV(C,10,E)   
SMA 10 ifadesi ise MOV(C,10,S)  şeklinde yazılır. 
 
 
 
1.3 Alanlar:  
Genel sekmesi altında ‘Alanlar’ kısmında Data olarak kullanılabilir veriler bulunmaktadır. 
 
Data: Matriks’te Formül yazımı yapılırken karşılaşacağımız ‘Data’ bir sayı, alanlardan gelen bir 
değer ya da bir indikatör olabilir. Sayısal değer taşıyan herhangi bir veri olabilir.

---

---

**📄 Source: PDF Page 8**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 8 / 107 
 
 
 
 Alanlar kısmında data olarak kullanılacak verilerin açıklamaları:  
 
 O – Open  - Açılış: Seçtiğiniz periyod için barın açılış fiyatı (ilk işlem fiyatı) demektir. 
Grafik periyodunuz günlük ise günlük açılış fiyatı (günün ilk işleminin fiyatı), 5 dk’lık 
ise 5 dk’lık barın açılış (söz konusu olan 5 dk’da gerçekleşen ilk işlemin fiyatı) fiyatıdır. 
 
 H – High  - Yüksek: Seçtiğiniz periyod için barın en yüksek fiyatı demektir. Grafik 
periyodunuz günlük ise günlük en yüksek fiyatı, 5 dk’lık ise söz konusu 5 dk’lık barın 
en yüksek fiyatıdır. 
 
 L – Low  - Düşük: Seçtiğiniz periyod için barın en düşük fiyatı demektir. Grafik 
periyodunuz günlük ise günlük en düşük fiyatı, 5 dk’lık ise söz konusu 5 dk’lık barın en 
düşük fiyatıdır. 
 
 C – Close  - Kapanış: Seçtiğiniz periyod için barın kapanış fiyatı demektir. Grafik 
periyodunuz günlük ise günlük son işlem fiyatı, 5 dk’lık ise söz konusu 5 dk’lık barın 
son işlem fiyatıdır.  
 
 W – Weighted Average – Ağırlıklı Ortalama: Seçtiğiniz periyod için barın ağırlıklı 
ortalaması demektir. Grafik periyodunuz günlük ise günlük ağırlıklı ortalama, 5 dk’lık 
ise söz konusu 5 dk’lık barın ağırlıklı ortalamasıdır.  
 
 V – Volume – Hacim: Seçtiğiniz periyod için toplam işlem miktarını gösterir. 
 
 (H+L)/2: Seçilen periyod için barın yüksek ve düşük rakamlarını toplar ve ikiye böler. 
Bazı kullanıcılar bu veriyi kullanmayı tercih ederler. 
 
 (H+L+C)/3: Seçilen periyod için yüksek, düşük ve kapanış fiyatlarını toplar ve üçe 
böler. Bazı kullanıcılar bu veriyi kullanmayı tercih ederler. 
 
 (H+L+2*C)/4: Seçilen periyod için barın kapanış fiyatını iki ile çarpıp yüksek ve düşüğe 
ekler çıkan toplamı dörde böler. Bazı kullanıcılar bu veriyi kullanmayı tercih ederler. 
 
İpucu: KHN Menüsü altındaki tüm uygulamalarda, Data alanları aynı harflerle temsil 
edilirler.  
 
 
  
1.4 Operatörler:  
Genel sekmesi altında ‘Operatörler’ penceresi içinde formül yazarken kullanacağımız 
matematiksel işlem operatörleri vardır. 
 
 Bu Operatörlerin açıklamaları:

---

---

**📄 Source: PDF Page 9**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 9 / 107 
 
 
AND ( VE ): Birden fazla koşulun aynı anda gerçekleşmesini istiyorsak bu koşulları AND ile 
birbirine bağlarız. Verdiğimiz 2 koşuldan 1 tanesi karşılanmıyorsa, sonuç olumsuza göre alınır. 
 
OR (VEYA): İki adet koşuldan herhangi birisinin gerçekleşmesi durumunda sonuç görmek 
istiyorsak bu iki koşulu OR ile birbirine bağlarız. Yani OR ile birbirine bağlanan herhangi 2 
koşuldan 1 tanesinin gerçekleşmesi yeterlidir, hangisinin gerçekleştiğinin önemi yoktur. 
Ancak her iki koşul da karşılanamıyorsa, sonuç olumsuza göre alınır. 
 
İpucu: Çok sayıda koşulu AND ve/ya OR ile birbirine bağlayabilirsiniz. Parantez kullanımı 
sonucu değiştirebilir. Dikkat ediniz. 
 
Bunların altında ise matematiksel işlemler için kullanacağımız +, - , ( , ) vb. işaretlemeler 
vardır. 4 işlem yapılırken parantez kullanımı sonucu etkilemektedir. Buna dikkat etmemiz 
gerekir. 
 
 Parantez Kullanımı: 
Matriks‘te yazılan tüm formüller, matematiksel öncelik kurallarına uygun olarak 
işlenmektedir. Bu nedenle, işlem yapılırken, önce ‘/’ ve ‘*’ işlemleri, sonrasında ‘+’ ve ‘-‘ 
işlemleri sırasıyla gerçekleştirilmektedir. 
    Örnek olarak:  
1+2*3-4 = 3    
(1+2)*3-4 = 5    
Çarpma yapmadan önce toplama yapmak istiyorsanız o bölümü parantez içine almalısınız.  
(1+2)*3-4 şeklinde yazdığınızda öncelikle 1+2 bölümü hesaplanacaktır. 
1+2*3-4 şeklinde yazdığınız da ise öncelik 2 ile 3 ün çarpımına geçecek sonra sonuç (6)  1 ile 
toplanacak ve çıkan sonuçtan 4 çıkarılacaktır. 
Bir formül deneyelim. Günlük yüksek, düşük ve kapanış fiyatlarının ortalamasını hesaplamak 
istersek, yazacağımız formül şu şekilde olmalıdır: (H+L+C)/3 
Eğer parantezi koymaz isek ve H+L+C/3 şeklinde yazarsak öncelik C/3 işlemine geçer. Önce C 
nin 3 te biri bulunup sonra buna H ve L eklenir ve ulaşmak istediğimiz ortalama rakamına 
ulaşamaz, farklı (yanlış) bir sonuca ulaşmış oluruz. 
 
 
1.5 Fonksiyonlar:  
Genel sekmesi altında ‘Fonksiyonlar’ penceresi içinde indikatör yazarken kullanacağımız 
muhtelif fonksiyonlar vardır. Bu mini pencerenin hemen altında da, gene formül yazarken 
kullanabileceğimiz muhtelif trigonometrik / matematiksel fonksiyonlar bulunmaktadır. 
Fonksiyonlar, özel matematiksel işlemler yapmayı sağlayan uygulamalardır. Açıklamaları 
aşağıdadır:  
 
 Abs (Absolute): Mutlak değerini alır.   
Yazım: Abs(Data) 
Mutlak değerini alması demek, sonuç negatif (-) bile olsa, pozitife (+) dönüştürmek demektir. 
(Sonuç pozitif ise öyle kalır)

---

---

**📄 Source: PDF Page 10**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 10 / 107 
 
 
 Bars Since:  
Yazım: BarsSince(Data) 
Tanımladığımız koşulun gerçekleşmesinden bu yana geçen bar sayısını hesaplar.  
Örnek: Barsince ( macd (26,12,9) < 0 )  
 Burada vereceği sonuç, yukarıdaki parametrelere göre hesaplanan  Macd nin 0 dan küçük 
olduğu en son bardan bu yana geçen bar sayısı olacaktır. 
 
 Correlation:  
Yazım: Correl(Data1(independent),Data2(dependent),Periyot, Shift) 
Belirli bir periyot için Data2’nin Data1’e göre korelasyonunu hesaplar. Bunu yaparken 
datanın N gün kadar Shift (Öteleme) yapılmış değerini alır.  
 
 Cross:  
Yazım: Cross(Data1,Data2) 
Cross fonksiyonu; yazılı ilk datanın, ikinci datayı aşağıdan yukarıya kestiği anı ifade eder. Bu 
haliyle klasik > < kullanımından farklıdır. 
→Örnek: Cross (C,mov(c,5,s)) Bu formülün vereceği sonuç, Data serisinin (Grafik 
Sembolünün) kapanışının, 5 günlük basit ortalamasını kestiği bar olacaktır.  
Koşul kapanışın 5 günlük basit ortalamayı yukarı doğru kestiği bar içinde gerçekleşmiştir. 
Bununla beraber kapanış ortalamanın üzerinde kalmaya devam etse bile diğer tüm barlarda 
koşul gerçekleşmesi söz konusu olmaz. Ancak kapanış ortalamayı aşağıya kesip, sonra tekrar 
yukarıya keser ise, bir kez daha koşul gerçekleşmiş olur.  
 
 Cumulate: 
Yazım: cum(data) 
Grafikte ilk datadan itibaren data düzeninin toplamını kümülatif olarak hesaplar.  
Örnek: Cum (1) grafiğin başından itibaren her bar için 1 değeri ekleyerek artar.  
Cum (C) ise grafiğin başından itibaren bütün kapanışların toplamını hesaplar.  
Bu sayede farklı tarzda ortalama hesaplaması yapabiliriz. 
 
 
 Current Hour / Minue / Second: 
Yazım:  
CurrentHOUR() 
CurrentMINUTE() 
CurrentSECOND() 
 
Bu fonksiyonlar, içinde bulunulan zamanı tanımlar / ölçer.  
Geçmiş barlarda çalışmazlar.  
Sadece içinde bulunduğumuz bar için, anlık zamanın ölçümünde kullanabilirsiniz.  
Düz bir biçimde grafik üzerine atarsanız şöyle bir görünüm oluşur:

---

---

**📄 Source: PDF Page 11**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 11 / 107 
 
 
 
 
3 tane çizgi, sırası ile saat, dakika ve saniyeyi göstermektedir. 
 Dikkat: Veriler sadece, fiyat datası geldikçe güncellenir. Bu sebeple data gelmeyen süreçte, 
gerçek saniye ile, indikatör içinde gösterilen saniye datası arasında farklılıklar oluşabilir.  
 
Bu fonksiyonları nasıl kullanabileceğimize bir örnek: 
 
barT:=hour()*3600+minute()*60;  
barLT10:=barT+10*60-1;  
currT:=currenthour()*3600+currentminute()*60+currentsecond();  
barLT10-currT 
 
Yukarıdaki formül 10 dakikalık grafikte, her barın açılışından itibaren, 600 den geriye doğru 
saymaya başlar.  
Buna koşul ekleyerek, geçici sinyalleri barın belli bir zamanından sonra almayı 
sağlayabilirsiniz.  
 
 
 Custom Trend: 
Yazım: MYTREND("Date1",Val1,"Date2",Val2) 
Bu fonksiyonun asıl kullanım amacı manuel olarak çizmiş olduğunuz bir trendi kopyalayarak 
sisteminizin içine almaktır. Çizmiş olduğunuz bir trend üzerinde sağ klik yapıp Kahin İçin 
Kopyala seçimini yaparsanız bunu indikatör builder (veya sistem tester veya expert advisor) 
içinde kullanabilirsiniz. İndikatör builder içinde tanım kısmına gelip yapıştır derseniz 
yukarıdaki şablona uygun olarak formülünüz yazılır.

---

---

**📄 Source: PDF Page 12**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 12 / 107 
 
 
MYTREND("09.11.18 15:00",7.78,"04.12.18 17:00",8.32) 
Burada görebileceğiniz gibi, dilerseniz tarih ve değerleri manuel girerek de sistem içinde 
trend çizimi yapabilir, buna bağlı koşul yazabilirsiniz.  
 
 Data Kanal: 
Yazım: DataKanal(DATA,Bar sayısı,Bitiş Noktası (bugün için 0, dün için -1),Y=yükselen 
D=düşen,%Seviye) 
Bu fonksiyon Data yerine yazacağınız herhangi bir veri için trend çizebilmenizi sağlar. Ek 
olarak %Seviye kısmına yazacağınız veri ile paralel trendler çizebilir böylece kanal 
oluşturabilirsiniz.  
 
 Data Trend: 
Yazım: DataTrend(DATA,Bar sayısı,Bitiş Noktası (bugün için 0, dün için -1),Y=yükselen 
D=düşen) 
Bu fonksiyon Data yerine yazacağınız herhangi bir veri için trend çizebilmenizi sağlar. Mesela 
RSI indikatörü için bir trend çizdirebilirsiniz. Bunu sembolün fiyatı için çizdireceğiniz trend ile 
karşılaştırarak uyumsuzluk arayabilirsiniz.  
 
 Day Of Month:  
Yazım: DAYOFMONTH() 
İlgili barda ayın kaçıncı gününde olduğunu gösterir. İlgili günün sayısal gün değeri gelir. 
 
 Day Of Week:  
Yazım: DAYOFWEEK() 
Pazartesi için 1 den başlayarak Cuma günü için 5 yazılır. İlgili barda haftanın kaçıncı gününde 
olunduğunu gösterir. Sal gün değeri (1-5 arası ) gelir. 
 
 DrawLine:  
Yazım: DrawLine(Koşul,Data) 
Koşul’un gerçekleştiği barda, o barın datasının olduğu yere bir kutucuk koyar. 
 
Örnek: 
DrawLine(cross(c,mov(c,10,e)),H) 
İfadesi aşağıdaki görünümü getirir.

---

---

**📄 Source: PDF Page 13**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 13 / 107 
 
 
 
 
Fiyatın, 10 luk hareketli ortalamanın üstüne çıktığı her barda, barın yükseğine 1 mini kutucuk 
(işaret) konduğu görülmektedir.  
 
 
EXP (e üssel hesaplaması):  
Yazım: EXP(Data) 
Matematikte ‘e’ isimli özel bir sayı vardır.  
e sayısı veya Euler sayısı, matematik, doğal bilimler ve mühendislikte önemli yeri olan sabit bir reel sayı, 
doğal logaritmanın tabanıdır.  
Yaklaşık değeri:  e = 2.71828…. 
Bu fonksiyon ile, e sayısının üssel değeri hesaplanır. Data yerine yazılan rakam için, e 
sayısının üssel değeri sonuç olarak döner. 
 
Örnek: 
EXP(2) formülü aşağıdaki sayıyı verir.

---

---

**📄 Source: PDF Page 14**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 14 / 107 
 
 
 
 
Hesaplar veya internetten kontrol ederseniz, doğru olduğunu görebilirsiniz.  
 
 
 
 
Formula Call:  
Yazım: FML("Indicator") 
Kullanıcının tanımladığı bir indikatör değerinin, başka bir indikatörde yada koşul içinde 
kullanılmasını sağlar. İndikatör Builder’da var olan / oluşturduğumuz herhangi bir  indikatörü 
explorer’da / bir başka yerde sistem / farklı bir indikatör oluştururken Formula Call 
fonksiyonu ile çağırıp kullanabilirsiniz. Formula Call’u çift tıkladığınızda koşul kısmına 
FML("Indicator") olarak gelen koşulun içinde indikatör kısmına çağırmak istediğiniz 
indikatörün kısa adını yazmanız yeterlidir. Bu kısa ad söz konusu indikatörün tanımlanırken, 
indikatör builder’da verilen kısa adıdır. 
→Örnek: FML("MTX") şeklinde. Bu ifade “MTX” kısa adıyla yazılan indikatörün değerini 
getirir. 
 
İpucu: Eğer FML ile çağrılan indikatör 1’den fazla çizgiye sahip ise, bu yazım şekli her 
durumda ilk çizgiyi çağırır. Eklenen bir özellik sayesinde sonraki satırların da çağrılabilmesi 
mümkün hale gelmiştir.  
FML("MTX",3) şeklinde yazınca, çağırılan indikatörün 3. Çizgisini oluşturan değer gelecektir.  
Dikkat: Eğer çağırılan indikatör verieln numaradan daha az sayıda çizgiye sahip ise, öyle bir 
çizgi olmadığı varsayılır ve sonuç sıfır (0) gelir.

---

---

**📄 Source: PDF Page 15**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 15 / 107 
 
 
 Frac: 
Yazım: frac(Data) 
Data yerine gelen verinin küsuratını getirir. Mesela data yerine yazdığınız veri 8.21 değerine 
sahipse o barda frac fonksiyonunun getireceği değer 0.21 olacaktır.  
 
 Highest: 
Yazım: Highest(data) 
Grafikte ilk bardan itibaren data serisinin en yüksek değerini hesaplar.  
→Örnek: Highest(RSI()) Bu fonksiyon ilk datadan itibaren en yüksek RSI değerini hesaplar.  
 
 Highest High: 
Yazım: HHV(Data,Periyot) 
Belirtilen periyotta data serisinin en yüksek değerini hesaplar.  
→Örnek: HHV(RSI(),100) Fonksiyon yukarıdaki şekliyle, geçmiş 100 barlık periyotta en yüksek 
RSI değerini hesaplar.  
 
 Highest Since: 
Yazım: highestsince (N.,koşul,Data) 
Koşulun gerçekleştiği en yakın “N”inci olaydan bu yana data serisinin aldığı en yüksek değeri 
hesaplar.  
→Örnek: highest since (2 , RSI()>80 ,C) fonksiyonunda, RSI değerinin 2. sefer 80 in üzerinde 
olduğu bardan bugüne kadar gerçekleşen en yüksek kapanış değerini verir. 
 
 Highest High Since Bars: 
Yazım: highestsincebars(N.,koşul,Data) 
Koşulun gerçekleştiği en yakın “N”inci olaydan bu yana data serisinin aldığı en yüksek değeri 
gördüğü bardan son bara kadar geçen bar sayısını hesaplar.  
→Örnek: highestsincebars(2 , RSI()>80 ,C) fonksiyonunda, RSI değerinin 2. sefer 80 in 
üzerinde olduğu bardan bugüne kadar gerçekleşen en yüksek kapanış değerinden son bara 
kadar olan bar sayısını verir. 
 
 Hour:  
Yazım: HOUR() Zamana bağlı koşul yazarken saati belirlemek için kullanabilirsiniz.  
 
 IF: 
Yazım: if(koşul,Then DA,Else DA)  
Koşul kısmına girilen koşul doğru ise, Then DA yerine yazılan işlem uygulanır, koşul yanlış ise 
Else DA yerine yazılan işlem uygulanır.  
→Örnek: if( C > mov(c,10,s), rsi(9), 0 ) Bu IF fonksiyonu örneği şu şekilde okunur:  
Eğer bu barın kapanışı, bu barın 10-barlık basit hareketli ortalamasından büyükse, 9-barlık bir 
RSI al / çiz, aksi halde bir şey yapma / sıfır çiz.

---

---

**📄 Source: PDF Page 16**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 16 / 107 
 
 
 INSIDE PREV BAR: 
Yazım: inside() 
İlgili barın bir önceki bara göre içte olması (o bar tarafından kapsanması) durumunda sonuç 
verir. İçte olmasının (Kapsanmasının) açıklaması: İlgili barın yükseğinin önceki barın 
yükseğinden küçük olması ve düşüğünün önceki barın düşüğünden büyük olması durumunda 
önceki barın içinde olduğu tanımı geçerli olur.  
 
 IsCurrExpDt: 
Yazım: IsCurrExpDt() 
 
Vadeli sembollerde, vadenin son gününü tanımlamak üzere oluşturulmuş bir fonksiyondur.  
Geçmiş barlar için çalışmaz. Sadece seans esnasında çalışır.  
Vadenin son günü için bir kurgu oluşturmanıza yardımcı olabilir. 
Mesela o gün pozisyon kapatmak gibi.  
 
 
 IsLastBrickClosed: 
Yazım: isLastBrickClosed() 
 
Renko grafiklere özel bir fonksiyondur. 
Geçmiş barlarla çalışan bir fonksiyon değildir. Sadece seans esnasında çalışır.  
Bar esnasında geçici olarak renko kutucuğu oluştu ise sıfır değerini alır. Bunun dışında daima 
1 değerine sahiptir.  
 
 
 
 
Mesela, ancak 2. Geçici kutucuk oluştuğunda bir sinyal almak için kullanılabilir.

---

---

**📄 Source: PDF Page 17**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 17 / 107 
 
 
 
 
 Kanal: 
Yazım: Kanal(Bar sayısı,Bitiş Noktası (bugün için 0, dün için -1),Y=yükselen D=düşen,%Seviye) 
Bu fonksiyon ile otomatik trende ek olarak paralel trendler çizebilirsiniz. %Seviye kısmına 
yazacağınız veri ile paralel trendlerin mesafesini ayarlayabilirsiniz.   
 
 Last Value: 
Yazım: Lastvalue(data serisi) 
İstenen datanın son hesaplanan değerini sabitleyerek data düzenine yüklenmesini sağlar. Bu 
fonksiyonun sonucu herhangi bir fonksiyonun içinde sabit olarak kullanılabilir.  
→Örnek: "lastvalue(rsi(14))" formülü, 14-günlük RSI indikatörünün son değerini getirir. Bu 
değeri sabitleyip grafiğe ekler. Böylece son değere göre bulmak istediğiniz farkı bulabilirsiniz. 
Eğer data serisi belirtilmezse, (örneğin, yalnızca 100-günlük data yüklendiğinde, 200-günlük 
hareketli 
ortalama 
değerini 
isterseniz, 
LastValue 
fonksiyonu 
sıfır 
döner.  
Bu fonksiyon, başka bir data serisinin son değeriyle birlikte tüm data serisini yüklemesi 
sebebiyle, bir formülün geleceği dönük olmasına izin vermektedir. Bu, pek çok indikatör için 
kabul edilemezdir ancak pattern tanımlama gibi konularda oldukça faydalıdır.  
 
 
 LineTo: 
Yazım: LineTO(Koşul,Data) 
Koşulun gerçekleştiği barları baz alır. O barların, data kısmında tanımladığınız verisini alır. 
Bunları bir çizgi ile birleştirir.  
 
Mesela:  
LineTO(cross(c,mov(c,10,e)),H) 
İfadesi fiyatın 10 luk hareketli ortalamayı kestiği barların H değerleri arasına çizgi çizer.  
 
 
 
Bu arada, çizilen bu çizgi, yükseliyorsa yeşil, düşüyorsa kırmızı renktedir.  
Dikkat: Koşulun tekrarlarını baz alır. Yukarıdaki örnekte, çizginin kırılımları, fiyatın 10 luk 
üssel ortalamayı yukarı kestiği noktalardır. Aşağı kesmeler yoktur.

---

---

**📄 Source: PDF Page 18**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 18 / 107 
 
 
 
 Load Daily Data: 
Yazım: LoadDaily("Sembol",DataSerisi O H L C W V TLVOL,PrevDayCount) 
Grafik sembolünün veya istenen bir sembolün önceki GÜN’lere ait temel fiyat verilerini 
getirir. Sembol kısmını boş bırakırsanız doğrudan grafik sembolü verileri gelir. Sembol yerine 
bir sembolün kısa kodunu yazarsanız o sembolün verileri gelir. PrevDayCount önceki 
günlerden hangisini seçeceğimizi belirlemek için kullanılır. 1 yazılması halinde önceki gün 
verileri gelecektir.  
İpucu: Bu fonksiyon alt periyotlarda (GÜN altı periyotlar) çalışır. Periyodu GÜN veya yukarısı 
seçerseniz çalışmaz. 
 
 Lowest:  
Yazım: Lowest(data serisi) 
Grafikte ilk bardan itibaren data serisinin en düşük değerini hesaplar.  
Lowest(RSI()) İlk datadan itibaren en düşük RSI değerini hesaplar.  
 Lowest Low: 
Yazım: LLV(Data,Periyot) 
Belirtilen periyotta data serisinin en düşük değerini hesaplar.  
→Örnek: LLV(RSI(),100) 100 Barlık periyotta en düşük RSI değerini hesaplar.  
 
 Lowest Since: 
Yazım: lowestsince(N.,koşul,Data) 
Koşulun gerçekleştiği en yakın “N”inci olaydan bu yana data serisinin aldığı en düşük değeri 
hesaplar.  
→Örnek: lowestsince(2 , RSI()>30 ,C) fonksiyonunda, RSI değerinin 2. sefer 30 un üzerinde 
olduğu bardan bugüne kadar gerçekleşen en düşük kapanış değerini verir. 
 
 Lowest Since Bars: 
Yazım: lowestsincebars(N.,koşul,Data) 
Koşulun gerçekleştiği en yakın “N”inci olaydan bu yana data serisinin aldığı en düşük değeri 
gördüğü günden bugüne geçen süreyi hesaplar.  
lowestsincebars(2 , RSI()>30 ,C) fonksiyonunda, RSI değerinin 2. sefer 30 un üzerinde olduğu 
bardan bugüne kadar gerçekleşen en düşük kapanış değerinden son bara kadar olan bar 
sayısını verir. 
 
 
 Maximum:  
Yazım: MAX(Data1,Data2) Data1 ve Data2 den büyük olanı seçer. 
 
 Minimum:  
Yazım: MIN(Data1,Data2) Data1 ve Data2 den küçük olanı seçer. 
 
 Minute:  
Yazım: MINUTE() 
Zamana bağlı koşul yazarken dakika belirlemek için kullanabilirsiniz. MINUTE()=10 
örneğindeki gibi yazılır. Dakikanın 10 olduğu zamanları bulur.

---

---

**📄 Source: PDF Page 19**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 19 / 107 
 
 
 
 Month:  
Yazım: MONTH()  
İlgili barda içinde bulunulan ayın rakamsal karşılığı (1-12) kullanılarak koşul oluşturulabilir. 
MONTH()=10 örneğindeki gibi yazılır. Ayın 10 olduğu barları seçer.  
 
 OUTSIDE PREV BAR: 
Yazım: outside() 
İlgili barın bir önceki barı kapsıyor olması durumunda sonuç verir. Kapsamanın açıklaması: 
İlgili barın yükseğinin önceki barın yükseğinden büyük olması ve düşüğünün önceki barın 
düşüğünden küçük olması durumunda önceki barı kapsıyor olduğu tanımı geçerli olur.  
 
 
 PEAK: 
Yazım: peak(Nth,DATA,%Min Chng) 
Zig zag indikatörünü temel alır. Tanımlanan yüzdelik orana göre, seçilen datanın dönüş 
yaptığı yüksek seviyeyi gösterir. Nth kısmı ile geriye doğru kaçıncı en yükseği baz almak 
istiyorsanız onu belirleyebilirsiniz.  
 
 
 
 PEAKBARS: 
Yazım: peakbars(Nth,DATA,%Min Chng) 
Zig zag indikatörünü temel alır. Tanımlanan yüzdelik orana göre, seçilen datanın dönüş 
yaptığı yüksek seviyeden itibaren geçen bar sayısını gösterir. Nth kısmı ile geriye doğru 
kaçıncı en yükseği baz almak istiyorsanız onu belirleyebilirsiniz.

---

---

**📄 Source: PDF Page 20**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 20 / 107 
 
 
 
 
 Power:  
Yazım: POWER(C,2) 
Belirtilen data serisinin üssünü alır. 
→Örnek: POWER(C,2) = karesi, POWER (C,3) = kübü ise POWER(C,4) = POWER(C,2)* 
POWER(C,2) 
 
 
 
 Rate of Change: 
Yazım: ROC(Data, Periyot, Yöntem % TL) 
Rate of Change fonksiyonu, belirlenen bir periyot üzerinden, bir data serisindeki puan veya 
yüzde olarak değişimi hesaplar. Yüzdesel veya puan değerleri, % veya TL olarak kısaltılabilir. 
→Örnek: ROC(C,12,%) formülü, 12-bar önceki kapanış fiyatına göre değişimini yüzdesel 
olarak gösterir. 
 
 Referans:  
Yazım: ref(data,periyot) 
Bir data serisinde, daha önceki değerleri getirmeyi sağlar. Negatif bir rakam girilmelidir.  
→Örnek: "ref(C,-12)" formülü, 12 bar önceki kapanış fiyatını gösterir. Buna göre, 12-günlük 
değişimi (puan olarak) "C-ref(c,-12)" olarak yazmak mümkündür.   
 
 Security Data: 
Yazım: Security(“Sembol”, DataSerisi O H L C W V TLVOL) 
Başka bir sembolün dilediğimiz bir datasını getirip, kullanmamızı sağlar.  
→Örnek: Security ( "DJI", C )  ,  Dow Jones kapanışını ifade eder. Grafikte hangi sembol olursa 
olsun, başka bir sembol (Burada Dow Jones) sabitlenecek ve o sembole ait değerler (Burada 
Kapanış) alınacaktır.  
 
 Sqr:  
Yazım: Sqr(Data)  Datanın karekökünü alır.

---

---

**📄 Source: PDF Page 21**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 21 / 107 
 
 
 Summation: 
Yazım: Sum(data,periyot) 
Bir data serisi üzerinde, bugünkü değer dahil belirlenen sayıda geriye dönük periyot kadar 
kümülatif toplama yapar.  
→Örnek: "sum(C,12)" formülü, son 12 dönemin kapanış fiyatlarının toplamını hesaplar. Buna 
göre, 12-günlük basit hareketli ortalama formülü: sum(c,12)/12 olarak yazılabilir.  
 
 
 TextOut: 
Yazım: TextOut(Koşul,txt Data,U D) 
Bu fonksiyon, içine yazılmış olan koşulun gerçekleştiği bara veri yazılmasını sağlar. Formül 
içinde tanımlayacağınız datanın bu bara denk gelen değerini veya tırnak içine alacağınız 
herhangi bir text’i, seçiminize göre, barın üstüne veya altına yazar. 
Örnek:  
TextOut(cross(c,mov(c,10,e)),L,D); 
TextOut(cross(c,mov(c,10,e)),"DKT",U) 
Formülü, grafik üzerine aşağıda göreceğiniz şekilde L datasının ve DKT harflerinin yazılmasını 
sağlar.  
Bunlar fiyatın 10’luk üssel H.O yu aşağıdan yukarı kestiği barın altına ve üstüne gelmektedir.  
 
 
 NOT: Data olarak barın fiyat verisine bağlı kalmak zorunda değilsiniz. O bara denk gelen RSI 
değerini de, mesela, grafik üstüne yazdırabilirsiniz.

---

---

**📄 Source: PDF Page 22**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 22 / 107 
 
 
 Trend: 
Yazım: Trend(Bar sayısı, Bitiş Noktası (bugün için 0, dün için -1),Y=yükselen D=düşen) 
Verilen parametrelere göre oluşturulan bir trendin bugünkü değerini verir.  
→Örnek: Trend (5,-1,D) genel yazılımı ile gösterilen trend fonksiyonu, 5 günlük, 1 bar önce 
sona ermiş Düşen trendin (D=Düşen, Y=Yükselen) bugünkü olması gereken değerini verir. 
Gerçekleşen değere bakarak trendin sonlanıp sonlanmadığını görebilme amacı ile 
kullanılabilir.   
 
 TROUGH: 
Yazım: Trough(Nth,DATA,%Min Chng) 
Peak fonksiyonu ile aynı işlevi düşük seviye için gerçekleştirir. Zig zag indikatörünü temel alır. 
Tanımlanan yüzdelik orana göre, seçilen datanın dönüş yaptığı düşük seviyeyi gösterir. Nth 
kısmı ile geriye doğru kaçıncı en düşüğü baz almak istiyorsanız onu belirleyebilirsiniz.  
 
 
 TROUGHBARS: 
Yazım: Troughbars(Nth,DATA,%Min Chng) 
Peakbars fonksiyonu ile aynı işlevi düşük seviye için gerçekleştirir. Zig zag indikatörünü temel 
alır. Tanımlanan yüzdelik orana göre, seçilen datanın dönüş yaptığı düşük seviyeden itibaren 
geçen bar sayısını gösterir. Nth kısmı ile geriye doğru kaçıncı en düşüğü baz almak 
istiyorsanız onu belirleyebilirsiniz.  
 
 Value When: 
Yazım: valuewhen(N (adım),koşul,Data) 
Koşulun doğru olduğu en yakın “n”inci  olayda data serisinin aldığı değeri hesaplar.  
→Örnek: Valuewhen(1,c=h,c) formülasyonu şu anlama gelir: 
Kapanış değerinin (C) en yüksek değere (H) eşit olduğu geriye dönük ilk seferdeki kapanış 
değerini verir. Eğer, parantez içindeki adım değeri 1 değilde 2 olsaydı koşulun gerçekleştiği 2. 
seferdeki kapanış değerini verecekti. 
 
 Year:  
Yazım: YEAR()  Yılı belirlemek için kullanılabilir.   
Ayrıca listelenmeyen ama oldukça kullanışlı bir fonksiyon daha vardır.  
 
İpucu: Bu listede görünmeyen bazı evrensel fonksiyonları da kullanabilirsiniz. Bunlarla ilgili 
açıklamayı dokümanın sonunda Ek Bilgiler kısmında bulabilirsiniz.

---

---

**📄 Source: PDF Page 23**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 23 / 107 
 
 
 
Bu pencerenin alt kısmında ise matematiksel (trigonometrik vb.) fonksiyonlar bulunur; 
 ABS   absolute 
 ATN  arctanjant 
 COS  Cosinus  
 EXP   Exponential 
 LOG  Logaritmik 
 SIN    Sinus 
 SQR  Square 
 TAN  Tanjant 
 
Bu fonksiyonları kullanırken yanlarına parantez ekleyiniz. Ve açıları radyan cinsinden yazınız.  
İpucu:  
Derece radyana nasıl dönüştürülür  
Derece cinsinden verilen değeri radyana dönüştürmek için değer 180 / π değeriyle çarpılır. 
Yani Radyan = Derece * (π / 180) şeklinde hesaplanır. 
π (Pi sayısı) = 3.14…. şeklinde giden özel bir sayıdır.  
Örnek 1: 180 derece kaç radyan eder? 
180 * (π / 180) = π radyan 
Örnek 2: 90 derece kaç radyan eder? 
90 * (π / 180) = 1,57079... radyan 
 
Sonuca ait bir örnek: 
Sin 90’ nin sonucu 1 değerini verir. 
Matriks içinde formülasyonu aşağıdaki gibi yaparsanız 
SIN(90/180*3.14)  
Bu ifadenin sonucu 1 olarak gelecektir.  
 
1.6 Alarm Sekmesi: 
İndikatör Builder penceresinin orta kısmında, indikatör yazımında kullanılacak verileri içeren 
bölüm vardır. Bu kısmın sol tarafında, dikine yazılı, Genel / Alarm ve Parametre butonları 
vardır. 
Genel sekmesi yukarda anlatılmıştır. Alarm sekmesi altında aşağıdaki görünüm karşınıza 
çıkar. 
 
 
İndikatör değeri belli bir seviyenin altına indiğinde ya da üstüne çıktığında uyarı vermesini 
sağlayacak ayarlamalar buradan yapılır.

---

---

**📄 Source: PDF Page 24**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 24 / 107 
 
 
Ayrıntılı bilgi aşağıda, örnek indikatör oluşturma esnasında verilmiştir. 
 
1.7 Parametre Sekmesi: 
Parametre içeren bir indikatör yazdığınız takdirde bu sekme aktifleşir. 
 
 
 
Yukarıdaki örnekte görebileceğiniz gibi, indikatör içeriğinde veri girişi ( Input komutu ile 
parametre seçimi) söz konusu olur ise, indikatörün uygulanması aşamasında buradan 
değişiklik yapabilirsiniz. Parametre içermeyen indikatörlerde bu sekme aktif olmaz. 
 
 
1.8 Tanım Kısmı: 
 
 
İndikatör Builder penceremiz ilk açıldığında bu kısım boştur. İndikatör oluşturmaya 
başladığımızda, yazacağımız her türlü tanım burada görünecektir. 
Ayrıntılı bilgi aşağıda, örnek indikatör oluşturma esnasında verilmiştir.  
1.9 Diğer Detaylar: 
Pencerenin alt kısmında oluşturacağımız indikatörün görsel ayarlarını belirlememizi 
sağlayacak seçenekler sunan kısımlar vardır.  
 
 
 
Bu kısımla ilgili daha ayrıntılı bilgi, örnek indikatör oluşturma esnasında verilmiştir.

---

---

**📄 Source: PDF Page 25**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 25 / 107 
 
 
1.10 İndikatör Oluşturma:  
İndikatör oluşturmak için Genel sekmesi altındaki verilerden faydalanırız.  
 
DİKKAT: İndikatör kısaltmaları harf ile başlamalıdır. Rakamla başlatmayınız. 
 
1.10.1 Örnek Yazım (Hareketli Ortalama): 
İlk aşamada var olan indikatörlerden birisini nasıl tanımlayacağımızı görelim.  
Yazacaklarımız, bir analiz yapabilmek için oluşturulan bir takım formüller şeklinde olacaktır 
ve pencerenin ‘tanım’ kısmında görülecektir. 
İndikatörler penceresinden bir indikatör üzerinde çalışalım. 
 
Kullanacağınız indikatöre çift tıklarsanız, indikatörün genel yazım formatı ‘Tanım’ kısmında 
görünür.  
Örneğin indikatör penceresinden Moving Average / Hareketli Ortalama (MOV) üzerine çift 
tıkladığınızda Tanım penceresinde  
MOV(Data,Period,Yöntem S E W TRI VAR ZL WW TSF HAR E2)  ibaresi görünür.  
 
 
 
İpucu: Tanım kısmının hemen sağında bulunan minik + - butonları ile yazı karakterini büyütüp 
/ küçültebilirsiniz. 
 
 
Parantezin içinde bulunan tanımlar / kısaltmalar kullanıcılara yol göstermesi için 
bulunmaktadır. Yapmanız gereken bu parantezin içine istediğiniz / uygun parametreleri 
yazmaktır.  
İpucu: Parantez, virgül, noktalı virgül, tırnak işaretlerine dokunmayınız. Bunların dışında 
gördüğünüz tanımların yerine ilgili veriyi yazınız.  
 
Data Herhangi bir işlem yaparken kullanabileceğimiz herhangi bir veri olabilir. 
Mesela, indikatörler mini penceresinin hemen sağındaki ‘Alanlar’ penceresi içinde 
görebileceğiniz kapanış, açılış, yüksek, düşük gibi bir veri olabileceği gibi başka bir indikatör 
de olabilir.  
 
Moving Average indikatörü ile ‘Kapanış fiyatlarının 5 günlük basit ortalamasını’ yazmak 
istediğimizi düşünelim. 
Bu durumda burada Data olarak kullanacağımız veri KAPANIŞ’tır. Tanımın, ‘Data’ yazılı 
kısmına, kapanış verisinin gelmesi gerekir. 
Bu sebeple, öncelikle Data yazısını silip onun yerine c yazıyoruz. C (close) kapanış fiyatıdır. 
Bunun açıklaması ‘Alanlar’ kısmında verilmiştir. Buraya klavye ile ‘c’ harfini yazmak yerine,

---

---

**📄 Source: PDF Page 26**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 26 / 107 
 
 
tanım alanında C harfi üzerine çift tıklayarak da aşağıya alabilirsiniz. Tabii bu işlemi, imleç 
Data’nın yazılacağı yerde iken yapmalısınız. Böylece C harfi Data yazan kısma gelecektir.  
Büyük ya da küçük harf kullanabilirsiniz. Şimdi görünüm aşağıdaki gibi olacaktır. 
MOV(c, Periyot, Yöntem S E W TRI VAR ZL WW) 
Sonra periyodumuzu belirliyoruz.  
Her indikatörün daha anlamlı / sağlıklı sonuçlar verdiği periyotlar vardır. Bu konudan 
indikatörler kısmında bahsedilmiştir.  
Bizim örneğimizde kararlaştırdığımız periyot 5’tir. Periyod yazısını silip yerine 5 yazıyoruz.  
 
DİKKAT: Aradaki virgülleri silmiyoruz. Parantez, tırnak vb işaretlere dokumuyoruz. 
Şimdi görünüm şöyle olacaktır: MOV(c,5,Yöntem S E W TRI VAR ZL WW TSF HAR E2)   
 
İpucu: Formüller büyük küçük harf duyarlı değildir.  
 
Yöntem Belirleme:  
Son olarak, ortalamayı alma yöntemimizi belirleyen seçimi yapıyoruz. Burada yöntemden 
kasıt ortalamayı hesaplama metodudur. Ve aşağıda listelenen seçeneklerden birisi vasıtası ile 
yapılabilir. 
 
 S – Simple (Basit) Verilerin hepsi eşit ağırlığa sahip olarak kullanılır. Mesela son 5 
günün kapanış ortalamasında, 5 kapanışın toplamı 5’e bölünerek bulunur. 
 
 E – Exponential (Üssel) Son gün en ağırlıklı olmak üzere, son günden geriye doğru 
ortalama ağırlıkları üssel olarak hesaplanır.   
 
 W – Weighted (Ağırlıklı) Ağırlık son günlere kaydırılır. Mesela 1. gün 1 ile 2. gün 2 ile 
……5. gün 5 ile çarpılır. Toplam 15 e ( 1+2+3+4+5) bölünür. 
 TRI – Triangle (Üçgensel) Seçilen periyotta ortada kalan barlara daha fazla ağırlık 
vererek hesaplama yapar. 
 VAR – Variable (Değişken) Ağırlık verme noktalarını değişken olarak alır. 
 
 ZL - Zero Lag Fiyat ile ortalama arasındaki açıklığı olabildiğince daraltmayı hedefleyen 
bir indikatördür. Fiyat hareketlerine daha duyarlı bir grafik verir. 
 
 WW - Welles Wilder Bu ortalama şeklini türeten analistin adı ile anılmaktadır. Ağırlıklı 
ortalamaya benzer. Eski fiyatlar ağırlıklı ortalamaya daha az katkı sağlarken, yakın 
tarihli fiyatlar, ortalama üzerinde daha fazla ağırlık sahibidir.  
 
 TSF – Times Square Forecast TSF indikatörünün moving average içine işlenmiş halidir. 
Talep üzerine eklenmiştir.  
 
 TSF – Times Square Forecast TSF indikatörünün moving average içine işlenmiş halidir. 
Talep üzerine eklenmiştir.  
 
 HAR – Harmonic Oldukça çok bilinen harmonic ortalamanın kullanılmasını sağlar.

---

---

**📄 Source: PDF Page 27**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 27 / 107 
 
 
 E2 – Exponential (Üssel) Versiyon 2 Önceki üssel hareketli ortalamadan farkı şudur:   
Bazı kurumlar üssel hesaplamasının ilk barında basit hareketli ortalamayı kullanarak 
başlamaktadır. Bu da bir fark oluşturmaktaydı. Gelen talepler üzerine her 2 seçeneği 
de ekledik. İlk barlarda değerler arasında farklar oluşur. İlerleyen barlarda bu fark 
kaybolur.  
Yukarıda belirttiğimiz gibi kapanışın 5 günlük basit ortalamasını yazacağımız için yöntem 
kısmını silip yalnızca S harfini bırakıyoruz. Ve indikatörümüz son şeklini alıyor: 
MOV(c,5,S). Bu formülü indikatör builder üzerinde yazıp, grafiğin üzerinde gösterilmesini 
sağlarsanız, aynı grafik üzerinde hazır olarak sağlanan hareketli ortalama indikatörü ile 
birebir aynı çizgiyi çizecektir.  
Buraya kadar hazırladığımız, zaten var olan bir indikatörün verilerini yerleştirip, indikatör 
builder üzerinde yazmak oldu.   
 
 Uygulama: Yukarıda bahsettiğimiz ortalamalardan bir kısmının grafik üzerindeki 
görünümü aşağıdaki gibidir.  
 
 
1.10.2 Data Olarak İndikatör Kullanmak:  
Data olarak indikatör kullanımını bir örnekle görelim. 14 günlük RSI’ın 5 günlük hareketli 
ortalamasını bulmak istediğimizi varsayalım.  
 
Önceki örnekte C (kapanış) yazdığımız Data kısmına, bu sefer 14 günlük RSI yazmamız gerekli 
ve yeterli olacaktır.  
Bunu yapmak için RSI formatını ezbere bilmek zorunda da değiliz.  
Önce indikatörlerden ortalama hesaplayan MOV üzerine çift tıklayıp, formülünün aşağıdaki 
Tanım kısmına geçmesini sağlayınız. Bunu yukarıda anlatmıştık. 
 
Bu sefer, tanım kısmında MOV (Data, Periyot, Yöntem S E W TRI VAR) içinde, data yazısı 
yerine tıklayınız. Sonra da, yukarıdaki indikatörlerden RSI üzerine çift tıklarsanız RSI formatı 
aşağıda data yerine gelir. MOV indikatörü için, periyod olarak 5, yöntem olarak da gene 
simple (s) seçerseniz aşağıda göreceğiniz formül ortaya çıkar. 
MOV(RSI(Data, Periyot),5,s))

---

---

**📄 Source: PDF Page 28**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 28 / 107 
 
 
→Burada yapmaya çalıştığımız şudur: 
Önceki örnekte kapanışların 5 günlük basit ortalamasını alıyorduk. Bu aslında hazır indikatör 
olarak zaten var. Eğer, bir başka indikatörün mesela RSI’ın 5 günlük basit ortalamasını almak 
istersek yukarıdaki formata uygun veriler girmeliyiz. Ve bunun sonucunda elimizde RSI’ın 5 
günlük basit ortalamasını alan, yeni bir indikatör oluşur. 
Yukarıdaki tanımda, RSI(Data,Periyot) kısmı, RSI indikatör kısmıdır. Bunun içindeki 
değişkenleri de tanımlamamız gerekir.  
Data olarak kapanışları girelim. Tabii ki, hedefimize / yaklaşım tarzımıza göre başka bir data 
da girebiliriz. Periyot olarak ise 14 girdiğimizi düşünelim. 
Son görünüm şöyle olacaktır: 
MOV(RSI(c,14),5,S)   Bu indikatör, uyguladığımız senedin, kapanışlar ve 14 günlük periyot için 
oluşan RSI değerlerinin 5 günlük periyotlar için basit ortalamasını hesaplayacaktır.  
Eğer, yazım esnasında herhangi bir hata yapar isek, kaydet tuşuna bastığımızda, program bir 
hata olduğunu gösteren uyarı penceresi açacaktır.  
 
Mesela yukarıdaki formülü MOV(RSI(c,14),5,s)) şeklinde yazarsak ( en sonda fazla bir 
parantez vardır) ve kaydet tuşuna basarsak, aşağıdaki uyarı penceresi gelecektir.    
 
 
 
Dikkat: Sistem somut hataları tanımakla birlikte, tüm hataları tanımayacaktır. Bu sebeple 
özellikle öğrenme aşamasında yazdıklarınızın doğruluğunu teyid edecek kontroller yapınız.  
 
1.10.3 Alarm Tanımlama:  
 ‘Alarm’ sekmesini tuşladığınızda, indikatör penceresinin orta kısmında aşağıdaki görünümün 
geleceğinden bahsetmiştik.   
 
 
 
İndikatör değeri belli bir seviyenin altına indiğinde ya da üstüne çıktığında grafik üzerinde 
uyarı vermesini sağlayacak seçenekler vardır.

---

---

**📄 Source: PDF Page 29**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 29 / 107 
 
 
Bunun için alt ve üst sınır koymanın daha anlamlı olduğu bir indikatör seçip, onun üzerinde 
çalışalım.  
Alarm seviyesi belirlemek için, yazdığınız / kullandığınız indikatörün özelliklerini bilmeniz 
faydalı olacaktır. Mesela RSI için sınır seviyeleri 30 ve 70 tir. 30 un altı aşırı satış, 70’in üstü 
aşırı alım sinyali demektir.  
Bu durumda alarm seviyesi olarak alt sınırı 30 ve üst sınırı 70 seçmemiz bir anlam ifade eder. 
 
 
 
Yukarıda göreceğiniz üzere, üst seviye ve alt seviyeleri el ile yazdık. 
Alarm rengi için renk kutucuğunun üzerine tıklayarak açılacak pencereden renk seçimi 
yapabiliriz.  
Grafik üzerinde Göster seçeneğini işaretlersek, alarm seviyelerini grafik üzerinde gösterir. 
Alarm Ver seçeneğini işaretlersek, alarm koşulu gerçekleştiğinde, ‘İndikatör Seviye Alarmı’ 
penceresi açılarak uyarı verir. 
 
 
 
 
Bunun altındaki pencerede, Seviye / Bölge seçeneği vardır.  
Seviye seçimi, grafikte alarm sınırının bir çizgi olarak görünmesini sağlar.

---

---

**📄 Source: PDF Page 30**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 30 / 107 
 
 
Alarm ver seçeneği işaretlendi ise, seviye aşıldığı anda alarm verilmesini sağlar. Ve seviyenin 
üstünde kalındığı sürece, finansal enstrüman işlem gördükçe alarm verir. 
 
Bölge seçimi, grafikte alarm koşuluna uyan tüm bölgenin ilgili renge boyanmasını sağlar.  
 
 
 
Alarm ver seçeneği işaretlendi ise, aynen seviye seçiminde olduğu gibi, seviye aşıldığı anda 
alarm verilmesini sağlar. Ve seviyenin üstünde kalındığı sürece, finansal enstrüman işlem 
gördükçe alarm verir. 
Uygula tuşuna bastığımızda, verdiğimiz alarm koşulları indikatöre eklenmiş olur. 
 
 
Bir indikatörün kendi içinde alarm tanımlamak: 
İndikatör parametre penceresi üstünde alarm seviyeleri butonu vardır.  
 
 
 
Alarm Seviyeleri butonuna bastığınızda, alarm tanımlaması yapmanıza olanak veren ‘Alarm 
Seviyeleri’ penceresi açılır.

---

---

**📄 Source: PDF Page 31**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 31 / 107 
 
 
 
 
Bu pencere üzerindeki işlevler, yukarıda anlatılan alarm tanımları kısmındaki işlevlerle 
aynıdır.  
Yukarıda anlatıldığı şekilde alarm tanımladıktan sonra, tamam butonuna basarsanız, alarm 
tanımlanmış olarak bu pencere kapanır. 
 
Burada dikkat edilmesi gereken nokta şudur: 
İndikatörün parametre penceresinde, 
 butonu vardır. 
Alarmımızın kalıcı olmasını istiyorsak, bu tuşa basarak alarm için verdiğimiz değerlerin ön 
tanımlı olarak kalmasını sağlarız. 
Alarmı iptal etmek istersek, tekrar alarm seviyeleri penceresine gelip, tanımları ve seçimleri 
iptal ettikten sonra, tamam butonuna basmamız ve indikatör parametre penceresinde, 
tekrar
 butonunu tuşlamamız gereklidir. 
 
 
 
1.10.4 İndikatör Builder Penceresinin Diğer Açıklamaları: İndikatör Builder Penceresinin alt 
kısmından yapacağımız tanımlamalar şunlardır:  
 
 
 
Grafik Üzerinde Göster butonu ile tanımlı indikatörler kısmında listelenen indikatörlerden 
istediğinizi, üzerine tıklayarak seçtikten sonra,  
 
 grafik üzerine uygulayabilirsiniz.

---

---

**📄 Source: PDF Page 32**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 32 / 107 
 
 
Bölge kısmında, oluşturacağımız indikatörün grafiğini hangi bölgeye (Ayrı bir pencere / data 
penceresi üzerine)  atmak istediğimizi seçebiliriz.  
 
Combo penceresi: Kaydet tuşuna bastığımızda burada indikatör kısaltması görülür.  
 
Burada bir parantez açıp ek bilgi vermemizde fayda vardır: 
 
Değişken Tanımlanması ve Çok Çizgili (Satırlı) İndikatör Yazılması 
 
Bazen indikatör yazarken değişken tanımlamak işimizi kolaylaştırabilir. Aynı parametreyi 
birkaç yerde kullanacak isek bir değişken tanımlarız. Ve burada yapacağımız tek bir değişiklik 
ile bu değerin kullanıldığı her yerde veriyi değiştirebilmiş oluruz.  
 
 
 
Yukarıda a ve b değişkenleri tanımlanmıştır. 
 
İpucu: Yukarıda dikkat ederseniz, satır sonlarına ; (noktalı virgül) konmuştur. Bu matriks 
dilinde bu satır bitti demektir.  
Formülü, 
a:=10; b:=50; mov(c,a,s); mov(c,b,s) şeklinde de yazsanız aynı sonucu alırsınız. 
Araya ; koymazsanız hata mesajı alırsınız. 
Dikkat: En son satırın sonuna ; konmaz. Böylece formülün bittiği anlaşılır.  
 
Bazı indikatörler birden fazla çizgi içerirler. İndikatör oluştururken dilersek çok sayıda çizgi 
içeren bir indikatör oluşturabiliriz. Üstte yazılmış olan indikatör aynı zamanda bunun bir 
örneğidir.  
İlk 2 satır değişken içerir. 
Son 2 satır ise çizgi oluşturacak tanımlamalardır. 
Yukarıdaki formül 2 tane çizgi çizer. 
10 Barlık basit hareketli ortalama ve 50 barlık basit hareketli ortalama. 
İndikatör 1’den fazla satır içerdiğinde Combo kısmında L1,L2,… şeklinde satır numaraları 
görünür.

---

---

**📄 Source: PDF Page 33**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 33 / 107 
 
 
Combo penceresinde hemen sağındaki Ok’a tıkladığınızda, buradan satırları seçebilir ve 
sağda kalan seçim hücreleri ile görünüm ayarlarını yapabilirsiniz.  
 
Satırlara ayrıca isim verebilirsiniz: 
Normalde satır isimleri L1, L2 şeklinde görünür. 
Klavyeden L1 yerine vermek istediğiniz ismi yazınız. 
 
 
 
Ve klavyeden Enter yapınız. 
Aynı şeyi sonraki satırlar için de yaparsanız, her satıra isim vermiş olursunuz ve görünüm 
aşağıdaki gibi olur.  
 
 
 
 
Renk Penceresi: Buraya tıkladığınızda renk seçim penceresi açılır. Buradan, indikatör 
çizgisinin grafik rengini seçeriz. 
 
Yükselen / Düşen Renk: Fiyat düne göre yükselmişse yükselen, düşmüşse düşen rengi 
aktifleşir. 
 
Çizgi penceresinden çizgi tipini seçebilirsiniz. 
 
  Düz çizgi / histogram / Nokta (lı çizgi)  seçenekleri vardır. 
 
Kalınlık Penceresinden çizgi kalınlığını ayarlayabilirsiniz.  
 
Öteleme penceresinden çizgiyi (Datayı) kaç bar öteleyeceğinizi belirleyebilirsiniz.  
 
En alt bantta bulunan butonlar: 
 
Gönder / Al butonu: Bu butonları kullanarak elinizde var olan bir indikatörü bir başka 
kullanıcıya gönderebilir veya başka bir kullanıcıdan indikatör alabilirsiniz. 
Bu konu Sistem Tester altında 4.1.4 Sistem Gönder başlığı altında detaylı anlatılmıştır.

---

---

**📄 Source: PDF Page 34**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 34 / 107 
 
 
Burada tek fark dosya uzantısının  .mib olmasıdır. Ve e-posta ile doğrudan gönderilebilir.  
 
Yardım Butonu: Matriks indikatör builder yardım sayfasına gider.   
 
Kaydet Butonu ile indikatörünüzü kaydedersiniz. İndikatör yazımında hata var ise, ‘yazım 
hatası’ uyarısı gelir. Kaydettiğinizde, oluşturduğunuz indikatör kısa adı ile indikatörler 
penceresine eklenir.  
 
 
 
Ayrıca, tanımlı indikatörler altında listelenmekte olan indikatörler üzerine tıkladığınızda, o 
indikatörün tanımlarını görebilir ve bunlar üstünde değişiklik yaparak son halini 
kaydedebilirsiniz. 
 
Sil tuşu ile tanımladığınız indikatörlerden kullanmayacaklarınızı silebilirsiniz. 
 
Kapat Tuşu ile İndikatör Builder penceresini kapatırsınız. 
 
1.10.5 Öteleme İçin Örnek:   
Bazı durumlarda, bir sinyalden emin olmak için, ek bir süre daha geçip, sinyalin daha kalıcı 
olmasını tercih edebiliriz. Bu gibi durumlarda verinin ötelenerek gelmesini sağlamak pratik 
bir çözümdür. Bunun için, fonksiyonlardan ‘Referans’ fonksiyonunu kullanırız.  
Ötelemeyi rahatça görmek için önce cross ile kesişim noktalarını göreceğimiz bir indikatör 
yazalım. İndikatörler listesinden cross üzerine çift tıklarsak, tanım alanına aşağıdaki 
formülasyon gelir. 
 
 
Cross fonksiyonunun özelliği, 2 ayrı datanın birbirini kestiği noktaları belirlemeyi 
sağlamasıdır. Birinci data serisinin, ikinci seriyi yukarı kestiği anda, "+1" değeri verir, aksi 
halde "0" değeri verir. 
Data 1 ve Data 2 olarak 5 ve 14 günlük hareketli ortalamaları alalım. Bunların kesişimi bize 
bazı sinyaller üretecektir. 
Cross(Data1,Data2) olarak yazmalıyız. Verileri yerleştirdiğimizde: 
Cross(MOV(C,5,E),MOV(c,14,E)) sonucunu alırız. 
Bazen tam kesişimin olduğu barda değil de bir sonraki barda alım sinyali vermesini tercih 
edebiliriz. (Mesela bu örnekte, kapanıştan önce AL vermesine rağmen kapanışta AL dışında 
kalabilir diye)  
Ötelemeyi grafik üzerinde daha net görebilmek için 2 gün olarak seçelim. 
Verileri yerleştirdiğimizde:

---

---

**📄 Source: PDF Page 35**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 35 / 107 
 
 
REF(Cross(MOV(C,5,E),MOV(C,14,E)),-2) sonucunu alırız. Bu 
2 
indikatörü alt alta 
uyguladığımızda: 
 
 
 
 
Öteleme durumunu çok rahatça görebilirsiniz.  
 
2. İndikatör Pozisyonları 
KHN menüsü altındaki İndikatör Pozisyonlarına tıkladığınızda açılan sayfada ön tanımlı 5 adet 
indikatör göreceksiniz.  
Bu indikatörlerden istemediklerinizi çıkarabilir ve yeni indikatörler ekleyebilirsiniz. Nasıl 
yapabileceğiniz aşağıda anlatılmıştır. 
Seçilen semboller için, listede bulunan indikatörlerin her birine özel olarak tanımlanmış olan 
koşullara göre, vereceği AL ve SAT sinyallerini bir tablo halinde sunar. İndikatör Pozisyonları 
Penceresi ilk açıldığında aşağıdaki görünüme sahiptir. 
 
 
 
2.1 Genel Görünüm:  
Üst banttaki menüler sonraki maddelerde anlatılmıştır. 
Onun altında bulunan kısımdaki tanımlama araçlarının kullanımı şöyledir:

---

---

**📄 Source: PDF Page 36**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 36 / 107 
 
 
2.1.1 Periyod: Periyod ön tanımlı olarak günlüktür.  
 
 
İsterseniz buradan farklı bir periyod seçebilirsiniz. 
 
2.1.2 Birim:  
Ön tanımlı birim TL’dir. Dilerseniz başka para birimleri, endeks / enflasyon / başka bir senet 
bazında da hesaplama yapılmasını sağlayabilirsiniz. Bu mini penceredeki alt birimlerden 
‘senet’ seçerseniz hemen sağında senet seçimi yapabileceğiniz bir mini pencere açılır: 
 
 Bu sayede, seçtiğiniz finansal enstrümanların bir 
başka finansal enstrümana göre değişimlerini de analiz edebilirsiniz. 
 
2.1.3 Sinyali Son ….. Barda Ara:  
Normalde program 5.000 – 8.000 birimlik periyotta işlem yapar. Bunu gereksiz bulabilirsiniz. 
Daha hızlı sonuca ulaşmak isteyebilirsiniz. Bu durumda bu seçeneğin başındaki mini kutucuğu 
işaretleyip, istediğiniz bar ( periyod birim) sayısını aradaki mini pencereye yazmanız gerekir. 
Örnek: 
 Bu şekilde işaretleyip doldurduğumuzda, program analizi 
/ hesaplamayı son 100 periyot birimi ( gün / seans vb.) için yapacaktır. 
2.1.4 ….. dk. da Bir Yenile: 
İndikatör pozisyonları işlevini sürekli açık tutuyorsanız, özellikle seans içinde eklenecek yeni 
verilerle sonuçlarda değişiklikler olabilir. Bunun için hesaplamayı seçtiğimiz süre periyodunda 
yenileyerek yapmasını sağlayabiliriz. 
Örnek: 
 Bu durumda, 5 dk. da bir sonuçlar yenilenecektir. 
 
2.1.5 Hesapla Butonu:  
Seçimlerinizi ve tanımlamalarınızı yaptıktan sonra, programı çalıştırmanızı sağlar. Program 
hesaplamaları yapıp sonuçları bir tablo halinde size sunar. 
Yardım Butonu: 
 Matriks yardım menüsünü açar. 
2.1.6 Sütun İçerikleri:  
 
 Sembol sütunu altında, analizini yapmak için seçtiğiniz sembolleri görürsünüz. 
 
 Son sütunu altında, o satırdaki sembolün son fiyatını görürsünüz.

---

---

**📄 Source: PDF Page 37**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 37 / 107 
 
 
 
 Sonraki sütunlar ön tanımlı olarak programa yerleştirilmiş olan 5 adet indikatöre 
aittir. 
  
 
 Bu sütunlarda, bu indikatörlere göre ortaya çıkan AL / SAT sinyallerini tarihleri ile 
görürsünüz. 
 
 Ön tanımlı olarak var olan indikatörlerle ilgili kısa tanımlar şöyledir: 
 
 MTX Mov(5,22) 5 ve 22 günlük ortalamaların kesişimine göre oluşan sinyaller. 
 
 MTX Rsi(30/70) RSI indikatörünün 30 ve 70 sınır değerlerini kesmesine göre oluşan 
sinyaller. 
 
 MTX Stocs Stochastic Slow indikatörünün 2 çizgisinin birbiri ile kesişimi sonucu oluşan 
sinyaller. 
 
 MTXPosc Price Oscilatör indikatörü ile kendi hareketli ortalamasının kesişimi sonucu 
oluşan sinyaller  
 
 MTX Macd Macd indikatörünün 2 çizgisinin (Macd ve Macd Trigger) birbiri ile kesişimi 
sonucu oluşan sinyaller. 
 
 Dilerseniz, bu indikatörlerden istemediklerinizi çıkarabilirsiniz. Dilerseniz, Matriks 
programı altında var olan indikatörlerden seçip, değişkenlerini ve koşulu 
tanımlayabilir ve tabloya ekleyebilirsiniz.  
2.2 Sembol Seçimi:  
Ekranın sol üst kenarından Sembol Seçimi tuşuna bastığınızda sembolleri seçebileceğiniz bir 
pencere açılır. Buradan analiz etmek istediğiniz sembolleri seçebilirsiniz.  
2.3 İndikatör Seçimi: 
Yeni bir indikatör eklemek isterseniz İndikatör Pozisyonları penceresinin üst bölümünde 
İndikatör Seçimini tıklamanız gerekir. Bu butona tuşladığınızda aşağıda göreceğiniz ‘Kolon 
Seçimi’ penceresi açılır.

---

---

**📄 Source: PDF Page 38**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 38 / 107 
 
 
 
 
Var olan 5 adet indikatörü ekranda göreceksiniz.  
 
2.3.1 Yeni Kolon Ekle butonuna tıklarsanız Kolon Düzenle penceresi açılır.  
Bu modülde kullanıcılar, diledikleri indikatörler için, diledikleri AL-SAT kurallarını, var olan 
koşul oluşturma seçeneklerinden birini (veya birkaçını) seçerek tanımlayabilirler.  
 
 
 
Burada öncelikle yeni kolonumuza bir isim veriyoruz. MTXtest diyelim.

---

---

**📄 Source: PDF Page 39**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 39 / 107 
 
 
 
Gösterge Seçiniz:  
Bu kısımda kullanacağımız indikatörü seçiyoruz. Örnek olarak Moving Average seçelim.  
Gösterge seçim mini penceresinin hemen yanındaki Parametreler bölümünde, seçilen 
indikatöre göre, değerler verebileceğiniz parametreler ( Data vb.) penceresi açılacaktır. Bu 
konuda ayrıntılı bilgi için Matriks Grafik dokümanında ilgili başlığa bakabilirsiniz.  
Grafik üzerinde bulunan indikatörler butonu ile açılan ‘indikatör’ penceresi içinde, indikatör 
adı üzerine çift tıkladığımızda açılan pencere ile aynıdır.  
Bu pencere ile parametreleri belirleyebilir ve görsel düzenlemeler yapabilirsiniz. 
 
 
Burada sadece parametreleri belirlemek için kullanacağız.  
 
 Periyot kısmından indikatörün kullanmasını istediğimiz periyot verisini giriniz.  
  
 Veri Tipini seçebileceğimiz kısımdan, hangi datayı veri olarak girmek istediğinizi 
seçiniz. Normalde burada ‘Kapanış’ datasını seçiyoruz. 
 
 Hesaplama Yöntemi kısmından hangi tip ortalamayı istediğimizi seçeriz. Burada Basit 
( Simple) yöntemini seçiyoruz. 
 
 Bölge kısmında, oluşturacağımız indikatörün grafiğini hangi bölgeye (Ayrı bir pencere 
/ var olan bir data penceresi üzerine)  atmak istediğimizi seçebiliriz.  
 
 Öteleme kısmına, analizin ötelenerek yapılmasını istiyorsak, öteleme istediğimiz 
periyot miktarını yazarız.  
 
 Tamam tuşu ile yaptığınız değişiklikler kaydedilip bu pencere kapanacaktır. 
 
 İptal tuşu ile yaptığınız değişiklikler kaydedilmeden bu pencere kapanacaktır. 
 
 Default olarak kaydet tuşu ile bu pencerede verdiğiniz son parametreler ön tanımlı 
hale gelecektir. Bundan sonra değiştirmediğiniz sürece bu parametreler ile işlem 
yapacaktır. Bunu seçmediğiniz takdirde, yaptığınız değişiklikler 1 defaya mahsus 
uygulanacaktır. Bir sonraki sefer indikatör pozisyonlarını kullandığınızda, daha

---

---

**📄 Source: PDF Page 40**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 40 / 107 
 
 
önceden ön tanımlı olan parametreler ne ise, o parametreleri kullanarak hesaplama 
yapacaktır. 
 
Koşul Belirleme: Kolon Düzenle Penceresinin gösterge seçiminin altındaki bölümlerinde, 
koşul belirleme kısımları vardır.   
Bu kısımda en olası koşul belirleme seçeneklerini göreceksiniz. Bunların içinden, o indikatöre 
uygun olanı (olanları) kullanarak koşullar belirleyebilirsiniz. 
 
Uygulamak istediğimiz koşulun başındaki kutucuğa tıkladığınızda, o koşulu uygulayacağınızı 
belirtmiş olursunuz. Sonra da koşulunuzu belirleyiniz.  
İndikatörler hakkında ayrıntılı bilgi için Bakınız: İndikatörler isimli doküman. 
 
Fiyat Serisi ile Kesişim: 
Seçilen indikatör değeri ile senet fiyatı arasında, seviye karşılaştırması yaparak sinyal 
verilmesini sağlar. 
 
Fiyat verisi olarak yukarıda göreceğimiz seçeneklerden herhangi birisini alabiliriz. 
 
 
 
Bu örnekte indikatörümüz olan Moving Average ile seçtiğimiz fiyat verisini karşılaştırmak için 
yukarıdaki seçeneklerden birini belirleyebilirsiniz. 
Burada şunu bilmemiz gerekiyor: Normalde Fiyatın, Moving averajın üzerinde olması AL 
durumu, altında olması SAT durumudur. 
Sinyalin tam kesişim anında gelmesini tercih ederseniz, seçiminizi ona göre yapınız.   
 
Seviye Kontrolü: 
Burada, indikatör değerimiz belli bir rakamın seviyesini aştığında ( aşağı ya da yukarı olabilir) 
sinyal vermesini istiyorsak, seviye kontrolü işaretlenir ve seviye rakamı belirlenir. 
RSI, Stochastic, DI+ DI- gibi seviyelere göre sinyal oluşturan göstergeler için, seviye kontrolü 
yardımıyla AL ve SAT sinyali tanımlaması yapılabilir.  
 
Örneğin, RSI göstergesi için bir sabit değer tanımlanarak (örneğin 20); bu değere eşit, büyük 
veya eşit, küçük, küçük veya eşit, bu seviyeyi yukarı kırınca veya bu seviyeyi aşağıya kırınca 
AL veya SAT sinyalinin üretilmesi sağlanabilir.

---

---

**📄 Source: PDF Page 41**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 41 / 107 
 
 
Moving Average gibi, doğrudan sembol fiyatından üretilen göstergelerde, değişken değerler 
söz konusu olduğundan, Seviye Kontrolü kullanmak anlamlı değildir.   
 
 
 
Hareketli Ortalaması ile Kesişim: 
İndikatör ile indikatörün kendi hareketli ortalaması kesiştiğinde sinyal verir. Burada da, bu 
değere eşit, büyük veya eşit, küçük, küçük veya eşit, bu seviyeyi yukarı kırınca veya bu 
seviyeyi aşağıya kırınca seçenekleri vardır. 
 
 
 
 
Önceki Değeri İle Karşılaştırma: 
Seçilen göstergenin, bir önceki değeri ile karşılaştırılması sonucunda oluşan duruma göre AL 
veya SAT sinyali üretmesi tanımlanabilir. Bu seçenekte, bir göstergenin bir önceki değerinden 
büyük, büyük eşit, eşit, küçük eşit, küçük olması veya önceki değer aşağı döndüğünde/yukarı 
döndüğünde AL veya SAT sonucu alınabilir.    
 
 
 
Bu uygulama, indikatör için yükselen düşen renklerinin kullanılmasına ve buna göre sinyal 
üretilmesine eşdeğer bir uygulamadır. 
 
Başka Bir Gösterge İle Kesişim:

---

---

**📄 Source: PDF Page 42**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 42 / 107 
 
 
İndikatörümüzün, burada seçeceğiniz başka bir indikatör (gösterge) ile kesişmesi durumuna 
göre sinyal üretilmesini istiyorsanız bu bölümü kullanınız.  
 
 
 
Başka bir gösterge ile kesişim işaretlenip, hemen yanındaki bölümden diğer indikatör seçilir. 
Burada gene Moving Average seçelim. Seçtiğimiz anda hemen altta  içinde MOV yazan küçük 
kutucuk gelir. 
 
 
 
Başka bir indikatör seçseydik, o indikatörün adı yazan bir kutucuk gelecek ve bizim o 
indikatörün parametrelerini girmemizi sağlayacaktı. 
Bu kutucuğa tıkladığımızda, yukarıda gördüğümüz / incelediğimiz, indikatör parametrelerini 
belirleme penceresi açılır.  
 
Bu ikinci hareketli ortalama (MOV) için periyodu 20 yapalım. Renk kırmızı kalsın. Esas 
indikatörümüzde rengi yeşil seçmiştik. Eğer sadece AL-SAT sinyallerini tablo üstünde 
görmekle yetinecek isek, bu renk değişikliğinin önemi yoktur. Biraz sonra bahsedeceğimiz 
gibi, Grafik üzerinde izleme şansımız da vardır. Bu durumda, renklerin farklı olması görsel 
olarak daha iyi fark etmemizi sağlayacaktır. 
 
İpucu: Bir indikatör için birden fazla seçenek işaretlerseniz (Seviye kontrolü, Hareketli 
ortalama kesişimi, Önceki değerle karşılaştırma ve Başka bir gösterge ile kesişim gibi), AL ve 
SAT sinyallerinin üretimi, işaretlenen tüm şartların aynı anda gerçekleşmesini gerektirir. 
Örneğin, Seviye kontrolü ve Hareketli Ortalama Kesişimi işaretli ise, sinyalin üretilmesi için, 
hem seviye şartının hem de hareketli ortalama kesişiminin aynı anda gerçekleşmiş olması 
gerekir.  Bu durumda sonuç alma olasılığınız çok azalabilir, bazı çoklu koşullar için imkansız 
olabilir.  
 
Tanımlarınızı bitirdikten sonra ‘Tamam’ tuşuna basınız. Kolon seçim penceresinde MTXtest 
ismini verdiğimiz yeni kolon belirir.

---

---

**📄 Source: PDF Page 43**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 43 / 107 
 
 
 
 
 
 
Kolon seçim penceresi üzerindeki diğer tuşların işlevi şöyledir: 
 
2.3.2 Düzenle:  
Listedeki indikatörlerden istediğiniz birinin üzerine tıklayarak seçtiğinizde, O satır mavi olur.  
 
 
 
Düzenle 
tuşuna 
bastığınızda, 
seçtiğiniz 
indikatörün 
parametre 
ve 
koşullarını 
değiştirebilmenizi sağlayacak şekilde, Kolon Düzenle penceresi açılır. Doğal olarak daha 
önceden tanımlanmış tüm parametreler ve koşullar yüklüdür. Az önce anlatılanları baz 
alarak, bu değerlerde değişiklik yapabilirsiniz. 
 
2.3.3 Sil Tuşu:  
Bu tuş ile seçeceğiniz indikatörü silip listeden çıkarabilirsiniz. Bunu yaparken dikkat 
etmemizde fayda vardır. Program aşağıda göreceğiniz pencere ile silme kararınızın onayını 
soracaktır.

---

---

**📄 Source: PDF Page 44**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 44 / 107 
 
 
 
 
2.3.4 Tamam Tuşu:  
Yeni indikatörü ile ilgili çalışmanızı tamamladıktan sonra, Kolon Seçimi penceresinde en 
alttaki tuşlardan Tamam tuşuna basarsanız, tanımladığınız yeni indikatör de, İndikatör 
Pozisyonları penceresinde yeni bir kolonda belirecektir.  
 
2.3.5 İptal Tuşu:  
Eğer Kolon Seçimi penceresinde, Tamam tuşunun yanındaki iptal tuşuna basarsanız, 
yaptığınız işlemler kaydedilmeden o pencere kapanacaktır. 
 
 
 
 
Yukarıda en sağda, MTXTest başlıklı kolonu görmektesiniz. Yani oluşturduğumuz indikatör 
tanımları ile listeye eklenmiştir. 
Burada indikatörlerin seçimi ile ilgili bir detay daha vardır. Aşağıda, ‘2.6 Şablonlar’ adı altında 
anlatılacaktır. 
 
2.4 Excel’e Aktar:  
Tabloyu excel’e aktarmanızı sağlar. 
 
2.5 Yazdır: 
Tablonun yazıcınızdan çıktısını almanızı sağlar. 
2.6 Şablonlar: 
Yukarıda gördüğünüz ‘Kolon Seçim’ penceresinde listelenmiş olan indikatörlerle ilgili 2 çeşit 
seçim söz konusudur. Bir tanesi yukarıda bahsettiğimiz, üzerine tıklayarak seçim. Bu 
durumda, o satır mavi renge dönüşür. Bu seçim sonrası yapılabilecekler yukarıda 
anlatılmıştır.

---

---

**📄 Source: PDF Page 45**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 45 / 107 
 
 
Diğeri ise, indikatörün analiz grubu içinde olup olmamasının seçimi. İndikatörün önündeki 
mini kutularda bu amaçla seçili olduklarını gösteren ‘check’ işaretlerini görürsünüz:  
 
 
 
Yeni bir indikatörü ilk tanımladığınızda listeye eklendiği halde seçilmemiş durumda olur. 
Kutucuğa tıklayarak seçmelisiniz ve seçiminizin kalıcı olmasını istiyorsanız, şablon olarak 
kaydetmelisiniz. 
Bunu şablon tanımlayarak sağlayabilirsiniz. 
 
 
Başlangıçta program içine ön tanımlı olarak yerleştirilmişi olan 5 adet indikatör şablon 1 
olarak kayıtlıdır. Biz 6. bir indikatör ekledik. Şu anda ‘Kolon Seçimi’ penceresinde durum 
aşağıdaki gibidir.  
 
 
 
Eğer MTX Test uygulamasının her durumda analizlerin içinde olmasını istiyorsanız, önce MTX 
Test in önündeki kutucuğa tıklayarak seçiniz. Sonra bu pencereyi kapatınız. İndikatör 
Pozisyonları penceresinde, Şablonlar altındaki ‘Şablonu Kaydet’ alt menüsünü tuşlayınız. Bu 
durumda Şablon 1 altında 6 adet indikatör işlev görmeye başlayacaktır. 
 
Ayrıca, listeye çok sayıda indikatör eklemiş olabilirsiniz ve bazı analizlerde bazı indikatörlerin 
sonuçlarını görmeye gerek duymayabilirsiniz. Tablonun sağa doğru çok uzun olmasını 
istemeyebilirsiniz. Farklı durumlarda farklı analizlerle çalışmak isteyebilirsiniz. 
Bu durumda Şablon Seç alt menüsünün altından Şablon2’yi seçin. Ekranda indikatör adı olan 
bir sütun kalmayacaktır.

---

---

**📄 Source: PDF Page 46**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 46 / 107 
 
 
 
 
İndikatör Seçimi tuşunu tıklayarak ilgili pencereyi açarsanız aşağıdaki görünümde olacaktır. 
 
 
 
Elinizdeki tanımlı tüm indikatörler orada ama hiçbiri seçili değil. İstediklerinizi önündeki 
kutucuğa tıklayarak seçiniz. 
 
 
Tamam deyip kapattığınızda, indikatör pozisyonları penceresi aşağıdaki görünümde olacaktır. 
 
 
 
Gördüğünüz gibi sadece 3 adet kolon başlığında seçtiğimiz 3 adet indikatör görülmektedir. 
Eğer bu seçimlerimizin kalıcı olmasını istiyorsak, Şablonlar altındaki ‘Şablonu Kaydet’ alt 
menüsünü tuşlamamız gerekir. Bu durumda Şablon 2 altında bu 3 adet indikatör işlev

---

---

**📄 Source: PDF Page 47**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 47 / 107 
 
 
görmeye başlayacaktır. Şablonların içeriğini değiştirmek anlayacağınız üzere oldukça 
kolaydır. 
2.7. Hesapla: 
Son olarak, Hesapla tuşuna basıp üretilen sinyalleri görebiliriz.  
Seçtiğimiz tüm semboller için, tanımlı indikatörlere göre, en son AL veya SAT sinyalleri bu 
sinyallerin verildiği tarihlerle tabloda görünür.  
Aşağıdaki ‘İndikatör Pozisyonları’ tablosunun sinyalleri listeleme biçimini görebilirsiniz.  
Sistem, eğer var olan tüm indikatörler / koşullar için AL sinyali varsa tüm satırı maviye, tümü 
için SAT sinyali varsa tüm satırı kırmızıya boyar.  
 
 
 
Pencerenin üst başlığında, hesaplamayı yaptığınız tarih ve saat görünür. 
Sinyallerin tarihlerine dikkat etmenizde fayda vardır. Kolonlarda yer alan tarihler, son sinyalin 
gerçekleştiği tarihtir. Son sinyalin verilmesinden bu yana uzun zaman geçmiş olması yanıltıcı 
olabilir. 
 
Bir satır üzerine tıkladığınızda o satırdaki finansal enstrüman için indikatörlerin verdiği 
sinyaller hakkında bilgiler, kısaca pencerenin alt kısmında aşağıda göründüğü şekilde yazılır.

---

---

**📄 Source: PDF Page 48**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 48 / 107 
 
 
2.8. Sağ Klik Menüleri:  
İndikatör pozisyonları penceresi üzerinde sağ klik yaparsanız aşağıda göreceğiniz menüler 
açılır.  
 
 
Grafik Üzerinde Göster menüsü ile  
Eğer sembol üzerinde tıkladı iseniz, o sembol için tablodaki tüm indikatörlerin göründüğü 
grafik penceresi açılır. 
 
 
 
 
Eğer indikatör sütunlarından birisi üzerinde tıkladı iseniz, ilgili satırdaki sembol için sadece 
ilgili sütundaki indikatörün göründüğü grafik penceresi açılır.

---

---

**📄 Source: PDF Page 49**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 49 / 107 
 
 
 
 
Sağ klik altındaki diğer menüler, yukarıda zaten anlatılmıştır.  
 
 
3. İndikatör Değerleri: 
Bu modül, sadece grafik üzerinde kullanmakta olduğunuz indikatörlerin son değerlerini 
seçilen hisseler için bir tablo halinde listeler. Modülün içinde indikatör seçimi için bir alan 
yoktur. Bunun yerine, açmış olduğunuz grafikte kullanılan indikatörler hangileri ise, doğrudan 
onlarla çalışır. Bu modülün amacı, indikatörlerin değerlerinin çok yüksek ya da çok düşük 
olmasına göre karar verebilecek yatırımcıların, toplu olarak indikatörlerin değerini bir tablo 
halinde görebilmesidir.  
 
 
 
Bu grafik üzerinde çalışırken, Kahin altındaki indikatör değerleri menüsünü tıklarsanız, 
aşağıdaki tablo karşınıza gelir.

---

---

**📄 Source: PDF Page 50**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 50 / 107 
 
 
 
 
Tabloda yer alan indikatörler, yukarıdaki grafikte kullandığımız indikatörlerdir. 
 
3.1. Sembol seçimi:  
Bu menü ile daha önceki anlatımlarda bahsettiğimiz Senet seçim penceresi açılır. Buradan 
seçeceğimiz semboller için, tablodaki indikatör değerlerini görebiliriz. 
 
3.2. Excel’e Aktar:  
Tabloyu excel’e aktarmanızı sağlar. 
 
3.3. Yazdır:  
Tablonun yazıcınızdan çıktısını almanızı sağlar. 
 
3.4. Varsayılan Olarak Kaydet:   
Varsayılan olarak kaydettiğinizde, bundan sonra bu analizi açtığınızda, o anda var olan kolon 
başlıkları ile gelecektir. 
 
3.5. Periyot:  
Bu pencereden, grafik / analiz periyodunu değiştirebiliriz. 
 
3.6. Birim:  
Bu pencere üzerinden, aynı analizi başka para birimleri ile hesaplanan verilere göre 
yapabiliriz. 
 
3.7. Hesapla:  
Sembolleri seçip hesapla tuşuna bastığımızda, program her sembol içini indikatör değerlerini 
bir tablo halinde sunar.

---

---

**📄 Source: PDF Page 51**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 51 / 107 
 
 
 
 
 
 
3.8 İndikatör Değerleri Penceresi Sağ Klik Menüleri:  
Bu pencere üzerinde sağ klik yaparsanız aşağıda göreceğiniz menüler açılır.  
 
 
 
Grafik Üzerinde Göster Bu menü ile ilgili satırdaki sembol için tablodaki tüm indikatörlerin 
göründüğü grafik penceresi açılır.

---

---

**📄 Source: PDF Page 52**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 52 / 107 
 
 
 
 
Sağ klik altındaki diğer menüler, yukarıda zaten anlatılmıştır.  
 
4. System Tester: 
KHN başlığı altındaki System Tester modülü önemli bir Teknik Analiz uygulamasıdır. 
Oluşturulmuş bir sistemin, geçmiş dönemlerde kullanılması durumunda nasıl bir sonuç elde 
edileceğine dair testleri yapar. Ve gelecekteki fiyat oluşumlarına göre AL-SAT sinyalleri üretir.  
Öncelikle kısaca bir göz atalım:

---

---

**📄 Source: PDF Page 53**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 53 / 107 
 
 
4.1 Üst Banttaki Menüler:  
System Tester penceresinin üst bandındaki butonların işlevleri: 
 
 
 
4.1.1 Yeni Sistem:  
Bu menü ile yeni bir sistem tanımlamanızı sağlayacak şekilde sistem oluşturma penceresi 
açılır. Aşağıda anlatılacaktır. 
 
4.1.2 Düzenle:  
Bu menü ile tanımlı sistemlerden birini seçip değişiklik yapabilirsiniz. 
 
4.1.3 Sil:  
Bu menü ile tanımlı sistemlerden seçtiğiniz sistemi silebilirsiniz. 
 
4.1.4 Sistem Gönder:  
Başka bir bilgisayarınıza ya da başka bir kullanıcıya sistem gönderebilmenizi sağlar. Tanımlı 
sistemlerden birisini seçip, sistem gönder tuşuna basarsanız, sistem gönder penceresi 
açılacaktır.  
 
 
 
Sistem gönderirken, dilerseniz karşı tarafın görmemesi için, formülü gizleyebilirsiniz. 
Gönderdiğiniz kişi sistemi deneyebilir, sonuçlarını görebilir ama formülü göremez. Herhangi 
bir sebeple sistemi gönderdiğiniz kişinin formülü görmesini istemiyorsanız buradaki 2 
seçenekten birisini kullanabilirsiniz.  
Öncelikle, eğer formülü gizlemek istiyorsanız, pencerenin üst kısmındaki ‘Formülü Gizle’ 
yazısının önündeki kutucuğu işaretlemelisiniz. Bu size alttaki 2 uygulamadan birisini yapma 
seçeneği verir. 
 
 Formülü Şifrele:  
Formülü şifreleyerek koruyabilirsiniz. Bu şekilde, dilediğinizde şifreyi vererek, karşı tarafın 
formülü görmesini sağlayabilirsiniz. Bunu seçtiğiniz takdirde, altındaki ‘Şifreyi Girin’ ve ‘Şifreyi 
Girin (Tekrar)’ kısımlarına belirlediğiniz şifreyi yazınız.  
Devam butonuna tuşladığınızda, sistem dosyasını bilgisayarınıza kaydetmenizi sağlayacak 
‘Sistem Dosyasının Adını Yazınız’ ismi ile Windows penceresi açılır.

---

---

**📄 Source: PDF Page 54**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 54 / 107 
 
 
 
 
Herhangi bir sistemi e-posta ya da benzeri bir yolla gönderebilmek için önce bilgisayarınıza 
ayrı bir dosya olarak kaydetmeniz gereklidir.  
 
 Burada dikkat etmeniz gereken husus şudur: Buraya dosya adı olarak gönderdiğiniz 
sistemin adını girmenizde fayda vardır. Siz burada hangi ismi verirseniz verin, karşı 
taraf sistemi ‘System Tester’ programına yüklediği zaman, sistemi yazarken vermiş 
olduğunuz ad ile görünecektir. Bu yüzden kaydetme işlemini, sistemin system 
tester’daki adı ile yapmanızda fayda vardır.  
 
 Dosya uzantısının mst olmasına dikkat ediniz.  
 
 Formülü Sil:  
Diğer seçeneğiniz ise, formülü silerek göndermektir. Bu durumda karşı tarafın formüle 
ulaşma ihtimali hiç olmaz. Bu seçeneği uyguladığınızda da, devamında yapacaklarınız 
yukarıda anlatılanla aynıdır. 
Sistem dosyasını gönderdiğinizde, alan kişinin yapacakları da ‘Sistem Al’ başlığı altında 
anlatılmıştır. 
 
4.1.5 Sistem Al:  
Gönderilen bir sistemi almak için, önce karşı taraftan gelen mst uzantılı  sistem dosyasını 
bilgisayarınıza kaydediniz. Sonra, System Tester penceresi üzerinden, ‘Sistem Al’ butonuna 
basınız. Sistem gönder işleminde karşınıza çıkan aynı pencere bu sefer, ‘Sistem Dosyasını 
Seçiniz’ adı ile açılır. 
 
Buradan Sistem dosyasını kaydettiğiniz yere ulaşarak, mst uzantılı sistem dosyasını seçiniz ve 
pencerenin sağ alt kısmında bulunan ‘Aç’ butonuna basınız. 
Bunu yaptığınız anda, ilgili sistem tanımlı sistemler arasında listelenecektir.

---

---

**📄 Source: PDF Page 55**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 55 / 107 
 
 
Listeden sistemi seçip, ‘Düzenle’ düğmesine basarsanız açılacak ‘Sistem Düzenleme’ 
penceresinin koşul yazım kısmında Formül içeriği yazarı tarafından silinmiş ibaresi 
görünecektir. 
 
 
 
Eğer formül şifrelenmiş olursa, bu seferde: 
 
  yazısı görünecektir. 
 
İpucu: Sistem gönderme esnasında kaydettiğiniz dosyanın uzantısı mst olacaktır. Bunu e-
posta ile göndermek isterseniz virüs programları engelleyebilir. Bu durumun üstesinden 
gelebilmek için göndermeden önce sistemin uzantısını mesela ‘aa’ olarak değiştiriniz. Karşı 
tarafta dosyayı alan kişinin, Sistem Al öncesinde uzantıyı tekrar mst yapması şarttır. 
 
4.1.6 Varsayılan Değerlerle Çalıştır:  
Aşağıda göreceğiniz değişken tanımlama kısmında, bu butonu ne amaçla kullanabileceğiniz 
açıklanmıştır. 
 
4.1.7 Favorilerime Ekle / Favorilerimden Çıkar: 
Butonları Tanımlı sistemlerin listelendiği System Tester ana ekranından, istediğimiz 
sistemleri,  bu seçenekler ile favorilere ekleyerek toplu çalıştırılabilecek bir favori sistemler 
listesi oluşturabilirsiniz. KHN menüsündeki ‘Favori Sistemlerim’ seçeneği, bu şekilde 
tanımlanmış olan tüm sistemlere kolayca ulaşmanızı sağlar.  
 
4.2 Tanımlı Sistemler:  
Pencerenin sol tarafında ‘Tanımlı Sistemler’ kısmı vardır. Bu kısımda Matriks tarafından hazır 
olarak sunulmuş sistemleri ve kendi tanımladığınız sistemleri göreceksiniz. 
Bir sistem oluşturup kaydettiğinizde, o sistem, verdiğiniz isim ile bu pencerede görünür.  
Bu pencerenin alt kısmında aşağıdaki ibareyi göreceksiniz.

---

---

**📄 Source: PDF Page 56**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 56 / 107 
 
 
 
 
Yani birden fazla sistemi, klavyedeki Ctrl tuşunu basılı tutarak seçebilir ve aynı anda 
çalıştırabiliriz. 
 
 
4.3 Uygulanmış Simülasyonlar:  
Sağ taraftaki Uygulanmış Simülasyonlar kısmında, daha önce uyguladığımız simülasyonların 
listesi bulunur.  
 
 
Simülasyon adı ( sistem tarafından otomatik verilir) / Hangi sistemin kullanıldığı / 
Simülasyonun yapıldığı sembolün / grubun adı / simülasyon durumu, ve uygulandığı tarih 
bilgileri vardır. 
 Uygulanmış Simülasyonlar Kısmının Altındaki Menü Butonları: 
 
 
 
 Temizle: 
Uygulanmış simülasyonlar listesinin tümünü siler. Öncesinde aşağıda göreceğiniz gibi bir 
pencere ile uyarı gelir. 
 
 
Onaylarsanız listede yer alan eski testlerin tamamı silinir.  
 
 Sil:  
Üzerine tıklayarak seçtiğiniz simülasyonu siler. Tıklayıp seçim yaptığınız simülasyon zemini 
hafifçe renk değiştirir.  
 
 Rapor:  
Üzerine tıklayarak seçtiğiniz simülasyonun ‘System Tester Sonuçları’ penceresini açar. 
Tıklayıp seçim yaptığınız simülasyon zemini hafifçe renk değiştirir.

---

---

**📄 Source: PDF Page 57**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 57 / 107 
 
 
 
4.4 Yeni Sistem (Oluşturma):  
Bu butonu tıkladığınızda, ‘İndikatör Builder’ penceresine benzeyen ‘Sistem Düzenleme’ 
penceresi açılacaktır. 
 
 
Açılan pencere üzerinde yeni bir sistem oluşturabilirsiniz. Var olan sistemlerden birinin 
üzerine tıklayıp seçtikten sonra, düzenle butonuna bastığınızda, ya da var olan sistem üzerine 
çift tıkladığınızda da bu pencere açılır. Var olan bir sistem için pencereyi bu şekilde açtıysanız, 
pencere üzerinde sistem yazılımını görebilir, yazılım üzerinde değişiklik yapabilirsiniz. 
Formüllerinizi pencerenin Alt kısmında görmüş olduğunuz AL, SAT, Açığa Sat, Açık Pozisyon 
Kapat sekmelerine yazmalısınız. 
 
4.4.1 Sistem Adı:  
Oluşturacağınız sisteme bir isim veriniz. Dilediğiniz gibi bir isim verebilirsiniz. Doğal olarak 
size ne hazırladığınızı hatırlatacak bir isim vermeniz daha uygundur. İsim vermeden 
kaydetmeye çalıştığınızda program sizi uyaracaktır.  
 
4.4.2 Seçimler Kısmı:  
Pencerenin üst bölümü, ‘İndicator Builder’ ile tamamen aynıdır.  
Aslında yazacağımız formül, İndicatör builder da yaptığımızla benzer bir uygulama olacaktır. 
Burada formülünüz koşul içermelidir. (Koşul içeren biçimde yazılmış olmalıdır) Bu koşulların 
gerçekleşmesi durumuna göre AL-SAT sinyalleri oluşacaktır. Yani yazacağınız formülün sinyal 
üretecek bir koşul içermesi gerekir. 
Sistem Tester modülü ‘açığa satış’ın yapılabildiği finansal enstrümanlara da uygundur. Bu 
yüzden Açığa sat ve açık pozisyon kapat sekmeleri vardır.

---

---

**📄 Source: PDF Page 58**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 58 / 107 
 
 
İpucu: Genel olarak Açık Pozisyon Kapat’a AL ile aynı koşulu yazılır. Açığa Sat kısmına da SAT 
ile aynı koşul yazılır. Bununla beraber bu bir zorunluluk değildir. Sistemin yapısını kendi 
tarzınıza göre oturtmanızda fayda vardır.  
 Parametreleri Kopyala:  
İndikatör seçimi yaparken, bu seçeneği işaretledi iseniz, indikatörler listesinden seçtiğiniz 
indikatörün üzerine çift tıkladığınızda, indikatör gerekli parametrelerini göstererek gelir: 
 
MOV(Data,Periyot,Yöntem S E W TRI VAR ) 
Eğer bu seçeneği işaretlemezseniz, parametreler görünmeden sadece adı ile gelir: MOV 
 
Eğer, indikatörün parametrelerini ezbere biliyorsanız, bu seçimle, parametre isimlerini 
silmekle uğraşmanıza gerek kalmayacaktır. 
 
 Bazen sistemin al-sat uygulamalarını X bar geciktirmesini tercih 
edebilirsiniz. Sinyalin kalıcı olduğundan emin olmak vb. sebeplerle. Bu durumda buraya 
gecikmeyi istediğiniz bar miktarı kaç ise, o rakamı girmeniz gerekir. 
4.4.3 Koşulların Yazılması:  
AL koşulunuz için, AL kutucuğunu Mouse ile işaretleyip koşul kısmına formülünüzü 
yazabilirsiniz. Formül yazımı: Pencerenin koşul tanımlama kısmına yazacağınız her türlü 
tanımlama formül olarak adlandırılmaktadır. Bu çok basit bir tanımlama olabileceği gibi, bir 
kaç tane indikatör ve fonksiyonun birleşiminden oluşan kompleks bir tanımda olabilir.  
SAT koşulunuz için, SAT butonuna tıkladığınızda, SAT sekmesi açılır. Koşul kısmı boş olarak 
gelir. Bu koşul kısmına formülünüzü yazabilirsiniz. 
 
İpucu: Sistem Tester’ın çalışması AL ve SAT sinyallerinin peş peşe gelmesi şeklindedir. Yani 
Alır, Satar, sonra tekrar alır. SAT gerçekleşmeden ikinci bir sefer alım yazmaz. Bu sebeple AL 
ve SAT koşullarının karşılıklı tanımlanmış olması gerekir. Benzer biçimde Açığa Sat ve Açık 
Pozisyon Kapat koşulları da karşılıklı tanımlı olmalıdır.  
 
Sistem Tester’da Tanımlı sistemler altındaki örneklerden mtx_mov üzerine tıklayıp düzenle 
derseniz aşağıdaki AL ve SAT koşullarının yazılmış olduğunu görürsünüz.  
 
 AL için:

### Code Examples

```elixir
use ile işaretleyip koşul kısmına formülünüzü
```

---

---

**📄 Source: PDF Page 59**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 59 / 107 
 
 
 
 
 
 SAT için:  
 
 
Açıklama: Yukarıdaki koşullar 3 günlük basit hareketli ortalamanın 10 günlük basit hareketli 
ortalamayı aşağıdan yukarıya kestiği zamanda AL sinyali üretecek, yukarıdan aşağıya kestiği 
zamanda SAT sinyali üretecektir. Cross fonksiyonunun şablonu Cross(Data1,Data2) 
şeklindedir. Data1 yerine yazılan verinin Data2 yerine yazılan veriyi aşağıdan yukarıya kestiği 
zamanı gösterir.  
İpucu: 1.5 Fonksiyonlar kısmında program içinde yer alan tüm fonksiyonların kısa 
açıklamaları vardır.      
 
Açığa Sat ve Açık pozisyon kapat sekmelerine koşul yazmakta fayda vardır. İlerleyen aşamada 
sistem size, Açığa satış opsiyonunu kullanıp kullanmayacağınızı belirleme olanağı verecektir. 
Aşağıda anlatılmıştır.  
Test’i açığa satış yap(a)mayacağınız bir finansal enstrüman üzerinden yapıyor iseniz, Açığa 
satış opsiyonunu aktif hale getirmemeniz gerekir. Yoksa test sonucu yanıltıcı olacaktır.  
Normalde açığa sat sekmesine SAT ile aynı koşulu ( çünkü sonuçta bu bir satış işlemidir), Açık 
pozisyon kapat penceresine de AL ile aynı koşulu (çünkü sonuçta bu bir alış işlemidir) 
yazmamız uygundur. Bununla beraber sistemin çalışması için, bu koşulların aynı olması 
zorunlu değildir.  
 
4.4.4 Değişkenler Sekmesi:  
System Tester, yapı itibariyle bir sistemin getirisini test etmek amacıyla oluşturulmuş bir 
modüldür. Bu nedenle, sistemin daha yüksek getiri elde etmesini sağlayacak şekilde farklı 
periyotlarda çalışması konusunda da testler yapılabilir.  
Bu noktada, kullanılan indikatörler içinde sabit periyotlar kullanmak yerine, en yüksek 
getiriye ulaşan periyotların program tarafından tespit edilebilmesi söz konusu olmaktadır.  
Bu durumda, AL, SAT, Açığa Sat, Açık Pozisyon Kapat sekmelerine formülleri yazarken, hangi 
sayısal parametre için programın uygun veri değerini bulması isteniyorsa, o parametreler 
yerine OPT1, OPT2 gibi tanımlamalar yapılmalıdır. 
Mesela mtx macd sisteminde, ön tanımlı macd değerleri olan 26,12,9 gibi sabit sayılar yerine 
değişkenler verilmiş ve formül Cross(MACD(opt1,opt2,opt3),MACDTrigger(opt1,opt12,opt3)) 
şeklinde yazılmıştır.   
Bu değerler için değişkenler kısmından aşağıda pencerede bir örneğini görebileceğiniz 
şekilde, alt sınır, üst sınır ve adım değeri belirlemelisiniz.

---

---

**📄 Source: PDF Page 60**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 60 / 107 
 
 
 
 
 
 
 
Bu durumda, sistem, değişkenlerin alabileceği her değer için ayrı bir test yapar ve 
belirlediğiniz miktar kadar en iyi getiri sağlayan optimizasyon değerlerini bir tablo halinde 
size verir.  
Burada ayrıca Varsayılan Değer tanımlayabileceğiniz bir hücre de vardır. Buraya tanımlama 
yaparsanız, dilediğiniz zaman, sistemi varsayılan değer ile çalıştırabilirsiniz. Bunu sistem 
tester penceresi üzerinde bulunan  
butonu ile yapabilirsiniz. Böylece 
her seferinde değişkenleri içeren uzun testler yapmak durumunda kalmazsınız. 
 
Verdiğiniz parametre sınırları ve adım seçimlerinize göre, yapılması gereken test sayısı bu 
sekmenin sağ üst kısmında gösterilir.  
 
 
 
İpucu: Test sayısı çok fazla olduğunda sonuç almanız çok uzayacaktır. Adım değerlerini 
büyüterek test sayısını azaltabilirsiniz. 
 
Bu sayede değişken olarak belirlediğiniz datalar için en uygun değerleri belirleyebilirsiniz.  
 
Bunu yaparken neyi nasıl belirleyebileceğiniz, biraz aşağıda Sistem Çalıştırma kısmında 
anlatılmıştır.  
 
Ek Bilgi: Sistem tester optimizasyonunda hafıza durumu ile ilgili düzenleme yapıldı. Hafıza 
yetersizliği olacak durumlarda uyarı çıkmaktadır.

---

---

**📄 Source: PDF Page 61**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 61 / 107 
 
 
4.4.5 Stop Sekmesi: 
Sistemlerinizi yazarken STOP tanımlayabilirsiniz.  
 
 
 
STOP tanımlamadaki amaç, karlı işlem yapıp, en az zararla pozisyonu kapatmaktır. STOP 
penceresinde; 
 Kar Realizasyonu bölümünde Taşınan Pozisyonlara Uygula ve Açık Pozisyonlara 
Uygula seçeneklerini görürsünüz. Taşınan Pozisyonun anlamı al koşulu ile alınmış 
pozisyon, Açık pozisyonlara uygula ise, Açığa Sat işlevi ile açılmış pozisyondur. Burada 
kar hedefini belirlerken hesaplamanın % olarak mı puan olarak mı yapılacağına karar 
vermelisiniz. Ve buna göre seçim yapmalısınız. Örnek olarak %5’lik bir kar hedefi 
varsa Kar Hedefi kutusuna 5 yazılıp % bölümü işaretlenmelidir. Bir pozisyon açtıktan 
sonra, belirli bir miktar kar elde edildiği takdirde pozisyonunuzu kapatmak istiyorsanız 
Kar Realizasyonu bölümünü kullanabilirsiniz.   
 
 Zararı Durdur bölümü yine aynı şekilde çalışmaktadır. Burada da yine Taşınan 
Pozisyonlara ve/veya Açık Pozisyonlara zararı durdur uygulaması seçimi yapılıp, % 
veya Puan tercihi belirlenip, stop miktarı Maximum Zarar kutusuna yazılmalıdır. 
Pozisyonunuzu açtıktan sonra zararı minimumda tutmak için Zararı Durdur seçeneği 
kullanılabilir. Bu bölüm, örnek olarak zarar kriterimiz %2 ise, pozisyonunuzu açtıktan

---

---

**📄 Source: PDF Page 62**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 62 / 107 
 
 
sonra fiyat %2 geri gelirse bir Stop ile Alarm verir. (Ya da seçiminize göre emir 
gönderim penceresini açar – emir gönderir )  
 
 Süre Sınırı yine aynı şekilde stop’un hangi pozisyonlara uygulanacağı seçilip, sınırı bar 
sayısı olarak belirleyebileceğiniz bölümdür.  
 
 
 Hareketli Stop Loss ise fiyatlar pozisyonunuz yönünde ilerledikçe, belirlenen Stop 
seviyesi ötelenir. Fiyatlar ters yönde hareket ederken stop seviyesi sabit tutulur. 
* Açıklama: Mesela bir senedi 10 TL den aldığınızı ve %1 Hareketli stop loss 
belirlediğinizi düşünelim. Fiyat 11 TL’ye çıktığı zaman, stop seviyesi 9.9 TL’ye (11TL’nin 
% 1 aşağısı) yükselecektir.  Fiyatın geri geldiği zamanlarda stop seviyesi yerinde 
kalacaktır.  
 
 Kademeli Hareketli Kar Stopu  Kar seviyesine bağlı olarak stop seviyesinde farklılıklar 
oluşturabilmenizi sağlar. Ayrı bir dokümanda anlatılmıştır. Bakınız: Kademeli 
Hareketli Kar Stop Loss Nasıl Çalışır isimli doküman.  
 
DİKKAT: Geçmişin testinde STOP’larla ilgili önemli bir detay vardır: Kar Al ve Zarar Durdur 
stop seviyelerinin yerleri nettir. Geçmiş testindeki veriler gerçek hayatla örtüşür.  
Bununla beraber Hareketli Stop’lar için geçmiş testinde durum belirsizdir.  
Sistem bar içindeki fiyat hareketlerinin sürecini bilemeyeceği için yükseklere ve kapanışlara 
bakarak STOP üretir. AL işleminin gerçekleştiği Bar’ın kapanışı alış fiyatınızdır. İlk anda bu 
değer stop seviyesi için baz alınır.  
Sonraki bardan itibaren fiyat daha  ‘Yüksek’ bir seviye görürse (ki normal şartlar altında 
görecektir) stop seviyesini buna göre revize eder. Ve bu barın kapanışı ile stop seviyesini 
karşılaştırır, kapanış daha aşağıda ise ‘STOP’ verir. 
(Yani, aynı bar içindeki yüksek ve kapanış farkı dolayısı ile stop verebilir.) 
Değilse bir sonraki barda aynı kontrolleri yaparak devam eder. Daha yüksek bir seviye görülür 
ise stop seviyesi buna göre tekrar revize edilir. Fiyat stop seviyesine görmüş ise de ‘STOP’ 
verir. İlk işlemin ‘Açığa Sat’ olması durumunda, yukarıda bahsedilen işlem ters yönde 
uygulanır. Testin getirisi bu stop seviyesine göre hesaplanır. 
Seans esnasında ise, gerçekleşen son fiyat STOP koşulunu gerektirdiği anda STOP oluşur. Stop 
seviyesine o bar içinde yüksek görülmeden önce ulaşılmış olabilir.  
Bu yüzden STOP uygulaması olan sistemlerin geçmiş testlerinde sonuçlar gerçek süreçle tam 
örtüşmeyebilir. Hatta düşük miktarlı stoplarda oldukça ciddi biçimde ayrışır. Bu sebeple 
hareketli stoplardan birisini kullanıyorsanız, geçmiş testlerine ihtiyatlı yaklaşmanız önemlidir.  
 
 Kar Hedefi ile SAT / KAPAT ENGELLE: Bu sekmenin işlevi, burada tanımlayacağınız 
miktarın / oranın altında bir kar ile pozisyon kapatma sinyali gelecek olur ise, 
engellemesidir.  
Dikkat: Bu özelliği ısrarla istendiği için ekledik. Kullanmanızı önermiyoruz. Kullanacak 
olursanız da, mutlaka zarar stop’u ile birlikte kullanınız.  
Geçmiş testi yaparken, bu seçim getirilerinizin artmasını sağlar. Bununla beraber riskli 
bir seçenektir.

---

---

**📄 Source: PDF Page 63**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 63 / 107 
 
 
Şöyle ki: Sisteminiz AL durumunda iken, az bir kar veya zarar ile SAT verecekti 
diyelim. Bu seçeneği işaretlediğiniz için de vermedeğini var sayın. Ve fiyatın düşmeye 
devam ettiğini düşünün. Sisteminizde stop yok ise, sistem senaryonuzun tekrar sat 
vermesi için, önce bir daha AL vermesi (gerçekte almayacak tabii ki, çünkü zaten AL 
durumunda) ve sonra tekrar sizin koyduğunuz sınırın üstünde bir kar seviyesi ile sat 
vermesi gerekecektir. Çok ciddi zararlar ile karşılaşabilirsiniz. Bu sebeple, kullanırsanız 
da, zarar stopu ile birlikte kullanınız. 
 
 
 Varsayılan Olarak Kaydet: Var olan bir sistem üzerinde, yaptığınız değişikliklerin kalıcı 
olmasını (bundan sonra her seferinde yeni tanımlamalarımızla çalışmasını) sağlar. 
 
 
4.4.6 Not Sekmesi:  
Bu sekme altında dilediğiniz açıklamayı yazabileceğiniz bir pencere gelir. 
 
4.4.7 Tamam Butonu:  
Bu butona bastığınızda, yazdığınız sistem / değiştirdiğiniz sistem son hali ile  System Tester 
penceresinin, tanımlı sistemler kısmında görünecektir. 
 
 
4.5 Sistem Çalıştırma:  
Çalıştırmak istediğiniz sistemi seçip, simülasyon tuşuna basarsanız, karşınıza sistem 
simülasyon ayarlarını yapmanızı sağlayacak Sistem Tester-Sembol Seçimi  penceresi 
gelecektir. 
 
 
Pencerenin ortasındaki kısımda Sistem tester’a giriş yapmak için kullanmış olduğunuz 
grafikteki sembol ve periyodu listelenecektir.

---

---

**📄 Source: PDF Page 64**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 64 / 107 
 
 
 
 Sembol Kodu penceresinden bir sembol seçip, ‘Ekle’ butonu ile seçtiğiniz sembolü 
listeye ayrıca ekleyebilirsiniz.  
 
 Periyod penceresinden testin kullanacağı periyodu (Gün / seans / xx dakika vb.) 
seçebilir / değiştirebilirsiniz.  
 
 Birim penceresinden de, sonuçları görmek istediğiniz para birimini seçebilir / 
değiştirebilirsiniz. 
 
 Tüm Periyotları Değiştir Sembolleri üstteki sembol kodundan tek tek girerken, farklı 
periyotlar tanımlayabiliriz. 
 
 
 
 
Yukarıda göreceğiniz gibi 3 ayrı sembol, analiz için 3 ayrı periyotta seçilebilir. Eğer, tüm 
seçimlerimizin aynı periyotta test edilmesini istersek, önce periyot penceresinde istediğimiz 
periyodu girip, sonra 
 butonuna basmalıyız.  
Periyodu 60 dk. seçip, ‘Tüm Periyodları Değiştir’ butonuna bastığımızda, aşağıda göreceğiniz 
gibi tüm satırlarda periyod 60 dk. olarak yenilenir. 
 
 
 
Tüm birimleri Değiştir: Periyot seçiminde olduğu gibi, birim seçiminde de, sembolleri üstteki 
sembol kodundan tek tek girerken, farklı birimler tanımlayabiliriz.

---

---

**📄 Source: PDF Page 65**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 65 / 107 
 
 
 
 
Yukarıda TL ve Euro seçimleri görülmektedir. 
 
Eğer, tüm seçimlerimizin aynı birim seçimi ile test edilmesini istersek, önce birim 
penceresinde istediğimiz birimi girip, sonra 
 butonuna basmalıyız.  
 
Birim olarak kullanabileceğiniz seçenekleri, pencerenin içindeki Ok’a tıkladığınızda 
göreceksiniz.  
 
 
 
 
Seçtiğiniz finansal enstrümanın değişimini, TL / USD / EUR gibi para birimlerine göre test 
edebileceğiniz gibi, BİST 100 endeksine göre, faiz oranlarına göre, TEFE ve TÜFE’ye göre de 
test edebilirsiniz. 
Hatta Senet seçeneği ile diğer tüm finansal enstrümanlar bazında değerleri ile de test 
edebilirsiniz. 
Senet seçimi yaparsanız, bu pencerenin hemen sağında senet seçimi yapabileceğiniz bir 
pencere daha açılacaktır. 
 
 
 
Birimi TEFE seçip, ‘Tüm Birimleri Değiştir’ butonuna bastığımızda, aşağıda göreceğiniz gibi 
tüm satırlarda Birim TEFE olarak yenilenir.

---

---

**📄 Source: PDF Page 66**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 66 / 107 
 
 
 Ekle Butonu ile Sembol Kodu penceresinde görülen finansal enstrüman listeye 
eklenir. 
 
 Sil Butonu ile listeden seçeceğiniz bir sembolü ( üzerine tıklayıp seçtiğinizde zemin 
rengi maviye dönüşür) silebilirsiniz. 
 
 Tümü Sil Butonu ile listedeki seçilmiş tüm sembolleri silebilirsiniz. 
 
 Çoklu Sembol Seçimi butonu ile test etmek istediğiniz sembolleri topluca listeye 
ekleyebileceğiniz ‘Senet Seçiniz’ penceresi açılır.  
 
İpucu: Sistem tester modulü oldukça yoğun işlemler içermektedir. Bu sebeple çok sayıda 
sembol seçmeniz uzun süre beklemenizi gerektirebilir. Programın çalışmasında aksaklıklarla 
da karşılaşabilirsiniz. 
Burada asıl hedef bir sembolün, en fazla birkaç ayrı periyod seçimi için test edilmesi olmalıdır. 
 
 Test Bölgesi 
:  
 
Listedeki sembolleri seçip sonra Test bölgesi tuşuna tıklayarak, ya da tek bir sembolün 
üzerine çift tıklayarak ‘Simülasyon Ayarları’ penceresini açarsınız.  
 
 
 
 Test Dönemi Seçimi: Bu pencerenin üst kısmında testi hangi dönem için yapmak 
istediğinizi seçersiniz. 3 adet seçeneğiniz vardır: 
 
 Tarih aralığını seçerseniz, belirleyeceğiniz 2 tarih arasında test yapılır.

---

---

**📄 Source: PDF Page 67**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 67 / 107 
 
 
 
 Son xxx barı Kullan seçerseniz, bugünden geriye doğru belirleyeceğiniz miktarda 
seçmiş olduğunuz bar sayısı kadar geriye gidip bu süre için test yapılacaktır.   
 
 Renko Heiken Ashi Seçimi, Testin bu grafik tipleri ile yapılmasını sağlar. Bu yöntemler 
için, ayrıca doküman hazırlanacaktır.  
 
 
 
 Walk Forward Analiz  bölgesi, Bu kısmı işaretleyerek sistemin walk forward analizini 
yapmasını ve buna göre sonuçlar getirmesini sağlayabilirsiniz.    
 
Not: Sadece optimizasyon içeren sistemlere yönelik bir analizdir.  Optimizasyon 
içermeyen sistemlerde pasif gelir.  
 
 
 
Ayrı bir dokümanda anlatılacaktır.  
 
 Tüm Barları Kullan seçerseniz, teorik olarak ana periyodlar için geriye dönük 8.000 
barı kullanır ama, pratikte kullanılan bar sayısı daha az olabilir.   
 
 
 Tüm Listeye Uygula: Bu uygulama ile seçtiğiniz tüm semboller için bu test periyodu 
seçilmiş olur. 
 
 Default Olarak Kaydet: Bu seçim ile ilerde yapacağınız her simülasyon, değişiklik 
yapmadığınız sürece, seçmiş olduğunuz parametreler için yapılacaktır. 
 
 Tamam Butonu Bu buton ile seçiminiz uygulanmak üzere pencere kapanır. 
 
 
 Tek Tek / Toplu Değerlendirme Seçeneği: Simülasyon penceresini sol alt köşesinde 
yer alan, ‘Bu senetleri ayrı ayrı değerlendir’ ya da ‘Bu senetlerin toplam getirisini 
değerlendir’ seçenekleri önemlidir.  
 
 
 
Bu kısım değişkenlerle ilgilidir. Değişken tanımladığımızda, sistem testini çok sayıda sembol 
için yapıyorsak, şu 2 seçeneğimiz vardır: Her bir senet için optimum değişkeni ayrı ayrı

---

---

**📄 Source: PDF Page 68**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 68 / 107 
 
 
belirleyebiliriz. Bu durumda senetleri ayrı ayrı değerlendir seçeneğini seçmeliyiz. Her birisi 
için test seçeneklerini ayrı ayrı yapar ve her bir simge için en uygun değişkeni ayrı ayrı 
hesaplar.  
Eğer tüm semboller için ortak en iyi değişken rakamını bulmak istiyorsak bu sefer tümü için 
ortak test yapar ve tümü için ortak en iyi değişken değerini bulur. 
 
Dikkat:  
Optimizasyon sayısı / sınırları geniş tutulursa test sayısı çok artar. Buna bir de, senetleri 
topluca değerlendir seçimi eklenirse ve çok sayıda sembol seçilmiş olur ise, sistem kaynakları 
yetersiz kalabilir.  
Bu gibi durumlarda şöyle bir uyarı alabilirsiniz:  
 
 
 
Portöy Modu: Senetlerin topluca değerlendirilmesi, portföy modu olarak adlandırılır. 
Bu, sistem kaynaklarını fazladan tüketen bir seçenektir. Yüksek sayıdaki (milyon üzeri) test 
sayısı ile birleşince, Sistem hafızasının yetersiz kalmasına sebep olabilir. Ve sonuç olarak bu 
uyarıyı alabilirsiniz. Test sayısını ve / veya senet sayısını azaltmanız gerekir.  
 
 
 Değişken Kullanımı: Değişken kullandı isek, çok sayıda test yapılacağı için, sonuçların 
tümünü görmemiz mümkün olmaz.  Doğal olarak sıralama en iyi getiriden başlayarak 
yapılacaktır. Pencerenin sağ alt tarafında, aşağıda göreceğiniz limit / sayı belirleme kısmı 
vardır.  
 
 
 
Sistemin yapacağı testler içinden en yüksek getirili X sayıda sonucu göstermesini buradan 
sağlayabiliriz. 
İpucu: Gelen listenin sonunda en kötü getiri ve bunu sağlayan opt değerleri de listelenecektir.  
Bunun istisnası şudur: Bir üstte bahsettiğimiz gibi, Senetleri Topluca Değerlendir seçili olur ise 
en kötü getiri gösterilmez.  
 
Sistem Tester – Sembol Seçimi Penceresinin en alt kısmında aşağıda göreceğiniz menü 
butonları vardır.

---

---

**📄 Source: PDF Page 69**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 69 / 107 
 
 
 
 
Buradaki menü / tanımlama seçenekleri şöyledir: 
Sol tarafta, sürekli test edebileceğimiz şekilde kendinize özel sembol listeleri 
oluşturabilirsiniz. 
Başlangıçta tanımlanmış bir liste yoktur. Diyelim ki, sürekli test ettiğiniz 5 adet senet var. 
Bunlar yukarıda listede görünür iken, bu kısımdaki kaydet tuşuna bastığımızda 
oluşturacağımız listeye isim vermemizi sağlayacak bir pencere açılır. 
 
 
 
Burada listeye isim verip Tamam tuşuna bastığınızda, Sistem tester – sembol seçimi 
penceresinde listelenmiş olan senetleri içeren bir grup oluşur ve mini pencerede görünür. 
 
 
 
Üzerine tıklayarak, bu grubu seçtiğinizde zemin rengi maviye dönüşür. 
 
Sil tuşu ile bu grubu silebilirsiniz. 
Yükle tuşu ile de, bu grup altındaki hisseleri test için listeye ekleyebiliriz. 
 İleri Tuşu: Hazır liste oluşturma mini penceresini hemen sağındaki 
 tuşuna 
basarsanız ek ayarlamalar yapabileceğiniz ‘Sistem Ayarları’  penceresi açılır.

---

---

**📄 Source: PDF Page 70**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 70 / 107 
 
 
4.6 Sistem Ayarları: 
Sistem ayarları penceresi aşağıdaki görünüme sahiptir.  
 
 
 
 
 
→Bu pencere üzerinden yapabileceğiniz ayarlar / düzenlemeler: 
 
 Simülasyon Adı:  
Otomatik gelir. Dilerseniz bu ismi değiştirebilirsiniz. Sistemi çalıştırdığınızda, simülasyon 
sonuçları penceresinde bu isimle görülür.  
 
 
 
 Puan Testi:  
Test yapılırken, finansal enstrümanın yapısına göre tercih edebileceğiniz 2 ayrı seçenek 
vardır. Normalde 1.000 TL başlangıç bakiyesi ile işlem yapılır ve artış / azalışlarda elde 
bulunan para kullanılarak devam edilir. 
Özellikle VİOP enstrümanlarında, sözleşme sayısı sizin için parasal tutardan daha anlamlı 
olabilir. Bu durumda, puan testi seçeneğini işaretleyebilirsiniz.  
 
 
 
 
Bu seçim yapıldığında, her seferinde 1 sözleşme / 1 lot alım ya da satım yapıldığı varsayılır. 
Testin başlangıç tarihindeki, sembolün kapanış değeri baz alınır. Elde edilen getirinin bu 
değere göre % lik oranı, getiri yüzdesi olarak hesaplanır, gösterilir.

---

---

**📄 Source: PDF Page 71**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 71 / 107 
 
 
Ek Bilgi:  
 
Başlangıç bakiyesi ile test yaptığınızda, raporun performans sekmesinde % Değişim - % Getiri 
karşılaştırması görürsünüz.  
 
 
 
Puan testi yaptığınızda ise, raporun performans sekmesinde Data – Getiri karşılaştırması 
görürsünüz.  
 
 
 
 
 
 Başlangıç Bakiyesini değiştirebilirsiniz. 
 
 Kaldıraç ekleyebilirsiniz. 
 
 Komisyon oranı / Faiz oranı girebilirsiniz. 
 
 İşlem Tipi önemlidir. 
 
 Senet ise: Normalde sadece AL-SAT seçiniz.  
 
 VİOP ise: Tüm işlemler ( Açığa sat – açık pozisyon kapat da dahil) seçiniz. 
 
Alarm ver seçeneği için, Sistem Ayarları penceresinin sağ üst kısmını kullanabilirsiniz. 
Tüm sinyaller için / Sadece Kalıcı sinyaller için seçeneği vardır.  İçinde bulunulan bar ( seçili 
zaman dilimi) kapanana kadar, sinyal, geçici sinyal olarak tanımlanır. Çünkü bar kapanmadan 
gerçekleşecek bir fiyat değişikliği ile sinyal devreden çıkabilir. Bar kapandıktan sonra, sinyal 
koşulu hala geçerli ise, kalıcı hale dönüşür.  
Hemen altındaki ‘Sürekli Sesli Uyarı Modu’ ile alarmın bizi sesle uyarmasını da 
sağlayabilirsiniz. 
 
Gösterge renklerini değiştirebilirsiniz.

---

---

**📄 Source: PDF Page 72**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 72 / 107 
 
 
 
 
 
Üst satırdan normal alış satışlar için, alt satırdan açığa satış, açık pozisyon kapama için ayrı 
ayrı tanımlamalar yapabilirsiniz. 
Ok kullan / işaret kullan seçenekleri ile grafik üzerinde AL sat sinyallerinin ne şekilde 
görüneceğini belirleyebilirsiniz.    
Sonuç sayfasının altında grafik üzerinde göster seçeneği vardır. 
 
 
 Fiyat Seçenekleri Butonu 
 
 
Bu tuş ile sistem tester back testi için kullanmak istediğiniz fiyat tipini seçebileceğiniz bir 
pencere açılır. 
 
 
 
Pencerelerin kenarlarındaki Ok’a tuşlayarak, her bir işlem (Alış-Satış-Açığa Satış-Pozisyon 
Kapama) için ayrı ayrı fiyat tipleri seçebiliriz. 
 
 
 
Gene her bir işlem için, istediğiniz oran veya miktarda, fiyat kayması tanımlayabilirsiniz.

---

---

**📄 Source: PDF Page 73**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 73 / 107 
 
 
 
 
Bu kayma, yüzdelik oran ya da net sabit bir miktar şeklinde seçilebilir. Bu durumda sistem, 
belirlediğiniz düzeyde kayma uygulanmış haliyle belirlenen fiyat seviyesinde işlem yapar.   
İsterseniz 
 kısmı ile seçeceğiniz periyot kadar önceki bir 
zamandaki fiyatları kullanabiliriz.  
 
 
Dikkat: Fiyat seçeneklerinde aslolan kapanış seçilmesidir. Diğer seçimler sadece back-test 
sonuçlarını etkiler. Otomatik emir gönderiminde emirlerinizin seçtiğiniz fiyatla gönderilmesini 
sağlayamaz.  
İpucu: Gerçeğe yakın sonuçlar almak için, fiyat seçeneği olarak Kapanış seçmenin yanı sıra 
ters yönde (karı azaltıcı yönde) kayma uygulayınız. Back-test raporları bar kapanışına göre 
hesaplanır. Otomatik emir gönderimi bir sonraki barın açılışında gönderilir. Ve ayrıca 
kademelerden dolayı 1-3 kademe kaybedebilirsiniz. Kayma tanımlarken alışlarda + değer, 
satışlarda – (negatif) değer tanımlanmalıdır.  
 
 butonu ile bundan sonraki her seferinde, testin şimdi belirlediğimiz 
tanımlamalarla yapılmasını sağlarız. Varsayılan olarak kaydetmezseniz her seferinde bu 
parametreleri girmeniz gerekir. 
Varsayılan olarak kaydederseniz de, sistemin bu datalar ile çalışacağını unutmamalısınız. 
 
 
Tüm pozisyonları son barda kapat:  
Bu seçimi yaparsanız grafik üzerinde son barda pozisyonun sıfırlandığını görürsünüz. 
İpucu: Bu seçimi uygulamayınız. Eğer uygularsanız yeni barlarda sinyaller gelmeyecektir.  
 
 
Sistem içinde değişken tanımlı değil ise bu kısım pasif gelir. Değişken tanımlandığı takdirde 
bu kısım aktif ve seçili gelir. Seçimi kaldırırsanız sistem varsayılan değerlerle çalıştırılır. 
 
 
Bu seçimi yaparsanız sistem AL ve Açığa Sat durumlarında ilgili renklere boyanır.  
 
Bu seçimi işaretlediğiniz takdirde, emrin gerçekleştiği barın kapanış seviyesine bir sonraki 
sinyale kadar uzanan yatay bir çizgi çizilir. Son AL veya SAT için bu çizgi skalaya kadar uzatılır.

---

---

**📄 Source: PDF Page 74**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 74 / 107 
 
 
 
 
Geri al 
 tuşu ile bir önceki sistem tester- sembol seçimi penceresine 
dönersiniz. 
 Olasılığını seçersek, sistem eklenen yeni verilere göre sürekli 
güncelleme yapar.  
 Bundan sonra ‘çalıştır’ butonu ile test işlemini başlatabilirsiniz. 
 
4.7 Sistem Tester Sonuçları  
Çalıştır butonu ile sistemin çalışması sonucunda aşağıda bir örneğini göreceğiniz ‘System 
Tester Sonuçları’ tablosu gelir. 
 
4.7.1 Özet Sekmesi:  
İlk açılışta tablonun ‘Özet’ sekmesi görünür. Bu sekmede özet bilgiler vardır.

---

---

**📄 Source: PDF Page 75**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 75 / 107 
 
 
 
 
İlk satırda, sistem adı ve testin yapıldığı zamanın yanı sıra hangi senet için hangi tarihler 
arasında yapıldığını görebiliriz. 
 
Performans kısmında, Başlangıç bakiyesi, komisyon masrafları ve son bakiye, varsa faiz geliri 
ve yüzdelik getiri görülebilir. 
 
İşlemler kısmında, kaç işlem yapıldığı, bunların kaç tanesinin karlı, kaç tanesinin zararla 
kapatılmış işlem olduğu ve kaç tanesinin açık pozisyondan yapıldığı ve işlem başına ortalama 
kar / ortalama zarar miktarları görülebilir. 
İstatistikler kısmında, En karlı, en zararlı, en uzun süreli, en kısa süreli pozisyon bilgileri 
sunulur. 
 
İşlemsiz Süre kısmında, En uzun işlemsiz süre ve toplam işlemsiz süre görülebilir. 
 
Son Durum kısmında, son fiyat bilgisi, son işlem tarihi, niteliği ve fiyatı ve son bar itibari ile 
taşınan pozisyon bilgisi görülür. 
 
Sayfa altındaki menüler yardımı ile Sayfayı yazdırabilirsiniz / Sistem uygulamasını grafik 
üzerinde izleyebilirsiniz. / Pencereyi kapatabilirsiniz. 
 
→Sistemi grafikte görmek için bir örnek:

---

---

**📄 Source: PDF Page 76**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 76 / 107 
 
 
 
 
 
Yukarıda gördüğünüz grafiğin alt penceresi, çalışmakta olan sistemin kazanç eğrisini 
göstermektedir. Sistem tester penceresinin sol üst köşesinde Sistemin adı bulunur. Bunun 
hemen altında ‘Overall’ (Son toplam değer diye çevirebiliriz) karşısında ise, sistemin kullanımı 
halinde, başlangıçtaki paranın seçilmiş olan bardaki ulaşmış olduğu değer gösterilir. 
4.7.2 İşlemler Sekmesi:  
Yapılan tüm işlemleri bir grafik altında, tablo halinde gösterir. 
 
 
4.7.3 Pozisyon Sekmesi:  
Bu sekmede alınan her pozisyon için genel bilgiler verilir.

---

---

**📄 Source: PDF Page 77**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 77 / 107 
 
 
 
 
Her pozisyon için, miktar / Açılış-Kapanış tarihleri, fiyat, komisyon ve kar-zarar ( toplam değer 
– değer farkı) bilgileri verilir. 
 
4.7.4 Performans Sekmesi:   
Bu sekmede, işlemlerimizin sonucu ile finansal enstrümanın getirisi grafik üzerinde 
karşılaştırılır.

---

---

**📄 Source: PDF Page 78**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 78 / 107 
 
 
4.7.5 Sistem Bilgileri sekmesinde, kullanılan sistemin teknik bilgileri yer alır. 
 
 
Bu sekmenin ilk kısmında sistemin adı-tipi ve yazdı isek NOT içeriği görülür. 
İkinci kısmında, AL-SAT-Açığa Sat-Açık Pozisyon Kapat koşullarının formülleri ve 
tanımlamaları görülür. 
Stop kısmında, stop tanımlamaları ve varsa değişken bilgileri görülür. 
Sayfa altındaki menüler yardımı ile Sayfayı yazdırabilirsiniz / Test sonuçlarını grafik üzerinde 
izleyebilirsiniz / Pencereyi kapatabilirsiniz. 
Doğal olarak hangi grafik üzerinde uyguladı iseniz, O grafiğin ait olduğu senedin verileri gelir. 
 
İpucu: Eğer sistemde değişken tanımladı iseniz doğal olarak test çoklu seçenek için 
yapılacaktır. Bu durumda, karşınıza yukarıda gördüğünüz sonuç tablosu değil, aşağıda 
göreceğiniz gibi bir tablo gelecektir.

---

---

**📄 Source: PDF Page 79**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 79 / 107 
 
 
 
Bu tablo tanımladığınız değişkenlerin olası değerleri için, seçtiğiniz sayıdaki en iyi X getiri 
sonucunu gösterir.  
Mesela yukarıda en iyi 5 getiri seçilmiş olup, bunların sonuçları görülmektedir. 
Sütunların açıklamaları: 
İlk sütunda sıra numarası vardır. 
 
 Getiri: Rakamsal getiriyi gösterir. 
 
 % Getiri: Oransal getiriyi gösterir. 
 
 İşlem sayısı: İlgili satırdaki test için kaç adet işlem yapıldığını gösterir. 
 
 Kar / zarar: Yapılan işlemlerin kaç tanesinin karlı işlem; kaç tanesinin ise zararla sonuçlanan 
işlem olduğunu gösterir. 
 
 Komisyon: işlemler için ödenecek komisyonu gösterir. 
 
 Overall: Portföyün son değerini gösterir. 
 
 OPT1: İlk değişkenin bu test için alınmış olan değerini gösterir. 
 
 OPT2: İkinci değişkenin bu test için alınmış olan değerini gösterir.

---

---

**📄 Source: PDF Page 80**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 80 / 107 
 
 
4.8 Grafik Üzerinde Ek Menüler 
Sistem Tester uygulamasını grafik üzerine atadıktan sonra KHN butonu altına Sistem Tester 
ile ilgili bazı ek menü seçenekleri gelecektir. Aşağıdaki resimde sağ tarafta eklenen menü 
seçeneklerini görebilirsiniz. 
 
 
 
Sistem Raporu: Bu menü seçeneği ile uygulamadaki sistemin ‘Sonuç Raporu’ açılır. Bakınız 
4.7 Sistem Tester Sonuçları  
 
Sistem Ayarları: Bu menü altında bulunan alt menüler ile uygulamadaki sistemde kullanmış 
olduğunuz parametreleri izleyebilir / değiştirebilirsiniz. 
Bu seçenekler önceki bölümlerde anlatılmıştır. 
 
 Tarih Aralığı: Sistemin çalıştığı tarih aralığını gösterir. 
 Seçenekler: Uygulamadaki sistemin ayarlarını içeren ‘Sistem Ayarları’ penceresini 
açar. 
 Değişkenler: Uygulanan sistemde ‘Değişken’ kullanımı var ise, grafik üzerine atanan 
seçenekteki değişken (OPT) değerlerini gösterir. buradaki OPT alt menüsüne 
tıklarsanız, aşağıda göreceğiniz Değişkenler isimli pencere açılır.  
 
 
 
            Buradan sistemde kullanılan değişken rakamını değiştirebilirsiniz. 
 
 Sistemi Düzenle: Bu menü altında uygulamadaki sistemin ‘Sistem Düzenleme’ 
penceresi açılır. Dilerseniz buradan koşullarınızı değiştirebilirsiniz.  
 Simulasyonu Yeniden Hesapla: Veri eksiği vb. olasılıklar yüzünden hesaplamanın 
yeniden yapılmasını isterseniz bu menü seçeneği ile sağlayabilirsiniz.

---

---

**📄 Source: PDF Page 81**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 81 / 107 
 
 
İpucu: otomatik Emir Gönderimi (Bağlı Emir) söz konusu ise, programın kapalı olduğu 
zamanlarda oluşan sinyaller grafik üzerinde gösterilmez. Bu menü seçeneği ile bu 
dönemlerdeki sinyallerin grafik üzerine atanmasını sağlayabilirsiniz. 
 
 Bağlı Emirler: Lisansa tabii bir Matriks uygulaması olan Otomatik Emir gönderimi için, 
sistem tester uygulamasının emre dönüşmesini sağlayacak menü seçeneğidir. Ayrı bir 
dokümanda anlatılmıştır.  
Gerçekleşen Sistem Alarmları :  
Sistem Tester içinde kurmuş olduğunuz alarmlar içinde gerçekleşmiş olanları topluca gösteren ‘Sistem 
Tester Alarmları’ penceresi açılır.  
 
 
Favori Sistemlerim : 
Tanımlı sistemlerin listelendiği System Tester ana ekranında bulunan tanımlı sistemlerden, istediğiniz 
sistemleri seçerek ‘Favorilerime ekle / çıkar’ butonları ile favorilere ekleyebilirsiniz. Bu şekilde 
favorilerinize eklediğiniz sistemlerin listedeki adının yanında, aşağıda göreceğiniz şekilde, parantez 
içinde bir yıldız görünür.  
 
 
 
Bu şekilde isterseniz topluca çalıştırılabilecek bir favori sistemler listesi oluşturabilirsiniz. ‘Favori 
Sistemlerim’ uygulaması ile bu şekilde tanımlanmış olan tüm sistemlerin bir arada çalışmasını ve 
sonuçların tüm tanımlanmış olan sistemlerde verilmesini sağlayabilirsiniz. 
Favori olarak sistem belirledi iseniz, bu sistemler bu menü altında listelenecektir.  
 
 
 
Ve bunlardan herhangi birisini seçerek çalıştırabilir, ya da ‘En iyi sonuçları bul’ seçeneği ile tümünü 
çalıştırıp sonuçları aşağıdaki gibi bir tablo halinde izleyebilirsiniz.

---

---

**📄 Source: PDF Page 82**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 82 / 107 
 
 
5. Explorer  
5.1. İlk Bakış: 
Seçilen semboller arasında istenen kriterlere uyan sembolleri seçebilmenizi sağlar. İlk olarak 
aşağıda göreceğiniz ‘Explorer’ penceresi açılır.  
 
 
İlk açıldığında Tanımlı Explorer Sistemlerini gördüğünüz bir pencere gelir. Bu pencerenin 
üstündeki menü tuşlarının işlevleri şöyledir. 
 
5.1.1 Yeni Sistem:  
Bu menü ile yeni bir sistem tanımlamaya başlayabilirsiniz. Aşağıda anlatılacaktır. 
5.1.2 Düzenle:  
Bu menü ile tanımlı sistemlerden birini seçip değişiklik yapabilirsiniz. 
5.1.3 Sil:  
Bu menü ile tanımlı sistemlerden seçtiğiniz sistemi silebilirsiniz. 
5.1.4 Sistem Gönder:  
Bakınız System tester / Sistem Gönder 4.1.4 
5.1.5 Sistem Al:  
Bakınız System tester / Sistem Al 4.1.5  
5.1.6 Tanımlı Explorer Sistemleri:  
Pencerenin bu kısmında Tanımlı (Hazır / Sizin Eklediğiniz)  sistemler vardır.  
5.1.7 Çalıştır:  
Bu menü ile tanımlı sistemlerden birini seçip uygulama yapabilirsiniz. 
5.1.8 Kapat:  
Explorer penceresini kapatırsınız.

---

---

**📄 Source: PDF Page 83**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 83 / 107 
 
 
5.2. Yeni Sistem: 
Örnek olarak Explorer’da 5 günlük hareketli ortalamasını kesmiş olan hisse senetlerini 
bulmak istediğimizi varsayalım. Bunun için;  
 
‘Yeni Sistem’ butonuna tıklayınız. Explorer editor penceresi açılır. Temel olarak daha önce 
anlattığımız ‘Sistem Tester’ın sistem yazma penceresine benzer. 
 
 
 
Yazacağınız Explorer sistemine bir isim veriniz. Altındaki ‘NOT’ bölümünden not 
ekleyebilirsiniz. 
Explorer Editor Penceresinde 6 adet 1-6 numaralı sekme ve bir de Filtre sekmesi 
göreceksiniz.  
Filtre sekmesi, koşul tanımlanması için kullanılırken, 1-6 arası numaralanmış olan kolonlar, 
analizi yapılacak olan sembollere ait bilgi alanları olarak kullanılabilir. 
Bu veriler; kapanış, düşük, hacim benzeri fiyat alanları olabileceği gibi, bir indikatör ya da 
tanımlanmış herhangi başka bir formülün değeri olabilir. Kolon Adı mini penceresi ile veri 
listelenecek kolona isim verebilirsiniz. 
5.2.1 Filtre Sekmesi:  
Eğer yalnızca yazacağınız koşula uyan senetleri bulmak istiyorsanız koşulunuzu Filtre kısmına 
yazmanız gerekli ve yeterlidir.  
Cross(C,MOV(c,5,s)) yazdığınızda, kapanışı son barda 5 günlük hareketli ortalamasının 
üzerine çıkmış hisseleri getirecektir.

---

---

**📄 Source: PDF Page 84**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 84 / 107 
 
 
Ancak daha fazla detay görmek isterseniz, hacim, kapanışın değeri vb. gibi; bu durumda 
kolonlara izlemek istediğiniz veriyi sembolize eden kodlamayı yazmalısınız. Mesela 1. Kolona 
C (Close = Kapanış), 2. Kolona da V (Volume = Hacim) yazarak bu verileri de ayrıca 
izleyebilirsiniz.  
Kolonlara veri tanımlaması yaptığınızda, filtre kısmında bulunan koşulunuza uyan hisse 
senetleri bu verileri de içeren bir tablo eşliğinde gösterilecektir.  
 
DİKKAT: Filtre sekmesinde Formül yazısının hemen üzerinde, Filtreyi Kullan seçeneği vardır. 
   
  
Filtrenin çalışmasını istiyorsanız, mutlaka bu seçimi yapmış olmalısınız. 
 
İpucu: Normalde kolonlara veri izlemek için formül yazıyoruz. Filtre kısmına ise koşul 
belirliyoruz. Eğer kolonlarda yazdığınız formülü / veriyi bir bütün olarak filtre kısmında da 
kullanıyorsanız, ‘Filtre’ kısmına yazacağınız koşulu, kolonların adlarını kullanarak da 
belirleyebilirsiniz.  
Mesela cola>colb gibi. 
5.2.2 Bilgi kolonları:  
1-6 nolu sekmelerde veri tanımlaması yaparsanız, Explorer sonuç tablosunda koşula uyan 
senetlerin, tanımladığınız verileri gösterilecektir. Mesela bu durumda 1. kolonda hisse 
senetlerinin kapanış değerleri, 2. Kolonda ise hacim verileri listelenecektir.  
İpucu: Explorer sonuç penceresi altında ‘Ek Kolon Seçimi’ butonu vardır. Fiyat penceresinde 
var olan verileri bu kısımdan da rahatça tablonuza ekleyebilirsiniz. 
  
Explorer’da mutlaka bir filtre kullanmanıza gerek yoktur. Seçtiğiniz hisselerin sadece belirli 
fiyat vb. bilgilerini arıyorsanız da yine Explorer’ı kullanabilirsiniz. 
 
İpucu: Ek olarak, 1-6 arası bilgi alanlarının alternatif bir kullanım şekli, o alanlara da kriterler 
girilmesi olabilir. Bu durumda, o alana girilen kriter doğruysa “1”, değilse “0” değer 
dönecektir. Bu kullanım şekli, tüm hisselerin belli koşulları sağlayıp sağlamadığı şeklinde bir 
listeleme yapmak için kullanılabilir. 
5.2.3 Sembol Seçimi:  
Explorer Editor penceresinin alt taraftaki ‘Sembol Listesi’ butonu ile sembol ve tarih aralığı 
seçebileceğiniz Explorer-Sembol Seçimi penceresi açılır.  
 
İpucu: Sembol seçimini sisteminizi oluşturduktan sonra çalıştırma aşamasında da yapabilir 
veya seçiminizi değiştirebilirsiniz.

---

---

**📄 Source: PDF Page 85**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 85 / 107 
 
 
 
 
Bu pencere de, genel olarak Sistem Tester’ın sembol seçimi penceresine benzer. 
Üst kısım tamamıyla aynıdır.  
Sembol Kodu penceresinden bir sembol seçip, ‘Ekle’ butonu ile seçtiğiniz sembolü listeye 
ekleyebilirsiniz.  
 
İpucu: Explorer’da asıl amaç sembolleri çoklu olarak taramaktır. Bu sebeple normalde bu 
kısmı değil, hemen aşağıda bahsedeceğimiz Çoklu sembol Seçimi butonunu kullanırsınız. Bu 
kısımdan, özel olarak eklemek istediğiniz birkaç tek sembol olur ise, onları ekleyebilirsiniz.  
 
 Periyot penceresinden testin kullanacağı periyodu,  
 
 Birim penceresinden de, sonuçları görmek istediğiniz para birimini seçebilirsiniz. 
 
 Tüm Periyotları değiştir ile Bakınız…4.6.4 Tüm Periyotları değiştir  
 
 Tüm birimleri değiştir ile Bakınız…4.6.5 Tüm birimleri değiştir 
 
 Ekle butonu ile Sembol Kodu penceresinde görülen finansal enstrüman listeye 
eklenir. 
 
 Sil butonu ile listeden seçeceğiniz bir sembolü ( üzerine tıklayıp seçtiğinizde zemin 
rengi maviye dönüşür) silebilirsiniz. 
 
 Tümü Sil butonu ile listedeki seçilmiş tüm sembolleri silebilirsiniz.

---

---

**📄 Source: PDF Page 86**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 86 / 107 
 
 
 Çoklu sembol Seçimi butonu ile test etmek istediğiniz sembolleri topluca listeye 
ekleyebileceğiniz ‘Senet Seçiniz’ penceresi açılır.  
 
 
 
Bu pencere üzerinden sistemde taranmasını istediğiniz sembolleri seçebilirsiniz. 
 
 Sembol Grubu Ekle butonu, bir sembol grubunu farklı bir periyod için ekleyebilmenizi 
ve böylece aynı anda birden fazla periyodu test edebilmenizi sağlar. 
 
Sembol Grubu Ekle butonu ile gene Senet Seçim Penceresi açılır. Bu butona tıklamadan önce 
Explorer-Sembol Seçim penceresinin üst kısmındaki ilgili bölmeden periyodu değiştiriniz. 
Senet Seçim penceresi ile seçeceğiniz semboller bu periyod için eklenecektir. Böylece farklı 
periyodlara sahip sembol gruplarını Explorer listenize ekleyebilirsiniz.   
 
Explorer – Sembol seçimi penceresinin alt kısmında tarih belirleme bölümü vardır. 
 
 
Buradan analizin çalışacağı dönemi seçebilirsiniz. 
 Son XXX barı kullan seçeneği ile belirleyeceğiniz miktarda barı ( seçmiş olduğunuz 
periyod birimi) kullanır ya da tüm barları kullanır. 
 
Dikkat: Bu kısımda seçiminizi olabildiğince yüksek (Tüm barları kullan olarak) tutunuz. Bar 
sayısını azaltmanızın bir faydası yoktur. Koşulunuzda kullandığınız indikatörlerin periyotları 
yüksek olur ve burada da az sayıda bar kullanımını seçerseniz, elde edeceğiniz sonuçlar hatalı 
olacaktır.

---

---

**📄 Source: PDF Page 87**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 87 / 107 
 
 
 İnceleme Tarihi: 
Son barı, ya da geçmişten bir günü seçebiliriz. Son bar seçili olduğunda explorer’ı son barda 
çalıştırır. Geçmişten bir tarih seçersek o tarih itibari ile çalıştırır. Ondan sonraki günler hesaba 
katılmaz.  
 
İpucu: Explorer uygulaması kapanıştaki sonuçlara göre oluşan gerçekleşmeleri veya seans 
esnasında ise, içinde bulunduğumuz bar ile bir önceki bar kapanışında oluşan gerçekleşmeleri 
gösterir. Çünkü amaç, koşulun gerçekleştiği zamanı yakalamaktır. 
Bu sebeple, mesela 3 bar önceki bir koşul gerçekleşmesini göstermez. Bir sebeple önceki bir 
zaman için sonuçları görmek isterseniz, inceleme tarihi kısmından geçmiş bir tarihi seçmeniz 
gerekir. 
 
Sembol seçiminiz tamamlandıktan ve zamansal seçimlerinizi yaptıktan sonra sistem 
çalışmaya hazır halde olacaktır. 
Sistem yazımını tamamladıktan sonra Explorer Editor penceresinin alt kısmındaki  ‘Tamam’ 
butonuna tıklayınız. Sisteminiz verdiğiniz isim ile tanımlı sistemler arasında listelenecektir.  
5.3. Çalıştır İşlevi:  
Tanımlı bir sistemi seçip ‘Çalıştır’ dediğinizde karşınıza gene sembol seçim penceresi ama bu 
sefer ‘Çalıştır’ butonu seçeneği ile gelir. Bu size seçimlerinizi / ayarlarınızı bir kez daha gözden 
geçirme fırsatı verecektir. 
 
 
 
 
 Hatırlatma: Sembol Grubu Ekle butonu, bir sembol grubunu farklı bir periyot için 
ekleyebilmenizi ve böylece aynı anda birden fazla periyodu test edebilmenizi sağlar.

---

---

**📄 Source: PDF Page 88**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 88 / 107 
 
 
Sembol Grubu Ekle butonu ile gene Senet Seçim Penceresi açılır. Bu butona tıklamadan önce 
Explorer-Sembol Seçim penceresinin üst kısmındaki ilgili bölmeden periyodu değiştiriniz.  
 
Senet Seçim penceresi ile seçeceğiniz semboller bu periyod için eklenecektir. Böylece farklı 
periyodlara sahip sembol gruplarını Explorer listenize ekleyebilirsiniz.   
 
Çalıştır butonuna tıkladığınızda sisteminiz seçmiş olduğunuz sembolleri belirlediğiniz 
koşullara göre tarar. 
 
Bir explorer sistemi çalıştırılıp raporu alındığında aşağıdaki gibi bir sonuç tablosu gelir. 
 
 
 
Yukarıdan şunu anlıyoruz: Sistemin taraması sonucunda, seçtiğimiz finansal enstrümanlardan 
yazdığımız koşula uyanlar yukarıda görülen 2 adet semboldür. 
 
İpucu: Explorer sistemleri verdiğimiz koşula son + bir önceki periyot esnasında uyan 
sembolleri listeler. Mesela her sabah ‘Günlük Periyot’ ile tarama yaparsanız, bir önceki günün 
kapanış verilerine göre koşulunuza uyan sembolleri bulursunuz. 
  
5.3.1 Sonuçlar sekmesi:  
Pencere bu sekme ile açılır. Uyguladığınız koşula uygun sonuç veren finansal enstrümanlar bu 
sekmede listelenir.  
Bu liste, seçilen sembollerden ( burada BİST 100 seçtik), seçilen periyot içinde, hareketli 
ortalaması MOST’unu kesen hisselerin tespiti sonucu ortaya çıkmıştır. 
Pencerenin üst kısmında, analizin adı ve yapıldığı zaman yazılıdır. 
 
5.3.2 Filtrelenenler sekmesinde; 
Uyguladığınız indikatöre uygun sonuç vermeyen ve dolayısı ile elenen ( filtrelenen)  finansal 
enstrümanlar listelenir. Bu sekmeye tuşlarsanız, filtrelenen sembollerin listesi gelir.

---

---

**📄 Source: PDF Page 89**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 89 / 107 
 
 
 
5.3.3 Özet sekmesinde ise,  
 
 
 
Uygulanan indikatör sisteminin adı, formülü ve kullanım durumu gösterilir., 
Explorer sonuç penceresinin alt kısmında aşağıda anlatacağımız uygulamalar vardır:  
 
5.3.4 Otomatik Yenileme  
 Otomatik olarak çalışıp, yeni verilere göre sonuçları sunmayı sağlayacak 
bir alandır. Bu sayede, belirlenen periyotta otomatik olarak yeniden çalışıp, listenin 
güncellenmesi sağlanabilir. İlk kutucuğa tıklayıp seçim yapmak ve 2. kutucuk içine kaç 
dakikada bir yenileme yapmasını istiyorsanız, o rakamı girmeniz gerekir. 
İlk kutucuğa tıkladığınızda,  pencerenin sağ alt tarafında Gizle butonu görünür. 
 
 
Bu butona basarak bu pencerenin gizlenmesini sağlayabilirsiniz.  
Veriler yenilendiğinde pencere otomatik olarak açılacaktır.

---

---

**📄 Source: PDF Page 90**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 90 / 107 
 
 
5.3.5 Değişen Sembolleri Göster:  
 Bu seçeneği etkinleştirirseniz, bir önceki listeye göre değişen 
sembolleri gösterir. Sistem her güncellemede bir önceki tarama sonucuna göre, eklenenler 
ve çıkarılanlar olarak sembol bilgisi verecektir. 
5.3.6 Default Olarak Kaydet:  
 tuşu ile ilgili Explorer analizi bundan sonraki çalıştırmalarda 
tanımladığınız parametreler ile ön tanımlı olarak gelir. 
 
 seçeneği ile tablonun yazıcıdan çıktısını alırsınız. 
 seçeneği ile tabloya Excel tablosu halinde sahip olursunuz. 
tuşu ile aşağıda göreceğiniz Ek Kolon Seçim penceresi açılır. 
 
 
 
Buradan görmek istediğiniz verileri seçip ekleyerek, bu veri sütunlarının tablonuza kolon 
olarak eklenmesini sağlayabilirsiniz. Pencerenin sağ tarafı boş gelir. Oklar vasıtası ile tek tek 
ekleyebilir / çıkarabilirsiniz. Fiyat penceresinde ulaşabileceğiniz verileri buradan kolayca 
ekleyebilir ve sonuç tablosunda görebilirsiniz.  
 
 butonu ile analizi ( ve sonuçlarını) güncelleyebilirsiniz. 
 butonu ile Explorer analiz sonucu penceresini kapatırsınız. 
 
Ek Bilgi : Explorer uygulamasına TOPLU AL   / TOPLU SAT seçeneği eklenmiştir.

---

---

**📄 Source: PDF Page 91**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 91 / 107 
 
 
 
Sonuçlar penceresinin hemen altında ilgili butonları görebilirsiniz.  
Birini seçtiğinizde aşağıda göreceğiniz pencere açılır.  
 
 
Emir tipini, Piyasa / Aktif / Pasif olarak seçebilirsiniz.  
İşlem limitinizi toplam rakam olarak (her bir hisseye eşit paylaştırlır) veya her bir sembol için 
alınacak tutar olarak tamımlayabilirsiniz. Bu seçimi yaparken dikkatli olunuz.  
Tamam dediğiniz anda, sistem portföy pencerenizin toplu emirler sekmesine gider.  
Buradaki sonuç ve seçimlerinize göre semboller listeli halde gelir.  
Size sadece gönder butonuna basmak kalır.

---

---

**📄 Source: PDF Page 92**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 92 / 107 
 
 
6. Expert Advisor  
Expert Advisor, yatırımcıların işlem yaparken karar verme sürecine destek olmak için 
yazılmış, System Tester mantığı taşıyan farklı muhtelif seçenekler içeren bir analizdir.  
 
İpucu: Sistem tester’da geçmişi test edebilirsiniz. Expert Advisor’da edemezsiniz. Burada 
birden fazla AL / SAT koşulunu ayrı ayrı yazıp hepsinin sinyallerini ayrı ayrı görebilirsiniz. AL ve 
SAT sinyalleri, Sistem Tester’da olduğu gibi birbirini takip etmek zorunda değildir.  
6.1.Genel Bakış:  
KHN’den Expert Advisor’ı tıkladığınızda açılan pencerede varsa tanımlı sistemleri görürsünüz. 
 
 
 
 Yeni Sistem: Bu menü ile yeni bir sistem tanımlamaya başlayabilirsiniz. Aşağıda 
anlatılacaktır. 
 
 Düzenle: Bu menü ile tanımlı sistemlerden birini seçip değişiklik yapabilirsiniz. 
 
 Sil: Bu menü ile tanımlı sistemlerden seçtiğiniz sistemi silebilirsiniz. 
 
 Sistem Gönder: Bakınız 4.1.4 Sistem Gönder 
 
 Sistem Al: Bakınız 4.1.5 Sistem Al 
 
 Tanımlı Explorer Sistemleri: Pencerenin bu kısmında Tanımlı (Hazır / Bizim 
Eklediğimiz)  sistemler vardır. 
 
 Uygula: Bu menü ile tanımlı sistemlerden birini seçip uygulama yapabilirsiniz. 
 
 Kapat: Explorer penceresini kapatırsınız.

---

---

**📄 Source: PDF Page 93**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 93 / 107 
 
 
6.2. Yeni Sistem:  
Bu menüyü tuşladığınızda karşınıza Expert Advisor Editor penceresi gelir. 
 
 
 
 Öncelikle sisteminize bir isim veriniz.   
 
 Trendler, Renkler, Semboller, Alarmlar ve Not sekmelerini göreceksiniz.  
 
 Bunların hepsini aynı anda kullanabileceğiniz gibi, tek tek de kullanabilirsiniz. 
 
 Fonksiyonlar butonu ile daha önce diğer sistemlerde gördüğümüz Formül 
Tanımlamayı kolaylaştıran fonksiyonlar penceresi açılır. 
 
 Her kısmın altındaki Desen ve Renk kısımlarında görsel eklemeler yapabilirsiniz.  
 
İpucu: Sağ tarafta bulunan ‘Fonksiyonlar’ butonu ile İndikatör / Alanlar / Fonksiyonlar 
seçeneklerinin bulunduğu (İndikatör Builder’da doğrudan var olan) pencere açılır. 
Formüllerinizi yazarken buradan şablonları alabilirsiniz.  
6.2.1. Trendler Sekmesi:  
Bu bölümde Boğa Piyasası ve Ayı Piyasası pencereleri vardır.   
Boğa Piyasası Al koşulunu (Yükseliş yönünü) temsil eder. Klasik rengi yeşildir. 
Ayı Piyasası Sat koşulunu (Düşüş yönünü) temsil eder. Klasik rengi kırmızıdır. 
Burada bahsedilen trend kavramı, teknik analizde çizgi olarak çizilen trendler değil, piyasanın 
yönü anlamında yükseliş ya da düşüşü ifade etmektedir. 
6.2.2. Renkler Sekmesi:  
Bu bölümde yapılan düzenlemeler, grafik üzerine atayacağınız (AL-SAT için oluşturacağınız) 
şekil ve yazıların renklerini belirler. Oluşturulan kritere göre, aşırı alım bölgesi, aşırı satım 
bölgesi ya da izlenmeye başlanacak bir noktaya gelinmesi gibi farklı yapılara göre kriterler 
oluşturulabilir. Bu kriterler gerçekleştiğinde, kriter geçerliliğini koruduğu sürece barlar

---

---

**📄 Source: PDF Page 94**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 94 / 107 
 
 
istenen şekilde boyanacak, kriterin geçerliliği ortadan kalktığında normal grafik ayarlarına 
geri dönecektir. 
CROSS kullandığınız durumlarda AL ve SAT koşullarının oluştuğu noktaları renkli olarak 
gösterecek.  
Renkler sekmesinde Al koşuluna Trendler sekmesinde boğa piyasası için yazdığınız koşulu 
yazınız. Adı kısmına AL adını yazınız. Aşağıdaki görünüm olacaktır. 
 
 
 
Sağ orta taraftaki Kaydet duşuna bastığınızda, AL koşulu hafızaya kaydedilir ve alta geçer. 
Görünüm aşağıdaki gibi olur. 
 
 
 
SAT koşulu için tersini yazıp kaydediniz. Aşağıdaki görünüm oluşacaktır.

---

---

**📄 Source: PDF Page 95**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 95 / 107 
 
 
Renkler sekmesinde, sağ taraftaki tuşların işlevleri şöyledir: 
 Yeni tuşu: Yeni bir koşul girmek üzere üst pencereyi temizler. 
 
 Kaydet tuşu: Girdiğiniz koşulu kaydedip, adı ile alt pencereye yerleşmesini sağlar. 
Pencereye tanımladığınız koşullar için 2 tip seçim söz konusudur. 
Üzerine tıklayarak seçim: Zemin rengi maviye dönüşür. Tekrar tıkladığınızda, seçim iptal olur 
ve zemin renksizleşir. 
Önündeki kutucuğu tıklayarak seçim: Kutucuğun içine check işareti gelir. Tekrar 
tıkladığınızda, seçim iptal olur ve kutucuk boşalır. 
 
 Sil tuşu: Alt pencerede seçilmiş durumda olan koşulu siler. 
 Tümünü Seç tuşu: Alt penceredeki koşulların tümünü seçer.  
 Seçimleri İptal Et Tuşu: Alt penceredeki seçimleri iptal eder. 
 
Al ve Sat koşulunu yazıp kaydettikten sonra çalıştırdığınızda, ortaya çıkacak grafik aşağıdaki 
gibi olacaktır. Kesişimlerin olduğu barların renklerini seçtiğiniz renklerle boyayacaktır ve AL-
SAT noktalarını altta yeşil ve kırmızı çerçevelerle gösterilecektir.

---

---

**📄 Source: PDF Page 96**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 96 / 107 
 
 
6.2.3. Semboller Sekmesi:  
Burada da, Adı kısmına koşulumuzun adını, koşul kısmına koşul formülümüzü yazıyoruz.  
 
 
 
Sembol Seç kısmından koşulunuzun gerçekleştiği noktada nasıl bir sinyal görmek istiyorsanız 
onun seçimini yapınız. Oklar ile veya AL, SAT, TUT gibi yazı şeklinde. Sembol seçimi dışında 
etiket kısmına herhangi bir şey yazarsanız örneğin AL gibi, koşulun gerçekleştiği barın altına 
etiket koymaktadır.  
Barın üstüne / altına seçeneklerini, seçtiğiniz sembollerin grafikteki barların üstüne ya da 
altına koymak için kullanınız. 
Gene kaydederek aşağıya taşınmasını (kayıtlara geçmesini) sağlamanız gerekiyor. Farklı 
renkler verirseniz daha kolay dikkatinizi çekecektir.  
Buradaki koşullar renkler kısmındaki ile aynı olacaktır. Kopyalayıp taşıyabilirsiniz.  
Alt sağ taraftaki tuşların ( Yeni, kaydet, Sil, Tümünü Seç, Seçimleri iptal et) işlevleri aynen 
renkler sekmesinde olduğu gibidir. 
 
Bu işlemi yaptıktan ve uyguladıktan sonra ki görüntü aşağıdaki gibi olacaktır.

---

---

**📄 Source: PDF Page 97**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 97 / 107 
 
 
 
 
6.2.4. Alarmlar Sekmesi:  
Expert Advisor Matriks E-broker ve Matriks Trader’a sinyal göndermektedir. Bunun için 
Alarmlar penceresinden bu seçimi yapmak gerekir. 
Burada da koşulları aynen taşıyabilirsiniz. AL ve SAT için ayrı ayrı kopyalamayı unutmayınız.  
 
 
 
Her koşul için adının altına bir de mesaj girebileceğimiz bir pencere vardır. Alarm 
gerçekleştiği takdirde, bu mesajı da gösterir. 
Tüm sinyaller için / sadece kalıcı sinyaller için seçeneğinde kalıcı sinyalleri seçmeniz daha 
uygun olacaktır.  
 
İçinde bulunulan bar ( seçili zaman dilimi) kapanana kadar, sinyal, geçici sinyal olarak 
tanımlanır. Çünkü bar kapanmadan gerçekleşecek bir fiyat değişikliği ile sinyal devreden 
çıkabilir. Bar kapandıktan sonra, sinyal koşulu hala geçerli ise, sinyal kalıcı hale dönüşür.

---

---

**📄 Source: PDF Page 98**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 98 / 107 
 
 
 
 
Alt sağ taraftaki tuşların ( Yeni, kaydet, Sil, Tümünü Seç, Seçimleri iptal et) işlevleri aynen 
renkler sekmesinde olduğu gibidir. 
Sistem koşulun gerçekleştiği yerde işlem platformunuza sinyal gönderecek olup sizin onayınız 
olmadan alım ya da satım işlemi yapmaz.  
6.2.5. NOT Sekmesi:  
Kurduğunuz sistemle ilgili sonradan görmek isteyeceğiniz açıklamayı yazabileceğiniz boş bir 
pencere gelir.  
 
 
 
Sistem yazımını bitirip TAMAM dediğinizde sisteminiz Expert Advisor altında tanımlı sistemler 
kısmına eklenir. 
 
 
Listeden bu sistemi seçip ‘uygula’ tuşuna bastığınızda yukarıda görmüş olduğunuz sistemin 
Grafik üzerine uygulanmış hali gelir.

---

---

**📄 Source: PDF Page 99**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 99 / 107 
 
 
 
 
 
AL-SAT noktaları grafiğin altında –yeşil-kırmızı hücreler şeklinde- gösterilebileceği gibi, grafik 
üzerinde AL-SAT kutucukları veya muhtelif şekillerle de gösterilebilir.  
 
6.3. Sistemin Kapatılması / Düzenlenmesi: 
Expert Advisor’u çalıştırdığınızda KHN menüleri altına buna bağlı 3 adet ek menü gelir.  
 
 
 
 Expert Advisor’u Düzenle: Expert Advisor koşullarını yazdığınız pencere açılır. 
Dilerseniz parametrelerde değişiklik yapabilirsiniz.  
 Expert Advisor’u Kaldır: Expert Advisor’ın alarm vermesini istemiyorsanız 
uygulamadan kaldırma işlemini bu menü ile yapabilirsiniz. 
 Gerçekleşen Expert Advisor Alarmları: Expert Advisor’ın geçmişte vermiş olduğu 
alarmları bu menü ile izleyebilirsiniz. 


---

---

**📄 Source: PDF Page 100**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 100 / 107 
 
 
7. Formasyonları Bul 
Formasyonları Bul menüsü ile karşınıza formasyon ayarları penceresi açılır. Buradan 
seçimlerinizi yaptıktan sonra ‘Tamam’ butonuna tıklarsanız, sistem otomatik olarak verileri 
tarayacak ve bu sembol için oluşmuş olan formasyonları grafik üzerinde gösterecektir.  
 
 
Yukarıda formasyon gösterimine bir örnek görmektesiniz.  
 
Formasyon bulduğunuzda, menü seçenekleri altına Formasyonları Kaldır seçeneği gelir. 
Bu seçenek ile grafik üzerinden formasyonu kaldırabilirsiniz. 
 
İpucu: Formasyonlarla ilgili daha detaylı bir uygulama, Matriks başlığı menülerinden Analizler 
menüsü altında ‘Formasyon Analizi’ seçeneği ile yer almaktadır. Daha ayrıntılı bilgi için 
Bakınız: Formasyon Analiz Modülü dokümanı. 
http://217.118.24.4/documents/MATRIKS_FORMASYON_ANALIZ_MODULU.pdf 
 
 
 
8. Ek Bilgiler 
  
8.1 Bar Sayısı  
Geçmişe yönelik analizler için hafızada saklanan bar sayısının sınırları vardır. 
Uygulamalarınızda buna dikkat ediniz.  
Ana periyotlarda var olan maksimum bar sayısı 8.000 dir. Günlük, 60 dk.’lık ve 5 dk.’lık 
periyotlar ana periyotlardır. Diğer periyotların datası bunlardan türetildiği için geriye dönük 
olarak ulaşılabilecek bar sayısı daha düşük olacaktır.  Mesela 15 dk.’lık bar sayısı 5 dk.’lık 
periyodun bar sayısının 1/3 ü kadar olacaktır.  
Bununla beraber, programımızda 1 dk.’lık periyot için daha fazla veri saklama olanağınız 
vardır. Matriks başlığı altındaki Ayarlar menüsünün alt menülerinden ‘Bir Dakikalık Grafik 
Ayarları’ menüsünü seçerseniz aşağıda göreceğiniz ‘Tarihsel Veri Ayarları’ penceresi 
açılacaktır.

---

---

**📄 Source: PDF Page 101**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 101 / 107 
 
 
 
 
Ön tanımlı rakam 30.000’dir. Seçeceğiniz semboller için, piyasalar için ya da Tüm Piyasa ve 
Semboller için 1 dakikalık verilerden 30.000 adete kadar saklayabilirsiniz. 
 
İpucu: Tüm sembolleri seçtiğiniz takdirde, çok fazla veri yüklemiş olacağınız için, sembolleri 
tek tek seçerek veri yüklemenizi öneririz. 
Ek Bilgi: Dışarıdan Excel verisi Matriks programı içine alınarak grafik oluşturulabilir. Bu işlev 
grafik üzerinde SVD butonu altında yer alan Sembol Builder uygulaması ile 
gerçekleştirilebilmektedir. Grafikler dokümanı altında ilgili başlıkta anlatılmıştır.  
 
8.2 İndikatör Çizgilerinin Taşınması:  
Grafik üzerine atamış olduğunuz indikatörleri, çizgisini tutarak pencerenin başka bir kısmına / 
bölmesine taşıyabilirsiniz. 
 
8.3 İndikatör Builder’da Grafik Üzerine Atarken Değiştirebileceğimiz Değişken Kullanmak: 
İndikatör oluştururken 2 şekilde değişken tanımlayabiliriz. 
İlkinden yukarıda da bahsettik. 
 
İndikatörde değişken tanımlarken ‘input’ komutu kullanırsak grafik üzerinde göster komutu 
ile bize değişkenleri gösterir ve dilersek o anda değişiklik yapmamıza olanak tanır.  
Bir örnek:  
aa:=Input("Kısa Periyot",100,500,150); 
Kanal(aa,0,y,1)

---

---

**📄 Source: PDF Page 102**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 102 / 107 
 
 
Kısa Periyot değişkene verilen isim / tanımlamadır. Hiç bir şey de yazmayabilirsiniz. Buraya 
yazdığınız tanım kendinize hatırlatma içindir. Sonucu değiştirmez. 
Parantez içindeki  1,100,10 rakamları ise, sırası ile  aa değişkeninin değeri için alt sınırı / üst 
sınırı ve varsayılanı gösterir. 
 
İndikatörü grafik üzerine atarken size sorar. Dilerseniz o esnada varsayılan (kullanılacak olan) 
değeri değiştirebilirsiniz. 
 
 
 
Varsayılanı kalıcı olarak değiştirmek isterseniz formül içinde yapmalısınız. 
aa:=Input("Kısa Periyot",100,500,200); şeklinde değiştirirseniz varsayılan değeri 200 yapmış 
olursunuz 
 Formülü şu şekilde başlatsaydınız: 
aa:= 150 
Bu sefer aa değişkenine tek  bir değer (150) vermiş olacaktınız. Bu durumda indikatörü grafik 
üzerine atarken size sormayacaktı. 
Bunda değişiklik yapmak isterseniz indikatör formülü içinden değiştirebilirsiniz.  
 
8.4 Ters Grafik: 
Grafik üzerinde yer alan indikatör seçeneklerinden bir tanesi Ters Grafik’tir. Bu seçim ile 
sembolün grafiğinin yatay eksen üzerindeki ayna görüntüsü elde edilir.  
Ters grafik formülü : 
-C şeklinde yazılır. 
Grafik için ters grafik indikatörünü uyguladığınızda da rakamların negatif değerlerle 
gösterildiğini görebilirsiniz. 
Aşağıdaki resimde, sembolün kendisi, ters indikatör seçimi ile görünümü ve indikatör builder 
içinde –C formülü ile elde edilen görünümler yer almaktadır.

---

---

**📄 Source: PDF Page 103**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 103 / 107 
 
 
 
 
Data’yı kullanan indikatörler için C yerine –C yazarsanız, ters grafik üzerine atayacağınız 
indikatörlerle aynı sonuçları alırsınız.  
 
8.5 Listede Olmayan Fonksiyonlar: 
 
Küsurat Silme / Tamsayıya Dönüştürme konuları ile ilgili fonksiyonlar: 
 
İnteger fonksiyonu 
Yazım şekli: int(data)  
Küsuratı yok sayar. Tam sayıyı alır.  
 
Fix fonksiyonu 
Yazım şekli aynı : fix(Data) 
Bu fonksiyon da virgülden sonraki sayıyı görmüyor. 
 
Yani integer fonksiyonu gibi çalışır.  
 
İnteger ve Fix fonksiyonları arasındaki fark negatif sayılarda ortaya çıkar: 
İnteger fonksiyonu negatif sayının küsuratını atarken bir alt tamsayıya yuvarlar. 
Fix fonksiyonu ise negatif sayının küsuratını atar tamsayı kalır. 
 
Örnekler: 
int(8.8) =8      fix(8.8) =8 
int(-8.8)= -9     fix(-8.8)= -9

---

---

**📄 Source: PDF Page 104**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 104 / 107 
 
 
Dikkat parantez içindeki rakam -8.8 değil de, -8.3 olsaydı da aynı sonuçlar gelecekti. 
 
Clng Fonksiyonu 
Yazım şekli : clng(data) 
 
Özelliği : 
Normal olarak buçuğun altını aşağıya, üstünü yukarıya yuvarlıyor. 
Yani : 
3.2 ise 3 olur 
3.6 ise 4 oluyor mesela.  
Buçuk olması durumunda ufak bir değişiklik var. 
Rakamın asıl kısmı tek ise yukarıya yuvarlar. 
Çift ise aşağıya (kendisine) yuvarlar. 
Yani : 3.5 ise 4 oluyor. ( 3 tek sayı olduğu için) 
4.5 ise gene 4 oluyor. ( 4 çift sayı olduğu için) 
  
* 
 
Prev (Previous) Fonksiyonu: 
 
Previous fonksiyonu, içinde bulunduğu formülün bir önceki değerinin kullanılarak hesaplama 
yapılmasını sağlar. 
 
Bir örnek: 
atrper3:=18; 
atrfact3:=1; 
loss:=atrfact3*ATR(atrper3); 
if(c>PREV,c-loss,c+loss) 
 
Burada yapılan şudur: 
Bu barın kapanışı bir önceki barda bu formül ile hesaplanmış olan değerden büyük ise şunu 
yap, küçük ise bunu yap. 
Bu uygulama REF (Referans Fonksiyonu) ile yapılamaz. Çünkü REF fonksiyonu herhangi bir 
diğer dataya / hesaplamaya atıfta bulunabilir. Formülün bütününü formül içinde REF 
fonksiyonu içine alamazsınız.  
 
 
8.6 Oto Optimizasyon: 
Otomatik emir gönderimi lisansı olan kullanıcılar için, Otomatik Optimizasyon seçeneği 
eklenmiştir.  
Belli kurallara bağlı olarak, sistemin tekrar çalışmasını ve gelecek sonuçlara göre 
parametreleri değiştirmesini sağlayabilirsiniz.

---

---

**📄 Source: PDF Page 105**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 105 / 107 
 
 
 
 
Öncelikle OTO OPT seçimini yaparak uygulamanın devreye girecek olmasını sağlamalısınız.  
 
Alttaki ilk seçenekler grubu ile; 
 
Belli bir tarihte optimizasyonun tekrar yapılmasını seçebilirsiniz. 
X gün sonra tekrar yapılmasını seçebilirsiniz. 
X sayıda işlemde peş peşe zarar oluşması halinde, tekrar optimizasyon yapılmasını 
seçebilirsiniz.  
Toplam Kar / İşlem sayısı tanımlayacağınız rakamın altına düşerse, tekrar optimizasyon 
yapılmasını seçebilirsiniz.  
Kar Eden / Zarar Eden işlem sayısı oranı tanımlayacağınız rakamın altına düşerse, tekrar 
optimizasyon yapılmasını seçebilirsiniz.  
 
Bu seçeneklerden 1 den fazlasını seçerek, her hangi birisinin gerçekleşmesi halinde, tekrar 
optimizasyon yapılmasını sağlayabilirsiniz. 
 
Not: Her durumda otomatik optimizasyon, günde maksimum 1 sefer yapılır.

---

---

**📄 Source: PDF Page 106**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 106 / 107 
 
 
 
Optimizasyon için belli bir saatin beklenmesini sağlayabilirsiniz. 
Örnek olarak: Optimizasyon yapılması koşulu gün içinde oluşmuş olabilir. Siz, eğer gün 
sonunun beklenmesini istiyorsanız, bu seçeneği kullanabilirsiniz.  
Ve, gün sonunu beklerken, dilerseniz sistemin çalışmasını durdurabilirsiniz. Yani, sistem eski 
parametrelerle çalışmayı durdursun / emir üretmesin diyebilirsiniz.  
 
 
Optimizasyonu başlatmadan sor, diyebilirsiniz. 
Ekranı izliyor olabilirsiniz. Bununla beraber sistemin gidişatında, yukarıda bahsedilen 
durumlardan birisi olduğu takdirde, otomatik kontrol edilsin ve size haber verilsin isterseniz, 
bu seçimi yapabilirsiniz.  
Otomatik optimizasyon koşulu oluştuğu takdirde, bir uyarı penceresi açılır. 
Tamam derseniz optimizasyon yapılır. 
 
Optimizasyon sırasında eski parametreli sistemi durdur 
Seçimi ile, optimizasyon yapılırken sistemi durdurabilirsiniz.  
 
Yeni Parametre Seçimi:  
 
 
Optimizasyon yapıldıktan sonra, gelen sonuçlardan hangisinin seçileceğine buradan karar 
verirsiniz.  
Yukarıda görülen 3 seçimden birisini yapabilirsiniz.  
Veya hemen altında yer alan kısımdan 
 
 
Şu sıradaki sonucu seç diyebilirsiniz.  
 
Uyumlaştırma:  
Sistemin pozisyonunu yeni duruma nasıl adapte edeceğinizi buradan belirleyebilirsiniz.  
 
 
 
ALIGN: Yeni optimizasyon sonucu ne ise, pozisyonu ona göre değiştirir.  
FLAT: Pozisyonu sıfırlar ve yeni başlangıçta, sinyal gelmesini bekler.

---

---

**📄 Source: PDF Page 107**

Teknik Analiz Modülleri. Kahin (KHN) Menüleri 
Matriks Bilgi Dağıtım Hizmetleri A.Ş. 
 
Sayfa 107 / 107 
 
 
AS IS: Pozisyona dokunmaz. Yeni optimizasyon değerleri ile karşıt sinyal gelene kadar sistem 
işlem üretmez.  
 
Mesela:  
Önceki parametrelere göre sistem AL durumunda ise.  
Ve yeni parametreler ile sistemin SAT / AÇIĞA SAT durumunda olması gerekiyor ise. 
 
Yukarıda yapacağınız seçimlere göre, 
ALIGN seçimi ile:  
Pozisyon SAT / AÇIĞA SAT haline dönüştürülüp devam edebilir. 
FLAT seçimi ile:  
Pozisyon sıfırlanır. Sistem yeni başlamış gibi ilerler. İlk AL veya Açığa Sat sinyali ile pozisyon 
açılır.  
AS IS seçimi ile:  
Pozisyon olduğu gibi bırakılır. Sistem yeni parametreler ile çalışmaya devam eder.  
Dikkat: Bu seçim sakınca içerir. 
Yeni parametrelerle sistem SAT durumunda. Halbuki sizin pozisyonunuz AL.  
Sistem yeniden SAT sinyali verme durumuna gelene kadar sinyal üretmeyecektir.  
AL koşulu oluşsa bile, uygulama zaten AL durumunda olduğu için AL sinyali üretilmez.  
Ancak bir AL durumu oluşup, sonra tekrar SAT koşulu oluşur ise emir gönderilecektir.  
Bir başka ifade ile, sistermin SAT durumunda olması fiyatın düşmesini işaret eder. Ve fiyat 
düşmeye devam ederse, zararınız artacaktır.  
Bu seçimi tercih etmemenizi öneririz.  
 
 
Hayırlı Trade’ler dileklerimizle.

---

