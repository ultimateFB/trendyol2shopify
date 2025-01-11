import pandas as pd

# Trendyol Excel dosyasını oku
input_file = "ty.xlsx"  # Trendyol Excel dosya adı
output_file = "shopify_import.csv"  # Shopify için oluşturulacak CSV dosyası

# Excel dosyasını oku
df = pd.read_excel(input_file)

# Shopify formatına uygun yeni DataFrame oluştur
shopify_df = pd.DataFrame()

# Alan eşleştirmeleri
shopify_df["Handle"] = df["Tedarikçi Stok Kodu"]
shopify_df["Title"] = df["Ürün Adı"]
shopify_df["Body (HTML)"] = df["Ürün Açıklaması"]
shopify_df["Vendor"] = df["Marka"]
shopify_df["Product Category"] = ""
shopify_df["Type"] = ""
shopify_df["Tags"] = ""
shopify_df["Published"] = True
shopify_df["Option1 Name"] = ""
shopify_df["Option1 Value"] = ""
shopify_df["Option2 Name"] = ""
shopify_df["Option2 Value"] = ""
shopify_df["Option3 Name"] = ""
shopify_df["Option3 Value"] = ""
shopify_df["Variant SKU"] = df["Tedarikçi Stok Kodu"]
shopify_df["Variant Grams"] = ""
shopify_df["Variant Inventory Tracker"] = "shopify"
shopify_df["Variant Inventory Qty"] = df["Ürün Stok Adedi"]
shopify_df["Variant Inventory Policy"] = "deny"
shopify_df["Variant Fulfillment Service"] = "manual"
shopify_df["Variant Price"] = df["Trendyol'da Satılacak Fiyat (KDV Dahil)"]
shopify_df["Variant Compare At Price"] = ""
shopify_df["Variant Requires Shipping"] = True
shopify_df["Variant Taxable"] = True
shopify_df["Variant Barcode"] = df["Barkod"].astype(str)
shopify_df["Image Src"] = df["Görsel 1"]
shopify_df["Image Position"] = 1  # İlk görsel
shopify_df["Image Alt Text"] = ""
shopify_df["Gift Card"] = False
shopify_df["SEO Title"] = df["Ürün Adı"]
shopify_df["SEO Description"] = df["Ürün Açıklaması"]
shopify_df["Google Shopping / Google Product Category"] = ""
shopify_df["Google Shopping / Gender"] = ""
shopify_df["Google Shopping / Age Group"] = ""
shopify_df["Google Shopping / MPN"] = ""
shopify_df["Google Shopping / AdWords Grouping"] = ""
shopify_df["Google Shopping / AdWords Labels"] = ""
shopify_df["Google Shopping / Condition"] = "New"
shopify_df["Google Shopping / Custom Product"] = ""
shopify_df["Google Shopping / Custom Label 0"] = ""
shopify_df["Google Shopping / Custom Label 1"] = ""
shopify_df["Google Shopping / Custom Label 2"] = ""
shopify_df["Google Shopping / Custom Label 3"] = ""
shopify_df["Google Shopping / Custom Label 4"] = ""
shopify_df["Variant Image"] = ""
shopify_df["Variant Weight Unit"] = "kg"
shopify_df["Variant Tax Code"] = ""
shopify_df["Cost per item"] = ""
shopify_df["Price / International"] = ""
shopify_df["Compare At Price / International"] = ""
shopify_df["Status"] = "active"

# Resim sütunlarını işleme
image_columns = ["Görsel 2", "Görsel 3", "Görsel 4", "Görsel 5", "Görsel 6", "Görsel 7", "Görsel 8"]
extra_images = []

for index, row in df.iterrows():
    for i, col in enumerate(image_columns):
        if pd.notna(row[col]):  # Eğer görsel URL boş değilse
            extra_images.append({
                "Handle": row["Tedarikçi Stok Kodu"],
                "Image Src": row[col],
                "Image Position": i + 2  # Resim sıralaması 2'den başlar
            })

# Shopify için ekstra resimler
images_df = pd.DataFrame(extra_images)

# Ürünler ve resimleri birleştir
merged_df = pd.concat([shopify_df, images_df], ignore_index=True).sort_values(by=["Handle", "Image Position"])

# Shopify formatında CSV olarak kaydet
merged_df.to_csv(output_file, index=False, encoding="utf-8-sig", quoting=1)

print(f"Shopify formatındaki dosya '{output_file}' olarak kaydedildi.")
