import os
import logging

api_id = int(os.environ.get("API_ID", "22362456"))
api_hash = os.environ.get("API_HASH", "8f1e661a440f2663ab0d3b52dd0d4cbc")
bot_token = os.environ.get("BOT_TOKEN", "")
# =========================================================== #

db_url = os.environ.get("DB_URL", "mongodb+srv://Menfess:Malik10_@cluster0.0q7u10d.mongodb.net/?retryWrites=true&w=majority")
db_name = os.environ.get("DB_NAME", "Cluster0")
# =========================================================== #

channel_1 = int(os.environ.get("CHANNEL_1", "-1002063775407"))
channel_2 = int(os.environ.get("CHANNEL_2", "-1001907458581"))
channel_log = int(os.environ.get("CHANNEL_LOG", "-1001628283862"))
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

hastag = os.environ.get("HASTAG", "#Girl #Boy #Spill #Story").replace(" ", "|").lower()
# =========================================================== #

pesan_join = os.environ.get("PESAN_JOIN", "<b>Tidak dapat diakses harap join terlebih dahulu. Kemudian Start Ulang</b>")
start_msg = os.environ.get("START_MSG", "<b>Hai {fullname} 🌱\n\nIni adalah bot menfess cari sahabat mutualan, anda bisa mengirim pesan secara anonymous, \n\nWajib pilih hastag sebagai berikut untuk mengirim pesan #boy ataw #girl untuk mengirim menfess. \n\nKetik /help info")

gagalkirim_msg = os.environ.get("GAGAL_KIRIM", """
{mention}, Silahkan ketik /help untuk menggunakan bot ini
""")
