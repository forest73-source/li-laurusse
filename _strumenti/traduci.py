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
  'Apri il menu': 'Open the menu',
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
  'Apri il menu': 'Ouvrir le menu',
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
    s = re.sub(r'<p class="anno">(Romanzo|Poesia|Saggio)', lambda m: '<p class="anno">' + GENERI[lang][m.group(1)], s)
    s = s.replace("</em> e all'<em>", '</em> ' + {'en': 'and ', 'fr': 'et à l’'}[lang] + '<em>')
    s = s.replace('<html lang="it">', f'<html lang="{lang}">')
    # percorsi verso i file condivisi
    s = re.sub(r'href="style\.css', 'href="../style.css', s)
    s = s.replace('src="img/', 'src="../img/').replace('href="img/', 'href="../img/').replace('href="favicon.ico"', 'href="../favicon.ico"')
    return s


# ---------- Anteprime social e Google ----------
BASE = 'https://forest73-source.github.io/li-laurusse/'
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
        righe.append('<script type="application/ld+json">' + json.dumps(PERSONA, ensure_ascii=False) + '</script>')
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
