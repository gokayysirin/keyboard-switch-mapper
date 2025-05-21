# Keyboard Switch Mapper

## Selam Klavye Tutkunları! 👋

Hepinize merhaba! Ben Gökay ve klavye dünyasına olan tutkumla sizlere Keyboard Switch Mapper uygulamasını sunmaktan heyecan duyuyorum.

## Bu Uygulama Nasıl Doğdu?

Geçen ay yeni bir hot-swap mekanik klavye aldım ve hayatımda ilk kez switch değiştirme özgürlüğünü yaşadım. Önce heyecanla taktığım Gateron Blue'lar güzel gidiyordu, sonra "Acaba Red nasıl hissettiriyor?" diye düşündüm ve birkaç tuşa kırmızı takayım dedim. Derken Brown'lar geldi, ardından Cherry MX'ler... 

Sonuç mu? **Tam bir switch karmaşası!**

Bir hafta sonra klavyeye baktığımda artık hangi tuşta hangi switch olduğunu tamamen unutmuştum. ESC tuşunda Gateron Blue mu vardı yoksa Cherry MX Red mi? Space'te hangisi vardı? WASD tuşlarına ne takmıştım? Hiçbir fikrim yoktu!

İşte tam bu noktada, bir yazılımcı refleksiyle düşündüm: "Bu sorunu çözmek için neden kendi uygulamama yapmıyorum?" Ve böylece Keyboard Switch Mapper doğdu.

## Ne İşe Yarar?

Keyboard Switch Mapper, hot-swap klavyenizde hangi tuşa hangi switch'i taktığınızı kaydetmenize ve görsel olarak takip etmenize olanak sağlar. Basit, kullanışlı ve tam olarak ihtiyacım olan şeydi!

### Özellikler:

- **Görsel Klavye Haritası**: %60 layout Türkçe Q klavye düzeninde switchlerinizi görsel olarak haritalamanızı sağlar
- **Özelleştirilebilir Switch Türleri**: Kendi switch türlerinizi ekleyebilir ve renk kodlarıyla eşleştirebilirsiniz
- **Kolay Atama**: Önce switch türünü seçip sonra klavye üzerindeki tuşa tıklayarak hızlıca atama yapabilirsiniz
- **Kalıcı Kayıt**: Tüm switch haritanız JSON formatında kaydedilir, böylece uygulama yeniden başlatıldığında verileriniz korunur

## Nasıl Kullanılır?

1. **Switch Türleri**: Sol panelde varsayılan switch türlerini göreceksiniz. Buradan kullanacağınız switch'i seçin
2. **Yeni Switch Ekle**: Kendi switch'lerinizi eklemek için isim girin, renk seçin ve "Ekle" butonuna tıklayın
3. **Tuşlara Atama**: Önce sol panelden bir switch türü seçin, ardından klavye görselinde atamak istediğiniz tuşa tıklayın
4. **Kaydetme**: İşiniz bittiğinde "Haritayı Kaydet" butonuna tıklayarak değişikliklerinizi kaydedin

## Geliştirme Notları

Bu uygulama Python ve Tkinter kullanılarak geliştirilmiştir. Kaynak koduna erişmek veya katkıda bulunmak isterseniz [GitHub repo](https://github.com/gokaysirin/keyboard-switch-mapper)'sunu ziyaret edebilirsiniz.

Eğer Python bilginiz varsa ve kodu kendiniz derlemek isterseniz:

```bash
# Gerekli kütüphaneleri yükleyin
pip install -r requirements.txt

# Uygulamayı çalıştırın
python keyboard_switch_mapper.py

# EXE'ye derlemek için
pyinstaller --onefile --windowed --name "Keyboard Switch Mapper" keyboard_switch_mapper.py
```

## İletişim ve Geri Bildirim

Bu basit uygulama klavye yolculuğumda bana oldukça yardımcı oldu. Umarım sizin de işinize yarar!

Herhangi bir öneri, geri bildirim veya sorunuz olursa, lütfen [GitHub Issues](https://github.com/gokaysirin/keyboard-switch-mapper/issues) üzerinden iletişime geçin.

---

Tuşlarınız her zaman doğru switch'te olsun! ⌨️

*Geliştirici: Gökay Şirin*
