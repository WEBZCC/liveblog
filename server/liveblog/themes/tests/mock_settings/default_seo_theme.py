default_seo_theme = {
    'name': 'default',
    'version': '3.3.56',
    'asyncTheme': True,
    'seoTheme': True,
    'contributors': [
        'Paul Solbach <psolbach@dpa-newslab.com>',
        'Massimo Scamarcia <massimo.scamarcia@sourcefabric.org>',
        'Löic Nogues <loic.nogues@sourcefabric.org>',
        'Aleksandar Backo Jelicic <aleksandar.jelicic@sourcefabric.org>'
    ],
    'options': [
        {
            'name': 'datetimeFormat',
            'label': 'Date time Format',
            'type': 'datetimeformat',
            'default': 'lll',
            'help': 'Sets the date time format to be used in the \
            embed. Please enter a custom format in valid moment.js \
            format http://momentjs.com/docs/#/parsing/string-format'
        },
        {
            'name': 'showUpdateDatetime',
            'label': 'Show post update time',
            'type': 'checkbox',
            'default': False,
            'help': 'If activated, users will see an additional timestamp, when the post has been updated'
        },
        {
            'name': 'postsPerPage',
            'label': 'Number of posts per page',
            'type': 'number',
            'default': 20,
            'help': 'Set the number of posts you initially want to show to your readers'
        },
        {
            'name': 'datetimeFormattest',
            'label': 'Date time Format test',
            'type': 'datetimeFormattest',
            'default': 'lll',
            'help': 'Test'
        },
        {
            'name': 'postOrder',
            'label': 'Default posts order',
            'type': 'select',
            'options': [
                {
                    'value': 'editorial',
                    'label': 'Editorial'
                },
                {
                    'value': 'newest_first',
                    'label': 'Newest first'
                },
                {
                    'value': 'oldest_first',
                    'label': 'Oldest first'
                }
            ],
            'default': 'editorial'
        },
        {
            'name': 'autoApplyUpdates',
            'label': 'All updates are auto-applied periodically',
            'type': 'checkbox',
            'default': True,
            'help': 'Turn off to prompt user to load updates'
        },
        {
            'name': 'canComment',
            'label': 'Users can comment',
            'type': 'checkbox',
            'default': False,
            'help': 'Enables a commenting form for users'
        },
        {
            'name': 'showImage',
            'label': 'Show the blog image',
            'type': 'checkbox',
            'default': False
        },
        {
            'name': 'showTitle',
            'label': 'Show the blog title',
            'type': 'checkbox',
            'default': False
        },
        {
            'name': 'showDescription',
            'label': 'Show the blog description',
            'type': 'checkbox',
            'default': False
        },
        {
            'name': 'showLiveblogLogo',
            'label': 'Show Liveblog logo',
            'type': 'checkbox',
            'default': True,
            'help': 'Turn off to hide the “powered by Live Blog” logo'
        },
        {
            'name': 'showAuthor',
            'label': 'Show the author',
            'type': 'checkbox',
            'default': True,
            'help': 'Show the author information on posts'
        },
        {
            'name': 'authorNameFormat',
            'label': 'Author name format',
            'type': 'select',
            'default': 'display_name',
            'dependsOn': {
                'showAuthor': True
            },
            'options': [
                {
                    'value': 'display_name',
                    'label': 'Full name'
                },
                {
                    'value': 'byline',
                    'label': 'Byline'
                },
                {
                    'value': 'sign_off',
                    'label': 'Sign off'
                }
            ],
            'help': 'How to show the author info'
        },
        {
            'name': 'showAuthorAvatar',
            'label': 'Show author avatar',
            'type': 'checkbox',
            'default': True,
            'dependsOn': {
                'showAuthor': True
            },
            'help': 'Shows an author image besides the author name'
        },
        {
            'name': 'hasHighlights',
            'label': 'Show highlight button',
            'type': 'checkbox',
            'default': False,
            'help': 'Introduces a button for the readers to filter the timeline by highlights'
        },
        {
            'name': 'permalinkDelimiter',
            'label': 'Permalink delimiter',
            'type': 'select',
            'options': [
                {
                    'value': '?',
                    'label': 'Query delimiter (?)'
                },
                {
                    'value': '#',
                    'label': ' Fragment identifier delimiter (#)'
                }
            ],
            'default': '?',
            'help': 'Sets the delimiter used to send the permalink. \
            ex: permalinkHashMark=?, http://example.com/?...'
        },
        {
            'name': 'blockSearchEngines',
            'label': 'Block search engines',
            'type': 'checkbox',
            'default': True,
            'help': 'Will block search engines from indexing the blog content'
        },
        {
            'name': 'showGallery',
            'label': 'Show slideshow gallery',
            'type': 'checkbox',
            'default': False,
            'help': 'Multiple image posts will show up as an image gallery'
        },
        {
            'name': 'stickyPosition',
            'label': 'Pinned post behaviour',
            'type': 'select',
            'options': [
                {
                    'value': 'bottom',
                    'label': 'Show below menu bar'
                },
                {
                    'value': 'top',
                    'label': 'Show above menu bar'
                }
            ],
            'default': 'bottom',
            'help': 'Please note: Pinned posts above the menu bar will \
            not show the author info nor a timestamp. This setting is \
            especially useful if you want to show a (streaming) video on top of your timeline.'
        },
        {
            'name': 'gaCode',
            'label': 'Google analytics code',
            'type': 'text',
            'placeholder': 'UA-XXXXX-Y',
            'default': '',
            'help': 'Please enter your google analytics account ID.'
        },
        {
            'name': 'renderForESI',
            'label': 'Optimise the Live Blog output for ESI',
            'type': 'checkbox',
            'default': False,
            'help': 'Strips the head and body tags from the Live Blog \
            output to publish it using Edge Side Includes'
        },
        {
            'name': 'removeStylesESI',
            'label': 'Remove stylesheet from the Live Blog output for ESI',
            'type': 'checkbox',
            'default': False,
            'help': 'Removes the link to the stylesheet from the Live \
            Blog output to publish it using Edge Side Includes '
        },
        {
            'name': 'language',
            'label': 'Theme language',
            'type': 'select',
            'options': [
                {
                    'value': 'en',
                    'label': 'English'
                },
                {
                    'value': 'fi',
                    'label': 'Finnish'
                },
                {
                    'value': 'de',
                    'label': 'Deutsch'
                },
                {
                    'value': 'fr',
                    'label': 'Français'
                },
                {
                    'value': 'nl',
                    'label': 'Nederlands'
                },
                {
                    'value': 'no',
                    'label': 'Norsk'
                },
                {
                    'value': 'cs',
                    'label': 'Čeština'
                },
                {
                    'value': 'ro',
                    'label': 'Română'
                }
            ],
            'default': 'en'
        },
        {
            'name': 'showSyndicatedAuthor',
            'label': 'Show syndicated author',
            'type': 'checkbox',
            'default': False,
            'help': 'If the users will see the syndicated author'
        },
        {
            'name': 'clientDatetimeOnly',
            'label': 'Show datetime only on client',
            'type': 'checkbox',
            'default': False,
            'help': 'If the users will see the datetime only on client rendered'
        },
        {
            "name": "enableGdprConsent",
            "label": "Enable GDPR Consent",
            "type": "checkbox",
            "default": False,
            "help": "If users will see a placeholder on embeds until consent is given"
        },
        {
            "name": "gdprConsentText",
            "label": "GDPR Consent Placeholder Text",
            "type": "text",
            "dependsOn": {
                "enableGdprConsent": True
            },
            "default": "Test placeholder for gdpr message",
            "help": "This text will be shown in the GDPR placeholder"
        }
    ],
    "styleOptions": [
        {
            "label": "Typography",
            "name": "typography",
            "cssSelector": "div.lb-timeline",
            "columns": 2,
            "serializerIgnore": True,
            "options": [
                {
                    "label": "Primary Font Family",
                    "property": "primary",
                    "type": "fontpicker"
                },
                {
                    "label": "Secondary Font Family",
                    "property": "secundary",
                    "type": "fontpicker"
                }
            ]
        },
        {
            "label": "General",
            "name": "general",
            "cssSelector": "div.lb-timeline",
            "columns": 3,
            "options": [
                {
                    "label": "Blog Margin",
                    "property": "margin",
                    "type": "text",
                    "placeholder": "px or %"
                },
                {
                    "label": "Blog Padding",
                    "property": "padding",
                    "type": "text",
                    "placeholder": "px or %"
                },
                {
                    "label": "Blog Max. Width",
                    "property": "max-width",
                    "type": "text",
                    "placeholder": "px or %"
                },
                {
                    "label": "Background",
                    "property": "background",
                    "type": "colorpicker",
                    "default": "#ffffff"
                },
                {
                    "label": "Link Color",
                    "property": "color",
                    "type": "colorpicker",
                    "tagName": "a",
                    "default": "#3394bc"
                }
            ]
        },
        {
            "label": "Title",
            "name": "blog-title",
            "cssSelector": "div.lb-timeline h1",
            "columns": 5,
            "options": [
                {
                    "label": "Font Family",
                    "property": "font-family",
                    "type": "dropdown",
                    "linkedToGroup": "typography",
                    "options": [
                        {"value": None, "label": "Select a font"},
                        {"value": "primary", "label": "Primary"},
                        {"value": "secundary", "label": "Secundary"}
                    ]
                },
                {
                    "label": "Font Size",
                    "property": "font-size",
                    "type": "text",
                    "placeholder": "px or rem"
                },
                {
                    "label": "Font Weight",
                    "property": "font-weight",
                    "type": "dropdown",
                    "default": "normal",
                    "options": [
                        {"value": "bold", "label": "Bold"},
                        {"value": "normal", "label": "Normal"}
                    ]
                },
                {
                    "label": "Font Style",
                    "property": "font-style",
                    "type": "dropdown",
                    "default": "normal",
                    "options": [
                        {"value": "italic", "label": "Italic"},
                        {"value": "normal", "label": "Normal"}
                    ]
                },
                {
                    "label": "Font Color",
                    "property": "color",
                    "type": "colorpicker",
                    "default": "#333333"
                }
            ]
        }
    ],
    'i18n': {
        'cs': {
            'Highlights': 'Hlavní body',
            'Comment by': 'Komentář',
            'Powered by': 'Poháněno',
            'Advertisement': 'reklama',
            'Cancel': 'Zrušit',
            'Comment': 'Váš příspěvek',
            'Comment *': 'Text *',
            'Comment should be maximum 300 characters in length': 'Maximální délka textu je 300 znaků',
            'Editorial': 'redakční',
            'Load more posts': 'Načíst další',
            'Loading': 'Načítám',
            'Name *': 'Jméno *',
            'Name should be maximum 30 characters in length': 'Maximální délka jména je 30 znaků',
            'Newest first': 'nejnovější',
            'No posts for now': 'Žádné příspěvky',
            'Oldest first': 'nejstarší',
            'One pinned post': 'Jeden připnutý příspěvek',
            'pinned posts': 'připnuté příspěvky',
            'Post a comment': 'Otázka / komentář',
            'See one new update': 'Zobraz 1 nový příspěvek',
            'See new updates': 'Zobraz nové příspěvky',
            'Send': 'Odeslat',
            'Show all posts': 'Zobrazit všechny',
            'Show highlighted post only': 'Zobraz jen zvýrazněné příspěvky',
            'Sort by:': 'Řazení:',
            'Updated': 'Aktualizace',
            'Your comment was sent for approval': 'Váš text byl úspěšně odeslán Čeká na schválení',
            'credit:': ' autor:'
        },
        'de': {
            'Highlights': 'Highlights',
            'Comment by': 'Kommentar von',
            'Powered by': 'Unterstützt von',
            'Advertisement': 'Werbung',
            'Cancel': 'Abbrechen',
            'Comment': 'Kommentar',
            'Comment *': 'Kommentar',
            'Comment should be maximum 300 characters in length': 'Kommentar \
                darf maximal 300 Zeichen lang sein',
            'Editorial': 'Redaktionell',
            'Load more posts': 'Weitere Beiträge',
            'Loading': 'Lade',
            'Name *': 'Name',
            'Name should be maximum 30 characters in length': 'Name darf maximal 30 Zeichen lang sein',
            'Newest first': 'Neueste zuerst',
            'No posts for now': 'Kein Beitrag vorhanden',
            'Oldest first': 'Älteste zuerst',
            'One pinned post': 'Angehefteter Eintrag',
            'pinned posts': 'Angeheftete Einträge',
            'Please fill in your Comment': 'Bitte Kommentar hier eintragen',
            'Please fill in your Name': 'Bitte Namen hier eintragen',
            'Post a comment': 'Kommentar posten',
            'See one new update': 'Neuen Beitrag anzeigen',
            'See new updates': 'Neue Beiträge anzeigen',
            'Send': 'Abschicken',
            'Show all posts': 'Alle Beiträge anzeigen',
            'Show highlighted post only': 'Anzeigen hervorgehoben Beitrag ist nur',
            'Sort by:': 'Ordnen nach',
            'Updated': 'Aktualisiert am',
            'Your comment was sent for approval': 'Ihr Kommentar wartet auf Freischaltung',
            'credit:': 'Bild:'
        },
        'fi': {
            'Highlights': 'Kohokohtia',
            'Comment by': 'Comment by',
            'Powered by': 'Powered by',
            'Advertisement': 'Mainos',
            'Cancel': 'Peruuta',
            'Comment': 'Kommentoi',
            'Comment *': 'Kommentti *',
            'Comment should be maximum 300 characters in length': 'Kommentin enimmäispituus on 300 merkkiä',
            'Editorial': 'Toimituksellinen',
            'Load more posts': 'Lataa lisää julkaisuja',
            'Loading': 'Lataa',
            'Name *': 'Nimi *',
            'Name should be maximum 30 characters in length': 'Nimen enimmäispituus on 30 merkkiä',
            'Newest first': 'Uusimmat ensin',
            'No posts for now': 'Ei uusia julkaisuja',
            'Oldest first': 'Vanhimmat ensin',
            'One pinned post': 'Yksi kiinnitetty julkaisu',
            'pinned posts': 'kiinnitettyä julkaisua',
            'Please fill in your Comment': 'Lisää kommenttisi',
            'Please fill in your Name': 'Lisää nimesi',
            'Post a comment': 'Lähetä kommentti',
            'See one new update': 'Lataa yksi uusi julkaisu',
            'See new updates': 'Lataa uutta julkaisua',
            'Send': 'Lähetä',
            'Show all posts': 'Näytä kaikki julkaisut',
            'Show highlighted post only': 'Näytä vain korostettu julkaisu',
            'Sort by:': 'Järjestä:',
            'Updated': 'Päivitetty',
            'Your comment was sent for approval': 'Kommenttisi lähetettiin hyväksyttäväksi',
            'credit:': '©'
        },
        'fr': {
            'Highlights': 'Messages en surbrillance',
            'Comment by': 'Commentaire de',
            'Powered by': 'Alimenté par',
            'Advertisement': 'Publicité',
            'Cancel': 'Annuler',
            'Comment': 'Commentaire',
            'Comment *': 'Commentaire *',
            'Comment should be maximum 300 characters in length': 'Un commentaire ne peut excéder 300 signes',
            'Editorial': 'Éditorial',
            'Load more posts': 'Afficher plus de messages',
            'Loading': 'Chargement',
            'Name *': 'Nom *',
            'Name should be maximum 30 characters in length': 'Le nom ne peut excéder 30 signes',
            'Newest first': "Le plus récent d'abord",
            'No posts for now': 'Aucun message pour le moment',
            'Oldest first': 'Plus ancien en premier',
            'One pinned post': 'Voir le nouveau message',
            'pinned posts': 'Voir nouveaux messages',
            'Please fill in your Comment': 'Votre commentaire',
            'Please fill in your Name': 'Votre nom',
            'Post a comment': 'Envoyer un commentaire',
            'See one new update': 'Voir le nouveau message',
            'See new updates': 'Voir nouveaux messages',
            'Send': 'Envoyer',
            'Show all posts': 'Afficher tous les messages',
            'Show highlighted post only': 'Afficher uniquement les messages en surbrillance',
            'Sort by:': 'Trier par:',
            'Updated': 'Mise à jour',
            'Your comment was sent for approval': 'Votre commentaire \
                a été envoyé et est en attente de validation',
            'credit:': 'crédit:'
        },
        'nl': {
            'Highlights': 'Highlights',
            'Comment by': 'Commentaar door',
            'Powered by': 'Aangedreven door',
            'Advertisement': 'Advertentie',
            'Cancel': 'Annuleren',
            'Comment': 'Reactie',
            'Comment *': 'Tekst *',
            'Comment should be maximum 300 characters in length': 'Uw reactie van maximaal 300 tekens',
            'Editorial': 'Redactioneel',
            'Load more posts': 'Meer',
            'Loading': 'Laden',
            'Name *': 'Naam *',
            'Name should be maximum 30 characters in length': 'Uw naam kan maximaal 30 tekens lang zijn',
            'Newest first': 'Toon nieuwste eerst',
            'No posts for now': 'Nog geen berichten beschikbaar',
            'Oldest first': 'Toon oudste eerst',
            'One pinned post': 'Bekijk nieuw bericht',
            'pinned posts': 'Bekijk nieuwe berichten',
            'Please fill in your Comment': 'Uw reactie',
            'Please fill in your Name': 'Vul hier uw naam in',
            'Post a comment': 'Schrijf een reactie',
            'See one new update': 'Bekijk nieuw bericht',
            'See new updates': 'Bekijk nieuwe berichten',
            'Send': 'Verzenden',
            'Sort by:': 'Sorteer:',
            'Your comment was sent for approval': 'Uw reactie is ontvangen ter beoordeling',
            'credit:': 'credit:'
        },
        'no': {
            'Highlights': 'Høydepunkter',
            'Comment by': 'Kommentar av',
            'Powered by': 'Drevet av',
            'Advertisement': 'Annonse',
            'Cancel': 'Avbryt',
            'Comment': 'Kommentar',
            'Comment *': 'Kommentar*',
            'Comment should be maximum 300 characters in length': 'Kommentarer kan være inntil 300 tegn',
            'Editorial': 'Redaksjonelt',
            'Load more posts': 'Henter flere poster',
            'Loading': 'Henter',
            'Name *': 'Navn*',
            'Name should be maximum 30 characters in length': 'Navn kan ikke ha mer enn 30 tegn',
            'Newest first': 'Nyeste først',
            'No posts for now': 'Ingen poster for øyeblikket',
            'Oldest first': 'Eldste først',
            'One pinned post': 'Én post festet til toppen',
            'pinned posts': 'poster festet til toppen',
            'Please fill in your Comment': 'Skriv inn din kommentar',
            'Please fill in your Name': 'Skriv inn navn',
            'Post a comment': 'Post en kommentar',
            'See one new update': 'Se én ny oppdatering',
            'See new updates': 'Se nye oppdateringer',
            'Send': 'Send',
            'Show all posts': 'Vis alle poster',
            'Show highlighted post only': 'Vis bare høydepunkter',
            'Sort by:': 'Sortér etter:',
            'Updated': 'Oppdatert',
            'Your comment was sent for approval': 'Din kommentar er sendt til godkjenning',
            'credit:': 'credit:'
        },
        'ro': {
            'Highlights': 'Repere',
            'Comment by': 'Comentariu de',
            'Powered by': 'Cu sprijinul',
            'Advertisement': 'Reclamă',
            'Cancel': 'Anulează',
            'Comment': 'Comentează',
            'Comment *': 'Comentariu *',
            'Comment should be maximum 300 characters in length': 'Comentariu \
                nu poate fi mai lung de 300 de caractere',
            'Editorial': 'Editorial',
            'Load more posts': 'Încarcă mai multe posturi',
            'Loading': 'Se încarcă',
            'Name *': 'Numele *',
            'Name should be maximum 30 characters in length': 'Numele nu poate fi mai lung de 30 de caractere',
            'Newest first': 'Cele mai noi',
            'No posts for now': 'Deocamdata nu sunt articole',
            'Oldest first': 'Cele mai vechi',
            'One pinned post': 'Vezi un articol nou',
            'pinned posts': 'Vezi articole noi',
            'Please fill in your Comment': 'Completează comentariu',
            'Please fill in your Name': 'Completează numele',
            'Post a comment': 'Scrie un comentariu',
            'See one new update': 'Vezi un articol nou',
            'See new updates': 'Vezi articole noi',
            'Send': 'Trimite',
            'Sort by:': 'Ordonează după:',
            'Your comment was sent for approval': 'Comentariul tău a fost trimis spre aprobare',
            'credit:': 'credit:'
        }
    }
}
