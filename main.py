from menu import Menu
from playsound import playsound
from os import listdir
from pydub.utils import mediainfo


try:
    sura_list = [i for i in listdir("./chapters/") if i.endswith(".wav")]
except FileNotFoundError:
    print("ERR. Shura(s) not found.")
    exit()


def foo0(x):
    print(f"{'-' * 50}\n{x[:-4]}\n{'-' * 50}")
    duration_ms = None
    mediainfo_data = mediainfo("./chapters/" + x)
    if 'duration' in mediainfo_data:
        duration_ms = int(float(mediainfo_data['duration']) * 1000)

    if duration_ms is not None:
        duration_hr, rem = divmod(duration_ms // 1000, 3600)
        duration_min, duration_sec = divmod(rem, 60)

        if duration_hr >= 1:
            print(
                f"Duration: {duration_hr} hr {duration_min} min {duration_sec} sec")
        else:
            print(f"Duration: {duration_min} min {duration_sec} sec")
    else:
        print("Error: Could not determine duration.")
    return playsound("./chapters/" + x)


funcs = []
for i in range(0, 114):
    doc = sura_list[i].split('_')[1][:-4]
    exec(
        f"def Surah_{i + 1}():\n\t\"{doc}\"\n\tfoo0(sura_list[{i}])")
    funcs.append(globals()[f"Surah_{i + 1}"])


suras = Menu(*funcs, validate_zero=False, show_doc=True)
suras.run()
