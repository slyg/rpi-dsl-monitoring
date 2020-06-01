.PHONY: sync
sync:
	rsync -a ./ pi@ariane.local:git/rpi-dsl-monitoring