# How To Use Kahoot API

### Each of these examples will have the same code simply change the url to the request type you want to do
```python
import requests
BASE = "URL/YOUR-UUID/REQUEST-TYPE"
response = requests.get(BASE)
```
## Get Full Data
`get-data`

## Get Question Details
`get-question-details`

## Get Questions
`get-questions`

## Get Question Names
`get-question-names`

## Get Quiz Length
`get-quiz-length`

## Get Question Details
`get-question-details/[QUESTION: int]`

## Get Answer
 `get-answer/[QUESTION: int]`