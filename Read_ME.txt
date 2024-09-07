By zalogować się jako SuperUser.
Login:Damianek
Hasło:qwerty1234

Standard User1
Login: Grażyna
Haslo: Haslo123

Standard User2
Login: Janusz
Haslo: Haslo123

Strona z zadaniami.

Cel:
1. Celem strony jest zapewnienie użytkownikowi kontroli nad swoimi zadaniami.
2. Użytkownik może:
2.1. Tworzyć nowe zadania.
2.2. Edytować zadania.
2.3. Zamykać zadania.
2.4. Usuwać zadania.
3. Każdy zalogowany użytkownik może widzieć tylko swoje własne zadania.
3.1. Mamy 3 userów (admin + 2 userów)
3.2. Można tą opcje łatwo zmienić:
(W pliku todolist_app\views linia kodu 26, wystarczy zmienić zmienną all_tasks=Tasklist.objects.all())

Frontend:
4. Frontend zrobiony za pomocą danych ze strony Bootstrap (https://getbootstrap.com/docs/5.3/getting-started/introduction/)
4.1. Jak w przypadku tego typu stron, kod który zmienia wygląd można poprostu skopiować ze strony.
5. Crispy (crispy-forms, crispy-bootstrap5)
5.1. Wykorzystamy to do zmiany wyglądu strony z rejestracją użytkownika oraz opisy błędów przy rejestracji będą czytelniejsze.
5.2. W pliku settings dodamy to do apps oraz stworzmy 2 zmienne na dole.
5.3 Musimy też dodać to w pliku register.html w 2 miejscach.

SQL
5. Baza danych - PostgreSQL.
5.1. Program jest połączony z bazą Postgres.
5.2. Mam chyba licencję trial - 14 dni. (oby była dłuższa).

Administracja:
6. http://127.0.0.1:8000/admin/ - poziom admina

