define ovidiu = Character("Ovidiu", color="#ff8000")
define misha = Character("Misha", color="#fffb00")
define valik = Character("Valik", color="#ff8000")
define you = Character("Tu")

label start:

    # Setarea scenei
    scene bg bedroom with fade
    play music "music/romantic_ambient.wav" fadein 2.0

    # Descriere
    "(Suntem în dormitorul lui Ovidiu, după concertul de la Skal. Aerul din cameră e înecăcios – transpirație, bere caldă, fum rămas de la cine știe ce țigară arsă pe jumătate)"
    "(Pe fundal, un instrumental ciudat – când romantic, când haotic, de parcă și-a pierdut sensul deja)"
    "(Ovidiu stă pe pat, cu capul pe pernă, respirând încet)"
    "(Eu – tot acolo, doar că mintea o fute in cercuri de la raskladurile posibile ale acestei seri)"
    "(În geam se reflectă niște lumini albastre, undeva afară urlă un bomj)"
    "(Caroci typical Chișinău night)"
    "(Îmi trec mâna peste față, de parcă aș putea să șterg realitatea, dar ea nu vrea să se șteargă)"

    # Monolog intern
    "Blea, iaiebu, eu amuș mă fut cu Ovidiu? Eu? Cu Ovidiu?"
    "Sau poate asta nu-i problema principală? Poate problema e că suntem transpirați, putem a sex și ceva vag metalic, și dacă m-aș uita în oglindă, n-aș mai înțelege șini dracu-i acolo?"

    "(Întind mâna după piva de pe podea, dar găsesc doar butîlka goala. O trântesc înapoi)"
    "(Ovidiu face un sunet vag, poate râde, poate doar expiră adânc)"

    "Dar hai, să spunem că asta-i normal. Că-s doar hormonii, că-i doar momentul."
    "Că n-aș trebui să mă gândesc prea mult, că dacă te gândești prea mult, ajungi să scrii poezii pizdastradaliskie pe stories pe insta și să te trezești dimineața cu rușine existențială."

    # Ovidiu începe să vorbească
    show ovidiu
    ovidiu "Băi, da tu ești moldovan sau și?"

    "(Ridic o sprânceană, dar nu zic nimic)"
    "(Ovidiu continuă, vocea lui leneșă, dar cu un zâmbet șiret ascuns pe undeva)"

    ovidiu "Ai văzut cum moldovenii, când se îmbată, ori se pizdesc, ori se iau în brațe și plâng?"
    ovidiu "Ei, eu cred că tu ești a doua variantă."

    "(Tace un pic, își întoarce capul spre mine)"

    ovidiu "În fine, eu n-am jin. Numa pivî. Așa că ori taci și mă lași să adorm, ori hai să mai turnăm ceva înainte să ne ia gândurile razna."

    "(Îl privesc. În întuneric, ochii lui sclipesc ușor. Nu știu ce să zic. O parte din mine vrea să râdă, alta vrea să se ridice și să plece)"

    ovidiu "Și încă ceva… dacă o să stai așa încruntat, ai să îmbătrânești înainte de 30."
    ovidiu "Și asta, brat, ar fi un păcat mai mare ca fututul între prieteni."

    # Vibe intens
    "(Ovidiu nu mai râde, nu mai trage de timp)" 
    "(E concentrat, ochii lui mă ard, o secundă fixă și apăsătoare)" 
    "(Și-apoi mă trage spre el, cu acea siguranță de parcă am trecut deja punctul de întoarcere)"

    ovidiu "Tu ai două opțiuni. Ori gândești, ori faci. Și mi se pare că ai gândit destul."

    "(Respirația mea e grea. Se apleacă puțin spre mine. Mâna lui e pe umărul meu, nu mă împinge, dar nici nu mă lasă să fug)"
    "(Îmi simt inima bătând în urechi, pulsul e sus, de parcă creierul urlă: fă ceva, fă ceva, fă ceva)"

    "(Ovidiu face mișcarea decisiva)"

    # Ovidiu sare la futut
    stop music
    play movie "video/ovidiu_jump.ogv"
    $ renpy.pause(8.0)

    # Mișa intră
    play sound "sfx/door_kick_down_effect.wav"
    $ renpy.pause(3.5)

    show misha at right
    misha "Blea, Ovidiu, Valik, și tvariț voi aiși?!"

    show valik at left

    "(Tăcere absolută. Muzica pe fundal, care trebuia să fie ceva intens, a dispărut complet)"
    "(Ovidiu se uită la mine, eu la dânsul. Mișa clipește, se uită la noi)"

    misha "Eu nu o să dapustesc așa ceva să se întâmple fără mine!"

    ovidiu "Da tu la mama ta acasă n-ai treabă?"

    misha "N-am. Amuș aici e treaba mea."

    scene bg black with fade
    return
