---
name: matriks-system-tester
description: Matriks DATA Terminali - System Tester, İndikatör Builder, Explorer ve Expert Advisor modüllerinin kullanımı ile örnek stratejiler ve formüller
---

# Matriks DATA - System Tester ve Teknik Analiz Modülleri

Matriks Bilgi Dağıtım Hizmetleri A.Ş. terminal programı için System Tester, İndikatör Builder ve diğer teknik analiz modüllerinin kullanım kılavuzu.

## Ne Zaman Kullanılır

Bu skill'i şu durumlarda kullan:
- Matriks DATA'da sistematik ticaret stratejileri oluşturmak
- Geri test (backtesting) yapmak için System Tester kullanmak
- Özel indikatörler oluşturmak için İndikatör Builder kullanmak
- Explorer ile piyasa taraması yapmak
- Expert Advisor ile alarm sistemleri kurmak

## Temel Modüller

### 1. System Tester
Gerçekleştirdiğiniz stratejileri geçmiş veriler üzerinde test etmenizi sağlar.

**Temel özellikler:**
- Strateji AL/SAT sinyalleri tanımlama
- Tarihsel veri üzerinde geri test
- Performans metrikleri (kar/zarar, drawdown, vs.)
- Sembol seçimi ve periyot ayarları

### 2. İndikatör Builder
Kendi özel göstergelerinizi oluşturabileceğiniz modül.

### 3. Explorer
Belirli koşulları sağlayan sembolleri tarama.

### 4. Expert Advisor
Tanımladığınız koşullar gerçekleştiğinde alarm tetikleme.

## Örnek Stratejiler

### AlphaTrend Stratejisi

**AL Koşulu:**
```matriks
coeff:=OPT1;
AP:=OPT2;
momentum:=1;
mom:=if(momentum=1,MFI(AP),RSI(AP));
upT:=L-ATR(AP)*coeff;
downT:=H+ATR(AP)*coeff;
AlphaTrend:=If(mom>=50,If(upT<PREV,PREV,upT),If(downT>PREV,PREV,downT));
cross(AlphaTrend,ref(AlphaTrend,-2))
```

**SAT Koşulu:**
```matriks
coeff:=OPT1;
AP:=OPT2;
momentum:=1;
mom:=if(momentum=1,MFI(AP),RSI(AP));
upT:=L-ATR(AP)*coeff;
downT:=H+ATR(AP)*coeff;
AlphaTrend:=If(mom>=50,If(upT<PREV,PREV,upT),If(downT>PREV,PREV,downT));
cross(ref(AlphaTrend,-2),AlphaTrend)
```

**Parametreler:** OPT1=1.5-3.0, OPT2=14

### PHL1 YİGİT KAYNAK Stratejisi

Günlük bazda yüksek-düşük takibi yapan pivot benzeri bir strateji.

**AL Koşulu:**
```matriks
YIGIT:=dayofmonth()><ref(dayofmonth(),-1);
ADAM:=valuewhen(1,YIGIT,ref(c,-1));
TX:=valuewhen(1,YIGIT,ref(highestsince(1,YIGIT,h),-1));
RX:=valuewhen(1,YIGIT,ref(lowestsince(1,YIGIT,l),-1));
YGT:=(ADAM+RX+TX)/3;
DI:=2*YGT-RX;
DE:=2*YGT-TX;
Mov(C,1,s)>DI
```

**SAT Koşulu:**
```matriks
YIGIT:=dayofmonth()><ref(dayofmonth(),-1);
ADAM:=valuewhen(1,YIGIT,ref(c,-1));
TX:=valuewhen(1,YIGIT,ref(highestsince(1,YIGIT,h),-1));
RX:=valuewhen(1,YIGIT,ref(lowestsince(1,YIGIT,l),-1));
YGT:=(ADAM+RX+TX)/3;
DI:=2*YGT-RX;
DE:=2*YGT-TX;
Mov(C,1,s)<DE
```

**Mantık:**
- YIGIT: Gün değişimini tespit eder
- ADAM: Önceki günün kapanışı
- TX: Günün en yükseği
- RX: Günün en düşüğü
- YGT: Ortalama (pivot) noktası
- DI: Üst seviye (direnç)
- DE: Alt seviye (destek)

**Periyot:** Günlük ve altı

### TOTT Stratejisi
OTT indikatörü ile değişken hareketli ortalamanın kesişimi.

**AL Koşulu:**
```matriks
Cross(MOV(C,opt1,VAR),OTT(C,opt1,opt2)*(1+opt3))
```

**SAT Koşulu:**
```matriks
Cross(OTT(C,opt1,opt2)*(1-opt3),MOV(C,opt1,VAR))
```

**Parametreler:** OPT1=periyot, OPT2=OTT periyot, OPT3=yüzde

### RSOTTO Stratejisi
RSI ile OTT'yi birleştiren strateji.

**AL Koşulu:**
```matriks
X1:=OPT1;
X2:=OPT2;
X3:=OPT3;
CROSS(MOV(RSI(C,X1),X2,VAR)+1000,OTT(MOV(RSI(C,X1),X2,VAR)+1000,2,X3))
```

**SAT Koşulu:**
```matriks
X1:=OPT1;
X2:=OPT2;
X3:=OPT3;
CROSS(OTT(MOV(RSI(C,X1),X2,VAR)+1000,2,X3),MOV(RSI(C,X1),X2,VAR)+1000)
```

**Parametreler:** OPT1=RSI periyot, OPT2=MA periyot, OPT3=OTT %

### VFHMOST Stratejisi
VHF ve MOST indikatörlerinin birleşimi.

**AL Koşulu:**
```matriks
sum(VHF(c,28)>ref(VHF(c,28),-1),3)=-3 AND mov(c,opt1,e)>most(c,opt1,opt2)
```

**SAT Koşulu:**
```matriks
sum(VHF(c,28)>ref(VHF(c,28),-1),3)=-3 AND mov(c,opt1,e)<most(c,opt1,opt2)
```

**Parametreler:** OPT1=MA periyot, OPT2=MOST %

## Örnek İndikatör Formülleri

### 1. Bollinger Band Pozisyonu
```matriks
((C-BBandBot(C,20,S,2))/(BBandTop(C,20,S,2)-BBandBot(C,20,S,2)))*100
```

### 2. Hareketli Ortalama Farkı (Golden Cross)
```matriks
HOPER:=Input("period",1,100,7);
HOPER1:=Input("period1",1,100,20);
a1:=MOV(c,HOPER,E);
a2:=MOV(c,HOPER1,E);
a1-a2
```

### 3. ATR Bazlı Kanal
```matriks
VL:=Input("ATR Period",1,50,10);
HOPER:=Input("period",1,100,7);
a1:=Mov(H,HOPER,E);
a2:=a1-(1.2*atr(VL));
a3:=a1+(1.2*atr(VL));
b1:=If(a1<PREV,a2,if(a2>PREV,a2,PREV));
b2:=If(a1>PREV,a3,if(a3<PREV,a3,PREV));
k1:=Cross(a1,Ref(b2,-1));
k2:=Cross(Ref(b1,-1),a1);
s1:=BarsSince(k1) < BarsSince(k2);
s2:=If(s1=-1,b1,b2);
a1;s2
```

### 4. AET (Adaptive Exponential Trend)
```matriks
AET:=(REF(HHV(H,20),-1)+REF(LLV(L,20),-1))/2;
a2:=AET-Mov(ATR(10),13,E);
a3:=AET+Mov(ATR(10),13,E);
b1:=If(AET<PREV,a2,if(a2>PREV,a2,PREV));
b2:=If(AET>PREV,a3,if(a3<PREV,a3,PREV));
k1:=Cross(AET,Ref(b2,-1));
k2:=Cross(Ref(b1,-1),AET);
s1:=BarsSince(k1) < BarsSince(k2);
s2:=If(s1=-1,b1,b2);
AET;s2
```

### 5. MACD Bollinger Bands
```matriks
a:=MACD();
BBandBot(a,10,E,2);
BBand(a,10,E,2);
BBandTop(a,10,E,2);
a
```

### 6. DI Hareketli Ortalama
```matriks
a:=DI();
a1:=MOV(a,20,W);
a2:=MOV(a1,20,W);
a1;a2;0
```

### 7. İchimoku Benzeri
```matriks
x:=((((H+L+C+O)/2)-L)+(((H+L+C+O)/2)-H))/2;
A:=MOV(X,5,ZL);
MOV(A,20,ZL);x
```

### 8. Günlük Destek-Direnç
```matriks
DSK:=ValueWhen(1,HOUR()<Ref(HOUR(),-1),Ref(LowestSince(1,HOUR()<Ref(HOUR(),-1),LLV(L,21)),-1));
YKSK:=ValueWhen(1,HOUR()<Ref(HOUR(),-1),Ref(HighestSince(1,HOUR()<Ref(HOUR(),-1),HHV(H,21)),-1));
(DSK+YKSK)/2
```

### 9. Volume Weighted MA
```matriks
Period:=5;
A:=(If(MOV(c,Period,E)>Ref(MOV(c,Period,E),-1),1,If(MOV(c,Period,E)<Ref(MOV(c,Period,E),-1),-1,0))*MOV(v,Period,E))+PREV;
A;MOV(A,Period,E)
```

### 10. SuperTrend Benzeri
```matriks
Factor:=Input("Factor",1,10,1);
Pd:=Input("ATR Periods",1,100,10);
Pd1:=Input("Td Periods",1,100,13);
C1:=MOV(W,10,E);
Up:=C1+(Factor*ATR(Pd));
Dn:=C1-(Factor*ATR(Pd));
Td:=If(Cross(C1,LLV(Up,Pd1)),1,If(Cross(HHV(Dn,Pd1),C1),-1,PREV));
Dnx:=If(Dn=HighestSince(1,Cross(Td,0),Dn),Dn,PREV);
Upx:=If(Up=LowestSince(1,Cross(0,Td),Up),Up,PREV);
If(Td=1,Dnx,Upx);Upx
```

## Kaynaklar

- **Eğitim Dokümanı**: `references/matriks-dokumani.md` (107 sayfa)
- **İndikatör Örnekleri**: `references/indikator-calismalari.md` (10 örnek)
- **AlphaTrend**: https://algokutuphanesi.com/Sistem/Detay/Matriks/AlphaTrend-Strategy
- **PHL1 Yığit Kaynak**: https://www.algokutuphanesi.com/Sistem/Detay/Matriks/PHL1-Y%C4%B0G%C4%B0T-KAYNAK
- **Tüm Stratejiler**: https://www.algokutuphanesi.com/Sistem?application=Matriks&category=System%20Tester
- **Formül Örnekleri**: https://www.fiyatneder.com/?pnum=58&pt=MATR%C4%B0KS+FORM%C3%9CLLER%C4%B0
