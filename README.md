# **Trendyol to Shopify**
🚀 **Trendyol ürünlerinizi Shopify formatına dönüştürmenin kolay yolu!**

Bu araç, Trendyol satıcı panelinden indirilen Excel dosyanızı Shopify'ın içeri aktarabileceği **CSV formatına dönüştürür**. Basit ama çok etkili bir araçtır. 🛠️

---

## **🔧 Kurulum ve Kullanım**
### **1. Gerekli Kütüphaneleri Yükleyin**
Kodun çalışması için aşağıdaki kütüphaneleri yüklemeniz gerekiyor:
```bash
pip install pandas  
pip install openpyxl  
```
---

### **2. Trendyol Excel Dosyanızı Hazırlayın**
Trendyol'dan aldığınız ürün listesini uygulamanın kök dizinine **`ty.xlsx`** adıyla kaydedin.

---

### **3. Uygulamayı Çalıştırın**
Aşağıdaki komutla uygulamayı başlatın:
```bash
python app.py  
```
---

### **4. Shopify CSV Dosyasını Alın**
Uygulama, kök dizinde **`shopify_import.csv`** adlı bir dosya oluşturacaktır. Bu dosyayı Shopify panelinizde içeri aktarabilirsiniz.

---

## **📄 Çıktı Dosyası**
Shopify için oluşturulan CSV dosyası şu alanları içerir:
- **Handle**
- **Title**
- **Body (HTML)**
- **Vendor**
- **Variant SKU**
- **Variant Inventory Qty**
- **Variant Price**
- **Image Src** ve daha fazlası!

---

## **❓ Sıkça Sorulan Sorular**
### **Bu araç görselleri destekliyor mu?**
Evet! Trendyol ürün listenizdeki görseller **Image Src** alanına aktarılır.

### **Excel dosyasını başka bir adla kaydedebilir miyim?**
Hayır. Dosya adı mutlaka **`ty.xlsx`** olmalıdır. Ancak dilerseniz kodda `input_file` değişkenini düzenleyebilirsiniz.

### **Hata alırsam ne yapmalıyım?**
Destek için bize ulaşabilirsiniz:  
📧 **mehmetvarisli42@gmail.com**

---

## **📢 Destek ve Katkı**
Bu aracı geliştirmek veya önerilerde bulunmak isterseniz bana ulaşabilirsiniz. Araç, Trendyol'dan Shopify'a ürün taşımayı kolaylaştırmak için tasarlanmıştır. Her türlü geri bildirime açığım! 😊

---

### **👨‍💻 Destekleyenler**
**Mehmet Varışlı**  
📧 **mehmetvarisli42@gmail.com**  

---

💡 **Haydi, Trendyol ürünlerinizi Shopify'a taşımanın keyfini çıkarın!** 🎉
