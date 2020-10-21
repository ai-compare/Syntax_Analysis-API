# Syntax_Analysis - AI-Compare API
## Description
This repositery provides code to implement [AI-Compare Syntax Analysis API](https://www.ai-compare.com/text_apis/syntax_analysis/). [AI-Compare Syntax Analysis API](https://www.ai-compare.com/text_apis/syntax_analysis/) allows to call Syntax Analysis APIs from Google Cloud Platform Natural Language, AWS Comprehend and IBM Watson Natural Language Understanding. It permits to get results from these providers and compare the results.

## What is AI-Compare ?
[AI-Compare](https://www.ai-compare.com/) is a SaaS providing APIs connected to big (AWS, GCP, etc.) and small AI providers: [object detection](https://www.ai-compare.com/vision_apis/object_detection), [OCR](https://www.ai-compare.com/vision_apis/ocr), [NLP](https://www.ai-compare.com/text_apis/sentiment_analysis/), [speech-to-text](https://www.ai-compare.com/audio_apis/speech_recognition), custom vision, etc. Our solution allows users to compare the performance of these providers APIs according to their data and use them directly via our API thus offering great flexibility and making it very easy to change supplier. In particular, we offer better performance with the "Genius" feature that cleverly combines results from multiple providers.

AI-Compare offers 2$ free credits when you [create your account for free](https://www.ai-compare.com/accounts/login/?next=/my_apis). You can then use [APIs](https://www.ai-compare.com/v1/redoc/), use the [interface](https://www.ai-compare.com/my_apis), manage your account and have access to all the APIs.

You can find APIs documentation here : https://www.ai-compare.com/v1/redoc/

## Usage
### Initialization
Enter your access token and select your API endpoint. You can get your token on your account manager [here](https://www.ai-compare.com/accounts/login/?next=/my_apis/my_account).
```python
import requests
headers = {  'Authorization': 'Bearer your API Key'}
url = 'https://www.ai-compare.com/v1/pretrained/text/syntax_analysis'
```
### Select parameters 
Set your text, the language, the attempted result, and providers APIs you want to run :
```python
payload = {'providers': '[\'ibm\', \'aws\', \'google_cloud\']','text':'I am angry today','language': 'en-US'}
```
### Get results
```python
response = requests.request("POST", url, headers=headers, data = payload)
print(response.text.encode('utf8'))
```

## Response example
<details>
<summary>

```json
[
  {
    "solution_name": "Google Cloud",
    "execution_time": "1.21301",
    "result": {
      "text": "Hello everybody",
      "keywords": [
        "Hello",
        "everybody"
      ],
      "importances": [
        "\nnull,\nnull"
      ],
      "tags": [
        "Noun",
        "Noun"
      ],
      "lemmas": [
        "Hello",
        "everybody"
      ],
      "others": [
        {
          "proper_name": "PROPER"
        },
        {
          "number": "SINGULAR",
          "proper_name": "NOT_PROPER"
        }
      ]
    },
    "api_response": {
      "sentences": [
        {
          "text": {
            "content": "Hello everybody",
            "beginOffset": 0
          }
        }
      ],
      "tokens": [
        {
          "text": {
            "content": "Hello",
            "beginOffset": 0
          },
          "partOfSpeech": {
            "tag": "NOUN",
            "aspect": "ASPECT_UNKNOWN",
            "case": "CASE_UNKNOWN",
            "form": "FORM_UNKNOWN",
            "gender": "GENDER_UNKNOWN",
            "mood": "MOOD_UNKNOWN",
            "number": "NUMBER_UNKNOWN",
            "person": "PERSON_UNKNOWN",
            "proper": "PROPER",
            "reciprocity": "RECIPROCITY_UNKNOWN",
            "tense": "TENSE_UNKNOWN",
            "voice": "VOICE_UNKNOWN"
          },
          "dependencyEdge": {
            "headTokenIndex": 0,
            "label": "ROOT"
          },
          "lemma": "Hello"
        },
        {
          "text": {
            "content": "everybody",
            "beginOffset": 6
          },
          "partOfSpeech": {
            "tag": "NOUN",
            "aspect": "ASPECT_UNKNOWN",
            "case": "CASE_UNKNOWN",
            "form": "FORM_UNKNOWN",
            "gender": "GENDER_UNKNOWN",
            "mood": "MOOD_UNKNOWN",
            "number": "SINGULAR",
            "person": "PERSON_UNKNOWN",
            "proper": "NOT_PROPER",
            "reciprocity": "RECIPROCITY_UNKNOWN",
            "tense": "TENSE_UNKNOWN",
            "voice": "VOICE_UNKNOWN"
          },
          "dependencyEdge": {
            "headTokenIndex": 0,
            "label": "NN"
          },
          "lemma": "everybody"
        }
      ],
      "language": "fr-FR"
    },
    "found_keywords": "Success"
  },
  {
    "solution_name": "Amazon Web Services",
    "execution_time": "0.465954",
    "result": {
      "text": "Hello everybody",
      "keywords": [
        "Hello",
        "everybody"
      ],
      "importances": [
        0.43402501940727234,
        0.8557144999504089
      ],
      "tags": [
        "Proper_noun",
        "Proper_noun"
      ],
      "lemmas": [
        "\nnull,\nnull"
      ],
      "others": [
        "\nnull,\nnull"
      ]
    },
    "api_response": {
      "SyntaxTokens": [
        {
          "TokenId": 1,
          "Text": "Hello",
          "BeginOffset": 0,
          "EndOffset": 5,
          "PartOfSpeech": {
            "Tag": "PROPN",
            "Score": 0.43402501940727234
          }
        },
        {
          "TokenId": 2,
          "Text": "everybody",
          "BeginOffset": 6,
          "EndOffset": 15,
          "PartOfSpeech": {
            "Tag": "PROPN",
            "Score": 0.8557144999504089
          }
        }
      ],
      "ResponseMetadata": {
        "RequestId": "a91c104e-d40c-4ea6-be32-a85ec495547f",
        "HTTPStatusCode": 200,
        "HTTPHeaders": {
          "x-amzn-requestid": "a91c104e-d40c-4ea6-be32-a85ec495547f",
          "content-type": "application/x-amz-json-1.1",
          "content-length": "258",
          "date": "Wed, 05 Aug 2020 09:00:40 GMT"
        },
        "RetryAttempts": 0
      }
    },
    "found_keywords": "Success"
  },
  {
    "solution_name": "Genius",
    "nb_Provider": 2,
    "found_keywords": "Success",
    "result": {
      "keywords": [
        "Hello",
        "everybody"
      ],
      "tags": [
        "Proper_noun",
        "Proper_noun"
      ],
      "lemmas": [
        "Hello",
        "everybody"
      ],
      "others": [
        {
          "proper_name": "PROPER"
        },
        {
          "number": "SINGULAR",
          "proper_name": "NOT_PROPER"
        }
      ]
    }
  }
]
```

</details>

## FAQ
Here you can access to AI-Compare [FAQ](https://www.ai-compare.com/faq/).

## Use cases
We provides on our website some [use cases examples for NLP APIs](https://www.ai-compare.com/use_cases_nlp/)

## Contact
If you have any question or request, you can contact us at contact@ai-compare.com

## Terms of use
You can access to our terms [here](https://www.ai-compare.com/terms/) on our website.

#
![Screenshot](Ai-compare_new.png)

