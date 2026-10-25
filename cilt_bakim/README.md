# Cilt Bakımı Analizatörü

## Amaç

Bu uygulama, seçilen cilt bakım içeriklerini basitçe karşılaştırır ve olası tahriş eşleşmelerini bir açılır pencerede gösterir.

## Özellikler

- AHA, BHA ve PHA gruplarından yaygın asitleri içerir.
- Salisilik asidi, diğer BHA/LHA seçeneklerinden ayrı gösterir.
- Arbutin, alfa arbutin, retinoid, niasinamid ve benzoyl peroksit gibi aktifler seçilebilir.
- Analiz sonucunu açılır pencerede gösterir.

## Nasıl çalışır?

1. Kullanılan içerikler listeden işaretlenir.
2. **Analiz et** düğmesine basılır.
3. Uygulama retinoid veya benzoyl peroksit ile eksfoliyan asitlerin aynı seçimde olup olmadığını kontrol eder.
4. Birden fazla eksfoliyan asit seçilmişse ek bir hassasiyet uyarısı gösterir.



## Çalıştırma

Python 3 yüklü olmalıdır. Dosyanın bulunduğu klasörde terminal açıp şu komutu çalıştırınız:

```bash
python cilt_bakimi_analizoru.py