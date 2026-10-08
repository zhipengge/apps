# GWAVE
> An application for play the radio stations from self-built audio stream.

## Features
- 9 system autio
    - caffe room
    - water flow
    - ocean wave
    - white noise
    - pink noise
    - clock tick
    - keyboard typing
    - rain
    - wind
- Custom audio stream support
    - import json/text file to add more audio streams
    - json
        ~~~json
        [
        {
            "name": "station name",
            "url": "http://your-audio-stream-url"
        },
        {
            "name": "another station",
            "url": "http://your-another-audio-stream-url"
        }
        ]
        ~~~
    - text
        - [样例请勿滥用](./public_radio.txt)
        ~~~plain-text
        station name,http://your-audio-stream-url
        another station,http://your-another-audio-stream-url
        ~~~
- Take definite shared-url for single audio stream
- Background play support
- More for you to explore...