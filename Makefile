.service_name = dsl_monitoring.service

.PHONY: sync
sync:
	rsync -a ./ pi@ariane.local:git/rpi-dsl-monitoring

.PHONY: install-service
install-service:
	sudo cp $(.service_name) /etc/systemd/system/$(.service_name)

.PHONY: start-service
start-service:
	sudo systemctl start $(.service_name)

.PHONY: stop-service
stop-service:
	sudo systemctl stop $(.service_name)

.PHONY: set-onrestart
set-onrestart:
	sudo systemctl enable $(.service_name)

.PHONY: unset-onrestart
unset-onrestart:
	sudo systemctl disable $(.service_name)
