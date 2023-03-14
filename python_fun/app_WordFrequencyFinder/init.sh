echo "start Word Frequency Finder"
docker build -t word_frequency_finder .
docker run word_frequency_finder python ./Word_Frequency_Finder/app.py