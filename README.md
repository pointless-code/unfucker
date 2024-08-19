![Unfucker](https://github.com/user-attachments/assets/4841dcb7-e5ce-4c17-9e7a-d997d121b662)

## About Unf*cker

UnF*cker scrubs your text clean of those unwanted F-bombs. Whether it's a file or a rant, just pass it through, and watch as the magic happens. No more "fuck"—just a polished, profanity-free masterpiece.

## Pull from docker

```bash
docker pull pointlesscode/unfucker:latest
docker run --rm -v $(pwd):/usr/src/app pointlesscode/unfucker --file your_text_file.txt

# or pass your text

docker run --rm pointlesscode/unfucker --text "Your text."
```

## Build it yourself
- clone the project and cd to folder
- build and run the image
```bash
docker build -t unfucker .
docker run --rm -v $(pwd):/usr/src/app unfucker --file your_text_file.txt

# or pass your text

docker run --rm unfucker --text "Your text."
```

## Social

<a href="https://pointlesscode.dev/">.less</a><br>
<a href="https://www.instagram.com/pointlesscode">Instagram</a><br>
<a href="https://x.com/pointlessCodes">Twitter</a><br>
<a href="https://github.com/pointless-code">GitHub</a><br>
<a href="https://hub.docker.com/u/pointlesscode">DockerHub</a>

## License

The project is open-sourced software licensed under the [MIT license](https://opensource.org/licenses/MIT).
