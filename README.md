# Faculty of Health, Social Work and Psychology — NaUKMA website

Web programming lab 3. A Django website for a NaUKMA faculty that does not
have its own site: a home page, study programs, departments with teachers,
and an academic exchange section.

## Quick start

```bash
python -m pip install -r requirements-dev.txt
python manage.py migrate
python manage.py loaddata foz_content
python manage.py runserver
```

- `migrate` creates the tables and already adds the 6 exchange programs
  from the dean's office table;
- `loaddata foz_content` loads the faculty content: 4 departments,
  7 study programs, 36 teachers and the home page text.

| Page | URL |
| --- | --- |
| Home | `/` |
| Study programs | `/programs/`, `/programs/<id>/` |
| Departments | `/departments/`, `/departments/<id>/` |
| Academic exchange | `/exchange/` (with a country filter) |
| Admin | `/admin/` |

Answers to the questions from part 2 are in [ANSWERS.md](ANSWERS.md).

## Why this faculty

The Faculty of Health, Social Work and Psychology (FOZ) is the youngest
faculty of NaUKMA, founded in 2023. On the "Faculties" page of the main
university website, separate websites are listed only for the Faculty of
Informatics, the Faculty of Law and the kmbs Business School. FOZ has no
website of its own.

## Analysis of existing information about FOZ

Information about the faculty exists, but it is scattered and partly
contradictory:

1. **Two different faculty pages.** The new page on `web.ukma.edu.ua` names
   the dean and 4 structural units, but has no department heads and no
   program codes. The old page on `www.ukma.edu.ua` is still placed in the
   section of *another* faculty (Social Sciences), lists only 3 units and no
   dean, but does have department heads and the old program codes
   (053, 229, 231).
2. **Programs and codes live on a separate site.** Current codes from the
   new list of specialties (C4, I10, I9, D3), program descriptions and
   courses exist only in the NaUKMA ECTS catalogue, which is hard to reach
   from the faculty page.
3. **Teachers are listed in different places and formats.** The Department
   of Psychology and the School of Health Care Management show positions and
   degrees; the School of Social Work keeps its list on its own website; the
   School of Public Health shows only names.
4. **Contacts are hard to get.** Email addresses on the pages are hidden
   behind JavaScript, and admission coordinators are not listed anywhere.
5. **No information about academic exchange** for the faculty's students.

**What this website does:** it collects everything in one place with a
consistent structure. Every study program has a code, description, courses,
admission coordinator and contact; every department has a head, programs and
teachers; a separate section lists exchange programs with their admission
status.

**What is still missing and could be added next:** a page for applicants
(dates, requirements, tuition), faculty news, and a separate page for the
Medical

## Local setup

Requires the latest patch release of Python 3.12, 3.13, or 3.14. Run these commands from the project directory containing
`manage.py`.

1. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   
   # for linux/macos
   source .venv/bin/activate
   # for Windows:
   .venv\Scripts\activate
   ```

2. Install dependencies:

   ```bash
   python -m pip install -r requirements-dev.txt
   ```


3. Apply migrations to create the local SQLite database:

   ```bash
   python manage.py migrate
   ```

4. Start the development server:

   ```bash
   python manage.py runserver
   ```

## Endpoints

With the server running at `http://127.0.0.1:8000`:

| URL | Behavior |
| --- | --- |
| http://127.0.0.1:8000/ | No application homepage; may show Django's development welcome page while `DEBUG = True` |
| http://127.0.0.1:8000/admin/ | Django admin, available after applying migrations |

With `DEBUG = False`, unmatched URLs such as `/` return HTTP 404.

To create an account for admin login, run this after applying migrations:

```bash
python manage.py createsuperuser
```

## Add your first application

1. Create an app from the directory containing `manage.py` (replace `myapp`
   with your application name):

   ```bash
   python manage.py startapp myapp
   ```

2. Add its generated configuration class, `myapp.apps.MyappConfig`, to
   `INSTALLED_APPS` in `config/settings.py`.
3. Define your views and create `myapp/urls.py` with their URL patterns.
4. Register that URLconf in `config/urls.py` using `path()` and `include()`,
   choosing a URL prefix for the app and retaining the admin route.

See the official Django 6.1 tutorial for
[views and URL registration](https://docs.djangoproject.com/en/6.1/intro/tutorial01/)
and [app registration and models](https://docs.djangoproject.com/en/6.1/intro/tutorial02/).

## Git attributes

Git detects text files automatically and normalizes them to LF. Checkouts use
LF on Linux and Windows, while `.bat` and `.cmd` files use CRLF. Binary files
are auto-detected and left unchanged, helping avoid newline-only diffs.


## Code style and submission verification

All submissions are required to adhere to PEP-8, Django best practices, and standard HTML/CSS/JS formatting. A deterministic cross-platform utility is provided to help you check and format your code.

### 1. Verification (Check Mode)
Before submitting, verify that all files adhere to the required standards:

```bash
python check_submission.py
```

If all checks pass, you are ready to submit! If any checks fail, review the error output or run the auto-formatter below.

### 2. Auto-Formatting
To automatically format Python files, fix safe PEP-8 rules, format Django HTML templates, and format CSS/JS static files:

```bash
python check_submission.py --format
```

### 3. PyCharm Integration
If you use PyCharm:
- **One-Click Run:** In the top-right toolbar run configurations dropdown, select **"Verify Submission"** or **"Format Project"** and click the green **Play** button.

## Development only

The included settings use `DEBUG = True`, a development secret key, and a local
SQLite database. The default mailer uses the console backend: email is printed
to the process's console instead of being delivered.

This configuration and Django's development server are not suitable for
production deployment.
