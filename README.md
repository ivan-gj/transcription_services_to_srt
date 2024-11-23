# Transcribing services' output to SRT

For some reason, many Whisper tools you see online don't automatically generate
SRT files, or sometimes not even based on any standard at all.

This project aims to fix this.


## Disclaimer

This is just a collection of tools I've created to make online Whisper tools actually
productive.
Also, as an excuse to test out [UV][uv].

Use at your own risk.

**Contributions are welcome.**


## Currently supported

- [`sanchit-gandhi`'s Whisper-JAX.](./src/sanchit_gandhi_whisper_jax/to_srt.py)
- [Yescribe.ai](./src/yescribe_ai/to_srt.py)


## How to use

Download this repo and execute your desired script. You'll need Python 3.10 at least.

For example,
```python
python src/yescribe_ai/to_srt.py yescribe_transcription.txt
```
will generate a `yescribe_transcription.srt` file.


## Developers

We are using [UV][uv] as the package manager,
as this whole project is actually me just playing around with it
and seeing if it's cool or not.

So far it is, very very cool, and most respecting of Python standards. I like it.
You should try it.


## Documentation

### [License](./LICENSE.md)

Licensed under the AGPL v3.


[uv]: https://docs.astral.sh/uv