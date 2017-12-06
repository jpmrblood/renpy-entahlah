# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image bg krupuk = "bg_krupuk.png"
image jepe = "jepe_kipas.png"
image hitam = "#000"
image merah = "#f44242"
image putih = "#ffffff"
image tambah dua = "penambahan_dua.png"

# Declare characters used by this game.
define n = Character(None, kind=nvl, color="#f5fdff") 
define nn = Character(None, color="#f5fdff")
define e = Character('Kipase', color="#c8ffc8")
define p = Character('...', color="#ffecc8")

# The game starts here.
label start:

    scene bg krupuk

    n "Telah diketemukan bahwa kerupuk telah habis."
    n "Bumi bisa hancur! Kerusuhan terjadi!"
    n "{fast}Kepanikan di tempat disko!"

    scene hitam
    with fade
    
    e "Pahlawan... Pahlawan..."
    
    scene bg krupuk
    with fade
    
    e "Bumi bisa hancur! Sekarang, "
    
    p "..."
    
    p "Siapa kamu? Saya di mana?"
    
    
    
    show jepe
    with zoomin
    
    
    e "Ihiy.{p}Maaf...."
    
    e "Aku tidaklah penting. Kamu harus menjawab pertanyaan ini untuk menyelamatkan bumi...."

    e "Berapakah" 
    
    show tambah dua at top
    
    e "Berapakah 2 + 2?" with vpunch
    
menu:
    "0":
        jump bodoh
       
    "4":
        jump vektor
       
    "tidak tahu.":
        jump tdtahu

label bodoh:
    scene merah 
    with dissolve
    e "NGASAL!!!" with vpunch 
    e "Kalau memang tidak tahu, janganlah sok tahu. {p} Lihat! {w} Dunia hancur karenamu!"
    
    jump ending

label vektor:
    scene merah
    e "SALAH!" with vpunch
    e "SALAH! {p}Saya tidak lagi menggunakan ruang vektor umum. Saya mendefinisikan ruang vektor yang lain yang mana 2+2 bukanlah 4!"
    e "Aku tidak percaya denganmu. Binasalah bumi karena pengetahuanmu yang kecil. Ha... ha... ha...."
    jump ending

label tdtahu:
    scene putih
    with dissolve
    e "Benar!" 
    show jepe
    e "Ada banyak cara pertanyaan tersebut diubah. {p} Kita tidak tahu ruang vektor apa yang dipakai. {p} Himpunan bilangan apa yang dipakai. ..."
    e "Operasi penambahan pun belum didefinisikan."
    
    e "Ah... {p}Kamu perlu cari tahu lebih dalam sebelum menjawab. {p}Saya pun pede percayakan bumi kepadamu."
    hide jepe with dissolve
    e "bye."
    
    jump ending

label ending:
    scene hitam
    nn "Tamat."
    return
