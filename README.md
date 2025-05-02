> Note: I will eventually figure out how to host this API online for free

# Tutorial
Let's say the site is `http://rblx-api-dict.com` for example (because idk how to host online)

### Get Entire Dictionary
If you want to get the entire dictionary, you should use the `GET` method on `http://rblx-api-dict.com` or `http://rblx-api-dict.com/root`

### Get Classes
> Basically the entire dictionary

If you want to retrieve the classes section, you should use the `GET` method on `http://rblx-api-dict.com/classes`

### Get Information About a DataType
If you want to get information about a datatype (ex. BasePart), you should use the `GET` method on `http://rblx-api-dict.com/instance?target=DATATYPE_NAME`

### Get Properties of a DataType
If you want to get the properties of a datatype, you should use the `GET` method on `http://rblx-api-dict.com/properties?target=DATATYPE_NAME`
<br>
<hr>
<br>

# Example
For example, if I wanted to retrieve the properties of `AnimationTrack`, I would send an http request (`GET`) to `http://rblx-api-dict.com/properties?target=AnimationTrack`

In return, I would get this data (JSON Encoded) which details a list of all of the properties of the `AnimationTrack` class:

```json
{
  "Animation": {
    "Capabilities": [
      "Animation"
    ],
    "Name": "Animation",
    "ReadOnly": true,
    "Tags": [
      "ReadOnly",
      "NotReplicated"
    ],
    "ValueType": "Animation"
  },
  "IsPlaying": {
    "Capabilities": [
      "Animation"
    ],
    "Name": "IsPlaying",
    "ReadOnly": true,
    "Tags": [
      "ReadOnly",
      "NotReplicated"
    ],
    "ValueType": "bool"
  },
  "Length": {
    "Capabilities": [
      "Animation"
    ],
    "Name": "Length",
    "ReadOnly": true,
    "Tags": [
      "ReadOnly",
      "NotReplicated"
    ],
    "ValueType": "float"
  },
  "Looped": {
    "Capabilities": [
      "Animation"
    ],
    "Name": "Looped",
    "ReadOnly": true,
    "Tags": {

    },
    "ValueType": "bool"
  },
  "Priority": {
    "Capabilities": [
      "Animation"
    ],
    "Name": "Priority",
    "ReadOnly": true,
    "Tags": {

    },
    "ValueType": "AnimationPriority"
  },
  "Speed": {
    "Capabilities": [
      "Animation"
    ],
    "Name": "Speed",
    "ReadOnly": true,
    "Tags": [
      "ReadOnly",
      "NotReplicated"
    ],
    "ValueType": "float"
  },
  "TimePosition": {
    "Capabilities": [
      "Animation"
    ],
    "Name": "TimePosition",
    "ReadOnly": true,
    "Tags": [
      "NotReplicated"
    ],
    "ValueType": "float"
  },
  "WeightCurrent": {
    "Capabilities": [
      "Animation"
    ],
    "Name": "WeightCurrent",
    "ReadOnly": true,
    "Tags": [
      "ReadOnly",
      "NotReplicated"
    ],
    "ValueType": "float"
  },
  "WeightTarget": {
    "Capabilities": [
      "Animation"
    ],
    "Name": "WeightTarget",
    "ReadOnly": true,
    "Tags": [
      "ReadOnly",
      "NotReplicated"
    ],
    "ValueType": "float"
  }
}
```
