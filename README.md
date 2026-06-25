# 🌐 Web On Web - Python Web Browser

Un browser web modern și bogat în funcționalități, construit integral în Python folosind PyQt5.

## Caracteristici

✨ **Caracteristici principale:**
- 🌍 Posibilitate completă de navigare web
- 📑 Suport pentru multiple tab-uri
- ⏮️ Navigare Back/Forward
- 🔄 Reîncarcă pagina
- 🏠 Pagina de start
- 📜 Gestionare istoricului de navigare
- 🔍 Bara de URL cu search
- ⚡ Încărcare rapidă a paginilor

## Instalare

### Cerințe
- Python 3.7+
- PyQt5
- requests
- BeautifulSoup4

### Configurare

1. Clonează repository-ul:
```bash
git clone https://github.com/safmptp-debug/Web-On-Web.git
cd Web-On-Web
```

2. Instalează dependențele:
```bash
pip install -r requirements.txt
```

3. Rulează browserul:
```bash
python main.py
```

## Utilizare

### Navigare de bază
- **Butonul Back**: Du-te la pagina anterioară
- **Butonul Forward**: Du-te la pagina următoare
- **Butonul Refresh**: Reîncarcă pagina curentă
- **Butonul Home**: Revino la pagina de start
- **Bara URL**: Introdu o URL și apasă Enter pentru navigare

### Tab-uri
- Adaugă noi tab-uri pentru mai multe pagini
- Comută rapid între tab-uri

### Istoric
- Tracking automat al paginilor vizitate
- Caută prin istoric
- Vizualizează paginile cel mai des vizitate

## Structura Proiectului

```
Web-On-Web/
├── main.py                 # Punct de intrare
├── requirements.txt        # Dependențe Python
├── README.md              # Acest fișier
└── browser/
    ├── __init__.py        # Inițializarea pachetului
    ├── window.py          # Fereastra principală a browserului
    ├── renderer.py        # Motor de renderare HTML/CSS
    └── history.py         # Gestionare istoric de navigare
```

## Componente

### window.py
Implementare a ferestrei principale a browserului cu controale UI:
- Butoane de navigare
- Bara de adresă
- Gestionare tab-uri
- Bara de stare

### renderer.py
Motor de renderare a paginilor:
- Parsare și procesare HTML
- Extragere de linkuri
- Extragere de imagini
- Extragere de metadate
- Generare pagini de eroare

### history.py
Gestionare istoric de navigare:
- Tracking de intrări
- Navigare înainte/înapoi
- Căutare în istoric
- Pagini cel mai des vizitate

## Arhitectură

Browserul este construit pe o arhitectură modulară:

1. **UI Layer** (`window.py`): Gestionează interfața utilizatorului și interacțiuni
2. **Rendering Layer** (`renderer.py`): Procesează HTML și conținut pagini
3. **History Layer** (`history.py`): Gestionează istoricul de navigare

## Comenzi Rapid (Keyboard Shortcuts)

| Scurtătură | Acțiune |
|-----------|--------|
| Enter (în bara URL) | Navigare la URL |
| Alt + ← | Du-te înapoi |
| Alt + → | Du-te înainte |
| F5 | Reîncarcă pagina |
| Ctrl + H | Arată istoric |

## Performanță

- Ușor și eficient
- Încărcare rapidă a paginilor
- Utilizare optimizată a memoriei
- Interfață responsivă

## Siguranță

- Suport pentru header User-Agent
- Protecție timeout la conexiuni
- Gestionare erori pentru probleme de rețea
- Handling sigur de URL-uri

## Îmbunătățiri Viitoare

- [ ] Gestionare bookmark-uri
- [ ] Suport pentru cookie-uri
- [ ] Execuție JavaScript
- [ ] Manager de descărcări
- [ ] Mod privat
- [ ] Suport pentru extensii
- [ ] Temă modul întunecat
- [ ] Integrare cu motor de căutare

## Contribuții

Simt-te liber să faci fork la acest proiect și să trimiti pull requests cu îmbunătățiri!

## Licență

Acest proiect este open source și disponibil sub Licența MIT.

## Autor

Web On Web Development Team

---

**Făcut cu ❤️ în Python**
