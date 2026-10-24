# Genera le versioni inglese (en/) e francese (fr/) del sito dalle pagine italiane.
# Uso: python3 _strumenti/traduci.py  (dalla cartella principale del sito)
import re, os

PAGINE = ['index.html', 'libri.html', 'arte.html', 'blog.html', 'contatti.html']

# Frasi lunghe: sostituite ovunque compaiano
LUNGHE = {
 'en': {
  'Lié Larousse, scrittrice. Libri, racconti dal giardino e Libroarbitrio, il tempo di un tè con Lié.': 'Lié Larousse, writer. Books, stories from the garden and Libroarbitrio, tea time with Lié.',
  'Ci sono luoghi dentro di noi dove il tempo': 'There are places within us where time',
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
  "Poesie di Lié Larousse · Opera d'esordio": 'Poems by Lié Larousse · Debut work',
  'Una silloge poetica intensamente intima e ritmica.': 'An intensely intimate and rhythmic collection of poems.',
  "<em>.Lié.</em> è un'opera letteraria d'esordio che porta il nome della sua autrice, una silloge poetica intensamente intima e ritmica. Tra gioco linguistico, musicalità e visione, la parola scritta si fa performance: un viaggio tra le pieghe dell'anima, le vulnerabilità e l'incanto quotidiano.": '<em>.Lié.</em> is a debut literary work that bears its author’s name, an intensely intimate and rhythmic collection of poems. Between wordplay, musicality and vision, the written word becomes performance: a journey through the folds of the soul, its vulnerabilities and everyday enchantment.',
  'Un libro che seduce e risuona come un canto antico e contemporaneo al tempo stesso.': 'A book that seduces and resonates like a song both ancient and contemporary.',
  '>Non disponibile<': '>Not available<',
  "Creare con le mani è un atto di preghiera e di risveglio. Quando la mente tace e le mani plasmano la carta, tracciano una parola a inchiostro, rilegano un diario, colano la cera di una candela per un rituale o dispongono sul tavolo le <strong>Carte dei Nat per dialogare con gli archetipi e gli antenati</strong>, Anima trova finalmente lo spazio per raccontarsi. Nella mia visione, <strong>la Craft Art è una via meditativa</strong> per ritrovare noi stessi dove ci siamo dimenticati: con gesti semplici pieni d'amore.": 'Creating with our hands is an act of prayer and awakening. When the mind falls silent and the hands shape paper, trace a word in ink, bind a journal, pour the wax of a candle for a ritual or lay out on the table the <strong>Nat Cards to dialogue with archetypes and ancestors</strong>, Soul finally finds room to tell its story. In my vision, <strong>Craft Art is a meditative path</strong> to find ourselves again where we have forgotten ourselves: with simple gestures full of love.',
  "<strong>Nel mio fare Anima</strong>, la creazione manuale si ispira alla filosofia artigianale nata nel periodo vittoriano, un'epoca che amo profondamente per il suo <em>ritorno alla purezza della materia, alla cura del dettaglio e al rispetto dei ritmi naturali</em>. Per me la Craft Art non è un semplice esercizio estetico, ma uno strumento vivo che intreccio al mio percorso di scrittrice e ricercatrice, utilizzandolo come canale d'elezione nei miei percorsi di risveglio della mente.": '<strong>In my soul-making</strong>, handcraft draws on the artisan philosophy born in the Victorian era, a time I deeply love for its <em>return to the purity of materials, care for detail and respect for natural rhythms</em>. For me Craft Art is not a mere aesthetic exercise, but a living tool that I weave into my path as a writer and researcher, using it as a favoured channel in my journeys of awakening the mind.',
  'Ogni foglio di carta fatto a mano, ogni calligrafia, ogni quaderno rilegato, ogni candela poetica e la lettura immaginale delle Carte dei Nat sono tesori dedicati a chi desidera radicarsi nel presente, custodendone le memorie e la poesia.': 'Every sheet of handmade paper, every piece of calligraphy, every bound notebook, every poetic candle and the imaginal reading of the Nat Cards are treasures for those who wish to root themselves in the present, keeping its memories and its poetry.',
  "Ti invito a rallentare il passo e a sfogliare con gli occhi questi tesori. Che tu desideri un'opera unica creata su misura o voglia scrivermi per iniziare insieme un percorso di “fare Anima” attraverso l'arte, la materia e il simbolo, questo è il tuo rifugio.": 'I invite you to slow your pace and leaf through these treasures with your eyes. Whether you would like a unique piece made to measure or wish to write to me to begin a journey of “soul-making” together through art, matter and symbol, this is your refuge.',
  'I miei 6 tesori per fare Anima': 'My 6 treasures for soul-making',
  '>Scrivimi<': '>Write to me<',
  '<strong>La Carta Fatta a Mano</strong>': '<strong>Handmade Paper</strong>',
  '<h2>La Carta Fatta a Mano</h2>': '<h2>Handmade Paper</h2>',
  '<strong>Carta Fatta a Mano</strong>': '<strong>Handmade Paper</strong>',
  '<h2>Carta Fatta a Mano</h2>': '<h2>Handmade Paper</h2>',
  '<strong>Dedicopoesie & Calligrafia</strong>': '<strong>Dedication Poems & Calligraphy</strong>',
  '<h2>Dedicopoesie & Calligrafia</h2>': '<h2>Dedication Poems & Calligraphy</h2>',
  '<strong>Quaderni e brevi Fiabe Rilegate e Scritte a Mano</strong>': '<strong>Notebooks and Short Fairy Tales, Hand-bound and Handwritten</strong>',
  '<h2>Quaderni e brevi Fiabe Rilegate e Scritte a Mano</h2>': '<h2>Notebooks and Short Fairy Tales, Hand-bound and Handwritten</h2>',
  '<strong>Diario Creativo & Scrapbooking</strong>': '<strong>Creative Journal & Scrapbooking</strong>',
  '<h2>Diario Creativo & Scrapbooking</h2>': '<h2>Creative Journal & Scrapbooking</h2>',
  '<strong>Candele Poetiche & Rituali</strong>': '<strong>Poetic Candles & Rituals</strong>',
  '<h2>Candele Poetiche & Rituali</h2>': '<h2>Poetic Candles & Rituals</h2>',
  '<strong>Lettura Immaginale con le Carte dei Nat</strong>': '<strong>Imaginal Reading with the Nat Cards</strong>',
  '<h2>Lettura Immaginale con le Carte dei Nat</h2>': '<h2>Imaginal Reading with the Nat Cards</h2>',
  '>Materia che accoglie e custodisce pensieri<': '>Matter that welcomes and keeps thoughts<',
  ">L'incanto delle parole scritte a stilografica e pennino, per celebrare l'anima<": '>The enchantment of words written with fountain pen and nib, to celebrate the soul<',
  ">L'incanto delle parole scritte a stilografica e pennino per celebrare Anima<": '>The enchantment of words written with fountain pen and nib to celebrate the Soul<',
  '>Scrigni per il nostro bambino adulto, custodi della felicità di stringere tra le mani piccoli tesori<': '>Treasure chests for our adult child, keepers of the joy of holding little treasures in our hands<',
  '>Spazi di ascolto, libera espressione e risveglio della mente<': '>Spaces for listening, free expression and awakening of the mind<',
  '>Spazio di ascolto, libera espressione e risveglio della mente<': '>A space for listening, free expression and awakening of the mind<',
  '>Fiamme di luce per custodire intenzioni e fare spazio al silenzio<': '>Flames of light to hold intentions and make room for silence<',
  '>Uno strumento di ascolto, dialogo con gli antenati e pacificazione interiore<': '>A tool for listening, dialogue with the ancestors and inner peace<',
  "Nata dall'incontro lento tra acqua, fibre e gesti antichi, la carta fatta a mano è una superficie viva. Ogni foglio conserva piccole imperfezioni, sfumature e bordi sfilacciati che raccontano di pazienza e presenza. Non è solo un supporto per scrivere, ma una materia che respira: un grembo delicato pronto ad accogliere le intenzioni, le memorie e i pensieri più puri. Ci sono parole che si scrivono con l'inchiostro e altre che si intrecciano con la materia. Qui la carta prende forma in racconti che diventano scrigni di stoffa e carta, e il gesto manuale si fa meditazione.": 'Born from the slow meeting of water, fibres and ancient gestures, handmade paper is a living surface. Every sheet keeps small imperfections, nuances and deckled edges that speak of patience and presence. It is not just something to write on, but a material that breathes: a delicate womb ready to welcome the purest intentions, memories and thoughts. There are words written in ink and others woven into matter. Here paper takes shape in stories that become little chests of fabric and paper, and the work of the hands becomes meditation.',
  "L'inchiostro traccia solchi leggeri sul foglio, trasformando il pensiero in un segno visibile e sacro. Le Dedicopoesie nascono dall'ascolto e prendono forma attraverso il ritmo lento della mia stilografica. Ogni parola tracciata a mano diventa un'opera unica, un dono visivo nato per celebrare un momento, un legame o una rinascita di Anima.": 'Ink traces light furrows on the page, turning thought into a visible, sacred sign. Dedication poems are born from listening and take shape through the slow rhythm of my fountain pen. Every word traced by hand becomes a unique work, a visual gift created to celebrate a moment, a bond or a rebirth of the Soul.',
  "Cuciti e rilegati con cura artigianale, questi quaderni e piccoli racconti scritti a mano nascono per dare voce al nostro bambino adulto. Sono un invito a ritrovare la meraviglia e la gioia pura di quando, da piccoli, custodivamo tra le mani i nostri tesori più segreti. Piccoli libri d'affezione, fatti per ricordare che la bellezza dell'incanto non ha età.": 'Sewn and bound with artisan care, these notebooks and little handwritten stories are made to give a voice to our adult child. They invite us to rediscover the wonder and pure joy of the days when, as children, we held our most secret treasures in our hands. Little books of affection, made to remind us that the beauty of enchantment has no age.',
  "Il diario creativo è un rifugio in cui la parola incontra la materia, il colore e le immagini dell'anima. Attraverso lo scrapbooking e il gesto manuale, la mente rallenta, il giudizio tace e la creatività diventa una pratica di meditazione e risveglio interiore. È uno spazio intimo dove dare forma alle emozioni ma anche un luogo del cuore aperto per il futuro: una traccia viva in cui tornare nei momenti bui e tristi che a volte la vita ci porta a vivere, per ritrovare la strada, fare luce e ricordarsi di sé.": 'The creative journal is a refuge where words meet matter, colour and the images of the soul. Through scrapbooking and handwork, the mind slows down, judgement falls silent and creativity becomes a practice of meditation and inner awakening. It is an intimate space to give shape to emotions, but also a place of the heart open to the future: a living trace to return to in the dark and sad moments life sometimes brings, to find the way again, shed light and remember who we are.',
  "Create a mano con cere naturali, essenze e dettagli botanici, le candele poetiche nascono per accompagnare i momenti dedicati a sé e i piccoli rituali quotidiani. La loro fiamma non serve solo a illuminare una stanza, ma a fare luce dentro: un punto di fuoco e calore attorno al quale raccogliersi per meditare, scrivere, affidare un'intenzione al tempo e ritrovare la sacralità dei propri spazi interiori.": 'Handmade with natural waxes, essences and botanical details, poetic candles are created to accompany the moments we devote to ourselves and our small daily rituals. Their flame does not only light a room, but brings light within: a point of fire and warmth to gather around, to meditate, write, entrust an intention to time and rediscover the sacredness of our inner spaces.',
  'Ispirate agli spiriti della natura e al metodo immaginale, le Carte dei Nat non sono un semplice strumento di divinazione, ma uno specchio di Anima. Attraverso i loro simboli e archetipi ancestrali, la lettura diventa un incontro sacro in cui esplorare le proprie radici, sciogliere i nodi delle costellazioni familiari e ascoltare la voce guida che abita dentro di noi per ritrovare chiarezza e armonia sul proprio cammino.': 'Inspired by the nature spirits and by the imaginal method, the Nat Cards are not a simple tool of divination, but a mirror of the Soul. Through their symbols and ancestral archetypes, the reading becomes a sacred encounter in which to explore our roots, untie the knots of family constellations and listen to the guiding voice that lives within us, to find clarity and harmony on our path.',
  'alt="Fogli di carta fatta a mano su un telaio di legno, con fiori secchi"': 'alt="Sheets of handmade paper on a wooden mould, with dried flowers"',
  'alt="Buste di carta fatta a mano chiuse con sigilli di ceralacca, accanto a una stilografica"': 'alt="Handmade paper envelopes sealed with wax seals, next to a fountain pen"',
  'alt="Quaderni rilegati a mano in carta colorata, legati con lo spago"': 'alt="Hand-bound notebooks in coloured paper, tied with twine"',
  'alt="Diario creativo aperto con versi d\'autunno e adesivi ad acquerello"': 'alt="Open creative journal with autumn verses and watercolour stickers"',
  'alt="Candele in vasetti di vetro decorati con stoffe e motivi botanici"': 'alt="Candles in glass jars decorated with fabric and botanical motifs"',
  'alt="Il libro e il mazzo delle Carte dei Nat tra candele e fiori secchi"': 'alt="The book and deck of the Nat Cards among candles and dried flowers"',
  'data-copiato="Copiato!"': 'data-copiato="Copied!"',
  'data-su-richiesta="Prezzo su richiesta"': 'data-su-richiesta="Price on request"',
  'data-oggetto="Ordine dal sito: "': 'data-oggetto="Order from the website: "',
  'data-corpo="Ciao Lié, vorrei acquistare il libro «%TITOLO%».&#10;&#10;Ho pagato con: (bonifico / PayPal)&#10;&#10;Nome e cognome:&#10;Indirizzo di spedizione:&#10;CAP e città:&#10;Telefono (per il corriere):&#10;&#10;Grazie!"': 'data-corpo="Hello Lié, I would like to buy the book «%TITOLO%».&#10;&#10;I paid by: (bank transfer / PayPal)&#10;&#10;Full name:&#10;Shipping address:&#10;Postcode and city, country:&#10;Phone (for the courier):&#10;&#10;Thank you!"',
  'data-paypal-lc="IT"': 'data-paypal-lc="GB"',
  "Acquista direttamente dall'autrice": 'Buy directly from the author',
  'spese di spedizione incluse': 'shipping included',
  'Scegli come pagare:': 'Choose how to pay:',
  "Paghi in modo sicuro sul sito di PayPal, anche con carta di credito. PayPal ti chiederà l'indirizzo di spedizione.": 'Pay securely on the PayPal website, also by credit card. PayPal will ask for your shipping address.',
  '>Paga con PayPal<': '>Pay with PayPal<',
  '>Bonifico bancario<': '>Bank transfer<',
  '<dt>Intestatario</dt>': '<dt>Account holder</dt>',
  '<dt>Causale</dt>': '<dt>Reference</dt>',
  '>Copia<': '>Copy<',
  "Dopo il bonifico, inviami l'ordine con il tuo indirizzo di spedizione:": 'After the transfer, send me your order with your shipping address:',
  "Invia l'ordine via email": 'Send the order by email',
  'Per qualsiasi domanda scrivimi a': 'For any questions, write to me at',
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
  'Ci sono luoghi dentro di noi dove il tempo': 'Il existe des lieux en nous où le temps',
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
  "Poesie di Lié Larousse · Opera d'esordio": 'Poèmes de Lié Larousse · Premier ouvrage',
  'Una silloge poetica intensamente intima e ritmica.': 'Un recueil poétique intensément intime et rythmé.',
  "<em>.Lié.</em> è un'opera letteraria d'esordio che porta il nome della sua autrice, una silloge poetica intensamente intima e ritmica. Tra gioco linguistico, musicalità e visione, la parola scritta si fa performance: un viaggio tra le pieghe dell'anima, le vulnerabilità e l'incanto quotidiano.": '<em>.Lié.</em> est une première œuvre littéraire qui porte le nom de son autrice, un recueil poétique intensément intime et rythmé. Entre jeu linguistique, musicalité et vision, la parole écrite devient performance : un voyage dans les replis de l’âme, ses vulnérabilités et l’enchantement du quotidien.',
  'Un libro che seduce e risuona come un canto antico e contemporaneo al tempo stesso.': 'Un livre qui séduit et résonne comme un chant à la fois ancien et contemporain.',
  '>Non disponibile<': '>Non disponible<',
  "Creare con le mani è un atto di preghiera e di risveglio. Quando la mente tace e le mani plasmano la carta, tracciano una parola a inchiostro, rilegano un diario, colano la cera di una candela per un rituale o dispongono sul tavolo le <strong>Carte dei Nat per dialogare con gli archetipi e gli antenati</strong>, Anima trova finalmente lo spazio per raccontarsi. Nella mia visione, <strong>la Craft Art è una via meditativa</strong> per ritrovare noi stessi dove ci siamo dimenticati: con gesti semplici pieni d'amore.": 'Créer avec ses mains est un acte de prière et d’éveil. Quand l’esprit se tait et que les mains façonnent le papier, tracent un mot à l’encre, relient un journal, coulent la cire d’une bougie pour un rituel ou disposent sur la table les <strong>Cartes des Nat pour dialoguer avec les archétypes et les ancêtres</strong>, l’Âme trouve enfin l’espace pour se raconter. Dans ma vision, <strong>le Craft Art est une voie méditative</strong> pour nous retrouver là où nous nous sommes oubliés : par des gestes simples pleins d’amour.',
  "<strong>Nel mio fare Anima</strong>, la creazione manuale si ispira alla filosofia artigianale nata nel periodo vittoriano, un'epoca che amo profondamente per il suo <em>ritorno alla purezza della materia, alla cura del dettaglio e al rispetto dei ritmi naturali</em>. Per me la Craft Art non è un semplice esercizio estetico, ma uno strumento vivo che intreccio al mio percorso di scrittrice e ricercatrice, utilizzandolo come canale d'elezione nei miei percorsi di risveglio della mente.": '<strong>Dans mon travail de l’âme</strong>, la création manuelle s’inspire de la philosophie artisanale née à l’époque victorienne, une époque que j’aime profondément pour son <em>retour à la pureté de la matière, au soin du détail et au respect des rythmes naturels</em>. Pour moi, le Craft Art n’est pas un simple exercice esthétique, mais un outil vivant que j’entrelace à mon parcours d’écrivaine et de chercheuse, et que j’utilise comme canal privilégié dans mes parcours d’éveil de l’esprit.',
  'Ogni foglio di carta fatto a mano, ogni calligrafia, ogni quaderno rilegato, ogni candela poetica e la lettura immaginale delle Carte dei Nat sono tesori dedicati a chi desidera radicarsi nel presente, custodendone le memorie e la poesia.': 'Chaque feuille de papier fait main, chaque calligraphie, chaque carnet relié, chaque bougie poétique et la lecture imaginale des Cartes des Nat sont des trésors dédiés à celles et ceux qui souhaitent s’enraciner dans le présent, en gardant ses souvenirs et sa poésie.',
  "Ti invito a rallentare il passo e a sfogliare con gli occhi questi tesori. Che tu desideri un'opera unica creata su misura o voglia scrivermi per iniziare insieme un percorso di “fare Anima” attraverso l'arte, la materia e il simbolo, questo è il tuo rifugio.": 'Je vous invite à ralentir le pas et à feuilleter des yeux ces trésors. Que vous souhaitiez une œuvre unique créée sur mesure ou que vous vouliez m’écrire pour commencer ensemble un chemin de « travail de l’âme » à travers l’art, la matière et le symbole, ceci est votre refuge.',
  'I miei 6 tesori per fare Anima': 'Mes 6 trésors pour le travail de l’âme',
  '>Scrivimi<': '>Écrivez-moi<',
  '<strong>La Carta Fatta a Mano</strong>': '<strong>Le Papier Fait Main</strong>',
  '<h2>La Carta Fatta a Mano</h2>': '<h2>Le Papier Fait Main</h2>',
  '<strong>Carta Fatta a Mano</strong>': '<strong>Papier Fait Main</strong>',
  '<h2>Carta Fatta a Mano</h2>': '<h2>Papier Fait Main</h2>',
  '<strong>Dedicopoesie & Calligrafia</strong>': '<strong>Poèmes-dédicaces & Calligraphie</strong>',
  '<h2>Dedicopoesie & Calligrafia</h2>': '<h2>Poèmes-dédicaces & Calligraphie</h2>',
  '<strong>Quaderni e brevi Fiabe Rilegate e Scritte a Mano</strong>': '<strong>Carnets et Petits Contes Reliés et Écrits à la Main</strong>',
  '<h2>Quaderni e brevi Fiabe Rilegate e Scritte a Mano</h2>': '<h2>Carnets et Petits Contes Reliés et Écrits à la Main</h2>',
  '<strong>Diario Creativo & Scrapbooking</strong>': '<strong>Journal Créatif & Scrapbooking</strong>',
  '<h2>Diario Creativo & Scrapbooking</h2>': '<h2>Journal Créatif & Scrapbooking</h2>',
  '<strong>Candele Poetiche & Rituali</strong>': '<strong>Bougies Poétiques & Rituels</strong>',
  '<h2>Candele Poetiche & Rituali</h2>': '<h2>Bougies Poétiques & Rituels</h2>',
  '<strong>Lettura Immaginale con le Carte dei Nat</strong>': '<strong>Lecture Imaginale avec les Cartes des Nat</strong>',
  '<h2>Lettura Immaginale con le Carte dei Nat</h2>': '<h2>Lecture Imaginale avec les Cartes des Nat</h2>',
  '>Materia che accoglie e custodisce pensieri<': '>Une matière qui accueille et garde les pensées<',
  ">L'incanto delle parole scritte a stilografica e pennino, per celebrare l'anima<": '>L’enchantement des mots écrits au stylo-plume et au porte-plume, pour célébrer l’âme<',
  ">L'incanto delle parole scritte a stilografica e pennino per celebrare Anima<": '>L’enchantement des mots écrits au stylo-plume et au porte-plume pour célébrer l’Âme<',
  '>Scrigni per il nostro bambino adulto, custodi della felicità di stringere tra le mani piccoli tesori<': '>Des écrins pour notre enfant adulte, gardiens du bonheur de tenir de petits trésors entre nos mains<',
  '>Spazi di ascolto, libera espressione e risveglio della mente<': '>Des espaces d’écoute, de libre expression et d’éveil de l’esprit<',
  '>Spazio di ascolto, libera espressione e risveglio della mente<': '>Un espace d’écoute, de libre expression et d’éveil de l’esprit<',
  '>Fiamme di luce per custodire intenzioni e fare spazio al silenzio<': '>Des flammes de lumière pour garder les intentions et faire place au silence<',
  '>Uno strumento di ascolto, dialogo con gli antenati e pacificazione interiore<': '>Un outil d’écoute, de dialogue avec les ancêtres et d’apaisement intérieur<',
  "Nata dall'incontro lento tra acqua, fibre e gesti antichi, la carta fatta a mano è una superficie viva. Ogni foglio conserva piccole imperfezioni, sfumature e bordi sfilacciati che raccontano di pazienza e presenza. Non è solo un supporto per scrivere, ma una materia che respira: un grembo delicato pronto ad accogliere le intenzioni, le memorie e i pensieri più puri. Ci sono parole che si scrivono con l'inchiostro e altre che si intrecciano con la materia. Qui la carta prende forma in racconti che diventano scrigni di stoffa e carta, e il gesto manuale si fa meditazione.": 'Née de la lente rencontre entre l’eau, les fibres et des gestes anciens, le papier fait main est une surface vivante. Chaque feuille garde de petites imperfections, des nuances et des bords effrangés qui parlent de patience et de présence. Ce n’est pas seulement un support pour écrire, mais une matière qui respire : un écrin délicat prêt à accueillir les intentions, les souvenirs et les pensées les plus purs. Il y a des mots qui s’écrivent à l’encre et d’autres qui se tissent dans la matière. Ici le papier prend forme en récits qui deviennent des écrins de tissu et de papier, et le geste manuel devient méditation.',
  "L'inchiostro traccia solchi leggeri sul foglio, trasformando il pensiero in un segno visibile e sacro. Le Dedicopoesie nascono dall'ascolto e prendono forma attraverso il ritmo lento della mia stilografica. Ogni parola tracciata a mano diventa un'opera unica, un dono visivo nato per celebrare un momento, un legame o una rinascita di Anima.": 'L’encre trace de légers sillons sur la feuille, transformant la pensée en un signe visible et sacré. Les poèmes-dédicaces naissent de l’écoute et prennent forme au rythme lent de mon stylo-plume. Chaque mot tracé à la main devient une œuvre unique, un cadeau visuel né pour célébrer un moment, un lien ou une renaissance de l’Âme.',
  "Cuciti e rilegati con cura artigianale, questi quaderni e piccoli racconti scritti a mano nascono per dare voce al nostro bambino adulto. Sono un invito a ritrovare la meraviglia e la gioia pura di quando, da piccoli, custodivamo tra le mani i nostri tesori più segreti. Piccoli libri d'affezione, fatti per ricordare che la bellezza dell'incanto non ha età.": 'Cousus et reliés avec un soin artisanal, ces carnets et petits récits écrits à la main naissent pour donner une voix à notre enfant adulte. Ils invitent à retrouver l’émerveillement et la joie pure du temps où, enfants, nous gardions entre nos mains nos trésors les plus secrets. De petits livres d’affection, faits pour rappeler que la beauté de l’enchantement n’a pas d’âge.',
  "Il diario creativo è un rifugio in cui la parola incontra la materia, il colore e le immagini dell'anima. Attraverso lo scrapbooking e il gesto manuale, la mente rallenta, il giudizio tace e la creatività diventa una pratica di meditazione e risveglio interiore. È uno spazio intimo dove dare forma alle emozioni ma anche un luogo del cuore aperto per il futuro: una traccia viva in cui tornare nei momenti bui e tristi che a volte la vita ci porta a vivere, per ritrovare la strada, fare luce e ricordarsi di sé.": 'Le journal créatif est un refuge où la parole rencontre la matière, la couleur et les images de l’âme. Grâce au scrapbooking et au geste manuel, l’esprit ralentit, le jugement se tait et la créativité devient une pratique de méditation et d’éveil intérieur. C’est un espace intime où donner forme aux émotions, mais aussi un lieu du cœur ouvert sur l’avenir : une trace vivante où revenir dans les moments sombres et tristes que la vie nous fait parfois traverser, pour retrouver le chemin, faire la lumière et se souvenir de soi.',
  "Create a mano con cere naturali, essenze e dettagli botanici, le candele poetiche nascono per accompagnare i momenti dedicati a sé e i piccoli rituali quotidiani. La loro fiamma non serve solo a illuminare una stanza, ma a fare luce dentro: un punto di fuoco e calore attorno al quale raccogliersi per meditare, scrivere, affidare un'intenzione al tempo e ritrovare la sacralità dei propri spazi interiori.": 'Fabriquées à la main avec des cires naturelles, des essences et des détails botaniques, les bougies poétiques naissent pour accompagner les moments consacrés à soi et les petits rituels du quotidien. Leur flamme ne sert pas seulement à éclairer une pièce, mais à faire la lumière en nous : un point de feu et de chaleur autour duquel se rassembler pour méditer, écrire, confier une intention au temps et retrouver le caractère sacré de nos espaces intérieurs.',
  'Ispirate agli spiriti della natura e al metodo immaginale, le Carte dei Nat non sono un semplice strumento di divinazione, ma uno specchio di Anima. Attraverso i loro simboli e archetipi ancestrali, la lettura diventa un incontro sacro in cui esplorare le proprie radici, sciogliere i nodi delle costellazioni familiari e ascoltare la voce guida che abita dentro di noi per ritrovare chiarezza e armonia sul proprio cammino.': 'Inspirées des esprits de la nature et de la méthode imaginale, les Cartes des Nat ne sont pas un simple outil de divination, mais un miroir de l’Âme. À travers leurs symboles et leurs archétypes ancestraux, la lecture devient une rencontre sacrée pour explorer ses racines, dénouer les nœuds des constellations familiales et écouter la voix intérieure qui nous guide, afin de retrouver clarté et harmonie sur son chemin.',
  'alt="Fogli di carta fatta a mano su un telaio di legno, con fiori secchi"': 'alt="Feuilles de papier fait main sur un tamis en bois, avec des fleurs séchées"',
  'alt="Buste di carta fatta a mano chiuse con sigilli di ceralacca, accanto a una stilografica"': 'alt="Enveloppes en papier fait main fermées par des cachets de cire, à côté d’un stylo-plume"',
  'alt="Quaderni rilegati a mano in carta colorata, legati con lo spago"': 'alt="Carnets reliés à la main en papier coloré, noués avec de la ficelle"',
  'alt="Diario creativo aperto con versi d\'autunno e adesivi ad acquerello"': 'alt="Journal créatif ouvert avec des vers d’automne et des stickers à l’aquarelle"',
  'alt="Candele in vasetti di vetro decorati con stoffe e motivi botanici"': 'alt="Bougies dans des pots en verre décorés de tissus et de motifs botaniques"',
  'alt="Il libro e il mazzo delle Carte dei Nat tra candele e fiori secchi"': 'alt="Le livre et le jeu des Cartes des Nat entre bougies et fleurs séchées"',
  'data-copiato="Copiato!"': 'data-copiato="Copié !"',
  'data-su-richiesta="Prezzo su richiesta"': 'data-su-richiesta="Prix sur demande"',
  'data-oggetto="Ordine dal sito: "': 'data-oggetto="Commande depuis le site : "',
  'data-corpo="Ciao Lié, vorrei acquistare il libro «%TITOLO%».&#10;&#10;Ho pagato con: (bonifico / PayPal)&#10;&#10;Nome e cognome:&#10;Indirizzo di spedizione:&#10;CAP e città:&#10;Telefono (per il corriere):&#10;&#10;Grazie!"': 'data-corpo="Bonjour Lié, je souhaite acheter le livre «%TITOLO%».&#10;&#10;J’ai payé par : (virement / PayPal)&#10;&#10;Nom et prénom :&#10;Adresse de livraison :&#10;Code postal, ville et pays :&#10;Téléphone (pour le transporteur) :&#10;&#10;Merci !"',
  'data-paypal-lc="IT"': 'data-paypal-lc="FR"',
  "Acquista direttamente dall'autrice": 'Acheter directement auprès de l’autrice',
  'spese di spedizione incluse': 'frais de port inclus',
  'Scegli come pagare:': 'Choisissez votre mode de paiement :',
  "Paghi in modo sicuro sul sito di PayPal, anche con carta di credito. PayPal ti chiederà l'indirizzo di spedizione.": 'Payez en toute sécurité sur le site de PayPal, également par carte bancaire. PayPal vous demandera votre adresse de livraison.',
  '>Paga con PayPal<': '>Payer avec PayPal<',
  '>Bonifico bancario<': '>Virement bancaire<',
  '<dt>Intestatario</dt>': '<dt>Titulaire</dt>',
  '<dt>Causale</dt>': '<dt>Référence</dt>',
  '>Copia<': '>Copier<',
  "Dopo il bonifico, inviami l'ordine con il tuo indirizzo di spedizione:": 'Après le virement, envoyez-moi votre commande avec votre adresse de livraison :',
  "Invia l'ordine via email": 'Envoyer la commande par e-mail',
  'Per qualsiasi domanda scrivimi a': 'Pour toute question, écrivez-moi à',
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
  'Leggi la trama': 'Read the plot', 'Acquista': 'Buy',
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
  'Leggi la trama': 'Lire le résumé', 'Acquista': 'Acheter',
  'Ultimi articoli dal blog': 'Derniers articles du blog', 'Tutti gli articoli →': 'Tous les articles →',
  '12 ottobre 2026': '12 octobre 2026',
 },
}

# Bio completa per lingua (sostituisce l'intero blocco bio-text)
BIO = {"en": "    <div class=\"bio-text\">\n      <p class=\"dropcap\">Lié Larousse Cortona lives exactly there, among the rhythms of the earth, the magic of small things and the depth of invisible bonds. A novelist and short-story writer, a poet, a practitioner and researcher in psychology and botany, she tends and nourishes life by caring for a vegetable garden where, beside her, Mrs Bianchina and her six sisters scratch about, feathered creatures who are her joy and her centre, along with Romeo, an elegant tabby cat, and Bruno, a sweet little bunny who fills the rooms of the house with light pawsteps and a presence that smells of hay.</p>\n      <p>Since 2012 Lié has nurtured her digital space <a href=\"https://libroarbitrio.wordpress.com/\" target=\"_blank\" rel=\"noopener\"><em>“Libroarbitrio – Il tempo di un tè con Lié”</em></a>, an internationally recognised literary and cultural blog.</p>\n      <p>Winner of prestigious prizes including the “My Book: Tell Your Story” prize, awarded by Dacia Maraini for her short story <em>“Ma le formiche si decompongono?”</em> (“But Do Ants Decompose?”), and with years of touring the country’s leading festivals behind her, Lié today devotes her vocation to the word, expressing it in all its forms.</p>\n      <p>Her work ranges from poetry, which explores the soul, with the collections <a href=\"libri.html#trama-lie\" class=\"link-titolo\"><em>.Lié.</em></a>, <a href=\"libri.html#trama-vita\" class=\"link-titolo\"><em>.la vita comunque.</em></a>, <a href=\"libri.html#trama-dopo\" class=\"link-titolo\"><em>.Dopo di noi.</em></a>, to fiction, where she explores unknown caverns of the mind, discovering secret, labyrinthine rooms, with the novels <a href=\"libri.html#trama-rid\" class=\"link-titolo\"><em>Rid Dementia</em></a> and <a href=\"libri.html#trama-nato\" class=\"link-titolo\"><em>NATO SOLO</em></a> (awarded at Casa Sanremo Writers for best TV series screenplay), and a careful social inquiry into the use of artificial intelligence in her latest publication <a href=\"libri.html#trama-ciao\" class=\"link-titolo\"><em>Ciao, come posso aiutarti? I.A. Innamorati Artificiali</em></a>.</p>\n      <p>Her new novel is coming out in December: an intense work on our relationship with pain, suffering and healing through hypnosis.</p>\n      <p>Her writing is a caress that joins dream and reality, an invitation to tend our roots so that the new can sprout in silence, keeping alive that first language she discovered as a child in the pages of countless diaries. Exploring the territories of the human soul, Lié brings her passions together through art in all its forms, and this is how she expresses her way of living in and being in the world: weaving paths of awakening the mind, evocative writing and “Soul-Making” through Craft Art.</p>\n    </div>", "fr": "    <div class=\"bio-text\">\n      <p class=\"dropcap\">Lié Larousse Cortona habite exactement là, entre les rythmes de la terre, la magie des petites choses et la profondeur des liens invisibles. Romancière et nouvelliste, poétesse, professionnelle et chercheuse dans les domaines de la psychologie et de la botanique, elle protège et nourrit la vie en prenant soin d’un potager où, à ses côtés, picorent madame Bianchina et ses six sœurs, créatures de plumes qui sont sa joie et son centre, l’élégant Romeo, chat tigré, et le doux petit lapin Bruno, qui remplit la maison de légers bruits de pattes et d’une présence qui sent le foin.</p>\n      <p>Depuis 2012, Lié cultive son espace numérique <a href=\"https://libroarbitrio.wordpress.com/\" target=\"_blank\" rel=\"noopener\"><em>“Libroarbitrio – Il tempo di un tè con Lié”</em></a>, un blog de référence littéraire et culturelle à l’échelle internationale.</p>\n      <p>Lauréate de prix prestigieux, dont le prix « My Book: Tell Your Story », récompensée par Dacia Maraini pour sa nouvelle <em>“Ma le formiche si decompongono?”</em> (« Mais les fourmis se décomposent-elles ? »), et forte de longues années de tournées dans les plus grands festivals du pays, Lié consacre aujourd’hui sa vocation à la parole, en l’exprimant sous toutes ses formes.</p>\n      <p>Son œuvre s’étend de la poésie, qui sonde l’âme, avec les recueils <a href=\"libri.html#trama-lie\" class=\"link-titolo\"><em>.Lié.</em></a>, <a href=\"libri.html#trama-vita\" class=\"link-titolo\"><em>.la vita comunque.</em></a>, <a href=\"libri.html#trama-dopo\" class=\"link-titolo\"><em>.Dopo di noi.</em></a>, à la fiction, où elle explore des antres inconnus de l’esprit, à la découverte de chambres secrètes et labyrinthiques, avec les romans <a href=\"libri.html#trama-rid\" class=\"link-titolo\"><em>Rid Dementia</em></a> et <a href=\"libri.html#trama-nato\" class=\"link-titolo\"><em>NATO SOLO</em></a> (primés à Casa Sanremo Writers pour le meilleur scénario de série télévisée), jusqu’à une enquête sociale attentive sur l’usage de l’intelligence artificielle avec sa dernière publication <a href=\"libri.html#trama-ciao\" class=\"link-titolo\"><em>Ciao, come posso aiutarti? I.A. Innamorati Artificiali</em></a>.</p>\n      <p>Son nouveau roman paraîtra en décembre : une œuvre intense sur notre rapport à la douleur, à la souffrance et à la guérison par l’hypnose.</p>\n      <p>Son écriture est une caresse qui unit rêve et réalité, une invitation à prendre soin de nos racines pour laisser le nouveau germer dans le silence, en gardant vivant ce premier langage découvert dès l’enfance dans les pages d’innombrables journaux intimes. Explorant les territoires de l’âme humaine, Lié réunit ses passions à travers l’art sous toutes ses formes : c’est ainsi qu’elle exprime sa manière d’habiter le monde et d’y être, en tissant des chemins d’éveil de l’esprit, d’écriture évocatrice et de « Faire Âme » à travers le Craft Art.</p>\n    </div>"}
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
    s = re.sub(r'    <div class="bio-text">.*?\n    </div>', lambda m: BIO[lang], s, flags=re.S)
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
    s = re.sub(r'>Acquista · (\d+),(\d+) €<', lambda m: ('>Buy · €' + m.group(1) + '.' + m.group(2) + '<') if lang == 'en' else ('>Acheter · ' + m.group(1) + ',' + m.group(2) + ' €<'), s)
    s = s.replace('https://www.etsy.com/it/people/', 'https://www.etsy.com/people/')
    s = s.replace("</em> e all'<em>", '</em> ' + {'en': 'and ', 'fr': 'et à l’'}[lang] + '<em>')
    s = s.replace('<html lang="it">', f'<html lang="{lang}">')
    # percorsi verso i file condivisi
    s = re.sub(r'href="style\.css', 'href="../style.css', s)
    s = s.replace('src="img/', 'src="../img/').replace('data-copertina="img/', 'data-copertina="../img/').replace('href="img/', 'href="../img/').replace('href="favicon.ico"', 'href="../favicon.ico"')
    return s


# ---------- Anteprime social e Google ----------
BASE = 'https://lielarousse.it/'
LOCALE = {'it': 'it_IT', 'en': 'en_GB', 'fr': 'fr_FR'}
DESCRIZIONI = {
 'it': {
  'index.html': 'Lié Larousse, scrittrice e poetessa tra psicologia e botanica. Autrice di Rid Dementia, NATO SOLO e Ciao, come posso aiutarti? e del blog Libroarbitrio – Il tempo di un tè con Lié.',
  'libri.html': 'I libri di Lié Larousse: Ciao, come posso aiutarti? I.A. Innamorati Artificiali, i romanzi Rid Dementia e NATO SOLO e le raccolte di poesie .Lié., .la vita comunque. e .Dopo di noi.',
  'blog.html': 'Libroarbitrio – Il tempo di un tè con Lié: il blog e il canale YouTube di Lié Larousse, tra libri, natura e tempo lento.',
  'arte.html': 'Craft Art di Lié Larousse: carta fatta a mano, dedicopoesie e calligrafia, quaderni rilegati, diario creativo, candele poetiche e lettura immaginale con le Carte dei Nat.',
  'contatti.html': 'Contatta Lié Larousse per presentazioni, interviste e collaborazioni. Email, Instagram, Facebook e YouTube.',
 },
 'en': {
  'index.html': 'Lié Larousse, writer and poet working between psychology and botany. Author of Rid Dementia, NATO SOLO and Ciao, come posso aiutarti?, and of the blog Libroarbitrio – Il tempo di un tè con Lié.',
  'libri.html': 'The books of Lié Larousse: Ciao, come posso aiutarti? I.A. Innamorati Artificiali, the novels Rid Dementia and NATO SOLO, and the poetry collections .Lié., .la vita comunque. and .Dopo di noi.',
  'blog.html': 'Libroarbitrio – Il tempo di un tè con Lié: the blog and YouTube channel of Lié Larousse, about books, nature and slow living.',
  'arte.html': 'Craft Art by Lié Larousse: handmade paper, dedication poems and calligraphy, hand-bound notebooks, creative journals, poetic candles and imaginal reading with the Nat Cards.',
  'contatti.html': 'Contact Lié Larousse for book presentations, interviews and collaborations. Email, Instagram, Facebook and YouTube.',
 },
 'fr': {
  'index.html': 'Lié Larousse, écrivaine et poétesse entre psychologie et botanique. Autrice de Rid Dementia, NATO SOLO et Ciao, come posso aiutarti?, et du blog Libroarbitrio – Il tempo di un tè con Lié.',
  'libri.html': 'Les livres de Lié Larousse : Ciao, come posso aiutarti? I.A. Innamorati Artificiali, les romans Rid Dementia et NATO SOLO, et les recueils de poèmes .Lié., .la vita comunque. et .Dopo di noi.',
  'blog.html': 'Libroarbitrio – Il tempo di un tè con Lié : le blog et la chaîne YouTube de Lié Larousse, entre livres, nature et temps lent.',
  'arte.html': 'Craft Art de Lié Larousse : papier fait main, poèmes-dédicaces et calligraphie, carnets reliés, journal créatif, bougies poétiques et lecture imaginale avec les Cartes des Nat.',
  'contatti.html': 'Contactez Lié Larousse pour des présentations, des interviews et des collaborations. E-mail, Instagram, Facebook et YouTube.',
 },
}
PERSONA = {
 "@context": "https://schema.org", "@type": "Person", "name": "Lié Larousse",
 "url": BASE, "image": BASE + "img/lie-ritratto-bio.jpg", "email": "mailto:lielarousse@yahoo.it",
 "jobTitle": "Scrittrice e poetessa",
 "sameAs": ["https://www.instagram.com/lielarousse/", "https://www.facebook.com/lie.larousse/",
            "https://www.youtube.com/@Libroarbitrio", "https://libroarbitrio.wordpress.com/"],
 "sibling": {"@type": "Person", "name": "Cortona Francesca", "url": "https://cortonafrancesca.it/", "jobTitle": "Pittrice"}
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


def collega(s):
    """Il nome di Cortona Francesca porta al suo sito."""
    link = '<a href="https://cortonafrancesca.it/" class="link-nome" target="_blank" rel="noopener">Cortona Francesca</a>'
    s = s.replace(link, 'Francesca Cortona')
    s = s.replace('<a href="https://cortonafrancesca.it/" class="link-nome" target="_blank" rel="noopener">Francesca Cortona</a>', 'Francesca Cortona')
    corpo_inizio = s.index('<body>')
    return s[:corpo_inizio] + s[corpo_inizio:].replace('Francesca Cortona', link)


for pagina in PAGINE:
    it = open(pagina, encoding='utf-8').read()
    it = metti_switcher(it, 'it', pagina)
    it = collega(seo(it, 'it', pagina))
    open(pagina, 'w', encoding='utf-8').write(it)
    for lang in ['en', 'fr']:
        os.makedirs(lang, exist_ok=True)
        out = collega(seo(metti_switcher(traduci(collega(it).replace(
            '<a href="https://cortonafrancesca.it/" class="link-nome" target="_blank" rel="noopener">Cortona Francesca</a>', 'Francesca Cortona'), lang), lang, pagina), lang, pagina))
        open(f'{lang}/{pagina}', 'w', encoding='utf-8').write(out)
sitemap()
print('fatto')
