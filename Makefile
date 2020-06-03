.PHONY: sync
sync:
	rsync -a ./ pi@ariane.local:git/rpi-dsl-monitoring

install-service:
	sudo cp dsl_monitoring.service /etc/systemd/system/dsl_monitoring.service

start-service:
	sudo systemctl start dsl_monitoring.service

stop-service:
	sudo systemctl stop dsl_monitoring.service

set-onrestart:
	sudo systemctl enable dsl_monitoring.service

unset-onrestart:
	sudo systemctl disable dsl_monitoring.service
