from rubpy import Client
import asyncio
from datetime import datetime
import pytz

# تنظیمات اولیه
SESSION_NAME = "shayan_session"  # نام فایل نشست
PHONE_NUMBER = "989022628772"    # شماره شما با کد کشور (مثال: 989123456789)
FIXED_NAME = "Shayan"             # اسم ثابت شما

async def main():
    # اتصال به روبیکا
    client = Client(SESSION_NAME)
    await client.start(phone_number=PHONE_NUMBER)
    
    print("✅ برنامه با موفقیت شروع به کار کرد")
    print(f"👤 نام ثابت: {FIXED_NAME}")
    print("🔄 در حال تغییر خودکار نام هر دقیقه...")
    
    while True:
        try:
            # گرفتن ساعت ایران
            iran_tz = pytz.timezone('Asia/Tehran')
            current_time = datetime.now(iran_tz)
            
            # فرمت ساعت (مثال: 14:35)
            time_str = current_time.strftime("%H:%M")
            
            # ساخت نام جدید: Shayan | 14:35
            new_name = f"{FIXED_NAME} | {time_str}"
            
            # تغییر نام
            await client.update_profile(first_name=new_name)
            
            # نمایش نتیجه
            print(f"[{time_str}] ✅ نام تغییر کرد: {new_name}")
            
            # یک دقیقه صبر کن
            await asyncio.sleep(60)
            
        except Exception as e:
            print(f"❌ خطا: {e}")
            await asyncio.sleep(60)  # در صورت خطا هم یک دقیقه صبر کن

if __name__ == "__main__":
    asyncio.run(main())
