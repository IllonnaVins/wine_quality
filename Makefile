

download: clean
	@kaggle datasets download rajyellow46/wine-quality -f winequalityN.csv -p ./data/raw

all: download

clean:
	@del .\data\raw\winequalityN.csv >nul 2>&1

