connections:
	python3 Create_Connections.py

passwords:
	python3 main.py | tee wordlist.txt

filter:
	python3 Apply_Filters.py | tee wordlist_filtered.txt

clear_cache:
	rm -rf __pycache__

clear_profiles:
	rm -rf profiles/*

clear_wordlists:
	rm *.txt
