import os
from deep_translator import GoogleTranslator
from bullet import Bullet
from bullet import colors
lang = "ca"
traductor = GoogleTranslator(source='ca', target=lang)
cli = Bullet(
  choices = [traductor.translate("Espanyol"), traductor.translate("Ingles"), traductor.translate("Frances"),  traductor.translate("Catala"), traductor.translate("Portuges") ], 
  bullet = "",
  bullet_color=colors.bright(colors.foreground["cyan"]),
  word_color=colors.bright(colors.foreground["yellow"]),
  word_on_switch=colors.bright(colors.foreground["yellow"]),
  background_on_switch=colors.background["black"],
  pad_right = 0
)

result = (cli.launch())
if result == traductor.translate("Espanyol"):
  lang = "es"
elif result == traductor.translate("Ingles"):
  lang = "en"
elif result == traductor.translate("Frances"):
  lang = "fr"
elif result == traductor.translate("Catala"):
  lang = "ca"
elif result == traductor.translate("Portuges"):
  lang = "pt"
traductor = GoogleTranslator(source='ca', target=lang)
os.system("clear")
a = input(traductor.translate("Escriu una frase: "))
while True:
  
  cli = Bullet(
    prompt = "\n" + traductor.translate("Selecciona una opcio: "),
    choices = [traductor.translate("1. Longitud de text"),traductor.translate("2. Text en majúscules"),traductor.translate("3. Text en minúscules"),traductor.translate("4. Quantitat de paraules"),traductor.translate("5. Cercar una paraula"), traductor.translate("6. Censurar paraules"),traductor.translate("7. Retallar el text"),traductor.translate("8. Llistar paraules"),traductor.translate("0. Sortir")
    ], 
    indent = 0,
    align = 5, 
    margin = 2,
    bullet = "★",
    bullet_color=colors.bright(colors.foreground["cyan"]),
    word_color=colors.bright(colors.foreground["yellow"]),
    word_on_switch=colors.bright(colors.foreground["yellow"]),
    background_color=colors.background["black"],
    background_on_switch=colors.background["black"],
    pad_right = 5
  )

  result = cli.launch()
  if result == traductor.translate("1. Longitud de text"):
    print(len(a))
  elif result == traductor.translate("2. Text en majúscules"):
    print(a.upper())
  elif result == traductor.translate("3. Text en minúscules"):
    print(a.lower())
  elif result == traductor.translate("4. Quantitat de paraules"):
    print(len(a.split()))
  elif result == traductor.translate("5. Cercar una paraula"):
    b = input(traductor.translate("Escriu la paraula que vols cercar: "))
    print(a.find(b))
  elif result == traductor.translate("6. Censurar paraules"):
    c = input(traductor.translate("Escriu la paraula que vols censurar: "))
    print(a.replace(c,("*" * len(c))))
  elif result == traductor.translate("7. Retallar el text"):
    e = int(input(traductor.translate("Escriu el primer numero: ")))
    d = int(inputtraductor.translate(("Escriu el ulitmo numero: ")))
    print(a[e:d])
  elif result == traductor.translate("8. Llistar paraules"):
    list = (a.split())
    for i in list:
      print(i)
  elif result == traductor.translate("0. Sortir"):
    print(traductor.translate("Adeu"))
    exit()

