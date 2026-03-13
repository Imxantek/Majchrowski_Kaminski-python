# Projekt: Start pracy zespołowej - Python + GitHub

## 👥 Zespół
**Grupa:** Majchrowski_Kaminski
**Skład zespołu:**
* Wojciech Majchrowski
* Antoni Kaminski

## ✈️ Cel projektu
Celem projektu jest przygotowanie środowiska pracy w Pythonie oraz praktyczne opanowanie podstaw współpracy zespołowej z wykorzystaniem systemu kontroli wersji Git i platformy GitHub. Projekt pozwala przećwiczyć pracę na branchach, tworzenie commitów, zgłaszanie Pull Requestów oraz przeprowadzanie code review.

## 🐾 Instrukcja uruchomienia

1. Sklonuj repozytorium na swój dysk lokalny:
    git clone <https://github.com/Imxantek/Majchrowski_Kaminski-python.git>

2. (Opcjonalnie) Utwórz i aktywuj wirtualne środowisko Pythona:
    python -m venv venv
    ### Aktywacja (Windows):
    venv\Scripts\activate
    ### Aktywacja (Mac/Linux):
    source venv/bin/activate

3. Zainstaluj wymagane pakiety (jeśli plik nie jest pusty):
    pip install -r requirements.txt

4. Uruchomienie programu (z poziomu głównego katalogu projektu wpisz w terminalu):
    python -m src.main

5. Uruchomienie testów (z poziomu głównego katalogu projektu wpisz w terminalu):
    python -m tests.tests

---

## 📝 Podsumowanie pracy zespołu

### 🛠️ Kto za co odpowiadał:
* **Wojciech Majchrowski:** Konfiguracja struktury testów, napisanie testów w pliku tests.py, stworzenie tego pięknego README
* **Antoni Kaminski:** Utworzenie szkieletu projektu w src/main.py, przygotowanie pierwszych funkcji bazowych. Przygotowanie repozytorium na Githubie

### ⚠️ Napotkane problemy:
* Pojawił się problem ze ścieżkami modułów (błąd ModuleNotFoundError dla pakietu src), gdy próbowaliśmy uruchamiać testy bezpośrednio z poziomu edytora. Problem rozwiązaliśmy, uruchamiając kod za pomocą terminala jako moduły (z użyciem flagi -m) z poziomu głównego katalogu projektu.

### 💡 Czego nauczyliśmy się podczas pracy:
* Jak poprawnie ułożyć strukturę katalogów (src/, tests/) w prostym projekcie w Pythonie.
* Jak bezpiecznie importować kod między folderami.
* Przećwiczyliśmy mechanikę GitHuba: tworzenie osobnych branchy, synchronizację zmian (fetch/pull) oraz proces zgłaszania uwag w Code Review przed scaleniem kodu (Merge PR).