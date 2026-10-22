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
  'Lié Larousse abita esattamente lì, tra i ritmi della terra, la magia delle piccole cose e la profondità dei legami invisibili. Scrittrice di romanzi e racconti, poetessa, professionista e ricercatrice nei campi della psicologia e della botanica, Lié coltiva dal 2013 il suo spazio digitale':
   'Lié Larousse lives exactly there, among the rhythms of the earth, the magic of small things and the depth of invisible bonds. A novelist and short-story writer, a poet, a practitioner and researcher in psychology and botany, since 2013 Lié has nurtured her digital space',
  ', blog di riferimento letterario e culturale a livello internazionale.': ', an internationally recognised literary and cultural blog.',
  "Il suo impegno letterario va dalla poesia, che indaga l'anima, con le raccolte": 'Her literary work ranges from poetry, which explores the soul, with the collections',
  ', alla narrativa, che esplora le stanze segrete della mente, con i romanzi': ', to fiction, which explores the secret rooms of the mind, with the novels',
  "(entrambi premiati per la miglior sceneggiatura per serie TV a Casa Sanremo Writers), fino al suo prossimo romanzo in uscita a dicembre: un'opera intensa sull'umano rapporto con il dolore, la cura mentale e la guarigione attraverso l'ipnosi. Il suo percorso spazia inoltre fino all'analisi sociale sull'uso dell'intelligenza artificiale con":
   '(both awarded for best TV series screenplay at Casa Sanremo Writers), and on to her next novel, out in December: an intense work on our human relationship with pain, mental care and healing through hypnosis. Her path also reaches into the social analysis of artificial intelligence with',
  "La sua scrittura è una carezza che unisce sogno e realtà, un invito a custodire le radici per permettere al nuovo di germogliare nel silenzio. Esplorando i territori dell'animo umano, Lié unisce la passione per la parola a quella per la psicologia, intrecciando percorsi di risveglio della mente e fare anima attraverso la craft art.":
   'Her writing is a caress that joins dream and reality, an invitation to tend our roots so that the new can sprout in silence. Exploring the territories of the human soul, Lié brings together her passion for words and for psychology, weaving paths of awakening the mind and soul-making through craft art.',
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
  'Apri il menu': 'Open the menu',
 },
 'fr': {
  'Lié Larousse, scrittrice. Libri, racconti dal giardino e Libroarbitrio, il tempo di un tè con Lié.': 'Lié Larousse, écrivaine. Livres, récits du jardin et Libroarbitrio, le temps d’un thé avec Lié.',
  'Ci sono luoghi dentro di noi in cui il tempo': 'Il existe des lieux en nous où le temps',
  'per fare spazio alla': 'pour faire place à la',
  'Lié Larousse abita esattamente lì, tra i ritmi della terra, la magia delle piccole cose e la profondità dei legami invisibili. Scrittrice di romanzi e racconti, poetessa, professionista e ricercatrice nei campi della psicologia e della botanica, Lié coltiva dal 2013 il suo spazio digitale':
   'Lié Larousse habite exactement là, entre les rythmes de la terre, la magie des petites choses et la profondeur des liens invisibles. Romancière et nouvelliste, poétesse, professionnelle et chercheuse dans les domaines de la psychologie et de la botanique, Lié cultive depuis 2013 son espace numérique',
  ', blog di riferimento letterario e culturale a livello internazionale.': ', un blog littéraire et culturel de référence à l’international.',
  "Il suo impegno letterario va dalla poesia, che indaga l'anima, con le raccolte": 'Son œuvre littéraire va de la poésie, qui sonde l’âme, avec les recueils',
  ', alla narrativa, che esplora le stanze segrete della mente, con i romanzi': ', à la fiction, qui explore les chambres secrètes de l’esprit, avec les romans',
  "(entrambi premiati per la miglior sceneggiatura per serie TV a Casa Sanremo Writers), fino al suo prossimo romanzo in uscita a dicembre: un'opera intensa sull'umano rapporto con il dolore, la cura mentale e la guarigione attraverso l'ipnosi. Il suo percorso spazia inoltre fino all'analisi sociale sull'uso dell'intelligenza artificiale con":
   '(tous deux primés pour le meilleur scénario de série télévisée à Casa Sanremo Writers), jusqu’à son prochain roman, à paraître en décembre : une œuvre intense sur le rapport humain à la douleur, au soin psychique et à la guérison par l’hypnose. Son parcours s’étend aussi à l’analyse sociale de l’usage de l’intelligence artificielle avec',
  "La sua scrittura è una carezza che unisce sogno e realtà, un invito a custodire le radici per permettere al nuovo di germogliare nel silenzio. Esplorando i territori dell'animo umano, Lié unisce la passione per la parola a quella per la psicologia, intrecciando percorsi di risveglio della mente e fare anima attraverso la craft art.":
   'Son écriture est une caresse qui unit le rêve et la réalité, une invitation à prendre soin de nos racines pour laisser le nouveau germer dans le silence. Explorant les territoires de l’âme humaine, Lié unit sa passion pour les mots à celle pour la psychologie, en tissant des chemins d’éveil de l’esprit et de travail de l’âme à travers l’art créatif.',
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
  'Apri il menu': 'Ouvrir le menu',
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
  'Il blog · dal 2013': 'The blog · since 2013', 'Leggi il blog ▸': 'Read the blog ▸',
  'Il mio canale YouTube': 'My YouTube channel', 'Guarda i video ▸': 'Watch the videos ▸',
  'Dal mio canale YouTube': 'From my YouTube channel', 'Tutti i video ▸': 'All videos ▸',
  'Nome': 'Name', 'Messaggio': 'Message', 'Invia': 'Send',
  'La tua email': 'Your email',
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
  'Il blog · dal 2013': 'Le blog · depuis 2013', 'Leggi il blog ▸': 'Lire le blog ▸',
  'Il mio canale YouTube': 'Ma chaîne YouTube', 'Guarda i video ▸': 'Voir les vidéos ▸',
  'Dal mio canale YouTube': 'Sur ma chaîne YouTube', 'Tutti i video ▸': 'Toutes les vidéos ▸',
  'Nome': 'Nom', 'Messaggio': 'Message', 'Invia': 'Envoyer', 'Email': 'E-mail',
  'La tua email': 'Votre e-mail',
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
    s = s.replace('placeholder="La tua email"', f'placeholder="{PLACEHOLDER[lang]}"')
    s = s.replace('</em></a> e <a', f'</em></a> {CONGIUNZIONE[lang]} <a').replace('</em> e <em>', f'</em> {CONGIUNZIONE[lang]} <em>')
    s = s.replace("</em> e all'<em>", '</em> ' + {'en': 'and ', 'fr': 'et à l’'}[lang] + '<em>')
    s = s.replace('<html lang="it">', f'<html lang="{lang}">')
    # percorsi verso i file condivisi
    s = re.sub(r'href="style\.css', 'href="../style.css', s)
    s = s.replace('src="img/', 'src="../img/')
    return s


for pagina in PAGINE:
    it = open(pagina, encoding='utf-8').read()
    it = metti_switcher(it, 'it', pagina)
    open(pagina, 'w', encoding='utf-8').write(it)
    for lang in ['en', 'fr']:
        os.makedirs(lang, exist_ok=True)
        out = metti_switcher(traduci(it, lang), lang, pagina)
        open(f'{lang}/{pagina}', 'w', encoding='utf-8').write(out)
print('fatto')
