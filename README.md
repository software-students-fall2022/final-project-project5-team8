[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=9335331&assignment_repo_type=AssignmentRepo)

![Workflow Status](https://github.com/software-students-fall2022/containerized-app-exercise-team7/actions/workflows/webapp_test.yml/badge.svg?event=push)

![Workflow Status](https://github.com/software-students-fall2022/containerized-app-exercise-team7/actions/workflows/machine_learning_test.yml/badge.svg?event=push)

# Containerized App Exercise

Build a containerized app that uses machine learning. See [instructions](./instructions.md) for details.

[1, Local mongodb setup within Docker](#local-mongodb-database-set-up-within-docker)

[2, Root environment](#root-environment)

[3, Required dependencies](#required-dependencies)

[4, Usage Instructions](#usage-instructions)

[5, Supported Languages](#supported-languages)

[6, Contributors](#contributors)

## Local mongodb database set up within Docker

### 1. Docker Desktop

Make sure Docker Desktop is installed, if not check [here](https://www.docker.com/products/docker-desktop/).

### 2. Mongo image

Pull the mongo image by running the following command in terminal

```bash
docker pull mongo
```

### 3. Run container

Once installed, run the mongo container with the following command:

```bash
docker run -itd --name mongo -p 27017:27017 mongo --auth
```

### 4. Set up admin

We can either connect to to mongo by opening the terminal inside Docker Desktop or run the following command in terminal:

```bash
docker exec -it mongo mongo admin
```

**If using the terminal inside Docker Desktop, use mongosh to get connection:**

```bash
# mongosh
```

Then in order to set up an admin account:

```bash
# use admin
```

Create a user named admin with a password of 123456:

```bash
db.createUser({ user:'admin',pwd:'123456',roles:[ { role:'userAdminAnyDatabase', db: 'admin'},"readWriteAnyDatabase"]});
```

Try to connect using the user information created above.

```bash
db.auth('admin', '123456')
```

## Root environment

Create a `.env` file and can set them as environment variables.

Under root for the project, create `.env` file with content:

```env
FLASK_DEBUG = True

MONGO_URI = mongodb+srv://doadmin:1064QhnZay98pt73@db-mongodb-nyc1-48676-bf5b041d.mongo.ondigitalocean.com/admin?authSource=admin
MONGO_LANG_DBNAME = language
MONGO_TEXT_DBNAME = text
MONGO_USER = admin
MONGO_PASS = 123456

OPENAI_API_KEY = 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
```
## Running with Docker
1. Navigate to the root folder of this project, then run:
   ```
   docker compose up
   ```
# Deployed Apps
We have deployed both of our apps. You can try them using the links below:
<br>
[Web App](https://plankton-app-kozt5.ondigitalocean.app/hihillary-final-project-project/)

# Docker Images
We have pushed our custom subsystem images to DockerHub:
<br>
[Docker Hub Repo](https://hub.docker.com/r/hihillary/final-project-project5-team8-app/tags

## Required dependencies

```python
beautifulsoup4==4.11.1
certifi==2022.9.24
charset-normalizer==2.1.1
click==8.1.3
colorama==0.4.6
comtypes==1.1.14
deep-translator==1.9.1
dnspython==2.2.1
dominate==2.7.0
Flask==2.2.2
Flask-Bootstrap==3.3.7.1
idna==3.4
install==1.3.5
itsdangerous==2.1.2
Jinja2==3.1.2
MarkupSafe==2.1.1
PyAudio==0.2.12
pymongo==3.8.0
python-dotenv==0.21.0
pyttsx3==2.90
requests==2.28.1
soupsieve==2.3.2.post1
SpeechRecognition==3.8.1
urllib3==1.26.13
visitor==0.1.3
Werkzeug==2.2.2
gTTS==2.3.0
Flask-gTTS==0.18
pillow == 9.3.0
pytesseract == 0.3.10
```

## Usage Instructions

### <ins>AUDIO TRANSLATION</ins>

RECORD a voice message in English

- Pause button: Temporary stop recording

- Stop button: Stop recording

UPLOAD or SAVE the voice message

- Upload button: Upload the voice message to the database

- Save button: Save the voice message to the local machine

CHOOSE a language to translate the recording to

- Select a language from the dropdown menu

TRANSLATE the recording by clicking the translate button

### <ins>IMAGE-TO-TEXT TRANSLATION</ins>

UPLOAD an image file (png, jpg, webp) with English text to be translated

CHOOSE a language to translate the recording to

- Select a language from the dropdown menu

TRANSLATE the recording by clicking the translate button

## Supported Languages

### Input language

- English

### Output languages

- Bulgarian
- Czech
- Danish
- German
- Greek
- English
- Spanish
- Estonian
- Finnish
- French
- Hungarian
- Italian
- Japanese
- Korean
- Latvian
- Dutch
- Polish
- Portuguese
- Romanian
- Russian
- Slovak
- Swedish
- Tamil
- Filipino
- Ukrainian
- Vietnamese
- Ukrainian
- Chinese (Simplified)

## Contributors

[Darren Le](https://github.com/DarrenLe20)

[Daniel Atlas](https://github.com/Spectraorder)

[Paula Seraphim](https://github.com/paulasera)

[Leo Xu](https://github.com/leo6016)

[Hillary Davis](https://github.com/hillarydavis1)

[Michelle Lu]()

## Legacy Code Contributor

[Kedan Zha](https://github.com/Zackdan0227)
