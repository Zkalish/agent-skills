# indikator-calismalari

**Pages**: 1-12

---

**📄 Source: PDF Page 1**

Aşağıda paylaşılan teknik indikatörler tek başlarına bir anlam ifade etmezler.
Diğer indikatörler ile teyitli olarak strateji oluşturma için kullanılması daha sağlıklıdır.
Zaten tüm indikatörler fiyattan gelen veriler ile hesaplanır. Geleceği göstermezler. O an 
ne olup bittiğini gösterirler.
Tahmine dayalı yada repainte müsait olanları paylaşmamaya özen gösteriyorum.
İçlerinde işe yaramayan fakat yazım için örnek teşkil edebilecek nitelikte olanlar olduğu 
gibi çok güze trend takibi sağlayanlarda vardır.
İçlerinde birebir bana ait olanlar olduğu gibi sosyal medyadan, forumlardan herkese açık
olarak paylaşılmış olanlarda vardır.
Formüllerin yanında grafik görüntülerini de koydum ki nasıl hareket ettiklerini görebilesiniz.
Her paylaşımı on tane ile sınırlı tutmaya çalıştım ki boğulmayın.
Formülleri bölüp parçalayıp, ne nereden nasıl gelmiş, ne yapmış anlamaya çalışırsanız 
daha sağlıklı olur.

---

---

**📄 Source: PDF Page 2**

((C-BBandBot(C,20,s ,2))/(BBandTop(C,20,s ,2)-BBandBot(C,20,s ,2)))*100;0;50;100
www.fiyatneder.com
fiyatneder@gmail.com

---

---

**📄 Source: PDF Page 3**

fiyatneder@gmail.com
HOPER:=Input("period",1,100,7);
HOPER1:=Input("period1",1,100,20);
a1:=MOV(c,HOPER,E );
a2:=MOV(c,HOPER1,E );a1-a2;0
www.fiyatneder.com

---

---

**📄 Source: PDF Page 4**

VL:=Input("ATR Period",1,50,10); 
HOPER:=Input("period",1,100,7);
a1:=Mov(H,HOPER,E); a2:=a1-(1.2*atr(VL)); 
a3:=a1+(1.2*atr(VL));
b1:=If(a1<PREV,a2,if(a2>PREV,a2,PREV)); 
b2:=If(a1>PREV,a3,if(a3<PREV,a3,PREV));
k1:=Cross(a1,Ref(b2,-1)); k2:=Cross(Ref(b1,-
1),a1);
s1:=BarsSince(k1) < BarsSince(k2);
s2:=If(s1=-
1,b1,b2);a4:=a1+2*(atr(VL));a5:=a1-
2*atr(VL);
a1;s2{;a4;a5}
fiyatneder@gmail.com
www.fiyatneder.com

---

---

**📄 Source: PDF Page 5**

www.fiyatneder.com
fiyatneder@gmail.com
AET:=(REF(HHV(H,20),-1)+REF(LLV(L,20),-
1))/2; a2:=AET-Mov(ATR(10) ,13,e) ; 
a3:=AET+Mov(ATR(10) ,13,e) ;
b1:=If(AET<PREV,a2,if(a2>PREV,a2,PREV)); 
b2:=If(AET>PREV,a3,if(a3<PREV,a3,PREV));
k1:=Cross(AET,Ref(b2,-1)); 
k2:=Cross(Ref(b1,-1),AET);
s1:=BarsSince(k1) <BarsSince(k2);
s2:=If(s1=-1,b1,b2);
AET;s2

---

---

**📄 Source: PDF Page 6**

www.fiyatneder.com
fiyatneder@gmail.com
a:=MACD();
BBandBot(a,10,E,2);
BBand(a,10,E,2);
BBandTop(a,10,E,2);a

---

---

**📄 Source: PDF Page 7**

www.fiyatneder.com
fiyatneder@gmail.com
a:=DI();
a1:=MOV(a,20,W);
a2:=MOV(a1,20,W);
a1;a2;0

---

---

**📄 Source: PDF Page 8**

fiyatneder@gmail.com
www.fiyatneder.com
x:=((((h+l+c+o)/2)-L)+(((h+l+c+o)/2)-H))/2;
A:=MOV(X,5,ZL);
MOV(A,20,ZL);x

---

---

**📄 Source: PDF Page 9**

DSK:=ValueWhen(1,HOUR()<Ref(HOUR(),-1),Ref(LowestSince(1,HOUR()<Ref(HOUR(),-1),Llv(l,21)),-1));
YKSK:=ValueWhen(1,HOUR()<Ref(HOUR(),-1),Ref(HighestSince(1,HOUR()<Ref(HOUR(),-1),Hhv(h,21)),-1));
(DSK+YKSK)/2
fiyatneder@gmail.com
www.fiyatneder.com

---

---

**📄 Source: PDF Page 10**

Period:=5;
A:=( If( MOV(c,Period,E)> Ref( MOV(c,Period,E), -1), 1, If( MOV(c,Period,E)< Ref( MOV(c,Period,E), -1 ), -1, 0 ) ) * 
MOV(v,Period,E) ) + PREV;
A;MOV(A,Period,E)
fiyatneder@gmail.com
www.fiyatneder.com

---

---

**📄 Source: PDF Page 11**

Factor:=Input("Factor",1,10,1); 
Pd:=Input("ATR Periods",1,100,10); 
Pd1:=Input("Td Periods",1,100,13);   
C1:=mov(W,10,e);Up:=c1+(Factor*ATR(Pd)); Dn:=c1-(Factor*ATR(Pd));
Td:=If(Cross(C1,LLV(Up,pd1)),1,If(Cross(HHV(Dn,pd1),C1 ),-1,PREV)); 
Dnx:=If(Dn=HighestSince(1,Cross(Td,0),Dn),Dn,PREV) ; 
Upx:=If(Up=LowestSince(1,Cross(0,Td),Up),Up,PREV); If(Td=1,Dnx,Upx) ;Upx
fiyatneder@gmail.com
www.fiyatneder.com

---

---

**📄 Source: PDF Page 12**

fiyatneder@gmail.com
www.fiyatneder.com
“Burada
yer
alan
yatırım
bilgi,
yorum
ve
tavsiyeler
yatırım
danışmanlığı kapsamında değildir.
Yatırım danışmanlığı hizmeti; aracı kurumlar, portföy yönetim
şirketleri, mevduat kabul etmeyen bankalar ile müşteri arasında
imzalanacak
yatırım
danışmanlığı
sözleşmesi
çerçevesinde
sunulmaktadır.
Burada yer alan değerlendirmeler, yorum ve
kişisel görüşlere
dayanmaktadır. Bu görüşler mali durumunuz ile risk ve getiri
tercihlerinize uygun olmayabilir.
Bu nedenle, sadece burada yer alan bilgilere dayanılarak yatırım
kararı verilmesi beklentilerinize uygun sonuçlar doğurmayabilir.”
Paylaşılan indikatör, Explorer, system tester çalışmaları eğitim
amaçlıdır ve herhangi bir kazanç garantisi vermez.
Sadece algoritmik trade konusunda kendini geliştirmek isteyen
kişilerin
gelişimine
katkı
sağlamak
amacıyla
paylaşılmıştır.
Yayınlanan çalışmalar teknik analiz ve temel analiz kriterlerine göre
subjektif yorumlar içerir. Al-sat-tut-tutma-yanından geçme-öte dur-
beri dur tavsiyesi değildir.
24.03.2018

---

