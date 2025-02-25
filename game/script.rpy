define ovidiu = Character("Ovidiu", color="#ff8912")
define misha = Character("Misha", color="#b1d9f5")
define valik = Character("Valik", color="#7effe5")
define ruslan = Character("Ruslan", color="#b49d66")
define bazic = Character("Bazic", color="#4ba688")
define eva = Character("Eva", color="#c0ebb9")
define sibov = Character("Sibov", color="#ffb9f0")
define vlad = Character("Vlad", color="#ffa57b")
define semionov = Character("Semionov", color="#7effe5")
define rokitskii = Character("Rokitskii", color="#ffa8a8")
define darie = Character("Darie", color="#d478ff")
define sandel = Character("Săndel", color="#ffcf4a")
define arturel = Character("Arturel", color="#439484")
define neus = Character("Neus", color="#b94545")

define you = Character("[mainCharacterName]")

label start:
    $ you = renpy.input("Cum te cheamă, brat?", length=32)
    $ love_misha = 0
    $ love_ovidiu = 0
    $ love_valik = 0

    # Setarea scenei
    scene bg bedroom with fade
    play music "music/romantic_ambient.wav" fadein 2.0

    # Descriere
    "Suntem în dormitorul lui Ovidiu, după concertul de la Skal. Aerul din cameră e înecăcios – transpirație, bere caldă, fum rămas de la vreo țigară arsă pe jumătate"
    "Pe fundal, un instrumental ciudat – când romantic, când haotic, de parcă și-a pierdut sensul deja"
    "Ovidiu stă pe pat, cu capul pe pernă, respirând încet"
    "Eu – tot acolo, doar că mintea o fute în cercuri de la raskladurile posibile ale acestei seri"
    "În geam se reflectă niște lumini albastre, undeva afară urlă un bomj"
    "Caroci typical Chișinău night"
    "Îmi trec mâna peste față, de parcă aș putea să șterg realitatea, dar ea nu vrea să se șteargă"
    "Blea, iaiebu, eu amuș mă fut cu Ovidiu? Eu? Cu Ovidiu?"
    "Întind mâna după piva de pe podea, dar găsesc doar butîlka goala. O trântesc înapoi"
    "Ovidiu face un sunet vag, poate râde, poate doar expiră adânc"
    "Dar hai, să spunem că asta-i normal. Că-s doar hormonii, că-i doar momentul."
    "Că n-aș trebui să mă gândesc prea mult, că dacă te gândești prea mult, ajungi să scrii poezii pizdastradaliskie pe stories pe insta și să te trezești dimineața cu rușine existențială."

    # Ovidiu începe să vorbească
    show ovidiu
    ovidiu "Băi, da tu ești moldovan sau și?"

    "Ridic o sprânceană, dar nu zic nimic"
    "Ovidiu continuă, vocea lui leneșă, dar cu un zâmbet șiret ascuns pe undeva"

    ovidiu "Ai văzut cum moldovenii, când se îmbată, ori se pizdesc, ori se iau în brațe și plâng?"
    ovidiu "Ei, eu cred că tu ești a doua variantă."

    "Tace un pic, își întoarce capul spre mine"

    ovidiu "În fine, eu n-am jin. Numa pivă. Așa că ori taci și mă lași să adorm, ori hai să mai turnăm ceva înainte să ne ia gândurile razna."

    "Îl privesc. În întuneric, ochii lui sclipesc ușor. Nu știu ce să zic. O parte din mine vrea să râdă, alta vrea să se ridice și să plece"

    ovidiu "Și încă ceva… dacă o să stai așa încruntat, ai să îmbătrânești înainte de 30."
    ovidiu "Și asta, brat, ar fi un păcat mai mare ca fututul între prieteni."

    # Vibe intens
    "Ovidiu nu mai râde, nu mai trage de timp" 
    "E concentrat, ochii lui mă ard, o secundă fixă și apăsătoare" 
    "Și-apoi mă trage spre el, cu acea siguranță de parcă am trecut deja punctul de întoarcere"

    ovidiu "Tu ai două opțiuni. Ori gândești, ori faci. Și mi se pare că ai gândit destul."

    "Respirația mea e grea. Se apleacă puțin spre mine. Mâna lui e pe umărul meu, nu mă împinge, dar nici nu mă lasă să fug"
    "Îmi simt inima bătând în urechi, pulsul e sus, de parcă creierul urlă: fă ceva, fă ceva, fă ceva"

    "Ovidiu face mișcarea decisiva"

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

    "Tăcere absolută. Muzica pe fundal, care trebuia să fie ceva intens, a dispărut complet"
    "Ovidiu se uită la mine, eu la dânsul. Mișa clipește, se uită la noi"

    misha "Eu nu o să dapustesc așa ceva să se întâmple fără mine!"

    ovidiu "Da tu la mama ta acasă n-ai treabă?"

    misha "N-am. Amuș aici e treaba mea."
    
    $ renpy.pause(3.5)

    # Substitutie temporara la muzica care ar trebui sa cante
    play music "music/romantic_ambient.wav" fadein 1.0
    # play music | sample track care o sa-l fac mai incolo "music/sample.wav" fadein 1.0

    ovidiu "Ap și brat, te-ai tusit cu frații Cerebral, ții minte ceva de ieri?"

    menu:
        "Da":
            you "Da, țin minte, ne-am razibit"
            ovidiu "O fost JOSTKAAAA!!!!"

        "Nu":
            you "Nu, da ce-o fost ieri?"
            ovidiu "Brat, o fost cel mai epic concert al nostru, ne-am ușis și oamenii s-o razibit"
            ovidiu "Ne-am certat cu organizatorii că i-o dat afară pe nefori"
            ovidiu "Și am venit aici să ne tusim mai departe"

    valik "Brat, și s-o întâmplat ieri?"
    valik "Nihuia nu țin minte"

    ovidiu "AHAHAHAHA bro! Ai rupt ca de obicei!"

    misha "Bai cesna, o fost Obraz"

    ovidiu "Fanconi"
    ovidiu "Băi, mi-e foame, ieri am borât tot kebabul care l-am mâncat"
    ovidiu "Mersi că ați avut grijă de mine, am adormit ca un iepuraș"

    valik "Ai adormit ca un pidaraș"
    valik "Eu n-am putut să dorm, m-am deprins cu night shift"
    valik "Da fără fete nu-i interesant"
    valik "Tu și fași brat?"

    "M-am emoționat să vorbesc. Valik e așa misterios, nu știu ce să zic"

    misha "Nu te emoționa bro, dintre noi 3, numai ovidiu e dikii"

    ovidiu "Blea, asta-i huinea"
    ovidiu "Amuș încep să mă gândesc la viață și mă dau într-o parte"
    ovidiu "Și după mă gândesc că-s loh și că viața mea nu are sens"
    ovidiu "Nu mă îndrept nicăieri, nu fac nimic cu viața mea"
    ovidiu "Job corporatist nu pot să am, am spus pa-pa la societate de mult"
    ovidiu "Prosta vreau să fac artă și să trăiesc"

    misha "Hai lasă jalea"
    misha "Amuș gătesc ceva"
    misha "Ovidiu, tu ai ceva de gătit?"

    ovidiu "Numai mivină și niște ouă" 

    misha "Lasă bro că-ți fac din asta ceva de-o să ahuiești"

    valik "Da ceva de băut este?"
    valik "Mă duc poate după pivă"

    ovidiu "Și eu vreau să mai dorm oleacă"
    ovidiu "Hai alege cu cine vrei să vorbești, cât ceilalți fac treaba"

    menu:
        "Ovidiu":
            $ love_ovidiu += 1
            hide misha
            hide valik
            show ovidiu at center
            # play music | muzica lui ovidiu "music/sample.wav" fadein 1.0

            ovidiu "Ok bro, hai să vorbim despre societate, suflet, dragoste, viață"
            ovidiu "Și pula, credeai că-s prosta un punk prost?"
            ovidiu "Toți cred asta, și subestimează sentimentele celorlalți"
            ovidiu "Yaebal, ce tare-mi place muzica,"
            ovidiu "Sincer, toată viața vreau să mă ocup de asta"

            "Ovidiu privește gânditor, cu un zâmbet larg și obosit"
            "Se uită la mine, vreau să zic ceva, dar e prea copleșitor"

            ovidiu "Băi, mersi mult că ai venit la concert și ne-ai susținut, fiecare persoană contează pentru mine"
            ovidiu "Blea, odată cântam pe la Pro, n-am fost așa beat niciodată"
            ovidiu "Deseară e rave la pro, hai cu noi"
            ovidiu "Da ce înseamnă pentru tine muzica noastră? Chiar te rupe?"

            "Încep să-i exprim cum simt energia lor, cum tot asta are sens"
            "În toate modurile posibile de a explica fenomenul Cerebral"

            ovidiu "Foarte deep, mă rupe, îmi place!)))"
            ovidiu "Da nu știu ce să zic, mă rușinez oleacă"
            ovidiu "Da singur te-am întrebat. Așteptam lăudat )))"
            ovidiu "Hai că ciuvașii s-o întors"

            "Niciodată n-am văzut o persoană așa haotică încercând atât de tare să te asculte"
            

        "Misha":
            $ love_misha += 1
            hide ovidiu
            hide valik
            show misha at center
            # play music | muzica lui misha "music/sample.wav" fadein 1.0

            misha "Nu sh cum bro"
            misha "Ne-am ucis ghinișor ieri, și avem șansa și pe diseară"
            misha "Va fi rave la Pro. Numai că trebuie rublă de găsit."
            misha "Hatea, s-o vândut binișor merch-u. Am stat și-am fost barâga de merch cât Ovidick și Valik se învârteau pe acolo"

            "Se uită la mine și nu înțeleg de ce"
            "De ce e așa înțelegător omul ăsta? Și ce anume Înțelege el?"

            misha "Tu tot bro ai cumpărat pivă Cerebral, știi că ea de fapt era kozel?"

            "Nu-mi vinea să cred. A fost cea mai bună pivă care am gustat-o vreodată. Și e KOZEL?!"
            "Totodată îmi amintesc cum Misha m-a atras la mașina lor, unde se afla merch-ul"
            "E ca un frate care nu știai că-l ai. Cea mai confortabilă prezență care poate fi"

            misha "Așa mi-i dragă viața de punk, faci ce vrei oricând"
            misha "Ești liber în viață"
            misha "Și fetele-s tare frumoase, așa multe fete frumoase sunt aici"
            misha "Amuș mă apuc eu palibomu să fac mivinele celea, mi-i foame pizdeț"
            misha "Ieri am dughit atâta pivă, eram țapăn"
            misha "Trebu de pohmelit oleacă"
            misha "Hai că ciuvașii s-au întors"
        
        "Valik":
            $ love_valik += 1
            hide ovidiu
            hide misha
            show valik at center
            # play music | muzica lui valik "music/sample.wav" fadein 1.0

            valik "What is this?"
            valik "Cum vapșe noi am ajuns aici?"
            valik "Mai bine la mine la hată trebuia, la Durlești e prea departe"
            valik "Și mâncare în frigider nu-i )"
            valik "Da amuș ne face Mishanea ceva"

            "M-am blocat în fața lui Valik, nu știu ce să zic"
            "E așa misterios și intimidant, cel mai încrezut om pe care l-am întâlnit"

            valik "Și brat, te temi de mine?"
            valik "Da trebu, eu îs tipa punk"
            valik "Hahaha glumesc, mă pricalesc"
            valik "Numai când îs cu cerebral mă pricalesc tipa îs rău"
            valik "Am băut atâta pivă aseară, vreo 12 litri"

            "Poate de asta nu-mi amintesc nimic de aseară"
            "Am băut cu Cerebralu mai mult ca niciodată, ciuvașii îs ibanutâie"

            valik "Daa, vesel o fost, ok, văd că acolo Mishanea gata cu mâncarea"
            valik "Dă să-l trezim pe Ovidiu, îi tragem un băț peste cap"

    # REAPAR TOȚI 3
    show ovidiu at center
    show misha at right
    show valik at left

    misha "Hai ș-om crăpa!!"
    ovidiu "Kancretnaaa"
    valik "Ooo da brat!"

    ## scena la pro. muzica techno

    # ovidiu misha valik
    ovidiu "Iac-așa brat, mi-o fost dor de locul ăsta"

    misha "Da bro, Pro e ca o a doua casă pentru noi. Venim, ne tusim, bem pivă, Usama e ca un unchi pentru noi"

    valik "Și piva-i bună. Fetele frumoase"

    ovidiu "Aici o fost primele noastre concerte, primele rave-uri, primul tot"

    misha "Prima experiență de tusă underground. This is the place"

    ovidiu "Oi blea! Este Ruslan!"

    misha "Eu pe Eva o văd. Și Sanea Neus este!"

    ovidiu "Vlad mai vreu concerte salut!! Arturel zdarova!"

    valik "O, este și Bazic cu Vadim, și Misha Rokitskii pe acolo"

    ovidiu "Yaebal, și Darie este, și Misha Sibov"

    misha "Săndeeel!"

    "Copleșitor, atâția oameni noi și diferiți, grupul începe să se despartă în cercuri de conversații diferite"
    "Acum vine punctul decisiv! Alege cu cine să mergi!"

    menu:
        "Ruslan și Eva":
            ## scena ovidiu ruslan și eva
            ovidiu "Și făceți băăăi dracilor!"
            ovidiu "Mi-o fost tare dor de voi! Cum la București?!"
            ruslan "Băi zaebisi, ne-am tusit tare mult"
            ruslan "Da nimic nu se compară cu tusele din Chișinău. Mi-o fost dor de voi"
            eva "Daaaa băi, acolo nu-s așa interesanți oamenii"
            ovidiu "Azi e raziob, toți oamenii care am vrut să vină au venit. Mă simt așa bucuros))"

        "Bazic și Misha Rokitskii":
            "Aceasta parte inca nu este implementata 🤷"
            ## scena valik bazic misha rokitskii
            ## vorbesc pe rusa
            #3 despre chestii deep


        "Darie și Săndel":
            "Aceasta parte inca nu este implementata 🤷"
            ## scena misha darie si sandel
            ## vorbesc despre muzică, proiectul rap Strada Romană a lui darie și săndel, și alte chetii random, despre chill-uială

        "Misha Sibov și Vadim":
            "Aceasta parte inca nu este implementata 🤷"
            ## scena valik misha sibov si vadim
            ## vorbesc despre cum i-a fost dor lui sibov de noi toti și de dvijul de la pro
            ## misha cu valik îi mai povestesc câte ceva personal sau din proiectele cu Cerebral care le facem
            ## vorbesc pe rusă


        "Vlad și Arturel":
            "Aceasta parte inca nu este implementata 🤷"
            ## scena ovidiu vlad si arturel
            ## vorbesc despre underground, concerte, rave-uri, cât e de raziob aici, etc

        "Sanea Neus":
            "Aceasta parte inca nu este implementata 🤷"
            ## scena neus misha si ovidiu
            ## vorbesc despre cât de pizdoase sunt pozele de la concert, ce raziob a fost, și alte chestii random din viață

    scene bg black with fade
    return
