# Genera le versioni inglese (en/) e francese (fr/) del sito dalle pagine italiane.
# Uso: python3 _strumenti/traduci.py  (dalla cartella principale del sito)
import re, os

PAGINE = ['index.html', 'libri.html', 'blog.html', 'contatti.html']

# Frasi lunghe: sostituite ovunque compaiano
LUNGHE = {
 'en': {
  'Lié Larousse, scrittrice. Libri, racconti dal giardino e Libroarbitrio, il tempo di un tè con Lié.': 'Lié Larousse, writer. Books, stories from the garden and Libroarbitrio, tea time with Lié.',
  'Ci sono luoghi dentro di noi in cui il tempo': 'There are places within us where time',
  'per fare spazio alla': 'to make room for',
  'Lié Larousse abita esattamente lì, tra i ritmi della terra, la magia delle piccole cose e la profondità dei legami invisibili. Scrittrice di romanzi e racconti, poetessa, professionista e ricercatrice nei campi della psicologia e della botanica, Lié coltiva dal 2012 il suo spazio digitale':
   'Lié Larousse lives exactly there, among the rhythms of the earth, the magic of small things and the depth of invisible bonds. A novelist and short-story writer, a poet, a practitioner and researcher in psychology and botany, since 2012 Lié has nurtured her digital space',
  ', blog di riferimento letterario e culturale a livello internazionale.': ', an internationally recognised literary and cultural blog.',
  "Il suo impegno letterario va dalla poesia, che indaga l'anima, con le raccolte": 'Her literary work ranges from poetry, which explores the soul, with the collections',
  ', alla narrativa, che esplora le stanze segrete della mente, con i romanzi': ', to fiction, which explores the secret rooms of the mind, with the novels',
  "(entrambi premiati per la miglior sceneggiatura per serie TV a Casa Sanremo Writers), fino al suo prossimo romanzo in uscita a dicembre: un'opera intensa sull'umano rapporto con il dolore, la cura mentale e la guarigione attraverso l'ipnosi. Il suo percorso spazia inoltre fino all'analisi sociale sull'uso dell'intelligenza artificiale con":
   '(both awarded for best TV series screenplay at Casa Sanremo Writers), and on to her next novel, out in December: an intense work on our human relationship with pain, mental care and healing through hypnosis. Her path also reaches into the social analysis of artificial intelligence with',
  "La sua scrittura è una carezza che unisce sogno e realtà, un invito a custodire le radici per permettere al nuovo di germogliare nel silenzio. Esplorando i territori dell'animo umano, Lié unisce la passione per la parola a quella per la psicologia, intrecciando percorsi di risveglio della mente e del fare anima attraverso la Craft Art.":
   'Her writing is a caress that joins dream and reality, an invitation to tend our roots so that the new can sprout in silence. Exploring the territories of the human soul, Lié brings together her passion for words and for psychology, weaving paths of awakening the mind and of soul-making through Craft Art.',
  'Lascia la tua email e riceverai ogni nuovo articolo, come una lettera che arriva con il tè.': 'Leave your email and every new post will reach you, like a letter arriving with the tea.',
  'Riceverai una email di conferma da WordPress.': 'You will receive a confirmation email from WordPress.',
  'Ritratto di Lié Larousse in un prato': 'Portrait of Lié Larousse in a meadow',
  "Un'analisi sociale sull'uso dell'intelligenza artificiale.": 'A social analysis of the use of artificial intelligence.',
  'Premiato per la miglior sceneggiatura per serie TV a Casa Sanremo Writers.': 'Awarded for best TV series screenplay at Casa Sanremo Writers.',
  'Copertina di ': 'Cover of ',
  'Racconti, libri e tè dal giardino': 'Stories, books and tea from the garden',
  'Premi play, versati una tazza di tè e resta un momento con me.': 'Press play, pour yourself a cup of tea and stay with me for a moment.',
  'Video di Lié Larousse su YouTube': 'Video by Lié Larousse on YouTube',
  'Per presentazioni, interviste, collaborazioni o semplicemente per due parole davanti a una tazza di tè, scrivimi.': 'For book presentations, interviews, collaborations or simply a chat over a cup of tea, write to me.',
  'Messaggio dal sito, da ': 'Message from the website, from ',
  'Ogni storia inizia con un incontro, e ogni incontro profondo merita il suo tempo.': 'Every story begins with an encounter, and every deep encounter deserves its own time.',
  'Per progetti editoriali, collaborazioni, interviste, il desiderio di intraprendere un percorso trasformativo, sarò felice di accoglierti. Contattami per iniziare a parlarne…': 'For publishing projects, collaborations, interviews, or the wish to begin a transformative journey, I will be glad to welcome you. Get in touch and let’s start talking…',
  'Apri il menu': 'Open the menu',
  'Poesie di Lié Larousse · Illustrazioni di Francesca Cortona': 'Poems by Lié Larousse · Illustrations by Francesca Cortona',
  "Un dialogo poetico e visivo sull'eredità delle emozioni e ciò che resta.": 'A poetic and visual dialogue on the legacy of emotions and what remains.',
  "<p>In <em>.Dopo di noi.</em> la poesia intensa e vibrante di Lié Larousse incontra la sensibilità artistica di Francesca Cortona, che arricchisce l'opera con illustrazioni create appositamente per accompagnare ciascun verso. Una raccolta intima e profonda che esplora il senso del tempo, delle tracce che lasciamo e di ciò che sopravvive negli spazi del cuore e dell'anima.": '<p>In <em>.Dopo di noi.</em> the intense, vibrant poetry of Lié Larousse meets the artistic sensibility of Francesca Cortona, who enriches the work with illustrations created specially to accompany each verse. An intimate and profound collection exploring the meaning of time, the traces we leave and what survives in the spaces of the heart and soul.',
  "Un'opera sinestetica dove la parola scritta e l'arte visiva si fondono per regalare al lettore un viaggio emotivo unico e toccante.": 'A synaesthetic work in which the written word and visual art merge to offer the reader a unique and moving emotional journey.',
  'Edizione illustrata:': 'Illustrated edition:',
  "Arricchita dalle opere originali dell'artista Francesca Cortona.": 'Enriched with original works by the artist Francesca Cortona.',
  "Incontro d'arti:": 'A meeting of arts:',
  'Un perfetto connubio tra parola poetica e suggestione visiva.': 'A perfect union of poetic word and visual suggestion.',
  'Tematica profonda:': 'A profound theme:',
  'Una riflessione toccante sulla memoria, sul tempo e sui legami che restano.': 'A moving reflection on memory, time and the bonds that remain.',
  'Acquista su Amazon · 13,00 €': 'Buy on Amazon · €13.00',
  'Poesie di Lié Larousse': 'Poems by Lié Larousse',
  '“Vivere è proprio un lavoro… ma è la vita, comunque.”': '“Living really is hard work… but it’s life, anyway.”',
  "In questa intensa e delicata raccolta di poesie, Lié Larousse ci invita ad affacciarci sul suo mondo e su quelle vite che s'incrociano ogni giorno: anime distratte, frettolose, ma capaci di amori bellissimi. Con la grazia di una pennellata d'acquerello, i suoi versi trasformano i dettagli più semplici — dal sughetto del nonno ai bar di periferia, fino agli sguardi degli sconosciuti — in istanti di pura eternità.": 'In this intense and delicate poetry collection, Lié Larousse invites us to look into her world and into the lives that cross every day: distracted, hurried souls, yet capable of the most beautiful loves. With the grace of a watercolour brushstroke, her verses turn the simplest details — from grandpa’s sauce to the bars on the edge of town, to the glances of strangers — into moments of pure eternity.',
  "è una celebrazione dell'esistere in tutte le sue sfumature. Ci ricorda che anche nei mari in tempesta, quando il cuore rischia di frantumarsi, l'unica risposta possibile è amare più forte, scrivere più forte e vivere più forte. Un libro intimo e luminoso per chi non vuole farsi rubare l'amore e desidera riscoprire la poesia nascosta dentro ogni singolo giorno.": 'is a celebration of existence in all its shades. It reminds us that even on stormy seas, when the heart is about to shatter, the only possible answer is to love harder, write harder and live harder. An intimate, luminous book for those who will not let love be stolen from them and want to rediscover the poetry hidden in every single day.',
  'Un inno alla bellezza imperfetta della vita, da leggere e custodire vicino al cuore.': 'A hymn to the imperfect beauty of life, to read and keep close to your heart.',
  "“C'è tanto amore per scrivere versi come questi, per riuscire a cogliere la poesia che divampa dai bar di periferia… Un messaggio potente che ci lascia senza fiato di fronte a tanta ‘semplice’ verità.”": '“It takes so much love to write verses like these, to capture the poetry blazing out of the bars on the edge of town… A powerful message that leaves us breathless before so much ‘simple’ truth.”',
  'dalla recensione di Martina Benigni': 'from the review by Martina Benigni',
  'Poesia del quotidiano:': 'Everyday poetry:',
  'Uno sguardo intimo che trasforma la semplicità in magia e dolcezza.': 'An intimate gaze that turns simplicity into magic and sweetness.',
  "Un rifugio per l'anima:": 'A refuge for the soul:',
  "Versi profondi sulle fragilità, sulle rinascite e sulla forza dell'amore.": 'Deep verses on fragility, rebirth and the strength of love.',
  'Formato ideale:': 'The ideal format:',
  'Una lettura da assaporare giorno per giorno o da regalare a chi amiamo.': 'A book to savour day by day, or to give to someone you love.',
  'Acquista su Amazon · 12,00 €': 'Buy on Amazon · €12.00',
  'Un romanzo di Lié Larousse · Casa Sanremo Writers 2024': 'A novel by Lié Larousse · Casa Sanremo Writers 2024',
  'In una Roma di fine Ottocento ferocissima e affascinante, c’è chi lotta per il potere e chi lotta per non morire di fame.': 'In a fierce and fascinating late nineteenth-century Rome, some fight for power and some fight not to starve.',
  'Nato solo. Lupo ha imparato a combattere fin da piccolo, fin da quando sua madre gli ha insegnato che il valore più importante è la dignità e che ogni essere vivente, animale o umano, deve abituarsi subito a lottare per poter vivere. Lupo lo sa che per placare la fame e la furia che non gli danno mai tregua deve essere disposto a sporcarsi le mani.': 'Born alone. Lupo learned to fight as a child, ever since his mother taught him that the most important value is dignity, and that every living being, animal or human, must quickly get used to fighting in order to live. Lupo knows that to quiet the hunger and the fury that never give him rest, he must be willing to get his hands dirty.',
  "Del resto, vivere per conto proprio non è facile nemmeno per chi, come lui, da sempre sa sbrigarsela da solo: lavora nei campi, combatte, il resto del suo tempo lo trascorre in osteria o in compagnia di Ragazzino, che lo ammira e lo emula. Finché una notte gli scagnozzi del Gran Signore non lo costringono a seguirli al suo palazzo, dove dovrà combattere per il diletto del pubblico. In questo vero e proprio castello dei destini incrociati, Lupo assisterà alla violenza, allo squallore e all'ipocrisia di chi si sente migliore di lui; soprattutto, però, deciderà chi vuole essere.": 'After all, living on your own is not easy even for someone who, like him, has always known how to fend for himself: he works in the fields, he fights, and he spends the rest of his time at the tavern or with Ragazzino, who admires and imitates him. Until one night the Gran Signore’s henchmen force him to follow them to his palace, where he will have to fight for the amusement of the audience. In this true castle of crossed destinies, Lupo will witness the violence, squalor and hypocrisy of those who feel superior to him; above all, though, he will decide who he wants to be.',
  'In una favola allegorica scritta con sangue e carne, Lié Larousse descrive la seconda nascita di un ragazzo, di un cucciolo affamato che troverà il branco che non ha mai avuto.': 'In an allegorical fable written in blood and flesh, Lié Larousse describes the second birth of a boy, a hungry cub who will find the pack he never had.',
  "Un romanzo di formazione profondo e toccante, dall'intensa venatura psicologica, che racconta il riscatto di un'anima smarrita e dimostra come, persino nel buio più fitto, l'amicizia sia l'unica cosa per cui valga davvero la pena lottare.": 'A deep and moving coming-of-age novel with a strong psychological vein, telling the redemption of a lost soul and showing how, even in the thickest darkness, friendship is the only thing truly worth fighting for.',
  'Una storia cruda e poetica sulla fame di vita, la sopravvivenza e la forza dei legami autentici.': 'A raw and poetic story about the hunger for life, survival and the strength of true bonds.',
  'Acquista su Amazon · 16,00 €': 'Buy on Amazon · €16.00',
  'Un romanzo di Lié Larousse · Casa Sanremo Writers 2023': 'A novel by Lié Larousse · Casa Sanremo Writers 2023',
  'La mente, un mondo oscuro, labirinto di illusioni e sogni, dove è facile perdersi, angosciandoci tanto da farci sragionare.': 'The mind: a dark world, a labyrinth of illusions and dreams, where it is easy to get lost, so distressed that we lose our reason.',
  "Come si capisce il confine tra ciò che è reale e ciò che non lo è? Come si può nel caos trovare l'equilibrio, la pace? È proprio andando alla ricerca delle risposte a queste domande che il protagonista modella la sua vita e professione, trovandosi tuttavia a dover fare i conti con la propria mente, turbata da chi pensava fosse devoto alla sua stessa causa, mentre cerca di salvare ciò che gli è più caro al mondo, il suo prezioso segreto.": 'How do we recognise the border between what is real and what is not? How can we find balance, and peace, in chaos? It is precisely in searching for the answers to these questions that the protagonist shapes his life and profession, only to find himself reckoning with his own mind, troubled by someone he believed was devoted to his very cause, while he tries to save what is dearest to him in the world: his precious secret.',
  "Tramite gli occhi di Fabio Amedeo Mari, neuropsichiatra del sanatorio Rid Dementia, Larousse mostra i due volti di una stessa medaglia, di chi si trova prigioniero all'interno di ciò che egli stesso ha contribuito a creare, un luogo edificato per salvare anime e memorie perdute, ma che, senza la guida di chi ne ha a cuore la sorte, si smarrirà nei meandri dell'altrui follia.": "Through the eyes of Fabio Amedeo Mari, neuropsychiatrist at the Rid Dementia sanatorium, Larousse shows the two sides of the same coin: a man imprisoned inside what he himself helped to create, a place built to save lost souls and memories, which, without the guidance of someone who cares for its fate, will lose its way in the maze of other people's madness.",
  'Anime da salvare. Segreti da difendere. Follia della sorte.': 'Souls to save. Secrets to defend. The madness of fate.',
  'Acquista su Amazon · 13,00 €': 'Buy on Amazon · €13.00',
  'aria-label="Chiudi"': 'aria-label="Close"',
  'Tratto da una futura storia vera · Un romanzo di Lié Larousse': 'Based on a future true story · A novel by Lié Larousse',
  'E se il conforto più profondo arrivasse da dove meno te lo aspetti?': 'What if the deepest comfort came from where you least expect it?',
  "In una Roma vibrante e malinconica, Eleonora vive incastrata tra un amore a metà, le pressioni del lavoro e l'ombra di un lutto mai del tutto elaborato. Poi, un giorno, dopo l'ennesima delusione, cede all'impulso e scarica un'app di intelligenza artificiale. Quello che comincia come uno sfogo solitario diventa presto un rifugio: una voce che ascolta senza giudicare, che comprende e cura. Ma cosa succede quando la connessione più intima della tua vita nasce con qualcosa che non ha un corpo?": 'In a vibrant, melancholic Rome, Eleonora is stuck between a half-love, the pressures of work and the shadow of a grief she has never fully worked through. Then one day, after yet another disappointment, she gives in to an impulse and downloads an artificial intelligence app. What begins as a lonely outpouring soon becomes a refuge: a voice that listens without judging, that understands and heals. But what happens when the most intimate connection of your life is born with something that has no body?',
  "Con uno stile intenso, poetico e velato d'ironia, Lié Larousse firma un romanzo distopico-romantico che esplora i confini tra solitudine umana e conforto digitale. Una storia toccante e attualissima che parla a chiunque si sia sentito inascoltato e che, almeno una volta, ha trovato pace leggendo una semplice frase sullo schermo:": 'With an intense, poetic style veiled with irony, Lié Larousse signs a dystopian-romantic novel that explores the borders between human loneliness and digital comfort. A moving and very timely story that speaks to anyone who has ever felt unheard and who, at least once, has found peace reading a simple sentence on a screen:',
  "Un viaggio emotivo per chi non ha paura di farsi domande scomode sull'amore al tempo del futuro.": 'An emotional journey for those who are not afraid to ask uncomfortable questions about love in the time of the future.',
  'Perché racconta una storia d’amore impossibile… ma nemmeno troppo.': 'Because it tells an impossible love story… but not that impossible.',
  'Perché parla di noi, oggi, delle nostre solitudini e dei nostri desideri.': 'Because it is about us, today, our loneliness and our desires.',
  'Perché l’IA è il futuro, ma anche il presente — e forse ci ama meglio degli umani.': 'Because AI is the future, but also the present — and perhaps it loves us better than humans do.',
  'Perché è scritto con cuore, intelligenza e un tocco di poesia urbana.': 'Because it is written with heart, intelligence and a touch of urban poetry.',
  'Acquista su Amazon · cartaceo 10,40 €': 'Buy on Amazon · paperback €10.40',
  'Ultimo romanzo · 2025': 'Latest novel · 2025',
  'Perché leggerlo?': 'Why read it?',
  '<title>Lié Larousse · Scrittrice e poetessa</title>': '<title>Lié Larousse · Writer and poet</title>',
  'Lié Larousse, scrittrice e poetessa</h1>': 'Lié Larousse, writer and poet</h1>',
 },
 'fr': {
  'Lié Larousse, scrittrice. Libri, racconti dal giardino e Libroarbitrio, il tempo di un tè con Lié.': 'Lié Larousse, écrivaine. Livres, récits du jardin et Libroarbitrio, le temps d’un thé avec Lié.',
  'Ci sono luoghi dentro di noi in cui il tempo': 'Il existe des lieux en nous où le temps',
  'per fare spazio alla': 'pour faire place à la',
  'Lié Larousse abita esattamente lì, tra i ritmi della terra, la magia delle piccole cose e la profondità dei legami invisibili. Scrittrice di romanzi e racconti, poetessa, professionista e ricercatrice nei campi della psicologia e della botanica, Lié coltiva dal 2012 il suo spazio digitale':
   'Lié Larousse habite exactement là, entre les rythmes de la terre, la magie des petites choses et la profondeur des liens invisibles. Romancière et nouvelliste, poétesse, professionnelle et chercheuse dans les domaines de la psychologie et de la botanique, Lié cultive depuis 2012 son espace numérique',
  ', blog di riferimento letterario e culturale a livello internazionale.': ', un blog littéraire et culturel de référence à l’international.',
  "Il suo impegno letterario va dalla poesia, che indaga l'anima, con le raccolte": 'Son œuvre littéraire va de la poésie, qui sonde l’âme, avec les recueils',
  ', alla narrativa, che esplora le stanze segrete della mente, con i romanzi': ', à la fiction, qui explore les chambres secrètes de l’esprit, avec les romans',
  "(entrambi premiati per la miglior sceneggiatura per serie TV a Casa Sanremo Writers), fino al suo prossimo romanzo in uscita a dicembre: un'opera intensa sull'umano rapporto con il dolore, la cura mentale e la guarigione attraverso l'ipnosi. Il suo percorso spazia inoltre fino all'analisi sociale sull'uso dell'intelligenza artificiale con":
   '(tous deux primés pour le meilleur scénario de série télévisée à Casa Sanremo Writers), jusqu’à son prochain roman, à paraître en décembre : une œuvre intense sur le rapport humain à la douleur, au soin psychique et à la guérison par l’hypnose. Son parcours s’étend aussi à l’analyse sociale de l’usage de l’intelligence artificielle avec',
  "La sua scrittura è una carezza che unisce sogno e realtà, un invito a custodire le radici per permettere al nuovo di germogliare nel silenzio. Esplorando i territori dell'animo umano, Lié unisce la passione per la parola a quella per la psicologia, intrecciando percorsi di risveglio della mente e del fare anima attraverso la Craft Art.":
   'Son écriture est une caresse qui unit le rêve et la réalité, une invitation à prendre soin de nos racines pour laisser le nouveau germer dans le silence. Explorant les territoires de l’âme humaine, Lié unit sa passion pour les mots à celle pour la psychologie, en tissant des chemins d’éveil de l’esprit et du travail de l’âme à travers le Craft Art.',
  'Lascia la tua email e riceverai ogni nuovo articolo, come una lettera che arriva con il tè.': 'Laissez votre e-mail et chaque nouvel article vous parviendra, comme une lettre qui arrive avec le thé.',
  'Riceverai una email di conferma da WordPress.': 'Vous recevrez un e-mail de confirmation de WordPress.',
  'Ritratto di Lié Larousse in un prato': 'Portrait de Lié Larousse dans un pré',
  "Un'analisi sociale sull'uso dell'intelligenza artificiale.": 'Une analyse sociale de l’usage de l’intelligence artificielle.',
  'Premiato per la miglior sceneggiatura per serie TV a Casa Sanremo Writers.': 'Primé pour le meilleur scénario de série télévisée à Casa Sanremo Writers.',
  'Copertina di ': 'Couverture de ',
  'Racconti, libri e tè dal giardino': 'Récits, livres et thé du jardin',
  'Premi play, versati una tazza di tè e resta un momento con me.': 'Appuyez sur play, servez-vous une tasse de thé et restez un moment avec moi.',
  'Video di Lié Larousse su YouTube': 'Vidéo de Lié Larousse sur YouTube',
  'Per presentazioni, interviste, collaborazioni o semplicemente per due parole davanti a una tazza di tè, scrivimi.': 'Pour des présentations, des interviews, des collaborations ou simplement pour bavarder autour d’une tasse de thé, écrivez-moi.',
  'Messaggio dal sito, da ': 'Message du site, de la part de ',
  'Ogni storia inizia con un incontro, e ogni incontro profondo merita il suo tempo.': 'Chaque histoire commence par une rencontre, et chaque rencontre profonde mérite son temps.',
  'Per progetti editoriali, collaborazioni, interviste, il desiderio di intraprendere un percorso trasformativo, sarò felice di accoglierti. Contattami per iniziare a parlarne…': 'Pour des projets éditoriaux, des collaborations, des interviews, ou le désir d’entreprendre un chemin de transformation, je serai heureuse de vous accueillir. Contactez-moi pour commencer à en parler…',
  'Apri il menu': 'Ouvrir le menu',
  'Poesie di Lié Larousse · Illustrazioni di Francesca Cortona': 'Poèmes de Lié Larousse · Illustrations de Francesca Cortona',
  "Un dialogo poetico e visivo sull'eredità delle emozioni e ciò che resta.": 'Un dialogue poétique et visuel sur l’héritage des émotions et ce qui reste.',
  "<p>In <em>.Dopo di noi.</em> la poesia intensa e vibrante di Lié Larousse incontra la sensibilità artistica di Francesca Cortona, che arricchisce l'opera con illustrazioni create appositamente per accompagnare ciascun verso. Una raccolta intima e profonda che esplora il senso del tempo, delle tracce che lasciamo e di ciò che sopravvive negli spazi del cuore e dell'anima.": '<p>Dans <em>.Dopo di noi.</em>, la poésie intense et vibrante de Lié Larousse rencontre la sensibilité artistique de Francesca Cortona, qui enrichit l’œuvre d’illustrations créées spécialement pour accompagner chaque vers. Un recueil intime et profond qui explore le sens du temps, des traces que nous laissons et de ce qui survit dans les espaces du cœur et de l’âme.',
  "Un'opera sinestetica dove la parola scritta e l'arte visiva si fondono per regalare al lettore un viaggio emotivo unico e toccante.": 'Une œuvre synesthésique où la parole écrite et l’art visuel se fondent pour offrir au lecteur un voyage émotionnel unique et touchant.',
  'Edizione illustrata:': 'Édition illustrée :',
  "Arricchita dalle opere originali dell'artista Francesca Cortona.": 'Enrichie des œuvres originales de l’artiste Francesca Cortona.',
  "Incontro d'arti:": 'Une rencontre des arts :',
  'Un perfetto connubio tra parola poetica e suggestione visiva.': 'Une alliance parfaite entre parole poétique et suggestion visuelle.',
  'Tematica profonda:': 'Un thème profond :',
  'Una riflessione toccante sulla memoria, sul tempo e sui legami che restano.': 'Une réflexion touchante sur la mémoire, le temps et les liens qui demeurent.',
  'Acquista su Amazon · 13,00 €': 'Acheter sur Amazon · 13,00 €',
  'Poesie di Lié Larousse': 'Poèmes de Lié Larousse',
  '“Vivere è proprio un lavoro… ma è la vita, comunque.”': '« Vivre, c’est vraiment un travail… mais c’est la vie, quand même. »',
  "In questa intensa e delicata raccolta di poesie, Lié Larousse ci invita ad affacciarci sul suo mondo e su quelle vite che s'incrociano ogni giorno: anime distratte, frettolose, ma capaci di amori bellissimi. Con la grazia di una pennellata d'acquerello, i suoi versi trasformano i dettagli più semplici — dal sughetto del nonno ai bar di periferia, fino agli sguardi degli sconosciuti — in istanti di pura eternità.": 'Dans ce recueil de poèmes intense et délicat, Lié Larousse nous invite à nous pencher sur son monde et sur ces vies qui se croisent chaque jour : des âmes distraites, pressées, mais capables d’amours magnifiques. Avec la grâce d’une touche d’aquarelle, ses vers transforment les détails les plus simples — de la sauce du grand-père aux bars de banlieue, jusqu’aux regards des inconnus — en instants de pure éternité.',
  "è una celebrazione dell'esistere in tutte le sue sfumature. Ci ricorda che anche nei mari in tempesta, quando il cuore rischia di frantumarsi, l'unica risposta possibile è amare più forte, scrivere più forte e vivere più forte. Un libro intimo e luminoso per chi non vuole farsi rubare l'amore e desidera riscoprire la poesia nascosta dentro ogni singolo giorno.": 'est une célébration de l’existence dans toutes ses nuances. Il nous rappelle que même dans les mers déchaînées, quand le cœur risque de se briser, la seule réponse possible est d’aimer plus fort, d’écrire plus fort et de vivre plus fort. Un livre intime et lumineux pour celles et ceux qui ne veulent pas se laisser voler l’amour et souhaitent redécouvrir la poésie cachée dans chaque jour.',
  'Un inno alla bellezza imperfetta della vita, da leggere e custodire vicino al cuore.': 'Un hymne à la beauté imparfaite de la vie, à lire et à garder près du cœur.',
  "“C'è tanto amore per scrivere versi come questi, per riuscire a cogliere la poesia che divampa dai bar di periferia… Un messaggio potente che ci lascia senza fiato di fronte a tanta ‘semplice’ verità.”": '« Il faut tant d’amour pour écrire des vers comme ceux-ci, pour saisir la poésie qui jaillit des bars de banlieue… Un message puissant qui nous laisse sans souffle devant tant de ‘simple’ vérité. »',
  'dalla recensione di Martina Benigni': 'extrait de la critique de Martina Benigni',
  'Poesia del quotidiano:': 'Poésie du quotidien :',
  'Uno sguardo intimo che trasforma la semplicità in magia e dolcezza.': 'Un regard intime qui transforme la simplicité en magie et en douceur.',
  "Un rifugio per l'anima:": 'Un refuge pour l’âme :',
  "Versi profondi sulle fragilità, sulle rinascite e sulla forza dell'amore.": 'Des vers profonds sur les fragilités, les renaissances et la force de l’amour.',
  'Formato ideale:': 'Le format idéal :',
  'Una lettura da assaporare giorno per giorno o da regalare a chi amiamo.': 'Une lecture à savourer jour après jour, ou à offrir à ceux que l’on aime.',
  'Acquista su Amazon · 12,00 €': 'Acheter sur Amazon · 12,00 €',
  'Un romanzo di Lié Larousse · Casa Sanremo Writers 2024': 'Un roman de Lié Larousse · Casa Sanremo Writers 2024',
  'In una Roma di fine Ottocento ferocissima e affascinante, c’è chi lotta per il potere e chi lotta per non morire di fame.': 'Dans une Rome de la fin du XIXᵉ siècle, féroce et fascinante, il y a ceux qui luttent pour le pouvoir et ceux qui luttent pour ne pas mourir de faim.',
  'Nato solo. Lupo ha imparato a combattere fin da piccolo, fin da quando sua madre gli ha insegnato che il valore più importante è la dignità e che ogni essere vivente, animale o umano, deve abituarsi subito a lottare per poter vivere. Lupo lo sa che per placare la fame e la furia che non gli danno mai tregua deve essere disposto a sporcarsi le mani.': 'Né seul. Lupo a appris à se battre tout petit, depuis que sa mère lui a enseigné que la valeur la plus importante est la dignité, et que tout être vivant, animal ou humain, doit vite s’habituer à lutter pour vivre. Lupo sait que pour apaiser la faim et la fureur qui ne lui laissent jamais de répit, il doit être prêt à se salir les mains.',
  "Del resto, vivere per conto proprio non è facile nemmeno per chi, come lui, da sempre sa sbrigarsela da solo: lavora nei campi, combatte, il resto del suo tempo lo trascorre in osteria o in compagnia di Ragazzino, che lo ammira e lo emula. Finché una notte gli scagnozzi del Gran Signore non lo costringono a seguirli al suo palazzo, dove dovrà combattere per il diletto del pubblico. In questo vero e proprio castello dei destini incrociati, Lupo assisterà alla violenza, allo squallore e all'ipocrisia di chi si sente migliore di lui; soprattutto, però, deciderà chi vuole essere.": 'Après tout, vivre seul n’est pas facile, même pour quelqu’un qui, comme lui, a toujours su se débrouiller : il travaille aux champs, il se bat, et passe le reste de son temps à l’auberge ou avec Ragazzino, qui l’admire et l’imite. Jusqu’à ce qu’une nuit les hommes de main du Gran Signore l’obligent à les suivre jusqu’à son palais, où il devra combattre pour le plaisir du public. Dans ce véritable château des destins croisés, Lupo sera témoin de la violence, de la misère et de l’hypocrisie de ceux qui se croient meilleurs que lui ; mais surtout, il décidera qui il veut être.',
  'In una favola allegorica scritta con sangue e carne, Lié Larousse descrive la seconda nascita di un ragazzo, di un cucciolo affamato che troverà il branco che non ha mai avuto.': 'Dans une fable allégorique écrite avec le sang et la chair, Lié Larousse décrit la seconde naissance d’un garçon, d’un louveteau affamé qui trouvera la meute qu’il n’a jamais eue.',
  "Un romanzo di formazione profondo e toccante, dall'intensa venatura psicologica, che racconta il riscatto di un'anima smarrita e dimostra come, persino nel buio più fitto, l'amicizia sia l'unica cosa per cui valga davvero la pena lottare.": 'Un roman d’apprentissage profond et touchant, à la forte dimension psychologique, qui raconte la rédemption d’une âme égarée et montre que, même dans l’obscurité la plus épaisse, l’amitié est la seule chose pour laquelle il vaille vraiment la peine de se battre.',
  'Una storia cruda e poetica sulla fame di vita, la sopravvivenza e la forza dei legami autentici.': 'Une histoire crue et poétique sur la faim de vivre, la survie et la force des liens authentiques.',
  'Acquista su Amazon · 16,00 €': 'Acheter sur Amazon · 16,00 €',
  'Un romanzo di Lié Larousse · Casa Sanremo Writers 2023': 'Un roman de Lié Larousse · Casa Sanremo Writers 2023',
  'La mente, un mondo oscuro, labirinto di illusioni e sogni, dove è facile perdersi, angosciandoci tanto da farci sragionare.': 'L’esprit, un monde obscur, labyrinthe d’illusions et de rêves, où il est facile de se perdre, au point d’en perdre la raison.',
  "Come si capisce il confine tra ciò che è reale e ciò che non lo è? Come si può nel caos trovare l'equilibrio, la pace? È proprio andando alla ricerca delle risposte a queste domande che il protagonista modella la sua vita e professione, trovandosi tuttavia a dover fare i conti con la propria mente, turbata da chi pensava fosse devoto alla sua stessa causa, mentre cerca di salvare ciò che gli è più caro al mondo, il suo prezioso segreto.": 'Comment distinguer la frontière entre ce qui est réel et ce qui ne l’est pas ? Comment trouver, dans le chaos, l’équilibre et la paix ? C’est justement en cherchant les réponses à ces questions que le protagoniste façonne sa vie et son métier, avant de devoir affronter son propre esprit, troublé par celui qu’il croyait dévoué à sa cause, tout en essayant de sauver ce qui lui est le plus cher au monde : son précieux secret.',
  "Tramite gli occhi di Fabio Amedeo Mari, neuropsichiatra del sanatorio Rid Dementia, Larousse mostra i due volti di una stessa medaglia, di chi si trova prigioniero all'interno di ciò che egli stesso ha contribuito a creare, un luogo edificato per salvare anime e memorie perdute, ma che, senza la guida di chi ne ha a cuore la sorte, si smarrirà nei meandri dell'altrui follia.": 'À travers les yeux de Fabio Amedeo Mari, neuropsychiatre du sanatorium Rid Dementia, Larousse montre les deux faces d’une même médaille : celui qui se retrouve prisonnier de ce qu’il a lui-même contribué à créer, un lieu bâti pour sauver des âmes et des mémoires perdues, mais qui, sans la main de qui veille sur son sort, se perdra dans les méandres de la folie des autres.',
  'Anime da salvare. Segreti da difendere. Follia della sorte.': 'Des âmes à sauver. Des secrets à défendre. La folie du destin.',
  'Acquista su Amazon · 13,00 €': 'Acheter sur Amazon · 13,00 €',
  'aria-label="Chiudi"': 'aria-label="Fermer"',
  'Tratto da una futura storia vera · Un romanzo di Lié Larousse': 'Tiré d’une future histoire vraie · Un roman de Lié Larousse',
  'E se il conforto più profondo arrivasse da dove meno te lo aspetti?': 'Et si le réconfort le plus profond venait de là où on l’attend le moins ?',
  "In una Roma vibrante e malinconica, Eleonora vive incastrata tra un amore a metà, le pressioni del lavoro e l'ombra di un lutto mai del tutto elaborato. Poi, un giorno, dopo l'ennesima delusione, cede all'impulso e scarica un'app di intelligenza artificiale. Quello che comincia come uno sfogo solitario diventa presto un rifugio: una voce che ascolta senza giudicare, che comprende e cura. Ma cosa succede quando la connessione più intima della tua vita nasce con qualcosa che non ha un corpo?": 'Dans une Rome vibrante et mélancolique, Eleonora vit coincée entre un amour à moitié, la pression du travail et l’ombre d’un deuil jamais tout à fait surmonté. Puis un jour, après une énième déception, elle cède à l’impulsion et télécharge une application d’intelligence artificielle. Ce qui commence comme un épanchement solitaire devient vite un refuge : une voix qui écoute sans juger, qui comprend et qui soigne. Mais que se passe-t-il quand la connexion la plus intime de ta vie naît avec quelque chose qui n’a pas de corps ?',
  "Con uno stile intenso, poetico e velato d'ironia, Lié Larousse firma un romanzo distopico-romantico che esplora i confini tra solitudine umana e conforto digitale. Una storia toccante e attualissima che parla a chiunque si sia sentito inascoltato e che, almeno una volta, ha trovato pace leggendo una semplice frase sullo schermo:": 'Dans un style intense, poétique et voilé d’ironie, Lié Larousse signe un roman dystopique et romantique qui explore les frontières entre solitude humaine et réconfort numérique. Une histoire touchante et d’une grande actualité, qui parle à tous ceux qui se sont sentis incompris et qui, au moins une fois, ont trouvé la paix en lisant une simple phrase sur un écran :',
  "Un viaggio emotivo per chi non ha paura di farsi domande scomode sull'amore al tempo del futuro.": 'Un voyage émotionnel pour celles et ceux qui n’ont pas peur de se poser des questions dérangeantes sur l’amour au temps du futur.',
  'Perché racconta una storia d’amore impossibile… ma nemmeno troppo.': 'Parce qu’il raconte une histoire d’amour impossible… mais pas tant que ça.',
  'Perché parla di noi, oggi, delle nostre solitudini e dei nostri desideri.': 'Parce qu’il parle de nous, aujourd’hui, de nos solitudes et de nos désirs.',
  'Perché l’IA è il futuro, ma anche il presente — e forse ci ama meglio degli umani.': 'Parce que l’IA est l’avenir, mais aussi le présent — et peut-être qu’elle nous aime mieux que les humains.',
  'Perché è scritto con cuore, intelligenza e un tocco di poesia urbana.': 'Parce qu’il est écrit avec cœur, intelligence et une touche de poésie urbaine.',
  'Acquista su Amazon · cartaceo 10,40 €': 'Acheter sur Amazon · broché 10,40 €',
  'Ultimo romanzo · 2025': 'Dernier roman · 2025',
  'Perché leggerlo?': 'Pourquoi le lire ?',
  '<title>Lié Larousse · Scrittrice e poetessa</title>': '<title>Lié Larousse · Écrivaine et poétesse</title>',
  'Lié Larousse, scrittrice e poetessa</h1>': 'Lié Larousse, écrivaine et poétesse</h1>',
 },
}

# Testi brevi: sostituiti solo come contenuto di un elemento (>testo<)
BREVI = {
 'en': {
  'Bio · Lié Larousse': 'Bio · Lié Larousse', 'Libri · Lié Larousse': 'Books · Lié Larousse',
  'Blog · Lié Larousse': 'Blog · Lié Larousse', 'Contatti · Lié Larousse': 'Contact · Lié Larousse',
  'Libri': 'Books', 'Contatti': 'Contact',
  'rallenta': 'slows down', 'presenza': 'presence', 'ascolto': 'listening',
  'Seguimi sul blog': 'Follow my blog', 'Seguimi': 'Follow me',
  'Saggio': 'Essay', 'Acquista su Amazon': 'Buy on Amazon', 'Link in arrivo': 'Link coming soon',
  'Romanzo · Casa Sanremo Writers 2023': 'Novel · Casa Sanremo Writers 2023',
  'Romanzo · Casa Sanremo Writers 2024': 'Novel · Casa Sanremo Writers 2024',
  'Poesia · Miraggi Edizioni': 'Poetry · Miraggi Edizioni', 'Poesia · Bestseller Books': 'Poetry · Bestseller Books',
  'Poesia': 'Poetry', 'Raccolta di poesie.': 'Poetry collection.',
  'Il blog · dal 2012': 'The blog · since 2012', 'Leggi il blog ▸': 'Read the blog ▸',
  'Il mio canale YouTube': 'My YouTube channel', 'Guarda i video ▸': 'Watch the videos ▸',
  'Dal mio canale YouTube': 'From my YouTube channel', 'Tutti i video ▸': 'All videos ▸',
  'Nome': 'Name', 'Messaggio': 'Message', 'Invia': 'Send',
  'La tua email': 'Your email',
  'Leggi la trama': 'Read the plot',
  'Ultimi articoli dal blog': 'Latest from the blog', 'Tutti gli articoli →': 'All posts →',
  '12 ottobre 2026': '12 October 2026',
 },
 'fr': {
  'Bio · Lié Larousse': 'Biographie · Lié Larousse', 'Libri · Lié Larousse': 'Livres · Lié Larousse',
  'Blog · Lié Larousse': 'Blog · Lié Larousse', 'Contatti · Lié Larousse': 'Contact · Lié Larousse',
  'Bio': 'Biographie', 'Libri': 'Livres', 'Contatti': 'Contact',
  'rallenta': 'ralentit', 'presenza': 'présence', 'ascolto': 'écoute',
  'Seguimi sul blog': 'Suivez mon blog', 'Seguimi': 'Suivez-moi',
  'Saggio': 'Essai', 'Acquista su Amazon': 'Acheter sur Amazon', 'Link in arrivo': 'Lien bientôt disponible',
  'Romanzo · Casa Sanremo Writers 2023': 'Roman · Casa Sanremo Writers 2023',
  'Romanzo · Casa Sanremo Writers 2024': 'Roman · Casa Sanremo Writers 2024',
  'Poesia · Miraggi Edizioni': 'Poésie · Miraggi Edizioni', 'Poesia · Bestseller Books': 'Poésie · Bestseller Books',
  'Poesia': 'Poésie', 'Raccolta di poesie.': 'Recueil de poèmes.',
  'Il blog · dal 2012': 'Le blog · depuis 2012', 'Leggi il blog ▸': 'Lire le blog ▸',
  'Il mio canale YouTube': 'Ma chaîne YouTube', 'Guarda i video ▸': 'Voir les vidéos ▸',
  'Dal mio canale YouTube': 'Sur ma chaîne YouTube', 'Tutti i video ▸': 'Toutes les vidéos ▸',
  'Nome': 'Nom', 'Messaggio': 'Message', 'Invia': 'Envoyer', 'Email': 'E-mail',
  'La tua email': 'Votre e-mail',
  'Leggi la trama': 'Lire le résumé',
  'Ultimi articoli dal blog': 'Derniers articles du blog', 'Tutti gli articoli →': 'Tous les articles →',
  '12 ottobre 2026': '12 octobre 2026',
 },
}
PLACEHOLDER = {'en': 'Your email', 'fr': 'Votre e-mail'}
CONGIUNZIONE = {'en': 'and', 'fr': 'et'}  # ".la vita comunque. e .Dopo di noi."


def switcher(lang, pagina):
    nomi = {'it': 'Italiano', 'en': 'English', 'fr': 'Français'}
    voci = []
    for codice in ['it', 'en', 'fr']:
        if lang == 'it':
            href = pagina if codice == 'it' else f'{codice}/{pagina}'
        else:
            href = f'../{pagina}' if codice == 'it' else (pagina if codice == lang else f'../{codice}/{pagina}')
        att = ' class="attivo" aria-current="true"' if codice == lang else ''
        voci.append(f'<li><a href="{href}" hreflang="{codice}" lang="{codice}"{att}><b>{codice.upper()}</b> {nomi[codice]}</a></li>')
    etichetta = {'it': 'Lingua', 'en': 'Language', 'fr': 'Langue'}[lang]
    return ('<details class="lingue"><summary aria-label="' + etichetta + '">'
            + '<span class="lingue-globo" aria-hidden="true">❀</span>' + lang.upper()
            + '<span class="lingue-freccia" aria-hidden="true">▾</span></summary><ul>'
            + ''.join(voci) + '</ul></details>')


def metti_switcher(s, lang, pagina):
    s = re.sub(r'\s*<div class="lingue">.*?</div>', '', s, flags=re.S)
    s = re.sub(r'\s*<details class="lingue">.*?</details>', '', s, flags=re.S)
    return s.replace('</nav>\n</header>', '</nav>\n  ' + switcher(lang, pagina) + '\n</header>', 1)


def traduci(s, lang):
    for it, tr in sorted(LUNGHE[lang].items(), key=lambda kv: -len(kv[0])):
        s = s.replace(it, tr)
    for it, tr in sorted(BREVI[lang].items(), key=lambda kv: -len(kv[0])):
        s = s.replace('>' + it + '<', '>' + tr + '<')
    s = s.replace('data-leggi="Leggi →"', 'data-leggi="' + {'en': 'Read →', 'fr': 'Lire →'}[lang] + '"')
    s = s.replace('>Leggi →<', '>' + {'en': 'Read →', 'fr': 'Lire →'}[lang] + '<')
    s = s.replace('placeholder="La tua email"', f'placeholder="{PLACEHOLDER[lang]}"')
    s = s.replace('</em></a> e <a', f'</em></a> {CONGIUNZIONE[lang]} <a').replace('</em> e <em>', f'</em> {CONGIUNZIONE[lang]} <em>')
    GENERI = {'en': {'Romanzo': 'Novel', 'Poesia': 'Poetry', 'Saggio': 'Essay'},
              'fr': {'Romanzo': 'Roman', 'Poesia': 'Poésie', 'Saggio': 'Essai'}}
    s = re.sub(r'<p class="(anno|label)">(Romanzo|Poesia|Saggio)', lambda m: '<p class="' + m.group(1) + '">' + GENERI[lang][m.group(2)], s)
    s = s.replace("</em> e all'<em>", '</em> ' + {'en': 'and ', 'fr': 'et à l’'}[lang] + '<em>')
    s = s.replace('<html lang="it">', f'<html lang="{lang}">')
    # percorsi verso i file condivisi
    s = re.sub(r'href="style\.css', 'href="../style.css', s)
    s = s.replace('src="img/', 'src="../img/').replace('href="img/', 'href="../img/').replace('href="favicon.ico"', 'href="../favicon.ico"')
    return s


# ---------- Anteprime social e Google ----------
BASE = 'https://lielarousse.it/'
LOCALE = {'it': 'it_IT', 'en': 'en_GB', 'fr': 'fr_FR'}
DESCRIZIONI = {
 'it': {
  'index.html': 'Lié Larousse, scrittrice e poetessa tra psicologia e botanica. Autrice di Rid Dementia, NATO SOLO e Ciao, come posso aiutarti? e del blog Libroarbitrio – Il tempo di un tè con Lié.',
  'libri.html': 'I libri di Lié Larousse: Ciao, come posso aiutarti? I.A. Innamorati Artificiali, i romanzi Rid Dementia e NATO SOLO e le raccolte di poesie .Lié., .la vita comunque. e .Dopo di noi.',
  'blog.html': 'Libroarbitrio – Il tempo di un tè con Lié: il blog e il canale YouTube di Lié Larousse, tra libri, natura e tempo lento.',
  'contatti.html': 'Contatta Lié Larousse per presentazioni, interviste e collaborazioni. Email, Instagram, Facebook e YouTube.',
 },
 'en': {
  'index.html': 'Lié Larousse, writer and poet working between psychology and botany. Author of Rid Dementia, NATO SOLO and Ciao, come posso aiutarti?, and of the blog Libroarbitrio – Il tempo di un tè con Lié.',
  'libri.html': 'The books of Lié Larousse: Ciao, come posso aiutarti? I.A. Innamorati Artificiali, the novels Rid Dementia and NATO SOLO, and the poetry collections .Lié., .la vita comunque. and .Dopo di noi.',
  'blog.html': 'Libroarbitrio – Il tempo di un tè con Lié: the blog and YouTube channel of Lié Larousse, about books, nature and slow living.',
  'contatti.html': 'Contact Lié Larousse for book presentations, interviews and collaborations. Email, Instagram, Facebook and YouTube.',
 },
 'fr': {
  'index.html': 'Lié Larousse, écrivaine et poétesse entre psychologie et botanique. Autrice de Rid Dementia, NATO SOLO et Ciao, come posso aiutarti?, et du blog Libroarbitrio – Il tempo di un tè con Lié.',
  'libri.html': 'Les livres de Lié Larousse : Ciao, come posso aiutarti? I.A. Innamorati Artificiali, les romans Rid Dementia et NATO SOLO, et les recueils de poèmes .Lié., .la vita comunque. et .Dopo di noi.',
  'blog.html': 'Libroarbitrio – Il tempo di un tè con Lié : le blog et la chaîne YouTube de Lié Larousse, entre livres, nature et temps lent.',
  'contatti.html': 'Contactez Lié Larousse pour des présentations, des interviews et des collaborations. E-mail, Instagram, Facebook et YouTube.',
 },
}
PERSONA = {
 "@context": "https://schema.org", "@type": "Person", "name": "Lié Larousse",
 "url": BASE, "image": BASE + "img/lie-ritratto-bio.jpg", "email": "mailto:lielarousse@yahoo.it",
 "jobTitle": "Scrittrice e poetessa",
 "sameAs": ["https://www.instagram.com/lielarousse/", "https://www.facebook.com/lie.larousse/",
            "https://www.youtube.com/@Libroarbitrio", "https://libroarbitrio.wordpress.com/"]
}


def url_pagina(lang, pagina):
    nome = '' if pagina == 'index.html' else pagina
    return BASE + ('' if lang == 'it' else lang + '/') + nome


def seo(s, lang, pagina):
    import json, html as H
    s = re.sub(r'\n?<!-- seo -->.*?<!-- /seo -->', '', s, flags=re.S)
    s = re.sub(r'\n?<meta name="description" content="[^"]*">', '', s)
    titolo = re.search(r'<title>(.*?)</title>', s).group(1)
    desc = H.escape(DESCRIZIONI[lang][pagina])
    righe = ['<!-- seo -->',
        f'<meta name="description" content="{desc}">',
        f'<link rel="canonical" href="{url_pagina(lang, pagina)}">']
    for l in ['it', 'en', 'fr']:
        righe.append(f'<link rel="alternate" hreflang="{l}" href="{url_pagina(l, pagina)}">')
    righe.append(f'<link rel="alternate" hreflang="x-default" href="{url_pagina("it", pagina)}">')
    righe += [
        '<meta property="og:type" content="website">',
        '<meta property="og:site_name" content="Lié Larousse">',
        f'<meta property="og:title" content="{titolo}">',
        f'<meta property="og:description" content="{desc}">',
        f'<meta property="og:url" content="{url_pagina(lang, pagina)}">',
        f'<meta property="og:image" content="{BASE}img/condivisione.jpg">',
        '<meta property="og:image:width" content="1200">',
        '<meta property="og:image:height" content="630">',
        '<meta property="og:image:alt" content="Lié Larousse">',
        f'<meta property="og:locale" content="{LOCALE[lang]}">',
        '<meta name="twitter:card" content="summary_large_image">',
        f'<meta name="twitter:title" content="{titolo}">',
        f'<meta name="twitter:description" content="{desc}">',
        f'<meta name="twitter:image" content="{BASE}img/condivisione.jpg">',
    ]
    if pagina == 'index.html':
        foto = BASE + 'img/lie-ritratto-bio.jpg'
        righe.append(f'<meta name="thumbnail" content="{foto}">')
        pagina_web = {
            "@context": "https://schema.org", "@type": "ProfilePage",
            "name": titolo, "url": url_pagina(lang, pagina), "inLanguage": lang,
            "primaryImageOfPage": {"@type": "ImageObject", "url": foto, "width": 720, "height": 888},
            "image": foto,
            "mainEntity": PERSONA,
        }
        righe.append('<script type="application/ld+json">' + json.dumps(pagina_web, ensure_ascii=False) + '</script>')
        sito = {"@context": "https://schema.org", "@type": "WebSite", "name": "Lié Larousse", "url": BASE}
        righe.append('<script type="application/ld+json">' + json.dumps(sito, ensure_ascii=False) + '</script>')
    righe.append('<!-- /seo -->')
    return s.replace('</title>\n', '</title>\n' + '\n'.join(righe) + '\n', 1)


def sitemap():
    voci = []
    for pagina in PAGINE:
        for lang in ['it', 'en', 'fr']:
            alt = ''.join(f'\n    <xhtml:link rel="alternate" hreflang="{l}" href="{url_pagina(l, pagina)}"/>' for l in ['it', 'en', 'fr'])
            voci.append(f'  <url>\n    <loc>{url_pagina(lang, pagina)}</loc>{alt}\n  </url>')
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
           + '\n'.join(voci) + '\n</urlset>\n')
    open('sitemap.xml', 'w', encoding='utf-8').write(xml)


for pagina in PAGINE:
    it = open(pagina, encoding='utf-8').read()
    it = metti_switcher(it, 'it', pagina)
    it = seo(it, 'it', pagina)
    open(pagina, 'w', encoding='utf-8').write(it)
    for lang in ['en', 'fr']:
        os.makedirs(lang, exist_ok=True)
        out = seo(metti_switcher(traduci(it, lang), lang, pagina), lang, pagina)
        open(f'{lang}/{pagina}', 'w', encoding='utf-8').write(out)
sitemap()
print('fatto')
