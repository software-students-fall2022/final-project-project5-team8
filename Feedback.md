# Tutor session

## 1, Multiple language

There is no need for multiple input languages after finishing the chatGPT function since we got all the requirements. The tutor said that it's not necessary since multiple APIs for integrating languages is complicated and unnecessary work. 

## 2, Dockerfile

We need more dockerfiles for databases and other services separately. It is possible to put them into same folders and add multiple services in the docker compose file. 

## 3, Test code coverage

For test code coverage, we can use `--cov` to check the code coverage and how many lines that we are missing for the test. For example:

```bash
pytest web_app/tests/test_webapp.py --cov
```

A possible feedback for code coverage would be:

```bash
---------- coverage: platform win32, python 3.10.2-final-0 -----------
Name                           Stmts   Miss  Cover
--------------------------------------------------
web_app\controller.py             93     30    68%
web_app\database.py               24      4    83%
web_app\tests\__init__.py          0      0   100%
web_app\tests\test_webapp.py      65      3    95%
web_app\trans.py                   5      1    80%
--------------------------------------------------
TOTAL                            187     38    80%
```

## 4, Pull request related

While doing a merge for the pull request, use `squash and merge ` instead of `create a merge commit`.

Due to grading problems, it's for the best for them to review and make it more comprehensible.

