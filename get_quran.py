from pydub import AudioSegment
import requests
import os
from tqdm import tqdm
import shutil


def rename_files(old_name, new_name):
    """Renames all files in the current directory with the given old name to the new name."""
    for filename in os.listdir():
        if filename == old_name:
            os.rename(filename, new_name)


def download_audio(url, filename):
    """Downloads the audio file from the given URL and saves it with the given filename."""
    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)


def convert_mp3_to_wav(filename):
    """Converts the MP3 file with the given filename to WAV format and deletes the original MP3 file."""
    audio = AudioSegment.from_mp3(filename)
    audio.export(filename[:-4] + ".wav", format="wav")
    os.remove(filename)


def clean_files():
    """Deletes all MP3 and WAV files in the current directory and the 'chapters' directory (if it exists)."""
    bar0 = [i for i in os.listdir() if i.endswith(".mp3")]
    bar1 = [i for i in os.listdir() if i.endswith(".wav")]

    for i in (bar0 + bar1):
        os.remove(i)

    if os.path.exists("./chapters"):
        shutil.rmtree("./chapters")


try:
    print("\n------ Start ------\n")
    print("[*] Downloading suras")
    pbar = tqdm(total=114)
    for i in range(114):
        url = f"https://podcasts.qurancentral.com/abdul-rahman-al-sudais/192/abdul-rahman-al-sudais-{i + 1:03}-qurancentral.com-192.mp3"
        download_audio(url, f"{i}.mp3")
        pbar.update(1)
    pbar.close()
except KeyboardInterrupt:
    clean_files()
    exit()


try:
    print("\n[*] Converting mp3 to wav")
    pbar = tqdm(total=114)
    for i in [x for x in os.listdir() if x.endswith(".mp3")]:
        convert_mp3_to_wav(i)
        pbar.update(1)
    pbar.close()
except KeyboardInterrupt:
    clean_files()
    exit()


filenames = [
    "001_Surah Al Fatihah - The Opener",
    "002_Surat Al-Baqarah (The Calf)",
    "003_Surah Ali-Imran (Family of Imran)",
    "004_Surah An-Nisa (The Women)",
    "005_Surah Al-Maidah (The Table Spread)",
    "006_Surah Al-Anam (The Cattle)",
    "007_Surah Al-Araf (The Heights)",
    "008_Surah Al-Anfal (The Spoils of War)",
    "009_Surah At-Tawba (The Repentance)",
    "010_Surah Yunus (Jonah)",
    "011_Surah Hud (Hud)",
    "012_Surah Yusuf (Joseph)",
    "013_Surah Ar-R'ad (The Thunder)",
    "014_Surah Ibrahim (Ibrahim)",
    "015_Surah Al-Hijr (The Rocky Tract)",
    "016_Surah An-Nahl (The Opener)",
    "017_Surah Al-Isra (The Night Journey)",
    "018_Surah Al-Kahf (The Cave)",
    "019_Surah Maryam (Mary)",
    "020_Surat Taha (Ta-Ha)",
    "021_Surat Anbiya (The Prophets)",
    "022_Surah Al-Haj (The Pilgrimage)",
    "023_Surah Al-Mu'minun (The Believers)",
    "024_Surah An-Nur (The Light)",
    "025_Surah Al-Furqan (The Criterion)",
    "026_Ash-Shu'ara (The Poets)",
    "027_Surah An-Naml (The Ant)",
    "028_Surah Al-Qasas (The Story)",
    "029_Surah Al-Ankabut (The Spider)",
    "030_Surah Ar-Rum (The Romans)",
    "031_Surah Luqman (Luqman)",
    "032_Surah As-Sajdah (The Prostration)",
    "033_Surah Al-Ahzab - The Clans",
    "034_Saba (Sheba)",
    "035_Surah Fatir - The Originator",
    "036_Surah Ya-Sin (Ya Sin)",
    "037_Surah As-Saffat (Those Who Draw Up In Ranks)",
    "038_Surah Saad (The Letter Saad)",
    "039_Surah Az-Zumar (The Groups)",
    "040_Al Ghaafir (The Forgiver)",
    "041_Fussilat (Explained In Detail)",
    "042_Ash-Shura - The Consultation",
    "043_Az-Zukhruf (The Gold Adornments)",
    "044_Ad-Dukhan (The Smoke)",
    "045_Al-Jathiyah (The Kneeling Down, Crouching)",
    "046_Surah Al-Ahqaf (The Dunes)",
    "047_Surah Muhammad (Muhammad)",
    "048_Al-Fath (The Victory)",
    "049_Al-Hujurat (The Inner Apartments)",
    "050_Qaf (Qaf)",
    "051_Ad-Dhariyat - The Wind That Scatters",
    "052_At-Tur (The Mount)",
    "053_An-Najm (The Star, The Unfolding)",
    "054_Al-Qamar - The Moon (1)",
    "055_Ar-Rahman (The Beneficent)",
    "056_Al-Waqi'ah (The Inevitable, The Event)",
    "057_Al-Hadeed (The Iron)",
    "058_Al-Mujadilah (The Pleading, The Pleading Woman)",
    "059_Al-Hashr - (The Mustering, The Gathering, Exile, Banishment)",
    "060_Al-Mumtahanah (The Examined One)",
    "061_As-Saff - (The Ranks)",
    "062_Al-Jumu'ah (The Congregation, Friday)",
    "063_Al-Munafiqun (The Hypocrites)",
    "064_At-Taghabun - The Cheating",
    "065_At-Talaq - Divorce",
    "066_At-Tahreem - The Prohibition",
    "067_Al-Mulk (The Dominion, Sovereignty)",
    "068_Al-Qalam (The Pen)",
    "069_Al-Haqqah - (The Inevitable Reality) ",
    "070_Al-Ma'aarij - The Ascending Stairways",
    "071_Nuh (Noah)",
    "072_Al-Jinn (The Spirits, The Unseen Beings)",
    "073_Al-Muzzammil (The Enfolded One)",
    "074_Al-Muddathir (The Cloaked One)",
    "075_Al-Qiyamah (The Resurrection)",
    "076_Al-Insan (The Man)",
    "077_Surah Al-Mursalat (The Emissaries)",
    "078_Surat An-Naba (The Tidings)",
    "079_Surat An-Naziat (Those Who Drag Forth)",
    "080_Abasa (He Frowned)",
    "081_Takwir (The Overthrowing)",
    "082_Al-Infitar (The Cleaving)",
    "083_Al-Mutaffifin (The Defrauding)",
    "084_Al-Inshiqaq (The Sundering)",
    "085_Al-Buruj (The Mansions of the Stars)",
    "086_A-Tariq (The Night Comer)",
    "087_Al-Ala (The Most High)",
    "088_Al-Ghashiyah (The Overwhelming)",
    "089_Al-Fajr (The Dawn)",
    "090_Al-Balad (The City)",
    "091_Ash-Shams (The Sun)",
    "092_Al-Layl (The Night)",
    "093_Ad Duhaa (The Morning Hours)",
    "094_Ash Sharh (The Relief)",
    "095_At-Tin (The Fig)",
    "096_Al Alaq (The Clot)",
    "097_Al Qadr (The Power)",
    "098_Al Bayyinah (The Clear Proof)",
    "099_Az Zalzalah (The Earthquake)",
    "100_Al Adiyat (The Courser)",
    "101_Al Qariah (The Calamity)",
    "102_Al-Takathur (The Rivalry for Worldly Increase",
    "103_Al-Asr (The Declining Day)",
    "104_Al-Humazah (The Gossipmonger)",
    "105_Al-Fil (The Elephant)",
    "106_Quraysh (Quraysh)",
    "107_Al Mau'un (The Small Kindness)",
    "108_Al Kawthar (The Abundance)",
    "109_Al Kafirun (The Disbelievers)",
    "110_Surah An Nasr (The Divine Support)",
    "111_Surah Al Massad (The Palm Fibre)",
    "112_Surah Al Ikhlas (The Sincerity)",
    "113_Surah Al Falaq (The Daybreak)",
    "114_Surah An Nas (Mankind)",
]


try:
    print("\n[*] Renaming suras ...")
    pbar = tqdm(total=114)
    for x, i in enumerate(filenames):
        rename_files(f"{x}.wav", f"{i}.wav")
        pbar.update(1)
    pbar.close()
except KeyboardInterrupt:
    clean_files()
    exit()


try:
    print("\n[*] Final Arrangements.")

    if not os.path.exists("./chapters/"):
        os.makedirs("./chapters/")

    pbar = tqdm(total=114)
    for filename in os.listdir():
        if filename.endswith(".wav"):
            src_path = os.path.join("./", filename)
            dest_path = os.path.join("./chapters/", filename)
            shutil.move(src_path, dest_path)
            pbar.update(1)
    pbar.close()

except KeyboardInterrupt:
    clean_files()
    exit()


print("\n------ Finish ------")
