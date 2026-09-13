.PHONY: verify paper assets clean

verify:
	python3 -B scripts/verify_repository.py

paper:
	bash scripts/build_paper.sh

assets:
	@test -n "$(ASSETS)" || (echo "usage: make assets ASSETS=/path/to/assets"; exit 2)
	python3 -B scripts/verify_assets.py --assets-dir "$(ASSETS)"

clean:
	@if [ -d build ]; then find build -mindepth 1 -delete; rmdir build; fi
