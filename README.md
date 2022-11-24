# Scraping comments on Trendyol, Hespiburada and Amazon TR
> Not: Amazon TR'de sadece Türkiye lokasyonundan yapılan Türkçe yorumlar alınmaktadır.

Çalışmanın amacı ileride kullanılamak üzere direkt birbirinden farklı kullanıcılar tarafından üretilmiş ürün yorumlarını web ortamından kazıyarak depolamaktır. Bu aşamada Türkiye'de popüler olan 3 büyük online alışveriş sitesiyle sorunsuz çalışmaktadır.

## Özellikler

- Web ortamından veri çekmek için Selenium kullanılmıştır.
- PyQt5 ile oluşturulan arayüz sayesinde kullanım basitleştirilmiştir.
- Toparlanan veriler .csv .txt .xlsx olamak üzere 3 ayrı formatta kaydedilecek şekilde oluşturulmuştur.
  
## Kullanmadan Önce
> Kazımada Google Chrome'un otomatik kullanılabilmesi için driver kurulumu gerekmektedir. Bağlantıdan [Chrome Driver](https://chromedriver.storage.googleapis.com/index.html?path=107.0.5304.62/ "Chrome Driver") indirerek bulunduğu konumu Windows'a Path olarak gösterilmesi gerekmektedir. ([bkz](https://www.youtube.com/watch?v=mHtlBq5cP2Y "bkz").)

## Script Hakkında
Kullanmak için terminale aşağıdaki komutu girmeniz yeterlidir.  
  
`python commentScraping.py`
  
Açılan kullanıcı arayüzüne bağlantıyı girerek `Start` a tıklamanız yeterlidir.  Ardından arkanıza yaslanarak verilerin bir bir size gelmesini beklemelisiniz. Some Data alanında head veriler göründükten sonra seçtiğiniz formatta verilerinizi kaydedebilirsiniz.

### Bazı Görseller
![Kullanıcı Arayüzü](https://github.com/ismaildrcn/storeScraping/blob/master/commentScrapingPanel.png)
