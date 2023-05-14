import os
import logging

api_id = int(os.environ.get("API_ID", "16246834"))
api_hash = os.environ.get("API_HASH", "29b3ffa9245c07f05375b92f38e8f13d")
bot_token = os.environ.get("BOT_TOKEN", "5845508740:AAFgpdPF-qg4Kf0eYl4ZCklbQTxGoB30XlY")
# =========================================================== #

db_url = os.environ.get("DB_URL", "mongodb+srv://Kinxmusic:Malik10_@cluster0.iluzwge.mongodb.net/?retryWrites=true&w=majority")
db_name = os.environ.get("DB_NAME", "Cluster0")
# =========================================================== #

channel_1 = int(os.environ.get("CHANNEL_1", "-1001060380553"))
channel_2 = int(os.environ.get("CHANNEL_2", "-1001481870518"))
channel_log = int(os.environ.get("CHANNEL_LOG", "-1001604453419"))
# =========================================================== #

id_admin = int(os.environ.get("ID_ADMIN", "1715348447"))
# =========================================================== #

batas_kirim = int(os.environ.get("BATAS_KIRIM", "5"))
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

hastag = os.environ.get("HASTAG", "#carifwbindo").replace(" ", "|").lower()
# =========================================================== #

pesan_join = os.environ.get("PESAN_JOIN", "Tidak dapat diakses harap join terlebih dahulu, dan gunakan hastag #boy ataw #girl untuk mengirim menfess di @Carifwbindo")
start_msg = os.environ.get("START_MSG", "Hai {fullname} 🌱\n\nIni adalah bot menfess carifwbindo, semua pesan yang kamu kirim akan masuk ke channel secara anonymous, \n\nGunakan Hastag #boy ataw #girl untuk mengirim menfess. \n\nKetik /help info")

gagalkirim_msg = os.environ.get("GAGAL_KIRIM", """
{mention}, Silahkan ketik /help untuk menggunakan bot ini
""")
