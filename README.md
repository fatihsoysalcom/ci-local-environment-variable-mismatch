# CI Local Environment Variable Mismatch

This example demonstrates a common scenario where code works perfectly on a developer's local machine but fails in a Continuous Integration (CI) environment. The Python script attempts to read a critical configuration value (simulated as an API key) from an environment variable. If this variable is not set, the script simulates a CI build failure by exiting with an error code, illustrating the importance of consistent environment configuration between local and CI setups.

## Language

`python`

## How to Run

To run locally (success scenario):
export MY_SECRET_API_KEY="your_secret_key_123"
python main.py

To run simulating CI failure (variable not set):
python main.py

## Original Article

This example accompanies the Turkish article: [CI'da Kırılan, Kendi Makinenizde Çalışan Kod: Sebepler ve Çözümler Rehberi](https://fatihsoysal.com/blog/cida-kirilan-kendi-makinenizde-calisan-kod-sebepler-ve-cozumler-rehberi/).

## License

MIT — see [LICENSE](LICENSE).
