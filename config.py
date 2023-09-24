import os
import logging

api_id = int(os.environ.get("API_ID", "28094601"))
api_hash = os.environ.get("API_HASH", "70756c6b7f3bf1d996ab7d157b270970")
bot_token = os.environ.get("BOT_TOKEN", "6608316190:AAHXFVhN3mp_KYW8cuzPSnaJWyn9jckvAtQ")
# =========================================================== #

db_url = os.environ.get("DB_URL", "mongodb+srv://Menfess:Malik10_@cluster0.0q7u10d.mongodb.net/?retryWrites=true&w=majority")
db_name = os.environ.get("DB_NAME", "Cluster0")
# =========================================================== #

channel_1 = int(os.environ.get("CHANNEL_1", "-1001933177780"))
channel_2 = int(os.environ.get("CHANNEL_2", "-1001940308177"))
channel_log = int(os.environ.get("CHANNEL_LOG", "-1001729142523"))
# =========================================================== #

id_admin = int(os.environ.get("ID_ADMIN", "5657257558"))
# =========================================================== #

batas_kirim = int(os.environ.get("BATAS_KIRIM", "10"))
batas_talent = int(os.environ.get("BATAS_TALENT", "10"))
batas_daddy_sugar = int(os.environ.get("BATAS_DADDY_SUGAR", "10"))
batas_moansgirl = int(os.environ.get("BATAS_MOANSGIRL", "10"))
batas_moansboy = int(os.environ.get("BATAS_MOANSBOY", "10"))
batas_gfrent = int(os.environ.get("BATAS_GFRENT", "10"))
batas_bfrent = int(os.environ.get("BATAS_BFRENT", "10"))
# =========================================================== #

biaya_kirim = int(os.environ.get("BIAYA_KIRIM", "10"))
biaya_talent = int(os.environ.get("BIAYA_TALENT", "80"))
biaya_daddy_sugar = int(os.environ.get("BIAYA_DADDY_SUGAR", "70"))
biaya_moansgirl = int(os.environ.get("BIAYA_MOANSGIRL", "60"))
biaya_moansboy = int(os.environ.get("BIAYA_MOANSBOY", "50"))
biaya_gfrent = int(os.environ.get("BIAYA_GFRENT", "40"))
biaya_bfrent = int(os.environ.get("BIAYA_BFRENT", "30"))
# =========================================================== #

hastag = os.environ.get("HASTAG", "#Girl #Boy #Ask #Find #Spill #Story").replace(" ", "|").lower()
# =========================================================== #

pesan_join = os.environ.get("PESAN_JOIN", "Tidak dapat diakses harap join terlebih dahulu, dan wajib gunakan hastag #boy ataw #girl untuk mengirim pesan")
start_msg = os.environ.get("START_MSG", "Hai {fullname} 🌱\n\nIni adalah bot mutualan instagram, anda bisa mengirim pesan berupa ajakan mutualan instagram dengan mengirim link akun ig kalian pada bot, semua pesan yang kamu kirim akan masuk ke channel secara anonymous, \n\nWajib Gunakan Hastag #boy ataw #girl untuk mengirim menfess. \n\nKetik /help info")

gagalkirim_msg = os.environ.get("GAGAL_KIRIM", """
{mention}, Silahkan ketik /help untuk menggunakan bot ini
""")
